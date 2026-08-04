##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##########################################################################

# use tdklib library, which provides a wrapper for tdk testcase script
import tdklib
from time import sleep

# Test components to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB")
obj1 = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change
# This will be replaced with corresponding DUT IP and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_CheckWiFiHealthFile')
obj1.configureTestCase(ip,port,'TS_ONEWIFI_CheckWiFiHealthFile')

# Get the result of connection with test components and DUT
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus1 = obj1.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"

    # Save device's current state before it goes for reboot
    obj.saveCurrentState()

    # Initiate Factory Reset before checking the default value
    tdkTestObj = obj.createTestStep('WIFIAgent_Set')
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.FactoryReset")
    tdkTestObj.addParameter("paramValue","Router,Wifi,VoIP,Dect,MoCA")
    tdkTestObj.addParameter("paramType","string")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("TEST STEP 1: Initiate factory reset")
        print("EXPECTED RESULT 1: Should initiate factory reset")
        print("ACTUAL RESULT 1: %s" %details)
        print("[TEST EXECUTION RESULT] : SUCCESS")

        # Restore the device state saved before reboot
        obj.restorePreviousStateAfterReboot()
        print("Wait till box comes up - 10 Min")
        sleep(600)

        # Set WiFi telemetry LogInterval after Factory Reset
        tdkTestObj = obj.createTestStep('WIFIAgent_Set')
        tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval")
        tdkTestObj.addParameter("paramValue","300")
        tdkTestObj.addParameter("paramType","int")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("TEST STEP 2: Set the WiFi telemetry LogInterval after factory reset")
            print("EXPECTED RESULT 2: Should set the WiFi telemetry LogInterval to 300 seconds")
            print("ACTUAL RESULT 2: %s" %details)
            print("[TEST EXECUTION RESULT] : SUCCESS")

            # Check whether the wifihealth.txt file is present
            tdkTestObj = obj1.createTestStep('ExecuteCmd')
            cmd = "[ -f /rdklogs/logs/wifihealth.txt ] && echo \"File exist\" || echo \"File does not exist\""
            tdkTestObj.addParameter("command",cmd)
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails().strip().replace("\\n","")

            if expectedresult in actualresult and details == "File exist":
                tdkTestObj.setResultStatus("SUCCESS")
                print("TEST STEP 3: Check for wifihealth log file presence")
                print("EXPECTED RESULT 3: wifihealth log file should be present")
                print("ACTUAL RESULT 3: wifihealth log file is present")
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("TEST STEP 3: Check for wifihealth log file presence")
                print("EXPECTED RESULT 3: wifihealth log file should be present")
                print("ACTUAL RESULT 3: wifihealth log file is not present")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("TEST STEP 2: Set the WiFi telemetry LogInterval after factory reset")
            print("EXPECTED RESULT 2: Should set the WiFi telemetry LogInterval to 300 seconds")
            print("ACTUAL RESULT 2: %s" %details)
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("TEST STEP 1: Initiate factory reset")
        print("EXPECTED RESULT 1: Should initiate factory reset")
        print("ACTUAL RESULT 1: %s" %details)
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("wifiagent")
    obj1.unloadModule("sysutil")
else:
    print("Failed to load wifiagent/sysutil module")
    obj.setLoadModuleStatus("FAILURE")
    obj1.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

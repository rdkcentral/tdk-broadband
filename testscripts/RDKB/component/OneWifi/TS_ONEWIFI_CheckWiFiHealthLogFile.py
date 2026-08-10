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
from tdkutility import *
from time import sleep

# Test components to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB")
obj1 = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change
# This will be replaced with corresponding DUT IP and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_ONEWIFI_CheckWiFiHealthLogFile')
obj1.configureTestCase(ip,port,'TS_ONEWIFI_CheckWiFiHealthLogFile')

# Get the result of connection with test components and DUT
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus1 = obj1.getLoadModuleResult()

print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus)
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus1)

if "SUCCESS" in loadmodulestatus.upper() and \
   "SUCCESS" in loadmodulestatus1.upper():

    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")

    expectedresult = "SUCCESS"
    proceed_flag = 1

    # Save device's current state before it goes for reboot
    obj.saveCurrentState()

    # Initiate Factory Reset before checking the default value
    tdkTestObj = obj.createTestStep('WIFIAgent_Set')
    tdkTestObj.addParameter(
        "paramName",
        "Device.X_CISCO_COM_DeviceControl.FactoryReset"
    )
    tdkTestObj.addParameter(
        "paramValue",
        "Router,Wifi,VoIP,Dect,MoCA"
    )
    tdkTestObj.addParameter(
        "paramType",
        "string"
    )

    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    print("TEST STEP 1: Initiate factory reset")
    print("EXPECTED RESULT 1: Should initiate factory reset")

    if expectedresult in actualresult:

        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT 1: %s" %details)
        print("[TEST EXECUTION RESULT] : SUCCESS")

        # Restore the device state saved before reboot
        obj.restorePreviousStateAfterReboot()

        # Wait for the WiFi namespace after Factory Reset
        found,tdkTestObj = wait_for_namespace(
            obj,
            6,
            30,
            "Device.WiFi.",
            expectedresult
        )

        if found == 1:

            # Set WiFi telemetry LogInterval after Factory Reset
            tdkTestObj = obj.createTestStep('WIFIAgent_Set')
            tdkTestObj.addParameter(
                "paramName",
                "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval"
            )
            tdkTestObj.addParameter(
                "paramValue",
                "300"
            )
            tdkTestObj.addParameter(
                "paramType",
                "int"
            )

            tdkTestObj.executeTestCase(expectedresult)

            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            print("TEST STEP 2: Set the WiFi telemetry LogInterval after factory reset")
            print("EXPECTED RESULT 2: Should set the WiFi telemetry LogInterval to 300 seconds")

            if expectedresult in actualresult:

                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT 2: %s" %details)
                print("[TEST EXECUTION RESULT] : SUCCESS")

                # Wait after setting LogInterval to allow wifihealth.txt generation
                print("Waiting for WiFi telemetry log generation")
                sleep(600)

                # Check whether the wifihealth.txt file is present
                tdkTestObj = obj1.createTestStep('ExecuteCmd')
                cmd = "[ -f /rdklogs/logs/wifihealth.txt ] && echo \"File exist\" || echo \"File does not exist\""
                tdkTestObj.addParameter(
                    "command",
                    cmd
                )

                tdkTestObj.executeTestCase(expectedresult)

                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails().strip().replace("\\n","")

                print("TEST STEP 3: Check for wifihealth log file presence")
                print("EXPECTED RESULT 3: wifihealth log file should be present")

                if expectedresult in actualresult and details == "File exist":

                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT 3: wifihealth log file is present")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                else:

                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT 3: wifihealth log file is not present")
                    print("[TEST EXECUTION RESULT] : FAILURE")

            else:

                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT 2: %s" %details)
                print("[TEST EXECUTION RESULT] : FAILURE")

        else:

            proceed_flag = 0
            tdkTestObj.setResultStatus("FAILURE")
            print("Device.WiFi. namespace is not available after Factory Reset")
            print("[TEST EXECUTION RESULT] : FAILURE")

    else:

        proceed_flag = 0
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT 1: %s" %details)
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("wifiagent")
    obj1.unloadModule("sysutil")

else:

    print("Failed to load wifiagent/sysutil module")
    obj.setLoadModuleStatus("FAILURE")
    obj1.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

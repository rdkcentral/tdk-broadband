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

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1")

# IP and Port of box, No need to change
# This will be replaced with corresponding Box IP and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_SetSNRMarker_ForAllVAP')

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus)

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    proceed_flag = 1
    revert_flag = 0
    step = 1
    paramName = "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.SNRList"

    # Get the initial telemetry SNR list
    tdkTestObj = obj.createTestStep('WIFIAgent_Get')
    tdkTestObj.addParameter("paramName",paramName)
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    print("TEST STEP %d: Get the current telemetry SNR list" %step)
    print("EXPECTED RESULT %d: Should get the current telemetry SNR list" %step)

    if expectedresult in actualresult and "VALUE:" in details:
        orgSNR = details.split("VALUE:")[1].split("TYPE:")[0].strip()
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Current telemetry SNR list is %s" %(step,orgSNR))
        print("[TEST EXECUTION RESULT] : SUCCESS")
    else:
        proceed_flag = 0
        orgSNR = ""
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get the current telemetry SNR list. Details: %s" %(step,details))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Get the number of available WiFi SSID entries
    if proceed_flag == 1:
        step += 1
        tdkTestObj = obj.createTestStep('WIFIAgent_Get')
        tdkTestObj.addParameter("paramName","Device.WiFi.SSIDNumberOfEntries")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Get the number of available WiFi SSID entries" %step)
        print("EXPECTED RESULT %d: Should get a valid number of WiFi SSID entries" %step)

        if expectedresult in actualresult and "VALUE:" in details:
            ssidCount = details.split("VALUE:")[1].split(" ")[0].strip()
            if ssidCount.isdigit() and int(ssidCount) > 0:
                ssidCount = int(ssidCount)
                setSNR = ",".join(str(index) for index in range(1,ssidCount + 1))
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Number of WiFi SSID entries is %d" %(step,ssidCount))
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                proceed_flag = 0
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Invalid SSIDNumberOfEntries value: %s" %(step,ssidCount))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            proceed_flag = 0
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get SSIDNumberOfEntries. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Set SNR list for all available VAPs
    if proceed_flag == 1:
        step += 1
        tdkTestObj = obj.createTestStep('WIFIAgent_Set')
        tdkTestObj.addParameter("paramName",paramName)
        tdkTestObj.addParameter("paramValue",setSNR)
        tdkTestObj.addParameter("paramType","string")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Enable SNR telemetry markers for all available virtual access points" %step)
        print("EXPECTED RESULT %d: Should set the SNR list to %s" %(step,setSNR))

        if expectedresult in actualresult:
            revert_flag = 1
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: SNR list was set successfully. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            proceed_flag = 0
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to set the SNR list. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Validate the SNR list after SET
    if proceed_flag == 1:
        step += 1
        tdkTestObj = obj.createTestStep('WIFIAgent_Get')
        tdkTestObj.addParameter("paramName",paramName)
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Get and validate the telemetry SNR list after SET" %step)
        print("EXPECTED RESULT %d: Telemetry SNR list should be %s" %(step,setSNR))

        if expectedresult in actualresult and "VALUE:" in details:
            newSNR = details.split("VALUE:")[1].split("TYPE:")[0].strip()
            if newSNR == setSNR:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Telemetry SNR list is %s" %(step,newSNR))
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Expected SNR list %s, but retrieved %s" %(step,setSNR,newSNR))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get the telemetry SNR list after SET. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Restore the initial telemetry SNR list
    if revert_flag == 1:
        step += 1
        tdkTestObj = obj.createTestStep('WIFIAgent_Set')
        tdkTestObj.addParameter("paramName",paramName)
        tdkTestObj.addParameter("paramValue",orgSNR)
        tdkTestObj.addParameter("paramType","string")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Restore the initial telemetry SNR list" %step)
        print("EXPECTED RESULT %d: Should restore the telemetry SNR list to its initial value" %step)

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Initial telemetry SNR list was restored successfully. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to restore the initial telemetry SNR list. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        print("Telemetry SNR list revert operation is not required")

    obj.unloadModule("wifiagent")
else:
    print("Failed to load wifiagent module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

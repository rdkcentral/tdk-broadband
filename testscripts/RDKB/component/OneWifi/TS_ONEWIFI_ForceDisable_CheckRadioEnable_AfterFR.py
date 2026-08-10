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

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1")

# IP and Port of box, No need to change
# This will be replaced with corresponding DUT IP and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_ForceDisable_CheckRadioEnable_AfterFR')

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus)

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    proceed_flag = 1
    step = 1

    # Enable WiFi Force Disable
    tdkTestObj = obj.createTestStep('WIFIAgent_Set')
    tdkTestObj.addParameter("paramName","Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable")
    tdkTestObj.addParameter("paramValue","true")
    tdkTestObj.addParameter("paramType","boolean")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    print("TEST STEP %d: Enable the WiFi Force Disable" %step)
    print("EXPECTED RESULT %d: Should enable the WiFi Force Disable state" %step)

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: %s" %(step,details))
        print("[TEST EXECUTION RESULT] : SUCCESS")
        sleep(60)
    else:
        proceed_flag = 0
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: %s" %(step,details))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Get RadioNumberOfEntries
    if proceed_flag == 1:
        step += 1
        tdkTestObj = obj.createTestStep('WIFIAgent_Get')
        tdkTestObj.addParameter("paramName","Device.WiFi.RadioNumberOfEntries")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Get the number of WiFi radio entries" %step)
        print("EXPECTED RESULT %d: Should get a valid number of WiFi radio entries" %step)

        if expectedresult in actualresult and "VALUE:" in details:
            radio_count_value = details.split("VALUE:")[1].split(" ")[0].strip()

            if radio_count_value.isdigit() and int(radio_count_value) > 0:
                radio_count = int(radio_count_value)
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Number of WiFi radio entries is %d" %(step,radio_count))
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                proceed_flag = 0
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Invalid RadioNumberOfEntries value. Details: %s" %(step,details))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            proceed_flag = 0
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get RadioNumberOfEntries. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Check if all applicable radios are disabled
    radio_names = {1:"2.4GHz",2:"5GHz",3:"6GHz"}

    for radio_index in range(1,radio_count + 1):
        if proceed_flag == 1:
            step += 1
            paramName = "Device.WiFi.Radio.%d.Enable" %radio_index
            radio_name = radio_names.get(radio_index,"Radio %d" %radio_index)
            tdkTestObj = obj.createTestStep('WIFIAgent_Get')
            tdkTestObj.addParameter("paramName",paramName)
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            print("TEST STEP %d: Get the Radio Enable status for %s as false" %(step,radio_name))
            print("EXPECTED RESULT %d: Should get the Radio Enable status for %s as false" %(step,radio_name))

            if expectedresult in actualresult and "VALUE:" in details:
                radio_state = details.split("VALUE:")[1].split(" ")[0].strip()

                if radio_state == "false":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Radio Enable status for %s is %s" %(step,radio_name,radio_state))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    proceed_flag = 0
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Radio Enable status for %s is %s" %(step,radio_name,radio_state))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                proceed_flag = 0
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to get the Radio Enable status for %s. Details: %s" %(step,radio_name,details))
                print("[TEST EXECUTION RESULT] : FAILURE")

    # Initiate Factory Reset
    if proceed_flag == 1:
        obj.saveCurrentState()
        step += 1
        tdkTestObj = obj.createTestStep('WIFIAgent_Set')
        tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.FactoryReset")
        tdkTestObj.addParameter("paramValue","Router,Wifi,VoIP,Dect,MoCA")
        tdkTestObj.addParameter("paramType","string")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Initiate factory reset" %step)
        print("EXPECTED RESULT %d: Should initiate factory reset" %step)

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : SUCCESS")
            obj.restorePreviousStateAfterReboot()

            # Wait for the WiFi namespace to come up up to 3 minutes
            found,tdkTestObj = wait_for_namespace(obj,6,30,"Device.WiFi.",expectedresult)

            if found != 1:
                proceed_flag = 0
                tdkTestObj.setResultStatus("FAILURE")
                print("Device.WiFi. namespace not available after Factory Reset")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            proceed_flag = 0
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Check if WiFi Force Disable is false after Factory Reset
    if proceed_flag == 1:
        step += 1
        tdkTestObj = obj.createTestStep('WIFIAgent_Get')
        tdkTestObj.addParameter("paramName","Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Check if WiFi Force Disable is false after Factory Reset" %step)
        print("EXPECTED RESULT %d: Should get WiFi Force Disable as false" %step)

        if expectedresult in actualresult and "VALUE:" in details:
            force_disable_state = details.split("VALUE:")[1].split(" ")[0].strip()

            if force_disable_state == "false":
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: WiFi Force Disable state is %s" %(step,force_disable_state))
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                proceed_flag = 0
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: WiFi Force Disable state is %s" %(step,force_disable_state))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            proceed_flag = 0
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get WiFi Force Disable state. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Check if all applicable radios are enabled after Factory Reset
    for radio_index in range(1,radio_count + 1):
        if proceed_flag == 1:
            step += 1
            paramName = "Device.WiFi.Radio.%d.Enable" %radio_index
            radio_name = radio_names.get(radio_index,"Radio %d" %radio_index)
            tdkTestObj = obj.createTestStep('WIFIAgent_Get')
            tdkTestObj.addParameter("paramName",paramName)
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            print("TEST STEP %d: Check if Radio Enable status for %s is true after Factory Reset" %(step,radio_name))
            print("EXPECTED RESULT %d: Radio Enable status for %s should be true after Factory Reset" %(step,radio_name))

            if expectedresult in actualresult and "VALUE:" in details:
                radio_state = details.split("VALUE:")[1].split(" ")[0].strip()

                if radio_state == "true":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Radio Enable status for %s is %s" %(step,radio_name,radio_state))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    proceed_flag = 0
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Radio Enable status for %s is %s" %(step,radio_name,radio_state))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                proceed_flag = 0
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to get the Radio Enable status for %s. Details: %s" %(step,radio_name,details))
                print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("wifiagent")
else:
    print("Failed to load wifiagent module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

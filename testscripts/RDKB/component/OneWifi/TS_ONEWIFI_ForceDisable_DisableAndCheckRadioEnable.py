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

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1")

# IP and Port of box, No need to change
# This will be replaced with corresponding DUT IP and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_ForceDisable_DisableAndCheckRadioEnable')

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus)

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1
    proceed_flag = 1
    revert_flag = 0
    initial_radio_states = {}

    # Get the number of WiFi radio entries
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
            print("ACTUAL RESULT %d: Invalid RadioNumberOfEntries value: %s" %(step,radio_count_value))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        proceed_flag = 0
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get RadioNumberOfEntries. Details: %s" %(step,details))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Get and store the initial Enable state of all radios
    if proceed_flag == 1:
        step += 1
        radio_get_status = 1
        print("TEST STEP %d: Get and store the initial Enable state of all WiFi radios" %step)
        print("EXPECTED RESULT %d: Should get the initial Enable state of all WiFi radios" %step)

        for radio_index in range(1,radio_count + 1):
            paramName = "Device.WiFi.Radio.%d.Enable" %radio_index
            tdkTestObj = obj.createTestStep('WIFIAgent_Get')
            tdkTestObj.addParameter("paramName",paramName)
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            if expectedresult in actualresult and "VALUE:" in details:
                radio_state = details.split("VALUE:")[1].split(" ")[0].strip()
                if radio_state in ["true","false"]:
                    initial_radio_states[radio_index] = radio_state
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("%s initial state is %s" %(paramName,radio_state))
                else:
                    radio_get_status = 0
                    tdkTestObj.setResultStatus("FAILURE")
                    print("Invalid Enable state for %s: %s" %(paramName,radio_state))
                    break
            else:
                radio_get_status = 0
                tdkTestObj.setResultStatus("FAILURE")
                print("Failed to get %s. Details: %s" %(paramName,details))
                break

        if radio_get_status == 1:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Initial Enable states of all WiFi radios were retrieved successfully" %step)
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            proceed_flag = 0
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to retrieve the initial Enable states of all WiFi radios" %step)
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Get the initial WiFi Force Disable state
    if proceed_flag == 1:
        step += 1
        force_disable_param = "Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable"
        tdkTestObj = obj.createTestStep('WIFIAgent_Get')
        tdkTestObj.addParameter("paramName",force_disable_param)
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Get the current WiFi Force Disable state" %step)
        print("EXPECTED RESULT %d: Should get the current WiFi Force Disable state" %step)

        if expectedresult in actualresult and "VALUE:" in details:
            initial_force_disable = details.split("VALUE:")[1].split(" ")[0].strip()
            if initial_force_disable in ["true","false"]:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Current WiFi Force Disable state is %s" %(step,initial_force_disable))
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                proceed_flag = 0
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Invalid WiFi Force Disable value: %s" %(step,initial_force_disable))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            proceed_flag = 0
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get WiFi Force Disable state. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Enable WiFi Force Disable
    if proceed_flag == 1:
        step += 1
        tdkTestObj = obj.createTestStep('WIFIAgent_Set')
        tdkTestObj.addParameter("paramName",force_disable_param)
        tdkTestObj.addParameter("paramValue","true")
        tdkTestObj.addParameter("paramType","boolean")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Enable WiFi Force Disable" %step)
        print("EXPECTED RESULT %d: Should enable WiFi Force Disable" %step)

        if expectedresult in actualresult:
            revert_flag = 1
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: WiFi Force Disable was enabled successfully. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : SUCCESS")
            sleep(60)
        else:
            proceed_flag = 0
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to enable WiFi Force Disable. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Verify that all radios are disabled
    if proceed_flag == 1:
        step += 1
        radio_disable_status = 1
        print("TEST STEP %d: Verify that all WiFi radios are disabled after enabling WiFi Force Disable" %step)
        print("EXPECTED RESULT %d: The Enable state of every WiFi radio should be false" %step)

        for radio_index in range(1,radio_count + 1):
            paramName = "Device.WiFi.Radio.%d.Enable" %radio_index
            tdkTestObj = obj.createTestStep('WIFIAgent_Get')
            tdkTestObj.addParameter("paramName",paramName)
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            if expectedresult in actualresult and "VALUE:" in details:
                radio_state = details.split("VALUE:")[1].split(" ")[0].strip()
                if radio_state == "false":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("%s is disabled" %paramName)
                else:
                    radio_disable_status = 0
                    tdkTestObj.setResultStatus("FAILURE")
                    print("%s is not disabled. Current state: %s" %(paramName,radio_state))
            else:
                radio_disable_status = 0
                tdkTestObj.setResultStatus("FAILURE")
                print("Failed to get %s. Details: %s" %(paramName,details))

        if radio_disable_status == 1:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: All WiFi radios are disabled" %step)
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: One or more WiFi radios are not disabled" %step)
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Revert WiFi Force Disable
    if revert_flag == 1:
        step += 1
        tdkTestObj = obj.createTestStep('WIFIAgent_Set')
        tdkTestObj.addParameter("paramName",force_disable_param)
        tdkTestObj.addParameter("paramValue",initial_force_disable)
        tdkTestObj.addParameter("paramType","boolean")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Revert WiFi Force Disable to its initial value" %step)
        print("EXPECTED RESULT %d: Should revert WiFi Force Disable to %s" %(step,initial_force_disable))

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: WiFi Force Disable was reverted successfully. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : SUCCESS")
            sleep(60)

            # Validate the WiFi Force Disable revert
            step += 1
            tdkTestObj = obj.createTestStep('WIFIAgent_Get')
            tdkTestObj.addParameter("paramName",force_disable_param)
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            print("TEST STEP %d: Validate the reverted WiFi Force Disable state" %step)
            print("EXPECTED RESULT %d: WiFi Force Disable should be restored to %s" %(step,initial_force_disable))

            if expectedresult in actualresult and "VALUE:" in details:
                current_force_disable = details.split("VALUE:")[1].split(" ")[0].strip()
                if current_force_disable == initial_force_disable:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: WiFi Force Disable was restored to %s" %(step,current_force_disable))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Expected %s, but current value is %s" %(step,initial_force_disable,current_force_disable))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to get the reverted WiFi Force Disable state. Details: %s" %(step,details))
                print("[TEST EXECUTION RESULT] : FAILURE")

            # Restore all radios to their initial Enable states
            step += 1
            radio_restore_status = 1
            print("TEST STEP %d: Restore all WiFi radios to their initial Enable states" %step)
            print("EXPECTED RESULT %d: Every WiFi radio should be restored to its initial Enable state" %step)

            for radio_index in range(1,radio_count + 1):
                paramName = "Device.WiFi.Radio.%d.Enable" %radio_index
                initial_state = initial_radio_states[radio_index]
                tdkTestObj = obj.createTestStep('WIFIAgent_Set')
                tdkTestObj.addParameter("paramName",paramName)
                tdkTestObj.addParameter("paramValue",initial_state)
                tdkTestObj.addParameter("paramType","boolean")
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails()

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("%s was restored to %s" %(paramName,initial_state))
                else:
                    radio_restore_status = 0
                    tdkTestObj.setResultStatus("FAILURE")
                    print("Failed to restore %s to %s. Details: %s" %(paramName,initial_state,details))

            if radio_restore_status == 1:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: All WiFi radios were restored successfully" %step)
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: One or more WiFi radios were not restored" %step)
                print("[TEST EXECUTION RESULT] : FAILURE")

            sleep(5)

            # Verify all radios returned to initial states
            step += 1
            radio_revert_status = 1
            print("TEST STEP %d: Verify that all WiFi radios returned to their initial Enable states" %step)
            print("EXPECTED RESULT %d: Every WiFi radio should match its initial Enable state" %step)

            for radio_index in range(1,radio_count + 1):
                paramName = "Device.WiFi.Radio.%d.Enable" %radio_index
                expected_radio_state = initial_radio_states[radio_index]
                tdkTestObj = obj.createTestStep('WIFIAgent_Get')
                tdkTestObj.addParameter("paramName",paramName)
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails()

                if expectedresult in actualresult and "VALUE:" in details:
                    current_radio_state = details.split("VALUE:")[1].split(" ")[0].strip()
                    if current_radio_state == expected_radio_state:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("%s was restored to %s" %(paramName,current_radio_state))
                    else:
                        radio_revert_status = 0
                        tdkTestObj.setResultStatus("FAILURE")
                        print("%s was not restored. Expected: %s, Actual: %s" %(paramName,expected_radio_state,current_radio_state))
                else:
                    radio_revert_status = 0
                    tdkTestObj.setResultStatus("FAILURE")
                    print("Failed to get %s. Details: %s" %(paramName,details))

            if radio_revert_status == 1:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: All WiFi radios returned to their initial Enable states" %step)
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: One or more WiFi radios did not return to their initial Enable states" %step)
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to revert WiFi Force Disable. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        print("WiFi Force Disable revert operation is not required")

    obj.unloadModule("wifiagent")
else:
    print("Failed to load wifiagent module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")


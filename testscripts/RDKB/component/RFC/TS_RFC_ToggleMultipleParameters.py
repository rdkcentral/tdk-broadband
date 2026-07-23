##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2025 RDK Management
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


import tdklib
from time import sleep
from RFCVariables import *
from RFCUtility import *
from tdkutility import *
import tdkbVariables

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181", "1")
sysobj = tdklib.TDKScriptingLibrary("sysutil", "1")

# IP and Port of box, No need to change, will be replaced with DUT details
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_RFC_ToggleMultipleParameters')
sysobj.configureTestCase(ip,port,'TS_RFC_ToggleMultipleParameters')

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus_sys.upper():
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    expectedresult = "SUCCESS"

    # Define multiple DM parameters to test - clean parameters without tr181 prefix
    dm_params = RFC_DM_PARAMS_MULTIPLE

    # Dictionary to store initial values
    initial_values = {}
    step = 1
    # Get MAC Address of the device
    print("\nTEST STEP %d: Get the MAC address of the device" % step)
    print("EXPECTED RESULT %d: The MAC address should be retrieved successfully" % step)
    tdkTestObj, actualresult, mac = get_mac(sysobj)
    if actualresult in expectedresult and mac != "":
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: The MAC address is retrieved successfully: %s" % (step, mac))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Get initial values for all DM parameters
        print("\nTEST STEP %d: Get initial values for all DM parameters: %s" % (step, ', '.join(dm_params)))
        print("EXPECTED RESULT %d: All initial DM values should be retrieved successfully" % step)
        initial_values_success = True
        for param in dm_params:
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
            actualresult, initial_value = getTR181Value(tdkTestObj, param)
            if actualresult in expectedresult and initial_value.strip() in ["true", "false"]:
                initial_value = initial_value.strip()
                initial_values[param] = initial_value
                print("Initial value for %s: %s" % (param, initial_value))
            else:
                initial_values_success = False
                print("Failed to retrieve initial value for %s" % param)
                break

        if initial_values_success:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: All initial DM values retrieved successfully" % step)
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Verify XConf server URL against rfc.properties
            print("\nTEST STEP %d: Verify XConf server URL against rfc.properties" % step)
            print("EXPECTED RESULT %d: URL should match the configured RFC_CONFIG_SERVER_URL" % step)
            command = "sh %s/tdk_utility.sh parseConfigFile RFC_PATH" % tdkbVariables.TDK_PATH
            tdkTestObj = sysobj.createTestStep('ExecuteCmd')
            actualresult, rfc_path = doSysutilExecuteCommand(tdkTestObj, command)
            rfc_path = rfc_path.strip()
            url_match = False
            if actualresult in expectedresult and rfc_path:
                # Check if RFC properties file exists
                tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                actualresult, file_exists = isFilePresent(tdkTestObj, rfc_path)
                if actualresult in expectedresult:
                    command = f"cat {rfc_path} | grep RFC_CONFIG_SERVER_URL= | cut -d'=' -f2"
                    tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                    actualresult, prop_url = doSysutilExecuteCommand(tdkTestObj, command)
                    prop_url = prop_url.strip()
                    if actualresult in expectedresult and prop_url == RFC_URL:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: URL matches. Configured: %s, Properties: %s" % (step, RFC_URL, prop_url))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                        url_match = True
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: URL mismatch or retrieval failed. Configured: %s, Properties: %s" % (step, RFC_URL, prop_url))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: RFC properties file does not exist at path: %s" % (step, rfc_path))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to retrieve RFC_PATH from tdk_platform.properties" % step)
                print("[TEST EXECUTION RESULT] : FAILURE")

            # Continue only if URL matches
            if url_match:
                step += 1
                # Configure RFC feature with multiple parameters - all clean parameters as dictionary
                print("\nTEST STEP %d: Configure RFC feature in XConf server with multiple parameters" % step)
                print("EXPECTED RESULT %d: Feature should be configured successfully with all parameters" % step)
                feature_id = Feature_name
                feature_name = Feature_name

                # Create parameter-value dictionary with toggled values - utility will add tr181 prefix
                param_value_dict = {}
                for param, initial_value in initial_values.items():
                    toggle_value = "true" if initial_value == "false" else "false"
                    param_value_dict[param] = toggle_value

                tdkTestObj, actualresult, details = rfc_configure_feature(sysobj, feature_id, feature_name, param_value_dict)
                feature_created = False
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Feature configured successfully with multiple parameters. Details: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                    feature_created = True

                    step += 1
                    # Set feature rule with estbMacAddress
                    print("\nTEST STEP %d: Set feature rule with estbMacAddress" % step)
                    print("EXPECTED RESULT %d: Feature rule should be set successfully" % step)
                    rule_id = feature_id  # Use feature_id as rule_id for consistency
                    tdkTestObj, actualresult, details = rfc_set_feature_rule(sysobj, rule_id, feature_name, mac)
                    rule_created = False
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Feature rule set successfully. Details: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                        rule_created = True
                        sleep(30)

                        step += 1
                        # Validate feature rule
                        print("\nTEST STEP %d: Validate feature rule using GET" % step)
                        print("EXPECTED RESULT %d: Feature rule should be validated" % step)
                        tdkTestObj, actualresult, details = rfc_validate_feature_rule(sysobj, mac, feature_name, param_value_dict)
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: Feature rule validated successfully. Details: %s" % (step, details))
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                            # Restart RFC after validation
                            step += 1
                            print("\nTEST STEP %d: Restart RFC service" % step)
                            print("EXPECTED RESULT %d: RFC service should restart successfully" % step)
                            tdkTestObj, actualresult, details = rfc_restart_service(sysobj)
                            if "active" in details:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: RFC service restarted successfully. Details: %s" % (step, details))
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                                sleep(5)

                                # Query all DM parameters to confirm toggle
                                step += 1
                                print("\nTEST STEP %d: Query all DM parameters to confirm toggle" % step)
                                print("EXPECTED RESULT %d: All DM parameters should be toggled from their initial values" % step)
                                all_toggled = True
                                for param, initial_value in initial_values.items():
                                    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                                    actualresult, updated_value = getTR181Value(tdkTestObj, param)
                                    updated_value = updated_value.strip()
                                    if actualresult in expectedresult and updated_value in ["true", "false"] and updated_value != initial_value:
                                        print("Parameter %s: Initial=%s, Updated=%s - TOGGLED" % (param, initial_value, updated_value))
                                    else:
                                        print("Parameter %s: Initial=%s, Updated=%s - NOT TOGGLED" % (param, initial_value, updated_value))
                                        all_toggled = False

                                if all_toggled:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print("ACTUAL RESULT %d: All DM parameters have been toggled successfully" % step)
                                    print("[TEST EXECUTION RESULT] : SUCCESS")

                                    # Revert DM values via RFC - using dictionary
                                    sleep(30)
                                    step += 1
                                    print("\nTEST STEP %d: Revert DM values to initial values via RFC update" % step)
                                    print("EXPECTED RESULT %d: All DM values should be reverted to initial values" % step)
                                    # Pass clean parameters with initial values as dictionary
                                    tdkTestObj, actualresult, details = rfc_revert_dm_value(sysobj, obj, feature_id, feature_name, initial_values)
                                    if expectedresult in actualresult:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: All DM values reverted successfully. Details: %s" % (step, details))
                                        print("[TEST EXECUTION RESULT] : SUCCESS")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: DM revert failed. Details: %s" % (step, details))
                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("ACTUAL RESULT %d: Not all DM parameters were toggled" % step)
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: RFC service restart failed. Details: %s" % (step, details))
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Feature rule validation failed. Details: %s" % (step, details))
                            print("[TEST EXECUTION RESULT] : FAILURE")

                        # Delete feature rule
                        if rule_created:
                            step += 1
                            print("\nTEST STEP %d: Delete feature rule from XConf server" % step)
                            print("EXPECTED RESULT %d: Feature rule should be deleted" % step)
                            tdkTestObj, actualresult, details = rfc_delete_feature_rule(sysobj, feature_id)
                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: Feature rule deleted successfully. Details: %s" % (step, details))
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: Failed to delete feature rule. Details: %s" % (step, details))
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            print("No need to delete feature rule as it was not created")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Feature rule set failed. Details: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : FAILURE")

                    # Delete feature
                    if feature_created:
                        step += 1
                        print("\nTEST STEP %d: Delete feature from XConf server" % step)
                        print("EXPECTED RESULT %d: Feature should be deleted" % step)
                        tdkTestObj, actualresult, details = rfc_delete_feature(sysobj, feature_id)
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: Feature deleted successfully. Details: %s" % (step, details))
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Failed to delete feature. Details: %s" % (step, details))
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        print("No need to delete feature as it was not created")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Feature configuration failed. Details: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to retrieve all initial DM values" % step)
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to retrieve the MAC address of the device. Details: %s" % (step, mac))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload the modules
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

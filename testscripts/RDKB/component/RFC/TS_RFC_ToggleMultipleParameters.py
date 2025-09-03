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
'''
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>44</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RFC_ToggleMultipleParameters</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RFC_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate that restarting the RFC service updates mutiple DMs with the new values configured in the corresponding RFC feature rule in XConf server.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks></remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>BPI</box_type>
    <!--  -->
    <box_type>Broadband</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_RFC_2</test_case_id>
    <test_objective>validate that restarting the RFC service updates mutiple DMs with the new values configured in the corresponding RFC feature rule in XConf server</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,BPI</test_setup>
    <pre_requisite>1. Ccsp Components should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2. TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters></input_parameters>
    <automation_approch>1. Load the modules
    2. Get initial DM values for multiple parameters
    3. Verify XConf server URL
    4. Configure RFC features with MAC for multiple parameters
    5. Set feature rule with MAC
    6. Validate feature rule with MAC
    7. Restart RFC service
    8. Validate RFC file creation
    9. Verify feature instance in RFC file
    10. Query updated DM parameters to confirm toggle
    11. Validate logs for DM updates
    12. Revert DM values to initial values
    13. Delete feature rule
    14. Delete feature
    15. Unload the modules</automation_approch>
    <expected_output>RFC Immediate Mode validation with multiple feature updates should be successful.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_RFC_ToggleMultipleParameters</test_script>
    <skipped>No</skipped>
    <release_version>M140</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''

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
    dm_params = [
        "Device.X_Comcast_com_ParentalControl.ManagedSites.Enable",
        "Device.X_Comcast_com_ParentalControl.ManagedServices.Enable",
        "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable"
    ]

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
        print("\nTEST STEP %d: Get initial values for all DM parameters" % step)
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
                    if actualresult in expectedresult and prop_url and prop_url == RFC_URL:
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
                        tdkTestObj, actualresult, details = rfc_validate_feature_rule(sysobj, mac)
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

                                # RFC file validation
                                step += 1
                                print("\nTEST STEP %d: Validate RFC file %s" % (step, RFC_FILE_PATH))
                                print("EXPECTED RESULT %d: RFC file should exist and contain feature instance %s" % (step, feature_name))
                                tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                                actualresult, file_details = isFilePresent(tdkTestObj, RFC_FILE_PATH)
                                if expectedresult in actualresult:
                                    command = f"cat {RFC_FILE_PATH} | grep '{feature_name}'"
                                    actualresult, parsed_details = doSysutilExecuteCommand(tdkTestObj, command)
                                    if "SUCCESS" in actualresult and feature_name in parsed_details:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: RFC file exists and contains feature instance %s. Details: %s" % (step, feature_name, parsed_details))
                                        print("[TEST EXECUTION RESULT] : SUCCESS")

                                        # Query all DM parameters to confirm toggle
                                        step += 1
                                        print("\nTEST STEP %d: Query all DM parameters to confirm toggle" % step)
                                        print("EXPECTED RESULT %d: All DM parameters should be toggled from their initial values" % step)
                                        all_toggled = True
                                        for param, initial_value in initial_values.items():
                                            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                                            actualresult, updated_value = getTR181Value(tdkTestObj, param)
                                            updated_value = updated_value.strip()
                                            if updated_value != initial_value:
                                                print("Parameter %s: Initial=%s, Updated=%s - TOGGLED" % (param, initial_value, updated_value))
                                            else:
                                                print("Parameter %s: Initial=%s, Updated=%s - NOT TOGGLED" % (param, initial_value, updated_value))
                                                all_toggled = False

                                        if all_toggled:
                                            tdkTestObj.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT %d: All DM parameters have been toggled successfully" % step)
                                            print("[TEST EXECUTION RESULT] : SUCCESS")

                                            # Validate logs for multiple DM updates
                                            step += 1
                                            print("\nTEST STEP %d: Validate logs for multiple DM updates" % step)
                                            print("EXPECTED RESULT %d: Logs should contain updates for all configured parameters" % step)
                                            log_found = True
                                            for param in initial_values.keys():
                                                command = f'cat {RFC_LOG_FILE} | grep "updated for {param}"'
                                                tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                                                actualresult, log_details = doSysutilExecuteCommand(tdkTestObj, command)
                                                if "SUCCESS" in actualresult and f"updated for {param}" in log_details:
                                                    print("Log found for %s: %s" % (param, log_details.strip()))
                                                else:
                                                    print("Log NOT found for %s" % param)
                                                    log_found = False

                                            if log_found:
                                                tdkTestObj.setResultStatus("SUCCESS")
                                                print("ACTUAL RESULT %d: Logs contain updates for all parameters" % step)
                                                print("[TEST EXECUTION RESULT] : SUCCESS")
                                            else:
                                                tdkTestObj.setResultStatus("FAILURE")
                                                print("ACTUAL RESULT %d: Some logs missing for parameter updates" % step)
                                                print("[TEST EXECUTION RESULT] : FAILURE")

                                            # Revert DM values via RFC - using dictionary
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
                                        print("ACTUAL RESULT %d: RFC file does not contain feature instance %s. Details: %s" % (step, feature_name, parsed_details))
                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("ACTUAL RESULT %d: RFC file does not exist. Details: %s" % (step, file_details))
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

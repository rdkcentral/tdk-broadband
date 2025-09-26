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
  <version>22</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RFC_ValidateNoUpdateWithSameValue</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RFC_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate that RFC service does not update the DM parameter when the configured value in XConf server matches the current DM value</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <box_type>RPI</box_type>
    <!--  -->
    <box_type>BPI</box_type>
    <!--  -->
    <box_type>Broadband</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_RFC_7</test_case_id>
    <test_objective>To validate that RFC service does not update the DM parameter when the configured value in XConf server matches the current DM value</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,BPI</test_setup>
    <pre_requisite>1. Ccsp Components should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. Xconf server should be up and running.</pre_requisite>
    <api_or_interface_used></api_or_interface_used>
    <input_parameters>Device.X_Comcast_com_ParentalControl.ManagedSites.Enable</input_parameters>
    <automation_approch>1. Load the modules
2. Get the MAC address of the device
3. Get the current DM value of ManagedSites.Enable parameter
4. Verify XConf server URL configuration
5. Clean up dcmrfc.log for fresh logging
6. Configure RFC feature with same value as current DM
7. Set feature rule with device MAC address
8. Restart RFC service
9. Validate feature rule
10. Query DM to confirm no change occurred
11. Validate logs for "new and old values are same" message
12. Clean up by deleting feature rule and feature
13. Unload the modules</automation_approch>
    <expected_output>RFC service should process the feature rule but not update the DM parameter since the new value matches the current value, and appropriate log messages should be generated.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_RFC_ValidateNoUpdateWithSameValue</test_script>
    <skipped>No</skipped>
    <release_version>M141</release_version>
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
obj.configureTestCase(ip,port,'TS_RFC_ValidateNoUpdateWithSameValue')
sysobj.configureTestCase(ip,port,'TS_RFC_ValidateNoUpdateWithSameValue')

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus_sys.upper():
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
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
        # Get the current enable status of RFC DM
        print("\nTEST STEP %d: Get the current enable status of Device.X_Comcast_com_ParentalControl.ManagedSites.Enable" % step)
        print("EXPECTED RESULT %d: The enable status should be retrieved successfully" % step)
        param = "Device.X_Comcast_com_ParentalControl.ManagedSites.Enable"
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
        actualresult, initial_value = getTR181Value(tdkTestObj, param)
        if actualresult in expectedresult and initial_value.strip() in ["true", "false"]:
            initial_value = initial_value.strip()
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Initial DM value retrieved: %s" % (step, initial_value))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Verify XConf server URL against rfc.properties using existing functionality
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
                # Delete the dcmrfc.log file to ensure clean logging
                print("\nTEST STEP %d: Delete the dcmrfc.log file to ensure clean logging" % step)
                print("EXPECTED RESULT %d: The dcmrfc.log file should be deleted successfully" % step)
                command = f"rm -f {RFC_LOG_FILE}"
                tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                actualresult, details = doSysutilExecuteCommand(tdkTestObj, command)
                if actualresult in expectedresult:
                    # Verify file is deleted using isFilePresent function
                    tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                    actualresult, file_details = isFilePresent(tdkTestObj, RFC_LOG_FILE)
                    # Check if the file details contain error messages indicating file doesn't exist
                    if "No such file" in file_details or "cannot access" in file_details or not file_details.strip():
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: dcmrfc.log file deleted successfully" % step)
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        # File still exists, check if it contains the filename (means file is present)
                        if RFC_LOG_FILE.split('/')[-1] in file_details:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: dcmrfc.log file still exists after deletion attempt. Output: %s" % (step, file_details))
                            print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: dcmrfc.log file deleted successfully" % step)
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to delete dcmrfc.log file. Details: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : FAILURE")

                step += 1
                # Configure RFC feature with same value as current DM - using dictionary for single parameter
                print("\nTEST STEP %d: Configure RFC feature in XConf server with same value as current DM" % step)
                print("EXPECTED RESULT %d: Feature should be configured successfully with same value: %s" % (step, initial_value))
                feature_id = Feature_name
                feature_name = Feature_name
                # Use the same value as initial_value (no toggle)
                # Pass clean parameter as dictionary - utility will add tr181 prefix
                param_value_dict = {param: initial_value}
                tdkTestObj, actualresult, details = rfc_configure_feature(sysobj, feature_id, feature_name, param_value_dict)
                feature_created = False
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Feature configured successfully with same value: %s. Details: %s" % (step, initial_value, details))
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

                            step += 1
                            # Restart RFC service after validation
                            print("\nTEST STEP %d: Restart RFC service" % step)
                            print("EXPECTED RESULT %d: RFC service should restart successfully" % step)
                            tdkTestObj, actualresult, details = rfc_restart_service(sysobj)
                            if "active" in details:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: RFC service restarted successfully. Details: %s" % (step, details))
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                # Wait for RFC cycle to complete
                                sleep(30)
                                step += 1
                                # Query DM to confirm no change
                                print("\nTEST STEP %d: Query DM to confirm no change from initial value" % step)
                                print("EXPECTED RESULT %d: DM value should remain same as initial value: %s" % (step, initial_value))
                                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                                actualresult, current_value = getTR181Value(tdkTestObj, param)
                                current_value = current_value.strip()
                                if actualresult in expectedresult and current_value == initial_value:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print("ACTUAL RESULT %d: DM value unchanged: %s (same as initial value)" % (step, current_value))
                                    print("[TEST EXECUTION RESULT] : SUCCESS")

                                    step += 1
                                    # Validate logs for processing without update
                                    print("\nTEST STEP %d: Validate logs for processing without update" % step)
                                    print("EXPECTED RESULT %d: Logs should contain 'new and old values are same value %s'" % (step, initial_value))
                                    command = f'cat {RFC_LOG_FILE} | grep "new and old values are same value {initial_value}"'
                                    tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                                    actualresult, log_details = doSysutilExecuteCommand(tdkTestObj, command)
                                    if "SUCCESS" in actualresult and f"new and old values are same value {initial_value}" in log_details:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: Logs confirm processing without update. Details: %s" % (step, log_details))
                                        print("[TEST EXECUTION RESULT] : SUCCESS")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: Logs do not contain expected same value message. Details: %s" % (step, log_details))
                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("ACTUAL RESULT %d: DM value changed unexpectedly. Expected: %s, Actual: %s" % (step, initial_value, current_value))
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
            print("ACTUAL RESULT %d: Failed to retrieve initial DM value" % step)
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


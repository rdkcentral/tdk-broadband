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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>4</version>
  <name>TS_WEBCONFIG_2G_WIFIValidationUsingPartialPrivateSSIDSubdoc</name>
  <primitive_test_id/>
  <primitive_test_name>Webconfig_DoNothing</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Validate WIFI via Webconfig Feature using partial privatessid subdoc for 2g</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
    <box_type>BPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WEBCONFIG_15</test_case_id>
    <test_objective>Validate WIFI via Webconfig Feature using partial privatessid subdoc for 2g</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband,RPI,BPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
    </pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get
TDKB_TR181Stub_Set
TDKB_TR181Stub_SetOnly
ExecuteCmd</api_or_interface_used>
    <input_parameters>Device.X_RDK_WebConfig.
Device.X_RDK_WebConfig.ForceSync
Device.WiFi.RadioNumberOfEntries
Device.WiFi.SSID.{i}.SSID
Device.WiFi.SSID.{i}.Enable
Device.WiFi.AccessPoint.{i}.SSIDAdvertisementEnabled
Device.WiFi.AccessPoint.{i}.Security.X_CISCO_COM_EncryptionMethod
Device.WiFi.AccessPoint.{i}.Security.ModeEnabled
Device.WiFi.AccessPoint.{i}.Security.X_COMCAST-COM_KeyPassphrase</input_parameters>
    <automation_approch>1. Load the modules
    2. Configure the webconfig settings if already not configured with webconfig server details.
    3  Get the WiFi parameters for 2.4GHz before updating the privatessid subdoc.
    4. Enter 2.4g partial privatessid subdoc informationin RDKM WebConfig Server via curl command.
    5. Set trigger parameter Device.X_RDK_WebConfig.ForceSync to root.
    6. Get the  WiFi parameters for 2.4GHz and validate whether it fails to get updated.
    7. Unload the modules.</automation_approch>
    <expected_output>WIFI validation via Webconfig Feature using 2g partial privatessid subdoc should be failure.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WEBCONFIG</test_stub_interface>
    <test_script>TS_WEBCONFIG_2G_WIFIValidationUsingPartialPrivateSSIDSubdoc</test_script>
    <skipped>No</skipped>
    <release_version>M140</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
from tdkutility import *
from WebconfigUtility import *
from WebconfigVariables import *

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WEBCONFIG_2G_WIFIValidationUsingPartialPrivateSSIDSubdoc')
sysobj.configureTestCase(ip,port,'TS_WEBCONFIG_2G_WIFIValidationUsingPartialPrivateSSIDSubdoc')
# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus_sys.upper():
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    expectedresult = "SUCCESS"

    step = 1
    #Get MAC Address of the device
    print("\nTEST STEP %d: Get the MAC address of the device" %step)
    print("EXPECTED RESULT %d: The MAC address should be retrieved successfully" %step)
    tdkTestObj, actualresult, mac = getMacAddress(sysobj)
    if actualresult in expectedresult and mac != "":
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: The MAC address is retrieved successfully: %s" %(step, mac))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        #Non-sensitive value for the trigger parameter
        value = "root"
        wifi_radio = "2g"

        #Configure the webconfig settings if not already done
        print("\nTEST STEP %d: Get the webconfig settings and configure it if not already done" %step)
        print("EXPECTED RESULT %d: The webconfig settings should be properly configured" %step)
        tdkTestObj, flag, initial_webconfig_settings = configureWebconfigSettings(obj, mac)
        if flag == 0:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Webconfig settings are configured properly" %step)
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            print("TEST STEP %d : Get the number of entries under Device.WiFi.Radio." %step)
            print("EXPECTED RESULT %d : Should get the number of entries successfully" %step)
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
            actualresult, details = getTR181Value(tdkTestObj, "Device.WiFi.RadioNumberOfEntries")
            radio_entries = int(details)
            if expectedresult in actualresult and radio_entries in [2, 3]:
                print("ACTUAL RESULT %d : Successfully get the number of entries. Details : %s" %(step, details))
                tdkTestObj.setResultStatus("SUCCESS")
                print("Number of entries under Device.WiFi.Radio : %s" %details)

                radios = ["2g", "5g"] if radio_entries == 2 else ["2g", "5g", "6g"]

                ssid_params = []
                wifi_values = []
                ssid_params_template = []
                initial_wifi_values = {}
                retrieval_flag = 0

                ssid_params_template = ["Device.WiFi.SSID.{AP}.SSID", "Device.WiFi.SSID.{AP}.Enable", "Device.WiFi.AccessPoint.{AP}.SSIDAdvertisementEnabled", "Device.WiFi.AccessPoint.{AP}.Security.X_CISCO_COM_EncryptionMethod", "Device.WiFi.AccessPoint.{AP}.Security.ModeEnabled", "Device.WiFi.AccessPoint.{AP}.Security.X_COMCAST-COM_KeyPassphrase"]

                for AP in range(1, radio_entries + 1):
                    step += 1
                    if AP == 3:
                        ssid_params = [param.format(AP=17) for param in ssid_params_template]
                    else:
                        ssid_params = [param.format(AP=AP) for param in ssid_params_template]


                    # Get the current values of WiFi parameters
                    print("\nTEST STEP %d: Get the current values of WiFi parameters for %s" %(step, radios[AP-1]))
                    print("EXPECTED RESULT %d: The current values of WiFi parameters should be retrieved successfully" %step)

                    tdkTestObj, result, wifi_values = getMultipleParams(obj, ssid_params)
                    wifi_values = {k: True if str(v).lower() == "true" else False if str(v).lower() == "false" else v for k, v in wifi_values.items()}

                    if "FAILURE" not in result:
                        initial_wifi_values[radios[AP-1]] = wifi_values

                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: The current values of %s WiFi parameters are retrieved successfully" %(step, radios[AP-1]))
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        if radios[AP-1] == wifi_radio:
                            wifi_params_getValue = wifi_values

                    else:
                        retrieval_flag = 1
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Failed to retrieve the current values of %s WiFi parameters" %(step, radios[AP-1]))
                        print("[TEST EXECUTION RESULT] : FAILURE")

                print("\nInitial Wifi Parameters and Values : %s" %initial_wifi_values)
                if retrieval_flag != 1:
                    step += 1
                    subdoc_name = "privatessid"
                    subdoc_type = "neg"
                    tr181_dm = "Device.WiFi.Private"
                    AP = 1

                    #Getting the subdoc info with partial values
                    info = getSubdocInfo(subdoc_name, subdoc_type, WIFI_RADIO=wifi_radio, radio_entries=radio_entries, initial_param_values=initial_wifi_values)

                    #Get partial privatessid subdoc info
                    subdoc_info = getPartialSubdocInfo(info)

                    set_values = extractValues(subdoc_info[f"private_ssid_{wifi_radio}"]) + extractValues(subdoc_info[f"private_security_{wifi_radio}"])

                    #Create and execute curl command to update the privatessid subdoc
                    print("\nTEST STEP %d: Execute the curl command to update %s subdoc for %s" %(step, subdoc_name, wifi_radio))
                    print("EXPECTED RESULT %d: The curl command should execute successfully" %step)

                    tdkTestObj, actualresult, details = CurlCommand(sysobj, subdoc_name, tr181_dm, subdoc_info, mac)

                    if expectedresult in actualresult and "Request successful" in details:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Curl command executed successfully. Details: %s" %(step, details))
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        step += 1
                        # Set the webconfig trigger to root. trigger_flag returns 1 if failed to set the trigger value.
                        trigger_flag = setWebconfigTrigger(obj, value, step)
                        sleep(10)
                        if trigger_flag != 1:
                            print("Successfully set the trigger value to %s" %value)

                            step += 1
                            ssid_params = [param.format(AP=AP) for param in ssid_params_template]
                            #Check whether the WiFi parameter values are updated
                            print("\nTEST STEP %d: Check whether the values of %s WiFi parameters fails to get updated as per partial privatessid subdoc" %(step, wifi_radio))
                            print("EXPECTED RESULT %d: Failure in updating the values of WiFi parameters " %step)

                            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                            tdkTestObj, result, final_wifi_values = getMultipleParams(obj, ssid_params)
                            final_values = [True if v.lower() == 'true' else False if v.lower() == 'false' else v for v in list(final_wifi_values.values())]

                            if "FAILURE" not in result and final_values != set_values:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: Failed to update the WiFi parameters as per partial privatessid subdoc" %step)
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: The values of WiFi parameters have been updated as per partial privatessid subdoc" %step)
                                print("[TEST EXECUTION RESULT] : FAILURE")
                                step += 1
                                # Revert the WiFi parameters to their initial values
                                print("\nTEST STEP %d: Execute curl command to revert the %s WiFi parameters to their initial values" %(step, wifi_radio))
                                print("EXPECTED RESULT %d: The WiFi parameters should be reverted successfully" %step)

                                #Get the revert subdoc info and execute the curl command to revert the privatessid subdoc
                                revert_subdoc_info = getSubdocInfo(subdoc_name, subdoc_type, radio_entries=radio_entries, initial_param_values=initial_wifi_values)
                                tdkTestObj, actualresult, details = CurlCommand(sysobj, subdoc_name, tr181_dm, revert_subdoc_info, mac)
                                if expectedresult in actualresult and "Request successful" in details:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print("ACTUAL RESULT %d : Curl command executed successfully to revert the privatessid subdoc. Details: %s" %(step,details))

                                    step += 1
                                    # Set the webconfig trigger to root
                                    trigger_flag = setWebconfigTrigger(obj, value, step)
                                    sleep(10)
                                    if trigger_flag != 1:
                                        #Validate the revert operation
                                        step += 1

                                        print("\nTEST STEP %d: Validate the revert operation by getting the WiFi parameters" %step)
                                        print("EXPECTED RESULT %d: The WiFi parameters should be reverted to their initial values successfully" %step)

                                        tdkTestObj, result, wifi_values = getMultipleParams(obj, ssid_params)
                                        wifi_values = {k: True if str(v).lower() == "true" else False if str(v).lower() == "false" else v for k, v in wifi_values.items()}

                                        if "FAILURE" not in result and wifi_values == wifi_params_getValue:
                                            tdkTestObj.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT %d: The WiFi parameters are reverted to their initial values successfully" %step)
                                            print("[TEST EXECUTION RESULT] : SUCCESS")
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT %d: Failed to revert the WiFi parameters to their initial values" %step)
                                            print("[TEST EXECUTION RESULT] : FAILURE")
                                    else:
                                        print("Failed to set the trigger value to %s" %value)
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("ACTUAL RESULT %d : Curl command execution failed to revert the privatessid subdoc. Details: %s" %(step, details))
                        else:
                            print("Failed to set the trigger value.")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Curl command execution failed. Details: %s" %(step, details))
                        print("[TEST EXECUTION RESULT] : FAILURE")

                else:
                    print("Failed to retrieve values of WiFi Parameters\n")
            step += 1
            #Revert the webconfig settings if they were changed
            print("\nTEST STEP %d: Revert the webconfig settings to initial values" %step)
            print("EXPECTED RESULT %d: The webconfig settings should be reverted successfully" %step)

            tdkTestObj, flag, revert_value = configureWebconfigSettings(obj, mac, initial_webconfig_settings)

            if flag == 0:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Webconfig settings reverted successfully" %step)
                print("[TEST EXECUTION RESULT] : SUCCESS\n")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to revert the webconfig settings" %step)
                print("[TEST EXECUTION RESULT] : FAILURE\n")

        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Webconfig settings are not configured properly" %step)
            print("[TEST EXECUTION RESULT] : FAILURE\n")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to retrieve the MAC address of the device" %step)
        print("[TEST EXECUTION RESULT] : FAILURE\n")

    #Unload the modules loaded
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")


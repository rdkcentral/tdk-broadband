##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <version>7</version>
  <name>TS_ONEWIFI_2.4GHzSetSupportedSecurityModes_WPA3PersonalTransitionEnabled</name>
  <primitive_test_id/>
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>When the WPA3 Personal Transition RFC, Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable is enabled, check if it possible to set Device.WiFi.AccessPoint.1.Security.ModeEnabled to all the supported security modes that are applicable.</synopsis>
  <groups_id/>
  <execution_time>3</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>BPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_ONEWIFI_176</test_case_id>
    <test_objective>When the WPA3 Personal Transition RFC, Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable is enabled, check if it possible to set Device.WiFi.AccessPoint.1.Security.ModeEnabled to all the supported security modes that are applicable.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable
paramName : Device.WiFi.AccessPoint.1.Security.ModeEnabled
paramValue : security mode
paramType : string
paramName : Device.WiFi.AccessPoint.1.Security.ModesSupported</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial security mode using Device.WiFi.AccessPoint.1.Security.ModeEnabled and store it.
3. Get the security configuration for the initial security mode and store it.
4. Check if the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable is enabled, else set it to true.
5. Get the supported modes using Device.WiFi.AccessPoint.1.Security.ModesSupported
6. Check if the SET operation of Device.WiFi.AccessPoint.1.Security.ModeEnabled is success for all supported modes that can be set for AP1. Ensure security configurations are set if required for mode transition.
7. Revert the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable status if required.
8. Revert the security mode enabled and security configuration values to initial values if required.
9. Unload the modules.</automation_approch>
    <expected_output>Should be able to set all the supported security modes that are applicable to Device.WiFi.AccessPoint.1.Security.ModeEnabled when the WPA3 RFC  Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable is enabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_ONEWIFI_2.4GHzSetSupportedSecurityModes_WPA3PersonalTransitionEnabled</test_script>
    <skipped>No</skipped>
    <release_version>M100</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *
from time import sleep;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_2.4GHzSetSupportedSecurityModes_WPA3PersonalTransitionEnabled');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";
    # Passphrases are test values only
    PASSPHRASEKEY = "effect8080chord"
    ENCRYPTION_MODE = "AES"
    index = 1
    get_config = 0

    #Get the initial security mode
    step = 1;
    tdkTestObj = obj.createTestStep("WIFIAgent_Get");
    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.ModeEnabled");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print("\nTEST STEP %d : Get the Security Mode using Device.WiFi.AccessPoint.1.Security.ModeEnabled" %step);
    print("EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.1.Security.ModeEnabled" %step);
    if expectedresult in actualresult:
        initial_mode = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
        tdkTestObj.setResultStatus("SUCCESS");
        print("ACTUAL RESULT %d: Get operation success; Details : %s" %(step, initial_mode));
        print("TEST EXECUTION RESULT :SUCCESS");

        #Get Security config values for the Mode : RADIUS config if initial mode is Enterprise and Security Passphrase if initial mode is Personal
        if initial_mode != "None":
            step = step + 1
            print("\nTEST STEP %d : Get the Security config values for %s" %(step, initial_mode));
            print("EXPECTED RESULT %d : Should get the config values" %step)
            tdkTestObj, actual_result, initial_security_config = getSecurityModeEnabledConfig(obj, initial_mode , index);
            if expectedresult in actual_result:
                tdkTestObj.setResultStatus("SUCCESS");
                print("ACTUAL RESULT %d : The values obtained are : %s" %(step,initial_security_config));
                print("TEST EXECUTION RESULT : SUCCESS\n");
            else:
                get_config = 1
                tdkTestObj.setResultStatus("FAILURE");
                print("ACTUAL RESULT %d : The values obtained are : %s" %(step,initial_security_config));
                print("TEST EXECUTION RESULT : FAILURE\n");
        else:
            initial_security_config = {}
        if get_config == 0:
            #Check the Pre-requisites - WPA3_Personal_Transition RFC should be enabled
            step = step + 1;
            pre_req_set, tdkTestObj, step, revert_flag, initial_value = CheckWPA3Pre_requiste(obj, step);

            if revert_flag == 0:
                print("WPA3 RFC was already in enabled  state.");
                last_mode_set = initial_mode
            else:
                print("Enabled WPA3 RFC from disabled state.")
                step = step + 1
                print("\nTEST STEP %d : Get the Security Mode and check whether it is WPA3-Personal-Transition" %step);
                print("EXPECTED RESULT %d : Should successfully get the security mode as WPA3-Personal-Transition " %step);
                step = step + 1
                tdkTestObj, actualresult, last_mode_set = wifi_GetParam(obj, "Device.WiFi.AccessPoint.1.Security.ModeEnabled")
                if expectedresult in actualresult and last_mode_set == "WPA3-Personal-Transition":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("ACTUAL RESULT %d: Get operation success; The current security Mode is : %s" %(step,last_mode_set));
                    print("TEST EXECUTION RESULT :SUCCESS");
                else:
                    last_mode_set = ""
                    tdkTestObj.setResultStatus("FAILURE");
                    print("ACTUAL RESULT %d : Security mode has not changed to expected value. The current security mode is : %s" %(step,last_mode_set));
                    print("TEST EXECUTION RESULT : FAILURE\n");

            if pre_req_set == 1 and last_mode_set != "":
                print("\n*************RFC Pre-requisite set for the DUT*****************");
                #Get the supported Security Modes
                step =  step + 1;
                tdkTestObj = obj.createTestStep("WIFIAgent_Get");
                tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.ModesSupported");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                print("\nTEST STEP %d : Get the supported modes supported using Device.WiFi.AccessPoint.1.Security.ModesSupported" %step);
                print("EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.1.Security.ModesSupported" %step);
                if expectedresult in actualresult:
                    supported_modes = details.split("VALUE:")[1].split(' ')[0].split(',');
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("ACTUAL RESULT %d: Get operation success; Details : %s" %(step,details));
                    print("TEST EXECUTION RESULT :SUCCESS");

                    valid_modes = [mode for mode in supported_modes if ("Personal" in mode and "Compatibility" not in mode)or mode == "None"]
                    print("Supported Modes to be set : ", valid_modes)

                    #Set all supported modes to the 2.4G private access point except the Enterprise modes when the WPA3 RFC is in enabled state
                    for mode in valid_modes:
                        print("\n****************For Mode %s*******************" %mode);
                        step = step + 1

                        config_needed = 0
                        # If current mode and previous mode are same, skip set operation.
                        # If previous mode is not Personal, set security configuration for mode transition.
                        if mode == last_mode_set:
                            print("The mode to be set is same as the current mode : %s" %mode)
                            continue
                        elif "Personal" not in last_mode_set:
                            config_needed = 1

                        if config_needed == 1:
                            #Set Security Key/SAE Passphrase and Encryption Method if initial mode is not personal
                            step = step + 1;
                            if "WPA3" not in mode:
                                passphrase_key = f"Device.WiFi.AccessPoint.{index}.Security.KeyPassphrase"
                            else:
                                passphrase_key = f"Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase"

                            encryption_key = f"Device.WiFi.AccessPoint.{index}.Security.X_CISCO_COM_EncryptionMethod"
                            # Passphrases are test values only
                            new_passphrase_config = {
                                passphrase_key: PASSPHRASEKEY,
                                encryption_key: ENCRYPTION_MODE
                            }

                            print("Mode to be set is %s \n New KeyPassphrase and Encryption method to be set : %s" %(mode, new_passphrase_config));
                            print("TEST STEP %d : Set the mode, the initial KeyPassphrase and the Encryption method to new values" %step);
                            print("EXPECTED RESULT %d : Should set the mode, the initial KeyPassphrase and the Encryption method to new values" %step);

                            tdkTestObj, actualresult = setSecurityModeEnabledConfig(obj, mode, index, new_passphrase_config, last_mode_set);
                            print("Result : %s" %actualresult);
                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print("ACTUAL RESULT %d : Set Operation is Success" %step);
                                print("TEST EXECUTION RESULT : SUCCESS\n");

                                sleep(2)
                                step = step + 1;
                                print("TEST STEP %d : Validate KeyPassphrase and Encryption method" %step);
                                print("EXPECTED RESULT %d : Set value should be reflected in get" %step);
                                tdkTestObj, result, set_passphrase_config = getSecurityModeEnabledConfig(obj, mode, index);
                                if expectedresult in result and set_passphrase_config == new_passphrase_config:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print("ACTUAL RESULT %d : The values set are : %s\n" %(step,set_passphrase_config));
                                    print("TEST EXECUTION RESULT : SUCCESS\n");
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print("ACTUAL RESULT %d: Set not getting reflected in get. Setting config values failed" %step);
                                    print("TEST EXECUTION RESULT :FAILURE\n");
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print("ACTUAL RESULT %d : Set Operation failed" %step);
                                print("TEST EXECUTION RESULT : FAILURE\n");
                        else:
                            #Set the security mode
                            step = step + 1;
                            tdkTestObj = obj.createTestStep("WIFIAgent_Set");
                            tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.ModeEnabled");
                            tdkTestObj.addParameter("paramValue",mode);
                            tdkTestObj.addParameter("paramType","string");
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();
                            print("\nTEST STEP %d : Set Device.WiFi.AccessPoint.1.Security.ModeEnabled to %s" %(step, mode));
                            print("EXPECTED RESULT %d : Should successfully set Device.WiFi.AccessPoint.1.Security.ModeEnabled to %s" %(step,mode));
                            if expectedresult in actualresult :
                                tdkTestObj.setResultStatus("SUCCESS");
                                print("ACTUAL RESULT %d: Set operation success; Details : %s" %(step,details));
                                print("TEST EXECUTION RESULT :SUCCESS");
                            else :
                                tdkTestObj.setResultStatus("FAILURE");
                                print("ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,details));
                                print("TEST EXECUTION RESULT :FAILURE");

                        sleep(2)
                        #Verify the SET with GET
                        step = step + 1;
                        tdkTestObj = obj.createTestStep("WIFIAgent_Get");
                        tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.ModeEnabled");
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        print("\nTEST STEP %d : Get the Security Mode using Device.WiFi.AccessPoint.1.Security.ModeEnabled and check if SET operation was success" %step);
                        print("EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.1.Security.ModeEnabled and should reflect the SET Mode" %step);
                        if expectedresult in actualresult:
                            final_mode = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                            tdkTestObj.setResultStatus("SUCCESS");
                            print("ACTUAL RESULT %d: Get operation success; Details : %s" %(step, final_mode));
                            print("TEST EXECUTION RESULT :SUCCESS");
                            print("Set Mode : ", mode);
                            print("Get Mode : ", final_mode);
                            if final_mode == mode:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print("SET is reflected in GET");
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print("SET is NOT reflected in GET");
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step, details));
                            print("TEST EXECUTION RESULT : FAILURE");
                        last_mode_set = mode
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step, details));
                    print("TEST EXECUTION RESULT : FAILURE");

                #Revert the pre-requisites set
                if revert_flag == 1:
                    step = step + 1;
                    status = RevertWPA3Pre_requisite(obj, initial_value);
                    print("\nTEST STEP %d : Revert the RFC pre-requisite to initial value" %step);
                    print("EXPECTED RESULT %d : Pre-requisites set should be reverted successfully" %step);
                    if status == 1:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print("ACTUAL RESULT %d : Revert operation was success" %step);
                        print("[TEST EXECUTION RESULT] : SUCCESS");
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print("ACTUAL RESULT %d : Revert operation failed" %step);
                        print("[TEST EXECUTION RESULT] : FAILURE");
                else:
                    print("Reverting RFC pre-requisites not required");
                #Revert the security mode and config values if required
                if (revert_flag == 0 and initial_mode != final_mode) or (revert_flag == 1 and initial_mode != "WPA2-Personal"):
                    print("Reverting to initial Security Mode...")
                    step = step + 1;

                    tdkTestObj,actualresult = setSecurityModeEnabledConfig(obj, initial_mode, index, initial_security_config, final_mode)
                    sleep(2)

                    print("\nTEST STEP %d : Revert Device.WiFi.AccessPoint.1.Security.ModeEnabled to initial mode : %s" %(step, initial_mode));
                    print("EXPECTED RESULT %d : Reverting to initial security mode should be success" %step);

                    if expectedresult in actualresult :
                        tdkTestObj.setResultStatus("SUCCESS");
                        print("ACTUAL RESULT %d : Reverting Mode to initial value was successful" %step);
                        print("TEST EXECUTION RESULT : SUCCESS");
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print("ACTUAL RESULT %d : Reverting Mode to initial value was NOT successful" %step);
                        print("TEST EXECUTION RESULT : FAILURE");

                elif (revert_flag == 1 and initial_mode == "WPA2-Personal"):
                    step = step + 1
                    tdkTestObj, actualresult, final_mode = wifi_GetParam(obj, "Device.WiFi.AccessPoint.1.Security.ModeEnabled")

                    print("\nTEST STEP %d : Check if Device.WiFi.AccessPoint.1.Security.ModeEnabled fell back to WPA2-Personal" %step);
                    print("EXPECTED RESULT %d : Device.WiFi.AccessPoint.1.Security.ModeEnabled should fall back to WPA2-Personal after disabling WPA3 Transition enable RFC" %step);

                    if expectedresult in actualresult and final_mode == "WPA2-Personal":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print("ACTUAL RESULT %d : Security mode fell back to WPA2-Personal; Details : %s" %(step, final_mode));
                        print("TEST EXECUTION RESULT : SUCCESS");
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print("ACTUAL RESULT %d : Security mode did not fall back to WPA2-Personal; Details : %s" %(step, final_mode));
                        print("TEST EXECUTION RESULT : FAILURE");
                else:
                    print("\nReverting Security Mode not required...")
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print("Pre-Requisite and security mode is not set successfully");
        else:
            print("Failed to get config values\n")
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step, initial_mode));
        print("TEST EXECUTION RESULT :FAILURE");
    obj.unloadModule("wifiagent");
else:
    print("Failed to load the module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");

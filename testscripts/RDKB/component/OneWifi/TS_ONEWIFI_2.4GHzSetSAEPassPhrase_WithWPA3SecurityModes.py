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
  <version>4</version>
  <name>TS_ONEWIFI_2.4GHzSetSAEPassPhrase_WithWPA3SecurityModes</name>
  <primitive_test_id/>
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if setting Device.WiFi.AccessPoint.1.Security.SAEPassphrase to valid Passphrase is success when the Access Point Security Mode Enabled Device.WiFi.AccessPoint.1.Security.ModeEnabled is set to WPA3-Personal and WPA3-Personal-Transition after enabling Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable</synopsis>
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
    <test_case_id>TC_ONEWIFI_178</test_case_id>
    <test_objective>Check if setting Device.WiFi.AccessPoint.1.Security.SAEPassphrase to valid Passphrase is success when the Access Point Security Mode Enabled Device.WiFi.AccessPoint.1.Security.ModeEnabled is set to WPA3-Personal and WPA3-Personal-Transition after enabling Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable
paramName : Device.WiFi.AccessPoint.1.Security.ModeEnabled
paramValue : security mode
paramType : string
paramName : Device.WiFi.AccessPoint.1.Security.SAEPassphrase
paramValue : Passphrase generated dynamically
paramType : string</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial security mode using Device.WiFi.AccessPoint.2.Security.ModeEnabled and store it.
3. Get the security configuration for the initial security mode and store it.
4. Check if the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable is enabled, else set it to true and validate with get.
5. Set the required security configurations if the current security mode is not Personal.
6. Set the Device.WiFi.AccessPoint.1.Security.ModeEnabled to WPA3-Personal-Transition and validate with get.
7. Check if the SET operation of Device.WiFi.AccessPoint.1.Security.SAEPassphrase to a valid new value returns success and validate with get.
8. Set the Device.WiFi.AccessPoint.1.Security.ModeEnabled to WPA3-Personal and validate with get.
9. Check if the SET operation of Device.WiFi.AccessPoint.1.Security.SAEPassphrase to a valid new value returns success and validate with get.
10. Revert the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable status if required.
11. Revert the security mode enabled and the security configuration values to initial value if required.
12. Unload the modules.</automation_approch>
    <expected_output>Setting Device.WiFi.AccessPoint.1.Security.SAEPassphrase should be successful in WPA3-Personal and WPA3-Personal-Transition modes when the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable is enabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_ONEWIFI_2.4GHzSetSAEPassPhrase_WithWPA3SecurityModes</test_script>
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
from random import randint;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_2.4GHzSetSAEPassPhrase_WithWPA3SecurityModes');

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
            if pre_req_set == 1:
                print("\n*************RFC Pre-requisite set for the DUT*****************");
                #Set SAEPassphrase for each of the WPA3 modes
                wpa3_modes = ["WPA3-Personal-Transition", "WPA3-Personal"]
                for mode in wpa3_modes:
                    print("\n****************For Mode %s*******************" %mode);
                    #Verify if WPA3-RFC was disabled and then enabled, the security mode transition to WPA3-Personal Transition
                    if mode == wpa3_modes[0] and revert_flag == 1:
                        print("RFC was disabled initially and then enabled, should auto set %s mode" %mode)
                    #Set Security Key/SAE Passphrase and Encryption Method if initial mode is not personal
                    elif mode == wpa3_modes[0] and revert_flag == 0 and "Personal" not in initial_mode:
                        print("WPA3 RFC was already in enabled  state.");
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

                        print("Security Mode to be set : %s \n New KeyPassphrase and Encryption method to be set : %s" %(mode, new_passphrase_config));

                        print("TEST STEP %d : Set the Security Mode, initial KeyPassphrase and Encryption method to new values" %step);
                        print("EXPECTED RESULT %d : Should set the Security Mode, initial KeyPassphrase and Encryption method to new values" %step);

                        tdkTestObj, actualresult = setSecurityModeEnabledConfig(obj, mode, index, new_passphrase_config, initial_mode);
                        print("Result : %s" %actualresult);
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print("ACTUAL RESULT %d : Set Operation is Success" %step);
                            print("TEST EXECUTION RESULT : SUCCESS\n");

                            step = step + 1;
                            print("TEST STEP %d : Validate the KeyPassphrase and Encryption method config" %step);
                            print("EXPECTED RESULT %d : Set value should be reflected in get" %step);
                            tdkTestObj, result, set_passphrase_config = getSecurityModeEnabledConfig(obj, mode , index);
                            if expectedresult in result and set_passphrase_config == new_passphrase_config:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print("ACTUAL RESULT %d : The values set are : %s\n" %(step,set_passphrase_config));
                                print("TEST EXECUTION RESULT : SUCCESS\n");
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print("ACTUAL RESULT %d: Set not getting reflected in get" %step);
                                print("TEST EXECUTION RESULT :FAILURE\n");
                                continue
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print("ACTUAL RESULT %d : Set Operation failed" %step);
                            print("TEST EXECUTION RESULT : FAILURE\n");
                    else:
                        #Set the security mode if not already done and the conditions don't require setting passphrase
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
                        else:
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
                    print("\nTEST STEP %d : Get the Security Mode using Device.WiFi.AccessPoint.1.Security.ModeEnabled and check if mode is %s" %(step, mode));
                    print("EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.1.Security.ModeEnabled as %s" %(step,mode));
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
                            #Set the SAEPassphrase to a new value
                            step = step + 1;
                            # Passphrases are test values only
                            saePassphrase = "test_password_" + str(randint(0, 100));
                            tdkTestObj = obj.createTestStep("WIFIAgent_Set");
                            tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.SAEPassphrase");
                            tdkTestObj.addParameter("paramValue",saePassphrase);
                            tdkTestObj.addParameter("paramType","string");
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();
                            print("\nTEST STEP %d : Set Device.WiFi.AccessPoint.1.Security.SAEPassphrase to %s" %(step, saePassphrase));
                            print("EXPECTED RESULT %d : Should successfully set Device.WiFi.AccessPoint.1.Security.SAEPassphrase to %s" %(step,saePassphrase));
                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print("ACTUAL RESULT %d: Set operation success; Details : %s" %(step,details));
                                print("TEST EXECUTION RESULT :SUCCESS");
                                #Verify SET with GET
                                step = step + 1;
                                tdkTestObj = obj.createTestStep("WIFIAgent_Get");
                                tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.SAEPassphrase");
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails();
                                print("\nTEST STEP %d : Get the SAEPassphrase using Device.WiFi.AccessPoint.1.Security.SAEPassphrase after the SET operation" %step);
                                print("EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.1.Security.SAEPassphrase" %step);
                                if expectedresult in actualresult:
                                    final_sae = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print("ACTUAL RESULT %d: Get operation success; Details : %s" %(step, final_sae));
                                    print("TEST EXECUTION RESULT :SUCCESS");
                                    print("Set SAEPassphrase : ", saePassphrase);
                                    print("Get SAEPassphrase : ", final_sae);
                                    if saePassphrase == final_sae:
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print("SET is reflected in GET");
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print("SET is not reflected in GET");
                                else:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step, details));
                                    print("TEST EXECUTION RESULT :SUCCESS");
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print("ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,details));
                                print("TEST EXECUTION RESULT :FAILURE");
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print("SET is NOT reflected in GET");
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step, details));
                        print("TEST EXECUTION RESULT : FAILURE");

                #Revert the pre-requisites set
                if revert_flag == 1:
                    step = step + 1;
                    status = RevertWPA3Pre_requisite(obj, initial_value);
                    print("\nTEST STEP %d : Revert the pre-requisite to initial value" %step);
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
                print("Pre-Requisite is not set successfully");
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

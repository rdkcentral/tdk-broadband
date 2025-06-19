##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
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
  <name>TS_ONEWIFI_5GHzCheckSAEPassphraseSet_WithNonWPA3Modes</name>
  <primitive_test_id/>
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the SET operation of Device.WiFi.AccessPoint.2.Security.SAEPassphrase returns failure when the Device.WiFi.AccessPoint.2.Security.ModeEnabled is any of the non-WPA3 modes after enabling Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_ONEWIFI_183</test_case_id>
    <test_objective>Check if the SET operation of Device.WiFi.AccessPoint.2.Security.SAEPassphrase returns failure when the Device.WiFi.AccessPoint.2.Security.ModeEnabled is any of the non-WPA3 modes after enabling Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.AccessPoint.2.Security.ModesSupported
paramName : Device.WiFi.AccessPoint.2.Security.ModeEnabled
paramValue : security mode
paramType : string
paramName : Device.WiFi.AccessPoint.2.Security.SAEPassphrase
paramValue : SAE Passphrase
paramType : string</input_parameters>
    <automation_approch>1. Load the module
2. Get the initial security mode using Device.WiFi.AccessPoint.2.Security.ModeEnabled and store it.
3. Get the initial security config based on initial security mode and store it.
4. Check if the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable is enabled, else set it to true and validate with get.
5. Set Device.WiFi.AccessPoint.2.Security.ModeEnabled to personal security modes except WPA3 personal modes
6. For each of the non-WPA3 personal security modes set, check if the SAE Passphrase Device.WiFi.AccessPoint.2.Security.SAEPassphrase set operation returns failure. Cross verify with GET.
7. Revert the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable status if required
8. Revert Device.WiFi.AccessPoint.2.Security.ModeEnabled to initial mode if required.
9. Unload the module.</automation_approch>
    <expected_output>Setting Device.WiFi.AccessPoint.2.Security.SAEPassphrase should return failure when the security mode configured is not WPA3-Personal or WPA3-Personal-Transition.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_ONEWIFI_5GHzCheckSAEPassphraseSet_WithNonWPA3Modes</test_script>
    <skipped>No</skipped>
    <release_version>M101</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
from time import sleep
import tdklib;
from tdkutility import *
from random import randint;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_5GHzCheckSAEPassphraseSet_WithNonWPA3Modes');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus)
index = 2
config_personal = 0
wpa2_flag = 0

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Get the initial security mode
    expectedresult = "SUCCESS";
    step = 1;
    tdkTestObj = obj.createTestStep("WIFIAgent_Get");
    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.Security.ModeEnabled");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print("\nTEST STEP %d : Get the Security Mode using Device.WiFi.AccessPoint.2.Security.ModeEnabled" %step);
    print("EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.2.Security.ModeEnabled" %step);

    if expectedresult in actualresult:
        initial_mode = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
        tdkTestObj.setResultStatus("SUCCESS");
        print("ACTUAL RESULT %d: Get operation success; Details : %s" %(step, initial_mode));
        print("TEST EXECUTION RESULT :SUCCESS");

        #Get initial security config
        step = step + 1
        initial_config = {}
        tdkTestObj,actualresult,initial_config = getSecurityModeEnabledConfig(obj, initial_mode, index)

        print(f"TEST STEP {step}: Get the initial security configuration")
        print(f"EXPECTED RESULT {step}: Should succesfully get initial security configuration")

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: Initial security configuration reterived successfully")
            print("TEST EXECUTION RESULT :SUCCESS")

            #Check the Pre-requisites - WPA3_Personal_Transition RFC should be enabled
            step = step + 1;
            pre_req_set, tdkTestObj, step, revert_flag, initial_value = CheckWPA3Pre_requiste(obj, step);

            if pre_req_set == 1:
                if revert_flag == 0 and "Personal" not in initial_mode:
                    config_personal = 1
                elif revert_flag == 1 and "WPA2-Personal" in initial_mode:
                    wpa2_flag = 1

                print("\n*************RFC Pre-requisite set for the DUT*****************");

                #Set SAEPassphrase for each of the supported modes for the 5G private access point except the WPA3 modes and Enterprise modes
                final_sae = ""
                setModes = ["WPA-Personal", "WPA2-Personal", "WPA-WPA2-Personal"]
                for mode in setModes:
                    print("\n****************For Mode %s*******************" %mode);

                    #Set the security mode
                    step = step + 1;
                    if config_personal == 1:
                        #test values not real keyPassphrase
                        Key_Passphrase = "asdf@1234"
                        Encryption_Mode = "AES"
                        config_SET = {
                                    f"Device.WiFi.AccessPoint.{index}.Security.KeyPassphrase":Key_Passphrase,
                                    f"Device.WiFi.AccessPoint.{index}.Security.X_CISCO_COM_EncryptionMethod":Encryption_Mode
                        }
                        tdkTestObj,actualresult = setSecurityModeEnabledConfig(obj, mode, index, config_SET, initial_mode)
                        print(f"TEST STEP {step}: Set security mode and WPA config params");
                        print(f"EXPECTED RESULT {step}: Should set security mode and WPA config params ");
                        details = tdkTestObj.getResultDetails();
                    else:
                        tdkTestObj = obj.createTestStep("WIFIAgent_Set");
                        tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.Security.ModeEnabled");
                        tdkTestObj.addParameter("paramValue",mode);
                        tdkTestObj.addParameter("paramType","string");
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        print("\nTEST STEP %d : Set Device.WiFi.AccessPoint.2.Security.ModeEnabled to %s" %(step, mode));
                        print("EXPECTED RESULT %d : Should successfully set Device.WiFi.AccessPoint.2.Security.ModeEnabled to %s" %(step,mode));

                    if expectedresult in actualresult :
                        tdkTestObj.setResultStatus("SUCCESS");
                        print("ACTUAL RESULT %d: Set operation success; Details : %s" %(step,details));
                        print("TEST EXECUTION RESULT :SUCCESS");

                        #Verify the SET with GET
                        sleep(2)
                        step = step + 1;
                        tdkTestObj = obj.createTestStep("WIFIAgent_Get");
                        expectedresult = "SUCCESS";
                        tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.Security.ModeEnabled");
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        print("\nTEST STEP %d : Get the Security Mode using Device.WiFi.AccessPoint.2.Security.ModeEnabled and check if SET operation was success" %step);
                        print("EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.2.Security.ModeEnabled and should reflect the SET Mode" %step);

                        if expectedresult in actualresult:
                            curr_mode = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                            tdkTestObj.setResultStatus("SUCCESS");
                            print("ACTUAL RESULT %d: Get operation success; Details : %s" %(step, curr_mode));
                            print("TEST EXECUTION RESULT :SUCCESS");

                            print("Set Mode : ", mode);
                            print("Get Mode : ", curr_mode);

                            if curr_mode == mode:
                                config_personal = 0
                                tdkTestObj.setResultStatus("SUCCESS");
                                print("SET is reflected in GET");

                                #Set the SAEPassphrase to a new value and the SET operation should fail for non WPA3 modes
                                step = step + 1;
                                saePassphrase = "test_password_" + str(randint(0, 100));
                                tdkTestObj = obj.createTestStep("WIFIAgent_Set");
                                expectedresult = "FAILURE";
                                tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.Security.SAEPassphrase");
                                tdkTestObj.addParameter("paramValue",saePassphrase);
                                tdkTestObj.addParameter("paramType","string");
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails();

                                print("\nTEST STEP %d : Set Device.WiFi.AccessPoint.2.Security.SAEPassphrase to %s in %s mode" %(step, saePassphrase, mode));
                                print("EXPECTED RESULT %d : Should not set Device.WiFi.AccessPoint.2.Security.SAEPassphrase to %s in %s mode" %(step, saePassphrase, mode));

                                if expectedresult in actualresult:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print("ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,details));
                                    print("TEST EXECUTION RESULT :SUCCESS");

                                    #Check if SAEPassPhrase remains unchanged from the initial value
                                    step = step + 1;
                                    tdkTestObj = obj.createTestStep("WIFIAgent_Get");
                                    expectedresult = "SUCCESS";
                                    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.Security.SAEPassphrase");
                                    tdkTestObj.executeTestCase(expectedresult);
                                    actualresult = tdkTestObj.getResult();
                                    details = tdkTestObj.getResultDetails();

                                    print("\nTEST STEP %d : Get the SAEPassphrase using Device.WiFi.AccessPoint.2.Security.SAEPassphrase after the SET operation" %step);
                                    print("EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.2.Security.SAEPassphrase and it should remain unchanged from initial value" %step);

                                    if expectedresult in actualresult:
                                        final_sae = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print("ACTUAL RESULT %d: Get operation success; Details : %s" %(step, final_sae));
                                        print("TEST EXECUTION RESULT :SUCCESS");

                                        print("Set SAEPassphrase : ", saePassphrase);
                                        print("Get SAEPassphrase : ", final_sae);

                                        if saePassphrase != final_sae:
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            print("SAEPassPhrase remains unchanged from its initial value");
                                            print("TEST EXECUTION RESULT :SUCCESS");
                                        else:
                                            if saePassphrase == final_sae :
                                                tdkTestObj.setResultStatus("FAILURE");
                                                print("SAEPassPhrase SET is reflected in GET for a non-WPA3 mode");
                                                print("TEST EXECUTION RESULT :FAILURE");
                                            else :
                                                tdkTestObj.setResultStatus("FAILURE");
                                                print("SAEPassPhrase does not retain the initial value");
                                                print("TEST EXECUTION RESULT :FAILURE");
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step, details));
                                        print("TEST EXECUTION RESULT :FAILURE");
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print("ACTUAL RESULT %d: Set operation success; Details : %s" %(step,details));
                                    print("TEST EXECUTION RESULT :FAILURE");
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print("SET is NOT reflected in GET");
                                print("TEST EXECUTION RESULT :FAILURE");
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step, details));
                            print("TEST EXECUTION RESULT : FAILURE");
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print("ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,details));
                        print("TEST EXECUTION RESULT :FAILURE");

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
                    print("\nReverting pre-requisites not required");
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print("Pre-Requisite is not set successfully");

            #Revert operation of security mode
            if curr_mode != initial_mode and wpa2_flag == 0:
                print("Reverting to initial Security Mode...")
                step = step + 1

                tdkTestObj,actualresult = setSecurityModeEnabledConfig(obj, initial_mode, index, initial_config, curr_mode)
                details = tdkTestObj.getResultDetails()
                step = step + 1
                print("\nTEST STEP %d : Revert Device.WiFi.AccessPoint.2.Security.ModeEnabled to initial mode : %s" %(step, initial_mode));
                print("EXPECTED RESULT %d : Reverting to initial security mode should be success" %step);

                if expectedresult in actualresult :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("ACTUAL RESULT %d : Reverting Mode to initial value was successful; Details : %s" %(step, details));
                    print("TEST EXECUTION RESULT : SUCCESS");

                    #get the security mode and check if changed to initial mode
                    step = step + 1
                    print(f"TEST STEP {step}: Get the security mode and check")
                    print(f"EXPECTED RESULT {step}: security mode should be {initial_mode}")

                    paramName = "Device.WiFi.AccessPoint.2.Security.ModeEnabled"
                    tdkTestObj,actualresult,SecurityMode = wifi_GetParam(obj,paramName)

                    if expectedresult in actualresult and SecurityMode == initial_mode:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Security mode: {SecurityMode}")
                        print("TEST EXECUTION RESULT : SUCCESS");
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Security mode: {SecurityMode}")
                        print("TEST EXECUTION RESULT : FAILURE");

                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print("ACTUAL RESULT %d : Reverting Mode to initial value was NOT successful; Details : %s" %(step, details));
                    print("TEST EXECUTION RESULT : FAILURE");
            else :
                print("\nReverting Security Mode not required...")
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,details));
        print("TEST EXECUTION RESULT :FAILURE");

    obj.unloadModule("wifiagent");
else:
    print("Failed to load wifiagent module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");

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
  <version>1</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_ONEWIFI_6GHZ_PassphraseAfterReset</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Verify whether the Device.WiFi.AccessPoint.17.Security.KeyPassphrase value changes after performing a WiFi Radio and WiFi Access Point factory reset.</synopsis>
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
    <test_case_id>TC_ONEWIFI_291</test_case_id>
    <test_objective>This test case is to check if the passphrase changes after doing a wifi factory reset</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,BPI</test_setup>
    <pre_requisite>1. Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
    2. TDK Agent should be in a running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.AccessPoint.{index}.Security.ModeEnabled
    Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase
    Device.WiFi.AccessPoint.{index}.Security.X_CISCO_COM_EncryptionMethod
    Device.WiFi.AccessPoint.{index}.Security.KeyPassphrase
    Device.WiFi.X_CISCO_COM_FactoryResetRadioAndAp</input_parameters>
    <automation_approch>1. Load the module
2. Get and save Device.WiFi.AccessPoint.17.Security.KeyPassphrase
3. set a temporary passphrase
4. Perform a WiFi Radio and Access Point reset for 6 GHz using Device.WiFi.X_CISCO_COM_FactoryResetRadioAndAp.
5. After reset check if the temporary passphrase is changed or not
6. Restore the value of Device.WiFi.AccessPoint.17.Security.KeyPassphrase
7. Unload the module.</automation_approch>
    <expected_output>KeyPassphrase value should change and populate with default value after doing a wifi radio and AccessPoint factory reset</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiAgent</test_stub_interface>
    <test_script>TS_ONEWIFI_6GHZ_PassphraseAfterReset</test_script>
    <skipped></skipped>
    <release_version>M140</release_version>
    <remarks></remarks>
  </test_cases>
</xml>
'''
import tdklib
from tdkutility import *
from time import sleep
import random

# Test component
obj = tdklib.TDKScriptingLibrary("wifiagent", "1")
index = 17
expectedresult = "SUCCESS"
sm_flag = 0
exit_flag = 0
pass_revert = 0
FR_pass_revert = 0
# Configure test case
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_6GHZ_PassphraseAfterReset')

# Load module
loadmodulestatus = obj.getLoadModuleResult()
print(f"[LIB LOAD STATUS]  :  {loadmodulestatus}")

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    #Get initial security mode
    print(f"TEST STEP {step}: Get initial security mode using Device.WiFi.AccessPoint.{index}.Security.ModeEnabled")
    print(f"EXPECTED RESULT {step} : Should get initial security mode")
    param_mode = f"Device.WiFi.AccessPoint.{index}.Security.ModeEnabled"
    tdkTestObj, actualresult, initial_mode = wifi_GetParam(obj, param_mode)

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Initial mode: {initial_mode}")
        print("TEST EXECUTION RESULT : SUCCESS")

        #if initial mode is not Personal mode change it to Personal mode
        if initial_mode != "WPA3-Personal":
            #Get the initial security config
            step = step + 1
            print(f"TEST STEP {step}: Get the initial security configuration")
            print(f"EXPECTED RESULT {step}: Should succesfully get initial security configuration")
            initial_config = {}
            tdkTestObj,actualresult,initial_config = getSecurityModeEnabledConfig(obj, initial_mode, index)

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Initial security configuration: {initial_config}")
                print("TEST EXECUTION RESULT :SUCCESS")

                #Set the security mode to WPA3-Personal
                step +=1
                #test values not real secrets
                SAE_Pass = "asdf@1234"
                Encryption_Mode = "AES"
                config_SET = {
                            f"Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase":SAE_Pass,
                            f"Device.WiFi.AccessPoint.{index}.Security.X_CISCO_COM_EncryptionMethod":Encryption_Mode
                }
                tdkTestObj,actualresult = setSecurityModeEnabledConfig(obj, "WPA3-Personal", index, config_SET, initial_mode)
                details = tdkTestObj.getResultDetails()

                print(f"TEST STEP {step}: Set security mode to WPA3-Personal")
                print(f"EXPECTED RESULT {step}: Should set security mode to WPA3-Personal")

                if expectedresult in actualresult:
                    sm_flag = 1
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}:SET operation successful.Details: {details}")
                    print("TEST EXECUTION RESULT :SUCCESS")

                    sleep(2)
                    #validate the security mode with get
                    step +=1
                    tdkTestObj = obj.createTestStep("WIFIAgent_Get")
                    tdkTestObj.addParameter("paramName",f"Device.WiFi.AccessPoint.{index}.Security.ModeEnabled")
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    details = tdkTestObj.getResultDetails()

                    print(f"TEST STEP {step} : Get the Security Mode and check it is changed to WPA3-Personal")
                    print(f"EXPECTED RESULT {step} : Should successfully set security mode to WPA3-Personal")

                    if expectedresult in actualresult and details != "":
                        sec_mode = details.split("VALUE:")[1].split(' ')[0].split(',')[0]
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Security Mode: {sec_mode}")
                        print("TEST EXECUTION RESULT :SUCCESS")

                        if sec_mode != "WPA3-Personal":
                            tdkTestObj.setResultStatus("FAILURE")
                            print("Security mode not changed to WPA3-Personal")
                            print("TEST EXECUTION RESULT :FAILURE")
                            exit_flag = 1
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Get operation failed Details : {details}")
                        print("TEST EXECUTION RESULT :FAILURE")
                        exit_flag = 1
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Set operation failed Details : {details}")
                    print("TEST EXECUTION RESULT :FAILURE")
                    exit_flag = 1
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Failed to retrive Initial security configuration")
                print("TEST EXECUTION RESULT :FAILURE")
                exit_flag = 1
        else:
            print(f"Initial mode is already WPA3-Personal. No Security mode change required.")

        if exit_flag != 1:
            #Get current keypassphrase
            step += 1
            print(f"TEST STEP {step}: Get current KeyPassphrase using Device.WiFi.AccessPoint.{index}.Security.KeyPassphrase")
            print(f"EXPECTED RESULT {step} : Should get current KeyPassphrase")
            param_key = f"Device.WiFi.AccessPoint.{index}.Security.KeyPassphrase"
            tdkTestObj, actualresult, Current_passphrase = wifi_GetParam(obj, param_key)

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Current KeyPassphrase: {Current_passphrase}")
                print("TEST EXECUTION RESULT : SUCCESS")

                #Set Keypassphrase to new value
                step += 1
                #it is a Test value not real secret
                new_passphrase = "TestKey" + str(random.randint(1000, 9999))
                print(f"New KeyPassphrase set value: {new_passphrase}")
                print(f"TEST STEP {step}: Set KeyPassphrase to new value")
                print(f"EXPECTED RESULT {step}: Should set Keypassphrase to new value")
                param = f"Device.WiFi.AccessPoint.{index}.Security.KeyPassphrase"
                tdkTestObj, actualresult = wifi_SetParam(obj, param, new_passphrase, "string")

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Set KeyPassphrase success")
                    print("TEST EXECUTION RESULT : SUCCESS")

                    sleep(3)
                    step += 1
                    print(f"TEST STEP {step}: Get KeyPassphrase to validate set value")
                    print(f"EXPECTED RESULT {step}: Should get Keypassphrase")
                    tdkTestObj, actualresult, tmp_pass = wifi_GetParam(obj, param)

                    if expectedresult in actualresult and tmp_pass == new_passphrase:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: KeyPassphrase: {tmp_pass}")
                        print("TEST EXECUTION RESULT : SUCCESS")
                        pass_revert = 1

                        #Do Factory Reset for wifi setting
                        step += 1
                        print(f"TEST STEP {step}: Initiate factory reset ")
                        print(f"EXPECTED RESULT {step}: Should Initiate factory reset ")
                        paramValue = "3,17"
                        param = "Device.WiFi.X_CISCO_COM_FactoryResetRadioAndAp"
                        tdkTestObj, actualresult = wifi_SetParam(obj, param, paramValue, "string")
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: Factory reset success")
                            print("TEST EXECUTION RESULT : SUCCESS")
                            sleep(180)

                            #Get the KeyPassphrase after FR
                            step += 1
                            print(f"TEST STEP {step}: Get KeyPassphrase to validate set value")
                            print(f"EXPECTED RESULT {step}: Should get Keypassphrase")
                            param = f"Device.WiFi.AccessPoint.{index}.Security.KeyPassphrase"
                            tdkTestObj, actualresult, pass_FR = wifi_GetParam(obj, param)

                            if expectedresult in actualresult and pass_FR != tmp_pass:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"ACTUAL RESULT {step}: KeyPassphrase Changed successfully after Factory Reset")
                                print(f"KeyPassphrase after Factory Reset: {pass_FR}")
                                print("TEST EXECUTION RESULT : SUCCESS")

                                if pass_FR != Current_passphrase:
                                    FR_pass_revert = 1
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: KeyPassphrase not changed after FR")
                                print(f"KeyPassphrase after Factory Reset: {pass_FR}")
                                print("TEST EXECUTION RESULT : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: Factory reset Failure")
                            print("TEST EXECUTION RESULT : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: KeyPassphrase: {tmp_pass}")
                        print("TEST EXECUTION RESULT : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Failed to set KeyPassphrase")
                    print("TEST EXECUTION RESULT : FAILURE")

                #Revert KeyPassphrase
                if (pass_revert == 1 or FR_pass_revert == 1) and sm_flag == 0:
                    step += 1
                    print(f"TEST STEP {step}: Revert KeyPassphrase to initial value")
                    print(f"EXPECTED RESULT {step}: Should revert Keypassphrase")
                    tdkTestObj, actualresult = wifi_SetParam(obj, param, Current_passphrase, "string")
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: KeyPassphrase  reverted to initial value")
                        print("TEST EXECUTION RESULT : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Failed to Revert KeyPassphrase to initial value")
                        print("TEST EXECUTION RESULT : FAILURE")
                else:
                    print("Reverting KeyPassphrase not required")

                #Revert security mode
                if sm_flag == 1:
                    print("Reverting to initial Security Mode...")
                    step += 1
                    tdkTestObj, actualresult = setSecurityModeEnabledConfig(obj, initial_mode, index, initial_config, sec_mode)
                    details = tdkTestObj.getResultDetails()

                    step += 1
                    print(f"TEST STEP {step} : Revert Device.WiFi.AccessPoint.{index}.Security.ModeEnabled to initial mode : {initial_mode}")
                    print(f"EXPECTED RESULT {step} : Reverting to initial security mode should be success")

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step} : Reverting Mode to initial value was successful Details : {details}")
                        print("TEST EXECUTION RESULT : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step} : Reverting Mode to initial value was NOT successful Details : {details}")
                        print("TEST EXECUTION RESULT : FAILURE")
                else:
                    print("Reverting Security Mode not required...")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Failed to get KeyPassphrase.")
                print("TEST EXECUTION RESULT : FAILURE")
        else:
            print("Not proceding further due to security mode change failure")
            tdkTestObj.setResultStatus("FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to get initial mode")
        print("TEST EXECUTION RESULT : FAILURE")

    obj.unloadModule("wifiagent")
else:
    print("Module loading failed")
    obj.setLoadModuleStatus("FAILURE")


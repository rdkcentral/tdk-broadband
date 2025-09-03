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
  <name>TS_ONEWIFI_6GHzSetKeyPassphrase_WithPersonalSecurityModes</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if KeyPassphrase is able to set when ModeEnabled is Personal security mode.</synopsis>
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
    <test_case_id>TC_ONEWIFI_293</test_case_id>
    <test_objective>Check if the KeyPassphrase is successfully set using Device.WiFi.AccessPoint.17.Security.KeyPassphrase when  personal security mode is set using Device.WiFi.AccessPoint.17.Security.ModeEnabled from the supported list of modes retrieved using Device.WiFi.AccessPoint.17.Security.ModesSupported
</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,BPI</test_setup>
    <pre_requisite>1. Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
    2. TDK Agent should be in a running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.AccessPoint.{index}.Security.ModesSupported
    Device.WiFi.AccessPoint.{index}.Security.ModeEnabled
    Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase
    Device.WiFi.AccessPoint.{index}.Security.X_CISCO_COM_EncryptionMethod</input_parameters>
    <automation_approch>1. Load the modules
2. Get the supported security modes using Device.WiFi.AccessPoint.17.Security.ModesSupported.
4. Get the initial security mode using Device.WiFi.AccessPoint.17.Security.ModeEnabled
3. Get the initial security KeyPassphrase using Device.WiFi.AccessPoint.17.Security.KeyPassphrase
4. Set the security mode to supported Personal modes and for each Personal mode set, set the Security KeyPassphrase and check if the SET operation is success.
5. Revert to initial values.
6. Unload the modules.</automation_approch>
    <expected_output>The KeyPassphrase should be successfully set using Device.WiFi.AccessPoint.17.Security.KeyPassphrase when  personal security mode is set using Device.WiFi.AccessPoint.17.Security.ModeEnabled from the supported list of modes retrieved using Device.WiFi.AccessPoint.17.Security.ModesSupported.
</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiAgent</test_stub_interface>
    <test_script>TS_ONEWIFI_6GHzSetKeyPassphrase_WithPersonalSecurityModes</test_script>
    <skipped></skipped>
    <release_version>M140</release_version>
    <remarks></remarks>
  </test_cases>
</xml>
'''

import tdklib
from tdkutility import *
from time import sleep

# Test component
obj = tdklib.TDKScriptingLibrary("wifiagent", "1")
# Configure test case
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_6GHzSetKeyPassphrase_WithPersonalSecurityModes')

# Load module
loadmodulestatus = obj.getLoadModuleResult()
print(f"[LIB LOAD STATUS]  :  {loadmodulestatus}")
index = 17
expectedresult = "SUCCESS"
sm_flag = 0
exit_flag  = 0
pass_flag = 0

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    step = 1

    #Get the supported Security Modes
    paramName = f"Device.WiFi.AccessPoint.{index}.Security.ModesSupported"
    tdkTestObj,actualresult,supported_modes = wifi_GetParam(obj,paramName)
    details = tdkTestObj.getResultDetails()

    print(f"TEST STEP {step} : Get the supported modes using Device.WiFi.AccessPoint.{index}.Security.ModesSupported")
    print(f"EXPECTED RESULT {step} : Should successfully get Device.WiFi.AccessPoint.{index}.Security.ModesSupported")

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Get operation success; Details : {details}")
        print(f"Supported Modes : {supported_modes}")
        print("TEST EXECUTION RESULT : SUCCESS")

        #Get initial security mode
        step +=1
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
                        print(f"ACTUAL RESULT {step}: {details}")
                        print("TEST EXECUTION RESULT :SUCCESS")

                        #validate the security mode with get
                        sleep(2)
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
                tdkTestObj, actualresult, current_passphrase = wifi_GetParam(obj, param_key)

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Current KeyPassphrase: {current_passphrase}")
                    print("TEST EXECUTION RESULT : SUCCESS")
                    #Set Keypassphrase to new value
                    step += 1
                    print(f"TEST STEP {step}: Set KeyPassphrase to new value")
                    print(f"EXPECTED RESULT {step}: Should set Keypassphrase to new value")
                    #it is a Test value
                    new_passphrase = "TestKeyPass123"
                    param = f"Device.WiFi.AccessPoint.{index}.Security.KeyPassphrase"
                    tdkTestObj, actualresult = wifi_SetParam(obj, param, new_passphrase, "string")

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Set KeyPassphrase success")
                        print("TEST EXECUTION RESULT : SUCCESS")
                        sleep(2)

                        step += 1
                        print(f"TEST STEP {step}: Get KeyPassphrase to validate set value")
                        print(f"EXPECTED RESULT {step}: Should get Keypassphrase")
                        tdkTestObj, actualresult, get_pass = wifi_GetParam(obj, param)

                        if expectedresult in actualresult and get_pass == new_passphrase:
                            pass_flag = 1
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: KeyPassphrase Changed successfully")
                            print("TEST EXECUTION RESULT : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: KeyPassphrase: {get_pass}")
                            print("TEST EXECUTION RESULT : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Failed to set KeyPassphrase.")
                        print("TEST EXECUTION RESULT : FAILURE")

                    #Revert KeyPassphrase
                    if pass_flag == 1 and sm_flag == 0:
                        step += 1
                        print(f"TEST STEP {step}: Revert KeyPassphrase to initial value")
                        print(f"EXPECTED RESULT {step}: Should revert Keypassphrase")
                        tdkTestObj, actualresult = wifi_SetParam(obj, param, current_passphrase, "string")
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
                    print(f"ACTUAL RESULT {step}: Failed to get KeyPassphrase.Details: {details}")
                    print("TEST EXECUTION RESULT : FAILURE")
            else:
                print("Not proceding further due to security mode change failure")
                tdkTestObj.setResultStatus("FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Failed to get initial mode. Details: {details}")
            print("TEST EXECUTION RESULT : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Get operation Failed. Details : {details}")
        print("TEST EXECUTION RESULT : FAILURE")

    obj.unloadModule("wifiagent")
else:
    print("Module loading failed")
    obj.setLoadModuleStatus("FAILURE")


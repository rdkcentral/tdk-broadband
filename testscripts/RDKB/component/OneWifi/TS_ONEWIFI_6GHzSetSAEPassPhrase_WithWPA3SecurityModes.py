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
  <name>TS_ONEWIFI_6GHzSetSAEPassPhrase_WithWPA3SecurityModes</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if setting Device.WiFi.AccessPoint.17.Security.SAEPassphrase to valid Passphrase is success when the Access Point Security Mode Enabled Device.WiFi.AccessPoint.17.Security.ModeEnabled is set to WPA3-Personal.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <test_case_id>TC_ONEWIFI_298</test_case_id>
    <test_objective>Check if setting Device.WiFi.AccessPoint.17.Security.SAEPassphrase to valid Passphrase is success when the Access Point Security Mode Enabled Device.WiFi.AccessPoint.17.Security.ModeEnabled is set to WPA3-Personal.
</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,BPI</test_setup>
    <pre_requisite>1. Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
    2. TDK Agent should be in a running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.AccessPoint.17.Security.ModeEnabled
    Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase
    Device.WiFi.AccessPoint.{index}.Security.X_CISCO_COM_EncryptionMethod</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial security mode using Device.WiFi.AccessPoint.17.Security.ModeEnabled and store it.
3. If the initial security mode is not WPA3-Personal then change it to WPA3-Personal along with the security configurations.
4. Now get initial SAEPassphrase using Device.WiFi.AccessPoint.17.Security.SAEPassphrase and store it.
5. Check if the SET operation of Device.WiFi.AccessPoint.17.Security.SAEPassphrase to a valid new value returns success and validate with get.
6. Revert SAEpassphrase to initial value if required.
7. Revert the security mode enabled and the security configuration values to initial value if required.
8. Unload the modules.</automation_approch>
    <expected_output>Setting Device.WiFi.AccessPoint.17.Security.SAEPassphrase should be successful when security mode is WPA3-Personal
</expected_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_ONEWIFI_6GHzSetSAEPassPhrase_WithWPA3SecurityModes</test_script>
    <skipped></skipped>
    <release_version>M141</release_version>
    <remarks></remarks>
  </test_cases>
</xml>
'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
from tdkutility import *
from random import randint
import time

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1")

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_6GHzSetSAEPassPhrase_WithWPA3SecurityModes')

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus)
index = 17
sm_flag = 0
exit_flag = 0

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    #Get Security Mode
    paramName = f"Device.WiFi.AccessPoint.{index}.Security.ModeEnabled"
    tdkTestObj,actualresult,initial_mode = wifi_GetParam(obj,paramName)

    print(f"\nTEST STEP {step} : Get the Security Mode using Device.WiFi.AccessPoint.17.Security.ModeEnabled")
    print(f"EXPECTED RESULT {step} : Should successfully get Device.WiFi.AccessPoint.17.Security.ModeEnabled")

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Initial security mode :{initial_mode}")
        print("TEST EXECUTION RESULT :SUCCESS")

        if initial_mode != "WPA3-Personal":
            #Get the initial security config
            step = step + 1
            print(f"TEST STEP {step}: Get the initial security configuration")
            print(f"EXPECTED RESULT {step}: Should succesfully get initial security configuration")
            initial_config = {}
            tdkTestObj,actualresult,initial_config = getSecurityModeEnabledConfig(obj, initial_mode, index)

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Initial security configuration reterived successfully")
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
                print(f"EXPECTED RESULT {step}: Should set security mode to WPA3-Personal ")

                if expectedresult in actualresult:
                    sm_flag = 1
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}:Security mode changed to WPA3-Personal. Details: {details}")
                    print("TEST EXECUTION RESULT :SUCCESS")

                    time.sleep(2)
                    #validate the security mode with get
                    step +=1
                    paramName = f"Device.WiFi.AccessPoint.{index}.Security.ModeEnabled"
                    tdkTestObj,actualresult,sec_mode = wifi_GetParam(obj,paramName)

                    print(f"\nTEST STEP {step} : Get the Security Mode and check it is changed to WPA3-Personal")
                    print(f"EXPECTED RESULT {step} : Should successfully set security mode to WPA3-Personal")

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Security Mode: {sec_mode}")
                        print("TEST EXECUTION RESULT :SUCCESS")

                        #check if security mode is WPA3-Personal
                        if sec_mode != "WPA3-Personal":
                            tdkTestObj.setResultStatus("FAILURE")
                            print("Securit mode is not WPA3-Personal")
                            exit_flag = 1
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Get operation failed ")
                        print("TEST EXECUTION RESULT :FAILURE")
                        exit_flag = 1
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Failed to set security mode to WPA3-Personal. Details: {details}")
                    print("TEST EXECUTION RESULT :FAILURE")
                    exit_flag = 1
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Failed to retrive Initial security configuration")
                print("TEST EXECUTION RESULT :FAILURE")
                exit_flag = 1
        else:
            print("Changing Security mode not required")

        if exit_flag != 1:
            #Get initial SAE passphrase
            step +=1
            paramName = f"Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase"
            tdkTestObj,actualresult,initial_SAE = wifi_GetParam(obj,paramName)

            print(f"\nTEST STEP {step} : Get the initial SAEpassphrase")
            print(f"EXPECTED RESULT {step} : Should successfully get initial SAEPassphrase")

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Initial SAEPassphrase :{initial_SAE}")
                print("TEST EXECUTION RESULT :SUCCESS")

                #Set SAEPass pharse to a test value
                step = step + 1
                #this is test value
                test_val = "test_saepass"
                paramName = f"Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase"
                tdkTestObj,actualresult = wifi_SetParam(obj,paramName,test_val,"string")

                print(f"TEST STEP {step} :  Set SAEPassphrase to {test_val}")
                print(f"EXPECTED RESULT {step} : Should Set SAEPassphrase to {test_val}")

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Set Operation success.")
                    print("TEST EXECUTION RESULT :SUCCESS")
                    time.sleep(2)

                    #Validate with Get
                    step += 1
                    paramName = f"Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase"
                    tdkTestObj,actualresult,set_SAE = wifi_GetParam(obj,paramName)

                    print(f"\nTEST STEP {step} : Get SAEpassphrase")
                    print(f"EXPECTED RESULT {step} : Should successfully get SAEPassphrase")

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: SAEPassphrase :{set_SAE}")
                        print("TEST EXECUTION RESULT :SUCCESS")

                        step += 1
                        print(f"\nTEST STEP {step} : Check {test_val} is reflected in SAEpassphrase")
                        print(f"EXPECTED RESULT {step} : {test_val} should reflect in SAEPassphrase")

                        if set_SAE == test_val:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: Set value is reflected in GET")
                            print("TEST EXECUTION RESULT :SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: Set value is not reflected in GET")
                            print("TEST EXECUTION RESULT :FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Get Operation failed.")
                        print("TEST EXECUTION RESULT :FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Set Operation Failure.")
                    print("TEST EXECUTION RESULT :FAILURE")

                # Revert operation
                if set_SAE != initial_SAE and sm_flag == 0:
                    print("\nReverting to initial SAEPassPhrase...")
                    step += 1
                    paramName = f"Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase"
                    tdkTestObj,actualresult = wifi_SetParam(obj,paramName,initial_SAE,"string")

                    print(f"TEST STEP {step} : Revert Device.WiFi.AccessPoint.17.Security.SAEPassphrase to {initial_SAE}")
                    print(f"EXPECTED RESULT {step} : Should successfully revert Device.WiFi.AccessPoint.17.Security.SAEPassphrase to {initial_SAE}")

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Set operation success.")
                        print("TEST EXECUTION RESULT : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Set operation failed.")
                        print("TEST EXECUTION RESULT : FAILURE")
                else:
                    print("\nSAEPassPhrase revert operation not required...")

                #Revert operation for security mode
                if sm_flag == 1:
                    print("Reverting to initial Security Mode...")
                    step += 1
                    tdkTestObj, actualresult = setSecurityModeEnabledConfig(obj, initial_mode, index, initial_config, sec_mode)
                    details = tdkTestObj.getResultDetails()

                    step += 1
                    print(f"\nTEST STEP {step} : Revert Device.WiFi.AccessPoint.17.Security.ModeEnabled to initial mode : {initial_mode}")
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
                    print("\nReverting Security Mode not required...")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Failed to get initial SAEPassphrase.")
                print("TEST EXECUTION RESULT :FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to get initial security mode.")
        print("TEST EXECUTION RESULT :FAILURE")

    obj.unloadModule("wifiagent")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
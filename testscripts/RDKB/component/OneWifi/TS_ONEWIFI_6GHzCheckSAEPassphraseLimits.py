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
  <name>TS_ONEWIFI_6GHzCheckSAEPassphraseLimits</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if SAEPassphrase SET operation fails when length of Passphrase is less than lower limit of 8 characters and more than upper limit of 63 characters</synopsis>
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
    <test_case_id>TC_ONEWIFI_292</test_case_id>
    <test_objective>Check if the SAEPassphrase Device.WiFi.AccessPoint.17.Security.SAEPassphrase SET operation fails when the length of the Passphrase is less than lower limit of 8 characters and more than upper limit of 63 characters</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,BPI</test_setup>
    <pre_requisite>1. Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
    2. TDK Agent should be in a running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.AccessPoint.17.Security.SAEPassphrase
    Device.WiFi.AccessPoint.17.Security.ModeEnabled
    Device.WiFi.AccessPoint.17.Security.X_CISCO_COM_EncryptionMethod</input_parameters>
    <automation_approch>1. Load the module
2. Get the initial security mode using Device.WiFi.AccessPoint.17.Security.ModeEnabled and store it.
3. Get the initial value of Device.WiFi.AccessPoint.17.Security.SAEPassphrase and store it.
4. Set Device.WiFi.AccessPoint.17.Security.ModeEnabled to "WPA3-Personal" and validate the SET with GET.
5. Check if the SET operation of Device.WiFi.AccessPoint.17.Security.SAEPassphrase fails for a passphrase length less than the lower limit of 8 characters. Verify the SET with GET.
6. Check if the SET operation of Device.WiFi.AccessPoint.17.Security.SAEPassphrase fails for a passphrase length more than the upper limit of 63 characters. Verify the SET with GET.
7. Revert Device.WiFi.AccessPoint.17.Security.SAEPassphrase if required.
8. Revert Device.WiFi.AccessPoint.17.Security.ModeEnabled to initial mode.
9. Unload the module</automation_approch>
    <expected_output>Setting Device.WiFi.AccessPoint.17.Security.SAEPassphrase to SAE Passphrases whose length is lower than the lower limit(8) and more than the upper limit(63) should return failure.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiAgent</test_stub_interface>
    <test_script>TS_ONEWIFI_6GHzCheckSAEPassphraseLimits</test_script>
    <skipped></skipped>
    <release_version>M140</release_version>
    <remarks></remarks>
  </test_cases>
</xml>
'''

def setSAEPassphrase(tdkTestObj, saePassphrase, expectedresult):
    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.17.Security.SAEPassphrase")
    tdkTestObj.addParameter("paramValue",saePassphrase)
    tdkTestObj.addParameter("paramType","string")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()
    return actualresult, details

def getSAEPassphrase(tdkTestObj, expectedresult):
    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.17.Security.SAEPassphrase")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()
    return actualresult, details



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
obj.configureTestCase(ip,port,'TS_ONEWIFI_6GHzCheckSAEPassphraseLimits')

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
    param_mode = f"Device.WiFi.AccessPoint.{index}.Security.ModeEnabled"
    tdkTestObj, actualresult, initial_mode = wifi_GetParam(obj, param_mode)
    details = tdkTestObj.getResultDetails()

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
                    tdkTestObj = obj.createTestStep("WIFIAgent_Get")
                    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.17.Security.ModeEnabled")
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    details = tdkTestObj.getResultDetails()

                    print(f"\nTEST STEP {step} : Get the Security Mode and check it is changed to WPA3-Personal")
                    print(f"EXPECTED RESULT {step} : Should successfully set security mode to WPA3-Personal")

                    if expectedresult in actualresult and details != "":
                        sec_mode = details.split("VALUE:")[1].split(' ')[0].split(',')[0]
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
                        print(f"ACTUAL RESULT {step}: Get operation failed Details : {details}")
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
        else:
            print("Changing Security mode not required")

        if exit_flag != 1:
            #Get current SAE passphrase
            step +=1
            param_mode = f"Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase"
            tdkTestObj, actualresult, Curr_SAE = wifi_GetParam(obj, param_mode)
            details = tdkTestObj.getResultDetails()

            print(f"\nTEST STEP {step} : Get the current SAEpassphrase")
            print(f"EXPECTED RESULT {step} : Should successfully get current SAEPassphrase")

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Current SAEPassphrase :{Curr_SAE}")
                print("TEST EXECUTION RESULT :SUCCESS")

                # Set the SAEPassPhrase to a value which has less than 8 characters
                print("\n*************Checking for Lower Limit condition*************")
                expectedresult = "FAILURE"
                step += 1
                saePassphrase = "test_" + str(randint(10, 100))
                tdkTestObj = obj.createTestStep("WIFIAgent_Set")
                actualresult, details = setSAEPassphrase(tdkTestObj, saePassphrase, expectedresult)

                print(f"\nTEST STEP {step} : Check if setting Device.WiFi.AccessPoint.17.Security.SAEPassphrase to a value less than the lower limit of characters (<8) - {saePassphrase} fails")
                print(f"EXPECTED RESULT {step} : Setting Device.WiFi.AccessPoint.17.Security.SAEPassphrase to a value less than the lower limit of characters (<8) - {saePassphrase} should fail")

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Set operation failed Details : {details}")
                    print("TEST EXECUTION RESULT : SUCCESS")

                    # Verify SET with GET
                    step += 1
                    expectedresult = "SUCCESS"
                    tdkTestObj = obj.createTestStep("WIFIAgent_Get")
                    actualresult, details = getSAEPassphrase(tdkTestObj, expectedresult)

                    print(f"\nTEST STEP {step} : Get the SAEPassphrase using Device.WiFi.AccessPoint.17.Security.SAEPassphrase after the SET operation")
                    print(f"EXPECTED RESULT {step} : Should successfully get Device.WiFi.AccessPoint.17.Security.SAEPassphrase")

                    if expectedresult in actualresult:
                        final_sae = details.split("VALUE:")[1].split(' ')[0].split(',')[0]
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Get operation success Details : {final_sae}")
                        print("TEST EXECUTION RESULT : SUCCESS")

                        print(f"Set SAEPassphrase : {saePassphrase}")
                        print(f"Get SAEPassphrase : {final_sae}")

                        if saePassphrase != final_sae and final_sae == Curr_SAE:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("SAEPassPhrase remains unchanged from its initial value")
                        else:
                            if saePassphrase == final_sae:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("SAEPassPhrase SET is reflected in GET even if the length of the Passphrase is less than lower limit")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("SAEPassPhrase does not retain the initial value")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Get operation failed. Details: {details}")
                        print("TEST EXECUTION RESULT : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Set operation success. Details: {details}")
                    print("TEST EXECUTION RESULT : FAILURE")

                # Set the SAEPassPhrase to a value which has more than 63 characters
                print("\n*************Checking for Upper Limit condition*************")
                expectedresult = "FAILURE"
                step += 1
                saePassphrase = "qwertyuioplkjhgfdsazxcvbnm@#$%^&*()_____MKIOPLSDDFWERG1234567890"
                tdkTestObj = obj.createTestStep("WIFIAgent_Set")
                actualresult, details = setSAEPassphrase(tdkTestObj, saePassphrase, expectedresult)

                print(f"\nTEST STEP {step} : Check if setting Device.WiFi.AccessPoint.17.Security.SAEPassphrase to a value more than the upper limit of characters (>63) - {saePassphrase} fails")
                print(f"EXPECTED RESULT {step} : Setting Device.WiFi.AccessPoint.17.Security.SAEPassphrase to a value more than the upper limit of characters (>63) - {saePassphrase} should fail")

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Set operation failed Details : {details}")
                    print("TEST EXECUTION RESULT : SUCCESS")

                    # Verify SET with GET
                    step += 1
                    expectedresult = "SUCCESS"
                    tdkTestObj = obj.createTestStep("WIFIAgent_Get")
                    actualresult, details = getSAEPassphrase(tdkTestObj, expectedresult)

                    print(f"\nTEST STEP {step} : Get the SAEPassphrase using Device.WiFi.AccessPoint.17.Security.SAEPassphrase after the SET operation")
                    print(f"EXPECTED RESULT {step} : Should successfully get Device.WiFi.AccessPoint.17.Security.SAEPassphrase")

                    if expectedresult in actualresult:
                        final_sae = details.split("VALUE:")[1].split(' ')[0].split(',')[0]
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Get operation success Details : {final_sae}")
                        print("TEST EXECUTION RESULT : SUCCESS")

                        print(f"Set SAEPassphrase : {saePassphrase}")
                        print(f"Get SAEPassphrase : {final_sae}")

                        if saePassphrase != final_sae and final_sae == Curr_SAE:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("SAEPassPhrase remains unchanged from its initial value")
                        else:
                            if saePassphrase == final_sae:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("SAEPassPhrase SET is reflected in GET even if the length of the Passphrase is more than upper limit")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("SAEPassPhrase does not retain the initial value")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Get operation failed Details : {details}")
                        print("TEST EXECUTION RESULT : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Set operation success Details : {details}")
                    print("TEST EXECUTION RESULT : FAILURE")

                # Revert operation
                if final_sae != Curr_SAE and sm_flag == 0:
                    print("\nReverting to initial SAEPassPhrase...")
                    step += 1
                    tdkTestObj = obj.createTestStep("WIFIAgent_Set")
                    expectedresult = "SUCCESS"
                    actualresult, details = setSAEPassphrase(tdkTestObj, Curr_SAE, expectedresult)

                    print(f"TEST STEP {step} : Revert Device.WiFi.AccessPoint.17.Security.SAEPassphrase to {Curr_SAE}")
                    print(f"EXPECTED RESULT {step} : Should successfully revert Device.WiFi.AccessPoint.17.Security.SAEPassphrase to {Curr_SAE}")

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Set operation success Details : {details}")
                        print("TEST EXECUTION RESULT : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Set operation failed Details : {details}")
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
                print(f"ACTUAL RESULT {step}: Failed to get initial SAEPassphrase. Details: {details}")
                print("TEST EXECUTION RESULT :FAILURE")
        else:
            print("Not proceding further due to security mode change failure")
            tdkTestObj.setResultStatus("FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to get initial security mode. Details: {details}")
        print("TEST EXECUTION RESULT :FAILURE")

    obj.unloadModule("wifiagent")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

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
  <name>TS_ONEWIFI_6GHZ_WPA_Config_On_EnhancedOpen_Psk</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check WPA configuration on security mode transition (Enhanced-Open-WPA3-Personal) for 6ghz</synopsis>
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
    <test_case_id>TC_ONEWIFI_296</test_case_id>
    <test_objective>Check WPA configuration on security mode transition (Enhanced-Open-WPA3-Personal) for 6ghz
</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,BPI</test_setup>
    <pre_requisite>1. Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
    2. TDK Agent should be in a running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.AccessPoint.{index}.Security.ModeEnabled
    Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase
    Device.WiFi.AccessPoint.{index}.Security.X_CISCO_COM_EncryptionMethod</input_parameters>
    <automation_approch>1. Load the module.
2. Get the initial security mode using Device.WiFi.AccessPoint.17.Security.ModeEnabled and store it.
3. Change security mode to Enhanced-Open using Device.WiFi.AccessPoint.17.Security.ModeEnabled.
4. Check initial WPA config using Device.WiFi.AccessPoint.17.Security.X_CISCO_COM_EncryptionMethod and Device.WiFi.AccessPoint.17.Security.SAEPassphrase. Encryption mode should be AES and SAEPassphrase should be empty when security mode is "Enhanced-Open".
5. Change the security mode to WPA3-Personal,  and SAEPassphrase to a new value.
6. Check if security mode set is reflected in get and if the WPA configuration is set to the new values.
7. Revert to initial security mode.
8. Unload the module</automation_approch>
    <expected_output>When security mode changes for open to psk (Enhanced-Open to WPA3-Personal) WPA config should reset.
</expected_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_ONEWIFI_6GHZ_WPA_Config_On_EnhancedOpen_Psk</test_script>
    <skipped></skipped>
    <release_version>M141</release_version>
    <remarks></remarks>
  </test_cases>
</xml>
'''

#import statements
import tdklib
from tdkutility import *
from time import sleep

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1")

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_6GHZ_WPA_Config_On_EnhancedOpen_Psk')

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
set_mode = 0
index = 17

if "SUCCESS" in loadmodulestatus.upper():
    # Set the load module status
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    #Get the initial Security Mode
    paramName = f"Device.WiFi.AccessPoint.{index}.Security.ModeEnabled"
    tdkTestObj,actualresult,initialSecurityMode = wifi_GetParam(obj,paramName)

    print(f"\nTEST STEP {step}: Get the initial security mode")
    print(f"EXPECTED RESULT {step}: Should get the initial security mode")

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Initial security mode is {initialSecurityMode}")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        #Get the initial security configuration
        step = step + 1
        print(f"TEST STEP {step}: Get the initial security configuration")
        print(f"EXPECTED RESULT {step}: Should succesfully get initial security configuration")
        initial_config = {}
        tdkTestObj,actualresult,initial_config = getSecurityModeEnabledConfig(obj, initialSecurityMode, index)

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: Initial security configuration reterived successfully. Initial config values: {initial_config}")
            print("TEST EXECUTION RESULT :SUCCESS")

            if initialSecurityMode == "WPA3-Personal":
                sae_key = f"Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase"
                SAEPass = initial_config.get(sae_key)
            else:
                SAEPass = "test_saepass"

            #Change security mode to Enhanced-Open
            step = step + 1
            paramName = f"Device.WiFi.AccessPoint.{index}.Security.ModeEnabled"
            tdkTestObj,actualresult = wifi_SetParam(obj,paramName,"Enhanced-Open","string")
            sleep(2)

            print(f"TEST STEP {step}: Change security mode to Enhanced-Open")
            print(f"EXPECTED RESULT {step}: Should set security mode to Enhanced-Open")

            if expectedresult in actualresult:
                set_mode = 1
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Set Operation success")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                #Check Security Mode and WPA Config
                step = step + 1
                print(f"TEST STEP {step}: Check security mode and WPA configuration")
                print(f"EXPECTED RESULT {step}: WPA configuration values should be reset when security mode is Enhanced-Open")

                paramName = f"Device.WiFi.AccessPoint.{index}.Security.ModeEnabled"
                tdkTestObj,actualresult,curr_secMode = wifi_GetParam(obj,paramName)
                WPA_config = {}
                tdkTestObj,actualresult1,WPA_config = getSecurityModeEnabledConfig(obj, "WPA3-Personal", index)

                expected_values = ["Enhanced-Open","0.0","AES"]
                actual_values = [curr_secMode,WPA_config.get(f"Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase"),WPA_config.get(f"Device.WiFi.AccessPoint.{index}.Security.X_CISCO_COM_EncryptionMethod")]

                if expectedresult in actualresult and expectedresult in actualresult1 and actual_values == expected_values:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT{step} : Security mode and WPA config values reset successful. WPA Config values: {actual_values}")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    #Change security mode to WPA3-Personal along with WPA config
                    step +=1
                    #test values not real secrets
                    SAE_Pass = "asdf@1234"
                    Encryption_Mode = "AES"
                    config_SET = {
                                f"Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase":SAE_Pass,
                                f"Device.WiFi.AccessPoint.{index}.Security.X_CISCO_COM_EncryptionMethod":Encryption_Mode
                    }
                    tdkTestObj,actualresult = setSecurityModeEnabledConfig(obj, "WPA3-Personal", index, config_SET, curr_secMode)
                    details = tdkTestObj.getResultDetails()
                    sleep(2)

                    print(f"TEST STEP {step}: Set security mode to WPA3-Personal along with WPA Config")
                    print(f"EXPECTED RESULT {step}: Should set security mode to WPA3-Personal along with WPA config")

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Set Operation success")
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        #Check Security Mode and WPA Config
                        step = step + 1

                        print(f"TEST STEP {step}: Check security mode and WPA configuration")
                        print(f"EXPECTED RESULT {step}: Security mode should set to WPA3-Personal and WPA configuration values should be set to new values")

                        paramName = f"Device.WiFi.AccessPoint.{index}.Security.ModeEnabled"
                        tdkTestObj,actualresult,curr_secMode = wifi_GetParam(obj,paramName)
                        WPA_config = {}
                        tdkTestObj,actualresult1,WPA_config = getSecurityModeEnabledConfig(obj, "WPA3-Personal", index)

                        expected_values = ["WPA3-Personal",SAE_Pass,Encryption_Mode]
                        actual_values = [curr_secMode,WPA_config.get(f"Device.WiFi.AccessPoint.{index}.Security.SAEPassphrase"),WPA_config.get(f"Device.WiFi.AccessPoint.{index}.Security.X_CISCO_COM_EncryptionMethod")]

                        if expectedresult in actualresult and expectedresult in actualresult and expected_values == actual_values:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT{step} : Security Mode and WPA Config reterived successfully. WPA Config values: {actual_values}")
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT{step} : Failed to retrive Security Mode and WPA Config or SET values not reflected in GET operation")
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Set Operation Failure")
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT{step}:Failed to get security mode and wpa config")
                    print("[TEST EXECUTION RESULT] : FAILURE")

                #Revert operation
                if set_mode == 1 and (curr_secMode != initialSecurityMode or WPA_config != initial_config):
                    #revert to initial security mode
                    print("Reverting to initial Security Mode...")
                    step += 1
                    tdkTestObj, actualresult = setSecurityModeEnabledConfig(obj, initialSecurityMode, index, initial_config, curr_secMode)
                    details = tdkTestObj.getResultDetails()

                    step += 1
                    print(f"\nTEST STEP {step} : Revert Device.WiFi.AccessPoint.17.Security.ModeEnabled to initial mode : {initialSecurityMode}")
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
                    print("Reverting security mode not requried")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Set Operation Failure")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Failed to retrive Initial security configuration")
            print("TEST EXECUTION RESULT :FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT{step}:Failed to get Initial security mode")
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload wifiagent and sysutil module
    obj.unloadModule("wifiagent")
else:
    print("Failed to load wifiagent module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
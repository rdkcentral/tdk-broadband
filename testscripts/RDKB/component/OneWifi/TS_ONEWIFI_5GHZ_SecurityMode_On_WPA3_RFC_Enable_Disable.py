##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2024 RDK Management
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
  <version>4</version>
  <name>TS_ONEWIFI_5GHZ_SecurityMode_On_WPA3_RFC_Enable_Disable</name>
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Verify that the Security Mode is correctly set when the WPA3 RFC feature is disabled</synopsis>
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
    <box_type>Broadband</box_type>
    <box_type>BPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_ONEWIFI_277</test_case_id>
    <test_objective>Verify Device.WiFi.AccessPoint.2.Security.ModeEnabled when WPA3_Personal_Transition.Enable is set to both true and false.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components in DUT should be in a running state that includes component under test Cable Modem 2. TDK Agent should be in a running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable
Device.WiFi.AccessPoint.2.Security.ModeEnabled</input_parameters>
    <automation_approach>
1.Load the module.
2.Perform Factory Reset on DUT
3.Get WPA3 RFC using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable and security mode using Device.WiFi.AccessPoint.2.Security.ModeEnabled.
4.Enable WPA3 RFC using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable
5.Get WPA3 RFC using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable and security mode using Device.WiFi.AccessPoint.2.Security.ModeEnabled.
6.Disable WPA3 RFC using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable.
7.Unload the module.
    </automation_approach>
    <expected_output>When WPA3_Personal_Transition.Enable is set to true, the security mode for Device.WiFi.AccessPoint.2.Security.ModeEnabled should be "WPA3-Personal-Transition".
    And when WPA3_Personal_Transition.Enable is disabled from enabled state, the security mode should change to "WPA2-Personal"</expected_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_ONEWIFI_5GHZ_SecurityMode_On_WPA3_RFC_Enable_Disable</test_script>
    <skipped></skipped>
    <release_version>M129</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# Import the necessary TDK libraries
import tdklib
from tdkutility import *
from time import sleep;

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent", "1")

# IP and Port of box, No need to change
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_5GHZ_SecurityMode_On_WPA3_RFC_Enable_Disable')

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus)

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    #Step 1: Do a Factory reset on DUT
    #Save the current state before going to reboot
    obj.saveCurrentState()
    paramName_FR = "Device.X_CISCO_COM_DeviceControl.FactoryReset"
    tdkTestObj,actualresult = wifi_SetParam(obj,paramName_FR,"Router,Wifi,VoIP,Dect,MoCA","string")

    print(f"TEST STEP {step}: Initiate factory reset ")
    print(f"EXPECTED RESULT {step}: Should initiate factory reset")

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Factory Reset successfull")
        print("TEST EXECUTION RESULT : SUCCESS")

        #Restore the device state saved before reboot
        obj.restorePreviousStateAfterReboot()
        sleep(180)

        #Step 2: Get WPA3RFC Enable and Security mode
        step = step + 1
        paramNames = [
            "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable",
            "Device.WiFi.AccessPoint.2.Security.ModeEnabled"
        ]
        paramResults = {}
        actualresult_all = []

        for paramName in paramNames:
            tdkTestObj, actualresult, paramValue = wifi_GetParam(obj, paramName)
            actualresult_all.append(actualresult)
            paramResults[paramName] = paramValue

        rfc_wpa3 = paramResults["Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable"]
        securityMode = paramResults["Device.WiFi.AccessPoint.2.Security.ModeEnabled"]

        print(f"TEST STEP {step}: Get the value of WPA3_Personal_Transition.Enable and security mode")
        print(f"EXPECTED RESULT {step}: Value of WPA3_Personal_Transition.Enable should be false and security mode should be WPA2-Personal")

        if "FAILURE" not in actualresult_all and rfc_wpa3 == "false" and securityMode == "WPA2-Personal":
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: WPA3_Personal_Transition.Enable is {rfc_wpa3} and security mode is {securityMode}")
            print("TEST EXECUTION RESULT : SUCCESS")

            #Step 3: Change WPA3_Personal_Transition.Enable to true
            step = step+1
            paramName = "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable"
            tdkTestObj,actualresult = wifi_SetParam(obj,paramName,"true","boolean")
            sleep(2)

            print(f"TEST STEP {step}: Change WPA3_Personal_Transition.Enable to true")
            print(f"EXPECTED RESULT {step}: Should change WPA3_Personal_Transition.Enable to true")

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
                print("TEST EXECUTION RESULT : SUCCESS")

                #Step 4: Get WPA3RFC Enable and Security mode
                step = step + 1
                paramNames = [
                    "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable",
                    "Device.WiFi.AccessPoint.2.Security.ModeEnabled"
                ]
                paramResults = {}
                actualresult_all = []

                for paramName in paramNames:
                    tdkTestObj, actualresult, paramValue = wifi_GetParam(obj, paramName)
                    actualresult_all.append(actualresult)
                    paramResults[paramName] = paramValue

                rfc_wpa3 = paramResults["Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable"]
                securityMode = paramResults["Device.WiFi.AccessPoint.2.Security.ModeEnabled"]

                print(f"TEST STEP {step}: Get the value of WPA3_Personal_Transition.Enable and security mode")
                print(f"EXPECTED RESULT {step}: Value of WPA3_Personal_Transition.Enable should be true and security mode should be WPA3-Personal-Transition")

                if "FAILURE" not in actualresult_all and rfc_wpa3 == "true" and securityMode == "WPA3-Personal-Transition":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: WPA3_Personal_Transition.Enable is {rfc_wpa3} and security mode is {securityMode}")
                    print("TEST EXECUTION RESULT : SUCCESS")

                    #Step 5: Revert WPA3-Personal-Transition to false
                    step = step+1
                    paramName = "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable"
                    tdkTestObj,actualresult = wifi_SetParam(obj,paramName,"false","boolean")
                    sleep(2)

                    print(f"TEST STEP {step}: Revert WPA3_Personal_Transition.Enable to false")
                    print(f"EXPECTED RESULT {step}: Should revert WPA3_Personal_Transition.Enable to false")

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
                        print("TEST EXECUTION RESULT : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: SET operation FAILURE")
                        print("TEST EXECUTION RESULT : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: WPA3_Personal_Transition.Enable is {rfc_wpa3} and security mode is {securityMode}")
                    print("TEST EXECUTION RESULT : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: SET operation FAILURE")
                print("TEST EXECUTION RESULT : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: WPA3_Personal_Transition.Enable is {rfc_wpa3} and security mode is {securityMode}")
            print("TEST EXECUTION RESULT : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Factory Reset FAILURE")
        print("TEST EXECUTION RESULT : FAILURE")

    obj.unloadModule("wifiagent")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

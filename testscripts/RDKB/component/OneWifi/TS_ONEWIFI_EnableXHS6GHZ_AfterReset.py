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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_ONEWIFI_EnableXHS6GHZ_AfterReset</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Test to enable XHS 6GHz SSID after a factory reset and check if status changes to "Up"</synopsis>
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
    <test_case_id>TC_ONEWIFI_294</test_case_id>
    <test_objective>Test to enable XHS 6GHz SSID after a factory reset and check if status changes to "Up"
</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,BPI</test_setup>
    <pre_requisite>1. Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
    2. TDK Agent should be in a running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.SSID.18.Enable
    Device.WiFi.SSID.18.Status
    Device.X_CISCO_COM_DeviceControl.FactoryReset</input_parameters>
    <automation_approch>1.Load the wifiagent module
2.Get and save the current enable state of Device.WiFi.SSID.18.Enable
3.Perform factory reset using Device.X_CISCO_COM_DeviceControl.FactoryReset
4.After factoryreset, check if Device.WiFi.SSID.18.Enable is false
5.If SSID.18 is disabled, set Device.WiFi.SSID.18.Enable to true
6.Verify if Device.WiFi.SSID.18.Status is "Up"
7.Revert Device.WiFi.SSID.18.Enable to original value if necessary
8.Unload the wifiagent module</automation_approch>
    <expected_output>XHS 6GHz SSID should be disabled by default after factory reset,once enabled SSID status should change to "Up".
</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiAgent</test_stub_interface>
    <test_script>TS_ONEWIFI_EnableXHS6GHZ_AfterReset</test_script>
    <skipped></skipped>
    <release_version>M140</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''

# use tdklib library, which provides a wrapper for tdk testcase script
import tdklib
from tdkutility import *
from time import sleep

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent", "1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding Box IP and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_EnableXHS6GHZ_AfterReset')

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus)

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    paramName = "Device.WiFi.SSID.18.Enable"
    tdkTestObj,actualresult,orgState = wifi_GetParam(obj,paramName)
    details = tdkTestObj.getResultDetails()


    print(f"TEST STEP {step}: Get the XHS enable state")
    print(f"EXPECTED RESULT {step}: Should get the XHS enable state")

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Initial XHS state is {orgState}")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        obj.saveCurrentState()

        step += 1
        paramName = "Device.X_CISCO_COM_DeviceControl.FactoryReset"
        tdkTestObj, actualresult = wifi_SetParam(obj,paramName,"Router,Wifi,VoIP,Dect,MoCA","string")
        details = tdkTestObj.getResultDetails()

        print(f"TEST STEP {step}: Initiate factory reset")
        print(f"EXPECTED RESULT {step}: Should initiate factory reset")

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: Factory Reset Success. Details:{details}")
            print("[TEST EXECUTION RESULT] : SUCCESS")

            obj.restorePreviousStateAfterReboot()
            found, tdkTestObj = wait_for_namespace(obj, 6, 30, "Device.WiFi.", expectedresult)

            if found == 1:
                step += 1
                paramName = "Device.WiFi.SSID.18.Enable"
                tdkTestObj,actualresult,curState = wifi_GetParam(obj,paramName)
                details = tdkTestObj.getResultDetails()

                print(f"TEST STEP {step}: Get the XHS enable state after reset")
                print(f"EXPECTED RESULT {step}: Should get the XHS enable state after reset")

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Current XHS state is {curState}")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step += 1
                    print(f"TEST STEP {step}: Check if XHS 6GHZ SSID is disabled after reset")
                    print(f"EXPECTED RESULT {step}: XHS 6GHZ SSID should be disabled after reset")

                    if curState == "false":
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: XHS 6GHZ SSID state is {curState}")
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        step += 1
                        paramName = "Device.WiFi.SSID.18.Enable"
                        tdkTestObj, actualresult = wifi_SetParam(obj,paramName,"true","boolean")
                        details = tdkTestObj.getResultDetails()

                        print(f"TEST STEP {step}: Enable XHS 6GHZ SSID")
                        print(f"EXPECTED RESULT {step}: Should enable XHS 6GHZ SSID")

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: {details}")
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                            sleep(5)
                            step += 1
                            paramName = "Device.WiFi.SSID.18.Status"
                            tdkTestObj,actualresult,status = wifi_GetParam(obj,paramName)

                            print(f"TEST STEP {step}: Check if XHS 6GHZ status is Up")
                            print(f"EXPECTED RESULT {step}: XHS 6GHZ should be Up")

                            if expectedresult in actualresult and "Up" in status:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"ACTUAL RESULT {step}: Status is {status}")
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: Status is {status}")
                                print("[TEST EXECUTION RESULT] : FAILURE")

                            step += 1
                            paramName = "Device.WiFi.SSID.18.Enable"
                            tdkTestObj, actualresult = wifi_SetParam(obj,paramName,orgState,"boolean")
                            details = tdkTestObj.getResultDetails()

                            print(f"TEST STEP {step}: Restore Enable state of XHS 6GHZ")
                            print(f"EXPECTED RESULT {step}: Should restore Enable state of XHS 6GHZ")

                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"ACTUAL RESULT {step}: {details}")
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: {details}")
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: {details}")
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: XHS 6GHZ SSID state is {curState}")
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Failed to get XHS 6GHZ SSID enable state. Details is {details}")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("Device.WiFi. namespace not available after Factory Reset")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: {details}")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to get XHS 6GHZ SSID enable state. Details is {details}")
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("wifiagent")
else:
    print("Failed to load wifi module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

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
  <name>TS_ONEWIFI_6GHzCheckSecurityModeUpdate_OnWPA3PersonalTransitionEnable_Disable</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if Security ModeEnabled is not changed for 6ghz on toggling WPA3-PersonalTransition.</synopsis>
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
    <test_case_id>TC_ONEWIFI_290</test_case_id>
    <test_objective>This test case is to check if ModeEnabled for 6ghz is WPA3-Personal when RFC WPA3-Personal-Transition is disabled and enabled
</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, BPI</test_setup>
    <pre_requisite>1. Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
    2. TDK Agent should be in a running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.X_CISCO_COM_DeviceControl.FactoryReset
    Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable
    Device.WiFi.AccessPoint.17.Security.ModeEnabled</input_parameters>
    <automation_approch>1.Load the module.
2. Get the ModeEnabled using Device.WiFi.AccessPoint.17.Security.ModeEnabled and store it. if ModeEnabled is not WPA3-Personal Set it to WPA3-Personal
3.Get the WPA3-Personal-transition using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable and store it.
4.Set WPA3-Personale-Transition to false if it is enabled.
5. Check if ModeEnabled is WPA3-Personal or not using Device.WiFi.AccessPoint.17.Security.ModeEnabled.
6. Now Set WPA3-Personale-Transition to true.
7. Check if ModeEnabled is WPA3-Personal or not using Device.WiFi.AccessPoint.17.Security.ModeEnabled.
8. Revert to initial values if requried.
9. Unload the module.
</automation_approch>
    <expected_output>when WPA3-Personal-Transiton is disabled or enabled ModeEnabled for 6ghz should be WPA3-Personal
</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiAgent</test_stub_interface>
    <test_script>TS_ONEWIFI_6GHzCheckSecurityModeUpdate_OnWPA3PersonalTransitionEnable_Disable</test_script>
    <skipped></skipped>
    <release_version>M140</release_version>
    <remarks></remarks>
  </test_cases>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
from tdkutility import *


#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1")

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_6GHzCheckSecurityModeUpdate_OnWPA3PersonalTransitionEnable_Disable')

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus)

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1


    print(f"TEST STEP {step}: Initiate factory reset ")
    print(f"EXPECTED RESULT {step}: Should initiate factory reset ")

    #Initiate a device FR
    obj.saveCurrentState()

    tdkTestObj = obj.createTestStep('WIFIAgent_Set')
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.FactoryReset")
    tdkTestObj.addParameter("paramValue","Router,Wifi,VoIP,Dect,MoCA")
    tdkTestObj.addParameter("paramType","string")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    print(f"TEST STEP {step}: Initiate factory reset")
    print(f"EXPECTED RESULT {step}: Should initiate factory reset")

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Factory Reset Success. Details:{details}")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        #Get WPA3-Personal-Transition Enable
        step += 1
        tdkTestObj = obj.createTestStep("WIFIAgent_Get")
        tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()


        print(f"TEST STEP {step}: Get intial WPA3-Personal-transition enable")
        print(f"EXPECTED RESULT {step}: Should get initial WPA3-Personal-transition enable")

        if expectedresult in actualresult and "false" in details:
            initial_wpa3_rfc = details.split("VALUE:")[1].split(' ')[0].split(',')[0]
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: WPA3-Personal-transition is: {initial_wpa3_rfc}")
            print("TEST EXECUTION RESULT :SUCCESS")

            #Get Security Mode
            step +=1
            tdkTestObj = obj.createTestStep("WIFIAgent_Get")
            tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.17.Security.ModeEnabled")
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            print(f"\nTEST STEP {step} : Get the Security Mode using Device.WiFi.AccessPoint.17.Security.ModeEnabled")
            print(f"EXPECTED RESULT {step} : Should successfully get Device.WiFi.AccessPoint.17.Security.ModeEnabled")

            if expectedresult in actualresult and "WPA3-Personal" in details:
                initial_mode = details.split("VALUE:")[1].split(' ')[0].split(',')[0]
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Initial security mode :{initial_mode}")
                print("TEST EXECUTION RESULT :SUCCESS")

                #Now toggle the WPA3-Personal-transition
                step +=1
                tdkTestObj = obj.createTestStep("WIFIAgent_Set")
                tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable")
                tdkTestObj.addParameter("paramValue","true")
                tdkTestObj.addParameter("paramType","bool")
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails()

                print(f"TEST STEP {step}: Set WPA3-Personal-transition enable to true")
                print(f"EXPECTED RESULT {step}: Should set WPA3-Personal-transition enable to true")

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Set operation success. Details:{details}")
                    print("TEST EXECUTION RESULT :SUCCESS")

                    #Get Security mode and check if it is changed or not
                    step +=1
                    tdkTestObj = obj.createTestStep("WIFIAgent_Get")
                    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.17.Security.ModeEnabled")
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    details = tdkTestObj.getResultDetails()

                    print(f"\nTEST STEP {step} : Get the Security Mode using Device.WiFi.AccessPoint.17.Security.ModeEnabled")
                    print(f"EXPECTED RESULT {step} : Should successfully get Device.WiFi.AccessPoint.17.Security.ModeEnabled")

                    if expectedresult in actualresult and "WPA3-Personal" in details:
                        sec_mode = details.split("VALUE:")[1].split(' ')[0].split(',')[0]
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Security mode : {sec_mode}")
                        print("TEST EXECUTION RESULT :SUCCESS")

                        #Revert WPA3-Personal transition to initial value
                        tdkTestObj = obj.createTestStep("WIFIAgent_Set")
                        tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable")
                        tdkTestObj.addParameter("paramValue",initial_wpa3_rfc)
                        tdkTestObj.addParameter("paramType","bool")
                        tdkTestObj.executeTestCase(expectedresult)
                        actualresult = tdkTestObj.getResult()
                        details = tdkTestObj.getResultDetails()

                        print(f"TEST STEP {step}: Revert  WPA3-Personal-transition enable to initial value")
                        print(f"EXPECTED RESULT {step}: Should revert WPA3-Personal-transition enable")

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}:Revert operation success. Details: {details}")
                            print("TEST EXECUTION RESULT :SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: Failed to set WPA3-Personal-transition to initial value. Details: {details}")
                            print("TEST EXECUTION RESULT :FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Get operation failed Details : {details}")
                        print("TEST EXECUTION RESULT :FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Failed to set WPA3-Personal-transition. Details {details}")
                    print("TEST EXECUTION RESULT :FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Get operation failed Details : {details}")
                print("TEST EXECUTION RESULT :FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Failed to get WPA3-Personal-transition. Details: {details} ")
            print("TEST EXECUTION RESULT :FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Factory Reset failed ")
        print("TEST EXECUTION RESULT :FAILURE")

    obj.unloadModule("wifiagent")
else:
    print("Failed to load wifiagent module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

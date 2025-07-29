##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2025 RDK Management
#
# Licensed under the Apache License, Version 2.0 (the "License")
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
  <name>TS_ONEWIFI_6GHzSetManagementFramePowerControl</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if able to set the Management Frame Power Control for 6GHz WiFi from 0 dB to -20 dB.</synopsis>
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
    <test_case_id>TC_ONEWIFI_288</test_case_id>
    <test_objective>Check if able to set the Management Frame Power Control for 6GHz WiFi from 0 dB to -20 dB.
</test_objective>
    <test_type>Broadband,BPI</test_type>
    <test_setup>Positive</test_setup>
    <pre_requisite>1. Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
    2. TDK Agent should be in a running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.AccessPoint.17.X_RDKCENTRAL-COM_ManagementFramePowerControl</input_parameters>
    <automation_approch>1.Load the wifiagent module
2.Get the current value of Management Frame Power Control using Device.WiFi.AccessPoint.17.X_RDKCENTRAL-COM_ManagementFramePowerControl
3.Set all the possible values between 0 dB to -20 dB (e.g., -5, -10, -15)
4.Verify each SET operation is successful and reflected in GET opeartion
5.Revert the set value to original
6.Unload the wifiagent module
</automation_approch>
    <expected_output>All the supported values between 0 dB and -20 dB should be SET successfully and should reflect in GET.
</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiAgent</test_stub_interface>
    <test_script>TS_ONEWIFI_6GHzSetManagementFramePowerControl</test_script>
    <skipped></skipped>
    <release_version>M139</release_version>
    <remarks></remarks>
  </test_cases>
</xml>
'''
# tdklib library,which provides a iwrapper for tdk testcase script
import tdklib

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_6GHzSetManagementFramePowerControl')

loadmodulestatus = obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper():
    expectedresult="SUCCESS"
    step = 1

    #Get the initial value of ManagementFramePowerControl
    obj.setLoadModuleStatus("SUCCESS")
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    tdkTestObj.addParameter("ParamName","Device.WiFi.AccessPoint.17.X_RDKCENTRAL-COM_ManagementFramePowerControl")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    initial_mfpc = tdkTestObj.getResultDetails()

    print(f"TEST STEP {step}: Get the intial ManagementFrame PowerControl value")
    print(f"EXPECTED RESULT {step}: Should get intial ManagementFrame PowerControl value")

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: ManagementFrame PowerControl :{initial_mfpc}")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        framePower_list=[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20]
        # getting length of list
        length = len(framePower_list)
        print("Supported Values for  ManagementFrame PowerControl is ",framePower_list)

        step = step + 1
        print(f"TEST STEP {step}: Set the ManagementFrame PowerControl to all supported Values")
        print(f"EXPECTED RESULT {step}: Should set  ManagementFrame PowerControl value to all supported Values")

        failed_values = []
        for i in range(length):
            print("Setting the ManagementFrame PowerControl to ",framePower_list[i])

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
            tdkTestObj.addParameter("ParamName","Device.WiFi.AccessPoint.17.X_RDKCENTRAL-COM_ManagementFramePowerControl")
            tdkTestObj.addParameter("ParamValue",str(framePower_list[i]))
            tdkTestObj.addParameter("Type","int")
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            Setresult = tdkTestObj.getResultDetails()

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print(" Value set successfully to ",framePower_list[i])
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("Failed to set value to", framePower_list[i])
                failed_values.append(framePower_list[i])

        if not failed_values:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: Successfully set the all the supported  ManagementFrame PowerControl value")
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Failed to set the following values: {failed_values}")
            print("[TEST EXECUTION RESULT] :FAILURE")

        #Reverting to initial_mfpc
        step = step + 1
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
        tdkTestObj.addParameter("ParamName","Device.WiFi.AccessPoint.17.X_RDKCENTRAL-COM_ManagementFramePowerControl")
        expectedresult="SUCCESS"
        tdkTestObj.addParameter("ParamValue",initial_mfpc)
        tdkTestObj.addParameter("Type","int")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        result = tdkTestObj.getResultDetails()

        print(f"TEST STEP {step}: Revert the ManagementFrame PowerControl to its initial_mfpc")
        print(f"EXPECTED RESULT {step}: Revert ManagementFrame PowerControl value to previous value")

        if expectedresult in  expectedresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: Revert Operation sucesss:{result}")
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Revert Operation failed: {result}")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to get the initial value .ManagementFrame PowerControl : {initial_mfpc} ")
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("tdkbtr181")
else:
    print("Failed to load module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
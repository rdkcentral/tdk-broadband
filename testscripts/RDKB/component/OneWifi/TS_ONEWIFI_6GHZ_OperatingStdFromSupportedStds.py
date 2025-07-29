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
  <name>TS_ONEWIFI_6GHZ_OperatingStdFromSupportedStds</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check Device.WiFi.Radio.3.OperatingStandards is a subset of SupportedStandards list</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
    <test_case_id>TC_ONEWIFI_285</test_case_id>
    <test_objective>Check Device.WiFi.Radio.3.OperatingStandards is a subset of SupportedStandards list
</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,BPI</test_setup>
    <pre_requisite>1. Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
    2. TDK Agent should be in a running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.Radio.3.SupportedStandards
    Device.WiFi.Radio.3.OperatingStandards</input_parameters>
    <automation_approch>1. Load the module
2. Get and save Device.WiFi.Radio.3.SupportedStandards.
3. Check if supported standard value has value of ax.
4  Get Device.WiFi.Radio.3.OperatingStandards
5. Check if operating standards are a subset of supported standards
6. Unload wifiagent module
</automation_approch>
    <expected_output>supported standard value for 6ghz should be ax. And Device.WiFi.Radio.3.OperatingStandards is a subset of SupportedStandards list
</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiAgent</test_stub_interface>
    <test_script>TS_ONEWIFI_6GHZ_OperatingStdFromSupportedStds</test_script>
    <skipped></skipped>
    <release_version>M139</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1")

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_6GHZ_OperatingStdFromSupportedStds')

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus)

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS"
    step = 1

    #Get the list of supported security modes
    tdkTestObj = obj.createTestStep('WIFIAgent_Get')
    tdkTestObj.addParameter("paramName","Device.WiFi.Radio.3.SupportedStandards")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()
    expectedBand = "ax"

    print(f"TEST STEP {step}: Get the list of supported standards")
    print(f"EXPECTED RESULT {step}: Should get list of supported standards")

    if expectedresult in actualresult and details != "":
        tdkTestObj.setResultStatus("SUCCESS")
        band = details.split("VALUE:")[1].split(' ')[0]
        print(f"ACTUAL RESULT {step}: Supported Standard is {band}")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        print(f"TEST STEP {step}: Check if supported standards is from expected list of values")
        print(f"EXPECTED RESULT {step}: Supported standards should be from the expected list of values")

        if band == expectedBand:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: Supported Standard is {band} Expected list is  {expectedBand}")
            print("[TEST EXECUTION RESULT] : SUCCESS")

            #Get Operating standard
            step = step + 1
            tdkTestObj = obj.createTestStep('WIFIAgent_Get')
            tdkTestObj.addParameter("paramName","Device.WiFi.Radio.3.OperatingStandards")
            tdkTestObj.executeTestCase("expectedresult")
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            print(f"TEST STEP {step}: Get the current operating standard")
            print(f"EXPECTED RESULT {step}: Should get current operating standard")

            if expectedresult in actualresult and details != "":
                tdkTestObj.setResultStatus("SUCCESS")
                operStd = details.split("VALUE:")[1].split(' ')[0].split(',')
                s_list = band.split(',')
                print(f"ACTUAL RESULT {step}: Operating standard is {operStd}.")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                print(f"TEST STEP {step}: Check if current operating standard is subset of supported standard list")
                print(f"EXPECTED RESULT {step}: current operating standard should be a subset of supported standard list")

                if set(operStd).issubset(set(s_list)):
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Operating standard is {operStd}. Supported standard {band} ")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Operating standard is not subset of Supported standards ")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Get operation Failed. Details {details} ")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Supported standard is not in expected list of value. Details {details} ")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Get operation failed")
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("wifiagent")
else:
    print("Failed to load wifi module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>10</version>
  <name>TS_USPPA_Get_InvalidParameter</name>
  <primitive_test_id/>
  <primitive_test_name>USPPA_Donothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if USP Agent can properly handle a Get message when a single invalid parameter is requested via USP protocol.</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>BPI</box_type>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_USPPA_20</test_case_id>
    <test_objective>This test case is to check if USP Agent can properly handle a Get message when a single invalid parameter is requested via USP protocol.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband,RPI,BPI</test_setup>
    <pre_requisite>1.Ccsp Components should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.USPPA should be enabled
4. USP agent and controller are up and communicating with each other.</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.LocalAgent.InvalidParameter</input_parameters>
    <automation_approch>1. Load sysutil module
2. Check the prerequisite function is success.
3. Configure USP controller to send GET request for invalid parameter.
4. Once request is success, parse the USP response and see if the agent handle invalid parameter gracefully.
5. Unload sysutil module</automation_approch>
    <expected_output>USP Agent should properly handle a Get message when a single invalid parameter is requested with appropriate error message via USP protocol.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_USPPA_Get_InvalidParameter</test_script>
    <skipped>No</skipped>
    <release_version>M141</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from usppaUtility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1")

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_USPPA_Get_InvalidParameter')

#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %result)

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS")

    #Check for prerequisites
    tdkTestObj,agentID,preRequisiteStatus = usppaPreRequisite(obj)
    if "SUCCESS" in preRequisiteStatus:
        #Get an invalid parameter
        print("\nTEST STEP 1:  Send GET request to get an invalid parameter and receive an error response via USP protocol")
        print("EXPECTED RESULT 1: Send GET request to get an invalid parameter and receive an error response via USP protocol")
        queryParam = {"name":"Device.LocalAgent.InvalidParameter"}
        status,queryResponse = usppaQuery(agentID,queryParam)
        if status == 200 :
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT 1: Sent GET request to get an invalid parameter via USP protocol")
            #Parse the response from get operation
            parsedResponse = parseUsppaResponse(queryResponse,"get","negative")
            if parsedResponse and "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                tdkTestObj.setResultStatus("SUCCESS")
                print("Agent handled correctly the GET message to get an invalid parameter via USP protocol")
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("Agent failed to handle the GET message to get an invalid parameter via USP protocol")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            if status == "FAILURE":
                print(" Token Generation failed during get operation")
            print(f"ACTUAL RESULT 1: Failed to send GET request to get invalid parameter via USP protocol with status: {status}")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("Usppa Pre-requisite failed. Please check if usppa processes are running in device or controller setup is ready or agent ID failed to fetch")
        print("[TEST EXECUTION RESULT] : FAILURE")
    obj.unloadModule("sysutil")
else:
    print("FAILURE to load module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading FAILURE")

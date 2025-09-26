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
  <name>TS_USPPA_GetSupportedDM_rootObject_firstlevelonly_false_eventsOnly</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>USPPA_Donothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To send a GET_SUPPORTED_DM request via the USP protocol to retrieve the details of root object, with first_level_only set to false and options like return_params and  return_commands are disabled, and the  return_events as enabled.</synopsis>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_USPPA_28</test_case_id>
    <test_objective>This test case is to send a GET_SUPPORTED_DM request via USP protocol to retrieve the details of root object, with first_level_only set to false and options like return_params and return_commandsare disabled, and the return_events as enabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,BPI</test_setup>
    <pre_requisite>1.Ccsp Components should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.USPPA should be enabled
4.USP agent and controller are up and communicating with each other.</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.</input_parameters>
    <automation_approch>1. Load sysutil module
2. Check the prerequisite function is success.
3. Configure USP controller to send GET_SUPPORTED_DM request for getting the details of root object with first_level_only as false and options like return_params and return_commands are disabled, and return_events as enabled.
4. Once request is success, parse the USP response and get the supported events alone with metadata.
5. Unload sysutil module</automation_approch>
    <expected_output>Should get the supported DM's event details of root object with first_level_only as false and options like return_params and return_commands  are disabled, and  return_events as enabled via USP protocol successfully.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_USPPA_GetSupportedDM_rootObject_firstlevelonly_false_eventsOnly</test_script>
    <skipped>No</skipped>
    <release_version>M141</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
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
obj.configureTestCase(ip,port,'TS_USPPA_GetSupportedDM_rootObject_firstlevelonly_false_eventsOnly')

#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %result)

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS")

    #Check for prerequisites
    tdkTestObj,agentID,preRequisiteStatus = usppaPreRequisite(obj)
    if "SUCCESS" in preRequisiteStatus:
        #Get the GetSupportedDM message using root object with first_level_only as false and and options like return_params and return_commands are disabled and return_events as enabled
        print("\n TEST STEP 1: Send a GET_SUPPORTED_DM request via the USP protocol to retrieve the supported data model details of root object, with first_level_only set to false and options like return_params and return_commands are disabled, and return_events as enabled")
        print("EXPECTED RESULT 1: Send a GET_SUPPORTED_DM request via the USP protocol to retrieve the supported data model details of the root object, with first_level_only set to false and options like return_params and return_commands are disabled, and return_events as enabled successfully")
        queryParam = {"name":"Device.","first_level_only" :"false","ret_param":"false","ret_cmd":"false","ret_event":"true"}
        status,queryResponse = usppaQuery(agentID,queryParam,"get_supported_dm")
        if status == 200:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT 1 : Sent a GET_SUPPORTED_DM request to retrieve the supported data model details of root object, with first_level_only set to false and options like return_params and return_commands are disabled, and return_events as enabled via the USP protocol successfully \n")
            #Parse the response from get_supported_dm operation
            parsedResponse = parseUsppaResponse(queryResponse,"get_supported_dm")
            if "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                tdkTestObj.setResultStatus("SUCCESS")
                print("Agent correctly processed correctly formatted fields for events when getSupported DM message sent with return_events only enabled successfully")
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("Agent failed to process the getSupported DM message sent with return_events only enabled")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT 1 : Failed to send a GET_SUPPORTED_DM request to retrieve the supported data model details of root object, with first_level_only set to false and options like return_params and return_commands are disabled, and return_events as enabled via USP protocol with status: {status}")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("Usppa Pre-requisite failed. Please check if usppa processes are running in device or controller setup is ready or agent ID failed to fetch \n")
        print("[TEST EXECUTION RESULT] : FAILURE")
    obj.unloadModule("sysutil")
else:
    print("FAILURE to load module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading FAILURE")

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
  <version>9</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_USPPA_AddDelete_ValidSubscription_allowpartial_true</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>USPPA_Donothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Send ADD message to add a valid agent subscription and DELETE message to delete the subscription with allow_partial as true and receive valid response via USP protocol</synopsis>
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
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
    <box_type>BPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_USPPA_17</test_case_id>
    <test_objective>This testcase is to send ADD message to add a valid agent subscription and DELETE message to delete the subscription with allow_partial as true and receive valid response via USP protocol</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,BPI</test_setup>
    <pre_requisite>1.Ccsp Components should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.USPPA should be enabled
4. USP agent and controller are up and communicating with each other.</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.LocalAgent.Subscription.</input_parameters>
    <automation_approch>1. Load sysutil module
2. Check the prerequisite function is success.
3. Configure USP controller to send ADD request for adding a valid Device.LocalAgent.Subscription. with allow_partial as true
4. Once request is success, save the instance number and parameters. Get the details of the newly added subscription instance via USP protocol.
5. Compare the parameter values from ADD and GET request. If success, it confirms the subscription is successfully added.
6.Delete the subscription with allow_partial as true and parse the response to confirm deletion.
7. Unload sysutil module</automation_approch>
    <expected_output>Should Add and delete a valid agent subscription successfully via USP protocol.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_USPPA_AddDelete_ValidSubscription_allowpartial_true</test_script>
    <skipped>No</skipped>
    <release_version>M140</release_version>
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
obj.configureTestCase(ip,port,'TS_USPPA_AddDelete_ValidSubscription_allowpartial_true')

#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult()

print("[LIB LOAD STATUS]  :  %s" %result)

if "SUCCESS" in result.upper():
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS")

    #Check for prerequisites
    tdkTestObj,agentID,preRequisiteStatus = usppaPreRequisite(obj)
    if "SUCCESS" in preRequisiteStatus:
        #Send ADD message request to add a valid Agent subscription
        print("\nTEST STEP 1: Send ADD message request to add a valid Agent subscription with allow_partial as true and receive valid response via USP protocol")
        print("EXPECTED RESULT 1: Send ADD message request to add a valid Agent subscription with allow_partial as true and receive valid response successfully via USP protocol")
        queryParam = {"name":"Device.LocalAgent.Subscription.","allow_partial":"true"}
        status,queryResponse = usppaQuery(agentID,queryParam,"add")
        if status == 200:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT 1: Send ADD message request to add a valid Agent subscription with allow_partial as true successfully via USP protocol")
            #Parse the response from ADD operation
            parsedResponse = parseUsppaResponse(queryResponse,"add")
            if "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                instanceNumber = parsedResponse[1]["instance_number"]
                params = parsedResponse[1]["params"]
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT 1: Agent correctly processed the ADD request to add a valid Agent Subscription with allow_partial as true successfully via USP protocol")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                #Get the details of newly added valid agent subscription
                print("\nTEST STEP 2: Send GET message request to get newly added valid Agent subscription details via USP protocol")
                print("EXPECTED RESULT 2: Send GET message request to get newly added valid Agent subscription details successfully via USP protocol")
                queryParam = {"name":f"Device.LocalAgent.Subscription.{instanceNumber}."}
                status,queryResponse = usppaQuery(agentID,queryParam)
                if status == 200:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT 2: Got the Valid Agent Subscription successfully via USP protocol")
                    #Parse the response from GET operation
                    parsedResponse = parseUsppaResponse(queryResponse)
                    if "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                        tdkTestObj.setResultStatus("SUCCESS")
                        getParams = parsedResponse[1]
                        print("Agent correctly processed GET request to get details of newly added valid Agent Subscription successfully via USP protocol")
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        print("\nTEST STEP 3: Check if the parameter values parsed from ADD request and GET request matches")
                        print("EXPECTED RESULT 3: Check if the parameter values parsed from ADD request and GET request matches successfully")
                        if getParams and params:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("Parameter list from ADD request and GET request is not empty")
                            mismatch = 0
                            for k, v in params.items():
                                if k in getParams and getParams[k] != v:
                                    mismatch = 1
                                    break
                            if mismatch == 0:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT 3: Parameter values parsed from ADD request and GET request matches successfully")
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT 3: Parameter values parsed from ADD request and GET request mismatches")
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("Parameter list from ADD request or GET request is empty")
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("Agent failed to GET request to get details of newly added valid Agent Subscription via USP protocol")
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    if status == "FAILURE":
                        print(" Token Generation failed during GET operation")
                    print(f"ACTUAL RESULT 1: Failed to get valid Agent Subscription via USP protocol with status: {status}")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("Agent failed to ADD request to add valid Agent Subscription with allow_partial as true via USP protocol")
                print("[TEST EXECUTION RESULT] : FAILURE")

            #Delete the newly added valid agent subscription
            print("\nTEST STEP 4: Send DELETE message request to delete newly added valid Agent subscription with allow_partial as true via USP protocol")
            print("EXPECTED RESULT 4: Send DELETE message request to delete newly added valid Agent subscription with allow_partial as true successfully via USP protocol")
            queryParam = {"name":f"Device.LocalAgent.Subscription.{instanceNumber}.","allow_partial":"true"}
            status,queryResponse = usppaQuery(agentID,queryParam,"delete")
            if status == 200:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT 4: Sent DELETE message request to delete newly added valid Agent subscription with allow_partial as true successfully via USP protocol")
                #Parse the response from DELETE operation
                parseResponse = parseUsppaResponse(queryResponse,"delete")
                if "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("Confirmed the deletion of Agent Subscription from USP response successfully")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("Failed to confirm the deletion of Agent Subscription from USP response")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT 4: Failed to Send DELETE message to delete newly added valid Agent subscription with allow_partial as true via USP protocol with status: {status}")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            if status == "FAILURE":
                print(" Token Generation failed during ADD operation")
            print(f"ACTUAL RESULT 1: Failed to add a valid Agent Subscription with allow_partial as true via USP protocol with status: {status}")
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

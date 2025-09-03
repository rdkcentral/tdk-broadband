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
  <version>25</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_USPPA_SetControllerPeriodicNotifInterval</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>USPPA_Donothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To send SET request to set the Controller PeriodicNotifInterval and receive a valid response via USP protocol</synopsis>
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
    <test_case_id>TC_USPPA_4</test_case_id>
    <test_objective>This test case is to send SET request to set the Controller PeriodicNotifInterval and receive a valid response via USP protocol</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,BPI</test_setup>
    <pre_requisite>1.Ccsp Components should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.USPPA should be enabled
4. USP agent and controller are up and communicating with each other.</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.LocalAgent.Controller.1.PeriodicNotifInterval</input_parameters>
    <automation_approch>1. Load sysutil module
2. Check the prerequisite function is success.
3. Configure USP controller to send GET request for Device.LocalAgent.Controller.1.PeriodicNotifInterval
4. Once request is success, parse the USP response and get the current controller PeriodicNotifInterval value.
5.  Configure USP controller to send a SET request for setting controller PeriodicNotifInterval  to another value.
 6.  Once request is success, parse the USP response and get the new controller PeriodicNotifInterval  value.
7. Check if new value matches with set value.
8. Revert the controller PeriodicNotifInterval  value to original value via  USP protocol.
9. Unload sysutil module</automation_approch>
    <expected_output>Controller PeriodicNotifInterval value should be set to another value successfully via USP protocol</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_USPPA_SetControllerPeriodicNotifInterval</test_script>
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
obj.configureTestCase(ip,port,'TS_USPPA_SetControllerPeriodicNotifInterval')

#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult()

print("[LIB LOAD STATUS]  :  %s" %result)

if "SUCCESS" in result.upper():
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS")

    #Check for prerequisites
    tdkTestObj,agentID,preRequisiteStatus = usppaPreRequisite(obj)
    if "SUCCESS" in preRequisiteStatus:
        #get the current Controller PeriodicNotifInterval
        print("\nTEST STEP 1: Send GET request to get the current Controller PeriodicNotifInterval and receive a valid response via USP protocol")
        print("EXPECTED RESULT 1: Send GET request to get current Controller PeriodicNotifInterval and receive a valid response successfully via USP protocol")
        queryParam = {"name":"Device.LocalAgent.Controller.1.PeriodicNotifInterval"}
        status,queryResponse = usppaQuery(agentID,queryParam)
        if status == 200:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT 1: Sent GET request to get the Controller PeriodicNotifInterval  successfully via USP protocol")
            #Parse the response from get operation
            parsedResponse = parseUsppaResponse(queryResponse)
            if "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                tdkTestObj.setResultStatus("SUCCESS")
                orgControllerPeriodicNotifInterval = parsedResponse[1]
                print(" Got the Controller PeriodicNotifInterval as %s successfully via USP protocol" %orgControllerPeriodicNotifInterval)
                print("[TEST EXECUTION RESULT] : SUCCESS")

                #set the Controller PeriodicNotifInterval
                if orgControllerPeriodicNotifInterval == "600":
                    newControllerPeriodicNotifInterval = "700"
                else:
                    newControllerPeriodicNotifInterval = "600"
                #set the Controller PeriodicNotifInterval
                print("\n TEST STEP 2:  Send SET request to set %s as new Controller PeriodicNotifInterval via USP protocol " %newControllerPeriodicNotifInterval)
                print("EXPECTED RESULT 2: Send SET request to set %s as new Controller PeriodicNotifInterval successfully via USP protocol" %newControllerPeriodicNotifInterval)
                queryParam = {"name":"Device.LocalAgent.Controller.1.PeriodicNotifInterval","value":newControllerPeriodicNotifInterval}
                status,queryResponse = usppaQuery(agentID,queryParam,"set")
                if status == 200 :
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT 2: Send SET request to set Controller PeriodicNotifInterval successfully via USP protocol")
                    #Parse the response from set operation
                    parsedResponse = parseUsppaResponse(queryResponse,"set")
                    if "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                        tdkTestObj.setResultStatus("SUCCESS")
                        setControllerPeriodicNotifInterval = parsedResponse[1]
                        print(" Agent processed correctly the SET request to set the Controller PeriodicNotifInterval as %s successfully via USP protocol" %setControllerPeriodicNotifInterval)
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        #Check if set and get value of Controller PeriodicNotifInterval matches
                        print("\nTEST STEP 3: Check if set and get value of Controller PeriodicNotifInterval matches")
                        print("EXPECTED RESULT 3: Set and get value of Controller PeriodicNotifInterval should match")
                        print("Send GET request to get the current Controller PeriodicNotifInterval via USP protocol")
                        queryParam = {"name":"Device.LocalAgent.Controller.1.PeriodicNotifInterval"}
                        status,queryResponse = usppaQuery(agentID,queryParam)
                        if status == 200:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("Sent GET request to get Controller PeriodicNotifInterval successfully via USP protocol")
                            #Parse the response from get operation
                            parsedResponse = parseUsppaResponse(queryResponse)
                            if "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                                tdkTestObj.setResultStatus("SUCCESS")
                                getControllerPeriodicNotifInterval = parsedResponse[1]
                                print("Got  Controller PeriodicNotifInterval  as %s successfully via USP protocol" %getControllerPeriodicNotifInterval)
                                if setControllerPeriodicNotifInterval == getControllerPeriodicNotifInterval:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print("ACTUAL RESULT 3 : Set and get value of Controller PeriodicNotifInterval  matches")
                                    print("[TEST EXECUTION RESULT] : SUCCESS")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("ACTUAL RESULT 3 : Set and get value of Controller PeriodicNotifInterval mismatch")
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("Failed to get Controller PeriodicNotifInterval via USP protocol")
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            if status == "FAILURE":
                                print(" Token Generation failed during get operation of get and set value check")
                            print(f"Failed to fetch the get value of Controller PeriodicNotifInterval via USP protocol with status: {status} ")
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(" Agent failed to process the SET request to set the Controller PeriodicNotifInterval  via USP protocol")
                        print("[TEST EXECUTION RESULT] : FAILURE")

                    #Revert to original value
                    print("\nTEST STEP 4: Revert to the original value of Controller PeriodicNotifInterval as %s via USP protocol" %orgControllerPeriodicNotifInterval)
                    print("EXPECTED RESULT 4: The value of Controller PeriodicNotifInterval should be reverted successfully via USP protocol")
                    queryParam = {"name":"Device.LocalAgent.Controller.1.PeriodicNotifInterval","value":orgControllerPeriodicNotifInterval}
                    status,queryResponse = usppaQuery(agentID,queryParam,"set")
                    if status == 200 :
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT 4: Sent SET request to revert the Controller PeriodicNotifInterval successfully via USP protocol")
                        #Parse the response from get operation
                        parsedResponse = parseUsppaResponse(queryResponse,"set")
                        if "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                            tdkTestObj.setResultStatus("SUCCESS")
                            getControllerPeriodicNotifInterval = parsedResponse[1]
                            print("Reverted Controller PeriodicNotifInterval as %s successfully via USP protocol" %getControllerPeriodicNotifInterval)
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("Failed to get Controller PeriodicNotifInterval via USP protocol")
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        if status == "FAILURE":
                            print(" Token Generation failed during revert operation")
                        print(f" ACTUAL RESULT 4: The revert operation returned failure via USP protocol with status: {status}")
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT 2: Failed to send SET request to set Controller PeriodicNotifInterval via USP protocol with status: {status}")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("Failed to get Controller PeriodicNotifInterval via USP protocol")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            if status == "FAILURE":
                print(" Token Generation failed during get operation")
            print(f"ACTUAL RESULT 1: Failed to fetch the get value of Controller PeriodicNotifInterval via USP protocol with status: {status}")
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

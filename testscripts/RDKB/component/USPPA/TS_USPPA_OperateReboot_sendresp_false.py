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
  <version>19</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_USPPA_OperateReboot_sendresp_false</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>USPPA_Donothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Send OPERATE message to reboot the EUT with send_resp set to false, receives no valid response and resumes connectivity with the test system via USP protocol.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>20</execution_time>
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
    <test_case_id>TC_USPPA_10</test_case_id>
    <test_objective>This test case is to send OPERATE message to reboot the EUT with send_resp set to false, receives no valid response backand resumes connectivity with the test system via USP protocol.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,BPI</test_setup>
    <pre_requisite>1.Ccsp Components should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.USPPA should be enabled
4. USP agent and controller are up and communicating with each other.</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.Reboot()
Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason</input_parameters>
    <automation_approch>1. Load sysutil module
2. Check the prerequisite function is success.
3. Configure USP controller to send OPERATE request for rebooting the EUT via Device.Reboot() with send_resp set to false.
4. Once request is success with no valid response, wait for the device to come up.
5.Query the last reboot reason to confirm the EUT's reboot, and controller-agent connection restored via USP protocol.
6. Unload sysutil module</automation_approch>
    <expected_output>The EUT reboots with no response and resumes connectivity with the test system successfully via USP protocol.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_USPPA_OperateReboot_sendresp_false</test_script>
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
import time

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1")

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_USPPA_OperateReboot_sendresp_false');

#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %result)

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS")

    #Check for prerequisites
    tdkTestObj,agentID,preRequisiteStatus = usppaPreRequisite(obj)
    if "SUCCESS" in preRequisiteStatus:
        #Send operate message to reboot the EUT
        print("TEST STEP 1: Send operate message to reboot the EUT with send_resp set to false and receive no valid response back via USP protocol")
        print("EXPECTED RESULT 1: Send operate message to reboot the EUT with send_resp set to false successfully and receive no valid response back via USP protocol")
        queryParam = {"name":"Device.Reboot()", "send_resp":"false"}

        #save device's current state before it goes for reboot
        obj.saveCurrentState()
        status,queryResponse = usppaQuery(agentID,queryParam,"operate")
        if status == 504 and "usp message response timeout" in str(queryResponse):
            #Restore the device state saved before reboot
            obj.restorePreviousStateAfterReboot()
            #Wait upto 5 min to establish connection between controller and agent
            print("Sleeping for 300s")
            time.sleep(300)

            print("\n Checking PREREQUISITES after Reboot \n")
            tdkTestObj,agentID,preRequisiteStatus = usppaPreRequisite(obj)
            if "SUCCESS" in preRequisiteStatus:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT 1: Sent operate message to reboot the EUT with send_resp set to false successfully and received USP message timeout via USP protocol")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                #Check if EUT is rebooted successfully
                print("\nTEST STEP 2 : Check if the EUT is actually rebooted and controller-agent connection restored by checking the last reboot reason via USP protocol")
                print("EXPECTED RESULT 2: Get the last reboot reason as usp-reboot to confirm the EUT's reboot and controller-agent connection restored successfully via USP protocol")
                queryParam = {"name":"Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason"}
                status,queryResponse = usppaQuery(agentID,queryParam)
                if status == 200:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(" Got the last reboot reason successfully via USP protocol")
                    #Parse the response from get operation
                    parsedResponse = parseUsppaResponse(queryResponse)
                    if "SUCCESS" in parsedResponse[0] and parsedResponse[1]=="usp-reboot":
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT 2: Got the last reboot reason as %s confirmed the EUT's reboot and controller-agent connection restored successfully via USP protocol" %parsedResponse[1])
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT 2: Got a different last reboot reason as %s  than expected but controller-agent connection restored via USP protocol" %parsedResponse[1])
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    if status == "FAILURE":
                        print("Token Generation failed during get operation")
                    print(f"Failed to get the last reboot reason and controlller-agent connection is not restored via USP protocol with status: {status}")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("Usppa Pre-requisite failed after Reboot of EUT. Please check if usppa processes are running in device or controller setup is ready or agent ID failed to fetch")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            if status == "FAILURE":
                print(" Token Generation failed")
            print(f"ACTUAL RESULT 1: Failed to send operate message to reboot the EUT with send_resp set to false via USP protocol with status: {status}")
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

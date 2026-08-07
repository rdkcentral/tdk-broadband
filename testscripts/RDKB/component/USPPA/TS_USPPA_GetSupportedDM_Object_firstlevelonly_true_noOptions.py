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
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from usppaUtility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1")

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_USPPA_GetSupportedDM_Object_firstlevelonly_true_noOptions')

#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %result)

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS")

    #Check for prerequisites
    tdkTestObj,agentID,preRequisiteStatus = usppaPreRequisite(obj)
    if "SUCCESS" in preRequisiteStatus:
        #Get the GetSupportedDM message of single object with first_level_only as true and and options like return_params, return_commands and return_events are disabled
        print("\n TEST STEP 1: Send a GET_SUPPORTED_DM request to retrieve the supported data model details of single object, with first_level_only set to true and options like return_params, return_commands and return_events are disabled via USP protocol")
        print("EXPECTED RESULT 1: Send a GET_SUPPORTED_DM request to retrieve the supported data model details of a single object, with first_level_only set to true and options like return_params, return_commands and return_events are disabled via USP protocol successfully")
        queryParam = {"name":"Device.LocalAgent.","first_level_only":"true","ret_param":"false","ret_cmd":"false","ret_event":"false"}
        status,queryResponse = usppaQuery(agentID,queryParam,"get_supported_dm")
        if status == 200:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT 1 : Sent a GET_SUPPORTED_DM request to retrieve the supported data model details of single object, with first_level_only set to true and options like return_params, return_commands and return_events are disabled via USP protocol\n")
            #Parse the response from get_supported_dm operation
            parsedResponse = parseUsppaResponse(queryResponse,"get_supported_dm")
            if "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                tdkTestObj.setResultStatus("SUCCESS")
                print("Agent correctly processed the get_supported_dm message of a single object with first_level_only set to true and options like return_params, return_commands and return_events are disabled successfully")
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("Agent failed to process the get_supported_dm message for a single object with first_level_only set to true and options like return_params, return_commands and return_events are disabled")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT 1 : Failed to send GET_SUPPORTED_DM request to get the SupportedDM message for single object with first_level_only set to true and options like return_params, return_commands and return_events are disabled via USP protocol with status: {status}")
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

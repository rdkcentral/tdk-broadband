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
obj.configureTestCase(ip,port,'TS_USPPA_GetControllerObjectPath')

#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %result)

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS")

    #Check for prerequisites
    tdkTestObj,agentID,preRequisiteStatus = usppaPreRequisite(obj)
    if "SUCCESS" in preRequisiteStatus:
        #Get the Agent's Instantiated Controller Data Model
        print("\nTEST STEP 1:  Send GET request to get Agent's Instantiated Controller Data Model when an object path is specified and receive a valid response via USP protocol")
        print("EXPECTED RESULT 1: Send GET request to get Agent's Instantiated Controller Data Model when an object path is specified and receive a valid response via USP protocol successfully");
        queryParam = {"name":"Device.LocalAgent.Controller."}
        status,queryResponse = usppaQuery(agentID,queryParam)
        if status == 200 :
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT 1: Sent GET request to get Agent's Instantiated Controller Data Model when an object path is specified via USP protocol successfully")
            #Parse the response from get operation
            parsedResponse = parseUsppaResponse(queryResponse)
            if "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                tdkTestObj.setResultStatus("SUCCESS")
                for param, value in  parsedResponse[1].items():
                    print(f"Parameter: {param}, Value: {value}")

                print("Agent processed correctly the GET message to get Agent's Instantiated Controller Data Model when an object path is specified via USP protocol")
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("Agent failed to process the GET message to get Agent's Instantiated Controller Data Model when an object path is specified via USP protocol")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            if status == "FAILURE":
                print(" Token Generation failed during get operation")
            print(f"ACTUAL RESULT 1: Failed to send GET request to get Agent's Instantiated Controller Data Model when an object path is specified via USP protocol with status: {status}")
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

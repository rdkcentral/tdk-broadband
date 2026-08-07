##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
from webpaUtility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WEBPA_SetBandSteeringCapability');

#Get the result of connection with test component and STB
result =obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %result);

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj,preRequisiteStatus = webpaPreRequisite(obj);
    if "SUCCESS" in preRequisiteStatus:
        print("\nTEST STEP 1: Get and save the current BandSteering capability")
        print("EXPECTED RESULT 1: Should get the current BandSteering capability")
        queryParam = {"name":"Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability"}
        queryResponse = webpaQuery(obj, queryParam)
        parsedResponse = parseWebpaResponse(queryResponse, 1)
        print("parsedResponse : %s" %parsedResponse);
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.executeTestCase("SUCCESS");
        if "SUCCESS" in parsedResponse[0] and parsedResponse[1] != "":
            tdkTestObj.setResultStatus("SUCCESS");
            orgValue = parsedResponse[1];
            print("ACTUAL RESULT 1: Got the current BandSteering capability as ",orgValue)
            print("[TEST EXECUTION RESULT] : SUCCESS")
            if orgValue == "true":
                newValue = "false"
            else:
                newValue = "true"
            print(f"\nTEST STEP 2: Set the BandSteering Capability to {newValue}")
            print(f"EXPECTED RESULT 2: Should set the  BandSteering Capability to {newValue}")
            queryParam = {"name":"Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability","value":newValue,"dataType":3}
            queryResponse = webpaQuery(obj, queryParam, "set")
            parsedResponse = parseWebpaResponse(queryResponse, 1, "set")
            tdkTestObj.executeTestCase("SUCCESS");
            if "FAILURE" in parsedResponse[0] and "520" in queryResponse:
                tdkTestObj.setResultStatus("SUCCESS");
                print(f"ACTUAL RESULT 2: BandSteering Capability is not set to {newValue}");
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print(f"ACTUAL RESULT 2: BandSteering Capability is set to {newValue}");
                print("[TEST EXECUTION RESULT] : FAILURE")

                print("\nTEST STEP 3: Revert the Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability to original value")
                print("EXPECTED RESULT 3: Should revert the Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability to original value")
                queryParam = {"name":"Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability","value":orgValue,"dataType":3}
                queryResponse = webpaQuery(obj, queryParam, "set")
                parsedResponse = parseWebpaResponse(queryResponse, 1, "set")
                tdkTestObj.executeTestCase("SUCCESS");
                if "SUCCESS" in parsedResponse[0] and parsedResponse[1] != "":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("ACTUAL RESULT 3: Reverted the Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability to original value")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("ACTUAL RESULT 3: Failed to revert the Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability to original value")
                    print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print("ACTUAL RESULT 1: Failed to get the current BandSteering capability")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print("Webpa Pre-requisite failed. Please check parodus and webpa processes are running in device")

    obj.unloadModule("sysutil");
else:
    print("FAILURE to load module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading FAILURE");
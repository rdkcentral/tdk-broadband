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
import time;
from webpaUtility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WEBPA_2.4GHzMACFilterEnable');

#Get the result of connection with test component and STB
result =obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %result);

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj,preRequisiteStatus = webpaPreRequisite(obj);
    if "SUCCESS" in preRequisiteStatus:
        #get the current state
        print("\nTEST STEP 1: Get and save the state of Mac Filter for 2.4GHz")
        print("EXPECTED RESULT 1: should get the state of Mac Filter for 2.4GHz")
        queryParam = {"name":"Device.WiFi.AccessPoint.10001.X_CISCO_COM_MACFilter.Enable"}
        queryResponse = webpaQuery(obj,queryParam)
        parsedResponse = parseWebpaResponse(queryResponse, 1)
        print("parsedResponse : %s" %parsedResponse);
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.executeTestCase("SUCCESS");
        #Checking if the response value is not null
        if "SUCCESS" in parsedResponse[0] and parsedResponse[1] != "":
            tdkTestObj.setResultStatus("SUCCESS");
            OrgValue = parsedResponse[1];
            print("ACTUAL RESULT 1: Mac Filter for 2.4 GHz's State: ",OrgValue);
            print("[TEST EXECUTION RESULT] : SUCCESS")
            #toggling by using set
            print("\nTEST STEP 2: Toggle the value of Mac Filter Enable for 2.4GHz")
            print("EXPECTED RESULT 2: Should toggle the value of Mac Filter Enable for 2.4GHz")
            if parsedResponse[1] == "false":
                flag="true"
            else:
                flag="false"
            queryParam = {"name":"Device.WiFi.AccessPoint.10001.X_CISCO_COM_MACFilter.Enable","value":flag,"dataType":3}
            queryResponse = webpaQuery(obj, queryParam,"set")
            setResponse = parseWebpaResponse(queryResponse, 1,"set")
            tdkTestObj.executeTestCase("SUCCESS");
            if "SUCCESS" in setResponse[0] and setResponse[1] != "":
                tdkTestObj.executeTestCase("SUCCESS")
                print("ACTUAL RESULT 2: Toggled the value of MAC Filter Enable for 2.4GHz")
                print("[TEST EXECUTION RESULT] : SUCCESS")
                time.sleep(30)
                #getting the set value which is toggled
                print("\nTEST STEP 3: Get the value of MAC Filter Enable for 2.4GHz after toggle")
                print("EXPECTED RESULT 3: Should get the value of MAC Filter Enable for 2.4GHz after toggle")
                queryParam = {"name":"Device.WiFi.AccessPoint.10001.X_CISCO_COM_MACFilter.Enable"}
                queryResponse = webpaQuery(obj, queryParam)
                getResponse = parseWebpaResponse(queryResponse, 1)
                tdkTestObj.executeTestCase("SUCCESS");
                #check for successful set
                if "SUCCESS" in getResponse[0] and getResponse[1] != "" and getResponse[1]== flag:
                    tdkTestObj.setResultStatus("SUCCESS");
                    Value = parsedResponse[1];
                    print("ACTUAL RESULT 3: Got the value of MAC Filter Enable for 2.4GHz after toggle as ",Value);
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("ACTUAL RESULT 3: Failed to get the value of MAC Filter Enable for 2.4GHz after toggle")
                    print("[TEST EXECUTION RESULT] : FAILURE")

                #Setting back to original
                print("\nTEST STEP 4: Setting back the value of MAC Filter Enable for 2.4GHz to original value")
                print("EXPECTED RESULT 4: Should set back the value of MAC Filter Enable for 2.4GHz to original value")
                queryParam = {"name":"Device.WiFi.AccessPoint.10001.X_CISCO_COM_MACFilter.Enable","value":OrgValue,"dataType":3}
                queryResponse = webpaQuery(obj, queryParam,"set")
                setResponse = parseWebpaResponse(queryResponse, 1,"set")
                tdkTestObj.executeTestCase("SUCCESS");
                if "SUCCESS" in setResponse[0] and setResponse[1] != "":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("ACTUAL RESULT 4: Revert operation is successful")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("ACTUAL RESULT 4: Revert operation failed")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print("ACTUAL RESULT 2: Failed to toggle MAC Filter Enable for 2.4GHz")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print("ACTUAL RESULT 1: Failed to get MAC Filter Enable for 2.4GHz")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print("Webpa Pre-requisite failed. Please check parodus and webpa processes are running in device")
    obj.unloadModule("sysutil");
else:
    print("FAILURE to load module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading FAILURE");
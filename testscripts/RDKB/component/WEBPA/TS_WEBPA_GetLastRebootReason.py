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
obj.configureTestCase(ip,port,'TS_WEBPA_GetLastRebootReason');

#Get the result of connection with test component and STB
result =obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %result);

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj,preRequisiteStatus = webpaPreRequisite(obj);
    if "SUCCESS" in preRequisiteStatus:
        #set RebootDevice value
        print("\nTEST STEP 1: Reboot the device via webpa ")
        print("EXPECTED RESULT 1: Should reboot the device via webpa")
        queryParam = {"name":"Device.X_CISCO_COM_DeviceControl.RebootDevice","value":"Device","dataType":0}
        #save device's current state before it goes for reboot
        obj.saveCurrentState()
        queryResponse = webpaQuery(obj, queryParam, "set")
        parsedResponse = parseWebpaResponse(queryResponse, 1,"set")
        tdkTestObj.executeTestCase("SUCCESS");
        if "SUCCESS" in parsedResponse[0] and parsedResponse[1] != "":
            #Restore the device state saved before reboot
            obj.restorePreviousStateAfterReboot()
            tdkTestObj.setResultStatus("SUCCESS");
            print("ACTUAL RESULT 1: Rebooted the device : %s" %parsedResponse);
            print("[TEST EXECUTION RESULT] : SUCCESS")
            #get the last Reboot Reason
            print("\nTEST STEP 2: Check if the the last Reboot Reason value is 'webpa-reboot'")
            print("EXPECTED RESULT 2: Should get the Last Reboot reason as 'webpa-reboot'")
            queryParam = {"name":"Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason"}
            queryResponse = webpaQuery(obj, queryParam)
            parsedResponse = parseWebpaResponse(queryResponse, 1)
            tdkTestObj.executeTestCase("SUCCESS");
            if "SUCCESS" in parsedResponse[0] and parsedResponse[1] != "":
                RebootReason= parsedResponse[1];
                print("ACTUAL RESULT 2: Last Reboot Reason is : ", RebootReason)
                if RebootReason == "webpa-reboot":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("Got the Last Reboot reason as 'webpa-reboot'")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("Failed to get the Last Reboot reason as 'webpa-reboot'")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print("ACTUAL RESULT 2: Failed to get the last reboot reason")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print("ACTUAL RESULT 1: Failed to reboot the device via webpa")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print("Webpa Pre-requisite failed. Please check parodus and webpa processes are running in device")
    obj.unloadModule("sysutil");
else:
    print("FAILURE to load module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading FAILURE");
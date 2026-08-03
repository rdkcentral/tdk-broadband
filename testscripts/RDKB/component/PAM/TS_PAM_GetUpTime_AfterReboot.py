##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_GetUpTime_AfterReboot');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus);

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.UpTime");
    expectedresult="SUCCESS";

    #Execute the test case in STB
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print("TEST STEP 1 :Get the uptime before reboot");
        print("EXPECTED RESULT 1 : Should return the uptime successfully");
        print("ACTUAL RESULT 1 : UpTime before reboot is %s" %details);
        #rebooting the device
        obj.initiateReboot();
        sleep(300)
        #checking the uptime after reboot
        tdkTestObj = obj.createTestStep('pam_GetParameterValues');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.UpTime");
        #Execute the test case in STB
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        afterdetails = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            if int(details)>=int(afterdetails):
                print("TEST STEP 2: compare the uptime before and after reboot");
                print("EXPECTED RESULT 2 :Uptime before reboot should be greater than uptime after reboot");
                print("ACTUAL RESULT 2 : UpTime after reboot is %s" %afterdetails);
                print("Successfully updated the uptime after reboot");

                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : %s" %actualresult);
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print("TEST STEP 2: compare the uptime before and after reboot");
                print("EXPECTED RESULT 2 :Uptime before reboot should be greater than uptime after reboot");
                print("ACTUAL RESULT 2: UpTime after reboot is %s" %afterdetails);
                print("Failed to update the uptime after reboot")
                print("[TEST EXECUTION RESULT] :%s" %actualresult);
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print("TEST STEP 1 :Get the uptime");
            print("EXPECTED RESULT 1 : Should return the uptime successfully");
            print("ACTUAL RESULT 1 :Failed to get the uptime after reboot %s" %details);
            print("[TEST EXECUTION RESULT] : %s" %actualresult);

    else:
        tdkTestObj.setResultStatus("FAILURE");
        print("TEST STEP 1: Get the UpTime");
        print("EXPECTED RESULT 1: Should return the uptime successfully");
        print("ACTUAL RESULT 1: Failed to get the uptime before reboot %s" %details);
        print("[TEST EXECUTION RESULT] : %s" %actualresult);
    obj.unloadModule("pam");

else:
    print("Failed to load pam module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");

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
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_GetUpTime_AfterReboot');

#Get the result of connection with test component and STB
loadmodulestatus = obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus);

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.UpTime");

    #Execute the test case in STB
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip();

    print("TEST STEP 1: Get the uptime before reboot");
    print("EXPECTED RESULT 1: Should return the uptime successfully");
    print("ACTUAL RESULT 1: UpTime before reboot is %s" %details);

    if expectedresult in actualresult and details.isdigit():
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

        #Rebooting the device
        obj.initiateReboot();
        sleep(300);

        #Checking the uptime after reboot
        tdkTestObj = obj.createTestStep('pam_GetParameterValues');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.UpTime");

        #Execute the test case in STB
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        afterdetails = tdkTestObj.getResultDetails().strip();

        print("TEST STEP 2: Verify the uptime after reboot");
        print("EXPECTED RESULT 2: Uptime after reboot should be a valid integer greater than 0");
        print("ACTUAL RESULT 2: UpTime after reboot is %s" %afterdetails);

        if expectedresult in actualresult:
            try:
                if int(afterdetails) > 0:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("[TEST EXECUTION RESULT] : SUCCESS");
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("[TEST EXECUTION RESULT] : FAILURE");
            except ValueError:
                tdkTestObj.setResultStatus("FAILURE");
                print("ACTUAL RESULT 2: Invalid UpTime value received after reboot: %s" %afterdetails);
                print("[TEST EXECUTION RESULT] : FAILURE");
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print("ACTUAL RESULT 2: Failed to get the uptime after reboot. Details: %s" %afterdetails);
            print("[TEST EXECUTION RESULT] : FAILURE");
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    obj.unloadModule("pam");

else:
    print("Failed to load pam module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");

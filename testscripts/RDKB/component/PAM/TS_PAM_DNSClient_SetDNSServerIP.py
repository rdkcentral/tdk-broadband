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

#import statement
import tdklib;

#Test component to be tested
pamObj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamObj.configureTestCase(ip,port,'TS_PAM_DNSClient_SetDNSServerIP');

#Get the result of connection with test component and STB
loadmodulestatus =pamObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    pamObj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObj = pamObj.createTestStep('pam_GetParameterNames');
    tdkTestObj.addParameter("ParamName","Device.DNS.Client.Server.");
    tdkTestObj.addParameter("ParamList","Device.DNS.Client.Server.");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    interface = tdkTestObj.getResultDetails().strip();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print("TEST STEP 1: Get an IP Interface")
        print("EXPECTED RESULT 1: Should get an IP Interface")
        print("ACTUAL RESULT 1: Interface is %s" %interface);
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : SUCCESS, %s" %interface);

        tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
        tdkTestObj.addParameter("ParamName","%sType" %interface);
        print("Parameter Name: %s" %interface)
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip();

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print("TEST STEP 2: Retrieve the Server Type of the DNS client")
            print("EXPECTED RESULT 2: Should Retrieve the Server Type of the DNS client")
            print("ACTUAL RESULT 2: DNS Client Server Type is %s" %details);
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : SUCCESS, %s" %details)

            #Set the DNS Server IP when Server Type is not static
            if 'Static' not in details:
                tdkTestObj = pamObj.createTestStep("pam_SetParameterValues");
                tdkTestObj.addParameter("ParamName","%sDNSServer" %interface);
                print("Parameter Name: %s" %interface)
                tdkTestObj.addParameter("Type","string");
                tdkTestObj.addParameter("ParamValue","60.252.50.50");
                expectedresult = "FAILURE";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    details = tdkTestObj.getResultDetails();
                    print("[TEST STEP 3]: Set the DNS Server IP when server type is not static");
                    print("[EXPECTED RESULT 3]: Should fail to set DNS Server IP when server type is not static");
                    print("[ACTUAL RESULT 3]: %s" %details);
                    print("[TEST EXECUTION RESULT] : SUCCESS");
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    details = tdkTestObj.getResultDetails();
                    print("[TEST STEP 3]: Set the DNS Server IP when server type is not static");
                    print("[EXPECTED RESULT 3]: Should fail to set DNS Server IP when server type is not static");
                    print("[ACTUAL RESULT 3]: %s" %details);
                    print("[TEST EXECUTION RESULT] : FAILURE");
            else:
                print("DNS Client Server Type is Static")
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print("TEST STEP 2: Retrieve the Server Type of the DNS client")
            print("EXPECTED RESULT 2: Should Retrieve the Server Type of the DNS client")
            print("ACTUAL RESULT 2: DNS Client Server Type is %s" %details);
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : FAILURE, %s" %details)
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print("TEST STEP 1: Get an IP Interface")
        print("EXPECTED RESULT 1: Should get an IP Interface")
        print("ACTUAL RESULT 1: Failure in getting the Interface. Details : %s" %interface);
        print("[TEST EXECUTION RESULT] : FAILURE");
    pamObj.unloadModule("pam");

else:
    print("Failed to load pam module");
    pamObj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");

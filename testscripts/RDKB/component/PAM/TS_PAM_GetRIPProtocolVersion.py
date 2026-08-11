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

# Import statement
import tdklib;

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");

# IP and Port of box, No need to change,
# This will be replaced with corresponding Box IP and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_PAM_GetRIPProtocolVersion');

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus);

if "SUCCESS" in loadmodulestatus.upper():

    # Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    ############################################################
    # STEP 1 : Get the RIP Send Version
    ############################################################

    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Routing.RIP.InterfaceSetting.1.X_CISCO_COM_SendVersion"
    );

    # Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    SendVersion = tdkTestObj.getResultDetails().strip();

    print("TEST STEP 1: Retrieve the RIP Send Version");
    print("EXPECTED RESULT 1: Should retrieve a valid RIP Send Version");

    if expectedresult in actualresult and "RIP" in SendVersion:

        # Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print("ACTUAL RESULT 1: RIP Send Version is %s" %SendVersion);
        print("[TEST EXECUTION RESULT] : SUCCESS");

        ############################################################
        # STEP 2 : Get the RIP Receive Version
        ############################################################

[O        tdkTestObj = obj.createTestStep('pam_GetParameterValues');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Routing.RIP.InterfaceSetting.1.X_CISCO_COM_ReceiveVersion"
        );

        # Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        ReceiveVersion = tdkTestObj.getResultDetails().strip();

        print("TEST STEP 2: Retrieve the RIP Receive Version");
        print("EXPECTED RESULT 2: Should retrieve a valid RIP Receive Version");

        if expectedresult in actualresult and "RIP" in ReceiveVersion:

            # Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print("ACTUAL RESULT 2: RIP Receive Version is %s" %ReceiveVersion);
            print("[TEST EXECUTION RESULT] : SUCCESS");

            ############################################################
            # STEP 3 : Compare the RIP Send and Receive Versions
            ############################################################

            print("TEST STEP 3: Compare the RIP Send and Receive Versions");
            print("EXPECTED RESULT 3: RIP Send and Receive Versions should match");

            if SendVersion == ReceiveVersion:

                tdkTestObj.setResultStatus("SUCCESS");
                print(
                    "ACTUAL RESULT 3: RIP Send Version %s and "
                    "Receive Version %s are matching"
                    %(SendVersion,ReceiveVersion)
                );
                print("[TEST EXECUTION RESULT] : SUCCESS");

            else:

                tdkTestObj.setResultStatus("FAILURE");
                print(
                    "ACTUAL RESULT 3: RIP Send Version %s and "
                    "Receive Version %s are not matching"
                    %(SendVersion,ReceiveVersion)
                );
                print("[TEST EXECUTION RESULT] : FAILURE");

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print(
                "ACTUAL RESULT 2: Failed to retrieve a valid RIP "
                "Receive Version. Received value: %s"
                %ReceiveVersion
            );
            print("[TEST EXECUTION RESULT] : FAILURE");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print(
            "ACTUAL RESULT 1: Failed to retrieve a valid RIP "
            "Send Version. Received value: %s"
            %SendVersion
        );
        print("[TEST EXECUTION RESULT] : FAILURE");

    obj.unloadModule("pam");

else:

    print("Failed to load pam module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");


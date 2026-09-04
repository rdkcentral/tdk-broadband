##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2024 RDK Management
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
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_CelllularManager_GetRadioEnvConditions_CONNECTED');

#Get the result of connection with test component and DUT
result = obj.getLoadModuleResult();
print ("[LIB LOAD STATUS]  :  %s" %result);

if "SUCCESS" in result.upper():

    obj.setLoadModuleStatus("SUCCESS");

    step = 1;
    enableModified = False;

    ############################################################
    # STEP 1 : Get Device.Cellular.Interface.1.Enable
    ############################################################

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.Interface.1.Enable"
    );

    expectedresult = "SUCCESS";

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    initialEnable = tdkTestObj.getResultDetails().strip();

    print("\nTEST STEP %d : Get Device.Cellular.Interface.1.Enable" %step);
    print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.Enable" %step);
    print("ACTUAL RESULT %d : Value is %s" %(step, initialEnable));

    if expectedresult in actualresult:

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 2 : Enable Interface if Required
    ############################################################

    step = step + 1;

    if initialEnable == "false":

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.Enable"
        );
        tdkTestObj.addParameter(
            "ParamValue",
            "true"
        );
        tdkTestObj.addParameter(
            "Type",
            "bool"
        );

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();

        print("\nTEST STEP %d : Enable Device.Cellular.Interface.1.Enable" %step);
        print("EXPECTED RESULT %d : Cellular interface should be enabled" %step);

        if expectedresult in actualresult:

            enableModified = True;

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

            sleep(20);

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print("[TEST EXECUTION RESULT] : FAILURE");

    else:

        print("\nTEST STEP %d : Interface already enabled" %step);
        print("[TEST EXECUTION RESULT] : SUCCESS");

    ############################################################
    # STEP 3 : Verify CONNECTED Status
    ############################################################

    step = step + 1;

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.X_RDK_Status"
    );

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    connectedStatus = tdkTestObj.getResultDetails();

    print("\nTEST STEP %d : Verify Device.Cellular.X_RDK_Status" %step);
    print("EXPECTED RESULT %d : Status should be CONNECTED" %step);
    print("ACTUAL RESULT %d : Status is %s" %(step, connectedStatus));

    if expectedresult in actualresult and connectedStatus == "CONNECTED":

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

        ############################################################
        # STEP 4 : Get Cellular Manager Status
        ############################################################

        step = step + 1;

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.X_RDK_Status"
        );

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        status = tdkTestObj.getResultDetails();

        print("\nTEST STEP %d : Get the cellular manager status using Device.Cellular.X_RDK_Status" %step);
        print("EXPECTED RESULT %d : Should successfully get Device.Cellular.X_RDK_Status" %step);

        if expectedresult in actualresult:

            tdkTestObj.setResultStatus("SUCCESS");
            print("ACTUAL RESULT %d : Get operation success; Details : %s" %(step,status));
            print("[TEST EXECUTION RESULT] : SUCCESS");

            ############################################################
            # STEP 5 : Verify CONNECTED or REGISTERED
            ############################################################

            step = step + 1;

            print("\nTEST STEP %d : Check if the cellular manager status as CONNECTED or REGISTERED" %step);
            print("EXPECTED RESULT %d : Should get the cellular manager status as CONNECTED or REGISTERED" %step);

            if status == "CONNECTED" or status == "REGISTERED":

                tdkTestObj.setResultStatus("SUCCESS");
                print("ACTUAL RESULT %d : %s" %(step,status));
                print("[TEST EXECUTION RESULT] : SUCCESS");

                ############################################################
                # STEP 6 : Get Radio Environment Conditions
                ############################################################

                valid_conditions = {'EXCELLENT', 'GOOD', 'FAIR', 'POOR'};

                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                tdkTestObj.addParameter(
                    "ParamName",
                    "Device.Cellular.Interface.1.X_RDK_RadioEnvConditions"
                );

                tdkTestObj.executeTestCase(expectedresult);

                actualresult = tdkTestObj.getResult();
                RadioEnvCondition = tdkTestObj.getResultDetails();

                step = step + 1;

                print("\nTEST STEP %d : Get the RadioEnvCondition using Device.Cellular.Interface.1.X_RDK_RadioEnvConditions" %step);
                print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.X_RDK_RadioEnvConditions" %step);

                if expectedresult in actualresult:

                    tdkTestObj.setResultStatus("SUCCESS");
                    print("ACTUAL RESULT %d : Get operation success; Details : %s"
                          %(step,RadioEnvCondition));
                    print("[TEST EXECUTION RESULT] : SUCCESS");

                    ############################################################
                    # STEP 7 : Validate Radio Environment Conditions
                    ############################################################

                    step = step + 1;

                    print("\nTEST STEP %d : Validate Radio Environment Conditions" %step);
                    print("EXPECTED RESULT %d : Value should be EXCELLENT, GOOD, FAIR or POOR" %step);

                    if RadioEnvCondition in valid_conditions:

                        tdkTestObj.setResultStatus("SUCCESS");
                        print("ACTUAL RESULT %d : %s"
                              %(step,RadioEnvCondition));
                        print("[TEST EXECUTION RESULT] : SUCCESS");

                        ############################################################
                        # STEP 8 : Get RSRP
                        ############################################################

                        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                        tdkTestObj.addParameter(
                            "ParamName",
                            "Device.Cellular.Interface.1.RSRP"
                        );

                        tdkTestObj.executeTestCase(expectedresult);

                        actualresult = tdkTestObj.getResult();
                        RSRP = tdkTestObj.getResultDetails();

                        step = step + 1;

                        print("\nTEST STEP %d : Get the RSRP value using Device.Cellular.Interface.1.RSRP" %step);
                        print("EXPECTED RESULT %d : Should get the RSRP value" %step);

                        if expectedresult in actualresult:

                            tdkTestObj.setResultStatus("SUCCESS");
                            print("ACTUAL RESULT %d : Get operation success; Details : %s"
                                  %(step,RSRP));
                            print("[TEST EXECUTION RESULT] : SUCCESS");

                            ############################################################
                            # STEP 9 : Validate RSRP vs Radio Conditions
                            ############################################################

                            step = step + 1;

                            print("\nTEST STEP %d : Check if the RSRP value matches the respective RadioEnvConditions" %step);
                            print("EXPECTED RESULT %d : RSRP value should match RadioEnvConditions" %step);

                            if RadioEnvCondition == "EXCELLENT" and (int(RSRP) > -85):

                                tdkTestObj.setResultStatus("SUCCESS");
                                print("ACTUAL RESULT %d : RadioEnvConditions %s matches RSRP %s"
                                      %(step,RadioEnvCondition,RSRP));
                                print("[TEST EXECUTION RESULT] : SUCCESS");

                            elif RadioEnvCondition == "GOOD" and (-85 >= int(RSRP) > -95):

                                tdkTestObj.setResultStatus("SUCCESS");
                                print("ACTUAL RESULT %d : RadioEnvConditions %s matches RSRP %s"
                                      %(step,RadioEnvCondition,RSRP));
                                print("[TEST EXECUTION RESULT] : SUCCESS");

                            elif RadioEnvCondition == "FAIR" and (-95 >= int(RSRP) > -105):

                                tdkTestObj.setResultStatus("SUCCESS");
                                print("ACTUAL RESULT %d : RadioEnvConditions %s matches RSRP %s"
                                      %(step,RadioEnvCondition,RSRP));
                                print("[TEST EXECUTION RESULT] : SUCCESS");

                            elif RadioEnvCondition == "POOR" and (-105 >= int(RSRP) > -115):

                                tdkTestObj.setResultStatus("SUCCESS");
                                print("ACTUAL RESULT %d : RadioEnvConditions %s matches RSRP %s"
                                      %(step,RadioEnvCondition,RSRP));
                                print("[TEST EXECUTION RESULT] : SUCCESS");

                            else:

                                tdkTestObj.setResultStatus("FAILURE");
                                print("ACTUAL RESULT %d : RadioEnvConditions %s is not matching expected RSRP range : %s"
                                      %(step,RadioEnvCondition,RSRP));
                                print("[TEST EXECUTION RESULT] : FAILURE");

                        else:

                            tdkTestObj.setResultStatus("FAILURE");
                            print("ACTUAL RESULT %d : Get operation failed; Details : %s"
                                  %(step,RSRP));
                            print("[TEST EXECUTION RESULT] : FAILURE");

                    else:

                        tdkTestObj.setResultStatus("FAILURE");
                        print("ACTUAL RESULT %d : %s"
                              %(step,RadioEnvCondition));
                        print("[TEST EXECUTION RESULT] : FAILURE");

                else:

                    tdkTestObj.setResultStatus("FAILURE");
                    print("ACTUAL RESULT %d : Get operation failed; Details : %s"
                          %(step,RadioEnvCondition));
                    print("[TEST EXECUTION RESULT] : FAILURE");

            else:

                tdkTestObj.setResultStatus("FAILURE");
                print("ACTUAL RESULT %d : %s"
                      %(step,status));
                print("[TEST EXECUTION RESULT] : FAILURE");

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print("ACTUAL RESULT %d : Get operation failed; Details : %s"
                  %(step,status));
            print("[TEST EXECUTION RESULT] : FAILURE");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 10 : Revert Interface State
    ############################################################

    if enableModified:

        step = step + 1;

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.Enable"
        );
        tdkTestObj.addParameter(
            "ParamValue",
            initialEnable
        );
        tdkTestObj.addParameter(
            "Type",
            "bool"
        );

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();

        print("\nTEST STEP %d : Revert Device.Cellular.Interface.1.Enable" %step);
        print("EXPECTED RESULT %d : Original value should be restored" %step);

        if expectedresult in actualresult:

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

            sleep(20);

            ############################################################
            # STEP 11 : Verify Status After Revert
            ############################################################

            step = step + 1;

            expectedRestoreStatus = \
                "CONNECTED" if initialEnable == "true" else "DEREGISTERED";

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter(
                "ParamName",
                "Device.Cellular.X_RDK_Status"
            );

            tdkTestObj.executeTestCase(expectedresult);

            actualresult = tdkTestObj.getResult();
            restoreStatus = tdkTestObj.getResultDetails().strip();

            print("\nTEST STEP %d : Verify Device.Cellular.X_RDK_Status after revert" %step);
            print("EXPECTED RESULT %d : Status should be %s"
                  %(step, expectedRestoreStatus));
            print("ACTUAL RESULT %d : Status is %s"
                  %(step, restoreStatus));

            if expectedresult in actualresult and \
               restoreStatus == expectedRestoreStatus:

                tdkTestObj.setResultStatus("SUCCESS");
                print("[TEST EXECUTION RESULT] : SUCCESS");

            else:

                tdkTestObj.setResultStatus("FAILURE");
                print("[TEST EXECUTION RESULT] : FAILURE");

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print("[TEST EXECUTION RESULT] : FAILURE");

    obj.unloadModule("tdkbtr181");

else:

    print("Failed to load the module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");


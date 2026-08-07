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
obj.configureTestCase(ip,port,'TS_CellularManager_GetStatistics_DEREGISTERED');

#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();
print ("[LIB LOAD STATUS]  :  %s" %result);

if "SUCCESS" in result.upper():
    step = 1
    flag = 0
    enableModified = False

    # Get original Enable value
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.Interface.1.Enable"
    )

    expectedresult = "SUCCESS"
    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    initialEnable = tdkTestObj.getResultDetails().strip()

    print("TEST STEP %d : Get Device.Cellular.Interface.1.Enable" % step)
    print("EXPECTED RESULT %d : Should get Device.Cellular.Interface.1.Enable value" % step)
    print("ACTUAL RESULT %d : Device.Cellular.Interface.1.Enable is %s" % (step, initialEnable))

    step += 1
    if initialEnable == "false":

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.Enable"
        )
        tdkTestObj.addParameter(
            "ParamValue",
            "true"
        )
        tdkTestObj.addParameter(
            "Type",
            "bool"
        )

        tdkTestObj.executeTestCase(expectedresult)

        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d : Set Device.Cellular.Interface.1.Enable to true" % step)
        print("EXPECTED RESULT %d : Device.Cellular.Interface.1.Enable should be true" % step)
        print("ACTUAL RESULT %d : %s" % (step, details))

        if expectedresult in actualresult:
            enableModified = True
            sleep(10)

    step += 1
    obj.setLoadModuleStatus("SUCCESS");
    #Prmitive test case which associated to this Script
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.Cellular.X_RDK_Status");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    status = tdkTestObj.getResultDetails();
    print("\nTEST STEP %d : Get the cellular manager status using Device.Cellular.X_RDK_Status" %step);
    print("EXPECTED RESULT %d : Should successfully get Device.Cellular.X_RDK_Status" %step);
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print("ACTUAL RESULT %d: Get operation success; Details : %s" %(step,status));
        print("TEST EXECUTION RESULT :SUCCESS");

        step = step + 1 ;
        print("\nTEST STEP %d : Check if cellular manager status using Device.Cellular.X_RDK_Status is CONNECTED as per prerequisite" %step);
        print("EXPECTED RESULT %d : Should successfully get Device.Cellular.X_RDK_Status as CONNECTED" %step);
        if status == "CONNECTED" :
            tdkTestObj.setResultStatus("SUCCESS");
            print("ACTUAL RESULT %d : %s" %(step,status));
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : SUCCESS");

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
            tdkTestObj.addParameter("ParamName","Device.Cellular.Interface.1.Enable");
            tdkTestObj.addParameter("ParamValue","false");
            tdkTestObj.addParameter("Type","bool");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            interfaceEnable = tdkTestObj.getResultDetails();

            step = step + 1;
            print("\nTEST STEP %d : Set Device.Cellular.Interface.1.Enable to false" %step);
            print("EXPECTED RESULT %d : Should successfully set Device.Cellular.Interface.1.Enable to false" %step);
            if expectedresult in actualresult :
                flag = 1;
                tdkTestObj.setResultStatus("SUCCESS");
                print("ACTUAL RESULT %d: Set operation success; Details : %s" %(step,interfaceEnable));
                print("TEST EXECUTION RESULT :SUCCESS");

                obj.setLoadModuleStatus("SUCCESS");
                #Prmitive test case which associated to this Script
                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                tdkTestObj.addParameter("ParamName","Device.Cellular.Interface.1.Enable");
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                enable = tdkTestObj.getResultDetails();
                step = step + 1;
                print("\nTEST STEP %d : Check if Device.Cellular.Interface.1.Enable is false" %step);
                print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.Enable as false" %step);
                if expectedresult in actualresult and enable == 'false':
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("ACTUAL RESULT %d: Get operation success; Device.Cellular.Interface.1.Enable : %s" %(step,enable));
                    print("TEST EXECUTION RESULT :SUCCESS");

                    step = step + 1;
                    obj.setLoadModuleStatus("SUCCESS");
                    #Prmitive test case which associated to this Script
                    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                    tdkTestObj.addParameter("ParamName","Device.Cellular.X_RDK_Status");
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    newstatus = tdkTestObj.getResultDetails();
                    print("\nTEST STEP %d : Get the cellular manager status using Device.Cellular.X_RDK_Status" %step);
                    print("EXPECTED RESULT %d : Should successfully get Device.Cellular.X_RDK_Status" %step);
                    if expectedresult in actualresult and newstatus == "DEREGISTERED":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print("ACTUAL RESULT %d: Get operation success and Status is : %s" %(step,newstatus));
                        print("TEST EXECUTION RESULT :SUCCESS");

                        step = step + 1;
                        obj.setLoadModuleStatus("SUCCESS");
                        #Prmitive test case which associated to this Script
                        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                        tdkTestObj.addParameter("ParamName","Device.Cellular.Interface.1.X_RDK_Statistics.BytesSent");
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        bytesSent = tdkTestObj.getResultDetails();
                        print("\nTEST STEP %d : Get Byte sent statistics using Device.Cellular.Interface.1.X_RDK_Statistics.BytesSent" %step);
                        print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.X_RDK_Statistics.BytesSent" %step);
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print("ACTUAL RESULT %d: Get operation success and Details : %s" %(step,bytesSent));
                            print("TEST EXECUTION RESULT :SUCCESS");

                            step = step + 1;
                            print("\nTEST STEP %d : Check if Byte sent statistics using Device.Cellular.Interface.1.X_RDK_Statistics.BytesSent is zero" %step);
                            print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.X_RDK_Statistics.BytesSent as zero" %step);
                            if int(bytesSent) == 0 :
                                tdkTestObj.setResultStatus("SUCCESS");
                                print("ACTUAL RESULT %d: Device.Cellular.Interface.1.X_RDK_Statistics.BytesSent : %s" %(step,bytesSent));
                                print("TEST EXECUTION RESULT :SUCCESS");
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print("ACTUAL RESULT %d: Device.Cellular.Interface.1.X_RDK_Statistics.BytesSent : %s" %(step,bytesSent));
                                #Get the result of execution
                                print("[TEST EXECUTION RESULT] : FAILURE");
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,bytesSent));
                            #Get the result of execution
                            print("[TEST EXECUTION RESULT] : FAILURE");

                        obj.setLoadModuleStatus("SUCCESS");
                        #Prmitive test case which associated to this Script
                        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                        tdkTestObj.addParameter("ParamName","Device.Cellular.Interface.1.X_RDK_Statistics.BytesReceived");
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        bytesReceived = tdkTestObj.getResultDetails();
                        print("\nTEST STEP %d : Get Byte sent statistics using Device.Cellular.Interface.1.X_RDK_Statistics.BytesReceived" %step);
                        print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.X_RDK_Statistics.BytesReceived" %step);
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print("ACTUAL RESULT %d: Get operation success and Details : %s" %(step,bytesReceived));
                            print("TEST EXECUTION RESULT :SUCCESS");

                            step = step + 1;
                            print("\nTEST STEP %d : Check if Byte sent statistics using Device.Cellular.Interface.1.X_RDK_Statistics.BytesReceived is zero" %step);
                            print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.X_RDK_Statistics.BytesReceived as zero" %step);
                            if int(bytesReceived) == 0 :
                                tdkTestObj.setResultStatus("SUCCESS");
                                print("ACTUAL RESULT %d: Device.Cellular.Interface.1.X_RDK_Statistics.BytesReceived : %s" %(step,bytesReceived));
                                print("TEST EXECUTION RESULT :SUCCESS");
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print("ACTUAL RESULT %d: Device.Cellular.Interface.1.X_RDK_Statistics.BytesReceived : %s" %(step,bytesReceived));
                                #Get the result of execution
                                print("[TEST EXECUTION RESULT] : FAILURE");
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,bytesReceived));
                            #Get the result of execution
                            print("[TEST EXECUTION RESULT] : FAILURE");
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,newstatus));
                        #Get the result of execution
                        print("[TEST EXECUTION RESULT] : FAILURE");
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,enable));
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : FAILURE");
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print("ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,interfaceEnable));
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE");
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print("ACTUAL RESULT %d : %s" %(step,status));
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : FAILURE");
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,status));
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : FAILURE");

        # Revert to original values
    if enableModified :

        step = step + 1;

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
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

        expectedresult = "SUCCESS";

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print("TEST STEP %d: Revert Device.Cellular.Interface.1.Enable to original value" %step);
        print("EXPECTED RESULT %d: Should revert Device.Cellular.Interface.1.Enable to %s"
              %(step, initialEnable));

        if expectedresult in actualresult:

            tdkTestObj.setResultStatus("SUCCESS");
            print("ACTUAL RESULT %d: Device.Cellular.Interface.1.Enable revert is success"
                  %step);
            print("[TEST EXECUTION RESULT] : SUCCESS");

            sleep(10);

            ############################################################
            # STEP 12 : Verify Device.Cellular.X_RDK_Status
            ############################################################

            step = step + 1;

            expectedRestoreStatus = "CONNECTED" \
                if initialEnable == "true" else "DEREGISTERED";

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter(
                "ParamName",
                "Device.Cellular.X_RDK_Status"
            );

            tdkTestObj.executeTestCase(expectedresult);

            actualresult = tdkTestObj.getResult();
            restoreStatus = tdkTestObj.getResultDetails().strip();

            print("TEST STEP %d: Verify Device.Cellular.X_RDK_Status after revert"
                  %step);
            print("EXPECTED RESULT %d: Device.Cellular.X_RDK_Status should be %s"
                  %(step, expectedRestoreStatus));
            print("ACTUAL RESULT %d: Status is %s"
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
            print("ACTUAL RESULT %d: Device.Cellular.Interface.1.Enable revert failed"
                  %step);
            print("[TEST EXECUTION RESULT] : FAILURE");

    obj.unloadModule("tdkbtr181");
else:
    print("Failed to load the module");
    obj.setLoadModuleStatus("FAILURE");


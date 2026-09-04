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
obj.configureTestCase(ip,port,'TS_CellularManager_CheckParametersValue_CONNECTED');

#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();
print ("[LIB LOAD STATUS]  :  %s" %result);

if "SUCCESS" in result.upper():
    step = 1;
    enableModified = False

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.Interface.1.Enable"
    )

    expectedresult = "SUCCESS"
    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    initialEnable = tdkTestObj.getResultDetails().strip()

    print("\nTEST STEP %d : Get Device.Cellular.Interface.1.Enable" %step)
    print("EXPECTED RESULT %d : Should get Device.Cellular.Interface.1.Enable" %step)
    print("ACTUAL RESULT %d : Device.Cellular.Interface.1.Enable is %s"
        %(step, initialEnable))

    step = step + 1

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

        if expectedresult in actualresult:

            enableModified = True
            sleep(20)

    step = step + 1
    obj.setLoadModuleStatus("SUCCESS");
    #Prmitive test case which associated to this Script
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.Cellular.X_RDK_Status");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    status = tdkTestObj.getResultDetails();
    print("\nTEST STEP %d : Get the  cellular manager status using Device.Cellular.X_RDK_Status" %step);
    print("EXPECTED RESULT %d : Should successfully get Device.Cellular.X_RDK_Status" %step);
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print("ACTUAL RESULT %d: Get operation success; Details : %s" %(step,status));
        print("TEST EXECUTION RESULT :SUCCESS");

        step = step + 1;
        print("\nTEST STEP %d : Check if the cellular manager status as CONNECTED" %step);
        print("EXPECTED RESULT %d : Should get the cellular manager status as CONNECTED  " %step);
        if status == "CONNECTED" :
            tdkTestObj.setResultStatus("SUCCESS");
            print("ACTUAL RESULT %d : %s" %(step,status));
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : SUCCESS");

            obj.setLoadModuleStatus("SUCCESS");
            #Prmitive test case which associated to this Script
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter("ParamName","Device.Cellular.X_RDK_Enable");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            enable = tdkTestObj.getResultDetails();

            step = step + 1;
            print("\nTEST STEP %d : Get Device.Cellular.X_RDK_Enable" %step);
            print("EXPECTED RESULT %d : Should successfully get Device.Cellular.X_RDK_Enable " %step);
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print("ACTUAL RESULT %d: Get operation success; Details : %s" %(step,enable));
                print("TEST EXECUTION RESULT :SUCCESS");

                step = step + 1;
                print("\nTEST STEP %d : Check if Device.Cellular.X_RDK_Enable is true" %step);
                print("EXPECTED RESULT %d : Should successfully get Device.Cellular.X_RDK_Enable be true " %step);
                if enable == 'true':
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("ACTUAL RESULT %d: The value of Device.Cellular.X_RDK_Enable is %s" %(step,enable));
                    print("TEST EXECUTION RESULT :SUCCESS");
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("ACTUAL RESULT %d: The value of Device.Cellular.X_RDK_Enable is %s" %(step,enable));
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : FAILURE");
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,enable));
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE");

            obj.setLoadModuleStatus("SUCCESS");
            #Prmitive test case which associated to this Script
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter("ParamName","Device.Cellular.Interface.1.Enable");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            interfaceEnable = tdkTestObj.getResultDetails();

            step = step + 1;
            print("\nTEST STEP %d : Get Device.Cellular.Interface.1.Enable" %step);
            print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.Enable" %step);
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print("ACTUAL RESULT %d: Get operation success; Details : %s" %(step,interfaceEnable));
                print("TEST EXECUTION RESULT :SUCCESS");

                step = step + 1;
                print("\nTEST STEP %d : Check if Device.Cellular.Interface.1.Enable is true" %step);
                print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.Enable be true " %step);
                if interfaceEnable == 'true':
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("ACTUAL RESULT %d: The value of Device.Cellular.Interface.1.Enable  is %s" %(step,interfaceEnable));
                    print("TEST EXECUTION RESULT :SUCCESS");
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("ACTUAL RESULT %d: The value of Device.Cellular.Interface.1.Enable is %s" %(step,interfaceEnable));
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : FAILURE");
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,interfaceEnable));
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE");

            obj.setLoadModuleStatus("SUCCESS");
            valid_conditions = {'EXCELLENT', 'GOOD', 'FAIR', 'POOR'};
            #Prmitive test case which associated to this Script
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter("ParamName","Device.Cellular.Interface.1.X_RDK_RadioEnvConditions");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            RadioEnvCondition = tdkTestObj.getResultDetails();

            step = step + 1;
            print("\nTEST STEP %d : Get Device.Cellular.Interface.1.X_RDK_RadioEnvConditions" %step);
            print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.X_RDK_RadioEnvConditions" %step);
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print("ACTUAL RESULT %d: Get operation success; Details : %s" %(step,RadioEnvCondition));
                print("TEST EXECUTION RESULT :SUCCESS");

                step = step + 1;
                print("\nTEST STEP %d : Check if Device.Cellular.Interface.1.X_RDK_RadioEnvConditions is FAIR/EXCELLENT/POOR/GOOD" %step);
                print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.X_RDK_RadioEnvConditions be FAIR/EXCELLENT/POOR/GOOD " %step);
                if RadioEnvCondition in valid_conditions:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("ACTUAL RESULT %d: The value of Device.Cellular.Interface.1.X_RDK_RadioEnvConditions  is %s" %(step,RadioEnvCondition));
                    print("TEST EXECUTION RESULT :SUCCESS");
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("ACTUAL RESULT %d: The value of Device.Cellular.Interface.1.X_RDK_RadioEnvConditions is %s" %(step,RadioEnvCondition));
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : FAILURE");
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,RadioEnvCondition));
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE");

            obj.setLoadModuleStatus("SUCCESS");
            #Prmitive test case which associated to this Script
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter("ParamName","Device.Cellular.Interface.1.X_RDK_Identification.Imei");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            Imei = tdkTestObj.getResultDetails();

            step = step + 1;
            print("\nTEST STEP %d : Get Device.Cellular.Interface.1.X_RDK_Identification.Imei" %step);
            print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.X_RDK_Identification.Imei" %step);
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print("ACTUAL RESULT %d: Get operation success; Details : %s" %(step,Imei));
                print("TEST EXECUTION RESULT :SUCCESS");

                step = step + 1;
                print("\nTEST STEP %d : Check if Device.Cellular.Interface.1.X_RDK_Identification.Imei should be non-empty" %step);
                print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.Enable be non-empty" %step);
                if Imei:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("ACTUAL RESULT %d: The value of Device.Cellular.Interface.1.X_RDK_Identification.Imei  is %s" %(step,Imei));
                    print("TEST EXECUTION RESULT :SUCCESS");
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("ACTUAL RESULT %d: The value of Device.Cellular.Interface.1.X_RDK_Identification.Imei is %s" %(step,Imei));
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : FAILURE");
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,Imei));
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE");

            obj.setLoadModuleStatus("SUCCESS");
            #Prmitive test case which associated to this Script
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter("ParamName","Device.Cellular.Interface.1.Status");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            interfaceStatus = tdkTestObj.getResultDetails();

            step = step + 1;
            print("\nTEST STEP %d : Get Device.Cellular.Interface.1.Status" %step);
            print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.Status" %step);
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print("ACTUAL RESULT %d: Get operation success; Details : %s" %(step,interfaceStatus));
                print("TEST EXECUTION RESULT :SUCCESS");

                step = step + 1;
                print("\nTEST STEP %d : Check if Device.Cellular.Interface.1.Status" %step);
                print("EXPECTED RESULT %d : Should successfully get Device.Cellular.Interface.1.Status be UP " %step);
                if interfaceStatus == 'Up':
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("ACTUAL RESULT %d: The value of Device.Cellular.Interface.1.Status  is %s" %(step,interfaceStatus));
                    print("TEST EXECUTION RESULT :SUCCESS");
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("ACTUAL RESULT %d: The value of Device.Cellular.Interface.1.Status is %s" %(step,interfaceStatus));
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : FAILURE");
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print("ACTUAL RESULT %d : %s" %(step,status));
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : FAILURE");
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print("ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,status));
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : FAILURE");
    ############################################################
    # Revert to original value
    ############################################################

    if enableModified:

        step = step + 1

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.Enable"
        )
        tdkTestObj.addParameter(
            "ParamValue",
            initialEnable
        )
        tdkTestObj.addParameter(
            "Type",
            "bool"
        )

        tdkTestObj.executeTestCase(expectedresult)

        actualresult = tdkTestObj.getResult()

        print("TEST STEP %d : Revert Device.Cellular.Interface.1.Enable"
              %step)

        if expectedresult in actualresult:

            tdkTestObj.setResultStatus("SUCCESS")
            print("[TEST EXECUTION RESULT] : SUCCESS")

            sleep(20)

            step = step + 1

            expectedRestoreStatus = \
                "CONNECTED" if initialEnable == "true" else "DEREGISTERED"

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
            tdkTestObj.addParameter(
                "ParamName",
                "Device.Cellular.X_RDK_Status"
            )

            tdkTestObj.executeTestCase(expectedresult)

            actualresult = tdkTestObj.getResult()
            restoreStatus = tdkTestObj.getResultDetails().strip()

            print("TEST STEP %d : Verify Device.Cellular.X_RDK_Status after revert"
                  %step)

            print("EXPECTED RESULT %d : Status should be %s"
                  %(step, expectedRestoreStatus))

            print("ACTUAL RESULT %d : Status is %s"
                  %(step, restoreStatus))

            if expectedresult in actualresult and \
               restoreStatus == expectedRestoreStatus:

                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS")

            else:

                tdkTestObj.setResultStatus("FAILURE")
                print("[TEST EXECUTION RESULT] : FAILURE")    
    obj.unloadModule("tdkbtr181");
else:
    print("Failed to load the module");
    obj.setLoadModuleStatus("FAILURE");


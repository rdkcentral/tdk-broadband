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

obj.configureTestCase(ip,port,'TS_CellularManager_CheckRadioEnvConditions_DEREGISTERED');

#Get the result of connection with test component and DUT
#Loading cellular manager and tdkb tr181 modules
loadmodulestatus = obj.getLoadModuleResult();

print ("[LIB LOAD STATUS]  :  %s" %loadmodulestatus);

print("Loading TDKB-TR181 module")

if "SUCCESS" in loadmodulestatus.upper():

    obj.setLoadModuleStatus("SUCCESS");

    step = 1;

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

    print("TEST STEP %d: Get the Device.Cellular.Interface.1.Enable" %step);
    print("EXPECTED RESULT %d: Should get the Device.Cellular.Interface.1.Enable value" %step);
    print("ACTUAL RESULT %d: Interface status is %s" %(step,initialEnable));

    if expectedresult in actualresult:

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 2 : Disable Interface if Required
    ############################################################

    step = step + 1;

    interfaceModified = False;

    if initialEnable == "true":

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.Enable"
        );
        tdkTestObj.addParameter(
            "ParamValue",
            "false"
        );
        tdkTestObj.addParameter(
            "Type",
            "bool"
        );

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print("TEST STEP %d: Set Device.Cellular.Interface.1.Enable as false" %step);
        print("EXPECTED RESULT %d: Interface should be disabled" %step);
        print("ACTUAL RESULT %d: %s" %(step,details));

        if expectedresult in actualresult:

            interfaceModified = True;

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

            sleep(20);

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print("[TEST EXECUTION RESULT] : FAILURE");

    else:

        print("TEST STEP %d: Device.Cellular.Interface.1.Enable already false" %step);
        print("[TEST EXECUTION RESULT] : SUCCESS");

    ############################################################
    # STEP 3 : Verify DEREGISTERED Status
    ############################################################

    step = step + 1;

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.X_RDK_Status"
    );

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print("TEST STEP %d: Get the Device.Cellular.X_RDK_Status" %step);
    print("EXPECTED RESULT %d: Should get the Device.Cellular.X_RDK_Status as DEREGISTERED" %step);
    print("ACTUAL RESULT %d: Interface status is %s" %(step,details));

    if expectedresult in actualresult and details == "DEREGISTERED":

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

        ############################################################
        # STEP 4 : Verify Radio Environment Conditions
        ############################################################

        step = step + 1;

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.X_RDK_RadioEnvConditions"
        );

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print("TEST STEP %d: Get the Device.Cellular.Interface.1.X_RDK_RadioEnvConditions" %step);
        print("EXPECTED RESULT %d: Should get the Device.Cellular.Interface.1.X_RDK_RadioEnvConditions as UNAVAILABLE" %step);
        print("ACTUAL RESULT %d: Interface status is %s" %(step,details));

        if expectedresult in actualresult and details == "UNAVAILABLE":

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print("[TEST EXECUTION RESULT] : FAILURE");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 5 : Restore Original Interface State
    ############################################################

    if interfaceModified:

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

        print("TEST STEP %d: Revert Device.Cellular.Interface.1.Enable" %step);
        print("EXPECTED RESULT %d: Original value should be restored" %step);

        if expectedresult in actualresult:

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

            sleep(20);

            ############################################################
            # STEP 6 : Verify Status After Revert
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

            print("TEST STEP %d: Verify Device.Cellular.X_RDK_Status after revert" %step);
            print("EXPECTED RESULT %d: Status should be %s"
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
            print("[TEST EXECUTION RESULT] : FAILURE");

    #Unload tdkbtr181 and cellular manager modules
    obj.unloadModule("tdkbtr181");

else:

    print("Failed to load module");
    obj.setLoadModuleStatus("FAILURE");


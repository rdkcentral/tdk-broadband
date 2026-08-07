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
import time;
from time import sleep;

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_CellularManager_X_RDK_Enable_PersistenceOnReboot');
obj.configureTestCase(ip,port,'TS_CellularManager_X_RDK_Enable_PersistenceOnReboot');

#Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult();
loadmodulestatus = obj.getLoadModuleResult();

print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus_sys);
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus);

print("Loading Cellular Manager module");

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus_sys.upper():

    sysobj.setLoadModuleStatus("SUCCESS");
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult = "SUCCESS";
    step = 1;

    ############################################################
    # STEP 1 : Get Device.Cellular.Interface.1.Enable
    ############################################################

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.Interface.1.Enable"
    );

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    interfaceEnable = tdkTestObj.getResultDetails().strip();

    print("TEST STEP %d: Get Device.Cellular.Interface.1.Enable" %step);
    print("EXPECTED RESULT %d: Should get Device.Cellular.Interface.1.Enable value" %step);
    print("ACTUAL RESULT %d: Value is %s" %(step,interfaceEnable));

    if expectedresult in actualresult and interfaceEnable != "":

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 2 : Get Device.Cellular.X_RDK_Status
    ############################################################

    step = step + 1;

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.X_RDK_Status"
    );

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    status = tdkTestObj.getResultDetails().strip();

    print("TEST STEP %d: Get Device.Cellular.X_RDK_Status" %step);
    print("EXPECTED RESULT %d: Should get Device.Cellular.X_RDK_Status value" %step);
    print("ACTUAL RESULT %d: Status is %s" %(step,status));

    if expectedresult in actualresult and status != "":

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 3 : Get Device.Cellular.X_RDK_Enable
    ############################################################

    step = step + 1;

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.X_RDK_Enable"
    );

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    initialvalue = tdkTestObj.getResultDetails().strip();

    print("TEST STEP %d: Get Device.Cellular.X_RDK_Enable" %step);
    print("EXPECTED RESULT %d: Should get Device.Cellular.X_RDK_Enable" %step);
    print("ACTUAL RESULT %d: Value is %s" %(step,initialvalue));

    if expectedresult in actualresult and initialvalue in ["true", "false"]:

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

        ############################################################
        # STEP 4 : Set Device.Cellular.X_RDK_Enable to false
        ############################################################

        step = step + 1;

        setVal = "false";

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.X_RDK_Enable"
        );
        tdkTestObj.addParameter(
            "ParamValue",
            setVal
        );
        tdkTestObj.addParameter(
            "Type",
            "bool"
        );

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        setDetails = tdkTestObj.getResultDetails();

        print("TEST STEP %d: Set Device.Cellular.X_RDK_Enable" %step);
        print("EXPECTED RESULT %d: Should set Device.Cellular.X_RDK_Enable as %s" %(step,setVal));
        print("ACTUAL RESULT %d: Value is %s" %(step,setDetails));

        if expectedresult in actualresult:

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

        else:

            print("Set operation did not return SUCCESS, verifying parameter value using GET");

        sleep(10);

        ############################################################
        # STEP 5 : Verify Device.Cellular.X_RDK_Enable after Set
        ############################################################

        step = step + 1;

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.X_RDK_Enable"
        );

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        getAfterSet = tdkTestObj.getResultDetails().strip();

        print("TEST STEP %d: Verify Device.Cellular.X_RDK_Enable after Set" %step);
        print("EXPECTED RESULT %d: Device.Cellular.X_RDK_Enable should be %s" %(step,setVal));
        print("ACTUAL RESULT %d: Value is %s" %(step,getAfterSet));

        if expectedresult in actualresult and getAfterSet == setVal:

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

            ############################################################
            # STEP 6 : Reboot DUT
            ############################################################

            step = step + 1;

            print("TEST STEP %d: Reboot the DUT" %step);
            print("EXPECTED RESULT %d: DUT should reboot successfully" %step);

            sysobj.initiateReboot();
            sleep(60);

            print("ACTUAL RESULT %d: DUT reboot completed" %step);
            print("[TEST EXECUTION RESULT] : SUCCESS");

            ############################################################
            # STEP 7 : Get Device.Cellular.X_RDK_Enable after Reboot
            ############################################################

            step = step + 1;

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter(
                "ParamName",
                "Device.Cellular.X_RDK_Enable"
            );

            tdkTestObj.executeTestCase(expectedresult);

            actualresult = tdkTestObj.getResult();
            newvalue = tdkTestObj.getResultDetails().strip();

            print("TEST STEP %d: Get Device.Cellular.X_RDK_Enable after Reboot" %step);
            print("EXPECTED RESULT %d: Should get Device.Cellular.X_RDK_Enable value" %step);
            print("ACTUAL RESULT %d: Value is %s" %(step,newvalue));

            if expectedresult in actualresult and newvalue != "":

                tdkTestObj.setResultStatus("SUCCESS");
                print("[TEST EXECUTION RESULT] : SUCCESS");

                ############################################################
                # STEP 8 : Check Persistence after Reboot
                ############################################################

                step = step + 1;

                print("TEST STEP %d: Check persistence of Device.Cellular.X_RDK_Enable value after Reboot" %step);
                print("EXPECTED RESULT %d: Device.Cellular.X_RDK_Enable should persist as %s after reboot" %(step,setVal));
                print("ACTUAL RESULT %d: Value is %s" %(step,newvalue));

                if newvalue == setVal:

                    tdkTestObj.setResultStatus("SUCCESS");
                    print("[TEST EXECUTION RESULT] : SUCCESS");

                else:

                    tdkTestObj.setResultStatus("FAILURE");
                    print("[TEST EXECUTION RESULT] : FAILURE");

            else:

                tdkTestObj.setResultStatus("FAILURE");
                print("[TEST EXECUTION RESULT] : FAILURE");

            ############################################################
            # STEP 9 : Revert Device.Cellular.X_RDK_Enable to initial value
            ############################################################

            step = step + 1;

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter(
                "ParamName",
                "Device.Cellular.X_RDK_Enable"
            );
            tdkTestObj.addParameter(
                "ParamValue",
                initialvalue
            );
            tdkTestObj.addParameter(
                "Type",
                "bool"
            );

            tdkTestObj.executeTestCase(expectedresult);

            actualresult = tdkTestObj.getResult();
            revertDetails = tdkTestObj.getResultDetails();

            print("TEST STEP %d: Revert Device.Cellular.X_RDK_Enable to initial value" %step);
            print("EXPECTED RESULT %d: Device.Cellular.X_RDK_Enable should be restored to %s" %(step,initialvalue));
            print("ACTUAL RESULT %d: %s" %(step,revertDetails));

            if expectedresult in actualresult:

                tdkTestObj.setResultStatus("SUCCESS");
                print("[TEST EXECUTION RESULT] : SUCCESS");

                sleep(10);

                ############################################################
                # STEP 10 : Verify Device.Cellular.X_RDK_Enable after Revert
                ############################################################

                step = step + 1;

                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                tdkTestObj.addParameter(
                    "ParamName",
                    "Device.Cellular.X_RDK_Enable"
                );

                tdkTestObj.executeTestCase(expectedresult);

                actualresult = tdkTestObj.getResult();
                revertValue = tdkTestObj.getResultDetails().strip();

                print("TEST STEP %d: Verify Device.Cellular.X_RDK_Enable after revert" %step);
                print("EXPECTED RESULT %d: Device.Cellular.X_RDK_Enable should be %s" %(step,initialvalue));
                print("ACTUAL RESULT %d: Value is %s" %(step,revertValue));

                if expectedresult in actualresult and revertValue == initialvalue:

                    tdkTestObj.setResultStatus("SUCCESS");
                    print("[TEST EXECUTION RESULT] : SUCCESS");

                else:

                    tdkTestObj.setResultStatus("FAILURE");
                    print("[TEST EXECUTION RESULT] : FAILURE");

            else:

                tdkTestObj.setResultStatus("FAILURE");
                print("[TEST EXECUTION RESULT] : FAILURE");

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print("[TEST EXECUTION RESULT] : FAILURE");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");

else:

    print("Failed to load module");
    sysobj.setLoadModuleStatus("FAILURE");
    obj.setLoadModuleStatus("FAILURE");



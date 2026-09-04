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
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_CellularManager_GetSimCard_Status');
sysobj.configureTestCase(ip,port,'TS_CellularManager_GetSimCard_Status');

#load cellular manager,sysutil and tdkb-tr181 modules
loadmodulestatus_sys = sysobj.getLoadModuleResult();
loadmodulestatus = obj.getLoadModuleResult();

print ("[LIB LOAD STATUS]  :  %s" %loadmodulestatus_sys);
print ("[LIB LOAD STATUS]  :  %s" %loadmodulestatus);

print("Loading module")

if "SUCCESS" in loadmodulestatus.upper() and \
   "SUCCESS" in loadmodulestatus_sys.upper():

    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

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

    print("TEST STEP %d: Get Device.Cellular.Interface.1.Enable" %step);
    print("EXPECTED RESULT %d: Should get Device.Cellular.Interface.1.Enable" %step);
    print("ACTUAL RESULT %d: Value is %s" %(step, initialEnable));

    step = step + 1;

    ############################################################
    # STEP 2 : Enable Interface if Required
    ############################################################

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

        if expectedresult in actualresult:

            enableModified = True;
            sleep(20);

    step = step + 1;

    ############################################################
    # STEP 3 : Verify CONNECTED Status
    ############################################################

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.X_RDK_Status"
    );

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    status = tdkTestObj.getResultDetails();

    print("TEST STEP %d: Get Device.Cellular.X_RDK_Status" %step);
    print("EXPECTED RESULT %d: Status should be CONNECTED" %step);
    print("ACTUAL RESULT %d: Status is %s" %(step,status));

    if expectedresult in actualresult and status == "CONNECTED":

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

        ############################################################
        # STEP 4 : Get SIM Operator Name
        ############################################################

        step = step + 1;

        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        tdkTestObj.addParameter(
            "command",
            "qmicli -p -d /dev/cdc-wdm0 --nas-get-home-network | grep -i \"Description\""
        );

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print("TEST STEP %d: Get sim card name" %step);
        print("EXPECTED RESULT %d: Should get sim card operator name" %step);

        if expectedresult in actualresult and details != "":

            operator = details[13:-2];

            print("ACTUAL RESULT %d: Operator name : %s"
                  %(step,operator));

            tdkTestObj.setResultStatus("SUCCESS");

            print("[TEST EXECUTION RESULT] : SUCCESS");

        else:

            print("ACTUAL RESULT %d: Error: Failed to obtain sim card name"
                  %step);

            tdkTestObj.setResultStatus("FAILURE");

            print("[TEST EXECUTION RESULT] : FAILURE");

        ############################################################
        # STEP 5 : Get SIM Slot Status
        ############################################################

        step = step + 1;

        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        tdkTestObj.addParameter(
            "command",
            "qmicli -p -d /dev/cdc-wdm0 --uim-get-slot-status | grep \"Slot status: active\""
        );

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        details = details[:-2];

        print("TEST STEP %d: Get the sim card slot status" %step);
        print("EXPECTED RESULT %d: Should get the sim card slot status" %step);
        print("ACTUAL RESULT %d: %s" %(step,details));

        if expectedresult in actualresult and details != "":

            tdkTestObj.setResultStatus("SUCCESS");

            print("[TEST EXECUTION RESULT] : SUCCESS");

        else:

            tdkTestObj.setResultStatus("FAILURE");

            print("[TEST EXECUTION RESULT] : FAILURE");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 6 : Revert Interface State
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

        print("TEST STEP %d: Revert Device.Cellular.Interface.1.Enable"
              %step);

        if expectedresult in actualresult:

            tdkTestObj.setResultStatus("SUCCESS");

            print("[TEST EXECUTION RESULT] : SUCCESS");

            sleep(20);

            ############################################################
            # STEP 7 : Verify Status After Revert
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

            print("TEST STEP %d: Verify Device.Cellular.X_RDK_Status after revert"
                  %step);

            print("EXPECTED RESULT %d: Status should be %s"
                  %(step,expectedRestoreStatus));

            print("ACTUAL RESULT %d: Status is %s"
                  %(step,restoreStatus));

            if expectedresult in actualresult and \
               restoreStatus == expectedRestoreStatus:

                tdkTestObj.setResultStatus("SUCCESS");

                print("[TEST EXECUTION RESULT] : SUCCESS");

            else:

                tdkTestObj.setResultStatus("FAILURE");

                print("[TEST EXECUTION RESULT] : FAILURE");

    sysobj.unloadModule("sysutil");
    obj.unloadModule("tdkbtr181");

else:

    print("Failed to load module");
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");

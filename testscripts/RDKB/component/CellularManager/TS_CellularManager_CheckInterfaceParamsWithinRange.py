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

obj.configureTestCase(ip,port,'TS_CellularManager_CheckInterfaceParamsWithinRange');

#load cellular manager and tdkbtr181 modules
loadmodulestatus = obj.getLoadModuleResult();
print ("[LIB LOAD STATUS]  :  %s" %loadmodulestatus);

print("Loading TDKB-TR181 module")

if "SUCCESS" in loadmodulestatus.upper():

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

    print("TEST STEP %d: Get Device.Cellular.Interface.1.Enable" %step);
    print("EXPECTED RESULT %d: Should get Device.Cellular.Interface.1.Enable" %step);
    print("ACTUAL RESULT %d: Value is %s" %(step, initialEnable));

    if expectedresult in actualresult:

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

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

        print("TEST STEP %d: Enable Device.Cellular.Interface.1.Enable" %step);
        print("EXPECTED RESULT %d: Interface should be enabled" %step);

        if expectedresult in actualresult:

            enableModified = True;
            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

            sleep(20);

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print("[TEST EXECUTION RESULT] : FAILURE");

    else:

        print("TEST STEP %d: Device.Cellular.Interface.1.Enable already true" %step);

    step = step + 1;

    ############################################################
    # STEP 3 : Verify Cellular Status
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
    print("ACTUAL RESULT %d: Status is %s" %(step, status));

    if expectedresult in actualresult and status == "CONNECTED":

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

        ############################################################
        # STEP 4 : Verify RSSI
        ############################################################

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.RSSI"
        );

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        rssi_value = tdkTestObj.getResultDetails();

        step = step + 1;

        print("TEST STEP %d: Get the value of Device.Cellular.Interface.1.RSSI" %step);
        print("EXPECTED RESULT %d: Value should be within range of -117 dBm to -25 dBm" %step);
        print("ACTUAL RESULT %d: Value is %s" %(step, rssi_value));

        if expectedresult in actualresult and (-117 < int(rssi_value) < -25):

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print("[TEST EXECUTION RESULT] : FAILURE");

        ############################################################
        # STEP 5 : Verify SNR
        ############################################################

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.X_RDK_SNR"
        );

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        snr_value = tdkTestObj.getResultDetails();

        step = step + 1;

        print("TEST STEP %d: Get the value of Device.Cellular.Interface.1.X_RDK_SNR" %step);
        print("EXPECTED RESULT %d: Value should be within range of 0 dB to 20 dB" %step);
        print("ACTUAL RESULT %d: Value is %s" %(step, snr_value));

        if expectedresult in actualresult and (0 < int(snr_value) < 20):

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print("[TEST EXECUTION RESULT] : FAILURE");

        ############################################################
        # STEP 6 : Verify RSRP
        ############################################################

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.RSRP"
        );

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        rsrp_value = tdkTestObj.getResultDetails();

        step = step + 1;

        print("TEST STEP %d: Get the value of Device.Cellular.Interface.1.RSRP" %step);
        print("EXPECTED RESULT %d: Value should be within range of -155 dBm to -44 dBm" %step);
        print("ACTUAL RESULT %d: Value is %s" %(step, rsrp_value));

        if expectedresult in actualresult and (-155 < int(rsrp_value) < -44):

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print("[TEST EXECUTION RESULT] : FAILURE");

        ############################################################
        # STEP 7 : Verify RSRQ
        ############################################################

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.RSRQ"
        );

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        rsrq_value = tdkTestObj.getResultDetails();

        step = step + 1;

        print("TEST STEP %d: Get the value of Device.Cellular.Interface.1.RSRQ" %step);
        print("EXPECTED RESULT %d: Value should be within range of -43 dB to 20 dB" %step);
        print("ACTUAL RESULT %d: Value is %s" %(step, rsrq_value));

        if expectedresult in actualresult and (-43 < int(rsrq_value) < 20):

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print("[TEST EXECUTION RESULT] : FAILURE");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 8 : Revert Interface State
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

        print("TEST STEP %d: Revert Device.Cellular.Interface.1.Enable" %step);
        print("EXPECTED RESULT %d: Original value should be restored" %step);

        if expectedresult in actualresult:

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

            sleep(20);

            ############################################################
            # STEP 9 : Verify Status After Revert
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

    obj.unloadModule("tdkbtr181");

else:

    print("Failed to load module");
    obj.setLoadModuleStatus("FAILURE");

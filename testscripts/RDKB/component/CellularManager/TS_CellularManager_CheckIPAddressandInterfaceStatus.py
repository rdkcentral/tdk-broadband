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
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_CellularManager_CheckIPAddressandInterfaceStatus');
sysobj.configureTestCase(ip,port,'TS_CellularManager_CheckIPAddressandInterfaceStatus');

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
    print("ACTUAL RESULT %d: Value is %s" %(step,initialEnable));

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

        print("TEST STEP %d: Interface already enabled" %step);
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
    status = tdkTestObj.getResultDetails();

    print("TEST STEP %d: Get Device.Cellular.X_RDK_Status" %step);
    print("EXPECTED RESULT %d: Status should be CONNECTED or REGISTERED" %step);
    print("ACTUAL RESULT %d: Status is %s" %(step,status));

    if expectedresult in actualresult and \
       status in ["CONNECTED", "REGISTERED"]:

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

        ############################################################
        # STEP 4 : Verify wwan0 Interface Status
        ############################################################

        step = step + 1;

        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        tdkTestObj.addParameter(
            "command",
            "ip link show | grep 'wwan0' | grep 'UP'"
        );

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print("TEST STEP %d: Check whether interface wwan0 is UP" %step);
        print("EXPECTED RESULT %d: wwan0 interface should be UP" %step);

        if expectedresult in actualresult and details != "":

            print("ACTUAL RESULT %d: wwan0 interface is UP" %step);

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

            ############################################################
            # STEP 5 : Get wwan0 IP Address
            ############################################################

            step = step + 1;

            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter(
                "command",
                "ifconfig wwan0 | grep 'inet addr' | cut -d ':' -f 2 | cut -d ' ' -f 1"
            );

            tdkTestObj.executeTestCase(expectedresult);

            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            ip_wwan0 = details[:-2];

            print("TEST STEP %d: Get the wwan0 IP address" %step);
            print("EXPECTED RESULT %d: Should obtain the wwan0 IP address" %step);
            print("ACTUAL RESULT %d: wwan0 IP : %s" %(step,ip_wwan0));

            if expectedresult in actualresult and ip_wwan0 != "":

                tdkTestObj.setResultStatus("SUCCESS");

                print("ACTUAL RESULT %d: Successfully obtained wwan0 IP : %s"
                      %(step,ip_wwan0));
                print("[TEST EXECUTION RESULT] : SUCCESS");

            else:

                print("ACTUAL RESULT %d: Failed to obtain wwan0 IP" %step);

                tdkTestObj.setResultStatus("FAILURE");
                print("[TEST EXECUTION RESULT] : FAILURE");

        else:

            print("ACTUAL RESULT %d: Error: Failed to obtain wwan0 interface"
                  %step);

            tdkTestObj.setResultStatus("FAILURE");
            print("[TEST EXECUTION RESULT] : FAILURE");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 6 : Restore Original Interface State
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

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print("[TEST EXECUTION RESULT] : FAILURE");

    sysobj.unloadModule("sysutil");
    obj.unloadModule("tdkbtr181");

else:

    print("Failed to load module");
    sysobj.setLoadModuleStatus("FAILURE");
    obj.setLoadModuleStatus("FAILURE");


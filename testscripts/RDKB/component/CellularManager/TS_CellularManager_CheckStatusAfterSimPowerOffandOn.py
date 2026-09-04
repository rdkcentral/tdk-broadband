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
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_CellularManager_CheckStatusAfterSimPowerOffandOn');
sysobj.configureTestCase(ip,port,'TS_CellularManager_CheckStatusAfterSimPowerOffandOn');

#load cellular manager,sysutil and tdkb-tr181 modules
loadmodulestatus_sys = sysobj.getLoadModuleResult();
loadmodulestatus = obj.getLoadModuleResult();

print ("[LIB LOAD STATUS]  :  %s" %loadmodulestatus_sys);
print ("[LIB LOAD STATUS]  :  %s" %loadmodulestatus);

print("Loading sysutil and tdkb-tr181 modules");

if "SUCCESS" in loadmodulestatus.upper() and \
   "SUCCESS" in loadmodulestatus_sys.upper():

    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    ############################################################
    # STEP 1 : Verify Device.Cellular.Interface.1.Enable
    ############################################################

    step = 1;

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.Interface.1.Enable"
    );

    expectedresult = "SUCCESS";

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    interfaceEnable = tdkTestObj.getResultDetails().strip();

    print("TEST STEP %d: Get Device.Cellular.Interface.1.Enable" %step);
    print("EXPECTED RESULT %d: Device.Cellular.Interface.1.Enable should be true" %step);
    print("ACTUAL RESULT %d: Value is %s" %(step, interfaceEnable));

    if expectedresult in actualresult and interfaceEnable == "true":

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 2 : Verify Device.Cellular.X_RDK_Status
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

    print("TEST STEP %d: Verify Device.Cellular.X_RDK_Status" %step);
    print("EXPECTED RESULT %d: Device.Cellular.X_RDK_Status should be CONNECTED" %step);
    print("ACTUAL RESULT %d: Status is %s" %(step, status));

    if expectedresult in actualresult and status == "CONNECTED":

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 3 : SIM Power OFF
    ############################################################

    step = step + 1;

    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter(
        "command",
        "qmicli -p -d /dev/cdc-wdm0 --uim-sim-power-off=1"
    );

    expectedresult = "SUCCESS";

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print("TEST STEP %d: Power off the SIM using qmicli command" %step);
    print("EXPECTED RESULT %d: Should successfully perform SIM power off" %step);
    print("ACTUAL RESULT %d: %s" %(step, details));

    if expectedresult in actualresult and details != "":

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 4 : Verify Status After SIM Power OFF
    ############################################################

    step = step + 1;

    sleep(5);

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.X_RDK_Status"
    );

    expectedresult = "SUCCESS";

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print("TEST STEP %d: Get the Device.Cellular.X_RDK_Status" %step);
    print("EXPECTED RESULT %d: Should get Device.Cellular.X_RDK_Status as DEREGISTERED or DOWN" %step);
    print("ACTUAL RESULT %d: Interface status is %s" %(step, details));

    if expectedresult in actualresult and \
       details in ["DEREGISTERED", "DOWN"]:

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 5 : SIM Power ON
    ############################################################

    step = step + 1;

    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter(
        "command",
        "qmicli -p -d /dev/cdc-wdm0 --uim-sim-power-on=1"
    );

    expectedresult = "SUCCESS";

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print("TEST STEP %d: Power on the SIM using qmicli command" %step);
    print("EXPECTED RESULT %d: Should successfully perform SIM power on" %step);
    print("ACTUAL RESULT %d: %s" %(step, details));

    if expectedresult in actualresult and details != "":

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 6 : Verify Status After SIM Power ON
    ############################################################

    sleep(20);

    step = step + 1;

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.X_RDK_Status"
    );

    expectedresult = "SUCCESS";

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print("TEST STEP %d: Get the Device.Cellular.X_RDK_Status" %step);
    print("EXPECTED RESULT %d: Should get Device.Cellular.X_RDK_Status as REGISTERED or CONNECTED" %step);
    print("ACTUAL RESULT %d: Interface status is %s" %(step, details));

    if expectedresult in actualresult and \
       details in ["REGISTERED", "CONNECTED"]:

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");

else:

    print("Failed to load module");
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");


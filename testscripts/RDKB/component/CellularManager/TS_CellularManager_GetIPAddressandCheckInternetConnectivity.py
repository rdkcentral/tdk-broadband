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
sysobj.configureTestCase(ip,port,'TS_CellularManager_GetIPAddressandCheckInternetConnectivity');
obj.configureTestCase(ip,port,'TS_CellularManager_GetIPAddressandCheckInternetConnectivity');

#Get the result of connection with test component and DUT
#Load cellular manager, tdkbtr181 and sysutil modules
loadmodulestatus2 = sysobj.getLoadModuleResult();
loadmodulestatus = obj.getLoadModuleResult();

print ("[LIB LOAD STATUS]  :  %s" %loadmodulestatus2);
print ("[LIB LOAD STATUS]  :  %s" %loadmodulestatus);

print("Loading sysutil and TDKB-TR181 module")

if "SUCCESS" in loadmodulestatus2.upper() and \
   "SUCCESS" in loadmodulestatus.upper():

    sysobj.setLoadModuleStatus("SUCCESS");
    obj.setLoadModuleStatus("SUCCESS");

    # Get Device.Cellular.Interface.1.Enable
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.Interface.1.Enable"
    );

    expectedresult = "SUCCESS";

    # Execute testcase in DUT
    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    initialEnable = details.strip();

    # Ensure Device.Cellular.Interface.1.Enable is false
    if initialEnable == "true":

        setVal = "false";

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.Enable"
        );
        tdkTestObj.addParameter(
            "ParamValue",
            setVal
        );
        tdkTestObj.addParameter(
            "Type",
            "bool"
        );

        # Execute testcase in DUT
        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

    print("TEST STEP 1: Set the Device.Cellular.Interface.1.Enable as false");
    print("EXPECTED RESULT 1: Should set the Device.Cellular.Interface.1.Enable as false");
    print("ACTUAL RESULT 1: Details : %s" %details);

    if expectedresult in actualresult and details != "":

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

        ############################################################
        # STEP 2
        ############################################################

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.X_RDK_Status"
        );

        expectedresult = "SUCCESS";

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print("TEST STEP 2: Get the Device.Cellular.X_RDK_Status");
        print("EXPECTED RESULT 2: Should get the Device.Cellular.X_RDK_Status as DEREGISTERED");
        print("ACTUAL RESULT 2: Interface status is %s" %details);

        if expectedresult in actualresult and details == "DEREGISTERED":

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

            ############################################################
            # STEP 3
            ############################################################

            tdkTestObj = sysobj.createTestStep('ExecuteCmd');

            query = "ping -c 2 8.8.8.8"

            print("query:%s" %query);

            tdkTestObj.addParameter(
                "command",
                query
            );

            expectedresult = "SUCCESS";

            tdkTestObj.executeTestCase(expectedresult);

            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip();

            print("TEST STEP 3: Do a ping operation and check for internet connectivity");
            print("EXPECTED RESULT 3: Ping operation should not work and result in 100% packet loss");

            if expectedresult in actualresult:

                print("ACTUAL RESULT 3: Ping operation failed with no internet connectivity");

                tdkTestObj.setResultStatus("SUCCESS");
                print("[TEST EXECUTION RESULT] : SUCCESS");

            else:

                print("ACTUAL RESULT 3: Ping operation is success with active internet connectivity");

                tdkTestObj.setResultStatus("FAILURE");
                print("[TEST EXECUTION RESULT] : FAILURE");

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print("[TEST EXECUTION RESULT] : FAILURE");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 4
    ############################################################

    setVal = "true";

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.Interface.1.Enable"
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
    details = tdkTestObj.getResultDetails();

    print("TEST STEP 4: Set the Device.Cellular.Interface.1.Enable as true");
    print("EXPECTED RESULT 4: Should set the Device.Cellular.Interface.1.Enable as true");
    print("ACTUAL RESULT 4: Details : %s" %details);

    if expectedresult in actualresult and details != "":

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

        sleep(20);

        ############################################################
        # STEP 5
        ############################################################

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.X_RDK_Status"
        );

        expectedresult = "SUCCESS";

        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print("TEST STEP 5: Get the Device.Cellular.X_RDK_Status");
        print("EXPECTED RESULT 5: Should get the Device.Cellular.X_RDK_Status as CONNECTED");
        print("ACTUAL RESULT 5: Interface status is %s" %details);

        if expectedresult in actualresult and details == "CONNECTED":

            tdkTestObj.setResultStatus("SUCCESS");
            print("[TEST EXECUTION RESULT] : SUCCESS");

            ############################################################
            # STEP 6
            ############################################################

            tdkTestObj = sysobj.createTestStep('ExecuteCmd');

            query = "ping -c 2 8.8.8.8"

            print("query:%s" %query);

            tdkTestObj.addParameter(
                "command",
                query
            );

            expectedresult = "SUCCESS";

            tdkTestObj.executeTestCase(expectedresult);

            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip();

            print("TEST STEP 6: Do a ping operation and check for internet connectivity");
            print("EXPECTED RESULT 6: Ping operation should be success with 0% packet loss");

            if expectedresult in actualresult:

                print("ACTUAL RESULT 6: Ping operation is success with active internet connectivity");

                tdkTestObj.setResultStatus("SUCCESS");
                print("[TEST EXECUTION RESULT] : SUCCESS");

            else:

                print("ACTUAL RESULT 6: Ping operation failed with no internet connectivity");

                tdkTestObj.setResultStatus("FAILURE");
                print("[TEST EXECUTION RESULT] : FAILURE");

        else:

            tdkTestObj.setResultStatus("FAILURE");
            print("[TEST EXECUTION RESULT] : FAILURE");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    ############################################################
    # STEP 7
    ############################################################

    tdkTestObj = sysobj.createTestStep('ExecuteCmd');

    tdkTestObj.addParameter(
        "command",
        "ifconfig wwan0 | grep 'inet addr' | cut -d ':' -f 2 | cut -d ' ' -f 1"
    );

    expectedresult = "SUCCESS";

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    ip_wwan0 = tdkTestObj.getResultDetails();

    print("TEST STEP 7: Get the wwan0 IP address");
    print("EXPECTED RESULT 7: Should get the wwan0 IP address");

    if expectedresult in actualresult and ip_wwan0 != "":

        ip_wwan0 = ip_wwan0[0:-2];

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

        print("wwan0 IP: %s" %ip_wwan0);

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

        print("Error: Failed to obtain wwan0 IP");

    ############################################################
    # STEP 8 : Revert Device.Cellular.Interface.1.Enable
    ############################################################

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
    details = tdkTestObj.getResultDetails();

    print("TEST STEP 8: Revert Device.Cellular.Interface.1.Enable to original value");
    print("EXPECTED RESULT 8: Original value should be restored");
    print("ACTUAL RESULT 8: %s" %details);

    if expectedresult in actualresult:

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

        sleep(20);

        ############################################################
        # STEP 9 : Verify Device.Cellular.X_RDK_Status after revert
        ############################################################

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

        print("TEST STEP 9: Verify Device.Cellular.X_RDK_Status after revert");
        print("EXPECTED RESULT 9: Status should be %s"
              %expectedRestoreStatus);
        print("ACTUAL RESULT 9: Status is %s"
              %restoreStatus);

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
    sysobj.unloadModule("sysutil");

else:

    print("Failed to load module");
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");


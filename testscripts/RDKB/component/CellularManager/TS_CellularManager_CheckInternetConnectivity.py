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
import tdklib
from time import sleep

# Test components
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_CellularManager_CheckInternetConnectivity')
sysobj.configureTestCase(ip,port,'TS_CellularManager_CheckInternetConnectivity')

# Load modules
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

print("[LIB LOAD STATUS] : %s" % loadmodulestatus)
print("[LIB LOAD STATUS] : %s" % loadmodulestatus_sys)

print("Loading modules")

if "SUCCESS" in loadmodulestatus.upper() and \
   "SUCCESS" in loadmodulestatus_sys.upper():

    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    expectedresult = "SUCCESS"
    enableModified = False

    ############################################################
    # STEP 1 : Get Device.Cellular.Interface.1.Enable
    ############################################################

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.Interface.1.Enable"
    )

    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    initialEnable = tdkTestObj.getResultDetails().strip()

    print("TEST STEP 1: Get Device.Cellular.Interface.1.Enable")
    print("EXPECTED RESULT 1: Should get Device.Cellular.Interface.1.Enable value")
    print("ACTUAL RESULT 1: Device.Cellular.Interface.1.Enable is %s" % initialEnable)

    if expectedresult in actualresult and initialEnable in ["true", "false"]:

        tdkTestObj.setResultStatus("SUCCESS")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        ############################################################
        # STEP 2 : Enable Interface if Required
        ############################################################

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

            print("TEST STEP 2: Set Device.Cellular.Interface.1.Enable to true")
            print("EXPECTED RESULT 2: Device.Cellular.Interface.1.Enable should be set to true")
            print("ACTUAL RESULT 2: %s" % details)

            if expectedresult in actualresult:

                enableModified = True
                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                sleep(10)

            else:

                tdkTestObj.setResultStatus("FAILURE")
                print("[TEST EXECUTION RESULT] : FAILURE")

        else:

            print("TEST STEP 2: Cellular interface is already enabled")
            print("EXPECTED RESULT 2: No configuration change required")
            print("ACTUAL RESULT 2: Device.Cellular.Interface.1.Enable is already true")
            print("[TEST EXECUTION RESULT] : SUCCESS")

        ############################################################
        # STEP 3 : Verify Device.Cellular.X_RDK_Status
        ############################################################

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.X_RDK_Status"
        )

        tdkTestObj.executeTestCase(expectedresult)

        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails().strip()

        print("TEST STEP 3: Get Device.Cellular.X_RDK_Status")
        print("EXPECTED RESULT 3: Device.Cellular.X_RDK_Status should be CONNECTED")
        print("ACTUAL RESULT 3: Status is %s" % details)

        if expectedresult in actualresult and details == "CONNECTED":

            tdkTestObj.setResultStatus("SUCCESS")
            print("[TEST EXECUTION RESULT] : SUCCESS")

            ############################################################
            # STEP 4 : Get wwan0 IP Address
            ############################################################

            tdkTestObj = sysobj.createTestStep('ExecuteCmd')
            tdkTestObj.addParameter(
                "command",
                "ifconfig wwan0 | grep 'inet addr' | cut -d ':' -f 2 | cut -d ' ' -f 1"
            )

            tdkTestObj.executeTestCase(expectedresult)

            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            ip_wwan0 = details[:-2] if len(details) > 2 else details.strip()

            print("TEST STEP 4: Get the wwan0 IP address")
            print("EXPECTED RESULT 4: Should obtain the wwan0 IP address")

            if expectedresult in actualresult and ip_wwan0 != "":

                tdkTestObj.setResultStatus("SUCCESS")

                print("ACTUAL RESULT 4: Successfully obtained wwan0 IP : %s" % ip_wwan0)
                print("[TEST EXECUTION RESULT] : SUCCESS")

                ############################################################
                # STEP 5 : Verify Internet Connectivity
                ############################################################

                tdkTestObj = sysobj.createTestStep('ExecuteCmd')

                query = "ping -c 2 google.com | grep -i \"0% packet loss\""
                print("query:%s" % query)

                tdkTestObj.addParameter("command", query)

                tdkTestObj.executeTestCase(expectedresult)

                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails()

                print("TEST STEP 5: Do a ping operation and check for internet connectivity")
                print("EXPECTED RESULT 5: Ping operation should be successful with 0% packet loss")

                if expectedresult in actualresult and details != "":

                    tdkTestObj.setResultStatus("SUCCESS")

                    print("ACTUAL RESULT 5: Ping operation is successful with active internet connectivity")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                else:

                    tdkTestObj.setResultStatus("FAILURE")

                    print("ACTUAL RESULT 5: Ping operation failed with no internet connectivity")
                    print("[TEST EXECUTION RESULT] : FAILURE")

            else:

                tdkTestObj.setResultStatus("FAILURE")

                print("ACTUAL RESULT 4: Failed to obtain wwan0 IP")
                print("[TEST EXECUTION RESULT] : FAILURE")

        else:

            tdkTestObj.setResultStatus("FAILURE")

            print("[TEST EXECUTION RESULT] : FAILURE")

        ############################################################
        # STEP 6 : Revert Interface Enable
        ############################################################

        if enableModified:

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
            details = tdkTestObj.getResultDetails()

            print("TEST STEP 6: Revert Device.Cellular.Interface.1.Enable to original value")
            print("EXPECTED RESULT 6: Device.Cellular.Interface.1.Enable should be restored to %s" % initialEnable)
            print("ACTUAL RESULT 6: %s" % details)

            if expectedresult in actualresult:

                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                sleep(10)

                ############################################################
                # STEP 7 : Verify Status After Revert
                ############################################################

                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                tdkTestObj.addParameter(
                    "ParamName",
                    "Device.Cellular.X_RDK_Status"
                )

                tdkTestObj.executeTestCase(expectedresult)

                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails().strip()

                print("TEST STEP 7: Verify Device.Cellular.X_RDK_Status after revert")
                print("EXPECTED RESULT 7: Device.Cellular.X_RDK_Status should be DEREGISTERED")
                print("ACTUAL RESULT 7: Status is %s" % details)

                if expectedresult in actualresult and details == "DEREGISTERED":

                    tdkTestObj.setResultStatus("SUCCESS")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                else:

                    tdkTestObj.setResultStatus("FAILURE")
                    print("[TEST EXECUTION RESULT] : FAILURE")

        else:

            print("TEST STEP 6: Revert not required")
            print("EXPECTED RESULT 6: Interface was already enabled before execution")
            print("ACTUAL RESULT 6: No revert performed")

    else:

        tdkTestObj.setResultStatus("FAILURE")
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")

else:

    print("Failed to load module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")



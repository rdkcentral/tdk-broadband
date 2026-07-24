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

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")

# IP and Port of box
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_CellularManager_GetCurrentAccessTechnology')

# Get the result of connection with test component and DUT
result = obj.getLoadModuleResult()
print("[LIB LOAD STATUS] : %s" % result)

if "SUCCESS" in result.upper():

    step = 1
    enableModified = False

    ############################################################
    # STEP 1 : Get Device.Cellular.Interface.1.Enable
    ############################################################

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.Interface.1.Enable"
    )

    expectedresult = "SUCCESS"
    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    initialEnable = tdkTestObj.getResultDetails().strip()

    print("\nTEST STEP %d : Get Device.Cellular.Interface.1.Enable" % step)
    print("EXPECTED RESULT %d : Should get Device.Cellular.Interface.1.Enable" % step)
    print("ACTUAL RESULT %d : Device.Cellular.Interface.1.Enable is %s"
          % (step, initialEnable))

    step += 1

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

        if expectedresult in actualresult:

            enableModified = True
            sleep(20)

    step += 1

    ############################################################
    # STEP 3 : Verify CONNECTED Status
    ############################################################

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.X_RDK_Status"
    )

    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    status = tdkTestObj.getResultDetails()

    print("\nTEST STEP %d : Verify Device.Cellular.X_RDK_Status" % step)
    print("EXPECTED RESULT %d : Device.Cellular.X_RDK_Status should be CONNECTED" % step)

    if expectedresult in actualresult and status == "CONNECTED":

        tdkTestObj.setResultStatus("SUCCESS")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1

        ############################################################
        # ORIGINAL SCRIPT STARTS HERE
        ############################################################

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.SupportedAccessTechnologies"
        )

        tdkTestObj.executeTestCase(expectedresult)

        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("\nTEST STEP %d : Get SupportedAccessTechnologies" % step)

        if expectedresult in actualresult:

            supported_technologies = details.split(",")

            step += 1

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
            tdkTestObj.addParameter(
                "ParamName",
                "Device.Cellular.Interface.1.CurrentAccessTechnology"
            )

            tdkTestObj.executeTestCase(expectedresult)

            actualresult = tdkTestObj.getResult()
            accessTechnology = tdkTestObj.getResultDetails()

            print("\nTEST STEP %d : Get CurrentAccessTechnology" % step)

            if expectedresult in actualresult:

                step += 1

                print("\nTEST STEP %d : Verify CurrentAccessTechnology" % step)

                if accessTechnology in supported_technologies:

                    tdkTestObj.setResultStatus("SUCCESS")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                else:

                    tdkTestObj.setResultStatus("FAILURE")
                    print("[TEST EXECUTION RESULT] : FAILURE")

        ############################################################
        # REVERT
        ############################################################

        if enableModified:

            step += 1

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
                  % step)

            if expectedresult in actualresult:

                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                sleep(20)

                step += 1

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
                      % step)

                if expectedresult in actualresult and \
                   restoreStatus == expectedRestoreStatus:

                    tdkTestObj.setResultStatus("SUCCESS")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                else:

                    tdkTestObj.setResultStatus("FAILURE")
                    print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("tdkbtr181")

else:

    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")

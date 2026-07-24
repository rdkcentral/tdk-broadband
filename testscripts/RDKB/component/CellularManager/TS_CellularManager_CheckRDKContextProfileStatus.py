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

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_CellularManager_CheckRDKContextProfileStatus')

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus)

print("Loading TDKB-TR181 module")

if "SUCCESS" in loadmodulestatus.upper():

    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"

    ############################################################
    # STEP 1 : Get Device.Cellular.Interface.1.Enable
    ############################################################

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    tdkTestObj.addParameter("ParamName","Device.Cellular.Interface.1.Enable")

    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails().strip()

    print("TEST STEP 1: Get Device.Cellular.Interface.1.Enable")
    print("EXPECTED RESULT 1: Should get Device.Cellular.Interface.1.Enable")

    if expectedresult in actualresult and details in ["true","false"]:

        initialValue = details
        toggleValue = "false" if initialValue == "true" else "true"

        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT 1: Device.Cellular.Interface.1.Enable is %s" % initialValue)
        print("[TEST EXECUTION RESULT] : SUCCESS")

        ############################################################
        # STEP 2 : Verify current status values
        ############################################################

        expectedRDKStatus = "CONNECTED" if initialValue == "true" else "DEREGISTERED"
        expectedContextStatus = "ACTIVE" if initialValue == "true" else "INACTIVE"

        # Verify Device.Cellular.X_RDK_Status
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
        tdkTestObj.addParameter("ParamName","Device.Cellular.X_RDK_Status")

        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        rdkStatus = tdkTestObj.getResultDetails().strip()

        print("TEST STEP 2: Verify Device.Cellular.X_RDK_Status")
        print("EXPECTED RESULT 2: Device.Cellular.X_RDK_Status should be %s" % expectedRDKStatus)
        print("ACTUAL RESULT 2: Device.Cellular.X_RDK_Status is %s" % rdkStatus)

        if expectedresult in actualresult and rdkStatus == expectedRDKStatus:
            tdkTestObj.setResultStatus("SUCCESS")
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("[TEST EXECUTION RESULT] : FAILURE")

        # Verify Context Profile Status

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.X_RDK_ContextProfile.1.Status"
        )

        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        contextStatus = tdkTestObj.getResultDetails().strip()

        print("TEST STEP 2a: Verify Device.Cellular.Interface.1.X_RDK_ContextProfile.1.Status")
        print("EXPECTED RESULT 2a: Status should be %s" % expectedContextStatus)
        print("ACTUAL RESULT 2a: Status is %s" % contextStatus)

        if expectedresult in actualresult and contextStatus == expectedContextStatus:
            tdkTestObj.setResultStatus("SUCCESS")
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("[TEST EXECUTION RESULT] : FAILURE")

        ############################################################
        # STEP 3 : Toggle Interface Enable
        ############################################################

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.Enable"
        )
        tdkTestObj.addParameter(
            "ParamValue",
            toggleValue
        )
        tdkTestObj.addParameter("Type","bool")

        tdkTestObj.executeTestCase(expectedresult)

        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP 3: Toggle Device.Cellular.Interface.1.Enable")
        print("EXPECTED RESULT 3: Device.Cellular.Interface.1.Enable should be set to %s" % toggleValue)
        print("ACTUAL RESULT 3: %s" % details)

        if expectedresult in actualresult:

            tdkTestObj.setResultStatus("SUCCESS")
            print("[TEST EXECUTION RESULT] : SUCCESS")

            sleep(10)

            ############################################################
            # STEP 4 : Verify Device.Cellular.X_RDK_Status after toggle
            ############################################################

            expectedRDKStatus = "CONNECTED" if toggleValue == "true" else "DEREGISTERED"

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
            tdkTestObj.addParameter("ParamName","Device.Cellular.X_RDK_Status")

            tdkTestObj.executeTestCase(expectedresult)

            actualresult = tdkTestObj.getResult()
            rdkStatus = tdkTestObj.getResultDetails().strip()

            print("TEST STEP 4: Verify Device.Cellular.X_RDK_Status after toggle")
            print("EXPECTED RESULT 4: Device.Cellular.X_RDK_Status should be %s" % expectedRDKStatus)
            print("ACTUAL RESULT 4: Device.Cellular.X_RDK_Status is %s" % rdkStatus)

            if expectedresult in actualresult and rdkStatus == expectedRDKStatus:
                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("[TEST EXECUTION RESULT] : FAILURE")

            ############################################################
            # STEP 5 : Verify Context Profile Status after toggle
            ############################################################

            expectedContextStatus = "ACTIVE" if toggleValue == "true" else "INACTIVE"

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
            tdkTestObj.addParameter(
                "ParamName",
                "Device.Cellular.Interface.1.X_RDK_ContextProfile.1.Status"
            )

            tdkTestObj.executeTestCase(expectedresult)

            actualresult = tdkTestObj.getResult()
            contextStatus = tdkTestObj.getResultDetails().strip()

            print("TEST STEP 5: Verify Device.Cellular.Interface.1.X_RDK_ContextProfile.1.Status after toggle")
            print("EXPECTED RESULT 5: Status should be %s" % expectedContextStatus)
            print("ACTUAL RESULT 5: Status is %s" % contextStatus)

            if expectedresult in actualresult and contextStatus == expectedContextStatus:
                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("[TEST EXECUTION RESULT] : FAILURE")

            ############################################################
            # STEP 6 : Revert to Original Value
            ############################################################

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
            tdkTestObj.addParameter(
                "ParamName",
                "Device.Cellular.Interface.1.Enable"
            )
            tdkTestObj.addParameter(
                "ParamValue",
                initialValue
            )
            tdkTestObj.addParameter(
                "Type",
                "bool"
            )

            tdkTestObj.executeTestCase(expectedresult)

            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            print("TEST STEP 6: Revert Device.Cellular.Interface.1.Enable to original value")
            print("EXPECTED RESULT 6: Device.Cellular.Interface.1.Enable should be restored to %s" % initialValue)
            print("ACTUAL RESULT 6: %s" % details)

            if expectedresult in actualresult:

                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                sleep(10)

                ############################################################
                # STEP 7 : Verify Device.Cellular.X_RDK_Status after revert
                ############################################################

                expectedRDKStatus = "CONNECTED" if initialValue == "true" else "DEREGISTERED"

                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                tdkTestObj.addParameter("ParamName","Device.Cellular.X_RDK_Status")

                tdkTestObj.executeTestCase(expectedresult)

                actualresult = tdkTestObj.getResult()
                rdkStatus = tdkTestObj.getResultDetails().strip()

                print("TEST STEP 7: Verify Device.Cellular.X_RDK_Status after revert")
                print("EXPECTED RESULT 7: Device.Cellular.X_RDK_Status should be %s" % expectedRDKStatus)
                print("ACTUAL RESULT 7: Device.Cellular.X_RDK_Status is %s" % rdkStatus)

                if expectedresult in actualresult and rdkStatus == expectedRDKStatus:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("[TEST EXECUTION RESULT] : FAILURE")

                ############################################################
                # STEP 8 : Verify Context Profile Status after revert
                ############################################################

                expectedContextStatus = "ACTIVE" if initialValue == "true" else "INACTIVE"

                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                tdkTestObj.addParameter(
                    "ParamName",
                    "Device.Cellular.Interface.1.X_RDK_ContextProfile.1.Status"
                )

                tdkTestObj.executeTestCase(expectedresult)

                actualresult = tdkTestObj.getResult()
                contextStatus = tdkTestObj.getResultDetails().strip()

                print("TEST STEP 8: Verify Device.Cellular.Interface.1.X_RDK_ContextProfile.1.Status after revert")
                print("EXPECTED RESULT 8: Status should be %s" % expectedContextStatus)
                print("ACTUAL RESULT 8: Status is %s" % contextStatus)

                if expectedresult in actualresult and contextStatus == expectedContextStatus:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("[TEST EXECUTION RESULT] : FAILURE")

            else:

                tdkTestObj.setResultStatus("FAILURE")
                print("[TEST EXECUTION RESULT] : FAILURE")

        else:

            tdkTestObj.setResultStatus("FAILURE")
            print("[TEST EXECUTION RESULT] : FAILURE")

    else:

        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT 1: Failed to get Device.Cellular.Interface.1.Enable")
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("tdkbtr181")

else:

    print("Failed to load module")
    obj.setLoadModuleStatus("FAILURE")

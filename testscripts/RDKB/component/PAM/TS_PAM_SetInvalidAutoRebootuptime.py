##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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

# Use tdklib library, which provides a wrapper for TDK test case scripts
import tdklib

# Test components
obj = tdklib.TDKScriptingLibrary("wifiagent", "1")
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181", "1")

# IP and Port of the DUT
# These values will be replaced during script execution
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port, 'TS_PAM_SetInvalidAutoRebootuptime')
obj1.configureTestCase(ip,port, 'TS_PAM_SetInvalidAutoRebootuptime')

# Get module loading status
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus1 = obj1.getLoadModuleResult()

flag = 0
SetValue = 0

if (
    "SUCCESS" in loadmodulestatus.upper()
    and "SUCCESS" in loadmodulestatus1.upper()
):
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"

    # Save the device state before factory reset
    obj.saveCurrentState()

    # Initiate factory reset
    tdkTestObj = obj.createTestStep("WIFIAgent_Set")
    tdkTestObj.addParameter(
        "paramName",
        "Device.X_CISCO_COM_DeviceControl.FactoryReset"
    )
    tdkTestObj.addParameter(
        "paramValue",
        "Router,Wifi,VoIP,Dect,MoCA"
    )
    tdkTestObj.addParameter("paramType", "string")
    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    print("TEST STEP 1: Initiate factory reset")
    print("EXPECTED RESULT 1: Should initiate factory reset")

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT 1: %s" % details)
        print("[TEST EXECUTION RESULT] : SUCCESS")

        # Restore the saved device connection state after reboot
        obj.restorePreviousStateAfterReboot()

        # Get AutoReboot Enable status
        tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_Get")
        tdkTestObj.addParameter(
            "ParamName",
            "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AutoReboot.Enable"
        )
        tdkTestObj.executeTestCase(expectedresult)

        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP 2: Get the Auto Reboot status")
        print(
            "EXPECTED RESULT 2: "
            "Should get the Auto Reboot status as enabled"
        )

        if expectedresult in actualresult and details.strip() == "true":
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT 2: %s" % details)
            print("[TEST EXECUTION RESULT] : SUCCESS")

            # Get initial AutoReboot UpTime
            tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_Get")
            tdkTestObj.addParameter(
                "ParamName",
                "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AutoReboot.UpTime"
            )
            tdkTestObj.executeTestCase(expectedresult)

            actualresult = tdkTestObj.getResult()
            defaultUptime = tdkTestObj.getResultDetails().strip()

            print("TEST STEP 3: Get the AutoReboot UpTime")
            print(
                "EXPECTED RESULT 3: "
                "Should get the Auto Reboot UpTime as 120"
            )

            if (
                expectedresult in actualresult
                and defaultUptime.isdigit()
                and int(defaultUptime) == 120
            ):
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT 3: %s" % defaultUptime)
                print("[TEST EXECUTION RESULT] : SUCCESS")

                # Valid range is 1 to 365
                InvalidValue = [-1, 0, 366, 367]
                flag = 0

                for invalid_value in InvalidValue:
                    print(
                        "Setting Auto Reboot UpTime to invalid value: %d"
                        % invalid_value
                    )

                    tdkTestObj = obj1.createTestStep(
                        "TDKB_TR181Stub_Set"
                    )
                    tdkTestObj.addParameter(
                        "ParamName",
                        "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC."
                        "Feature.AutoReboot.UpTime"
                    )
                    tdkTestObj.addParameter(
                        "ParamValue",
                        str(invalid_value)
                    )
                    tdkTestObj.addParameter("Type", "int")

                    set_expectedresult = "FAILURE"
                    tdkTestObj.executeTestCase(set_expectedresult)

                    actualresult = tdkTestObj.getResult()
                    Setresult = tdkTestObj.getResultDetails()
                    SetValue = invalid_value

                    if set_expectedresult in actualresult:
                        print(
                            "The invalid value %d failed to set as expected"
                            % SetValue
                        )
                    else:
                        flag = 1
                        print(
                            "The invalid value %d was unexpectedly accepted"
                            % SetValue
                        )
                        print("Details: %s" % Setresult)
                        break

                print(
                    "TEST STEP 4: "
                    "Set the AutoReboot UpTime to invalid values"
                )
                print(
                    "EXPECTED RESULT 4: "
                    "Should not set Auto Reboot UpTime to invalid values"
                )

                if flag == 0:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(
                        "ACTUAL RESULT 4: "
                        "All invalid Auto Reboot UpTime values were rejected"
                    )
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(
                        "ACTUAL RESULT 4: "
                        "Auto Reboot UpTime accepted the invalid value %d"
                        % SetValue
                    )
                    print("[TEST EXECUTION RESULT] : FAILURE")

                    # Revert AutoReboot UpTime to its initial value
                    tdkTestObj = obj1.createTestStep(
                        "TDKB_TR181Stub_Set"
                    )
                    tdkTestObj.addParameter(
                        "ParamName",
                        "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC."
                        "Feature.AutoReboot.UpTime"
                    )
                    tdkTestObj.addParameter(
                        "ParamValue",
                        str(defaultUptime)
                    )
                    tdkTestObj.addParameter("Type", "int")

                    revert_expectedresult = "SUCCESS"
                    tdkTestObj.executeTestCase(
                        revert_expectedresult
                    )

                    actualresult = tdkTestObj.getResult()
                    revertResult = tdkTestObj.getResultDetails()

                    print(
                        "TEST STEP 5: "
                        "Revert AutoReboot UpTime to its initial value"
                    )
                    print(
                        "EXPECTED RESULT 5: "
                        "Should revert AutoReboot UpTime to %s"
                        % defaultUptime
                    )

                    if revert_expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(
                            "ACTUAL RESULT 5: "
                            "Revert operation was successful. Details: %s"
                            % revertResult
                        )
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        # Validate the reverted value using GET
                        tdkTestObj = obj1.createTestStep(
                            "TDKB_TR181Stub_Get"
                        )
                        tdkTestObj.addParameter(
                            "ParamName",
                            "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC."
                            "Feature.AutoReboot.UpTime"
                        )
                        tdkTestObj.executeTestCase(
                            revert_expectedresult
                        )

                        actualresult = tdkTestObj.getResult()
                        revertedUptime = (
                            tdkTestObj.getResultDetails().strip()
                        )

                        print(
                            "TEST STEP 6: "
                            "Validate the reverted AutoReboot UpTime"
                        )
                        print(
                            "EXPECTED RESULT 6: "
                            "AutoReboot UpTime should be restored to %s"
                            % defaultUptime
                        )

                        if (
                            revert_expectedresult in actualresult
                            and revertedUptime == defaultUptime
                        ):
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(
                                "ACTUAL RESULT 6: "
                                "AutoReboot UpTime was restored to %s"
                                % revertedUptime
                            )
                            print(
                                "[TEST EXECUTION RESULT] : SUCCESS"
                            )
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(
                                "ACTUAL RESULT 6: "
                                "AutoReboot UpTime was not restored. "
                                "Expected: %s, Actual: %s"
                                % (defaultUptime, revertedUptime)
                            )
                            print(
                                "[TEST EXECUTION RESULT] : FAILURE"
                            )
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(
                            "ACTUAL RESULT 5: "
                            "Failed to revert AutoReboot UpTime. "
                            "Details: %s"
                            % revertResult
                        )
                        print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT 3: %s" % defaultUptime)
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT 2: %s" % details)
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT 1: %s" % details)
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload modules
    obj.unloadModule("wifiagent")
    obj1.unloadModule("tdkbtr181")

else:
    print("Failed to load wifiagent or tdkbtr181 module")
    obj.setLoadModuleStatus("FAILURE")
    obj1.setLoadModuleStatus("FAILURE")
    print("Module loading failed")


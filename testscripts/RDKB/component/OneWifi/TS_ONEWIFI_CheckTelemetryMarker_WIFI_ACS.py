##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2024 RDK Management
#
# Licensed under the Apache License, Version 2.0 (the "License")
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

# Import statements
import tdklib
from time import sleep
import re

# Test component to be tested
pamobj = tdklib.TDKScriptingLibrary("pam", "1")
sysObj = tdklib.TDKScriptingLibrary("sysutil", "1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding Box IP and port while executing script
ip = <ipaddress>
port = <port>
pamobj.configureTestCase(ip,port, 'TS_ONEWIFI_CheckTelemetryMarker_WIFI_ACS')
sysObj.configureTestCase(ip,port, 'TS_ONEWIFI_CheckTelemetryMarker_WIFI_ACS')

# Get the result of connection with test component and DUT
pamloadmodulestatus = pamobj.getLoadModuleResult()
sysutilloadmodulestatus = sysObj.getLoadModuleResult()

step = 0
flag = 0
revertflag = 0

if "SUCCESS" in pamloadmodulestatus.upper() and "SUCCESS" in sysutilloadmodulestatus.upper():
    pamobj.setLoadModuleStatus("SUCCESS")
    sysObj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"

    # Get TelemetryEnable
    tdkTestObj = pamobj.createTestStep('pam_GetParameterValues')
    tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    initial_TelemetrylogEnable = tdkTestObj.getResultDetails()

    step = step + 1
    print("TEST STEP %s: Get the TelemetryEnable" % step)
    print("EXPECTED RESULT %s: Should get TelemetryEnable" % step)

    if expectedresult in actualresult:
        flag = 1
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %s: TelemetryEnable is %s " % (step, initial_TelemetrylogEnable))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        # If TelemetryEnable is false, enable it
        if initial_TelemetrylogEnable == "false":
            step = step + 1
            tdkTestObj = pamobj.createTestStep('pam_SetParameterValues')
            tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable")
            tdkTestObj.addParameter("ParamValue", "true")
            tdkTestObj.addParameter("Type", "bool")
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()

            print("TEST STEP %s: Set the TelemetryEnable to true" % step)
            print("EXPECTED RESULT %s: Should set the TelemetryEnable to true" % step)

            if expectedresult in actualresult:
                flag = 1
                revertflag = 1
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %s: TelemetryEnable changed successfully" % step)
                print("[TEST EXECUTION RESULT] : SUCCESS")

                # Verify TelemetryEnable with GET
                step = step + 1
                tdkTestObj = pamobj.createTestStep('pam_GetParameterValues')
                tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable")
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                TelemetrylogEnable = tdkTestObj.getResultDetails()

                print("TEST STEP %s: Get the TelemetryEnable" % step)
                print("EXPECTED RESULT %s: Should get TelemetryEnable" % step)

                if expectedresult in actualresult and TelemetrylogEnable == "true":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %s: TelemetryEnable is %s " % (step, TelemetrylogEnable))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    flag = 0
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %s: Failed to get expected TelemetryEnable value" % step)
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                flag = 0
                revertflag = 0
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %s: Failed to set TelemetryEnable" % step)
                print("[TEST EXECUTION RESULT] : FAILURE")

        # Set the loginterval to 300 seconds if Telemetry enable is true
        if flag == 1:
            # Get loginterval and store it
            step = step + 1
            tdkTestObj = pamobj.createTestStep('pam_GetParameterValues')
            tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval")
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            TelemetrylogInterval = tdkTestObj.getResultDetails()

            print("TEST STEP %s: Get the Telemetry LogInterval and store it" % step)
            print("EXPECTED RESULT %s: Should get the Telemetry LogInterval" % step)

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %s: Telemetry LogInterval get successful: %s" % (step, TelemetrylogInterval))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step = step + 1
                tdkTestObj = pamobj.createTestStep('pam_SetParameterValues')
                tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval")
                tdkTestObj.addParameter("ParamValue", "300")
                tdkTestObj.addParameter("Type", "int")
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()

                print("TEST STEP %s: Set the Telemetry LogInterval to 5 min" % step)
                print("EXPECTED RESULT %s: Should set the Telemetry LogInterval to 5 min" % step)

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %s: Telemetry LogInterval set to 5 min" % step)
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    # Get the loginterval and verify
                    step = step + 1
                    tdkTestObj = pamobj.createTestStep('pam_GetParameterValues')
                    tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval")
                    expectedresult = "SUCCESS"
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    loginterval = tdkTestObj.getResultDetails()

                    print("TEST STEP %s: Get the Telemetry LogInterval" % step)
                    print("EXPECTED RESULT %s: Should get the Telemetry LogInterval" % step)

                    if expectedresult in actualresult and loginterval == "300":
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %s: Telemetry LogInterval: %s" % (step, loginterval))
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        # Check whether the wifihealth.txt file is present or not
                        step = step + 1
                        tdkTestObj = sysObj.createTestStep('ExecuteCmd')
                        cmd = "[ -f /rdklogs/logs/wifihealth.txt ] && echo \"File exist\" || echo \"File does not exist\""
                        tdkTestObj.addParameter("command", cmd)
                        expectedresult = "SUCCESS"
                        tdkTestObj.executeTestCase(expectedresult)
                        actualresult = tdkTestObj.getResult()
                        details = tdkTestObj.getResultDetails().strip().replace("\\n", "")

                        print("TEST STEP %s: Check for wifihealth log file presence" % step)
                        print("EXPECTED RESULT %s: wifihealth log file should be present" % step)

                        if details == "File exist":
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %s: wifihealth log file is present" % step)
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                            # Check for any WIFI_ACS telemetry marker
                            step = step + 1
                            print("TEST STEP %s: Check for the presence of WIFI_ACS telemetry marker in wifihealth.txt" % step)
                            print("EXPECTED RESULT %s: WIFI_ACS telemetry marker should be present in wifihealth.txt" % step)

                            markerfound = 0
                            wifi_acs_value = ""
                            wifi_acs_marker_name = ""

                            for iteration in range(1, 6):
                                print("Waiting for the marker to get populated in wifihealth.txt....\nIteration : %s" % iteration)

                                query = "cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_ACS_\" | grep -vi \"TOTAL_COUNT\" | tail -1"
                                tdkTestObj = sysObj.createTestStep('ExecuteCmd')
                                tdkTestObj.addParameter("command", query)
                                expectedresult = "SUCCESS"
                                tdkTestObj.executeTestCase(expectedresult)
                                actualresult = tdkTestObj.getResult()
                                details = tdkTestObj.getResultDetails().strip().replace("\\n", "")

                                if expectedresult in actualresult and "WIFI_ACS_" in details:
                                    marker_match = re.search(r"(WIFI_ACS_[0-9]+):\s*([^,\s]+)", details, re.IGNORECASE)

                                    if marker_match:
                                        wifi_acs_marker_name = marker_match.group(1)
                                        wifi_acs_value = marker_match.group(2).strip()
                                        markerfound = 1
                                        break
                                    else:
                                        markerfound = 0
                                        sleep(60)
                                        continue
                                else:
                                    markerfound = 0
                                    sleep(60)
                                    continue

                            if markerfound == 1 and wifi_acs_value != "":
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %s: %s marker is found in wifihealth.txt with value: %s" % (step, wifi_acs_marker_name, wifi_acs_value))
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                # Validate WIFI_ACS marker value
                                step = step + 1
                                print("TEST STEP %s: Validate the WIFI_ACS telemetry marker value" % step)
                                print("EXPECTED RESULT %s: WIFI_ACS telemetry marker value should be non-empty and should be either true/false or 0/1" % step)

                                if wifi_acs_value.lower() in ["true", "false", "0", "1"]:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print("ACTUAL RESULT %s: WIFI_ACS telemetry marker value is valid: %s" % (step, wifi_acs_value))
                                    print("[TEST EXECUTION RESULT] : SUCCESS")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("ACTUAL RESULT %s: WIFI_ACS telemetry marker value is invalid: %s" % (step, wifi_acs_value))
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %s: WIFI_ACS telemetry marker is not found Details: %s" % (step, details))
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %s: wifihealth log file is not present" % step)
                            print("[TEST EXECUTION RESULT] : FAILURE")

                        # Revert the LogInterval
                        step = step + 1
                        tdkTestObj = pamobj.createTestStep('pam_SetParameterValues')
                        tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval")
                        tdkTestObj.addParameter("ParamValue", TelemetrylogInterval)
                        tdkTestObj.addParameter("Type", "int")
                        tdkTestObj.executeTestCase(expectedresult)
                        actualresult = tdkTestObj.getResult()

                        print("TEST STEP %s: Change the LogInterval to initial value" % step)
                        print("EXPECTED RESULT %s: Should change value of LogInterval to initial value" % step)

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %s: LogInterval changed to initial value successfully" % step)
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %s: Failed to change LogInterval to initial value" % step)
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %s: Failed to get expected Telemetry LogInterval value. Current value: %s" % (step, loginterval))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %s: Failed to set Telemetry LogInterval" % step)
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %s: Failed to get Telemetry LogInterval" % step)
                print("[TEST EXECUTION RESULT] : FAILURE")

            # Revert TelemetryEnable
            if revertflag == 1:
                step = step + 1
                tdkTestObj = pamobj.createTestStep('pam_SetParameterValues')
                tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable")
                tdkTestObj.addParameter("ParamValue", initial_TelemetrylogEnable)
                tdkTestObj.addParameter("Type", "bool")
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()

                print("TEST STEP %s: Change the TelemetryEnable to initial value" % step)
                print("EXPECTED RESULT %s: Should change value of TelemetryEnable to initial value" % step)

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %s: TelemetryEnable changed to initial value successfully" % step)
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %s: Failed to change TelemetryEnable to initial value" % step)
                    print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("Telemetry logger was disabled and failed on enabling")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %s: Failed to get TelemetryEnable" % step)
        print("[TEST EXECUTION RESULT] : FAILURE")

    pamobj.unloadModule("pam")
    sysObj.unloadModule("sysutil")
else:
    print("Failed to load pam/sysutil module")
    pamobj.setLoadModuleStatus("FAILURE")
    sysObj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

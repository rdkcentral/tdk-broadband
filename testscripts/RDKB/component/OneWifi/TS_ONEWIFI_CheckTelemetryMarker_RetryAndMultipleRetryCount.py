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

# use tdklib library, which provides a wrapper for tdk testcase script
import tdklib
from time import sleep
import re

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam", "RDKB")
sysObj = tdklib.TDKScriptingLibrary("sysutil", "RDKB")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT IP and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port, 'TS_ONEWIFI_CheckTelemetryMarker_RetryAndMultipleRetryCount')
sysObj.configureTestCase(ip,port, 'TS_ONEWIFI_CheckTelemetryMarker_RetryAndMultipleRetryCount')

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
sysutilloadmodulestatus = sysObj.getLoadModuleResult()
revertflag = 0
flag = 1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysutilloadmodulestatus.upper():
    # Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    sysObj.setLoadModuleStatus("SUCCESS")

    tdkTestObj = obj.createTestStep('pam_GetParameterValues')
    tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable")
    expectedresult = "SUCCESS"

    # Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    logEnable = tdkTestObj.getResultDetails()

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("TEST STEP 1: Get the Telemetry Enable state ")
        print("EXPECTED RESULT 1: Should get the TELEMETRY Enable state")
        print("ACTUAL RESULT 1: TELEMETRY Enable state :", logEnable)
        print("[TEST EXECUTION RESULT] : SUCCESS")

        if logEnable == "false":
            tdkTestObj = obj.createTestStep('pam_SetParameterValues')
            tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable")
            tdkTestObj.addParameter("ParamValue", "true")
            tdkTestObj.addParameter("Type", "bool")
            expectedresult = "SUCCESS"
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            if expectedresult in actualresult:
                flag = 1
                revertflag = 1
                tdkTestObj.setResultStatus("SUCCESS")
                print("TEST STEP 2: Set the Telemetry Enable state to true")
                print("EXPECTED RESULT 2: Should set the TELEMETRY Enable state to true")
                print("ACTUAL RESULT 2: TELEMETRY Enable state :", details)
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                flag = 0
                revertflag = 0
                tdkTestObj.setResultStatus("FAILURE")
                print("TEST STEP 2: Set the Telemetry Enable state to true")
                print("EXPECTED RESULT 2: Should set the TELEMETRY Enable state to true")
                print("ACTUAL RESULT 2: TELEMETRY Enable state :", details)
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            print("Telemetry Enable state is already enabled, not required to change it")

        if flag == 1:
            tdkTestObj = obj.createTestStep('pam_GetParameterValues')
            tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval")
            expectedresult = "SUCCESS"

            # Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            DeflogInt = tdkTestObj.getResultDetails()

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print("TEST STEP 2: Get the TELEMETRY LogInterval")
                print("EXPECTED RESULT 2: Should get the TELEMETRY LogInterval")
                print("ACTUAL RESULT 2: TELEMETRY LogInterval:", DeflogInt)
                print("[TEST EXECUTION RESULT] : SUCCESS")

                tdkTestObj = obj.createTestStep('pam_SetParameterValues')
                tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval")
                tdkTestObj.addParameter("ParamValue", "300")
                tdkTestObj.addParameter("Type", "int")
                expectedresult = "SUCCESS"
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails()

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("TEST STEP 3: Set the TELEMETRY LogInterval to 5 min")
                    print("EXPECTED RESULT 3: Should set the TELEMETRY LogInterval to 5 min")
                    print("ACTUAL RESULT 3: TELEMETRY LogInterval:", details)
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    # Check whether the wifihealth.txt file is present or not
                    tdkTestObj = sysObj.createTestStep('ExecuteCmd')
                    cmd = "[ -f /rdklogs/logs/wifihealth.txt ] && echo \"File exist\" || echo \"File does not exist\""
                    tdkTestObj.addParameter("command", cmd)
                    expectedresult = "SUCCESS"
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "")

                    if details == "File exist":
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("TEST STEP 4: Check for wifihealth log file presence")
                        print("EXPECTED RESULT 4: wifihealth log file should be present")
                        print("ACTUAL RESULT 4: wifihealth log file is present")
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        markerfound = 0
                        tel_retrycount = ""
                        retry_marker_name = ""

                        for i in range(1, 6):
                            if markerfound == 1:
                                break
                            else:
                                # Query for any WIFI_RETRYCOUNT telemetry marker
                                query = "cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_RETRYCOUNT_\" | grep -vi \"TOTAL_COUNT\" | tail -1"
                                print("query:%s" % query)

                                tdkTestObj = sysObj.createTestStep('ExecuteCmd')
                                tdkTestObj.addParameter("command", query)
                                expectedresult = "SUCCESS"
                                tdkTestObj.executeTestCase(expectedresult)
                                actualresult = tdkTestObj.getResult()
                                details = tdkTestObj.getResultDetails().strip().replace("\\n", "")
                                print("Marker Detail Found from Log file is: %s " % details)

                                if len(details) == 0 or "WIFI_RETRYCOUNT_" not in details:
                                    markerfound = 0
                                    sleep(60)
                                else:
                                    marker_match = re.search(r"(WIFI_RETRYCOUNT_[0-9]+):\s*([0-9]+)", details, re.IGNORECASE)

                                    if marker_match:
                                        retry_marker_name = marker_match.group(1)
                                        tel_retrycount = marker_match.group(2).strip()
                                        markerfound = 1
                                    else:
                                        markerfound = 0
                                        sleep(60)

                        if expectedresult in actualresult and markerfound == 1 and tel_retrycount != "":
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("TEST STEP 5: WIFI_RETRYCOUNT telemetry marker should be present")
                            print("EXPECTED RESULT 5: WIFI_RETRYCOUNT telemetry marker should be present and value should be retrieved")
                            print("ACTUAL RESULT 5: %s Marker is %s" % (retry_marker_name, tel_retrycount))
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                            if int(tel_retrycount) > 0:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("TEST STEP 6: Check if RETRYCOUNT telemetry marker value is greater than zero")
                                print("EXPECTED RESULT 6: RETRYCOUNT telemetry marker value should be greater than zero")
                                print("ACTUAL RESULT 6: RETRYCOUNT telemetry marker value:", tel_retrycount)
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("TEST STEP 6: Check if RETRYCOUNT telemetry marker value is greater than zero")
                                print("EXPECTED RESULT 6: RETRYCOUNT telemetry marker value should be greater than zero")
                                print("ACTUAL RESULT 6: RETRYCOUNT telemetry marker value:", tel_retrycount)
                                print("[TEST EXECUTION RESULT] : FAILURE")

                            markerfound = 0
                            tel_mretrycount = ""
                            multiple_retry_marker_name = ""

                            for i in range(1, 6):
                                if markerfound == 1:
                                    break
                                else:
                                    # Query for any WIFI_MULTIPLERETRYCOUNT telemetry marker
                                    query = "cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_MULTIPLERETRYCOUNT_\" | grep -vi \"TOTAL_COUNT\" | tail -1"
                                    print("query:%s" % query)

                                    tdkTestObj = sysObj.createTestStep('ExecuteCmd')
                                    tdkTestObj.addParameter("command", query)
                                    expectedresult = "SUCCESS"
                                    tdkTestObj.executeTestCase(expectedresult)
                                    actualresult = tdkTestObj.getResult()
                                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "")
                                    print("Marker Detail Found from Log file is: %s " % details)

                                    if len(details) == 0 or "WIFI_MULTIPLERETRYCOUNT_" not in details:
                                        markerfound = 0
                                        sleep(60)
                                    else:
                                        marker_match = re.search(r"(WIFI_MULTIPLERETRYCOUNT_[0-9]+):\s*([0-9]+)", details, re.IGNORECASE)

                                        if marker_match:
                                            multiple_retry_marker_name = marker_match.group(1)
                                            tel_mretrycount = marker_match.group(2).strip()
                                            markerfound = 1
                                        else:
                                            markerfound = 0
                                            sleep(60)

                            if expectedresult in actualresult and markerfound == 1 and tel_mretrycount != "":
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("TEST STEP 7: WIFI_MULTIPLERETRYCOUNT telemetry marker should be present")
                                print("EXPECTED RESULT 7: WIFI_MULTIPLERETRYCOUNT telemetry marker should be present and value should be retrieved")
                                print("ACTUAL RESULT 7: %s Marker is %s" % (multiple_retry_marker_name, tel_mretrycount))
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                if int(tel_mretrycount) > 0:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print("TEST STEP 8: Check if MULTIPLERETRYCOUNT telemetry marker value is greater than zero")
                                    print("EXPECTED RESULT 8: MULTIPLERETRYCOUNT telemetry marker value should be greater than zero")
                                    print("ACTUAL RESULT 8: MULTIPLERETRYCOUNT telemetry marker value:", tel_mretrycount)
                                    print("[TEST EXECUTION RESULT] : SUCCESS")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("TEST STEP 8: Check if MULTIPLERETRYCOUNT telemetry marker value is greater than zero")
                                    print("EXPECTED RESULT 8: MULTIPLERETRYCOUNT telemetry marker value should be greater than zero")
                                    print("ACTUAL RESULT 8: MULTIPLERETRYCOUNT telemetry marker value:", tel_mretrycount)
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("TEST STEP 7: WIFI_MULTIPLERETRYCOUNT telemetry marker should be present")
                                print("EXPECTED RESULT 7: WIFI_MULTIPLERETRYCOUNT telemetry marker should be present")
                                print("ACTUAL RESULT 7: WIFI_MULTIPLERETRYCOUNT telemetry marker not present")
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("TEST STEP 5: WIFI_RETRYCOUNT telemetry marker should be present")
                            print("EXPECTED RESULT 5: WIFI_RETRYCOUNT telemetry marker should be present")
                            print("ACTUAL RESULT 5: WIFI_RETRYCOUNT telemetry marker not present")
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("TEST STEP 4: Check for wifihealth log file presence")
                        print("EXPECTED RESULT 4: wifihealth log file should be present")
                        print("ACTUAL RESULT 4: wifihealth log file is not present")
                        print("[TEST EXECUTION RESULT] : FAILURE")

                    # Revert the Value
                    tdkTestObj = obj.createTestStep('pam_SetParameterValues')
                    tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval")
                    tdkTestObj.addParameter("ParamValue", DeflogInt)
                    tdkTestObj.addParameter("Type", "int")
                    expectedresult = "SUCCESS"
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    details = tdkTestObj.getResultDetails()

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("TEST STEP 9: Revert the TELEMETRY LogInterval to previous")
                        print("EXPECTED RESULT 9: Should revert the TELEMETRY LogInterval to previous")
                        print("ACTUAL RESULT 9: Revert successfull")
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("TEST STEP 9: Revert the TELEMETRY LogInterval to previous")
                        print("EXPECTED RESULT 9: Should revert the TELEMETRY LogInterval to previous")
                        print("ACTUAL RESULT 9: Revertion failed")
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("TEST STEP 3: Set the TELEMETRY LogInterval to 5 min")
                    print("EXPECTED RESULT 3: Should set the TELEMETRY LogInterval to 5 min")
                    print("ACTUAL RESULT 3: TELEMETRY LogInterval:", details)
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("TEST STEP 2: Get the TELEMETRY LogInterval")
                print("EXPECTED RESULT 2: Should get the TELEMETRY LogInterval")
                print("ACTUAL RESULT 2: TELEMETRY LogInterval:", DeflogInt)
                print("[TEST EXECUTION RESULT] : FAILURE")

            if revertflag == 1:
                # Revert the value
                tdkTestObj = obj.createTestStep('pam_SetParameterValues')
                tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable")
                tdkTestObj.addParameter("ParamValue", logEnable)
                tdkTestObj.addParameter("Type", "bool")
                expectedresult = "SUCCESS"
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails()

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("TEST STEP 10: Revert the Telemetry Enable status to previous")
                    print("EXPECTED RESULT 10: Should revert the Telemetry Enable status to previous")
                    print("ACTUAL RESULT 10: Revert successfull")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("TEST STEP 10: Revert the Telemetry Enable status to previous")
                    print("EXPECTED RESULT 10: Should revert the Telemetry Enable status to previous")
                    print("ACTUAL RESULT 10: Revertion failed")
                    print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            print("Telemetry logger was disbled and failed on enabling")
            tdkTestObj.setResultStatus("FAILURE")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("TEST STEP 1: Get the Telemetry Enable state ")
        print("EXPECTED RESULT 1: Should get the TELEMETRY Enable state")
        print("ACTUAL RESULT 1: TELEMETRY Enable state :", logEnable)
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("pam")
    sysObj.unloadModule("sysutil")
else:
    print("Failed to load pam/sysutil module")
    obj.setLoadModuleStatus("FAILURE")
    sysObj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

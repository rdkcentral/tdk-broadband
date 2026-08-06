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
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB")

# IP and Port of box, No need to change,
# This will be replaced with corresponding Box IP and port while executing script
ip = <ipaddress>
port = <port>

sysObj.configureTestCase(ip,port,'TS_ONEWIFI_CheckTelemetryMarker_WiFiClientRxTxValue')

# Get the result of connection with test component and DUT
loadmodulestatus = sysObj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper():

    # Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"

    tdkTestObj = sysObj.createTestStep('ExecuteCmd')
    cmd = "[ -f /rdklogs/logs/wifihealth.txt ] && echo \"File exist\" || echo \"File does not exist\""
    tdkTestObj.addParameter("command",cmd)
    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails().strip().replace("\\n","")

    if details == "File exist":

        tdkTestObj.setResultStatus("SUCCESS")
        print("TEST STEP 1: Check for wifihealth log file presence")
        print("EXPECTED RESULT 1: wifihealth log file should be present")
        print("ACTUAL RESULT 1: wifihealth log file is present")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        markerfound = 0
        telemetryRXClientValue = ""
        rx_marker_name = ""

        for i in range(1,15):

            if markerfound == 1:

                break

            else:

                query = "cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_RXCLIENTS_\" | grep -vi \"TOTAL_COUNT\" | tail -1"
                print("query:%s" %query)

                tdkTestObj = sysObj.createTestStep('ExecuteCmd')
                tdkTestObj.addParameter("command",query)
                expectedresult = "SUCCESS"
                tdkTestObj.executeTestCase(expectedresult)

                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails().strip().replace("\\n","")

                print("Marker Detail Found from Log file is: %s " %details)

                if len(details) == 0 or "WIFI_RXCLIENTS_" not in details:

                    markerfound = 0
                    sleep(60)

                else:

                    marker_match = re.search(
                        r"(WIFI_RXCLIENTS_[0-9]+):\s*([0-9]+)",
                        details,
                        re.IGNORECASE
                    )

                    if marker_match:

                        rx_marker_name = marker_match.group(1)
                        telemetryRXClientValue = marker_match.group(2).strip()
                        markerfound = 1

                    else:

                        markerfound = 0
                        sleep(60)

        if expectedresult in actualresult and markerfound == 1 and telemetryRXClientValue != "":

            tdkTestObj.setResultStatus("SUCCESS")
            print("TEST STEP 2: WIFI_RXCLIENTS telemetry marker should be present")
            print("EXPECTED RESULT 2: WIFI_RXCLIENTS telemetry marker should be present and value should be retrieved")
            print("ACTUAL RESULT 2: %s Marker is %s" %(rx_marker_name,telemetryRXClientValue))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            if int(telemetryRXClientValue) >= 0:

                tdkTestObj.setResultStatus("SUCCESS")
                print("TEST STEP 3: Check if RXCLIENTS telemetry marker value is greater than or equal to zero")
                print("EXPECTED RESULT 3: RXCLIENTS telemetry marker value should be greater than or equal to zero")
                print("ACTUAL RESULT 3: RXCLIENTS telemetry marker value:",telemetryRXClientValue)
                print("[TEST EXECUTION RESULT] : SUCCESS")

            else:

                tdkTestObj.setResultStatus("FAILURE")
                print("TEST STEP 3: Check if RXCLIENTS telemetry marker value is greater than or equal to zero")
                print("EXPECTED RESULT 3: RXCLIENTS telemetry marker value should be greater than or equal to zero")
                print("ACTUAL RESULT 3: RXCLIENTS telemetry marker value:",telemetryRXClientValue)
                print("[TEST EXECUTION RESULT] : FAILURE")

            markerfound = 0
            telemetryTXClientValue = ""
            tx_marker_name = ""

            for i in range(1,15):

                if markerfound == 1:

                    break

                else:

                    query = "cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_TXCLIENTS_\" | grep -vi \"TOTAL_COUNT\" | tail -1"
                    print("query:%s" %query)

                    tdkTestObj = sysObj.createTestStep('ExecuteCmd')
                    tdkTestObj.addParameter("command",query)
                    expectedresult = "SUCCESS"
                    tdkTestObj.executeTestCase(expectedresult)

                    actualresult = tdkTestObj.getResult()
                    details = tdkTestObj.getResultDetails().strip().replace("\\n","")

                    print("Marker Detail Found from Log file is: %s " %details)

                    if len(details) == 0 or "WIFI_TXCLIENTS_" not in details:

                        markerfound = 0
                        sleep(60)

                    else:

                        marker_match = re.search(
                            r"(WIFI_TXCLIENTS_[0-9]+):\s*([0-9]+)",
                            details,
                            re.IGNORECASE
                        )

                        if marker_match:

                            tx_marker_name = marker_match.group(1)
                            telemetryTXClientValue = marker_match.group(2).strip()
                            markerfound = 1

                        else:

                            markerfound = 0
                            sleep(60)

            if expectedresult in actualresult and markerfound == 1 and telemetryTXClientValue != "":

                tdkTestObj.setResultStatus("SUCCESS")
                print("TEST STEP 4: WIFI_TXCLIENTS telemetry marker should be present")
                print("EXPECTED RESULT 4: WIFI_TXCLIENTS telemetry marker should be present and value should be retrieved")
                print("ACTUAL RESULT 4: %s Marker is %s" %(tx_marker_name,telemetryTXClientValue))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                if int(telemetryTXClientValue) >= 0:

                    tdkTestObj.setResultStatus("SUCCESS")
                    print("TEST STEP 5: Check if TXCLIENTS telemetry marker value is greater than or equal to zero")
                    print("EXPECTED RESULT 5: TXCLIENTS telemetry marker value should be greater than or equal to zero")
                    print("ACTUAL RESULT 5: TXCLIENTS telemetry marker value:",telemetryTXClientValue)
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                else:

                    tdkTestObj.setResultStatus("FAILURE")
                    print("TEST STEP 5: Check if TXCLIENTS telemetry marker value is greater than or equal to zero")
                    print("EXPECTED RESULT 5: TXCLIENTS telemetry marker value should be greater than or equal to zero")
                    print("ACTUAL RESULT 5: TXCLIENTS telemetry marker value:",telemetryTXClientValue)
                    print("[TEST EXECUTION RESULT] : FAILURE")

            else:

                tdkTestObj.setResultStatus("FAILURE")
                print("TEST STEP 4: WIFI_TXCLIENTS telemetry marker should be present")
                print("EXPECTED RESULT 4: WIFI_TXCLIENTS telemetry marker should be present")
                print("ACTUAL RESULT 4: WIFI_TXCLIENTS telemetry marker is not present")
                print("[TEST EXECUTION RESULT] : FAILURE")

        else:

            tdkTestObj.setResultStatus("FAILURE")
            print("TEST STEP 2: WIFI_RXCLIENTS telemetry marker should be present")
            print("EXPECTED RESULT 2: WIFI_RXCLIENTS telemetry marker should be present")
            print("ACTUAL RESULT 2: WIFI_RXCLIENTS telemetry marker is not present")
            print("[TEST EXECUTION RESULT] : FAILURE")

    else:

        tdkTestObj.setResultStatus("FAILURE")
        print("TEST STEP 1: Check for wifihealth log file presence")
        print("EXPECTED RESULT 1: wifihealth log file should be present")
        print("ACTUAL RESULT 1: wifihealth log file is NOT present")
        print("[TEST EXECUTION RESULT] : FAILURE")

    sysObj.unloadModule("sysutil")

else:

    print("Failed to load sysutil module")
    sysObj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

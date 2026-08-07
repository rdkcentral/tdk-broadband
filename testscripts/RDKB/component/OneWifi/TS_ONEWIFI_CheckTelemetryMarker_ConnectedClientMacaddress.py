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
sysObj = tdklib.TDKScriptingLibrary("sysutil", "RDKB")

# IP and Port of box, No need to change,
# This will be replaced with corresponding Box IP and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port, 'TS_ONEWIFI_CheckTelemetryMarker_ConnectedClientMacaddress')

# Get the result of connection with test component and DUT
sysutilloadmodulestatus = sysObj.getLoadModuleResult()

if "SUCCESS" in sysutilloadmodulestatus.upper():
    # Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"

    # Check whether the wifihealth.txt file is present or not
    tdkTestObj = sysObj.createTestStep('ExecuteCmd')
    cmd = "[ -f /rdklogs/logs/wifihealth.txt ] && echo \"File exist\" || echo \"File does not exist\""
    tdkTestObj.addParameter("command", cmd)
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "")

    if details == "File exist":
        tdkTestObj.setResultStatus("SUCCESS")
        print("TEST STEP 1: Check for wifihealth log file presence")
        print("EXPECTED RESULT 1: wifihealth log file should be present")
        print("ACTUAL RESULT 1: wifihealth log file is present")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        markerfound = 0
        telemetryMacaddress = ""
        mac_marker_name = ""

        for i in range(1, 15):
            if markerfound == 1:
                break
            else:
                # Query for any WIFI_MAC telemetry marker
                query = "cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_MAC_\" | grep -vi \"TOTAL_COUNT\" | tail -1"
                print("query:%s" % query)

                tdkTestObj = sysObj.createTestStep('ExecuteCmd')
                tdkTestObj.addParameter("command", query)
                expectedresult = "SUCCESS"
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "")
                print("Marker Detail Found from Log file is: %s " % details)

                if len(details) == 0 or "WIFI_MAC_" not in details:
                    markerfound = 0
                    sleep(60)
                else:
                    marker_match = re.search(r"(WIFI_MAC_[0-9]+):\s*([A-Fa-f0-9:]{17})", details, re.IGNORECASE)

                    if marker_match:
                        mac_marker_name = marker_match.group(1)
                        telemetryMacaddress = marker_match.group(2).strip()
                        markerfound = 1
                    else:
                        markerfound = 0
                        sleep(60)

        if expectedresult in actualresult and markerfound == 1 and telemetryMacaddress != "":
            tdkTestObj.setResultStatus("SUCCESS")
            print("TEST STEP 2: WIFI_MAC telemetry marker should be present")
            print("EXPECTED RESULT 2: WIFI_MAC telemetry marker should be present and value should be retrieved")
            print("ACTUAL RESULT 2: %s Marker is %s" % (mac_marker_name, telemetryMacaddress))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            if re.match(r"^([A-Fa-f0-9]{2}:){5}[A-Fa-f0-9]{2}$", telemetryMacaddress):
                tdkTestObj.setResultStatus("SUCCESS")
                print("TEST STEP 3: Validate WIFI_MAC telemetry marker value")
                print("EXPECTED RESULT 3: WIFI_MAC telemetry marker value should be in valid MAC address format")
                print("ACTUAL RESULT 3: WIFI_MAC telemetry marker value is valid: %s" % telemetryMacaddress)
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("TEST STEP 3: Validate WIFI_MAC telemetry marker value")
                print("EXPECTED RESULT 3: WIFI_MAC telemetry marker value should be in valid MAC address format")
                print("ACTUAL RESULT 3: WIFI_MAC telemetry marker value is invalid: %s" % telemetryMacaddress)
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("TEST STEP 2: WIFI_MAC telemetry marker should be present")
            print("EXPECTED RESULT 2: WIFI_MAC telemetry marker should be present")
            print("ACTUAL RESULT 2: WIFI_MAC telemetry marker is not present")
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

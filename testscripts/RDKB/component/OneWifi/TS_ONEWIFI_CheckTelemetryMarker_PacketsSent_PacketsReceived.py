##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2025 RDK Management
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

import tdklib
from time import sleep
import re

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam", "RDKB")
sysObj = tdklib.TDKScriptingLibrary("sysutil", "RDKB")

# IP and Port of box, replaced with DUT details during execution
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port, 'TS_ONEWIFI_CheckTelemetryMarker_PacketsSent_PacketsReceived')
sysObj.configureTestCase(ip,port, 'TS_ONEWIFI_CheckTelemetryMarker_PacketsSent_PacketsReceived')

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
sysutilloadmodulestatus = sysObj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysutilloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    sysObj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    revertflag = 0
    flag = 0
    step = 1

    # Get Telemetry Enable state
    tdkTestObj = obj.createTestStep('pam_GetParameterValues')
    tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    logEnable = tdkTestObj.getResultDetails()

    print(f"TEST STEP {step}: Get the Telemetry Enable state")
    print(f"EXPECTED RESULT {step}: Should get the TELEMETRY Enable state")

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: TELEMETRY Enable state: {logEnable}")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        if logEnable == "false":
            step += 1
            tdkTestObj = obj.createTestStep('pam_SetParameterValues')
            tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable")
            tdkTestObj.addParameter("ParamValue", "true")
            tdkTestObj.addParameter("Type", "bool")
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            print(f"TEST STEP {step}: Set the Telemetry Enable state to true")
            print(f"EXPECTED RESULT {step}: Should set the TELEMETRY Enable state to true")

            if expectedresult in actualresult:
                revertflag = 1
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: TELEMETRY Enable state: {details}")
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                flag = 1
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: TELEMETRY Enable state: {details}")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            print("Telemetry Enable state is already enabled, not required to change it")

        if flag != 1:
            step += 1

            # Get TELEMETRY LogInterval
            tdkTestObj = obj.createTestStep('pam_GetParameterValues')
            tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval")
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            telemetry_loginterval = tdkTestObj.getResultDetails()

            print(f"TEST STEP {step}: Get the TELEMETRY LogInterval")
            print(f"EXPECTED RESULT {step}: Should get the TELEMETRY LogInterval")

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: TELEMETRY LogInterval: {telemetry_loginterval}")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1

                # Set TELEMETRY LogInterval to 5 min
                tdkTestObj = obj.createTestStep('pam_SetParameterValues')
                tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval")
                tdkTestObj.addParameter("ParamValue", "300")
                tdkTestObj.addParameter("Type", "int")
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails()

                print(f"TEST STEP {step}: Set the TELEMETRY LogInterval to 5 min")
                print(f"EXPECTED RESULT {step}: Should set the TELEMETRY LogInterval to 5 min")

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: SET operation for TELEMETRY LogInterval SUCCESS: {details}")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    # Get TELEMETRY LogInterval and validate
                    step += 1
                    tdkTestObj = obj.createTestStep('pam_GetParameterValues')
                    tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval")
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    tel_loginterval = tdkTestObj.getResultDetails()

                    print(f"TEST STEP {step}: Get the TELEMETRY LogInterval")
                    print(f"EXPECTED RESULT {step}: Should get the TELEMETRY LogInterval")

                    if expectedresult in actualresult and tel_loginterval == "300":
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: TELEMETRY LogInterval: {tel_loginterval}")
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        # Check wifihealth log file presence
                        step += 1
                        print(f"TEST STEP {step}: Check for wifihealth log file presence")
                        print(f"EXPECTED RESULT {step}: wifihealth log file should be present")

                        whl_found = 0
                        for i in range(1, 6):
                            if whl_found == 1:
                                break
                            else:
                                print(f"Checking wifihealth log file presence iteration {i}")
                                cmd = "[ -f /rdklogs/logs/wifihealth.txt ] && echo \"File exist\" || echo \"File does not exist\""
                                tdkTestObj = sysObj.createTestStep('ExecuteCmd')
                                tdkTestObj.addParameter("command", cmd)
                                tdkTestObj.executeTestCase(expectedresult)
                                actualresult = tdkTestObj.getResult()
                                details = tdkTestObj.getResultDetails()

                                if "File exist" in details:
                                    whl_found = 1
                                else:
                                    sleep(60)

                        if expectedresult in actualresult and whl_found == 1:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: wifihealth log file is present")
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                            # Check for any WIFI_PACKETSSENTCLIENTS telemetry marker in wifihealth log file
                            step += 1
                            print(f"TEST STEP {step}: Check if WIFI_PACKETSSENTCLIENTS telemetry marker is present in wifihealth log file")
                            print(f"EXPECTED RESULT {step}: WIFI_PACKETSSENTCLIENTS telemetry marker should be present and value should be retrieved successfully")

                            markerfound = 0
                            tel_packetssent = ""
                            packetssent_marker_name = ""

                            for i in range(1, 6):
                                if markerfound == 1:
                                    break
                                else:
                                    print(f"Checking WIFI_PACKETSSENTCLIENTS marker in wifihealth log file iteration {i}")
                                    query = "cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_PACKETSSENTCLIENTS_\" | grep -vi \"TOTAL_COUNT\" | tail -1"
                                    tdkTestObj = sysObj.createTestStep('ExecuteCmd')
                                    tdkTestObj.addParameter("command", query)
                                    tdkTestObj.executeTestCase(expectedresult)
                                    actualresult = tdkTestObj.getResult()
                                    details = tdkTestObj.getResultDetails().replace("\\n", "").strip()

                                    if len(details) == 0 or "WIFI_PACKETSSENTCLIENTS_" not in details:
                                        markerfound = 0
                                        sleep(60)
                                    else:
                                        marker_match = re.search(r"(WIFI_PACKETSSENTCLIENTS_[0-9]+):\s*([0-9]+)", details, re.IGNORECASE)

                                        if marker_match:
                                            packetssent_marker_name = marker_match.group(1)
                                            tel_packetssent = marker_match.group(2).strip()
                                            markerfound = 1
                                        else:
                                            markerfound = 0
                                            sleep(60)

                            if expectedresult in actualresult and markerfound == 1 and tel_packetssent != "":
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"ACTUAL RESULT {step}: {packetssent_marker_name} Marker is {tel_packetssent}")
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                step += 1
                                print(f"TEST STEP {step}: Check if packetssent telemetry marker value is greater zero")
                                print(f"EXPECTED RESULT {step}: packetssent telemetry marker value should be greater than zero")

                                if int(tel_packetssent) > 0:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print(f"ACTUAL RESULT {step}: packetssent telemetry marker value: {tel_packetssent}")
                                    print("[TEST EXECUTION RESULT] : SUCCESS")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print(f"ACTUAL RESULT {step}: packetssent telemetry marker value: {tel_packetssent}")
                                    print("[TEST EXECUTION RESULT] : FAILURE")

                                # Check for any WIFI_PACKETSRECEIVEDCLIENTS telemetry marker in wifihealth log file
                                step += 1
                                print(f"TEST STEP {step}: Check if WIFI_PACKETSRECEIVEDCLIENTS telemetry marker is present in wifihealth log file")
                                print(f"EXPECTED RESULT {step}: WIFI_PACKETSRECEIVEDCLIENTS telemetry marker should be present and value should be retrieved successfully")

                                markerfound = 0
                                tel_packetreceived = ""
                                packetsreceived_marker_name = ""

                                for i in range(1, 6):
                                    if markerfound == 1:
                                        break
                                    else:
                                        print(f"Checking WIFI_PACKETSRECEIVEDCLIENTS marker in wifihealth log file iteration {i}")
                                        query = "cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_PACKETSRECEIVEDCLIENTS_\" | grep -vi \"TOTAL_COUNT\" | tail -1"
                                        tdkTestObj = sysObj.createTestStep('ExecuteCmd')
                                        tdkTestObj.addParameter("command", query)
                                        tdkTestObj.executeTestCase(expectedresult)
                                        actualresult = tdkTestObj.getResult()
                                        details = tdkTestObj.getResultDetails().replace("\\n", "").strip()

                                        if len(details) == 0 or "WIFI_PACKETSRECEIVEDCLIENTS_" not in details:
                                            markerfound = 0
                                            sleep(60)
                                        else:
                                            marker_match = re.search(r"(WIFI_PACKETSRECEIVEDCLIENTS_[0-9]+):\s*([0-9]+)", details, re.IGNORECASE)

                                            if marker_match:
                                                packetsreceived_marker_name = marker_match.group(1)
                                                tel_packetreceived = marker_match.group(2).strip()
                                                markerfound = 1
                                            else:
                                                markerfound = 0
                                                sleep(60)

                                if expectedresult in actualresult and markerfound == 1 and tel_packetreceived != "":
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print(f"ACTUAL RESULT {step}: {packetsreceived_marker_name} Marker is {tel_packetreceived}")
                                    print("[TEST EXECUTION RESULT] : SUCCESS")

                                    step += 1
                                    print(f"TEST STEP {step}: Check if packetsreceived telemetry marker value is greater than zero")
                                    print(f"EXPECTED RESULT {step}: packetsreceived telemetry marker value should be greater than zero")

                                    if int(tel_packetreceived) > 0:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print(f"ACTUAL RESULT {step}: packetsreceived telemetry marker value: {tel_packetreceived}")
                                        print("[TEST EXECUTION RESULT] : SUCCESS")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print(f"ACTUAL RESULT {step}: packetsreceived telemetry marker value: {tel_packetreceived}")
                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print(f"ACTUAL RESULT {step}: WIFI_PACKETSRECEIVEDCLIENTS telemetry marker not found in wifihealth log file")
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: WIFI_PACKETSSENTCLIENTS telemetry marker not found in wifihealth log file")
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: wifihealth log file is not present")
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: SET operation not reflected in GET operation. TELEMETRY LogInterval: {tel_loginterval}")
                        print("[TEST EXECUTION RESULT] : FAILURE")

                    # Revert LogInterval
                    step += 1
                    tdkTestObj = obj.createTestStep('pam_SetParameterValues')
                    tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval")
                    tdkTestObj.addParameter("ParamValue", telemetry_loginterval)
                    tdkTestObj.addParameter("Type", "int")
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    details = tdkTestObj.getResultDetails()

                    print(f"TEST STEP {step}: Revert the TELEMETRY LogInterval to previous")
                    print(f"EXPECTED RESULT {step}: Should revert the TELEMETRY LogInterval to previous")

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Revert successful")
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Revert failed")
                        print("[TEST EXECUTION RESULT] : FAILURE")

                    # Revert Telemetry Enable if modified earlier
                    if revertflag == 1:
                        step += 1
                        tdkTestObj = obj.createTestStep('pam_SetParameterValues')
                        tdkTestObj.addParameter("ParamName", "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable")
                        tdkTestObj.addParameter("ParamValue", logEnable)
                        tdkTestObj.addParameter("Type", "bool")
                        tdkTestObj.executeTestCase(expectedresult)
                        actualresult = tdkTestObj.getResult()
                        details = tdkTestObj.getResultDetails()

                        print(f"TEST STEP {step}: Revert the Telemetry Enable status to previous")
                        print(f"EXPECTED RESULT {step}: Should revert the Telemetry Enable status to previous")

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: Revert successful")
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: Revert failed")
                            print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: SET operation failed: {details}")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: TELEMETRY LogInterval: {telemetry_loginterval}")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            print("Telemetry logger was disabled and failed on enabling")
            tdkTestObj.setResultStatus("FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: TELEMETRY Enable state: {logEnable}")
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("pam")
    sysObj.unloadModule("sysutil")
else:
    print("Failed to load pam/sysutil module")
    obj.setLoadModuleStatus("FAILURE")
    sysObj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

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
'''
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_ONEWIFI_CheckTelemetryMarker_6GHZ_ErrorSent</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if the error sent via TR-181 and telemetry marker are greater than or equal to  zero by changing the log interval to 5 min
</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks></remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>BPI</box_type>
    <!--  -->
    <box_type>Broadband</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_ONEWIFI_301</test_case_id>
    <test_objective>This test case is to check if the error sent via TR-181 and telemetry marker are greater than or equal to  zero by changing the log interval to 5 min
</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, BPI</test_setup>
    <pre_requisite>1. Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
    2. TDK Agent should be in a running state or invoke it through StartTdk.sh script
    3. At least one Wi-Fi client must be connected to the 6 GHz SSID</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable
Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval
Device.WiFi.AccessPoint.17.AssociatedDevice.1.Stats.ErrorsSent</input_parameters>
    <automation_approch>1.Load the module.
2.Check if telemetry markers are enabled ,if not enable using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable
3.Change the log interval to 300 sec i,e 5min using Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval
4.Check for telemetry marker WIFI_ERRORSSENT_17 in wifihealth.txt file and get the error sent using Device.WiFi.AccessPoint.17.AssociatedDevice.1.Stats.ErrorsSent .
5.Check if the values received are via telemetry marker and Tr-181 are equal and greater than or equal to zero and the
6. Revert the log interval value and telemetry enable status to original
7.Unload the Module
</automation_approch>
    <expected_output>Error sent via Tr-181 and telemetry markers must be greater than or equal to zero</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiAgent</test_stub_interface>
    <test_script>TS_ONEWIFI_CheckTelemetryMarker_6GHZ_ErrorSent</test_script>
    <skipped></skipped>
    <release_version>M141</release_version>
    <remarks>Connect only 1 wifi 6g client</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
import tdklib
from time import sleep

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam", "RDKB")
sysObj = tdklib.TDKScriptingLibrary("sysutil", "RDKB")

# IP and Port of box, replaced with DUT details during execution
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_CheckTelemetryMarker_6GHZ_ErrorSent')
sysObj.configureTestCase(ip,port,'TS_ONEWIFI_CheckTelemetryMarker_6GHZ_ErrorSent')

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
                        for i in range(1,6):
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

                            #Check for WIFI_ERRORSSENT_17 Marker in wifihealth log file
                            step += 1
                            print(f"TEST STEP {step}: Check if WIFI_ERRORSSENT_17 Marker is present in wifihealth log file")
                            print(f"EXPECTED RESULT {step}: WIFI_ERRORSSENT_17 Marker should be present wifihealth log file")
                            markerfound = 0
                            for i in range(1, 6):
                                if markerfound == 1:
                                    break
                                else:
                                    print(f"Checking WIFI_ERRORSSENT_17 in wifihealth log file iteration {i}")
                                    query = "cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_ERRORSSENT_17:\""
                                    tdkTestObj = sysObj.createTestStep('ExecuteCmd')
                                    tdkTestObj.addParameter("command", query)
                                    tdkTestObj.executeTestCase(expectedresult)
                                    actualresult = tdkTestObj.getResult()
                                    details = tdkTestObj.getResultDetails()
                                    if (len(details) == 0) or details.endswith(":") or "WIFI_ERRORSSENT_17" not in details:
                                        markerfound = 0
                                        sleep(60)
                                    else:
                                        tel_errorsent = details.split("WIFI_ERRORSSENT_17:")[1].split(',')[0].replace("\\n", "").strip()
                                        markerfound = 1

                            if expectedresult in actualresult and markerfound == 1 and tel_errorsent != "":
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"ACTUAL RESULT {step}: WIFI_ERRORSSENT_17 Marker is {tel_errorsent}")
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                # ErrorSent via TR-181
                                step += 1
                                tdkTestObj = obj.createTestStep('pam_GetParameterValues')
                                tdkTestObj.addParameter("ParamName", "Device.WiFi.AccessPoint.17.AssociatedDevice.1.Stats.ErrorsSent")
                                tdkTestObj.executeTestCase(expectedresult)
                                actualresult = tdkTestObj.getResult()
                                tr181_errorsent = tdkTestObj.getResultDetails()

                                print(f"TEST STEP {step}: Get the ErrorSent via TR-181 parameter")
                                print(f"EXPECTED RESULT {step}: Should get the ErrorSent via TR-181 parameter")

                                if expectedresult in actualresult:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print(f"ACTUAL RESULT {step}: ErrorSent via TR-181 parameter: {tr181_errorsent}")
                                    print("[TEST EXECUTION RESULT] : SUCCESS")

                                    # Verify ErrorSent >= 0
                                    step += 1
                                    print(f"TEST STEP {step}: Check if ErrorSent via TR-181 parameter and telemetry marker are greater than or equal to zero")
                                    print(f"EXPECTED RESULT {step}: ErrorSent via TR-181 parameter and telemetry marker should be greater than or equal to zero")
                                    if int(tel_errorsent) >= 0 and int(tr181_errorsent) >= 0:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print(f"ACTUAL RESULT {step}: ErrorSent via TR-181: {tr181_errorsent}, ErrorSent via Telemetry marker: {tel_errorsent}")
                                        print("[TEST EXECUTION RESULT] : SUCCESS")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print(f"ACTUAL RESULT {step}: ErrorSent sent via TR-181: {tr181_errorsent}, Telemetry marker: {tel_errorsent}")
                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print(f"ACTUAL RESULT {step}: ErrorSent via TR-181 parameter: {tr181_errorsent}")
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: WIFI_ERRORSSENT_17 Marker not found in wifihealth log file")
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: wifihealth log file is not present")
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}:SET operation not reflected in GET operation. TELEMETRY LogInterval: {tel_loginterval}")
                        print("[TEST EXECUTION RESULT] : FAILURE")

                    #  Revert LogInterval
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


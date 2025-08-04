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
  <name>TS_ONEWIFI_ForceDisable_Set6GWiFiParams</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if able to set Radio and AccessPoint params for 6ghz after enabling the ForceDisable</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <test_case_id>TC_ONEWIFI_295</test_case_id>
    <test_objective>This test case is to check if radioenable,KeyPassphrase,AccessPoint parameters for 6GHz are not writable when WiFi Force Disable is enabled.
</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,BPI</test_setup>
    <pre_requisite>1. Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
    2. TDK Agent should be in a running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used></api_or_interface_used>
    <input_parameters>Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable
    Device.WiFi.Radio.3.Enable
    Device.WiFi.AccessPoint.17.Enable
    Device.WiFi.AccessPoint.17.Security.X_COMCAST-COM_KeyPassphrase</input_parameters>
    <automation_approch>1.Load the wifiagent module
2.Get the current value of Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable and save it.
3.Set Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable to true
4.Now attempt to set write operations on: Device.WiFi.Radio.3.Enable, Device.WiFi.AccessPoint.17.Enable, Device.WiFi.AccessPoint.17.Security.KeyPassphrase
5.Each SET operation should fail
6.Check WiFiLog.txt.0 for log entry: WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED.
7.Revert ForceDisable to initial value.
8.Unload the wifiagent module</automation_approch>
    <expected_output>SET operation should fail for radioenable and AccessPoint parameters and the error message should be logged each time a set operation is performed when Force disable is enabled</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiAgent</test_stub_interface>
    <test_script>TS_ONEWIFI_ForceDisable_Set6GWiFiParams</test_script>
    <skipped></skipped>
    <release_version>M141</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
def getTelLogFileTotalLinesCount(tdkTestObj):
    expectedresult="SUCCESS"
    linecount = 0
    cmd = "cat /rdklogs/logs/WiFilog.txt.0| wc -l"
    tdkTestObj.addParameter("command",cmd)
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "")
    print(f"current WiFilog.txt.0 line count: {details}")
    if expectedresult in actualresult:
        if details.isdigit():
            linecount = int(details)
    return actualresult,linecount

def SetOperation(tdkTestObj,parameter):
    expectedresult="FAILURE"
    if parameter == "Device.WiFi.AccessPoint.17.Security.X_COMCAST-COM_KeyPassphrase":
        tdkTestObj.addParameter("paramName",parameter)
        tdkTestObj.addParameter("paramValue", "tdkbtestcase")
        tdkTestObj.addParameter("paramType","string")
        tdkTestObj.executeTestCase("expectedresult")
        actualresult = tdkTestObj.getResult()
    else:
        tdkTestObj.addParameter("paramName",parameter)
        tdkTestObj.addParameter("paramValue", "true")
        tdkTestObj.addParameter("paramType","boolean")
        tdkTestObj.executeTestCase("expectedresult")
        actualresult = tdkTestObj.getResult()
    return actualresult,expectedresult


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
from time import sleep
from tdkutility import *
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1")
obj1= tdklib.TDKScriptingLibrary("sysutil","1")
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_ForceDisable_Set6GWiFiParams')
obj1.configureTestCase(ip,port,'TS_ONEWIFI_ForceDisable_Set6GWiFiParams')

#result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult()
loadmodulestatus1=obj1.getLoadModuleResult()
FD_flag = 0
FD_revert = 0

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS"
    step = 1

    #Get initial value of FOrce disable
    paramName = "Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable"
    tdkTestObj,actualresult,intial_FD = wifi_GetParam(obj,paramName)

    print(f"\nTEST STEP {step}: Get the current WiFi Force Disable state")
    print(f"EXPECTED RESULT {step}: Should get current WiFi Force Disable state")

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Current WiFi Force Disable state is {intial_FD}")
        print(f"[TEST EXECUTION RESULT] : SUCCESS")
        step += 1

        if intial_FD == "false":
            #Set Force Disable to true
            paramName = "Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable"
            tdkTestObj,actualresult = wifi_SetParam(obj,paramName,"true","boolean")

            print(f"\nTEST STEP {step}: Enable the WiFi Force Disable")
            print(f"EXPECTED RESULT {step}: Should enable Force Disable state")

            if expectedresult in actualresult:
                FD_revert = 1
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: ForceDisable set to true.")
                print(f"[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                FD_flag = 1
                print(f"ACTUAL RESULT {step}: SET operstion failed")
                print(f"[TEST EXECUTION RESULT] : FAILURE")
        else:
            print("Setting Force Disable to true not required")

        if FD_flag == 0:
            step += 1
            #Now try to set Radio and AccessPoint params and check wifilogs
            params = ["Device.WiFi.Radio.3.Enable" ,"Device.WiFi.AccessPoint.17.Enable","Device.WiFi.AccessPoint.17.Security.X_COMCAST-COM_KeyPassphrase"]
            for parameter in params:
                tdkTestObj = obj1.createTestStep('ExecuteCmd')
                lineCountResult, initialLinesCount = getTelLogFileTotalLinesCount(tdkTestObj)

                if expectedresult in lineCountResult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    tdkTestObj = obj.createTestStep('WIFIAgent_Set')
                    print(f"***performing write operation on  {parameter} ****")
                    actualresult,expectedResult= SetOperation(tdkTestObj,parameter)

                    if expectedResult in actualresult:
                        sleep(5)
                        tdkTestObj = obj1.createTestStep('ExecuteCmd')
                        lineCountResult1, lineCountAfterSimu = getTelLogFileTotalLinesCount(tdkTestObj)
                        if expectedresult in lineCountResult1:
                            tdkTestObj.setResultStatus("SUCCESS")
                            tdkTestObj = obj1.createTestStep('ExecuteCmd')
                            cmd = f"sed -n -e {initialLinesCount},{lineCountAfterSimu}p /rdklogs/logs/WiFilog.txt.0 | grep -i \"WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED\""
                            print(f"cmd: {cmd}")
                            print(f"WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED log message should be present in WiFilog.txt.0")
                            tdkTestObj.addParameter("command", cmd)
                            tdkTestObj.executeTestCase(expectedresult)
                            actualresult = tdkTestObj.getResult()
                            details = tdkTestObj.getResultDetails()

                            if expectedresult in actualresult and "WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED" in details:
                                tdkTestObj.setResultStatus("SUCCESS")
                                details = tdkTestObj.getResultDetails().strip().replace("\\n", "")
                                print(f"{details}")
                                print(f"[TEST EXECUTION RESULT] :SUCCESS")

                                if "WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED" in details:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print(f"{details}")
                                    print(f"[TEST EXECUTION RESULT] :SUCCESS")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print(f"WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED  didnot populate when trying to set {parameter} in WiFilog.txt.0")
                                    print(f"[TEST EXECUTION RESULT] :FAILURE")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"Execution failure. Details: {details}")
                                print(f"[TEST EXECUTION RESULT] :FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"*******Failed get the line count of the log file*****")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"{parameter} set was success even with Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable  being enabled")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"*******Failed get the line count of the log file*****")

            if FD_revert == 1:
                # Revert ForceDisable to previous value
                paramName = "Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable"
                tdkTestObj,actualresult = wifi_SetParam(obj,paramName,intial_FD,"boolean")
                details = tdkTestObj.getResultDetails()
                print(f"\nTEST STEP {step}: Revert the WiFi Force Disable to previous")
                print(f"EXPECTED RESULT {step}: Should revert  Force Disable state to {intial_FD}")
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Revert operation success. Details: {details}")
                    print(f"[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Failed to revert ForceDisable to initial value. Details: {details}")
                    print(f"[TEST EXECUTION RESULT] : FAILURE")
            else:
                print("Reverting Force Disable not Required")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to get current WiFi Force Disable state.")
        print(f"[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("wifiagent")
    obj1.unloadModule("sysutil")
else:
    print(f"Failed to load wifiagent/sysutil module")
    obj.setLoadModuleStatus("FAILURE")
    obj1.setLoadModuleStatus("FAILURE")


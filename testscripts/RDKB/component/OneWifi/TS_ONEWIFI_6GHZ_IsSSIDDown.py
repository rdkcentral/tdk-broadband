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
  <name>TS_ONEWIFI_6GHZ_IsSSIDDown</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check when 6GHZ ssid state is disabled, its status is "down"</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
    <test_case_id>TC_ONEWIFI_282</test_case_id>
    <test_objective>Check when 6GHZ ssid state is disabled, its status is "down"</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,BPI</test_setup>
    <pre_requisite>1. Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
    2. TDK Agent should be in a running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.SSID.17.Enable
    Device.WiFi.SSID.17.Status</input_parameters>
    <automation_approch>1. Load the module
2. Get and save Device.WiFi.SSID.17.Enable value
3. Disable Device.WiFi.SSID.17.Enable
4. Get Device.WiFi.SSID.17.Status and check if its down
5. Set Device.WiFi.SSID.17.Enable to its previous value
6. unload the module.
</automation_approch>
    <expected_output>When ssid state is disabled, its status should be "down"
</expected_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_ONEWIFI_6GHZ_IsSSIDDown</test_script>
    <skipped></skipped>
    <release_version>M139</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
from time import sleep

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1")

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_6GHZ_IsSSIDDown')

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus)

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS"
    step = 1

    #Get the SSID Enable for 6ghz(SSID 17)
    tdkTestObj = obj.createTestStep('WIFIAgent_Get')
    tdkTestObj.addParameter("paramName","Device.WiFi.SSID.17.Enable")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    print(f"TEST STEP {step}: Get the Enable state of SSID17")
    print(f"EXPECTED RESULT {step}: Should get the Enable state of SSID17")

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        orgState = details.split("VALUE:")[1].split(' ')[0]
        print(f"ACTUAL RESULT {step}: State is {orgState}")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        if orgState == "true":
            tdkTestObj = obj.createTestStep('WIFIAgent_Set')
            tdkTestObj.addParameter("paramName","Device.WiFi.SSID.17.Enable")
            tdkTestObj.addParameter("paramValue","false")
            tdkTestObj.addParameter("paramType","boolean")
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            step = step + 1
            print(f"TEST STEP {step}: Disable Enable state of SSID17")
            print(f"EXPECTED RESULT {step}: Should disable Enable state of SSID17")

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: State is {details} " )
                print("[TEST EXECUTION RESULT] : SUCCESS")

                sleep(5)
                #check if ssid17 status is Down or not
                step = step + 1
                tdkTestObj = obj.createTestStep('WIFIAgent_Get')
                tdkTestObj.addParameter("paramName","Device.WiFi.SSID.17.Status")
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails()

                print(f"TEST STEP {step}: Get Device.WiFi.SSID.17.Status")
                print(f"EXPECTED RESULT {step}: Should Get Device.WiFi.SSID.17.Status")

                if expectedresult in actualresult and details != "":
                    tdkTestObj.setResultStatus("SUCCESS")
                    status = details.split("VALUE:")[1].split(' ')[0]
                    print(f"ACTUAL RESULT {step}: SSID Status is {status}")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step += 1
                    print(f"TEST STEP {step}: Check if SSID17 staus is Down or not")
                    print(f"EXPECTED RESULT {step}: SSID17 staus should be down")

                    if status == "Down":
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: SSID status is Down")
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        #change ssid17 state to previous one
                        step = step + 1
                        tdkTestObj = obj.createTestStep('WIFIAgent_Set')
                        tdkTestObj.addParameter("paramName","Device.WiFi.SSID.17.Enable")
                        tdkTestObj.addParameter("paramValue",orgState)
                        tdkTestObj.addParameter("paramType","boolean")
                        tdkTestObj.executeTestCase(expectedresult)
                        actualresult = tdkTestObj.getResult()
                        details = tdkTestObj.getResultDetails()

                        print(f"TEST STEP {step}: Restore Enable state of SSID17")
                        print(f"EXPECTED RESULT {step}: Should Restore Enable state of SSID17")

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: Enable State is restored to previous value. Details:{details} ")
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: Unable to restore Enable state to previous value. Details:{details} ")
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: SSID status is not Down")
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Get operartion failed. Details: {details}")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Set operation failed. Details: {details} ")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            #SSID17 is disabled check status
            step = step + 1
            tdkTestObj = obj.createTestStep('WIFIAgent_Get')
            tdkTestObj.addParameter("paramName","Device.WiFi.SSID.17.Status")
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            print(f"TEST STEP {step}: Get Device.WiFi.SSID.17.Status")
            print(f"EXPECTED RESULT {step}: Should Get Device.WiFi.SSID.17.Status")

            if expectedresult in actualresult and details != "":
                tdkTestObj.setResultStatus("SUCCESS")
                status = details.split("VALUE:")[1].split(' ')[0]
                print(f"ACTUAL RESULT {step}: Status is {status}")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                print(f"TEST STEP {step}: Check if SSID17 staus is Down or not")
                print(f"EXPECTED RESULT {step}: SSID17 staus should be down")

                if "Down" in status:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: SSID status is Down")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: SSID status is not Down")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Get operation failed. Details: {details}")
                print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to get Enable state of SSID 17. Details:{details}")
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("wifiagent")

else:
    print("Failed to load wifi module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

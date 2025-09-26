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
  <version>1</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_ONEWIFI_6GHzCheckHostActiveStatus_WithConnectedClient</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>onewifi_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if the Host Active status Device.Hosts.Host.{i}.Active is "true" for 6G connected client</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <test_case_id>TC_ONEWIFI_297</test_case_id>
    <test_objective>This test case is to check if the Host Active status Device.Hosts.Host.{i}.Active is "true" for 6G connected client
</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Boradband,BPI</test_setup>
    <pre_requisite>1. Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
    2. TDK Agent should be in a running state or invoke it through StartTdk.sh script
    3. One wifi connected client is needed</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.Hosts.HostNumberOfEntries
    Device.Hosts.Host.{index}.Layer1Interface
    Device.Hosts.Host.{index}.Active</input_parameters>
    <automation_approch>1. Load the module
2. Get the number of Host entries using Device.Hosts.HostNumberOfEntries
3. Iterate through the Host Table and query the Device.Hosts.Host.{i}.Layer1Interface for each of the host entries.
4. Find the Host Table entry for wifi client by checking if Device.Hosts.Host.{i}.Layer1Interface is equal to Device.WiFi.SSID.17.
5. For the Host Entry of wifi client, query Device.Hosts.Host.{i}.Active and check if it is Active. Else, return failure.
6. If none of the host entry's layer 1 interface gives "Device.WiFi.SSID.17", return failure.
7. Unload the module.</automation_approch>
    <expected_output>The Host Active status Device.Hosts.Host.{i}.Active should be "true" for 6G connected client
</expected_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_ONEWIFI_6GHzCheckHostActiveStatus_WithConnectedClient</test_script>
    <skipped></skipped>
    <release_version>M141</release_version>
    <remarks></remarks>
  </test_cases>
</xml>
'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
from tdkbVariables import *
from tdkutility import *

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB")

# IP and Port of box, No need to change,
# This will be replaced with corresponding Box IP and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_6GHzCheckHostActiveStatus_WithConnectedClient')

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
print(f"[LIB LOAD STATUS]  :  {loadmodulestatus}")

if "SUCCESS" in loadmodulestatus.upper():
    # Set the load module status
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"

    # Get the number of host table entries
    step = 1
    tdkTestObj = obj.createTestStep('WIFIAgent_Get')
    tdkTestObj.addParameter("paramName", "Device.Hosts.HostNumberOfEntries")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    value = tdkTestObj.getResultDetails()

    print(f"\nTEST STEP {step} : Get the number of Host entries using Device.Hosts.HostNumberOfEntries")
    print(f"EXPECTED RESULT {step} : Should successfully retrieve Device.Hosts.HostNumberOfEntries")

    if expectedresult in actualresult and value != "":
        hostEntries = value.split("VALUE:")[1].split(' ')[0]
        hostEntries = int(hostEntries)
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step} : Device.Hosts.HostNumberOfEntries : {hostEntries}")
        print(f"[TEST EXECUTION RESULT] : SUCCESS")

        # Iterate through the host table and find the index for which Layer1Interface is Device.WiFi.SSID.17
        clientDetected = 0
        for index in range(1, hostEntries + 1):
            print(f"\n**********For Host Table Entry {index}**********")
            # Get the value of Device.Hosts.Host.{i}.Layer1Interface
            step += 1
            paramName = f"Device.Hosts.Host.{index}.Layer1Interface"
            tdkTestObj.addParameter("paramName", paramName)
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            value = tdkTestObj.getResultDetails()

            print(f"\nTEST STEP {step} : Get the value of {paramName} and check if it is Device.WiFi.SSID.17")
            print(f"EXPECTED RESULT {step} : Should successfully retrieve {paramName}")

            if expectedresult in actualresult and value != "":
                layer1Interface = value.split("VALUE:")[1].split(' ')[0]
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step} : {paramName} : {layer1Interface}")
                print(f"[TEST EXECUTION RESULT] : SUCCESS")

                if layer1Interface == "Device.WiFi.SSID.17":
                    clientDetected = 1
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"Identified the Host Table Entry for connected client as : {index}")

                    # Check if the connected client is shown as active
                    step += 1
                    paramName = f"Device.Hosts.Host.{index}.Active"
                    tdkTestObj.addParameter("paramName", paramName)
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    value = tdkTestObj.getResultDetails()

                    print(f"\nTEST STEP {step} : Get the value of {paramName} and check if it is true")
                    print(f"EXPECTED RESULT {step} : Should successfully retrieve {paramName} and it should be true")

                    if expectedresult in actualresult and value != "":
                        activeStatus = value.split("VALUE:")[1].split(' ')[0]
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step} : {paramName} : {activeStatus}")
                        print(f"[TEST EXECUTION RESULT] : SUCCESS")

                        if activeStatus == "true":
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("Host is Active")
                            break
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("Host is NOT Active")
                            break
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step} : Get operation failed for {paramName}")
                        print(f"[TEST EXECUTION RESULT] : FAILURE")
                        break
                else:
                    print(f"Host Table Entry for connected client is not at index {index}")
                    continue
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step} : {paramName} : {layer1Interface}")
                print(f"[TEST EXECUTION RESULT] : FAILURE")
                break

        # Check if client connection is proper or not
        if clientDetected != 1:
            tdkTestObj.setResultStatus("FAILURE")
            print("\nNone of the Host Table entries show Device.WiFi.SSID.17 as Layer 1 Interface")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step} : Get Operation Failed")
        print(f"[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("wifiagent")
else:
    print("Failed to load wifi agent module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")


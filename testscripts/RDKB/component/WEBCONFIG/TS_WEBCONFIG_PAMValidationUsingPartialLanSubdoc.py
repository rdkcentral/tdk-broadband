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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>4</version>
  <name>TS_WEBCONFIG_PAMValidationUsingPartialLanSubdoc</name>
  <primitive_test_id/>
  <primitive_test_name>Webconfig_DoNothing</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Validate PAM via Webconfig Feature using partial LAN subdoc</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
    <box_type>BPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WEBCONFIG_10</test_case_id>
    <test_objective>Validate PAM via Webconfig Feature using partial LAN subdoc</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband,RPI,BPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
    </pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get
TDKB_TR181Stub_Set
TDKB_TR181Stub_SetOnly
ExecuteCmd</api_or_interface_used>
    <input_parameters>Device.X_RDK_WebConfig.
Device.X_RDK_WebConfig.ForceSync
Device.DHCPv4.Server.Pool.{i}.Enable
Device.DHCPv4.Server.Pool.{i}.IPRouters
Device.DHCPv4.Server.Pool.{i}.SubnetMask
Device.DHCPv4.Server.Pool.{i}.MinAddress
Device.DHCPv4.Server.Pool.{i}.LeaseTime
Device.DHCPv4.Server.Pool.{i}.MaxAddress.</input_parameters>
    <automation_approch>1. Load the modules
    2. Configure the webconfig settings if already not configured with webconfig server details.
    3  Get the Device.DHCPv4.Server.Pool.1.Enable, Device.DHCPv4.Server.Pool.1.IPRouters, Device.DHCPv4.Server.Pool.1.SubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress,  Device.DHCPv4.Server.Pool.1.LeaseTime and Device.DHCPv4.Server.Pool.1.MaxAddress.
    4. Enter partial LAN subdoc information with new values in RDKM WebConfig Server.
    5. Set trigger parameter Device.X_RDK_WebConfig.ForceSync to root.
    6. Get the  Device.DHCPv4.Server.Pool.1.Enable, Device.DHCPv4.Server.Pool.1.IPRouters, Device.DHCPv4.Server.Pool.1.SubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress,  Device.DHCPv4.Server.Pool.1.LeaseTime and Device.DHCPv4.Server.Pool.1.MaxAddress and validate whether it fails to be updated.
    7. Unload the modules.</automation_approch>
    <expected_output>PAM validation via Webconfig Feature using partial LAN subdoc should fail.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WEBCONFIG</test_stub_interface>
    <test_script>TS_WEBCONFIG_PAMValidationUsingPartialLanSubdoc</test_script>
    <skipped>No</skipped>
    <release_version>M140</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
from tdkutility import *
from WebconfigUtility import *
from WebconfigVariables import *

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WEBCONFIG_PAMValidationUsingPartialLanSubdoc')
sysobj.configureTestCase(ip,port,'TS_WEBCONFIG_PAMValidationUsingPartialLanSubdoc')
# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus_sys.upper():
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    expectedresult = "SUCCESS"

    step = 1
    #Get MAC Address of the device
    print("\nTEST STEP %d: Get the MAC address of the device" %step)
    print("EXPECTED RESULT %d: The MAC address should be retrieved successfully" %step)
    tdkTestObj, actualresult, mac = getMacAddress(sysobj)
    if actualresult in expectedresult and mac != "":
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: The MAC address is retrieved successfully: %s" %(step, mac))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step = step + 1
        #Non-sensitive value for the trigger parameter
        value = "root"


        #Configure the webconfig settings if not already done
        print("\nTEST STEP %d: Get the webconfig settings and configure it if not already done" %step)
        print("EXPECTED RESULT %d: The webconfig settings should be properly configured" %step)
        tdkTestObj, flag, initial_webconfig_settings = configureWebconfigSettings(obj, mac)
        if flag == 0:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Webconfig settings are configured properly" %step)
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            dhcp_params = ["Device.DHCPv4.Server.Pool.1.Enable", "Device.DHCPv4.Server.Pool.1.IPRouters", "Device.DHCPv4.Server.Pool.1.SubnetMask", "Device.DHCPv4.Server.Pool.1.MinAddress", "Device.DHCPv4.Server.Pool.1.MaxAddress", "Device.DHCPv4.Server.Pool.1.LeaseTime"]

            # Get the current values of DHCPv4 parameters
            print("\nTEST STEP %d: Get the current values of DHCPv4 parameters" %step)
            print("EXPECTED RESULT %d: The current values of DHCPv4 parameters should be retrieved successfully" %step)

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
            tdkTestObj, result, initial_dhcp_values = getMultipleParams(obj, dhcp_params)
            if "FAILURE" not in result:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: The current values of DHCPv4 parameters are retrieved successfully" %step)
                print("[TEST EXECUTION RESULT] : SUCCESS")


                step += 1
                subdoc_name = "lan"
                subdoc_type = "pos"
                tr181_dm = "Device.DHCPv4.Server.Lan"

                #Getting the subdoc info
                info = getSubdocInfo(subdoc_name, subdoc_type)
                #Make subdoc_info partial by removing some parameters
                subdoc_info = getPartialSubdocInfo(info)

                #Create and execute curl command to update the LAN subdoc
                print("\nTEST STEP %d: Execute the curl command to update %s subdoc partially" %(step, subdoc_name))
                print("EXPECTED RESULT %d: The curl command execution should fail" %step)

                tdkTestObj, actualresult, details = CurlCommand(sysobj, subdoc_name, tr181_dm, subdoc_info, mac)

                if expectedresult in actualresult and "Request successful" not in details:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Curl command execution failed. Details: %s" %(step, details))
                    print("[TEST EXECUTION RESULT] : SUCCESS")


                    step += 1
                    # Set the webconfig trigger to root
                    trigger_flag = setWebconfigTrigger(obj, value, step)
                    if trigger_flag != 1:
                        print("Successfully set the trigger value to %s" %value)

                        step += 1
                        #Check whether the dhcpv4 parameter values are updated
                        print("\nTEST STEP %d: Check whether the values of DHCPv4 parameters are updated as per LAN subdoc." %step)
                        print("EXPECTED RESULT %d: The values of DHCPv4 parameters should fail to update." %step)

                        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                        tdkTestObj, result, final_dhcp_values = getMultipleParams(obj, dhcp_params)
                        if "FAILURE" not in result and final_dhcp_values == initial_dhcp_values:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: The values of DHCPv4 parameters failed to get updated as per partial LAN subdoc" %step)
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Successfully updated the DHCPv4 parameters." %step)
                            print("[TEST EXECUTION RESULT] : FAILURE\n")

                            #Revert the values if the values are changed
                            step += 1
                            print("\nReverting the values of DHCPv4 parameters to initial values")
                            #Get the revert subdoc info and execute the curl command to revert the LAN subdoc
                            revert_subdoc_info = getSubdocInfo(subdoc_name, subdoc_type, initial_param_values=initial_dhcp_values)
                            tdkTestObj, actualresult, details = CurlCommand(sysobj, subdoc_name, tr181_dm, revert_subdoc_info, mac)
                            if expectedresult in actualresult and "Request successful" in details:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("Curl command execution to revert the LAN subdoc was successful. Details: %s\n" %details)

                                # Set the webconfig trigger to root
                                trigger_flag = setWebconfigTrigger(obj, value, step)
                                if trigger_flag != 1:
                                    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                                    tdkTestObj, result, dhcp_values = getMultipleParams(obj, dhcp_params)
                                    if "FAILURE" not in result and dhcp_values == initial_dhcp_values:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("Successfully reverted the DHCPv4 parameters to their initial values\n")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("Failed to revert the DHCPv4 parameters to their initial values\n")
                                else:
                                    print("Failed to set the trigger value to %s\n" %value)
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d : Curl command execution failed to revert the LAN subdoc. Details: %s\n" %(step, details))
                    else:
                        print("Failed to set the trigger value.\n")

                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Curl command execution succeeded. Details: %s" %(step, details))
                    print("[TEST EXECUTION RESULT] : FAILURE")

            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to retrieve the current values of DHCPv4 parameters" %step)
                print("[TEST EXECUTION RESULT] : FAILURE")

            step += 1
            #Revert the webconfig settings if they were changed
            print("\nTEST STEP %d: Revert the webconfig settings to initial values" %step)
            print("EXPECTED RESULT %d: The webconfig settings should be reverted successfully" %step)

            tdkTestObj, flag, revert_value = configureWebconfigSettings(obj, mac, initial_webconfig_settings)

            if flag == 0:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Webconfig settings reverted successfully" %step)
                print("[TEST EXECUTION RESULT] : SUCCESS\n")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to revert the webconfig settings" %step)
                print("[TEST EXECUTION RESULT] : FAILURE\n")

        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Webconfig settings are not configured properly" %step)
            print("[TEST EXECUTION RESULT] : FAILURE\n")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to retrieve the MAC address of the device" %step)
        print("[TEST EXECUTION RESULT] : FAILURE\n")

    #Unload the modules loaded
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")


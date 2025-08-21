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
  <name>TS_WEBCONFIG_PAMValidationUsingPortForwardingSubdoc</name>
  <primitive_test_id/>
  <primitive_test_name>Webconfig_DoNothing</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Validate PAM via Webconfig Feature using PortForwarding subdoc</synopsis>
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
    <test_case_id>TC_WEBCONFIG_13</test_case_id>
    <test_objective>Validate PAM via Webconfig Feature using PortForwarding subdoc</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,BPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
    </pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get
TDKB_TR181Stub_Set
TDKB_TR181Stub_SetOnly
TDKB_TR181Stub_DelObject
ExecuteCmd</api_or_interface_used>
    <input_parameters>Device.X_RDK_WebConfig.
Device.X_RDK_WebConfig.ForceSync
Device.X_CISCO_COM_DeviceControl.FactoryReset
Device.NAT.PortMappingNumberOfEntries
Device.NAT.PortMapping.{i}.
Device.NAT.PortMapping.{i}.InternalClient
Device.NAT.PortMapping.{i}.ExternalPortEndRange
Device.NAT.PortMapping.{i}.Enable
Device.NAT.PortMapping.{i}.Protocol
Device.NAT.PortMapping.{i}.Description
Device.NAT.PortMapping.{i}.ExternalPort</input_parameters>
    <automation_approch>1. Load the modules
    2. Configure the webconfig settings if already not configured with webconfig server details.
    3  Get the Device.NAT. DM.
    4. Enter PortMapping subdoc information with valid values via WebConfig server using curl command.
    5. Set trigger parameter Device.X_RDK_WebConfig.ForceSync to root.
    6. Get the Device.NAT. and validate whether profile is created as per the subdoc configured.
    7. Unload the modules.</automation_approch>
    <expected_output>PAM validation via Webconfig Feature using PortForwarding subdoc should be successful and profile is created.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WEBCONFIG</test_stub_interface>
    <test_script>TS_WEBCONFIG_PAMValidationUsingPortForwardingSubdoc</test_script>
    <skipped>No</skipped>
    <release_version>M140</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
from time import sleep
from tdkutility import *
from WebconfigUtility import *
from WebconfigVariables import *

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")
# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WEBCONFIG_PAMValidationUsingPortForwardingSubdoc')
sysobj.configureTestCase(ip,port,'TS_WEBCONFIG_PAMValidationUsingPortForwardingSubdoc')
# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus_sys.upper():
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    expectedresult = "SUCCESS"
    step = 1
    #Initiate Factory Reset of the device
    print("\nTEST STEP %d: Initiate Factory Reset of the device" %step)
    print("EXPECTED RESULT %d: Factory Reset should be initiated successfully" %step)

    #Save the current state before going to reboot
    obj.saveCurrentState()

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_SetOnly')
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset")
    tdkTestObj.addParameter("ParamValue", "Router,Wifi,VoIP,Dect,MoCA")
    tdkTestObj.addParameter("Type", "string")
    tdkTestObj.executeTestCase("SUCCESS")
    actualresult = tdkTestObj.getResult()
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d : Factory Reset has been initiated. " %step)
        print("[TEST EXECUTION RESULT] : SUCCESS")

        #Restore the device state saved before reboot
        obj.restorePreviousStateAfterReboot()
        sleep(300)

        step += 1
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
                portforwarding_params = ["Device.NAT.PortMapping.1.InternalClient", "Device.NAT.PortMapping.1.ExternalPortEndRange", "Device.NAT.PortMapping.1.Enable", "Device.NAT.PortMapping.1.Protocol", "Device.NAT.PortMapping.1.Description", "Device.NAT.PortMapping.1.ExternalPort"]
                subdoc_name = "portforwarding"
                subdoc_type = "pos" # positive scenario with valid values
                tr181_dm = "Device.NAT.X_RDK_PortMapping.Data"

                #Getting the subdoc info
                subdoc_info = getSubdocInfo(subdoc_name, subdoc_type)
                set_values = extractValues(subdoc_info)

                #Create and execute curl command to update the portforwarding subdoc
                print("\nTEST STEP %d: Execute the curl command to update %s subdoc" %(step, subdoc_name))
                print("EXPECTED RESULT %d: The curl command should execute successfully" %step)

                tdkTestObj, actualresult, details = CurlCommand(sysobj, subdoc_name, tr181_dm, subdoc_info, mac)

                if expectedresult in actualresult and "Request successful" in details:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Curl command executed successfully. Details: %s" %(step, details))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step += 1
                    # Set the webconfig trigger to root
                    trigger_flag = setWebconfigTrigger(obj, value, step)
                    sleep(10)
                    if trigger_flag != 1:
                        print("Successfully set the trigger value to %s" %value)

                        step += 1
                        #Check the number of port mapping entries and validate whether the profile is created or not
                        print("\nTEST STEP %d: Check if Device.NAT.PortMappingNumberOfEntries has been incremented to 1" %step)
                        print("EXPECTED RESULT %d: Device.NAT.PortMappingNumberOfEntries should be incremented to 1" %step)

                        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                        actualresult, details = getTR181Value(tdkTestObj, "Device.NAT.PortMappingNumberOfEntries")
                        if expectedresult in actualresult and int(details) == 1:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: The profile has been added. Device.NAT.PortMappingNumberOfEntries : %s" %(step, details))
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                            step += 1
                            # Check whether Port Mapping profile is created as per portforwarding subdoc
                            print("\nTEST STEP %d: Check whether Port Mapping profile is updated as per portforwarding subdoc" %step)
                            print("EXPECTED RESULT %d: The Port Mapping profile should be updated with the subdoc values" %step)

                            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                            tdkTestObj, result, final_portforwarding_values = getMultipleParams(obj, portforwarding_params)

                            print("\nValues from Portforwarding subdoc : %s" %set_values)
                            print("\nValues from Device.NAT.PortMapping.1 : %s" %list(final_portforwarding_values.values()))

                            if "FAILURE" not in result and set_values == list(final_portforwarding_values.values()):
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: The Port Mapping profile is created as updated as per portforwarding subdoc successfully" %step)
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: Failed to update Port Mapping profile as per the portforwarding subdoc." %step)
                                print("[TEST EXECUTION RESULT] : FAILURE")
                            step += 1
                            # Delete the port mapping profile created
                            print("\nTEST STEP %d: Delete the Port Mapping profile created" %step)
                            print("EXPECTED RESULT %d: The Port Mapping profile should be deleted successfully" %step)

                            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_DelObject')
                            tdkTestObj.addParameter("paramName","Device.NAT.PortMapping.1.")
                            tdkTestObj.executeTestCase(expectedresult)
                            actualresult = tdkTestObj.getResult()
                            details = tdkTestObj.getResultDetails()
                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: The Port Mapping profile is deleted successfully. Details : %s" %(step, details))
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: Failed to delete the Port Mapping profile. Details : %s" %(step, details))
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Failed to add the Port Mapping profile or the added number of profiles are not expected. \nDevice.NAT.PortMappingNumberOfEntries : %s" %(step, details))
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        print("Failed to set the trigger value.")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Curl command execution failed. Details: %s" %(step, details))
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
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT : Factory Reset failed. Details : %s" %details)
        print("[TEST EXECUTION RESULT] : FAILURE")

    #Unload the modules loaded
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

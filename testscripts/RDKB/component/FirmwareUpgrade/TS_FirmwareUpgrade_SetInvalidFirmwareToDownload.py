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
  <name>TS_FirmwareUpgrade_SetInvalidFirmwareToDownload</name>
  <primitive_test_id/>
  <primitive_test_name>FirmwareUpgrade_DoNothing</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To verify that setting an invalid firmware image name results in the firmware download status being set to "Failed".</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_FirmwareUpgrade_2</test_case_id>
    <test_objective>To verify that setting an invalid firmware image name results in the firmware download status being set to "Failed".</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.A Python HTTP server should be running on a WAN machine accessible from the DUT, hosting current and target firmware images for upgrade.</pre_requisite>
    <api_or_interface_used></api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareToDownload
Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadURL
Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadNow
Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus</input_parameters>
    <automation_approch>1. Load the modules
2. Get the current firmware name and store it.
3. Set a valid Firmware Upgrade URL value, invalid FirmwaretoDownload value and FirmwareDownloadNow to true.
4. Get the FirmwareDownloadStatus and verify if it is returned as Failed.
5. Revert the Firmware Upgrade URL value and FirmwaretoDownload value values.
6. Unload the modules.</automation_approch>
    <expected_output>The firmware download status returns "Failed".</expected_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TS_FirmwareUpgrade_SetInvalidFirmwareToDownload</test_script>
    <skipped>No</skipped>
    <release_version>M141</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
from firmwareUpgradeUtility import *
from tdkutility import *

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_FirmwareUpgrade_SetInvalidFirmwareToDownload')
sysobj.configureTestCase(ip,port,'TS_FirmwareUpgrade_SetInvalidFirmwareToDownload')
# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus_sys.upper():
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    step = 1
    config_keys = ["FW_NAME_SUFFIX"]
    expectedresult = "SUCCESS"
    tdkTestObj, actualresult_all, config_values = GetPlatformProperties(sysobj, config_keys)
    suffix = config_values["FW_NAME_SUFFIX"]
    print("Config values obtained from tdk_platform_properties : %s" %config_values)

    print("\nTEST STEP %d: Get the required config values from tdk_platform.properties" %step)
    print("EXPECTED RESULT %d: Should get the config values from tdk_platform.properties" %step)
    if "FAILURE" not in actualresult_all:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Values retrieved from tdk_platform.properties file successfully" %step)
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        #Get FWUpgrade URL, FirmwaretoDownload and FirmwareDownloadNow values
        getflag, fw_values = getFWUpgradeConfig(obj, step)
        fw_url = fw_values["Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadURL"]
        FirmwaretoDownload = fw_values["Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareToDownload"]
        if getflag == 1:
            step += 1
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
            actual_result, details = getTR181Value(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus")
            print("TEST STEP %d : Get the initial Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus " %step)
            print("EXPECTED RESULT %d: Should get the initial FirmwareDownloadStatus " %step)
            print("Firmware Download Status : %s" %details)
            if expectedresult in actual_result:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: The initial FirmwareDownloadStatus is returned as %s." %(step,details))
                print("[TEST EXECUTION RESULT] : SUCCESS\n")

                # Set FirmwareVersion to an invalid value. The hardcoded values are dummy values for test purposes only.
                FirmwareVersion = "DummyImage"
                FirmwareFilename = FirmwareVersion + suffix

                step += 1
                # Set the FWUpgrade URL, FirmwaretoDownload and FirmwareDownloadNow values
                print("Setting the FirmwareURL to a valid value and the FirmwareToDownload to an invalid image name: %s" %FirmwareFilename)
                setflag = setFWUpgradeConfig(obj, step, FirmwareFilename)

                if setflag == 1:
                    step += 1
                    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                    actual_result, details = getTR181Value(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus")
                    print("TEST STEP %d : Get the Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus " %step)
                    print("EXPECTED RESULT %d: Should get the FirmwareDownloadStatus as Failed " %step)
                    print("Firmware Download Status : %s" %details)
                    if expectedresult in actual_result and details == "Failed":
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: FirmwareDownloadStatus is returned as Failed when an invalid Firmware name is set." %step)
                        print("[TEST EXECUTION RESULT] : SUCCESS\n")
                        # Revert the Firmware Upgrade URL value and FirmwaretoDownload value values
                        print("Reverting the FirmwareUpgradeURL value and FirmwaretoDownload value values")
                        step += 1
                        setflag = setFWUpgradeConfig(obj, step, FirmwaretoDownload, fw_url)
                        if setflag == 1:
                            print("Successfully reverted the Firmware Upgrade URL value and FirmwaretoDownload values\n")
                        else:
                            print("Failed to revert the Firmware Upgrade URL value and FirmwaretoDownload values\n")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: FirmwareDownloadStatus is not returned as Failed when an invalid Firmware name is set." %step)
                        print("[TEST EXECUTION RESULT] : FAILURE\n")
                else:
                    print("Failed to set the FWUpgrade values \n")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failure in getting initial FirmwareDownloadStatus. Details: %s" %(step,details))
                print("[TEST EXECUTION RESULT] : FAILURE\n")
        else:
            print("Failed to get the FWUpgrade values \n")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to retrieve config values from tdk_platform.properties file" %step)
        print("[TEST EXECUTION RESULT] : FAILURE \n")
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

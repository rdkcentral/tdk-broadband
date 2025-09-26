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
  <name>TS_FirmwareUpgrade_SetInvalidFirmwareUpgradeURL</name>
  <primitive_test_id/>
  <primitive_test_name>FirmwareUpgrade_DoNothing</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To verify that setting an invalid firmware upgrade url results in the firmware download status remaining "Not Started".</synopsis>
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
    <test_case_id>TC_FirmwareUpgrade_3</test_case_id>
    <test_objective>To verify that setting an invalid firmware upgrade url results in the firmware download status remaining "Not Started".</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script.</pre_requisite>
    <api_or_interface_used></api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareToDownload
Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadURL
Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadNow
Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus</input_parameters>
    <automation_approch>1. Load the modules
2. Get the tdk_platform.properties config values.
3. Get the current firmware name and store it.
4. Get the initial FirmwareDownloadStatus.
5. Set an invalid FirmwareUpgradeURL value, valid FirmwaretoDownload value and FirmwareDownloadNow to true.
6. Get the FirmwareDownloadStatus and verify if it remains as Not Started.
7. Revert the Firmware Upgrade URL value and FirmwaretoDownload value values.
8. Unload the modules.</automation_approch>
    <expected_output>The firmware download status remains "Not Started"</expected_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TS_FirmwareUpgrade_SetInvalidFirmwareUpgradeURL</test_script>
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
from firmwareUpgradeVariables import *
from tdkutility import *

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_FirmwareUpgrade_SetInvalidFirmwareUpgradeURL')
sysobj.configureTestCase(ip,port,'TS_FirmwareUpgrade_SetInvalidFirmwareUpgradeURL')
# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus_sys.upper():
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    step = 1
    config_keys = ["DEVICETYPE", "FW_NAME_SUFFIX"]
    expectedresult = "SUCCESS"
    tdkTestObj, actualresult_all, config_values = GetPlatformProperties(sysobj, config_keys)
    suffix = config_values["FW_NAME_SUFFIX"]
    platform = config_values["DEVICETYPE"]
    key_value = dict(zip(config_keys, config_values))
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


                step += 1
                # Set FirmwareLocation to an invalid value. The hardcoded values are dummy values for test purposes only.
                FirmwareLocation = "dummy_url.com"
                FirmwareFilename = FIRMWARE_UPGRADE_RPI if platform == "RPI" else FIRMWARE_UPGRADE_BPI
                # Set the FWUpgrade URL, FirmwaretoDownload and FirmwareDownloadNow values
                print("Setting the FirmwareURL to an invalid value and the FirmwareToDownload to an valid image name: %s" %FirmwareFilename)
                flag = setFWUpgradeConfig(obj, step,FirmwareFilename, FirmwareLocation)

                if flag == 1:
                    step += 1
                    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                    actual_result, details = getTR181Value(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus")
                    print("TEST STEP %d : Get the Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus " %step)
                    print("EXPECTED RESULT %d: The FirmwareDownloadStatus should remain as Not Started when invalid URL is set. " %step)
                    print("Firmware Download Status : %s" %details)
                    if expectedresult in actual_result and details == "Not Started":
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: FirmwareDownloadStatus remains Not Started when an invalid Firmware name is set." %step)
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
                        print("ACTUAL RESULT %d: FirmwareDownloadStatus is not returned as Not Started when an invalid Firmware name is set." %step)
                        print("[TEST EXECUTION RESULT] : FAILURE\n")
                else:
                    print("Failed to set the FWUpgrade values \n")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failure in getting initial FirmwareDownloadStatus. Details: %s" %(step,details))
                print("[TEST EXECUTION RESULT] : FAILURE\n")
        else:
            print("Failed to get the FWUpgrade configs \n")
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

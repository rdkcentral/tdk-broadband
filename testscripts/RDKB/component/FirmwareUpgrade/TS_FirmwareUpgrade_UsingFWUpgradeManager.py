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
  <name>TS_FirmwareUpgrade_UsingFWUpgradeManager</name>
  <primitive_test_id/>
  <primitive_test_name>FirmwareUpgrade_DoNothing</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Validate firmware upgrade by setting rules via FirmwireUpgrade TR-181 commands.</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_FirmwareUpgrade_1</test_case_id>
    <test_objective>Validate firmware image upgradation using firmware manager TR-181 commands</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.A Python HTTP server should be running on a WAN machine accessible from the DUT, hosting current and target firmware images for upgrade.
4.For Firmware Upgrades using Firmware Upgrade Manager, ensure the rootfs partition size should be increased to 5 GB.</pre_requisite>
    <api_or_interface_used></api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareToDownload
Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadURL
Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadNow
Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus</input_parameters>
    <automation_approch>1. Load the modules
2. Check whether the prerequisite of rootfs partition size is met.
3. Get the erouter IP address.
4. Get the current and target firmware details.
5. Check whether the target and initial firmware is available in the HTTP server deployed.
6. Get the required Firmware Upgrade URL, FirmwaretoDownload values and FirmwareDownloadNow.
7. Set the required Firmware Upgrade URL, FirmwaretoDownload values and FirmwareDownloadNow to true.
8. Save the current state and run the command to check whether the image is being downloaded in the required location.
9. Run the TDKBPackage_Installer to wait for the device to come up after reboot and bring up TDK if build does not already have TDK up.
10. Get the current firmware name and check if it matches the target firmware.
11. Revert the firmware to initial version.
12. Unload the modules.</automation_approch>
    <expected_output>Firmware Upgrade using FirmwareUpgrade Manager TR-181 commands should be successful.</expected_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TS_FirmwareUpgrade_UsingFWUpgradeManager</test_script>
    <skipped>No</skipped>
    <release_version>M141</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
from firmwareUpgradeVariables import *
from firmwareUpgradeUtility import *
from tdkutility import *
import TDKBPackage_Installer

def loadAndUnloadModules():
    # Test component to be tested
    sysobj = tdklib.TDKScriptingLibrary("sysutil","1")
    obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
    # IP and Port of box, No need to change,
    # This will be replaced with corresponding DUT Ip and port while executing script
    ip = <ipaddress>
    port = <port>
    flag = 0
    obj.configureTestCase(ip,port,'TS_FirmwareUpgrade_UsingFWUpgradeManager')
    sysobj.configureTestCase(ip,port,'TS_FirmwareUpgrade_UsingFWUpgradeManager')
    # Get the result of connection with test component and DUT
    loadmodulestatus1 = sysobj.getLoadModuleResult()
    loadmodulestatus = obj.getLoadModuleResult()
    if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
        flag = 1
    else:
        flag = 0
    return flag, obj, sysobj


load_flag, obj, sysobj = loadAndUnloadModules()

if load_flag == 1:
    sysobj.setLoadModuleStatus("SUCCESS")
    obj.setLoadModuleStatus("SUCCESS")

    print("Prerequisite: 1. Ensure a Python HTTP server is running in a WAN machine accessible from the DUT, hosting current and target firmware images for upgrade.\n 2. Ensure the rootfs partition size is around 5 GB.\n")

    expectedresult = "SUCCESS"
    # Check whether the prerequisite of rootfs partition size is met
    step = 1
    print("TEST STEP %d: Check whether the prerequisite of rootfs partition size is met" %step)
    print("EXPECTED RESULT %d: The rootfs partition size should be around 5 GB" %step)
    query = "df -h / | awk 'NR==2 {print $2}'"
    print("Query: %s" %query)
    tdkTestObj = sysobj.createTestStep('ExecuteCmd')
    actualresult, details = doSysutilExecuteCommand(tdkTestObj,query)
    size = float(details.strip()[:-1])
    # Check if the partition size is greater than or equal to 5 GB
    if expectedresult in actualresult and round(size) >= 5.0 and details.strip()[-1] == 'G':
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: The Prerequisite is met. Rootfs partition size is %s" %(step,details.strip()))
        print("[TEST EXECUTION RESULT] : SUCCESS\n")

        step += 1
        #get erouter IP address
        erouter_ip, step = getErouterIP(sysobj, step)
        if erouter_ip != "":
            step += 1
            # get details of the current firmware in the device
            Old_FirmwareVersion, Old_FirmwareFilename = getCurrentFirmware(sysobj, step)

            step += 1
            # get target firmware details
            FirmwareVersion, FirmwareFilename = getFirmwareDetailsFromServer(sysobj, step)

            if FirmwareFilename != Old_FirmwareFilename and FirmwareFilename and Old_FirmwareFilename:
                step += 1
                #Get FWUpgrade URL, FirmwaretoDownload and FirmwareDownloadNow values
                getflag, fw_values = getFWUpgradeConfig(obj, step)

                if getflag == 1:
                    #Get the initial FirmwareDownloadStatus
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
                        # Set the FWUpgrade URL, FirmwaretoDownload and FirmwareDownloadNow values
                        set_flag = setFWUpgradeConfig(obj, step, FirmwareFilename)
                        if set_flag == 1:
                            # Get the updated FirmwareDownloadStatus
                            step += 1
                            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                            actual_result, details = getTR181Value(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus")
                            print("TEST STEP %d : Get the Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus" %step)
                            print("EXPECTED RESULT %d: Should get the FirmwareDownloadStatus as In Progress" %step)
                            print("Firmware Download Status : %s" %details)
                            if expectedresult in actual_result and details == "In Progress":
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: FirmwareDownloadStatus is returned as In Progress." %step)
                                print("[TEST EXECUTION RESULT] : SUCCESS\n")

                                TDKBPackage_Installer.package_installer(erouter_ip)
                                load_flag, obj, sysobj= loadAndUnloadModules()
                                if load_flag == 1:
                                    sysobj.setLoadModuleStatus("SUCCESS")
                                    obj.setLoadModuleStatus("SUCCESS")
                                    print("\nAfter DUT firmware upgrade !!!! ")

                                    # get details of the current firmware in the device
                                    step += 1
                                    print("Check the firmware after the image is downloaded and device is up after reboot")
                                    New_FirmwareVersion, New_FirmwareFilename = getCurrentFirmware(sysobj, step)

                                    # Check whether the image is upgraded successfully
                                    step += 1
                                    print("TEST STEP %d: Check if the device has successfully updated to the target firmware version." %step)
                                    print("EXPECTED RESULT %d: The current image should match the target image" %step)
                                    if New_FirmwareVersion == FirmwareVersion:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: The image is upgraded to target image %s successfully." %(step, New_FirmwareVersion))
                                        print("[TEST EXECUTION RESULT] : SUCCESS \n")

                                        # Revert the firmware to initial version
                                        # Set the FWUpgrade URL, FirmwaretoDownload and FirmwareDownloadNow values
                                        print("Revert the firmware to initial version: %s" %Old_FirmwareFilename)
                                        step += 1
                                        flag = setFWUpgradeConfig(obj, step, Old_FirmwareFilename)
                                        if flag == 1:
                                            TDKBPackage_Installer.package_installer(erouter_ip)
                                            load_flag, obj, sysobj = loadAndUnloadModules()
                                            if load_flag == 1:
                                                sysobj.setLoadModuleStatus("SUCCESS")
                                                obj.setLoadModuleStatus("SUCCESS")
                                                print("\nAfter DUT firmware upgrade !!!! ")

                                                step += 1
                                                FirmwareVersion, FirmwareFilename = getCurrentFirmware(sysobj, step)
                                                # Check whether the image is reverted successfully
                                                if FirmwareVersion == Old_FirmwareVersion:
                                                    tdkTestObj.setResultStatus("SUCCESS")
                                                    print("Successfully reverted the firmware to the initial firmware\n")
                                                else:
                                                    tdkTestObj.setResultStatus("FAILURE")
                                                    print("Failed to revert the firmware version.\n")
                                            else:
                                                sysobj.setLoadModuleStatus("FAILURE")
                                                obj.setLoadModuleStatus("FAILURE")
                                                print("Module loading failed")
                                        else:
                                            print("Failed to set the FWUpgrade configs \n")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: Failed to upgrade the image. Current Image Details : %s" %(step, New_FirmwareVersion))
                                        print("[TEST EXECUTION RESULT] : FAILURE \n")
                                else:
                                    sysobj.setLoadModuleStatus("FAILURE")
                                    obj.setLoadModuleStatus("FAILURE")
                                    print("Module loading failed")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: FirmwareDownloadStatus is %s." %(step,details))
                                print("[TEST EXECUTION RESULT] : FAILURE\n")
                        else:
                            print("Failed to set the FirmwareUpgrade configs \n")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Failure in getting initial FirmwareDownloadStatus. Details: %s" %(step,details))
                        print("[TEST EXECUTION RESULT] : FAILURE\n")
                else:
                    print("Failed to get the initial FirmwareUpgrade configs \n")
            else:
                print("Firmware details not found or Target Firmware matches initial firmware \n")
        else:
            print("Erouter IP not found \n")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to meet the Prerequisite. Rootfs partition size is %s" %(step,details.strip()))
        print("[TEST EXECUTION RESULT] : FAILURE\n")
    sysobj.unloadModule("sysutil")
    obj.unloadModule("tdkbtr181")
else:
    sysobj.setLoadModuleStatus("FAILURE")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")






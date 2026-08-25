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

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
from firmwareUpgradeVariables import *
from firmwareUpgradeUtility import *
from tdkutility import *
import FirmwareUpgradeMonitor

def loadAndUnloadModules():
    # Test component to be tested
    sysobj = tdklib.TDKScriptingLibrary("sysutil", "1")
    obj = tdklib.TDKScriptingLibrary("tdkbtr181", "1")
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

    print("Prerequisite: Ensure a Python HTTP server is running in a WAN machine accessible from the DUT, hosting current and target firmware images for upgrade.\n")

    expectedresult = "SUCCESS"
    step = 1
    # get erouter IP address
    tdkTestObj, erouter_ip, step = getErouterIP(sysobj, step)
    if erouter_ip != "":
        step += 1
        # get details of the current firmware in the device
        Old_FirmwareVersion, Old_FirmwareFilename = getCurrentFirmware(sysobj, step)

        step += 1
        # get target firmware details
        FirmwareVersion, FirmwareFilename = getFirmwareDetailsFromServer(sysobj, step)

        if FirmwareFilename != Old_FirmwareFilename and FirmwareFilename and Old_FirmwareFilename:
            step += 1
            # Get the current firmware download config values
            getflag, fw_values = getFWUpgradeConfig(obj, step)

            if getflag == 1:
                fw_protocol = fw_values[FW_DOWNLOAD_PROTOCOL_DM]
                fw_url = fw_values[FW_DOWNLOAD_URL_DM]
                old_firmware_to_download = fw_values[FW_TO_DOWNLOAD_DM]
                # Get the initial FirmwareDownloadStatus
                step += 1
                tdkTestObj, details, status_ok = getFirmwareDownloadStatus(obj, step)
                if status_ok:
                    step += 1
                    # Set the firmware download config values and trigger the download
                    set_flag = setFWUpgradeConfig(obj, step, FirmwareFilename)
                    if set_flag == 1:
                        # Get the updated FirmwareDownloadStatus
                        step += 1
                        tdkTestObj, details, status_ok = getFirmwareDownloadStatus(obj, step, expected_status="Completed")
                        if status_ok:
                            revert_flag, upgraded_FirmwareVersion = FirmwareUpgradeMonitor.fw_upgrade_checker(erouter_ip, Old_FirmwareVersion, FirmwareVersion, FWUPGRADE_BINARY)
                            load_flag, obj, sysobj = loadAndUnloadModules()
                            if load_flag == 1:
                                sysobj.setLoadModuleStatus("SUCCESS")
                                obj.setLoadModuleStatus("SUCCESS")
                                print("\nAfter DUT firmware upgrade !!!! ")

                                step += 1
                                print(f"TEST STEP {step}: Check if the device has successfully updated to the target firmware version.")
                                print(f"EXPECTED RESULT {step}: The current image should match the target image")
                                if upgraded_FirmwareVersion == FirmwareVersion:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print(f"ACTUAL RESULT {step}: The image is upgraded to target image {upgraded_FirmwareVersion} successfully.")
                                    print("[TEST EXECUTION RESULT] : SUCCESS \n")

                                    step += 1
                                    FirmwareVersionAfterRecover, FirmwareFilenameAfterRecover = getCurrentFirmware(sysobj, step)
                                    print(f"TEST STEP {step}: Check if the DUT firmware has been successfully reverted to the initial firmware version.")
                                    print(f"EXPECTED RESULT {step}: The current firmware should match the initial firmware image")
                                    if FirmwareVersionAfterRecover == Old_FirmwareVersion and revert_flag:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print(f"ACTUAL RESULT {step}: Reverted to initial firmware {Old_FirmwareVersion} successfully.")
                                        print("[TEST EXECUTION RESULT] : SUCCESS \n")

                                        step += 1
                                        print("Reverting the FirmwareDownloadProtocol, FirmwareUpgradeURL and FirmwareToDownload values")
                                        set_flag = setFWUpgradeConfig(obj, step, old_firmware_to_download, fw_url, fw_protocol, trigger_download=False)
                                        if set_flag == 1:
                                            print("Successfully reverted the FirmwareDownloadProtocol, FirmwareUpgradeURL and FirmwareToDownload values\n")
                                        else:
                                            print("Failed to revert the FirmwareDownloadProtocol, FirmwareUpgradeURL and FirmwareToDownload values\n")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print(f"ACTUAL RESULT {step}: Failed to revert the image. Current Firmware Version : {FirmwareVersionAfterRecover}")
                                        print("[TEST EXECUTION RESULT] : FAILURE \n")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print(f"ACTUAL RESULT {step}: The image is not upgraded to target image. Current Firmware Version : {upgraded_FirmwareVersion}")
                                    print("[TEST EXECUTION RESULT] : FAILURE \n")
                            else:
                                sysobj.setLoadModuleStatus("FAILURE")
                                obj.setLoadModuleStatus("FAILURE")
                                print("Module loading failed")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: FirmwareDownloadStatus is {details}.")
                            print("[TEST EXECUTION RESULT] : FAILURE\n")
                    else:
                        print("Failed to set the FirmwareUpgrade configs \n")
            else:
                print("Failed to get the initial FirmwareUpgrade configs \n")
        else:
            print("Firmware details not found or Target Firmware matches initial firmware \n")
    else:
        print("Erouter IP not found \n")
    sysobj.unloadModule("sysutil")
    obj.unloadModule("tdkbtr181")
else:
    sysobj.setLoadModuleStatus("FAILURE")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

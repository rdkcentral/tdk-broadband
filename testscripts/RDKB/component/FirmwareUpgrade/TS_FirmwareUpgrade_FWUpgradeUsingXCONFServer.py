##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2026 RDK Management
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
from time import sleep
from firmwareUpgradeVariables import *
from firmwareUpgradeUtility import *
from tdkutility import *
import FirmwareUpgradeMonitor

#Function to load and unload the required module
def loadAndUnloadModules():
    #Test component to be tested
    obj = tdklib.TDKScriptingLibrary("sysutil","1")
    #IP and Port of box, No need to change,
    #This will be replaced with corresponding DUT Ip and port while executing script
    ip = <ipaddress>
    port = <port>
    obj.configureTestCase(ip,port,'TS_FirmwareUpgrade_FWUpgradeUsingXCONFServer')
    #Get the result of connection with test component and DUT
    loadmodulestatus =obj.getLoadModuleResult()
    flag = int("SUCCESS" in loadmodulestatus.upper())
    return flag, obj

load_flag, obj = loadAndUnloadModules()
expectedresult = "SUCCESS"

if load_flag == 1:
    obj.setLoadModuleStatus("SUCCESS")

    print("\nPrerequisites: Ensure a Python HTTP server is running in a WAN machine accessible from the DUT, hosting current and target firmware images for upgrade.\n The local http server location should be configured in rdkcentral Xconf server to override the default location.\n")

    step = 1
    #get erouter IP address
    erouter_ip, step = getErouterIP(obj, step)

    step += 1
    #get details of the current firmware in the device

    Old_FirmwareVersion, Old_FirmwareFilename = getCurrentFirmware(obj, step)

    step += 1
    #get target firmware details
    FirmwareVersion, FirmwareFilename = getFirmwareDetailsFromServer(obj, step)

    if FirmwareFilename != Old_FirmwareFilename and FirmwareFilename and erouter_ip != "":
        step += 1
        #Configure the Xconf server config and rules. "POST" - Create Config and "PUT" - Update Config
        FW_VERSION_CHECKSUM = FirmwareFilename + checksum_suffix
        config_curl_cmd = getXCONFServer_CreateConfigCmd(obj, FW_VERSION_CHECKSUM, FirmwareFilename, "POST", step)
        step += 1
        size = len(config_curl_cmd)
        result = [None] * size
        cmd_details = [None] * size
        index = 0
        for operation, config_cmd in config_curl_cmd.items():
            sleep(XCONF_CMD_WAIT)
            if operation == "Get Config":
                sleep(XCONF_CMD_WAIT)  # Wait for the last command to ensure the server is ready
                print(f"\nValidating the added rule using {operation}")
            else:
                print(f"\nConfiguring {operation} in XConf Server")
            print(f"\nCommand: {config_cmd}")
            tdkTestObj = obj.createTestStep('ExecuteCmd')
            result[index], cmd_details[index] = doSysutilExecuteCommand(tdkTestObj, config_cmd)
            print(f"\nCommand details: {cmd_details[index]}\n")
            if not checkValidResponse(cmd_details[index]):
                result[index] = "FAILURE"
            index += 1

        print(f"Command execution result: {result}")
        print(f"\nTEST STEP {step}: Configure the XConf server - Model, Mac List, Firmware Config, MAC Rule and Define Properties with target firmware details. ")
        print(f"EXPECTED RESULT {step}: Should configure the XConf server Firmware Configs, MAC Rule and Define Properties with target firmware details.")
        if "FAILURE" not in result and "" not in cmd_details:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: The XConf server rules configured successfully. Details: {cmd_details[size-1]} ")
            print("[TEST EXECUTION RESULT] : SUCCESS\n")

            step += 1
            #Check whether firmware download is triggered in the device
            tdkTestObj, trigger_flag, step = triggerFirmwareDownload(obj, FWUPGRADE_BINARY, logFile, step)

            if trigger_flag:
                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS\n")
                step += 1
                #Check whether the firmware download is in progress in the device
                tdkTestObj, monitor_flag = monitorFirmwareUpgrade(obj, FirmwareFilename, FW_DOWNLOAD_PATH, step)

                if monitor_flag:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("[TEST EXECUTION RESULT] : SUCCESS\n")
                    revert_flag, upgraded_FirmwareVersion = FirmwareUpgradeMonitor.fw_upgrade_checker(erouter_ip, Old_FirmwareVersion, FirmwareVersion, FWUPGRADE_BINARY)

                    load_flag, obj = loadAndUnloadModules()
                    if load_flag == 1:
                        obj.setLoadModuleStatus("SUCCESS")
                        print("Module reloaded successfully after fwupgrade reboot")

                        #Check whether the image is upgraded successfully
                        step += 1
                        print(f"\nTEST STEP {step}: Check if the device has successfully updated to the target firmware version {FirmwareVersion}.")
                        print(f"EXPECTED RESULT {step}: The current image should match the target image")
                        if upgraded_FirmwareVersion == FirmwareVersion:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: The image is upgraded to target image {upgraded_FirmwareVersion} successfully.")
                            print("[TEST EXECUTION RESULT] : SUCCESS \n")

                            step += 1
                            #Checking whether reverting to initial firmware is successful or not using recover command
                            FirmwareVersion, FirmwareFilename = getCurrentFirmware(obj, step)
                            print(f"\nTEST STEP {step}: Check if the DUT firmware has been successfully reverted to the initial firmware version {Old_FirmwareVersion}.")
                            print(f"EXPECTED RESULT {step}: The current firmware should match the initial firmware image")
                            if FirmwareVersion == Old_FirmwareVersion and revert_flag:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"ACTUAL RESULT {step}: Reverted to initial firmware {Old_FirmwareVersion} successfully.")
                                print("[TEST EXECUTION RESULT] : SUCCESS \n")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: Failed to revert the image. Current Firmware Version : {FirmwareVersion}")
                                print("[TEST EXECUTION RESULT] : FAILURE \n")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: Failed to upgrade to target image. Current image is {FirmwareVersion}")
                            print("[TEST EXECUTION RESULT] : FAILURE \n")
                    else:
                        print("Failed to reload module after firmware upgrade reboot")
                        obj.setLoadModuleStatus("FAILURE")
                        print("Module loading failed after fwupgrade reboot")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("[TEST EXECUTION RESULT] : FAILURE\n")
                    print("The firmware is not available in the {FW_DOWNLOAD_PATH}.")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("[TEST EXECUTION RESULT] : FAILURE\n")
                print("Firmware download is not triggered in the device.")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Failed to configure the XConf server rules. Details: {cmd_details[size-1]} ")
            print("[TEST EXECUTION RESULT] : FAILURE\n")

        #Delete the XConf rule
        step += 1
        delete_curl_cmd = getXCONFServer_DeleteConfigCmd()
        size = len(delete_curl_cmd)
        result = [None] * size
        details = [None] * size
        for index in range(size):
            print(f"\nCommand: {delete_curl_cmd[index]}")
            tdkTestObj = obj.createTestStep('ExecuteCmd')
            result[index], details[index] = doSysutilExecuteCommand(tdkTestObj,delete_curl_cmd[index])
        print(f"\nTEST STEP {step}: Delete the XConf server Firmware MAC Rule, Firmware Config and Model")
        print(f"EXPECTED RESULT {step}: Should delete the XConf server Firmware MAC Rule, Firmware Config and Model")
        print(f"Command execution details: {details}")
        if "FAILURE" not in result:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: The XConf server rules deleted successfully.")
            print("[TEST EXECUTION RESULT] : SUCCESS\n")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Failed to delete the XConf server rules. Details {details} ")
            print("[TEST EXECUTION RESULT] : FAILURE \n")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("Required Details are not available to proceed with firmware upgrade. So skipping the test\n")

    #Unload the module
    obj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

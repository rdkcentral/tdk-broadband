# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
from time import sleep
from firmwareUpgradeVariables import *
from firmwareUpgradeUtility import *
from tdkutility import *

#Function to load and unload the required module
def loadAndUnloadModules():
    #Test component to be tested
    obj = tdklib.TDKScriptingLibrary("sysutil","1")
    #IP and Port of box, No need to change,
    #This will be replaced with corresponding DUT Ip and port while executing script
    ip = <ipaddress>
    port = <port>
    obj.configureTestCase(ip,port,'TS_FirmwareUpgrade_InvalidURL_FWUpgradeUsingXCONFServer')
    #Get the result of connection with test component and DUT
    loadmodulestatus =obj.getLoadModuleResult()
    flag = int("SUCCESS" in loadmodulestatus.upper())
    return flag, obj

load_flag, obj = loadAndUnloadModules()
expectedresult = "SUCCESS"

XCONF_CMD_WAIT = 30

if load_flag == 1:
    obj.setLoadModuleStatus("SUCCESS")

    print("\nPrerequisites: Ensure a Python HTTP server is running in a WAN machine accessible from the DUT, hosting current and target firmware images for upgrade.\n The local http server location should be configured in rdkcentral Xconf server to override the default location.\n")

    step = 1
    #Get the required config values from tdk_platform.properties file
    config_keys = ["FW_UPGRADE_BINARY", "FW_DOWNLOAD_PATH", "DEVICETYPE", "FW_NAME_SUFFIX"]

    tdkTestObj, actualresult_all ,config_values = GetPlatformProperties(obj, config_keys)
    FWUPGRADE_BINARY = config_values["FW_UPGRADE_BINARY"]
    FW_DOWNLOAD_PATH = config_values["FW_DOWNLOAD_PATH"]
    platform = config_values["DEVICETYPE"]
    suffix = config_values["FW_NAME_SUFFIX"]

    print(f"Config values obtained from tdk_platform_properties : {config_values}")

    print(f"\nTEST STEP {step}: Get the required config values from tdk_platform.properties")
    print(f"EXPECTED RESULT {step}: Should get the config values from tdk_platform.properties")
    if "FAILURE" not in actualresult_all:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Values retrieved from tdk_platform.properties file successfully")
        print("[TEST EXECUTION RESULT] : SUCCESS\n")

        step += 1
        #get erouter IP address
        tdkTestObj, erouter_ip, step = getErouterIP(obj, step)

        step += 1
        #get details of the current firmware in the device

        Old_FirmwareVersion, Old_FirmwareFilename = getCurrentFirmware(obj, step)

        step += 1
        #get target firmware details
        TARGET_FIRMWARE_UPGRADE = "FIRMWARE_UPGRADE_" + platform
        FirmwareVersion = globals()[TARGET_FIRMWARE_UPGRADE]
        FirmwareFilename = FirmwareVersion + suffix
        print(f"TEST STEP {step}: Fetch the target firmware name")
        print(f"EXPECTED RESULT {step}: Should fetch the target firmware name successfully")
        print(f"ACTUAL RESULT {step}: Target Firmware Details - {FirmwareFilename}.")
        if FirmwareVersion:
            tdkTestObj.setResultStatus("SUCCESS")
            print("[TEST EXECUTION RESULT] : SUCCESS\n")

            if FirmwareFilename != Old_FirmwareFilename and erouter_ip != "":
                step += 1
                #Configure the Xconf server config and rules. "POST" - Create Config and "PUT" - Update Config
                FW_VERSION_CHECKSUM = FirmwareFilename + checksum_suffix
                config_curl_cmd = getXCONFServer_CreateConfigCmd(obj, FW_VERSION_CHECKSUM, FirmwareFilename, "POST", step, scenario = "invalid_url")
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
                print(f"\nTEST STEP {step}: Configure the XConf server - Model, Mac List, Firmware Config, MAC Rule and Define Properties with invalid firmware URL details. ")
                print(f"EXPECTED RESULT {step}: Should configure the XConf server Firmware Configs, MAC Rule and Define Properties with invalid firmware URL details.")
                if "FAILURE" not in result and "" not in cmd_details:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: The XConf server rules configured successfully. Details: {cmd_details[size-1]} ")
                    print("[TEST EXECUTION RESULT] : SUCCESS\n")

                    step += 1
                    #Check whether firmware download is triggered in the device
                    tdkTestObj, trigger_flag, step = triggerFirmwareDownload(obj, FWUPGRADE_BINARY, logFile, step, scenario="invalid")

                    if not trigger_flag:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("[TEST EXECUTION RESULT] : SUCCESS\n")
                        print("Falilure logs are present in the device logs indicating firmware download is not triggered due to invalid firmware URL in XConf server config.")

                        step += 1
                        #Check whether the firmware download is in progress in the device
                        tdkTestObj, monitor_flag = monitorFirmwareUpgrade(obj, FirmwareFilename, FW_DOWNLOAD_PATH, step, scenario="invalid")

                        if not monitor_flag:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("[TEST EXECUTION RESULT] : SUCCESS\n")
                            print("The firmware file is not found in the download location as the firmware download is not triggered due to invalid firmware URL in XConf server config.")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("[TEST EXECUTION RESULT] : FAILURE\n")
                            print("The firmware is available in the {FW_DOWNLOAD_PATH}.")

                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("[TEST EXECUTION RESULT] : FAILURE\n")
                        print("Firmware download is triggered in the device.")

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
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("[TEST EXECUTION RESULT] : FAILURE\n")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to retrieve config values from tdk_platform.properties file")
        print("[TEST EXECUTION RESULT] : FAILURE \n")
    #Unload the module
    obj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

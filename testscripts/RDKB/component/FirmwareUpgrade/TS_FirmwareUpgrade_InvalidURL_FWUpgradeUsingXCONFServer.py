# use tdklib library,which provides a wrapper for tdk testcase script

import tdklib
from time import sleep
from firmwareUpgradeVariables import *
from firmwareUpgradeUtility import *
from tdkutility import *


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
SERVICE_RESTART_WAIT = 20
PARTITION_CREATION_WAIT = 100

if load_flag == 1:
    obj.setLoadModuleStatus("SUCCESS")

    print("\nPrerequisites: Ensure a Python HTTP server is running in a WAN machine accessible from the DUT, hosting current and target firmware images for upgrade.\n The local http server location should be configured in rdkcentral XConf server to override the default location.\n")

    step = 1
    #Get the required config values from tdk_platform.properties file
    config_keys = ["FW_UPGRADE_SERVICE"]
    
    tdkTestObj, actualresult_all ,config_values = GetPlatformProperties(obj, config_keys)
    FWUPGRADE_SERVICE = config_values["FW_UPGRADE_SERVICE"]
    print(f"Config values obtained from tdk_platform_properties : {config_values}")

    print(f"\nTEST STEP {step}: Get the required config values from tdk_platform.properties")
    print(f"EXPECTED RESULT {step}: Should get the config values from tdk_platform.properties")
    if "FAILURE" not in actualresult_all:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Values retrieved from tdk_platform.properties file successfully")
        print("[TEST EXECUTION RESULT] : SUCCESS\n")

        step += 1
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
            config_curl_cmd = getXCONFServer_CreateConfigCmd(obj, FirmwareVersion, FirmwareFilename, "POST", step, scenario = "invalid_url")
            
            step += 1
            size = len(config_curl_cmd)
            result = [None] * size
            cmd_details = [None] * size
            for index in range(size):
                print(f"\nCommand: {config_curl_cmd[index]}")
                sleep(XCONF_CMD_WAIT)
                if index == size - 1:
                    sleep(XCONF_CMD_WAIT)  # Wait for the last command to ensure the server is ready
                tdkTestObj = obj.createTestStep('ExecuteCmd')
                result[index], cmd_details[index] = doSysutilExecuteCommand(tdkTestObj,config_curl_cmd[index])
                print(f"\nCommand details: {cmd_details[index]}\n\n")
                if not checkValidResponse(cmd_details[index]):
                    result[index] = "FAILURE"

            print(f"Command execution result: {result}")
            print(f"\nTEST STEP {step}: Configure the XConf server - Firmware Config, Mac List, Mac Rule and Properties of Firmware rule [with invalid firmware upload location]")
            print(f"EXPECTED RESULT {step}: Should configure the XConf server Firmware Configs and Rule")
            if "FAILURE" not in result and "" not in cmd_details:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: The XConf server rules configured successfully. Details: {cmd_details[size-1]} ")
                print("[TEST EXECUTION RESULT] : SUCCESS\n")
                
                step += 1
                partition_count = getPartitionCount(obj, step)
                
                step += 1
                command = "systemctl restart " + FWUPGRADE_SERVICE
                print(f"Command: {command}")
                if partition_count < 3:
                    print(f"TEST STEP {step}: Restart the {FWUPGRADE_SERVICE} to create partition, wait for DUT to come up after reboot and upgrade the image.")
                    print(f"EXPECTED RESULT {step}: Should restart {FWUPGRADE_SERVICE} successfully, create partition and upgrade the image.")
                    #Saving the current state before firmware upgrade reboot
                    obj.saveCurrentState()
                    print(f"Command: {command}")
                    # Restart the swupdate service to trigger firmware upgrade
                    print(f"Restarting the {FWUPGRADE_SERVICE} to create partitions")
                    tdkTestObj = obj.createTestStep('ExecuteCmdReboot')
                    tdkTestObj.addParameter("command",command)
                    tdkTestObj.executeTestCase("SUCCESS")
                    sleep(PARTITION_CREATION_WAIT)
                    #Restore the saved state
                    obj.restorePreviousStateAfterReboot()
                    actualresult = tdkTestObj.getResult()
                else:
                    print(f"TEST STEP {step}: Restart the {FWUPGRADE_SERVICE} to trigger fwupgrade.")
                    print(f"EXPECTED RESULT {step}: Should restart {FWUPGRADE_SERVICE} successfully.")
                    # Restart the swupdate service to trigger firmware upgrade
                    tdkTestObj = obj.createTestStep('ExecuteCmd')
                    actualresult, details = doSysutilExecuteCommand(tdkTestObj,command)
                    
                sleep(SERVICE_RESTART_WAIT)
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: The {FWUPGRADE_SERVICE} is restarted successfully.")
                    print("[TEST EXECUTION RESULT] : SUCCESS\n")
                        
                    #Check whether firmware download is triggered in the device
                    step += 1
                    query = f"ls {xconf_firmware_location} | grep {FirmwareFilename}"
                    print(f"Command: {query}")

                    tdkTestObj = obj.createTestStep('ExecuteCmd')
                    actualresult, details = doSysutilExecuteCommand(tdkTestObj, query)

                    print(f"TEST STEP {step}: Check whether the firmware download is triggered in the device when invalid firmware location is provided")
                    print(f"EXPECTED RESULT {step}: The firmware download should not be triggered in the device")
                    if expectedresult in actualresult and FirmwareFilename not in details.strip():
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Firmware download is not triggered as expected since invalid firmware location is provided. Details: {details.strip()}")
                        print("[TEST EXECUTION RESULT] : SUCCESS\n")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Firmware download is triggered unexpectedly. Details: {details.strip()}")
                        print("[TEST EXECUTION RESULT] : FAILURE \n")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Failed to restart {FWUPGRADE_SERVICE}.")
                    print("[TEST EXECUTION RESULT] : FAILURE \n")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Failed to configure XConf server as required.")
                print("[TEST EXECUTION RESULT] : FAILURE \n")
            
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
            print(f"TEST STEP {step}: Delete the XConf server Firmware Rule, Firmware Config, MAC Rule and MACList")
            print(f"EXPECTED RESULT {step}: Should delete the XConf server Firmware Rule, Firmware Config, MAC Rule and MACList")
            if "FAILURE" not in result and all(detail == "" for detail in details):
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: The XConf server rules deleted successfully.")
                print("[TEST EXECUTION RESULT] : SUCCESS\n")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Failed to delete the XConf server rules. Details {details} ")
                print("[TEST EXECUTION RESULT] : FAILURE \n")
        else:
            print("Required Details are not available to proceed with firmware upgrade. So skipping the test\n")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to retrieve config values from tdk_platform.properties file")
        print("[TEST EXECUTION RESULT] : FAILURE \n")

    obj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

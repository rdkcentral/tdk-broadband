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
from firmwareUpgradeUtility import *
from tdkutility import *

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181", "1")
sysobj = tdklib.TDKScriptingLibrary("sysutil", "1")

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
    print(f"Config values obtained from tdk_platform_properties : {config_values}")

    print(f"\nTEST STEP {step}: Get the required config values from tdk_platform.properties")
    print(f"EXPECTED RESULT {step}: Should get the config values from tdk_platform.properties")
    if "FAILURE" not in actualresult_all:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Values retrieved from tdk_platform.properties file successfully")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Get the current firmware download config values
        getflag, fw_values = getFWUpgradeConfig(obj, step)
        fw_protocol = fw_values[FW_DOWNLOAD_PROTOCOL_DM]
        fw_url = fw_values[FW_DOWNLOAD_URL_DM]
        FirmwaretoDownload = fw_values[FW_TO_DOWNLOAD_DM]
        if getflag == 1:
            step += 1
            tdkTestObj, details, status_ok = getFirmwareDownloadStatus(obj, step)
            if status_ok:

                # Set FirmwareVersion to an invalid value. The hardcoded values are dummy values for test purposes only.
                FirmwareVersion = "DummyImage"
                FirmwareFilename = FirmwareVersion + suffix

                step += 1
                # Set the firmware download config values and trigger the download
                print(f"Setting the FirmwareURL to a valid value and the FirmwareToDownload to an invalid image name: {FirmwareFilename}")
                setflag = setFWUpgradeConfig(obj, step, FirmwareFilename)

                if setflag == 1:
                    step += 1
                    tdkTestObj, details, status_ok = getFirmwareDownloadStatus(obj, step, expected_status="Failed")
                    if status_ok:
                        # Revert the FirmwareDownloadProtocol, FirmwareUpgradeURL and FirmwareToDownload values
                        print("Reverting the FirmwareDownloadProtocol, FirmwareUpgradeURL and FirmwareToDownload values")
                        step += 1
                        setflag = setFWUpgradeConfig(obj, step, FirmwaretoDownload, fw_url, fw_protocol, trigger_download=False)
                        if setflag == 1:
                            print("Successfully reverted the FirmwareDownloadProtocol, FirmwareUpgradeURL and FirmwareToDownload values\n")
                        else:
                            print("Failed to revert the FirmwareDownloadProtocol, FirmwareUpgradeURL and FirmwareToDownload values\n")
                else:
                    print("Failed to set the FWUpgrade values \n")
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Failure in getting initial FirmwareDownloadStatus. Details: {details}")
                    print("[TEST EXECUTION RESULT] : FAILURE\n")
        else:
            print("Failed to get the FWUpgrade values \n")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to retrieve config values from tdk_platform.properties file")
        print("[TEST EXECUTION RESULT] : FAILURE \n")
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

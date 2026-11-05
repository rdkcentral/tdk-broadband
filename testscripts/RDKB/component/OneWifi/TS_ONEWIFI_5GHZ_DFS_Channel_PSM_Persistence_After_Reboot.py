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

import tdklib
from tdkutility import *
from time import sleep
import random

DFS_CHANNELS = [52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144]

obj = tdklib.TDKScriptingLibrary("wifiagent", "1")
sysobj = tdklib.TDKScriptingLibrary("sysutil", "1")
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_ONEWIFI_5GHZ_DFS_Channel_PSM_Persistence_After_Reboot')
sysobj.configureTestCase(ip,port,'TS_ONEWIFI_5GHZ_DFS_Channel_PSM_Persistence_After_Reboot')

loadmodulestatus = obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus)
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1
    dfs_channel_to_set = str(random.choice(DFS_CHANNELS))

    # Step 1: Enable DFS RFC
    tdkTestObj, actualresult = wifi_SetParam(obj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable", "true", "boolean")
    sleep(2)
    print(f"\nTEST STEP {step}: Enable DFS RFC")
    print(f"EXPECTED RESULT {step}: DFS RFC should be enabled")
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
        print("TEST EXECUTION RESULT : SUCCESS")

        # Step 2: Disable Auto Channel Selection
        step += 1
        tdkTestObj, actualresult = wifi_SetParam(obj, "Device.WiFi.Radio.2.AutoChannelEnable", "false", "boolean")
        sleep(2)
        print(f"\nTEST STEP {step}: Disable Auto Channel Selection")
        print(f"EXPECTED RESULT {step}: AutoChannelEnable should be false")
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
            print("TEST EXECUTION RESULT : SUCCESS")

            # Step 3: Set DFS channel and apply
            step += 1
            tdkTestObj, actualresult = wifi_SetParam(obj, "Device.WiFi.Radio.2.Channel", dfs_channel_to_set, "unsignedint")
            sleep(2)
            wifi_SetParam(obj, "Device.WiFi.ApplyRadioSettings", "true", "boolean")
            sleep(5)
            print(f"\nTEST STEP {step}: Set 5 GHz radio channel to DFS channel {dfs_channel_to_set} and apply")
            print(f"EXPECTED RESULT {step}: Channel should be set to {dfs_channel_to_set}")
            tdkTestObj, actualresult, current_channel = wifi_GetParam(obj, "Device.WiFi.Radio.2.Channel")
            if expectedresult in actualresult and current_channel == dfs_channel_to_set:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Channel is {current_channel}")
                print("TEST EXECUTION RESULT : SUCCESS")

                # Step 4: Reboot
                step += 1
                print(f"\nTEST STEP {step}: Reboot the device")
                print(f"EXPECTED RESULT {step}: Device should reboot and come back online")
                doRebootDUT(sysobj)
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Device rebooted successfully")
                print("TEST EXECUTION RESULT : SUCCESS")

                # Step 5: Verify DFS channel persisted after reboot
                step += 1
                paramNames = [
                    "Device.WiFi.Radio.2.Channel",
                    "Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable",
                    "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable"
                ]
                paramResults = {}
                actualresult_all = []
                for paramName in paramNames:
                    tdkTestObj, actualresult, paramValue = wifi_GetParam(obj, paramName)
                    actualresult_all.append(actualresult)
                    paramResults[paramName] = paramValue
                channel_after = paramResults["Device.WiFi.Radio.2.Channel"]
                dfs_enable_after = paramResults["Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable"]
                dfs_rfc_after = paramResults["Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable"]
                print(f"\nTEST STEP {step}: Verify DFS channel and DFS DMs after reboot")
                print(f"EXPECTED RESULT {step}: Channel should be {dfs_channel_to_set}, DFS RFC and DFSEnable should be true")
                if "FAILURE" not in actualresult_all and channel_after == dfs_channel_to_set and dfs_rfc_after == "true" and dfs_enable_after == "true":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Channel is {channel_after}, DFS RFC is {dfs_rfc_after}, DFSEnable is {dfs_enable_after}")
                    print("TEST EXECUTION RESULT : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Channel is {channel_after}, DFS RFC is {dfs_rfc_after}, DFSEnable is {dfs_enable_after}")
                    print("TEST EXECUTION RESULT : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Channel is {current_channel}, expected {dfs_channel_to_set}")
                print("TEST EXECUTION RESULT : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: AutoChannelEnable SET FAILURE")
            print("TEST EXECUTION RESULT : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Enable DFS RFC FAILURE")
        print("TEST EXECUTION RESULT : FAILURE")

    # Revert all the parameters changed to default value
    print("\n--- Reverting DFS RFC and AutoChannelEnable to default ---")
    wifi_SetParam(obj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable", "false", "boolean")
    wifi_SetParam(obj, "Device.WiFi.Radio.2.AutoChannelEnable", "true", "boolean")
    sleep(2)
    obj.unloadModule("wifiagent")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

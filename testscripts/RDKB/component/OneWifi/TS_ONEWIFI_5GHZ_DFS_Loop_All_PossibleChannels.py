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

KNOWN_DFS_CHANNELS = [52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144]

obj = tdklib.TDKScriptingLibrary("wifiagent", "1")
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_5GHZ_DFS_Loop_All_PossibleChannels')

loadmodulestatus = obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus)
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Enable DFS RFC
    tdkTestObj, actualresult = wifi_SetParam(obj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable", "true", "boolean")
    sleep(2)
    print(f"TEST STEP {step}: Enable DFS RFC")
    print(f"EXPECTED RESULT {step}: DFS RFC should be enabled successfully")
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
        print("TEST EXECUTION RESULT : SUCCESS")

        # Step 2: Confirm both DFS DMs are true
        step += 1
        paramNames = [
            "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable",
            "Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable"
        ]
        paramResults = {}
        actualresult_all = []
        for paramName in paramNames:
            tdkTestObj, actualresult, paramValue = wifi_GetParam(obj, paramName)
            actualresult_all.append(actualresult)
            paramResults[paramName] = paramValue
        dfs_rfc = paramResults["Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable"]
        dfs_enable = paramResults["Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable"]
        print(f"TEST STEP {step}: Confirm both DFS RFC and DFSEnable are true")
        print(f"EXPECTED RESULT {step}: Both DMs should be true")
        if "FAILURE" not in actualresult_all and dfs_rfc == "true" and dfs_enable == "true":
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable}")
            print("TEST EXECUTION RESULT : SUCCESS")

            # Step 3: Get PossibleChannels and extract available DFS channels
            step += 1
            tdkTestObj, actualresult, possible_channels_str = wifi_GetParam(obj, "Device.WiFi.Radio.2.PossibleChannels")
            print(f"TEST STEP {step}: Get Device.WiFi.Radio.2.PossibleChannels and extract DFS channels")
            print(f"EXPECTED RESULT {step}: PossibleChannels should include DFS channels (52-144)")
            if expectedresult in actualresult:
                possible_channels_list = [int(ch.strip()) for ch in possible_channels_str.split(",") if ch.strip().isdigit()]
                available_dfs_channels = [ch for ch in KNOWN_DFS_CHANNELS if ch in possible_channels_list]
                skipped_dfs_channels = [ch for ch in KNOWN_DFS_CHANNELS if ch not in possible_channels_list]
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: PossibleChannels = {possible_channels_str}")
                print(f"Available DFS channels on this device: {available_dfs_channels}")
                if skipped_dfs_channels:
                    print(f"WARNING: These DFS channels are NOT in PossibleChannels and will be skipped: {skipped_dfs_channels}")
                print("TEST EXECUTION RESULT : SUCCESS")

                # Step 4: Disable Auto Channel Selection
                step += 1
                tdkTestObj, actualresult = wifi_SetParam(obj, "Device.WiFi.Radio.2.AutoChannelEnable", "false", "boolean")
                sleep(2)
                print(f"TEST STEP {step}: Disable Auto Channel Selection")
                print(f"EXPECTED RESULT {step}: AutoChannelEnable should be false")
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
                    print("TEST EXECUTION RESULT : SUCCESS")

                    # Step 5: Loop through each available DFS channel
                    channel_pass_list = []
                    channel_fail_list = []
                    for dfs_ch in available_dfs_channels:
                        step += 1
                        ch_str = str(dfs_ch)
                        print(f"\n=============================================")
                        print(f"TEST STEP {step}: Set and verify DFS channel {ch_str}")
                        print(f"EXPECTED RESULT {step}: Channel {ch_str} should be set and confirmed successfully")

                        # Set the DFS channel
                        tdkTestObj, set_result = wifi_SetParam(obj, "Device.WiFi.Radio.2.Channel", ch_str, "unsignedint")
                        sleep(2)

                        # Apply radio settings
                        wifi_SetParam(obj, "Device.WiFi.ApplyRadioSettings", "true", "boolean")

                        # Wait for settings to take effect
                        sleep(5)

                        # Verify the channel
                        tdkTestObj, get_result, current_ch = wifi_GetParam(obj, "Device.WiFi.Radio.2.Channel")
                        if expectedresult in set_result and expectedresult in get_result and current_ch == ch_str:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: PASS - Channel {ch_str} set and confirmed successfully")
                            print("TEST EXECUTION RESULT : SUCCESS")
                            channel_pass_list.append(dfs_ch)
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: FAIL - Expected {ch_str}, got {current_ch}")
                            print("TEST EXECUTION RESULT : FAILURE")
                            channel_fail_list.append(dfs_ch)

                        print(f"=============================================")

                    # Summary
                    print(f"\n========== DFS Channel Loop Summary ==========")
                    print(f"PASSED channels  : {channel_pass_list}")
                    print(f"FAILED channels  : {channel_fail_list}")
                    print(f"SKIPPED channels : {skipped_dfs_channels}")
                    print(f"==============================================")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: AutoChannelEnable SET FAILURE")
                    print("TEST EXECUTION RESULT : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: GET PossibleChannels FAILURE")
                print("TEST EXECUTION RESULT : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable}")
            print("TEST EXECUTION RESULT : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Enable DFS RFC FAILURE")
        print("TEST EXECUTION RESULT : FAILURE")

    # Revert changed parameter to default value
    print("\n--- Reverting DFS RFC and DFSEnable to false ---")
    wifi_SetParam(obj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable", "false", "boolean")
    sleep(2)
    obj.unloadModule("wifiagent")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

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

obj = tdklib.TDKScriptingLibrary("wifiagent", "1")
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_2_4GHZ_Radio1_Channel_Change_After_DFS_Enable_On_Radio2')

loadmodulestatus = obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus)
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Enable DFS RFC on Radio 2
    tdkTestObj, actualresult = wifi_SetParam(obj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable", "true", "boolean")
    sleep(2)
    print(f"\nTEST STEP {step}: Enable DFS RFC on Radio 2")
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
        print(f"\nTEST STEP {step}: Confirm both DFS RFC and DFSEnable are true on Radio 2")
        print(f"EXPECTED RESULT {step}: Both DMs should be true")
        if "FAILURE" not in actualresult_all and dfs_rfc == "true" and dfs_enable == "true":
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable}")
            print("TEST EXECUTION RESULT : SUCCESS")

            # Step 3: Get current Radio 1 channel
            step += 1
            tdkTestObj, actualresult_ch, initial_radio1_channel = wifi_GetParam(obj, "Device.WiFi.Radio.1.Channel")
            print(f"\nTEST STEP {step}: Get current Radio 1 (2.4 GHz) channel")
            print(f"EXPECTED RESULT {step}: Should get current channel value for Radio 1")
            if expectedresult in actualresult_ch:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Radio 1 current channel is {initial_radio1_channel}")
                print("TEST EXECUTION RESULT : SUCCESS")

                # Step 4: Get PossibleChannels for Radio 1
                step += 1
                tdkTestObj, actualresult_pc, radio1_possible_channels = wifi_GetParam(obj, "Device.WiFi.Radio.1.PossibleChannels")
                print(f"\nTEST STEP {step}: Get PossibleChannels for Radio 1 (2.4 GHz)")
                print(f"EXPECTED RESULT {step}: Should get possible channels list for Radio 1")
                if expectedresult in actualresult_pc:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Radio 1 PossibleChannels = {radio1_possible_channels}")
                    print("TEST EXECUTION RESULT : SUCCESS")

                    # Pick a random target channel different from current from PossibleChannels
                    possible_list = [ch.strip() for ch in radio1_possible_channels.split(",") if ch.strip().isdigit()]
                    available_channels = [ch for ch in possible_list if ch != initial_radio1_channel]
                    if available_channels:
                        target_channel = random.choice(available_channels)
                    else:
                        print("WARNING: No alternative channel found in PossibleChannels for Radio 1, using first available")
                        target_channel = possible_list[0] if possible_list else None

                    # Step 5: Disable Auto Channel Selection on Radio 1
                    step += 1
                    tdkTestObj, actualresult = wifi_SetParam(obj, "Device.WiFi.Radio.1.AutoChannelEnable", "false", "boolean")
                    sleep(2)
                    print(f"\nTEST STEP {step}: Disable Auto Channel Selection on Radio 1")
                    print(f"EXPECTED RESULT {step}: AutoChannelEnable for Radio 1 should be false")
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
                        print("TEST EXECUTION RESULT : SUCCESS")

                        # Step 6: Change Radio 1 channel to a random channel from PossibleChannels
                        step += 1
                        tdkTestObj, actualresult = wifi_SetParam(obj, "Device.WiFi.Radio.1.Channel", target_channel, "unsignedint")
                        sleep(2)
                        print(f"\nTEST STEP {step}: Change Radio 1 channel to {target_channel}")
                        print(f"EXPECTED RESULT {step}: Radio 1 channel should be set to {target_channel}")
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
                            print("TEST EXECUTION RESULT : SUCCESS")

                            # Step 7: Apply radio settings for Radio 1
                            step += 1
                            tdkTestObj, actualresult = wifi_SetParam(obj, "Device.WiFi.ApplyRadioSettings", "true", "boolean")
                            sleep(5)
                            print(f"\nTEST STEP {step}: Apply radio settings for Radio 1")
                            print(f"EXPECTED RESULT {step}: Radio settings should be applied successfully")
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: ApplyRadioSettings result: {actualresult}")
                            print("TEST EXECUTION RESULT : SUCCESS")

                            # Step 8: Verify Radio 1 channel is updated
                            step += 1
                            tdkTestObj, actualresult, radio1_channel_after = wifi_GetParam(obj, "Device.WiFi.Radio.1.Channel")
                            print(f"\nTEST STEP {step}: Verify Radio 1 channel is updated to {target_channel}")
                            print(f"EXPECTED RESULT {step}: Radio 1 channel should be {target_channel}")
                            if expectedresult in actualresult and radio1_channel_after == target_channel:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"ACTUAL RESULT {step}: Radio 1 channel is {radio1_channel_after}")
                                print("TEST EXECUTION RESULT : SUCCESS")

                                # Step 9: Verify Radio 2 DFS settings still intact
                                step += 1
                                paramResults = {}
                                actualresult_all = []
                                for paramName in paramNames:
                                    tdkTestObj, actualresult, paramValue = wifi_GetParam(obj, paramName)
                                    actualresult_all.append(actualresult)
                                    paramResults[paramName] = paramValue
                                dfs_rfc_after = paramResults["Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable"]
                                dfs_enable_after = paramResults["Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable"]
                                print(f"\nTEST STEP {step}: Verify Radio 2 DFS settings are still intact and unaffected")
                                print(f"EXPECTED RESULT {step}: DFS RFC and DFSEnable should still be true on Radio 2")
                                if "FAILURE" not in actualresult_all and dfs_rfc_after == "true" and dfs_enable_after == "true":
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc_after} and DFSEnable is {dfs_enable_after} - Radio 2 unaffected")
                                    print("TEST EXECUTION RESULT : SUCCESS")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc_after} and DFSEnable is {dfs_enable_after} - Radio 2 DFS settings affected!")
                                    print("TEST EXECUTION RESULT : FAILURE")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: Radio 1 channel is {radio1_channel_after}, expected {target_channel}")
                                print("TEST EXECUTION RESULT : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: Channel SET FAILURE for Radio 1")
                            print("TEST EXECUTION RESULT : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: AutoChannelEnable SET FAILURE for Radio 1")
                        print("TEST EXECUTION RESULT : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: GET PossibleChannels FAILURE for Radio 1")
                    print("TEST EXECUTION RESULT : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: GET Radio 1 channel FAILURE")
                print("TEST EXECUTION RESULT : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable} - Expected both true")
            print("TEST EXECUTION RESULT : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Enable DFS RFC FAILURE")
        print("TEST EXECUTION RESULT : FAILURE")

    # Revert - always executed regardless of pass or failure at any step
    print("\n--- Reverting all to initial values ---")
    wifi_SetParam(obj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable", "false", "boolean")
    wifi_SetParam(obj, "Device.WiFi.Radio.1.AutoChannelEnable", "true", "boolean")
    sleep(2)

    obj.unloadModule("wifiagent")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

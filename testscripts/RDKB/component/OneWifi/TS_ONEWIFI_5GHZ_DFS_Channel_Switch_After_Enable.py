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

# DFS channel list to pick from randomly
DFS_CHANNELS = [52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144]

obj = tdklib.TDKScriptingLibrary("wifiagent", "1")
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_5GHZ_DFS_Channel_Switch_After_Enable')

loadmodulestatus = obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus)
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Enable DFS RFC
    tdkTestObj, actualresult = wifi_SetParam(obj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable", "true", "boolean")
    sleep(2)
    print(f"\nTEST STEP {step}: Enable Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable")
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
        print(f"\nTEST STEP {step}: Confirm both DFS RFC and DFSEnable are true")
        print(f"EXPECTED RESULT {step}: Both DMs should be true")
        if "FAILURE" not in actualresult_all and dfs_rfc == "true" and dfs_enable == "true":
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable}")
            print("TEST EXECUTION RESULT : SUCCESS")

            # Step 3: Get current channel
            step += 1
            tdkTestObj, actualresult, initial_channel = wifi_GetParam(obj, "Device.WiFi.Radio.2.Channel")
            print(f"\nTEST STEP {step}: Get current 5 GHz radio channel")
            print(f"EXPECTED RESULT {step}: Should get the current channel value")
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Current channel is {initial_channel}")
                print("TEST EXECUTION RESULT : SUCCESS")

                # Step 4: Disable Auto Channel Selection
                step += 1
                tdkTestObj, actualresult = wifi_SetParam(obj, "Device.WiFi.Radio.2.AutoChannelEnable", "false", "boolean")
                sleep(2)
                print(f"\nTEST STEP {step}: Disable Auto Channel Selection on Radio 2")
                print(f"EXPECTED RESULT {step}: AutoChannelEnable should be set to false")
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
                    print("TEST EXECUTION RESULT : SUCCESS")

                    # Step 5: Set a random DFS channel
                    step += 1
                    dfs_channel = str(random.choice(DFS_CHANNELS))
                    tdkTestObj, actualresult = wifi_SetParam(obj, "Device.WiFi.Radio.2.Channel", dfs_channel, "unsignedint")
                    sleep(2)
                    print(f"\nTEST STEP {step}: Set 5 GHz radio channel to DFS channel {dfs_channel}")
                    print(f"EXPECTED RESULT {step}: Channel should be set to {dfs_channel}")
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
                        print("TEST EXECUTION RESULT : SUCCESS")

                        # Step 6: Apply radio settings
                        step += 1
                        tdkTestObj, actualresult = wifi_SetParam(obj, "Device.WiFi.ApplyRadioSettings", "true", "boolean")
                        sleep(5)
                        print(f"\nTEST STEP {step}: Apply radio settings")
                        print(f"EXPECTED RESULT {step}: Radio settings should be applied successfully")
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
                            print("TEST EXECUTION RESULT : SUCCESS")

                            # Step 7: Verify channel is updated
                            step += 1
                            tdkTestObj, actualresult, current_channel = wifi_GetParam(obj, "Device.WiFi.Radio.2.Channel")
                            print(f"\nTEST STEP {step}: Verify 5 GHz radio channel is updated to {dfs_channel}")
                            print(f"EXPECTED RESULT {step}: Channel should be {dfs_channel}")
                            if expectedresult in actualresult and current_channel == dfs_channel:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"ACTUAL RESULT {step}: Channel is {current_channel}")
                                print("TEST EXECUTION RESULT : SUCCESS")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: Channel is {current_channel}, expected {dfs_channel}")
                                print("TEST EXECUTION RESULT : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: ApplyRadioSettings FAILURE")
                            print("TEST EXECUTION RESULT : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Channel SET FAILURE")
                        print("TEST EXECUTION RESULT : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: AutoChannelEnable SET FAILURE")
                    print("TEST EXECUTION RESULT : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: GET channel FAILURE")
                print("TEST EXECUTION RESULT : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable}")
            print("TEST EXECUTION RESULT : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Enable DFS RFC FAILURE")
        print("TEST EXECUTION RESULT : FAILURE")

    # Revert all the parameters
    print("\n--- Reverting DFS RFC to false ---")
    wifi_SetParam(obj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable", "false", "boolean")
    print("\n--- Reverting AutoChannelEnable DM to false ---")
    wifi_SetParam(obj, "Device.WiFi.Radio.2.AutoChannelEnable", "true", "boolean")
    sleep(2)
    obj.unloadModule("wifiagent")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

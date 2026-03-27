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
NON_DFS_CHANNELS = [36, 40, 44, 48, 149, 153, 157, 161, 165, 169, 173, 177]
 
obj = tdklib.TDKScriptingLibrary("wifiagent", "1") 
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_5GHZ_DFS_Channel_Revert_After_RFC_Disable')
 
loadmodulestatus = obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus)
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

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
        print(f"\nTEST STEP {step}: Disable Auto Channel Selection on Radio 2")
        print(f"EXPECTED RESULT {step}: AutoChannelEnable should be false")
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
            print("TEST EXECUTION RESULT : SUCCESS")
 
            # Step 3: Set to a DFS channel
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
 
                # Step 4: Apply radio settings
                step += 1
                tdkTestObj, actualresult = wifi_SetParam(obj, "Device.WiFi.ApplyRadioSettings", "true", "boolean")
                sleep(5)
                print(f"\nTEST STEP {step}: Apply radio settings")
                print(f"EXPECTED RESULT {step}: Radio settings should be applied")
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: ApplyRadioSettings result: {actualresult}")
                print("TEST EXECUTION RESULT : SUCCESS")
 
                # Step 5: Verify channel is set to dfs_channel
                step += 1
                tdkTestObj, actualresult, current_channel = wifi_GetParam(obj, "Device.WiFi.Radio.2.Channel")
                print(f"\nTEST STEP {step}: Verify channel is set to DFS channel {dfs_channel}")
                print(f"EXPECTED RESULT {step}: Channel should be {dfs_channel}")
                if expectedresult in actualresult and current_channel == dfs_channel:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Channel is {current_channel}")
                    print("TEST EXECUTION RESULT : SUCCESS")
 
                    # Step 6: Disable DFS RFC
                    step += 1
                    tdkTestObj, actualresult = wifi_SetParam(obj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable", "false", "boolean")
                    sleep(5)
                    print(f"\nTEST STEP {step}: Disable DFS RFC")
                    print(f"EXPECTED RESULT {step}: DFS RFC should be disabled")
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
                        print("TEST EXECUTION RESULT : SUCCESS")

                        # Step 7: Verify channel reverted to non-DFS
                        step += 1
                        tdkTestObj, actualresult, current_channel = wifi_GetParam(obj, "Device.WiFi.Radio.2.Channel")
                        print(f"\nTEST STEP {step}: Verify channel has switched back to a non-DFS channel")
                        print(f"EXPECTED RESULT {step}: Channel should NOT be in DFS range (52-144)")
                        if expectedresult in actualresult and int(current_channel) not in DFS_CHANNELS:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: Channel is {current_channel} - correctly switched to non-DFS")
                            print("TEST EXECUTION RESULT : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: Channel is {current_channel} - still on DFS channel after RFC disable")
                            print("TEST EXECUTION RESULT : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Disable DFS RFC FAILURE")
                        print("TEST EXECUTION RESULT : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Channel is {current_channel}, expected 52")
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
        print(f"ACTUAL RESULT {step}: Enable DFS RFC FAILURE")
        print("TEST EXECUTION RESULT : FAILURE")

    # Revert all the parameters to default value
    print("\n--- Reverting DFS RFC and AutoChannelEnable to default ---")
    wifi_SetParam(obj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable", "false", "boolean")
    wifi_SetParam(obj, "Device.WiFi.Radio.2.AutoChannelEnable", "true", "boolean")
    sleep(2)
    obj.unloadModule("wifiagent")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

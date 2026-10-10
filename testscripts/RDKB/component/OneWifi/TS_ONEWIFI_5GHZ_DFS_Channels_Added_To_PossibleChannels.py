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

DFS_CHANNELS = [52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144]

obj = tdklib.TDKScriptingLibrary("wifiagent", "1")
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_5GHZ_DFS_Channels_Added_To_PossibleChannels')

loadmodulestatus = obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus)

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Verify both DFS DMs are false by default
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
    print(f"\nTEST STEP {step}: Verify both DFS RFC and DFSEnable are false by default")
    print(f"EXPECTED RESULT {step}: Both DMs should be false")
    if "FAILURE" not in actualresult_all and dfs_rfc == "false" and dfs_enable == "false":
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable}")
        print("TEST EXECUTION RESULT : SUCCESS")

        # Step 2: Get PossibleChannels before enabling DFS - verify no DFS channels
        step += 1
        tdkTestObj, actualresult, possible_channels_before = wifi_GetParam(obj, "Device.WiFi.Radio.2.PossibleChannels")
        print(f"\nTEST STEP {step}: Get PossibleChannels before enabling DFS RFC")
        print(f"EXPECTED RESULT {step}: Only non-DFS channels should be listed (no 52-144 range)")
        channels_before_list = [int(ch.strip()) for ch in possible_channels_before.split(",") if ch.strip().isdigit()]
        dfs_found_before = [ch for ch in DFS_CHANNELS if ch in channels_before_list]
        if expectedresult in actualresult and len(dfs_found_before) == 0:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: PossibleChannels = {possible_channels_before}")
            print(f"No DFS channels found in PossibleChannels (as expected)")
            print("TEST EXECUTION RESULT : SUCCESS")

            # Step 3: Enable DFS RFC
            step += 1
            tdkTestObj, actualresult = wifi_SetParam(obj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable", "true", "boolean")
            sleep(2)
            print(f"\nTEST STEP {step}: Enable DFS RFC")
            print(f"EXPECTED RESULT {step}: DFS RFC should be enabled successfully")
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
                print("TEST EXECUTION RESULT : SUCCESS")

                # Step 4: Confirm both DFS DMs are true
                step += 1
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

                    # Step 5: Get PossibleChannels after enabling DFS - verify DFS channels added
                    step += 1
                    tdkTestObj, actualresult, possible_channels_after = wifi_GetParam(obj, "Device.WiFi.Radio.2.PossibleChannels")
                    channels_after_list = [int(ch.strip()) for ch in possible_channels_after.split(",") if ch.strip().isdigit()]
                    dfs_found_after = [ch for ch in DFS_CHANNELS if ch in channels_after_list]
                    missing_dfs = [ch for ch in DFS_CHANNELS if ch not in channels_after_list]
                    print(f"\nTEST STEP {step}: Get PossibleChannels after enabling DFS RFC and verify all DFS channels added")
                    print(f"EXPECTED RESULT {step}: All DFS channels (52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144) should be in PossibleChannels")
                    if expectedresult in actualresult and len(dfs_found_after) == len(DFS_CHANNELS):
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: PossibleChannels = {possible_channels_after}")
                        print(f"All {len(dfs_found_after)} DFS channels found in PossibleChannels")
                        print("TEST EXECUTION RESULT : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: PossibleChannels = {possible_channels_after}")
                        print(f"Missing DFS channels: {missing_dfs}")
                        print("TEST EXECUTION RESULT : FAILURE")

                    # Revert the DFS RFC parameter to default value
                    print("\n--- Reverting DFS RFC to false ---")
                    wifi_SetParam(obj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable", "false", "boolean")
                    sleep(2)
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable}")
                    print("TEST EXECUTION RESULT : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Enable DFS RFC FAILURE")
                print("TEST EXECUTION RESULT : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: PossibleChannels = {possible_channels_before}")
            print(f"DFS channels found before enabling RFC: {dfs_found_before}")
            print("TEST EXECUTION RESULT : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable} - Expected both false")
        print("TEST EXECUTION RESULT : FAILURE")

    obj.unloadModule("wifiagent")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

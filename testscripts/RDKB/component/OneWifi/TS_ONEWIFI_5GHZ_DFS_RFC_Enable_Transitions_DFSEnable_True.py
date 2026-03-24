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

obj = tdklib.TDKScriptingLibrary("wifiagent", "1")
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_5GHZ_DFS_RFC_Enable_Transitions_DFSEnable_True')

loadmodulestatus = obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus)
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Get initial values of both DFS DMs
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
    print(f"TEST STEP {step}: Get initial values of DFS RFC and DFSEnable DMs")
    print(f"EXPECTED RESULT {step}: Both DMs should be false by default")
    if "FAILURE" not in actualresult_all and dfs_rfc == "false" and dfs_enable == "false":
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable}")
        print("TEST EXECUTION RESULT : SUCCESS")

        # Step 2: Enable DFS RFC
        step += 1
        tdkTestObj, actualresult = wifi_SetParam(obj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable", "true", "boolean")
        sleep(2)
        print(f"TEST STEP {step}: Enable Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable")
        print(f"EXPECTED RESULT {step}: DFS RFC should be set to true successfully")
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
            print("TEST EXECUTION RESULT : SUCCESS")

            # Step 3: Verify both DMs are now true
            step += 1
            paramResults = {}
            actualresult_all = []
            for paramName in paramNames:
                tdkTestObj, actualresult, paramValue = wifi_GetParam(obj, paramName)
                actualresult_all.append(actualresult)
                paramResults[paramName] = paramValue
            dfs_rfc = paramResults["Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable"]
            dfs_enable = paramResults["Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable"]
            print(f"TEST STEP {step}: Verify both DFS RFC and DFSEnable are now true")
            print(f"EXPECTED RESULT {step}: Both DMs should be true after enabling DFS RFC")
            if "FAILURE" not in actualresult_all and dfs_rfc == "true" and dfs_enable == "true":
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable}")
                print("TEST EXECUTION RESULT : SUCCESS")

                # Step 4: Revert DFS RFC to false
                step += 1
                tdkTestObj, actualresult = wifi_SetParam(obj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable", "false", "boolean")
                sleep(2)
                print(f"TEST STEP {step}: Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable to false")
                print(f"EXPECTED RESULT {step}: DFS RFC should be reverted to false successfully")
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: SET operation SUCCESS")
                    print("TEST EXECUTION RESULT : SUCCESS")

                    # Step 5: Confirm revert
                    step += 1
                    paramResults = {}
                    actualresult_all = []
                    for paramName in paramNames:
                        tdkTestObj, actualresult, paramValue = wifi_GetParam(obj, paramName)
                        actualresult_all.append(actualresult)
                        paramResults[paramName] = paramValue
                    dfs_rfc = paramResults["Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable"]
                    dfs_enable = paramResults["Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable"]
                    print(f"TEST STEP {step}: Confirm both DMs are reverted to false")
                    print(f"EXPECTED RESULT {step}: Both DMs should be false after revert")
                    if "FAILURE" not in actualresult_all and dfs_rfc == "false" and dfs_enable == "false":
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable}")
                        print("TEST EXECUTION RESULT : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable}")
                        print("TEST EXECUTION RESULT : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Revert SET operation FAILURE")
                    print("TEST EXECUTION RESULT : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable} - Expected both true")
                print("TEST EXECUTION RESULT : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: SET operation FAILURE")
            print("TEST EXECUTION RESULT : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable} - Expected both false by default")
        print("TEST EXECUTION RESULT : FAILURE")
    obj.unloadModule("wifiagent")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

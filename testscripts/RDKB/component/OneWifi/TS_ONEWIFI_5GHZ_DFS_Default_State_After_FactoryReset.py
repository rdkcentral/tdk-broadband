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
obj.configureTestCase(ip,port,'TS_ONEWIFI_5GHZ_DFS_Default_State_After_FactoryReset')

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
        print(f"TEST STEP {step}: Confirm both DFS DMs are true before Factory Reset")
        print(f"EXPECTED RESULT {step}: Both DMs should be true")
        if "FAILURE" not in actualresult_all and dfs_rfc == "true" and dfs_enable == "true":
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable}")
            print("TEST EXECUTION RESULT : SUCCESS")

            # Step 3: Perform Factory Reset
            step += 1
            obj.saveCurrentState()
            tdkTestObj, actualresult = wifi_SetParam(obj, "Device.X_CISCO_COM_DeviceControl.FactoryReset", "Router,Wifi,VoIP,Dect,MoCA", "string")
            print(f"TEST STEP {step}: Perform Factory Reset")
            print(f"EXPECTED RESULT {step}: Factory Reset should be initiated successfully")
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Factory Reset initiated successfully")
                print("TEST EXECUTION RESULT : SUCCESS")
                obj.restorePreviousStateAfterReboot()
                sleep(300)

                # Step 4: Verify both DMs are false after Factory Reset
                step += 1
                paramResults = {}
                actualresult_all = []
                for paramName in paramNames:
                    tdkTestObj, actualresult, paramValue = wifi_GetParam(obj, paramName)
                    actualresult_all.append(actualresult)
                    paramResults[paramName] = paramValue
                dfs_rfc = paramResults["Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DFS.Enable"]
                dfs_enable = paramResults["Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable"]
                print(f"TEST STEP {step}: Verify both DMS are false after Factory Reset")
                print(f"EXPECTED RESULT {step}: Both DMs should be false confirming default state restored")
                if "FAILURE" not in actualresult_all and dfs_rfc == "false" and dfs_enable == "false":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable}")
                    print("TEST EXECUTION RESULT : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable} - Expected both false")
                    print("TEST EXECUTION RESULT : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Factory Reset FAILURE")
                print("TEST EXECUTION RESULT : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: DFS RFC is {dfs_rfc} and DFSEnable is {dfs_enable} - Expected both true")
            print("TEST EXECUTION RESULT : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Enable DFS RFC FAILURE")
        print("TEST EXECUTION RESULT : FAILURE")

    obj.unloadModule("wifiagent")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

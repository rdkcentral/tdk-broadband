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
import tdkbVariables

obj = tdklib.TDKScriptingLibrary("sysutil", "1")
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckMLDBridgeStatus')

loadmodulestatus = obj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Get MLD interface bridge and state info
    tdkTestObj = obj.createTestStep('ExecuteCmd')
    tdkTestObj.addParameter("command", "sh %s/tdk_platform_utility.sh getMLDInterfaceStatus" % tdkbVariables.TDK_PATH)
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    bridgeOutput = tdkTestObj.getResultDetails().strip().replace("\\n", "").strip()

    print("\nTEST STEP %d: Get MLD Interface bridge and state info" % step)
    print("EXPECTED RESULT %d: Should retrieve bridge and state info for MLD Interface" % step)
    if expectedresult in actualresult and bridgeOutput:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: MLD Interface bridge and state info retrieved: %s" % (step, bridgeOutput))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        # Step 2: Check if MLD interface is mastered to brlan0
        step += 1
        print("\nTEST STEP %d: Check if MLD Interface is added to brlan0 bridge" % step)
        print("EXPECTED RESULT %d: 'master brlan0' should be present in MLD Interface output" % step)
        if "master brlan0" in bridgeOutput:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: MLD Interface is mastered to brlan0 bridge" % step)
            print("[TEST EXECUTION RESULT] : SUCCESS")

            # Step 3: Check state is UP
            step += 1
            print("\nTEST STEP %d: Check if MLD Interface state is UP" % step)
            print("EXPECTED RESULT %d: 'state UP' should be present in MLD Interface output" % step)
            if "state UP" in bridgeOutput:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: MLD Interface state is UP" % step)
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: MLD Interface state is NOT UP" % step)
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: MLD Interface is NOT mastered to brlan0 bridge" % step)
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get MLD Interface bridge and state info" % step)
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("sysutil")
else:
    print("Failed to load sysutil module")
    obj.setLoadModuleStatus("FAILURE")

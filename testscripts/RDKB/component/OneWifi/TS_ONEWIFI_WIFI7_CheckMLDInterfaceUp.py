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

obj = tdklib.TDKScriptingLibrary("sysutil","1")
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckMLDInterfaceUp')

loadmodulestatus = obj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"

    # Step 1: Get MLD interface status
    tdkTestObj = obj.createTestStep('ExecuteCmd')
    tdkTestObj.addParameter("command", "sh %stdk_platform_utility.sh getMLDInterfaceStatus" % tdkbVariables.TDK_PATH)
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    ipLinkOutput = tdkTestObj.getResultDetails().strip().replace("\\n", "").strip()

    print("\nTEST STEP 1: Get MLD Interface status")
    print("EXPECTED RESULT 1: Should retrieve MLD Interface status")
    if expectedresult in actualresult and ipLinkOutput:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT 1: MLD Interface status retrieved: %s" % ipLinkOutput)
        print("[TEST EXECUTION RESULT] : SUCCESS")

        # Step 2: Check if UP,LOWER_UP flags are present to confirm operational status
        print("\nTEST STEP 2: Check if MLD Interface is operationally UP")
        print("EXPECTED RESULT 2: 'UP,LOWER_UP' flags should be present in MLD Interface status")
        if "UP,LOWER_UP" in ipLinkOutput:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT 2: UP,LOWER_UP flags found - MLD Interface is operationally UP")
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT 2: UP,LOWER_UP flags NOT found in MLD Interface status")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT 1: Failed to get MLD Interface status")
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("sysutil")
else:
    print("Failed to load sysutil module")
    obj.setLoadModuleStatus("FAILURE")

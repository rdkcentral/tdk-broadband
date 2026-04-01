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
obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckMLDMACAddress')

loadmodulestatus = obj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Get MLD Interface hardware address
    tdkTestObj = obj.createTestStep('ExecuteCmd')
    tdkTestObj.addParameter("command", "sh %s/tdk_platform_utility.sh getMLDIfconfigHWAddr" % tdkbVariables.TDK_PATH)
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    mldHWAddr = tdkTestObj.getResultDetails().strip().replace("\\n", "").strip()

    print("\nTEST STEP %d: Get the hardware address of MLD Interface" % step)
    print("EXPECTED RESULT %d: Should retrieve hardware address of MLD Interface" % step)
    if expectedresult in actualresult and mldHWAddr:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: MLD Interface hardware address: %s" % (step, mldHWAddr))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        # Step 2: Get MLD addr from wireless interface info
        step += 1
        tdkTestObj = obj.createTestStep('ExecuteCmd')
        tdkTestObj.addParameter("command", "sh %s/tdk_platform_utility.sh getMLDIwAddr" % tdkbVariables.TDK_PATH)
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        mldWirelessAddr = tdkTestObj.getResultDetails().strip().replace("\\n", "").strip()

        print("\nTEST STEP %d: Get MLD Interface addr from wireless interface info" % step)
        print("EXPECTED RESULT %d: Should retrieve addr from MLD Interface wireless info" % step)
        if expectedresult in actualresult and mldWirelessAddr:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: MLD Interface wireless addr: %s" % (step, mldWirelessAddr))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            # Step 3: Validate both MACs match (case-insensitive)
            step += 1
            print("\nTEST STEP %d: Validate MLD Interface hardware address matches wireless interface addr" % step)
            print("EXPECTED RESULT %d: Both MAC addresses should match" % step)
            if mldHWAddr.upper() == mldWirelessAddr.upper():
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: MAC addresses match - hardware address: %s, wireless addr: %s" % (step, mldHWAddr, mldWirelessAddr))
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: MAC addresses DO NOT match - hardware address: %s, wireless addr: %s" % (step, mldHWAddr, mldWirelessAddr))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get wireless addr for MLD Interface" % step)
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get hardware address of MLD Interface" % step)
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("sysutil")
else:
    print("Failed to load sysutil module")
    obj.setLoadModuleStatus("FAILURE")

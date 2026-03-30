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
obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckMLDSSID')

loadmodulestatus = obj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"

    step = 1
    # Step 1: Get SSID from iw mld0 info
    tdkTestObj = obj.createTestStep('ExecuteCmd')
    tdkTestObj.addParameter("command", "sh %s/tdk_platform_utility.sh getMLDSSID" % tdkbVariables.TDK_PATH)
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    ssidOutput = tdkTestObj.getResultDetails().strip().replace("\\n", "").strip()
    print("\nTEST STEP %d: Get SSID configured on mld0 interface" % step)
    print("EXPECTED RESULT %d: A valid SSID should be configured on mld0" % step)
    if expectedresult in actualresult and ssidOutput:
        tdkTestObj.setResultStatus("SUCCESS")
        # Extract SSID value
        ssidValue = ssidOutput.replace("ssid", "").strip()
        print("ACTUAL RESULT %d: SSID configured on mld0 interface: %s" % (step, ssidValue))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        # Step 2: Get mld0 HWaddr to extract last 6 digits of MAC
        step += 1
        tdkTestObj = obj.createTestStep('ExecuteCmd')
        tdkTestObj.addParameter("command", "sh %s/tdk_platform_utility.sh getCMMACAddress" % tdkbVariables.TDK_PATH)
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        mldHWAddr = tdkTestObj.getResultDetails().strip().replace("\\n", "").strip()
        print("\nTEST STEP %d: Get mld0 HWaddr to derive expected SSID suffix" % step)
        print("EXPECTED RESULT %d: Should retrieve HWaddr from ifconfig mld0" % step)
        if expectedresult in actualresult and mldHWAddr:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: mld0 HWaddr: %s" % (step, mldHWAddr))
            print("[TEST EXECUTION RESULT] : SUCCESS")
            # Derive last 6 hex digits from MAC (last 3 octets without colons)
            macParts = mldHWAddr.replace("-", ":").split(":")
            last6Digits = "".join(macParts[-3:]).lower()
            expectedSSID = "BPI-RDKB-MLO-AP-%s" % last6Digits

            # Step 3: Validate SSID format matches BPI-RDKB-MLO-AP-<last6ofMAC>
            step += 1
            print("\nTEST STEP %d: Validate SSID format is BPI-RDKB-MLO-AP-<last 6 digits of MAC>" % step)
            print("EXPECTED RESULT %d: SSID should be %s" % (step, expectedSSID))
            if ssidValue.lower() == expectedSSID.lower():
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: SSID matches expected format - %s" % (step, ssidValue))
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: SSID does NOT match expected format - %s" % (step, ssidValue))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get HWaddr from ifconfig mld0" % step)
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get SSID from iw mld0 info" % step)
        print("[TEST EXECUTION RESULT] : FAILURE")
    obj.unloadModule("sysutil")
else:
    print("Failed to load sysutil module")
    obj.setLoadModuleStatus("FAILURE")

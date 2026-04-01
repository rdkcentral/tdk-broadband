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
from tdkutility import *

obj = tdklib.TDKScriptingLibrary("sysutil", "1")
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181", "1")

ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckMLDSSID')
tr181obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckMLDSSID')

loadmodulestatus = obj.getLoadModuleResult()
tr181loadstatus = tr181obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in tr181loadstatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    tr181obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Get SSID from MLD Interface wireless info
    tdkTestObj = obj.createTestStep('ExecuteCmd')
    tdkTestObj.addParameter("command", "sh %s/tdk_platform_utility.sh getMLDSSID" % tdkbVariables.TDK_PATH)
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    ssidOutput = tdkTestObj.getResultDetails().strip().replace("\\n", "").strip()

    print("\nTEST STEP %d: Get SSID configured on MLD Interface" % step)
    print("EXPECTED RESULT %d: A valid non-empty SSID should be configured on MLD Interface" % step)
    if expectedresult in actualresult and ssidOutput:
        tdkTestObj.setResultStatus("SUCCESS")
        # Extract SSID value
        ssidValue = ssidOutput.replace("ssid", "").strip()
        print("ACTUAL RESULT %d: SSID configured on MLD Interface: %s" % (step, ssidValue))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        # Step 2: Get configured SSID from Device.WiFi.SSID.1.SSID via TR-181
        step += 1
        tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get')
        actualresult, tr181SSID = getTR181Value(tdkTestObj_Tr181_Get, "Device.WiFi.SSID.1.SSID")
        tr181SSID = tr181SSID.strip().strip('\\n').strip()

        print("\nTEST STEP %d: Get configured SSID from Device.WiFi.SSID.1.SSID" % step)
        print("EXPECTED RESULT %d: Should retrieve Device.WiFi.SSID.1.SSID" % step)
        if expectedresult in actualresult and tr181SSID:
            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Device.WiFi.SSID.1.SSID: %s" % (step, tr181SSID))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            # Step 3: Validate SSID from MLD Interface matches Device.WiFi.SSID.1.SSID
            step += 1
            print("\nTEST STEP %d: Validate MLD Interface SSID matches Device.WiFi.SSID.1.SSID" % step)
            print("EXPECTED RESULT %d: MLD Interface SSID should match Device.WiFi.SSID.1.SSID" % step)
            if ssidValue == tr181SSID:
                tdkTestObj_Tr181_Get.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: SSID matches - MLD Interface: %s, Device.WiFi.SSID.1.SSID: %s" % (step, ssidValue, tr181SSID))
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj_Tr181_Get.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: SSID MISMATCH - MLD Interface: %s, Device.WiFi.SSID.1.SSID: %s" % (step, ssidValue, tr181SSID))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj_Tr181_Get.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get Device.WiFi.SSID.1.SSID" % step)
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get SSID from MLD Interface" % step)
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("sysutil")
    tr181obj.unloadModule("tdkbtr181")
else:
    print("Failed to load sysutil or tdkbtr181 module")
    obj.setLoadModuleStatus("FAILURE")
    tr181obj.setLoadModuleStatus("FAILURE")

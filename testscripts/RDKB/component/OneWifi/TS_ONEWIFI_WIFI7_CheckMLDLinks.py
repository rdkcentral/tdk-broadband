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
obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckMLDLinks')
tr181obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckMLDLinks')

loadmodulestatus = obj.getLoadModuleResult()
tr181loadstatus = tr181obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in tr181loadstatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    tr181obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Get number of radios via tr181 object
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get')
    actualresult, radioCountOutput = getTR181Value(tdkTestObj_Tr181_Get, "Device.WiFi.RadioNumberOfEntries")
    radioCountOutput = radioCountOutput.strip()

    print("\nTEST STEP %d: Get number of WiFi radios from Device.WiFi.RadioNumberOfEntries" % step)
    print("EXPECTED RESULT %d: Should retrieve Device.WiFi.RadioNumberOfEntries" % step)
    if expectedresult in actualresult and radioCountOutput:
        if not radioCountOutput.isdigit():
            tdkTestObj_Tr181_Get.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Invalid value for RadioNumberOfEntries: %s" % (step, radioCountOutput))
            print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            radioCount = int(radioCountOutput)
            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: RadioNumberOfEntries = %s" % (step, radioCountOutput))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            # Steps 2 to N+1: Check each link ID is present in MLD Interface info via sysutil
            allLinksPresent = True
            for linkId in range(radioCount):
                step += 1
                tdkTestObj = obj.createTestStep('ExecuteCmd')
                tdkTestObj.addParameter("command", "sh %s/tdk_platform_utility.sh getMLDLinkInfo x x %d" % (tdkbVariables.TDK_PATH, linkId))
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                linkOutput = tdkTestObj.getResultDetails().strip().replace("\\n", "").strip()

                print("\nTEST STEP %d: Check MLD link ID %d is present in MLD Interface info" % (step, linkId))
                print("EXPECTED RESULT %d: link ID %d should be present in MLD Interface info" % (step, linkId))
                if expectedresult in actualresult and linkOutput != "":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: link ID %d found: %s" % (step, linkId, linkOutput))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: link ID %d NOT found in MLD Interface info" % (step, linkId))
                    print("[TEST EXECUTION RESULT] : FAILURE")
                    allLinksPresent = False

            if not allLinksPresent:
                print("\nOne or more MLD links are missing - check MLD Interface info output")
    else:
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get RadioNumberOfEntries" % step)
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("sysutil")
    tr181obj.unloadModule("tdkbtr181")
else:
    print("Failed to load sysutil or tdkbtr181 module")
    obj.setLoadModuleStatus("FAILURE")
    tr181obj.setLoadModuleStatus("FAILURE")

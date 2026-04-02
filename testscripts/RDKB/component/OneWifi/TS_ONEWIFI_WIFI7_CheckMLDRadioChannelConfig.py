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
import re
from tdkutility import *

obj = tdklib.TDKScriptingLibrary("sysutil", "1")
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181", "1")

ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckMLDRadioChannelConfig')
tr181obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckMLDRadioChannelConfig')

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

            for radioIdx in range(radioCount):
                linkId = radioIdx
                radioIndex = radioIdx + 1

                # Step: Get channel for this radio from TR-181
                step += 1
                tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get')
                actualresult, tr181Channel = getTR181Value(tdkTestObj_Tr181_Get, "Device.WiFi.Radio.%d.Channel" % radioIndex)
                tr181Channel = tr181Channel.strip()

                print("\nTEST STEP %d: Get channel for Radio %d from Device.WiFi.Radio.%d.Channel" % (step, radioIndex, radioIndex))
                print("EXPECTED RESULT %d: Should retrieve Device.WiFi.Radio.%d.Channel" % (step, radioIndex))
                if expectedresult in actualresult and tr181Channel:
                    tdkTestObj_Tr181_Get.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Device.WiFi.Radio.%d.Channel: %s" % (step, radioIndex, tr181Channel))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    # Step: Get channel for this link from MLD Interface info via sysutil
                    step += 1
                    tdkTestObj = obj.createTestStep('ExecuteCmd')
                    tdkTestObj.addParameter("command", "sh %s/tdk_platform_utility.sh getMLDLinkChannel x x %d" % (tdkbVariables.TDK_PATH, linkId))
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    mldLinkChannelRaw = tdkTestObj.getResultDetails().strip().replace("\\n", "").strip()
                    match = re.search(r'\b(\d+)\b', mldLinkChannelRaw)
                    mldLinkChannel = match.group(1) if match else ""

                    print("\nTEST STEP %d: Get channel for MLD link ID %d from MLD Interface info" % (step, linkId))
                    print("EXPECTED RESULT %d: Should retrieve channel for MLD link ID %d" % (step, linkId))
                    if expectedresult in actualresult and mldLinkChannel:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Channel for MLD link ID %d: %s" % (step, linkId, mldLinkChannel))
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        # Step: Compare TR-181 channel with MLD Interface info channel
                        step += 1
                        print("\nTEST STEP %d: Validate Device.WiFi.Radio.%d.Channel matches MLD link ID %d channel" % (step, radioIndex, linkId))
                        print("EXPECTED RESULT %d: Device.WiFi.Radio.%d.Channel and MLD link ID %d channel should match" % (step, radioIndex, linkId))
                        if tr181Channel == mldLinkChannel:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: Channel match for Radio %d - TR-181: %s, MLD Interface info: %s" % (step, radioIndex, tr181Channel, mldLinkChannel))
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Channel MISMATCH for Radio %d - TR-181: %s, MLD Interface info: %s" % (step, radioIndex, tr181Channel, mldLinkChannel))
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Failed to get channel for MLD link ID %d" % (step, linkId))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj_Tr181_Get.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to get Device.WiFi.Radio.%d.Channel" % (step, radioIndex))
                    print("[TEST EXECUTION RESULT] : FAILURE")
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

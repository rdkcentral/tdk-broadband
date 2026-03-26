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
    tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
    tdkTestObj.addParameter("ParamName", "Device.WiFi.RadioNumberOfEntries")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    radioCountOutput = tdkTestObj.getResultDetails().strip()

    print("\nTEST STEP %d: Get number of WiFi radios from Device.WiFi.RadioNumberOfEntries" % step)
    print("EXPECTED RESULT %d: Should retrieve Device.WiFi.RadioNumberOfEntries" % step)
    if expectedresult in actualresult and radioCountOutput:
        try:
            radioCount = int(radioCountOutput)
        except ValueError:
            radioCount = 0

        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: RadioNumberOfEntries = %s" % (step, radioCountOutput))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        for radioIdx in range(radioCount):
            linkId = radioIdx
            dmcliIndex = radioIdx + 1

            # Step: Get channel for this radio from tr181 get
            step += 1
            tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
            tdkTestObj.addParameter("ParamName", "Device.WiFi.Radio.%d.Channel" % dmcliIndex)
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            dmcliChannel = tdkTestObj.getResultDetails().strip()

            print("\nTEST STEP %d: Get channel for Radio %d from Device.WiFi.Radio.%d.Channel" % (step, dmcliIndex, dmcliIndex))
            print("EXPECTED RESULT %d: Should retrieve Device.WiFi.Radio.%d.Channel" % (step, dmcliIndex))
            if expectedresult in actualresult and dmcliChannel:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Channel for Radio %d: %s" % (step, dmcliIndex, dmcliChannel))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                # Step: Get channel for this link from iw mld0 info via sysutil
                step += 1
                tdkTestObj = obj.createTestStep('ExecuteCmd')
                tdkTestObj.addParameter("command", "sh %s/tdk_platform_utility.sh getMLDLinkChannel x x %d" % (tdkbVariables.TDK_PATH, linkId))
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                iwChannelRaw = tdkTestObj.getResultDetails().strip().replace("\\n", "").strip()
                match = re.search(r'\b(\d+)\b', iwChannelRaw)
                iwChannel = match.group(1) if match else ""

                print("\nTEST STEP %d: Get channel for MLD link ID %d from iw mld0 info" % (step, linkId))
                print("EXPECTED RESULT %d: Should retrieve channel for link ID %d" % (step, linkId))
                if expectedresult in actualresult and iwChannel:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: iw channel for link ID %d: %s" % (step, linkId, iwChannel))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    # Step: Compare channels
                    step += 1
                    print("\nTEST STEP %d: Validate dmcli channel matches iw channel for Radio %d / link ID %d" % (step, dmcliIndex, linkId))
                    print("EXPECTED RESULT %d: Device.WiFi.Radio.%d.Channel and iw channel should match" % (step, dmcliIndex))
                    if dmcliChannel == iwChannel:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Channel match for Radio %d - dmcli: %s, iw: %s" % (step, dmcliIndex, dmcliChannel, iwChannel))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Channel MISMATCH for Radio %d - dmcli: %s, iw: %s" % (step, dmcliIndex, dmcliChannel, iwChannel))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to get iw channel for link ID %d" % (step, linkId))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to get channel for Radio %d" % (step, dmcliIndex))
                print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get RadioNumberOfEntries" % step)
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("sysutil")
    tr181obj.unloadModule("tdkbtr181")
else:
    print("Failed to load sysutil or tdkbtr181 module")
    obj.setLoadModuleStatus("FAILURE")
    tr181obj.setLoadModuleStatus("FAILURE")

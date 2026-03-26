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
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181", "1")

ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckMLDLinkMACs')
tr181obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckMLDLinkMACs')

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

            # Step: Get link addr from iw mld0 info for this link ID
            step += 1
            tdkTestObj = obj.createTestStep('ExecuteCmd')
            tdkTestObj.addParameter("command",
                "sh %s/tdk_platform_utility.sh getMLDLinkAddr x x %d" % (tdkbVariables.TDK_PATH, linkId))
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            iwLinkAddr = tdkTestObj.getResultDetails().strip().replace("\\n", "").strip()

            print("\nTEST STEP %d: Get link addr for MLD link ID %d from iw mld0 info" % (step, linkId))
            print("EXPECTED RESULT %d: Should retrieve link addr for link ID %d" % (step, linkId))

            if expectedresult in actualresult and iwLinkAddr:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: iw link addr for link ID %d: %s" % (step, linkId, iwLinkAddr))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                # Step: Get HWaddr from ifconfig wifiX
                step += 1
                radioIf = "%s%d" % ("wifi", radioIdx)
                tdkTestObj = obj.createTestStep('ExecuteCmd')
                tdkTestObj.addParameter("command",
                    "sh %s/tdk_platform_utility.sh getRadioIfHWAddr x x %s" % (tdkbVariables.TDK_PATH, radioIf))
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                ifconfigAddr = tdkTestObj.getResultDetails().strip().replace("\\n", "").strip()

                print("\nTEST STEP %d: Get HWaddr of %s from ifconfig" % (step, radioIf))
                print("EXPECTED RESULT %d: Should retrieve HWaddr from ifconfig %s" % (step, radioIf))

                if expectedresult in actualresult and ifconfigAddr:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: ifconfig HWaddr for %s: %s" % (step, radioIf, ifconfigAddr))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    # Step: Compare link addr with ifconfig HWaddr
                    step += 1
                    print("\nTEST STEP %d: Validate MLD link ID %d addr matches %s HWaddr" % (step, linkId, radioIf))
                    print("EXPECTED RESULT %d: iw link addr and ifconfig HWaddr should match for link ID %d" % (step, linkId))

                    if iwLinkAddr.upper() == ifconfigAddr.upper():
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: MAC match for link ID %d - iw: %s, ifconfig: %s" % (step, linkId, iwLinkAddr, ifconfigAddr))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: MAC MISMATCH for link ID %d - iw: %s, ifconfig: %s" % (step, linkId, iwLinkAddr, ifconfigAddr))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to get HWaddr for %s" % (step, radioIf))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to get link addr for link ID %d" % (step, linkId))
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

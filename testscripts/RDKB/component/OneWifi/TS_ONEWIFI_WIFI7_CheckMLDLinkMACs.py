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

            # Step 2 onwards: Get per-band radio interface names from platform properties
            radioIfKeys = ["RADIO_IF_2G", "RADIO_IF_5G", "RADIO_IF_6G"]
            radioIfList = []
            allIfFetched = True

            for radioIfKey in radioIfKeys[:radioCount]:
                step += 1
                tdkTestObj = obj.createTestStep('ExecuteCmd')
                tdkTestObj.addParameter("command", "sh %s/tdk_utility.sh parseConfigFile %s" % (tdkbVariables.TDK_PATH, radioIfKey))
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                radioIfVal = tdkTestObj.getResultDetails().strip().strip('\\n').strip()

                print("\nTEST STEP %d: Get radio interface name for %s from platform properties" % (step, radioIfKey))
                print("EXPECTED RESULT %d: Should retrieve %s from platform properties" % (step, radioIfKey))
                if expectedresult in actualresult and radioIfVal:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: %s: %s" % (step, radioIfKey, radioIfVal))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                    radioIfList.append(radioIfVal)
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to get %s from platform properties" % (step, radioIfKey))
                    print("[TEST EXECUTION RESULT] : FAILURE")
                    allIfFetched = False
                    break

            if allIfFetched:
                for radioIdx in range(radioCount):
                    linkId = radioIdx
                    radioIf = radioIfList[radioIdx]

                    # Step: Get link addr from MLD Interface info for this link ID
                    step += 1
                    tdkTestObj = obj.createTestStep('ExecuteCmd')
                    tdkTestObj.addParameter("command",
                        "sh %s/tdk_platform_utility.sh getMLDLinkAddr x x %d" % (tdkbVariables.TDK_PATH, linkId))
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    mldLinkAddr = tdkTestObj.getResultDetails().strip().replace("\\n", "").strip()

                    print("\nTEST STEP %d: Get link addr for MLD link ID %d" % (step, linkId))
                    print("EXPECTED RESULT %d: Should retrieve link addr for MLD link ID %d" % (step, linkId))

                    if expectedresult in actualresult and mldLinkAddr:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Link addr for MLD link ID %d: %s" % (step, linkId, mldLinkAddr))
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        # Step: Get HWaddr of radio interface from platform properties
                        step += 1
                        tdkTestObj = obj.createTestStep('ExecuteCmd')
                        tdkTestObj.addParameter("command",
                            "sh %s/tdk_platform_utility.sh getRadioIfHWAddr x x %s" % (tdkbVariables.TDK_PATH, radioIf))
                        tdkTestObj.executeTestCase(expectedresult)
                        actualresult = tdkTestObj.getResult()
                        radioIfHWAddr = tdkTestObj.getResultDetails().strip().replace("\\n", "").strip()

                        print("\nTEST STEP %d: Get hardware address of radio interface %s" % (step, radioIf))
                        print("EXPECTED RESULT %d: Should retrieve hardware address for radio interface %s" % (step, radioIf))

                        if expectedresult in actualresult and radioIfHWAddr:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: Hardware address for radio interface %s: %s" % (step, radioIf, radioIfHWAddr))
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                            # Step: Compare link addr with radio interface HWaddr
                            step += 1
                            print("\nTEST STEP %d: Validate MLD link ID %d addr matches radio interface %s hardware address" % (step, linkId, radioIf))
                            print("EXPECTED RESULT %d: MLD link addr and radio interface hardware address should match for link ID %d" % (step, linkId))

                            if mldLinkAddr.upper() == radioIfHWAddr.upper():
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: MAC match for MLD link ID %d - link addr: %s, radio interface %s hardware address: %s" % (step, linkId, mldLinkAddr, radioIf, radioIfHWAddr))
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: MAC MISMATCH for MLD link ID %d - link addr: %s, radio interface %s hardware address: %s" % (step, linkId, mldLinkAddr, radioIf, radioIfHWAddr))
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Failed to get hardware address for radio interface %s" % (step, radioIf))
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Failed to get link addr for MLD link ID %d" % (step, linkId))
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

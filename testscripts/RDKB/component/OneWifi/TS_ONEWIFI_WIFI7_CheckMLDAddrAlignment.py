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
obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckMLDAddrAlignment')
tr181obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckMLDAddrAlignment')

loadmodulestatus = obj.getLoadModuleResult()
tr181loadstatus = tr181obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in tr181loadstatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    tr181obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Get MLD Interface Hardware address
    tdkTestObj = obj.createTestStep('ExecuteCmd')
    tdkTestObj.addParameter("command", "sh %s/tdk_platform_utility.sh getMLDIfconfigHWAddr" % tdkbVariables.TDK_PATH)
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    mldHWAddr = tdkTestObj.getResultDetails().strip().strip('\\n').strip()

    print("\nTEST STEP %d: Get the hardware address of MLD Interface" % step)
    print("EXPECTED RESULT %d: Should retrieve hardware address from MLD Interface" % step)
    if expectedresult in actualresult and mldHWAddr:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: MLD Interface hardware adress: %s" % (step, mldHWAddr))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        # Step 2: Get RadioNumberOfEntries via tr181 object
        step += 1
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

                # Step 3: Get MLD AP index list from platform utility via sysutil
                step += 1
                tdkTestObj = obj.createTestStep('ExecuteCmd')
                tdkTestObj.addParameter("command", "sh %s/tdk_utility.sh parseConfigFile MLD_AP_INDICES" % tdkbVariables.TDK_PATH)
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                apIndexOutput = tdkTestObj.getResultDetails().strip()

                print("\nTEST STEP %d: Get Private AccessPoint indices from platform properties" % step)
                print("EXPECTED RESULT %d: Should retrieve MLD_AP_INDICES from platform properties" % step)
                if expectedresult in actualresult and apIndexOutput:
                    tdkTestObj.setResultStatus("SUCCESS")
                    allIndexList = [idx.strip().strip('\\n').strip() for idx in apIndexOutput.split(",") if idx.strip()]

                    # Select only as many indices as there are radios
                    apIndexList = allIndexList[:radioCount]
                    print("ACTUAL RESULT %d: MLD_AP_INDICES from properties: %s, RadioNumberOfEntries: %d, Using indices: %s" % (step, allIndexList, radioCount, apIndexList))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    # Step per AP: Get MLD Address via tr181 object and compare with MLD Interface hardware address
                    for apIndex in apIndexList:
                        step += 1
                        tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get')
                        actualresult, mldAddr = getTR181Value(tdkTestObj_Tr181_Get, "Device.WiFi.AccessPoint.%s.MLD_Addr" % apIndex)
                        mldAddr = mldAddr.strip().strip('\\n').strip()

                        print("\nTEST STEP %d: Check Device.WiFi.AccessPoint.%s.MLD_Addr matches MLD Interface hardware address" % (step, apIndex))
                        print("EXPECTED RESULT %d: Device.WiFi.AccessPoint.%s.MLD_Addr should match MLD Interface hardware address %s" % (step, apIndex, mldHWAddr))
                        if expectedresult in actualresult and mldAddr:
                            if mldAddr.upper() == mldHWAddr.upper():
                                tdkTestObj_Tr181_Get.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: Device.WiFi.AccessPoint.%s.MLD_Addr matches MLD Interface hardware address: %s" % (step, apIndex, mldAddr))
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj_Tr181_Get.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: Device.WiFi.AccessPoint.%s.MLD_Addr MISMATCH - TR-181: %s, MLD Interface hardware address: %s" % (step, apIndex, mldAddr, mldHWAddr))
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj_Tr181_Get.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Failed to get Device.WiFi.AccessPoint.%s.MLD_Addr" % (step, apIndex))
                            print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to get MLD_AP_INDICES from platform properties" % step)
                    print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj_Tr181_Get.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get RadioNumberOfEntries" % step)
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get hardware address of MLD Interface" % step)
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("sysutil")
    tr181obj.unloadModule("tdkbtr181")
else:
    print("Failed to load sysutil or tdkbtr181 module")
    obj.setLoadModuleStatus("FAILURE")
    tr181obj.setLoadModuleStatus("FAILURE")

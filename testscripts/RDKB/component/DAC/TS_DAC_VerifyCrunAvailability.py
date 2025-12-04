##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2025 RDK Management
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
from time import sleep
from DACVariables import *
from DACUtility import *
from tdkutility import *
import tdkbVariables

# Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")

# IP and Port of box, No need to change, will be replaced with DUT details
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_DAC_VerifyCrunAvailability')
obj.configureTestCase(ip,port,'TS_DAC_VerifyCrunAvailability')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus = obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus_sys.upper() and "SUCCESS" in loadmodulestatus.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Factory Reset the device
    print("\nTEST STEP %d: Initiate Factory Reset on the DUT" %step)
    print("EXPECTED RESULT %d: Factory Reset should be triggered successfully" %step)
    sysobj.saveCurrentState()
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_SetOnly')
    actualresult, details = setTR181Value(tdkTestObj, FACTORY_RESET_PARAM, FACTORY_RESET_VALUE, "string")
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Factory Reset triggered successfully. Details : %s" %(step, details))
        print("[TEST EXECUTION RESULT] : SUCCESS")
        # Restore the device state saved before Factory Reset
        sysobj.restorePreviousStateAfterReboot()
        sleep(FACTORY_RESET_WAIT_TIME)

        step += 1
        binary_name = CRUN_BINARY
        # Check if crun binary exists
        print("\nTEST STEP %d: Check if %s binary exists" % (step, binary_name))
        print("EXPECTED RESULT %d: Binary should exist in the system" % step)
        tdkTestObj, actualresult, path = check_binary_exists(sysobj, binary_name)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Binary exists at path: %s" % (step, path))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Binary does not exist" % step)
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Factory Reset failed. Details : %s" %(step, details))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload the modules
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

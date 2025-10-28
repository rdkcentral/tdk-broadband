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
from CrashUploadVariables import *
from CrashUploadUtility import *
from tdkutility import *
import tdkbVariables

# Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change, will be replaced with DUT details
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_CrashUpload_VerifyCoredumpUploadPath')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus_sys.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1
    unit_name = COREDUMP_PATH_UNIT

    # Check path unit status
    print("\nTEST STEP %d: Check status of %s" % (step, unit_name))
    print("EXPECTED RESULT %d: Unit should be loaded and active" % step)
    tdkTestObj, actualresult, details = check_unit_status(sysobj, unit_name)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Unit status checked successfully. Details: %s" % (step, details))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Verify unit is enabled
        print("\nTEST STEP %d: Verify if %s is enabled" % (step, unit_name))
        print("EXPECTED RESULT %d: Unit should be enabled" % step)
        tdkTestObj, actualresult, details = check_unit_enabled(sysobj, unit_name)
        if expectedresult in actualresult and details == "enabled":
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Unit is enabled. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Verify active (waiting) state
            print("\nTEST STEP %d: Verify active state of %s" % (step, unit_name))
            print("EXPECTED RESULT %d: State should be active (waiting)" % step)
            tdkTestObj, actualresult, state = get_active_state(sysobj, unit_name)
            if expectedresult in actualresult and "active (waiting)" in state:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Active state is correct: %s" % (step, state))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                # Verify it triggers the service
                print("\nTEST STEP %d: Verify triggers for %s" % (step, unit_name))
                print("EXPECTED RESULT %d: Should trigger coredump-upload.service" % step)
                tdkTestObj, actualresult, triggers = get_triggers(sysobj, unit_name)
                if expectedresult in actualresult and COREDUMP_SERVICE_UNIT in triggers:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Triggers correct: %s" % (step, triggers))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Triggers incorrect: %s" % (step, triggers))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Active state incorrect: %s" % (step, state))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Unit not enabled. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Unit status check failed. Details: %s" % (step, details))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload the modules
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

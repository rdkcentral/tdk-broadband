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
sysobj.configureTestCase(ip,port,'TS_DAC_VerifyDobbyServiceStatus')
obj.configureTestCase(ip,port,'TS_DAC_VerifyDobbyServiceStatus')

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
        service_name = DOBBY_SERVICE
        # Check dobby service status
        print("\nTEST STEP %d: Check if %s is loaded" % (step, service_name))
        print("EXPECTED RESULT %d: Service should be loaded" % step)
        tdkTestObj, actualresult, details = check_service_status(sysobj, service_name)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Service is loaded. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Verify dobby service is enabled
            print("\nTEST STEP %d: Verify if %s is enabled" % (step, service_name))
            print("EXPECTED RESULT %d: Service should be enabled" % step)
            tdkTestObj, actualresult, details = check_service_enabled(sysobj, service_name)
            if expectedresult in actualresult and details == EXPECTED_ENABLED_STATE:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Service is enabled. Details: %s" % (step, details))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                # Verify dobby service is active (running)
                print("\nTEST STEP %d: Verify active state of %s" % (step, service_name))
                print("EXPECTED RESULT %d: State should be active (running)" % step)
                tdkTestObj, actualresult, state = get_service_active_state(sysobj, service_name)
                if expectedresult in actualresult and EXPECTED_ACTIVE_STATE in state:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Service is active (running). State: %s" % (step, state))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step += 1
                    # Verify DobbyDaemon process is running
                    print("\nTEST STEP %d: Verify %s process is running" % (step, DOBBY_DAEMON_PROCESS))
                    print("EXPECTED RESULT %d: Process should be running with valid PID" % step)
                    tdkTestObj, actualresult, process_pid = verify_process_exists(sysobj, DOBBY_DAEMON_PROCESS)
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: %s process is running with PID: %s" % (step, DOBBY_DAEMON_PROCESS, process_pid))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: %s process is not running" % (step, DOBBY_DAEMON_PROCESS))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Service is not active (running). State: %s" % (step, state))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Service is not enabled. Details: %s" % (step, details))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Service status check failed. Details: %s" % (step, details))
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

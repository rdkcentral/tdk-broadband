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
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")

# IP and Port of box, No need to change, will be replaced with DUT details
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_CrashUpload_VerifyCoredumpUploadService')
obj.configureTestCase(ip,port,'TS_CrashUpload_VerifyCoredumpUploadService')

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
    actualresult, details = setTR181Value(tdkTestObj, "Device.X_CISCO_COM_DeviceControl.FactoryReset", "Router,Wifi,VoIP,Dect,MoCA", "string")
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Factory Reset triggered successfully. Details : %s" %(step, details))
        print("[TEST EXECUTION RESULT] : SUCCESS")
        # Restore the device state saved before Factory Reset
        sysobj.restorePreviousStateAfterReboot()

        step += 1
        unit_name = COREDUMP_SERVICE_UNIT
        # Check service unit status
        print("\nTEST STEP %d: Check status of %s" % (step, unit_name))
        print("EXPECTED RESULT %d: Service should be loaded" % step)
        tdkTestObj, actualresult, details = check_unit_status(sysobj, unit_name)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Service status checked successfully. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Verify service is enabled
            print("\nTEST STEP %d: Verify if %s is enabled" % (step, unit_name))
            print("EXPECTED RESULT %d: Service should be enabled" % step)
            tdkTestObj, actualresult, details = check_unit_enabled(sysobj, unit_name)
            if expectedresult in actualresult and details == "enabled":
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Service is enabled. Details: %s" % (step, details))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                # Verify inactive (dead) state
                print("\nTEST STEP %d: Verify active state of %s" % (step, unit_name))
                print("EXPECTED RESULT %d: State should be inactive (dead) when not triggered" % step)
                tdkTestObj, actualresult, state = get_service_active_state(sysobj, unit_name)
                if expectedresult in actualresult and ("inactive (dead)" in state or "Active: active" in state):
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Active state is correct: %s" % (step, state))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step += 1
                    # Verify triggered by path unit
                    print("\nTEST STEP %d: Verify triggered by for %s" % (step, unit_name))
                    print("EXPECTED RESULT %d: Should be triggered by %s" % (step, COREDUMP_PATH_UNIT))
                    tdkTestObj, actualresult, triggered_by = get_triggered_by(sysobj, unit_name)
                    if expectedresult in actualresult and COREDUMP_PATH_UNIT in triggered_by:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Triggered by correct: %s" % (step, triggered_by))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Triggered by incorrect: %s" % (step, triggered_by))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Active state incorrect: %s" % (step, state))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Service not enabled. Details: %s" % (step, details))
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

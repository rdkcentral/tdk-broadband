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
from time import sleep
from RNDISVariables import *
from RNDISUtility import *
from tdkutility import *

# Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")

# IP and Port of box, No need to change, will be replaced with DUT details
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_RNDIS_VerifyCellularInterfaceToggling')
obj.configureTestCase(ip,port,'TS_RNDIS_VerifyCellularInterfaceToggling')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus = obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus_sys.upper() and "SUCCESS" in loadmodulestatus.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1
    initial_enable_value = ""

    # Step 1: Verify the target WAN interface is up with active IP (prerequisite)
    print("\nTEST STEP %d: Verify the target WAN interface %s has active IP address" % (step, ANDROID_WAN_INTERFACE))
    print("EXPECTED RESULT %d: Interface %s should have inet addr" % (step, ANDROID_WAN_INTERFACE))
    tdkTestObj, actualresult, interface_name = get_target_wan_interface(sysobj, ANDROID_WAN_INTERFACE)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: WAN interface %s has active IP address" % (step, interface_name))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Step 2: Get the default value of Device.Cellular.Interface.1.Enable
        print("\nTEST STEP %d: Get the default value of %s" % (step, DM_CELLULAR_INTERFACE_ENABLE))
        print("EXPECTED RESULT %d: Should get the current value (Expected: true)" % step)
        tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
        actualresult, details = getTR181Value(tdkTestObj_tr181, DM_CELLULAR_INTERFACE_ENABLE)
        if expectedresult in actualresult:
            initial_enable_value = details.split("VALUE:")[1].split(',')[0].strip() if "VALUE:" in details else details.strip()
            tdkTestObj_tr181.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Current value of %s is %s" % (step, DM_CELLULAR_INTERFACE_ENABLE, initial_enable_value))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Step 3: Set Device.Cellular.Interface.1.Enable to false and confirm
            print("\nTEST STEP %d: Set %s to false and confirm set operation" % (step, DM_CELLULAR_INTERFACE_ENABLE))
            print("EXPECTED RESULT %d: Set operation should succeed and value should be false" % step)
            tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Set')
            actualresult, details = setTR181Value(tdkTestObj_tr181, DM_CELLULAR_INTERFACE_ENABLE, "false", "bool")
            if expectedresult in actualresult:
                # Confirm the set operation by getting the value
                tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
                actualresult, details = getTR181Value(tdkTestObj_tr181, DM_CELLULAR_INTERFACE_ENABLE)
                if expectedresult in actualresult:
                    current_value = details.split("VALUE:")[1].split(',')[0].strip() if "VALUE:" in details else details.strip()
                    if current_value == EXPECTED_ENABLE_FALSE:
                        tdkTestObj_tr181.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Set operation succeeded, value is now %s" % (step, current_value))
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        step += 1
                        # Step 4: Check if Device.Cellular.X_RDK_Status is DEREGISTERED
                        print("\nTEST STEP %d: Check if %s is DEREGISTERED" % (step, DM_CELLULAR_RDK_STATUS))
                        print("EXPECTED RESULT %d: Status should be DEREGISTERED" % step)
                        tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
                        actualresult, details = getTR181Value(tdkTestObj_tr181, DM_CELLULAR_RDK_STATUS)
                        if expectedresult in actualresult:
                            rdk_status = details.split("VALUE:")[1].split(' ')[0].strip() if "VALUE:" in details else details.strip()
                            if rdk_status == EXPECTED_STATUS_DEREGISTERED:
                                tdkTestObj_tr181.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: Cellular status is %s" % (step, rdk_status))
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                step += 1
                                # Step 5: Toggle Device.Cellular.Interface.1.Enable back to true and confirm
                                print("\nTEST STEP %d: Toggle %s back to true and confirm set operation" % (step, DM_CELLULAR_INTERFACE_ENABLE))
                                print("EXPECTED RESULT %d: Set operation should succeed and value should be true" % step)
                                tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Set')
                                actualresult, details = setTR181Value(tdkTestObj_tr181, DM_CELLULAR_INTERFACE_ENABLE, "true", "bool")
                                if expectedresult in actualresult:
                                    # Confirm the set operation by getting the value
                                    tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
                                    actualresult, details = getTR181Value(tdkTestObj_tr181, DM_CELLULAR_INTERFACE_ENABLE)
                                    if expectedresult in actualresult:
                                        current_value = details.split("VALUE:")[1].split(',')[0].strip() if "VALUE:" in details else details.strip()
                                        if current_value == EXPECTED_ENABLE_TRUE:
                                            tdkTestObj_tr181.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT %d: Set operation succeeded, value is now %s" % (step, current_value))
                                            print("[TEST EXECUTION RESULT] : SUCCESS")

                                            step += 1
                                            # Step 6: Check if Device.Cellular.X_RDK_Status is REGISTERED
                                            print("\nTEST STEP %d: Check if %s is REGISTERED" % (step, DM_CELLULAR_RDK_STATUS))
                                            print("EXPECTED RESULT %d: Status should be REGISTERED" % step)
                                            tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
                                            actualresult, details = getTR181Value(tdkTestObj_tr181, DM_CELLULAR_RDK_STATUS)
                                            if expectedresult in actualresult:
                                                rdk_status = details.split("VALUE:")[1].split(' ')[0].strip() if "VALUE:" in details else details.strip()
                                                if rdk_status == EXPECTED_STATUS_REGISTERED:
                                                    tdkTestObj_tr181.setResultStatus("SUCCESS")
                                                    print("ACTUAL RESULT %d: Cellular status is %s" % (step, rdk_status))
                                                    print("[TEST EXECUTION RESULT] : SUCCESS")

                                                    step += 1
                                                    # Step 7: Monitor cellular status for 5 minutes
                                                    print("\nTEST STEP %d: Monitor %s for %d seconds (checking every %d seconds)" % 
                                                          (step, DM_CELLULAR_RDK_STATUS, MONITORING_DURATION, MONITORING_INTERVAL))
                                                    print("EXPECTED RESULT %d: Status should remain REGISTERED throughout monitoring period" % step)
                                                    tdkTestObj_tr181, actualresult, details = monitor_cellular_status(
                                                        obj, DM_CELLULAR_RDK_STATUS, EXPECTED_STATUS_REGISTERED, 
                                                        MONITORING_DURATION, MONITORING_INTERVAL)
                                                    if expectedresult in actualresult:
                                                        tdkTestObj_tr181.setResultStatus("SUCCESS")
                                                        print("ACTUAL RESULT %d: %s" % (step, details.split('\n')[0]))
                                                        print("[TEST EXECUTION RESULT] : SUCCESS")
                                                    else:
                                                        tdkTestObj_tr181.setResultStatus("FAILURE")
                                                        print("ACTUAL RESULT %d: %s" % (step, details.split('\n')[0]))
                                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                                else:
                                                    tdkTestObj_tr181.setResultStatus("FAILURE")
                                                    print("ACTUAL RESULT %d: Cellular status is %s (Expected: %s)" % 
                                                          (step, rdk_status, EXPECTED_STATUS_REGISTERED))
                                                    print("[TEST EXECUTION RESULT] : FAILURE")
                                            else:
                                                tdkTestObj_tr181.setResultStatus("FAILURE")
                                                print("ACTUAL RESULT %d: Failed to get cellular status. Details: %s" % (step, details))
                                                print("[TEST EXECUTION RESULT] : FAILURE")
                                        else:
                                            tdkTestObj_tr181.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT %d: Set operation failed, value is %s (Expected: true)" % (step, current_value))
                                            print("[TEST EXECUTION RESULT] : FAILURE")
                                    else:
                                        tdkTestObj_tr181.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: Failed to confirm set operation. Details: %s" % (step, details))
                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                else:
                                    tdkTestObj_tr181.setResultStatus("FAILURE")
                                    print("ACTUAL RESULT %d: Failed to set value to true. Details: %s" % (step, details))
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                tdkTestObj_tr181.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: Cellular status is %s (Expected: %s)" % 
                                      (step, rdk_status, EXPECTED_STATUS_DEREGISTERED))
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj_tr181.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Failed to get cellular status. Details: %s" % (step, details))
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj_tr181.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Set operation failed, value is %s (Expected: false)" % (step, current_value))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj_tr181.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to confirm set operation. Details: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj_tr181.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to set value to false. Details: %s" % (step, details))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj_tr181.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get initial value. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to verify WAN interface %s has IP address" % (step, ANDROID_WAN_INTERFACE))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload the modules
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

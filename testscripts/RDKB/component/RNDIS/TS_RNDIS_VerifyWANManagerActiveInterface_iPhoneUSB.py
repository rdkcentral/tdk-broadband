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
sysobj.configureTestCase(ip,port,'TS_RNDIS_VerifyWANManagerActiveInterface_iPhoneUSB')
obj.configureTestCase(ip,port,'TS_RNDIS_VerifyWANManagerActiveInterface_iPhoneUSB')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus = obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus_sys.upper() and "SUCCESS" in loadmodulestatus.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Verify the target WAN interface is up with active IP (prerequisite)
    print("\nTEST STEP %d: Verify the target WAN interface %s has active IP address" % (step, IOS_WAN_INTERFACE))
    print("EXPECTED RESULT %d: Interface %s should have inet addr" % (step, IOS_WAN_INTERFACE))
    tdkTestObj, actualresult, details = get_target_wan_interface(sysobj, IOS_WAN_INTERFACE)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: WAN interface %s has active IP address: %s" % (step, IOS_WAN_INTERFACE, details))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Step 2: Get the value of WanManager CurrentActiveInterface DM
        print("\nTEST STEP %d: Get the value of %s" % (step, DM_WAN_MANAGER_CURRENT_ACTIVE_INTERFACE))
        print("EXPECTED RESULT %d: Should successfully retrieve the current active interface" % step)
        tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
        actualresult, details = getTR181Value(tdkTestObj_tr181, DM_WAN_MANAGER_CURRENT_ACTIVE_INTERFACE)
        if expectedresult in actualresult and details != "":
            current_active_interface = details.strip()
            tdkTestObj_tr181.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Current active interface is: %s" % (step, current_active_interface))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Step 3: Verify and confirm the value is expected when RNDIS is active
            print("\nTEST STEP %d: Verify the current active interface is %s" % (step, IOS_WAN_INTERFACE))
            print("EXPECTED RESULT %d: Current active interface should be %s" % (step, IOS_WAN_INTERFACE))
            if current_active_interface == IOS_WAN_INTERFACE:
                tdkTestObj_tr181.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Current active interface matches - DM value: %s, Expected: %s" % 
                      (step, current_active_interface, IOS_WAN_INTERFACE))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                # Step 4: Get the value of WanManager CurrentStatus DM
                print("\nTEST STEP %d: Get the value of %s" % (step, DM_WAN_MANAGER_CURRENT_STATUS))
                print("EXPECTED RESULT %d: Should successfully retrieve the current WAN status" % step)
                tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
                actualresult, details = getTR181Value(tdkTestObj_tr181, DM_WAN_MANAGER_CURRENT_STATUS)
                if expectedresult in actualresult and details != "":
                    current_status = details.strip()
                    tdkTestObj_tr181.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Current WAN status is: %s" % (step, current_status))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step += 1
                    # Step 5: Verify and confirm the value is as expected when RNDIS is active
                    print("\nTEST STEP %d: Verify the current WAN status is Up" % step)
                    print("EXPECTED RESULT %d: Current status should be %s" % (step, EXPECTED_WAN_STATUS_UP))
                    if current_status == EXPECTED_WAN_STATUS_UP:
                        tdkTestObj_tr181.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Current WAN status matches - DM value: %s, Expected: %s" % 
                              (step, current_status, EXPECTED_WAN_STATUS_UP))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj_tr181.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Current WAN status mismatch - DM value: %s, Expected: %s" % 
                              (step, current_status, EXPECTED_WAN_STATUS_UP))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj_tr181.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to get current WAN status. Details: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj_tr181.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Current active interface mismatch - DM value: %s, Expected: %s" % 
                      (step, current_active_interface, IOS_WAN_INTERFACE))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj_tr181.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get current active interface. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to verify WAN interface %s has IP address" % (step, IOS_WAN_INTERFACE))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload the modules
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

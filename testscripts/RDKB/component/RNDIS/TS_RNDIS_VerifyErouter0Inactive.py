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

# IP and Port of box, No need to change, will be replaced with DUT details
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_RNDIS_VerifyErouter0Inactive')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus_sys.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Verify the target WAN interface is up with active IP (prerequisite)
    print("\nTEST STEP %d: Verify the target WAN interface %s has active IP address" % (step, ANDROID_WAN_INTERFACE))
    print("EXPECTED RESULT %d: Interface %s should have inet addr" % (step, ANDROID_WAN_INTERFACE))
    tdkTestObj, actualresult, interface_name = get_target_wan_interface(sysobj, ANDROID_WAN_INTERFACE)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: WAN interface %s has active IP address" % (step, interface_name))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Step 2: Check erouter0 interface status
        print("\nTEST STEP %d: Check %s interface status" % (step, DEFAULT_WAN_INTERFACE))
        print("EXPECTED RESULT %d: Should get %s interface details" % (step, DEFAULT_WAN_INTERFACE))
        tdkTestObj, actualresult, erouter_details = check_interface_no_ip(sysobj, DEFAULT_WAN_INTERFACE)
        # For this step, we just want to get the interface details, so we mark it SUCCESS
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Retrieved %s interface status" % (step, DEFAULT_WAN_INTERFACE))
        print("Interface details: %s" % erouter_details.split('\n')[0] if erouter_details else "No output")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Step 3: Verify erouter0 does not have an IP address
        print("\nTEST STEP %d: Verify %s does not have an IP address in RNDIS mode" % (step, DEFAULT_WAN_INTERFACE))
        print("EXPECTED RESULT %d: %s should not have 'inet addr' assigned" % (step, DEFAULT_WAN_INTERFACE))
        if actualresult == "SUCCESS":
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: %s does not have an IP address (as expected in RNDIS mode)" % (step, DEFAULT_WAN_INTERFACE))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: %s has an IP address (unexpected in RNDIS mode)" % (step, DEFAULT_WAN_INTERFACE))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to verify WAN interface %s has IP address" % (step, ANDROID_WAN_INTERFACE))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload the module
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

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
import tdkbVariables

# Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change, will be replaced with DUT details
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_RNDIS_VerifyPrimaryWANInactive_AndroidUSB')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus_sys.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Get primary WAN INTERFACE from platform properties
    print("\nTEST STEP %d: Get primary WAN INTERFACE from platform properties" % step)
    print("EXPECTED RESULT %d: Should successfully retrieve primary WAN INTERFACE value" % step)
    command = "sh %s/tdk_utility.sh parseConfigFile INTERFACE" % tdkbVariables.TDK_PATH
    tdkTestObj = sysobj.createTestStep('ExecuteCmd')
    actualresult, default_wan_interface = doSysutilExecuteCommand(tdkTestObj, command)
    default_wan_interface = default_wan_interface.strip()
    if expectedresult in actualresult and default_wan_interface != "":
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: primary WAN INTERFACE value is: %s" % (step, default_wan_interface))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Step 2: Verify the target WAN interface is up with active IP (prerequisite)
        print("\nTEST STEP %d: Verify the target WAN interface %s has active IP address" % (step, ANDROID_WAN_INTERFACE))
        print("EXPECTED RESULT %d: Interface %s should have inet addr" % (step, ANDROID_WAN_INTERFACE))
        tdkTestObj, actualresult, details = get_target_wan_interface(sysobj, ANDROID_WAN_INTERFACE)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: WAN interface %s has active IP address: %s" % (step, ANDROID_WAN_INTERFACE, details))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Step 3: Verify Primary WAN interface does not have an IP address when RNDIS is active
            print("\nTEST STEP %d: Verify %s does not have an IP address in RNDIS mode" % (step, default_wan_interface))
            print("EXPECTED RESULT %d: %s should not have %s assigned" % (step, default_wan_interface, INET_ADDR_PATTERN))
            tdkTestObj, actualresult = check_interface_no_ip(sysobj, default_wan_interface)
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: %s does not have an IP address (as expected in RNDIS mode)" % (step, default_wan_interface))
                print("Interface %s has no valid IP" % default_wan_interface)
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: %s has an IP address (unexpected in RNDIS mode)" % (step, default_wan_interface))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to verify WAN interface %s has IP address" % (step, ANDROID_WAN_INTERFACE))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get INTERFACE from platform properties. Details: %s" % (step, default_wan_interface))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload the module
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

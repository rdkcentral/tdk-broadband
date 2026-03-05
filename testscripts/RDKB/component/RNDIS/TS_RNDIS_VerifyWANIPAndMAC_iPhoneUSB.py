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
sysobj.configureTestCase(ip,port,'TS_RNDIS_VerifyWANIPAndMAC_iPhoneUSB')
obj.configureTestCase(ip,port,'TS_RNDIS_VerifyWANIPAndMAC_iPhoneUSB')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus = obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus_sys.upper() and "SUCCESS" in loadmodulestatus.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Get the target WAN interface name
    print("\nTEST STEP %d: Verify the target WAN interface %s has IP address assigned" % (step, IOS_WAN_INTERFACE))
    print("EXPECTED RESULT %d: Interface %s should have inet addr" % (step, IOS_WAN_INTERFACE))
    tdkTestObj, actualresult, wan_ip = get_target_wan_interface(sysobj, IOS_WAN_INTERFACE)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: WAN interface %s has IP address assigned: %s" % (step, IOS_WAN_INTERFACE, wan_ip))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Step 2: Get the MAC address of the WAN interface
        print("\nTEST STEP %d: Get the MAC address of the WAN interface %s" % (step, IOS_WAN_INTERFACE))
        print("EXPECTED RESULT %d: Should successfully retrieve MAC address" % step)
        tdkTestObj, actualresult, wan_mac = get_interface_mac_address(sysobj, IOS_WAN_INTERFACE)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: WAN interface MAC address: %s" % (step, wan_mac))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Step 3: Get the value of WAN IP DM
            print("\nTEST STEP %d: Get the data model parameter %s" % (step, DM_WAN_IP))
            print("EXPECTED RESULT %d: Should successfully retrieve DM WAN IP value" % step)
            tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
            actualresult, details = getTR181Value(tdkTestObj_tr181, DM_WAN_IP)
            if expectedresult in actualresult and details != "":
                dm_wan_ip = details.strip()
                tdkTestObj_tr181.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: DM WAN IP: %s" % (step, dm_wan_ip))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                # Step 4: Get the value of WAN MAC DM
                print("\nTEST STEP %d: Get the data model parameter %s" % (step, DM_WAN_MAC))
                print("EXPECTED RESULT %d: Should successfully retrieve DM WAN MAC value" % step)
                tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
                actualresult, details = getTR181Value(tdkTestObj_tr181, DM_WAN_MAC)
                if expectedresult in actualresult and details != "":
                    dm_wan_mac = details.strip()
                    tdkTestObj_tr181.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: DM WAN MAC: %s" % (step, dm_wan_mac))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step += 1
                    # Step 5: Verify that WAN IP DM value matches the target WAN interface IP
                    print("\nTEST STEP %d: Verify that DM WAN IP matches interface IP" % step)
                    print("EXPECTED RESULT %d: IP addresses should match" % step)
                    actualresult, details = verify_ip_match(wan_ip, dm_wan_ip)
                    if expectedresult in actualresult:
                        tdkTestObj_tr181.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj_tr181.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : FAILURE")

                    step += 1
                    # Step 6: Verify that WAN MAC DM value matches the target WAN interface MAC
                    print("\nTEST STEP %d: Verify that DM WAN MAC matches interface MAC" % step)
                    print("EXPECTED RESULT %d: MAC addresses should match" % step)
                    actualresult, details = verify_mac_match(wan_mac, dm_wan_mac)
                    if expectedresult in actualresult:
                        tdkTestObj_tr181.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj_tr181.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj_tr181.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to get DM WAN MAC. Details: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj_tr181.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to get DM WAN IP. Details: %s" % (step, details))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get WAN interface MAC address. Details: %s" % (step, wan_mac))
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

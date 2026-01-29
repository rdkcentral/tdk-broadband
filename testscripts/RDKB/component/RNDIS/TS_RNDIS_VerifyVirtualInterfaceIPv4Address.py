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
sysobj.configureTestCase(ip,port,'TS_RNDIS_VerifyVirtualInterfaceIPv4Address')
obj.configureTestCase(ip,port,'TS_RNDIS_VerifyVirtualInterfaceIPv4Address')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus = obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus_sys.upper() and "SUCCESS" in loadmodulestatus.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Confirm if usb0 interface is up with active IP (prerequisite)
    print("\nTEST STEP %d: Verify the target WAN interface %s has active IP address" % (step, ANDROID_WAN_INTERFACE))
    print("EXPECTED RESULT %d: Interface %s should have inet addr" % (step, ANDROID_WAN_INTERFACE))
    tdkTestObj, actualresult, interface_name = get_target_wan_interface(sysobj, ANDROID_WAN_INTERFACE)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: WAN interface %s has active IP address" % (step, interface_name))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Step 2: Get the value of Device.X_RDK_WanManager.Interface.2.VirtualInterface.1.IP.IPv4Address
        print("\nTEST STEP %d: Get the value of %s" % (step, DM_WAN_MANAGER_VIRTUAL_INTERFACE_IPV4))
        print("EXPECTED RESULT %d: Should successfully retrieve the virtual interface IPv4 address" % step)
        tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
        actualresult, details = getTR181Value(tdkTestObj_tr181, DM_WAN_MANAGER_VIRTUAL_INTERFACE_IPV4)
        if expectedresult in actualresult:
            dm_ipv4_address = details.split("VALUE:")[1].split(' ')[0].strip() if "VALUE:" in details else details.strip()
            tdkTestObj_tr181.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Virtual interface IPv4 address is: %s" % (step, dm_ipv4_address))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Step 3: Get the value of usb0 interface IP
            print("\nTEST STEP %d: Get the IP address of %s interface" % (step, ANDROID_WAN_INTERFACE))
            print("EXPECTED RESULT %d: Should successfully retrieve the interface IP address" % step)
            tdkTestObj, actualresult, usb0_ip = get_interface_ip_address(sysobj, ANDROID_WAN_INTERFACE)
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: %s interface IP address is: %s" % (step, ANDROID_WAN_INTERFACE, usb0_ip))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                # Step 4: Compare both values and confirm they are the same
                print("\nTEST STEP %d: Compare virtual interface IPv4 address with %s interface IP" % (step, ANDROID_WAN_INTERFACE))
                print("EXPECTED RESULT %d: Both IP addresses should match" % step)
                if dm_ipv4_address == usb0_ip:
                    tdkTestObj_tr181.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: IP addresses match - DM IPv4: %s, %s IP: %s" % 
                          (step, dm_ipv4_address, ANDROID_WAN_INTERFACE, usb0_ip))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj_tr181.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: IP addresses mismatch - DM IPv4: %s, %s IP: %s" % 
                          (step, dm_ipv4_address, ANDROID_WAN_INTERFACE, usb0_ip))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to get %s interface IP address" % (step, ANDROID_WAN_INTERFACE))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj_tr181.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get virtual interface IPv4 address. Details: %s" % (step, details))
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

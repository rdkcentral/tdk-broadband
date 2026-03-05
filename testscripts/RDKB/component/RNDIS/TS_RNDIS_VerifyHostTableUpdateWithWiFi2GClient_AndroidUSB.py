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
sysobj.configureTestCase(ip,port,'TS_RNDIS_VerifyHostTableUpdateWithWiFi2GClient_AndroidUSB')
obj.configureTestCase(ip,port,'TS_RNDIS_VerifyHostTableUpdateWithWiFi2GClient_AndroidUSB')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus = obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus_sys.upper() and "SUCCESS" in loadmodulestatus.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Verify the target WAN interface is up with active IP (Prerequisite)
    print("\nTEST STEP %d: Verify the target WAN interface %s has active IP address" % (step, ANDROID_WAN_INTERFACE))
    print("EXPECTED RESULT %d: Interface %s should have inet addr" % (step, ANDROID_WAN_INTERFACE))
    tdkTestObj, actualresult, details = get_target_wan_interface(sysobj, ANDROID_WAN_INTERFACE)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: WAN interface %s has active IP address: %s" % (step, ANDROID_WAN_INTERFACE, details))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Step 2: Get the number of Host entries
        print("\nTEST STEP %d: Get the number of Host entries" % step)
        print("EXPECTED RESULT %d: Should successfully retrieve HostNumberOfEntries DM value" % step)
        tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
        actualresult, details = getTR181Value(tdkTestObj_tr181, DM_HOSTS_HOST_NUMBER_OF_ENTRIES)
        if expectedresult in actualresult and details != "":
            hostEntries = details.strip()
            if hostEntries.isdigit():
                hostEntries = int(hostEntries)
                tdkTestObj_tr181.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: HostNumberOfEntries : %d" % (step, hostEntries))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                # Step 3: Iterate through the Host Table and find WiFi 2.4G client entry and check if host is active
                tdkTestObj_tr181, actualresult, clientDetected, clientIndex, step = traverse_host_table_for_client(obj, hostEntries, EXPECTED_LAYER1_INTERFACE_WIFI_2_4G, step)
            else:
                tdkTestObj_tr181.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: HostNumberOfEntries DM value is not a valid number: %s" % (step, hostEntries))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj_tr181.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get HostNumberOfEntries value Details: %s" % (step, details))
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

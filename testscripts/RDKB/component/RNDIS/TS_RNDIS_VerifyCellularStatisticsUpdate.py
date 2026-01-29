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
sysobj.configureTestCase(ip,port,'TS_RNDIS_VerifyCellularStatisticsUpdate')
obj.configureTestCase(ip,port,'TS_RNDIS_VerifyCellularStatisticsUpdate')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus = obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus_sys.upper() and "SUCCESS" in loadmodulestatus.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    obj.setLoadModuleStatus("SUCCESS")
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
        # Step 2: Get initial statistics
        print("\nTEST STEP %d: Get initial cellular interface statistics" % step)
        print("EXPECTED RESULT %d: Should successfully retrieve initial statistics" % step)
        tdkTestObj_tr181, initial_bytes_sent, initial_bytes_received, initial_packets_sent, initial_packets_received = get_cellular_statistics(obj)
        tdkTestObj_tr181.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Initial Statistics Retrieved" % step)
        print("BytesSent: %d, BytesReceived: %d, PacketsSent: %d, PacketsReceived: %d" % 
              (initial_bytes_sent, initial_bytes_received, initial_packets_sent, initial_packets_received))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Step 3: Generate network traffic
        print("\nTEST STEP %d: Generate network traffic using ping -c %d www.google.com" % (step, PING_COUNT))
        print("EXPECTED RESULT %d: Traffic generation should complete successfully" % step)
        tdkTestObj, actualresult, ping_details = perform_ping_test(sysobj, PING_TARGET, PING_COUNT)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Traffic generation completed successfully" % step)
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Step 4: Get final statistics and verify they increased
            print("\nTEST STEP %d: Get final cellular interface statistics and verify increase" % step)
            print("EXPECTED RESULT %d: Statistics should have increased after traffic generation" % step)
            tdkTestObj_tr181, final_bytes_sent, final_bytes_received, final_packets_sent, final_packets_received = get_cellular_statistics(obj)
            print("Final Statistics Retrieved:")
            print("BytesSent: %d (Initial: %d, Increase: %d)" % 
                  (final_bytes_sent, initial_bytes_sent, final_bytes_sent - initial_bytes_sent))
            print("BytesReceived: %d (Initial: %d, Increase: %d)" % 
                  (final_bytes_received, initial_bytes_received, final_bytes_received - initial_bytes_received))
            print("PacketsSent: %d (Initial: %d, Increase: %d)" % 
                  (final_packets_sent, initial_packets_sent, final_packets_sent - initial_packets_sent))
            print("PacketsReceived: %d (Initial: %d, Increase: %d)" % 
                  (final_packets_received, initial_packets_received, final_packets_received - initial_packets_received))
            # Verify statistics have increased
            stats_increased = (final_bytes_sent > initial_bytes_sent or 
                             final_bytes_received > initial_bytes_received or 
                             final_packets_sent > initial_packets_sent or 
                             final_packets_received > initial_packets_received)

            if stats_increased:
                tdkTestObj_tr181.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Statistics have increased appropriately after traffic generation" % step)
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj_tr181.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Statistics did not increase after traffic generation" % step)
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to generate traffic. Details: %s" % (step, ping_details))
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

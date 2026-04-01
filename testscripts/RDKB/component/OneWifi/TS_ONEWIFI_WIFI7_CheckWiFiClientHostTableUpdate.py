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
from tdkutility import *
import tdkbVariables

# Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil", "1")
obj = tdklib.TDKScriptingLibrary("tdkbtr181", "1")

# IP and Port of box, No need to change, will be replaced with DUT details
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckWiFiClientHostTableUpdate')
obj.configureTestCase(ip,port,'TS_ONEWIFI_WIFI7_CheckWiFiClientHostTableUpdate')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus = obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus_sys.upper() and "SUCCESS" in loadmodulestatus.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Step 1: Get the number of Host entries
    print("\nTEST STEP %d: Get the number of Host entries" % step)
    print("EXPECTED RESULT %d: Should successfully retrieve Device.Hosts.HostNumberOfEntries DM value" % step)
    tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
    actualresult, hostEntriesOutput = getTR181Value(tdkTestObj_tr181, "Device.Hosts.HostNumberOfEntries")
    hostEntriesOutput = hostEntriesOutput.strip().strip('\\n').strip()

    if expectedresult in actualresult and hostEntriesOutput:
        if hostEntriesOutput.isdigit():
            hostEntries = int(hostEntriesOutput)
            tdkTestObj_tr181.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: HostNumberOfEntries: %d" % (step, hostEntries))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            # Step 2 onwards: Iterate through the Host Table and find any active WiFi client entry
            clientDetected = False
            clientIndex = None

            for i in range(1, hostEntries + 1):
                step += 1

                # Get Layer1Interface for this host entry
                tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
                actualresult, layer1Interface = getTR181Value(tdkTestObj_tr181, "Device.Hosts.Host.%d.Layer1Interface" % i)
                layer1Interface = layer1Interface.strip().strip('\\n').strip()

                print("\nTEST STEP %d: Get the value of Device.Hosts.Host.%d.Layer1Interface and verify it contains a valid interface path" % (step, i))
                print("EXPECTED RESULT %d: Device.Hosts.Host.%d.Layer1Interface should contain a valid interface path" % (step, i))
                if expectedresult in actualresult and layer1Interface:
                    tdkTestObj_tr181.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Host.%d Layer1Interface: %s" % (step, i, layer1Interface))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    # Check if this is a WiFi client (Layer1Interface contains WiFi SSID path)
                    if "Device.WiFi.SSID." in layer1Interface:

                        # Step: Get Active status for this WiFi client
                        step += 1
                        tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
                        actualresult, activeStatus = getTR181Value(tdkTestObj_tr181, "Device.Hosts.Host.%d.Active" % i)
                        activeStatus = activeStatus.strip().strip('\\n').strip()

                        print("\nTEST STEP %d: Get the value of Device.Hosts.Host.%d.Active" % (step, i))
                        print("EXPECTED RESULT %d: Device.Hosts.Host.%d.Active should be true" % (step, i))
                        if expectedresult in actualresult and activeStatus:
                            if activeStatus.lower() == "true":
                                tdkTestObj_tr181.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: WiFi client at Host.%d is Active - Layer1Interface: %s, Active: %s" % (step, i, layer1Interface, activeStatus))
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                                clientDetected = True
                                clientIndex = i
                                # Break out once an active WiFi client is found
                                break
                            else:
                                # Host table refreshes periodically; inactive client is not a failure - continue loop
                                tdkTestObj_tr181.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: WiFi client at Host.%d is not currently active (host table may not have refreshed) - Layer1Interface: %s, Active: %s" % (step, i, layer1Interface, activeStatus))
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj_tr181.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Failed to get Active status for Host.%d" % (step, i))
                            print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj_tr181.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to get Layer1Interface for Host.%d" % (step, i))
                    print("[TEST EXECUTION RESULT] : FAILURE")

            # Report if an active WiFi client was found in the host table
            step += 1
            print("\nTEST STEP %d: Check if any active WiFi client is present in Host table" % step)
            print("EXPECTED RESULT %d: At least one active WiFi client should be present in Host table" % step)
            if clientDetected:
                tdkTestObj_tr181.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Active WiFi client found in Host table at Host.%d" % (step, clientIndex))
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj_tr181.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: No active WiFi client found in Host table - ensure MLD/non-MLD client is connected as prerequisite" % step)
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj_tr181.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: HostNumberOfEntries DM value is not a valid number: %s" % (step, hostEntriesOutput))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj_tr181.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get HostNumberOfEntries value" % step)
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload the modules
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

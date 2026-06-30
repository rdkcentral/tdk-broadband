#########################################################################
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

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
from tdkbIPv6Utility import *
from tdkutility import *

# Test component to be tested
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181", "1")
sysobj = tdklib.TDKScriptingLibrary("sysutil", "1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

tr181obj.configureTestCase(ip,port,'TS_IPV6_Check_ActiveWLANClient_IPv6Address')

# Get the result of connection with test component and DUT
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()

expectedresult = "SUCCESS"

if expectedresult in loadmodulestatus_tr181.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")

    # Get the number of active WLAN clients connected
    step = 1
    print(f"\nTEST STEP {step} : Get the number of active WLAN clients connected using Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber")
    print(f"EXPECTED RESULT {step} : Should get the number of active WLAN clients connected using Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber")
    tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
    actualresult, active_wlan_clients = getTR181Value(tdkTestObj, "Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber")
    if expectedresult in actualresult and int(active_wlan_clients) > 0:
        print(f"ACTUAL RESULT {step} : Successfully got the number of active WLAN clients connected using Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber. Number of active WLAN clients is {active_wlan_clients}")
        tdkTestObj.setResultStatus("SUCCESS")
        print("[TEST EXECUTION RESULT] : SUCCESS\n")

        # Get the index of the active WLAN client
        step += 1
        index, step = getActiveClientIndex(tr181obj, LAYER1_INTERFACE_WLAN, step)

        if index is not None:
            # Get the IPv6 address of the active WLAN client
            step += 1
            print(f"\nTEST STEP {step} : Get the IPv6 address of the active WLAN client using Device.Hosts.Host.{index}.IPv6Address.3.IPAddress")
            print(f"EXPECTED RESULT {step} : Should get the IPv6 address of the active WLAN client using Device.Hosts.Host.{index}.IPv6Address.3.IPAddress")
            tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
            actualresult, ipv6_address = getTR181Value(tdkTestObj, f"Device.Hosts.Host.{index}.IPv6Address.3.IPAddress")
            if expectedresult in actualresult and ipv6_address != "":
                print(f"ACTUAL RESULT {step} : Successfully got the IPv6 address of the active WLAN client using Device.Hosts.Host.{index}.IPv6Address.3.IPAddress. IPv6 address is {ipv6_address}")
                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS\n")
            else:
                print(f"ACTUAL RESULT {step} : Failed to get the IPv6 address of the active WLAN client using Device.Hosts.Host.{index}.IPv6Address.3.IPAddress")
                tdkTestObj.setResultStatus("FAILURE")
                print("[TEST EXECUTION RESULT] : FAILURE\n")

    else:
        print(f"ACTUAL RESULT {step} : Failed to get the number of active WLAN clients connected using Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber")
        tdkTestObj.setResultStatus("FAILURE")
        print("[TEST EXECUTION RESULT] : FAILURE\n")

    tr181obj.unloadModule("tdkbtr181")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

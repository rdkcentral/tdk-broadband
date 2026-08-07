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
from tdkbIPv6Variables import *

# Test component to be tested
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181", "1")
sysobj = tdklib.TDKScriptingLibrary("sysutil", "1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

tr181obj.configureTestCase(ip,port,'TS_IPV6_Check_Brlan0LinkLocalNeighborConnectivity_LANInterface')
sysobj.configureTestCase(ip,port,'TS_IPV6_Check_Brlan0LinkLocalNeighborConnectivity_LANInterface')

# Get the result of connection with test component and DUT
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

expectedresult = "SUCCESS"

if expectedresult in loadmodulestatus_tr181.upper() and expectedresult in loadmodulestatus_sys.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    interface = DUT_LAN_INTERFACE
    if interface != "":
        print(f"LAN interface {interface} is obtained successfully from variables file")
        step = 1
        print(f"Check whether the LAN interface {interface} auto-configures an inet6 address with link local scope")
        flag = verifyIPv6Address(sysobj, interface, step, scope="link")
        if flag:
            print(f"LAN interface {interface} has inet6 address with link local scope")

            step += 1
            index, step = getActiveClientIndex(tr181obj, LAYER1_INTERFACE_LAN, step)
            if index is not None:
                step += 1
                link_local_ipv6, flag = getClientLinkLocalIPv6Address(tr181obj, index, step)
                if flag:
                    step += 1
                    print(f"Check whether {interface} can ping the link-local IPv6 address of the active LAN client")
                    ping_flag = checkInternetConnectivity(sysobj, link_local_ipv6, PING_COUNT, step, interface)
                    if ping_flag:
                        print(f"The {interface} interface can ping the link-local IPv6 address of the active LAN client successfully")
                    else:
                        print(f"The {interface} interface cannot ping the link-local IPv6 address of the active LAN client")
                else:
                    print("Failed to get the link-local IPv6 address of the active LAN client")
            else:
                print("Failed to get the index of the active LAN client")
        else:
            print(f"LAN interface {interface} does not have inet6 address with link local scope")
    else:
        print(f"Failed to get the LAN interface {interface} from variables file.")

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load tdkbtr181 and sysutil modules")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")

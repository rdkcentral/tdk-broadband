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

# Test component to be tested
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

sysobj.configureTestCase(ip,port,'TS_IPV6_Get_WANIPv6LinkLocalAddress')
tr181obj.configureTestCase(ip,port,'TS_IPV6_Get_WANIPv6LinkLocalAddress')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()

expectedresult = "SUCCESS"

if expectedresult in loadmodulestatus_sys.upper() and expectedresult in loadmodulestatus_tr181.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    tr181obj.setLoadModuleStatus("SUCCESS")

    # Check whether the WAN interface has link local IPv6 address
    step = 1
    interface = getWAN_Interface(tr181obj, step)

    if interface != "":
        print("WAN interface is obtained successfully")
        step += 1
        print("Check whether the WAN interface auto-configures an inet6 address with link local scope")
        flag = verifyIPv6Address(sysobj, interface, step, scope = "link")

        if flag:
            print("WAN interface has inet6 address with link local scope")

            #Extract IPv6 address and prefix of the WAN interface
            step += 1
            tdkTestObj, ipv6_addr, ipv6_prefix, prefix_flag = extractIPv6PrefixandAddress(sysobj, interface, step, scope = "link")

            if prefix_flag:
                print(f"IPv6 address of the WAN interface is {ipv6_addr} and prefix is {ipv6_prefix}")

                step += 1
                #Check whether the link local wan interface ipv6 address prefix is equal to LAN_IPV6_PREFIX_LENGTH
                print(f"\nTEST STEP {step} : Check whether the prefix of the link local IPv6 address of WAN interface is /{LAN_IPV6_PREFIX_LENGTH}")
                print(f"EXPECTED RESULT {step} : The prefix of the link local IPv6 address of WAN interface should be /{LAN_IPV6_PREFIX_LENGTH}")
                if ipv6_prefix == LAN_IPV6_PREFIX_LENGTH:
                    print(f"ACTUAL RESULT {step} : The prefix of the link local IPv6 address of WAN interface is /{LAN_IPV6_PREFIX_LENGTH}")
                    print("[TEST EXECUTION RESULT] : SUCCESS\n")
                    tdkTestObj.setResultStatus("SUCCESS")
                else:
                    print(f"ACTUAL RESULT {step} : The prefix of the link local IPv6 address of WAN interface is NOT /{LAN_IPV6_PREFIX_LENGTH}. Prefix is {ipv6_prefix}")
                    print("[TEST EXECUTION RESULT] : FAILURE\n")
                    tdkTestObj.setResultStatus("FAILURE")
            else:
                print("Failed to get the prefix of the ip address")
        else:
            print("WAN interface does not have inet6 address with link local scope")
    else:
        print("Failed to get the WAN interface name")

    sysobj.unloadModule("sysutil")
    tr181obj.unloadModule("tdkbtr181")
else:
    print("\nFailed to load the module")
    sysobj.setLoadModuleStatus("FAILURE")
    tr181obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
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
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

sysobj.configureTestCase(ip,port,'TS_IPV6_Get_Brlan0_IPv6Address')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
expectedresult = "SUCCESS"
if expectedresult in loadmodulestatus_sys.upper():
    sysobj.setLoadModuleStatus("SUCCESS")

    interface = DUT_LAN_INTERFACE
    if interface != "":
        print("LAN interface is obtained successfully from variables file")
        step = 1
        # Check whether the LAN interface has an global inet6 IP address
        flag = verifyIPv6Address(sysobj, interface, step)

        if flag:
            print("LAN interface has inet6 address with global scope")

            #Extract IPv6 address and prefix of the LAN interface
            step += 1
            tdkTestObj, ipv6_addr, ipv6_prefix, prefix_flag = extractIPv6PrefixandAddress(sysobj, interface, step)

            if prefix_flag:
                print(f"IPv6 address of the LAN interface is {ipv6_addr} and prefix is {ipv6_prefix}")

                step += 1
                #Check whether the global LAN interface ipv6 address prefix is equal to LAN_IPV6_PREFIX_LENGTH
                print(f"\nTEST STEP {step} : Check whether the prefix of the global IPv6 address of LAN interface is /{LAN_IPV6_PREFIX_LENGTH}")
                print(f"EXPECTED RESULT {step} : The prefix of the global IPv6 address of LAN interface should be /{LAN_IPV6_PREFIX_LENGTH}")
                if ipv6_prefix == LAN_IPV6_PREFIX_LENGTH:
                    print(f"ACTUAL RESULT {step} : The prefix of the global IPv6 address of LAN interface is /{LAN_IPV6_PREFIX_LENGTH}")
                    print("[TEST EXECUTION RESULT] : SUCCESS\n")
                    tdkTestObj.setResultStatus("SUCCESS")

                else:
                    print(f"ACTUAL RESULT {step} : The prefix of the global IPv6 address of LAN interface is NOT /{LAN_IPV6_PREFIX_LENGTH}. Prefix is {ipv6_prefix}")
                    print("[TEST EXECUTION RESULT] : FAILURE\n")
                    tdkTestObj.setResultStatus("FAILURE")
            else:
                print("Failed to get the prefix of the ip address")
        else:
            print("LAN interface does not have inet6 address with global scope")
    else:
        print("Failed to get the LAN interface name from variables file")

    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
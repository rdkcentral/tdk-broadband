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

tr181obj.configureTestCase(ip,port,'TS_IPV6_Get_WANIPv6Address')
sysobj.configureTestCase(ip,port,'TS_IPV6_Get_WANIPv6Address')

# Get the result of connection with test component and DUT
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

expectedresult = "SUCCESS"

if expectedresult in loadmodulestatus_tr181.upper() and expectedresult in loadmodulestatus_sys.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    # Check whether the WAN interface has inet6 address with global scope and get the prefix of the ip address and verify prefix
    step = 1
    interface = getWAN_Interface(tr181obj, step)

    if interface != "":
        print("WAN interface is obtained successfully")
        step += 1
        flag = verifyIPv6Address(sysobj, interface, step)

        if flag:
            print("WAN interface has inet6 address with global scope")

            #Extract IPv6 address and prefix of the WAN interface
            step += 1
            tdkTestObj, ipv6_addr, ipv6_prefix, prefix_flag = extractIPv6PrefixandAddress(sysobj, interface, step)

            if prefix_flag:
                print(f"IPv6 address of the WAN interface is {ipv6_addr} and prefix is {ipv6_prefix}")

                step += 1
                #Check whether the global wan interface ipv6 address prefix is equal to WAN_IPV6_PREFIX_LENGTH
                print(f"\nTEST STEP {step} : Check whether the prefix of the global IPv6 address of WAN interface is /{WAN_IPV6_PREFIX_LENGTH}")
                print(f"EXPECTED RESULT {step} : The prefix of the global IPv6 address of WAN interface should be /{WAN_IPV6_PREFIX_LENGTH}")
                if ipv6_prefix == WAN_IPV6_PREFIX_LENGTH:
                    print(f"ACTUAL RESULT {step} : The prefix of the global IPv6 address of WAN interface is /{WAN_IPV6_PREFIX_LENGTH}")
                    print("[TEST EXECUTION RESULT] : SUCCESS\n")
                    tdkTestObj.setResultStatus("SUCCESS")

                    #Get the IPv6 address of the WAN interface and verify whether it is valid
                    step += 1
                    tdkTestObj, ipv6_tr181, flag, step = getWANIPv6Address(tr181obj, step, validity_check=True)
                    if flag:
                        print(f"IPv6 address obtained from TR-181 DM is {ipv6_tr181}")

                        #Compare the IPv6 address obtained from TR-181 DM and the IPv6 address obtained from the WAN interface
                        step += 1
                        print(f"\nTEST STEP {step} : Compare the IPv6 address obtained from TR-181 DM and the IPv6 address obtained from the WAN interface")
                        print(f"EXPECTED RESULT {step} : The IPv6 address obtained from TR-181 DM and the IPv6 address obtained from the WAN interface should be same")
                        if ipv6_addr == ipv6_tr181:
                            print(f"ACTUAL RESULT {step} : The IPv6 address obtained from TR-181 DM and the IPv6 address obtained from the WAN interface are same. IPv6 address from TR-181 DM is {ipv6_tr181} and IPv6 address from WAN interface is {ipv6_addr}")
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("[TEST EXECUTION RESULT] : SUCCESS\n")
                        else:
                            print(f"ACTUAL RESULT {step} : The IPv6 address obtained from TR-181 DM and the IPv6 address obtained from the WAN interface are NOT same. IPv6 address from TR-181 DM is {ipv6_tr181} and IPv6 address from WAN interface is {ipv6_addr}")
                            tdkTestObj.setResultStatus("FAILURE")
                            print("[TEST EXECUTION RESULT] : FAILURE\n")
                    else:
                        print("Failed to get the IPv6 address using Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6")
                else:
                    print(f"ACTUAL RESULT {step} : The prefix of the global IPv6 address of WAN interface is NOT /{WAN_IPV6_PREFIX_LENGTH}. Prefix is {ipv6_prefix}")
                    print("[TEST EXECUTION RESULT] : FAILURE\n")
                    tdkTestObj.setResultStatus("FAILURE")
            else:
                print("Failed to get the prefix of the ip address")
        else:
            print("WAN interface does not have inet6 address with global scope")
    else:
        print("Failed to get the WAN interface name")

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
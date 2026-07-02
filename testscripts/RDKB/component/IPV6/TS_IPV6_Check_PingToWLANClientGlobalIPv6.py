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

tr181obj.configureTestCase(ip,port,'TS_IPV6_Check_PingToWLANClientGlobalIPv6')
sysobj.configureTestCase(ip,port,'TS_IPV6_Check_PingToWLANClientGlobalIPv6')

# Get the result of connection with test component and DUT
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

expectedresult = "SUCCESS"

if expectedresult in loadmodulestatus_tr181.upper() and expectedresult in loadmodulestatus_sys.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    # Check whether WAN Interface has global IPv6 address
    step = 1
    interface = getWAN_Interface(tr181obj, step)

    if interface != "":
        print("WAN interface is obtained successfully")
        step += 1
        flag = verifyIPv6Address(sysobj, interface, step)

        if flag:
            print("WAN interface has inet6 address with global scope")

            #Check whether the LAN interface has global IPv6 address
            step += 1
            interface = DUT_LAN_INTERFACE

            step += 1
            flag = verifyIPv6Address(sysobj, interface, step)

            if flag:
                print("WLAN interface has inet6 address with global scope")

                #Get the index of the active WLAN client
                step += 1
                index, step = getActiveClientIndex(tr181obj, LAYER1_INTERFACE_WLAN, step)

                if index is not None:
                    #Get the IPv6 address of the WLAN interface
                    step += 1
                    print(f"\nTEST STEP {step} : Get the IPv6 address of the WLAN client")
                    print(f"EXPECTED RESULT {step} : Should get the IPv6 address of the WLAN client")
                    tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
                    actualresult, ipv6_address = getTR181Value(tdkTestObj, f"Device.Hosts.Host.{index}.IPv6Address.3.IPAddress")
                    if expectedresult in actualresult and ipv6_address != "":
                        print(f"ACTUAL RESULT {step} : Successfully got the IPv6 address of the WLAN client. Details : {ipv6_address}")
                        print("[TEST EXECUTION RESULT] : SUCCESS\n")
                        tdkTestObj.setResultStatus("SUCCESS")

                        #Ping the WLAN client from the DUT using the IPv6 address obtained
                        step += 1
                        print("Pinging WLAN client from the DUT using the IPv6 address obtained")
                        connectivity_flag = checkInternetConnectivity(sysobj, ipv6_address, PING_COUNT, step)

                        if connectivity_flag:
                            print("Successfully pinged the WLAN client from the DUT using the IPv6 address obtained")
                        else:
                            print("Failed to ping the WLAN client from the DUT using the IPv6 address obtained")
                    else:
                        print(f"ACTUAL RESULT {step} : Failed to get the IPv6 address of the WLAN client")
                        print("[TEST EXECUTION RESULT] : FAILURE\n")
                        tdkTestObj.setResultStatus("FAILURE")
            else:
                print("LAN interface does not have inet6 address with global scope")
        else:
            print("WAN interface does not have inet6 address with global scope")
    else:
        print("Failed to get the WAN interface name.")

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
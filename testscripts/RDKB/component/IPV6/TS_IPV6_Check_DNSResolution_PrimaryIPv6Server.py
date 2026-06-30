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
import ipaddress

# Test component to be tested
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

tr181obj.configureTestCase(ip,port,'TS_IPV6_Check_DNSResolution_PrimaryIPv6Server')
sysobj.configureTestCase(ip,port,'TS_IPV6_Check_DNSResolution_PrimaryIPv6Server')

# Get the result of connection with test component and DUT
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

expectedresult = "SUCCESS"

if expectedresult in loadmodulestatus_tr181.upper() and expectedresult in loadmodulestatus_sys.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    # Ensure the DUT has IPv6 WAN IP Address.
    step = 1
    tdkTestObj, ipv6_tr181, flag, step = getWANIPv6Address(tr181obj, step)
    if flag:
        print(f"The DUT has IPv6 WAN IP Address: {ipv6_tr181}")

        #Get the IPv6 Primary DNS server address.
        step += 1
        tdkTestObj, primary_dns = getIPv6DNSServerAddresses(tr181obj, step, type = "Primary")
        if primary_dns != "":
            print(f"Primary IPv6 DNS server address is present on the DUT: {primary_dns}")

            #Resolve a known domain via Primary DNS server.
            step += 1
            tdkTestObj, flag, resolved_ip = resolveDomainUsingDNS(sysobj, DOMAIN_NAME, primary_dns, step)
            if flag:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"TEST EXECUTION RESULT : SUCCESS")
                print(f"Successfully resolved the domain {DOMAIN_NAME} using Primary DNS server {primary_dns}")

                #Validae whether the resolved IP address is a valid IPv6 address.
                step += 1
                is_valid_ipv6 = False
                print(f"\nTEST STEP {step}: Validate whether the resolved IP address is a valid IPv6 address")
                print(f"EXPECTED RESULT {step}: The resolved IP address should be a valid IPv6 address")
                try:
                    ipaddress.IPv6Address(resolved_ip)
                    is_valid_ipv6 = True
                except ipaddress.AddressValueError:
                    is_valid_ipv6 = False
                if is_valid_ipv6:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: The resolved IP address {resolved_ip} is a valid IPv6 address")
                    print(f"TEST EXECUTION RESULT : SUCCESS\n")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: The resolved IP address {resolved_ip} is NOT a valid IPv6 address")
                    print(f"TEST EXECUTION RESULT : FAILURE\n")

            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"TEST EXECUTION RESULT : FAILURE")
                print(f"Failed to resolve the domain {DOMAIN_NAME} using Primary DNS server {primary_dns}")
    else:
        print("The DUT does not have IPv6 WAN IP Address. Exiting the test.")

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
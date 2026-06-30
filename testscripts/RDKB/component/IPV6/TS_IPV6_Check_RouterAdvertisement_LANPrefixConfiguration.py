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

tr181obj.configureTestCase(ip,port,'TS_IPV6_Check_RouterAdvertisement_LANPrefixConfiguration')
sysobj.configureTestCase(ip,port,'TS_IPV6_Check_RouterAdvertisement_LANPrefixConfiguration')

# Get the result of connection with test component and DUT
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

expectedresult = "SUCCESS"

if expectedresult in loadmodulestatus_tr181.upper() and expectedresult in loadmodulestatus_sys.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    step = 1
    #Check whether Router Advertisement is enabled and ensure it is true
    print(f"\nTEST STEP {step} : Check whether Router Advertisement is enabled")
    print(f"EXPECTED RESULT {step} : Router Advertisement should be enabled")
    tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
    actualresult, ra_status = getTR181Value(tdkTestObj, "Device.RouterAdvertisement.Enable")
    if expectedresult in actualresult and ra_status != "":
        print(f"ACTUAL RESULT {step} : Router Advertisement status is {ra_status}")
        tdkTestObj.setResultStatus("SUCCESS")
        print("[TEST EXECUTION RESULT] : SUCCESS\n")

        #Set the Router Advertisement status to true if it is not already true
        flag = True
        if ra_status.lower() != "true":
            step += 1
            print(f"\nTEST STEP {step} : Set the Router Advertisement status to true")
            print(f"EXPECTED RESULT {step} : Router Advertisement status should be set to true")
            tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Set')
            actualresult, details = setTR181Value(tdkTestObj, "Device.RouterAdvertisement.Enable", "true", "boolean")
            if expectedresult in actualresult:
                print(f"ACTUAL RESULT {step} : Router Advertisement status set to true successfully. Details : {details}")
                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS\n")
            else:
                flag = False
                print(f"ACTUAL RESULT {step} : Failed to set Router Advertisement status to true. Details : {details}")
                tdkTestObj.setResultStatus("FAILURE")
                print("[TEST EXECUTION RESULT] : FAILURE\n")
        if flag:
            #Get the IPv6 prefix configured for advertisement.
            step += 1
            print(f"\nTEST STEP {step} : Get the IPv6 prefix configured for advertisement")
            print(f"EXPECTED RESULT {step} : Should get the IPv6 prefix configured for advertisement")
            tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
            actualresult, details = getTR181Value(tdkTestObj, "Device.RouterAdvertisement.InterfaceSetting.1.Prefixes")
            print("Value of Device.RouterAdvertisement.InterfaceSetting.1.Prefixes is : ", details)
            ipv6_prefix = details.split("/")[1] if "/" in details else ""
            if expectedresult in actualresult and ipv6_prefix != "":
                print(f"ACTUAL RESULT {step} : IPv6 prefix is {ipv6_prefix}")
                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS\n")

                # Get the interface used for Router Advertisement
                step += 1
                print(f"\nTEST STEP {step} : Get the interface used for Router Advertisement")
                print(f"EXPECTED RESULT {step} : Should get the interface used for Router Advertisement")
                tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
                actualresult, interface = getTR181Value(tdkTestObj, "Device.RouterAdvertisement.InterfaceSetting.1.Interface")
                if expectedresult in actualresult and interface != "":
                    print(f"ACTUAL RESULT {step} : Interface used for Router Advertisement is {interface}")
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("[TEST EXECUTION RESULT] : SUCCESS\n")

                    #Get the prefix of the IPv6 address configured on the interface
                    step += 1
                    print("Obtaining the prefix of the IPv6 address configured on the interface used for Router Advertisement")
                    tdkTestObj, ipv6_addr, prefix, flag = extractIPv6PrefixandAddress(sysobj, interface, step)
                    if flag:
                        print(f"Successfully obtained the prefix of the IPv6 address configured on the interface used for Router Advertisement. IPv6 prefix is {prefix}")

                        #Check whether the prefix of the IPv6 address configured on the interface matches with the prefix configured for advertisement
                        step += 1
                        print(f"\nTEST STEP {step} : Check whether the prefix of the IPv6 address configured on the interface matches with the prefix configured for advertisement")
                        print(f"EXPECTED RESULT {step} : The prefix of the IPv6 address configured on the interface should match with the prefix configured for advertisement")
                        if int(ipv6_prefix) == int(prefix):
                            print(f"ACTUAL RESULT {step} : The prefix of the IPv6 address configured on the interface matches with the prefix configured for advertisement")
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("[TEST EXECUTION RESULT] : SUCCESS\n")
                        else:
                            print(f"ACTUAL RESULT {step} : The prefix of the IPv6 address configured on the interface does not match with the prefix configured for advertisement")
                            tdkTestObj.setResultStatus("FAILURE")
                            print("[TEST EXECUTION RESULT] : FAILURE\n")
                    else:
                        print(f"Failed to obtain the prefix of the IPv6 address configured on the interface used for Router Advertisement. Details : {ipv6_addr}")
                else:
                    print(f"ACTUAL RESULT {step} : Failed to get interface used for Router Advertisement. Details : {interface}")
                    tdkTestObj.setResultStatus("FAILURE")
                    print("[TEST EXECUTION RESULT] : FAILURE\n")
            else:
                print(f"ACTUAL RESULT {step} : Failed to get the IPv6 prefix configured for advertisement. Details : {details}")
                tdkTestObj.setResultStatus("FAILURE")
                print("[TEST EXECUTION RESULT] : FAILURE\n")
        else:
            print(f"Router Advertisement status is not enabled and failed to set it to true. Hence cannot proceed with the test")
    else:
        print(f"ACTUAL RESULT {step} : Failed to get the Router Advertisement status. Details : {ra_status}")
        tdkTestObj.setResultStatus("FAILURE")
        print("[TEST EXECUTION RESULT] : FAILURE\n")
    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
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

tr181obj.configureTestCase(ip,port,'TS_IPV6_Check_DHCPv6ClientStatus')
sysobj.configureTestCase(ip,port,'TS_IPV6_Check_DHCPv6ClientStatus')

# Get the result of connection with test component and DUT
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

expectedresult = "SUCCESS"

if expectedresult in loadmodulestatus_tr181.upper() and expectedresult in loadmodulestatus_sys.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    step = 1
    #Get the value of Device.DHCPv6.Client.1.Enable and validate it is true
    print(f"\nTEST STEP {step} : Get the value of Device.DHCPv6.Client.1.Enable")
    print(f"EXPECTED RESULT {step} : Should get the value of Device.DHCPv6.Client.1.Enable successfully and it should be true")
    tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
    actualresult, dhcpv6_client_enable = getTR181Value(tdkTestObj, "Device.DHCPv6.Client.1.Enable")
    if expectedresult in actualresult and dhcpv6_client_enable == "true":
        print(f"ACTUAL RESULT {step}: Successfully got the value of Device.DHCPv6.Client.1.Enable and it is {dhcpv6_client_enable}")
        tdkTestObj.setResultStatus("SUCCESS")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        #Get the value of Device.DHCPv6.Client.1.Status and validate it is "Enabled"
        step += 1
        print(f"\nTEST STEP {step} : Get the value of Device.DHCPv6.Client.1.Status")
        print(f"EXPECTED RESULT {step} : Should get the value of Device.DHCPv6.Client.1.Status successfully and it should be Enabled")
        tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
        actualresult, dhcpv6_client_status = getTR181Value(tdkTestObj, "Device.DHCPv6.Client.1.Status")
        if expectedresult in actualresult and dhcpv6_client_status == "Enabled":
            print(f"ACTUAL RESULT {step}: Successfully got the value of Device.DHCPv6.Client.1.Status and it is {dhcpv6_client_status}")
            tdkTestObj.setResultStatus("SUCCESS")
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            print(f"ACTUAL RESULT {step}: Failed to get the value of Device.DHCPv6.Client.1.Status or it is not Enabled. Value is {dhcpv6_client_status}")
            tdkTestObj.setResultStatus("FAILURE")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        print(f"ACTUAL RESULT {step}: Failed to get the value of Device.DHCPv6.Client.1.Enable or it is not true. Value is {dhcpv6_client_enable}")
        tdkTestObj.setResultStatus("FAILURE")
        print("[TEST EXECUTION RESULT] : FAILURE")
    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
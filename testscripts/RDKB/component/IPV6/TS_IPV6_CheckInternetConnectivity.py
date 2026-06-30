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
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

tr181obj.configureTestCase(ip,port,'TS_IPV6_CheckInternetConnectivity')
sysobj.configureTestCase(ip,port,'TS_IPV6_CheckInternetConnectivity')

# Get the result of connection with test component and DUT
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

expectedresult = "SUCCESS"

if expectedresult in loadmodulestatus_tr181.upper() and expectedresult in loadmodulestatus_sys.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    #Get the IPv6 address of the WAN interface
    step = 1
    tdkTestObj, ipv6_tr181, flag, step = getWANIPv6Address(tr181obj, step, validity_check=True)
    if flag:
        print(f"IPv6 address obtained from TR-181 DM is {ipv6_tr181}")

        # Check whether DUT has internet connectivity using the obtained IPv6 address
        step += 1
        print("Checking IPv6 internet connectivity")
        connectivity_flag = checkInternetConnectivity(sysobj, HOST_NAME, PING_COUNT, step)
        if connectivity_flag:
            print(f"Confirmed the availability of internet.")
        else:
            print(f"Internet connectivity is not available")

    else:
        print("Failed to get the IPv6 address using Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6")

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
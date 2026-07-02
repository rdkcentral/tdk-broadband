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

tr181obj.configureTestCase(ip,port,'TS_IPV6_CheckIPV6Address_AfterReboot')
sysobj.configureTestCase(ip,port,'TS_IPV6_CheckIPV6Address_AfterReboot')

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

        #Reboot the DUT
        print("\nRebooting the DUT")
        sysobj.initiateReboot()
        sleep(300)

        #Get the IPv6 address of the WAN interface after reboot
        step += 1
        print("\nGetting the IPv6 address of the WAN interface after reboot")
        tdkTestObj, ipv6_tr181_after_reboot, flag, step = getWANIPv6Address(tr181obj, step, validity_check=True)
        if flag:
            print(f"IPv6 address obtained from TR-181 DM after reboot is {ipv6_tr181_after_reboot}")
        else:
            print("Failed to get the IPv6 address using Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 after reboot")

    else:
        print("Failed to get the IPv6 address using Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6")

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
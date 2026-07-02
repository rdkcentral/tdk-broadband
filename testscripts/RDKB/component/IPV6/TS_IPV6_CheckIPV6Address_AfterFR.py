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

tr181obj.configureTestCase(ip,port,'TS_IPV6_CheckIPV6Address_AfterFR')
sysobj.configureTestCase(ip,port,'TS_IPV6_CheckIPV6Address_AfterFR')

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

        step += 1
        #Factory Reset the device
        print(f"\nTEST STEP {step}: Initiate Factory Reset on the DUT")
        print(f"EXPECTED RESULT {step}: Factory Reset should be triggered successfully")
        sysobj.saveCurrentState()

        tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly')
        actualresult, details = setTR181Value(tdkTestObj, "Device.X_CISCO_COM_DeviceControl.FactoryReset", "Router,Wifi,VoIP,Dect,MoCA", "string")

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: Factory Reset triggered successfully. Details : {details}")
            print("[TEST EXECUTION RESULT] : SUCCESS")

            sleep(300)
            #Restore the device state saved before FR
            sysobj.restorePreviousStateAfterReboot()
            print("Device is UP after Factory Reset...")

            #Get the IPv6 address of the WAN interface after Factory Reset
            step += 1
            print("\nGetting the IPv6 address of the WAN interface after Factory Reset")
            tdkTestObj, ipv6_tr181_after_reset, flag, step = getWANIPv6Address(tr181obj, step, validity_check=True)
            if flag:
                print(f"IPv6 address obtained from TR-181 DM after Factory Reset is {ipv6_tr181_after_reset}")
            else:
                print("Failed to get the IPv6 address using Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 after Factory Reset")

        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Failed to trigger Factory Reset. Details : {details}")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        print("Failed to get the IPv6 address using Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6")

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
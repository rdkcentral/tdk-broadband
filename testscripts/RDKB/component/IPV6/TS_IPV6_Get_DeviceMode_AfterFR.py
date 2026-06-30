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

tr181obj.configureTestCase(ip,port,'TS_IPV6_Get_DeviceMode_AfterFR')
sysobj.configureTestCase(ip,port,'TS_IPV6_Get_DeviceMode_AfterFR')

# Get the result of connection with test component and DUT
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

expectedresult = "SUCCESS"

if expectedresult in loadmodulestatus_tr181.upper() and expectedresult in loadmodulestatus_sys.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    step = 1
    print("\nTEST STEP %d : Trigger Factory Reset on the DUT" %step)
    print("EXPECTED RESULT %d : Factory Reset should be triggered successfully" %step)
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

        step += 1
        #Check whether the device is IPv6 capable
        print(f"\nTEST STEP {step} : Check whether the device is IPv6 capable.")
        print(f"EXPECTED RESULT {step} : Should get the IPv6 capability of the device")
        tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
        actualresult, ipv6_capable = getTR181Value(tdkTestObj, "Device.IP.IPv6Capable")
        if expectedresult in actualresult and ipv6_capable == "true":
            print(f"ACTUAL RESULT {step} : Successfully got the IPv6 capability of the device using Device.IP.IPv6Capable. IPv6 capable is {ipv6_capable}")
            tdkTestObj.setResultStatus("SUCCESS")
            print("[TEST EXECUTION RESULT] : SUCCESS\n")

            #Check whether IPV6 is enabled and ensure it is true
            step += 1
            print(f"\nTEST STEP {step} : Check whether IPv6 is enabled on the device")
            print(f"EXPECTED RESULT {step} : Should get the IPv6 enable status of the device")
            tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
            actualresult, ipv6_enable = getTR181Value(tdkTestObj, "Device.IP.IPv6Enable")
            if expectedresult in actualresult and ipv6_enable == "true":
                print(f"ACTUAL RESULT {step} : Successfully got the IPv6 enable status of the device using Device.IP.IPv6Enable. IPv6 enable is {ipv6_enable}")
                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS\n")

                #Validate whether IPv6 Status is enabled - Device.IP.IPv6Status
                step += 1
                print(f"\nTEST STEP {step} : Validate whether IPv6 Status is enabled.")
                print(f"EXPECTED RESULT {step} : Should get the IPv6 Status of the device")
                tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
                actualresult, ipv6_status = getTR181Value(tdkTestObj, "Device.IP.IPv6Status")
                if expectedresult in actualresult and ipv6_status == "Enabled":
                    print(f"ACTUAL RESULT {step} : Successfully got the IPv6 Status of the device. IPv6 Status is {ipv6_status}")
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("[TEST EXECUTION RESULT] : SUCCESS\n")

                    #Verify whether DUT has IPv6 WAN IP Address
                    step += 1
                    print("Verifying whether DUT has IPv6 WAN IP Address")
                    tdkTestObj, ipv6_tr181, flag, step = getWANIPv6Address(tr181obj, step)
                    if flag:
                        print("Successfully verified that DUT has IPv6 WAN IP Address")

                        #Get the default value of Device Mode - Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceMode
                        step += 1
                        print(f"\nTEST STEP {step} : Get the default value of Device Mode - Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceMode")
                        print(f"EXPECTED RESULT {step} : Should get the default value of Device Mode successfully")
                        tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
                        actualresult, device_mode = getTR181Value(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceMode")
                        if expectedresult in actualresult and device_mode == "Dualstack":
                            print(f"ACTUAL RESULT {step} : Successfully got the value of Device Mode - Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceMode. Device Mode is {device_mode}")
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("[TEST EXECUTION RESULT] : SUCCESS\n")
                        else:
                            print(f"ACTUAL RESULT {step}: Failed to get the value of Device Mode - Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceMode. Device Mode is {device_mode}")
                            tdkTestObj.setResultStatus("FAILURE")
                            print("[TEST EXECUTION RESULT] : FAILURE\n")
                    else:
                        print("Failed to verify that DUT has IPv6 WAN IP Address")
                else:
                    print(f"ACTUAL RESULT {step}: Failed to get the IPv6 Status of the device. IPv6 Status is {ipv6_status}")
                    tdkTestObj.setResultStatus("FAILURE")
                    print("[TEST EXECUTION RESULT] : FAILURE\n")
            else:
                print(f"ACTUAL RESULT {step}: Failed to get the IPv6 enable status of the device using Device.IP.IPv6Enable. IPv6 enable is {ipv6_enable}")
                tdkTestObj.setResultStatus("FAILURE")
                print("[TEST EXECUTION RESULT] : FAILURE\n")
        else:
            print(f"ACTUAL RESULT {step}: Failed to get the IPv6 capability of the device using Device.IP.IPv6Capable. IPv6 capable is {ipv6_capable}")
            print("[TEST EXECUTION RESULT] : FAILURE\n")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to trigger Factory Reset. Details : {details}")
        print("[TEST EXECUTION RESULT] : FAILURE")
    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
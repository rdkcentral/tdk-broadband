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

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

tr181obj.configureTestCase(ip,port,'TS_IPV6_Get_WANIPv6Address_BridgeMode')

# Get the result of connection with test component and DUT
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()

expectedresult = "SUCCESS"

if expectedresult in loadmodulestatus_tr181.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")

    #Get the initial LAN Mode - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
    step = 1
    print(f"\nTEST STEP {step} : Get the initial LAN Mode - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    print(f"EXPECTED RESULT {step} : Should get the initial LAN Mode successfully")
    tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get')
    actualresult, initial_lan_mode = getTR181Value(tdkTestObj, "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    if expectedresult in actualresult and initial_lan_mode != "":
        print(f"ACTUAL RESULT {step} : Successfully got the initial LAN Mode - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode. Initial LAN Mode is {initial_lan_mode}")
        tdkTestObj.setResultStatus("SUCCESS")
        print("[TEST EXECUTION RESULT] : SUCCESS\n")

        #Change the LAN Mode to Bridge-Static
        step += 1
        print(f"\nTEST STEP {step} : Change the LAN Mode to Bridge-Static")
        print(f"EXPECTED RESULT {step} : LAN Mode should be changed to Bridge-Static successfully")
        tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Set')
        actualresult, details = setTR181Value(tdkTestObj, "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode", "bridge-static", "string")
        if expectedresult in actualresult:
            print(f"ACTUAL RESULT {step} : Successfully changed the LAN Mode to Bridge-Static. Details : {details}")
            tdkTestObj.setResultStatus("SUCCESS")
            print("[TEST EXECUTION RESULT] : SUCCESS\n")

            #Get the IPv6 address of the WAN interface on bridge-static mode and verify whether it is valid
            step += 1
            print("Obtaining the IPv6 address of the WAN interface on bridge-static mode and verifying whether it is valid")
            tdkTestObj, ipv6_tr181, flag, step = getWANIPv6Address(tr181obj, step, validity_check=True)
            if flag:
                print("Obtained valid IPv6 address of the WAN interface on bridge-static mode.")
            else:
                print("Failed to get valid IPv6 address of the WAN interface on bridge-static mode.")

            #Revert the LAN Mode to initial value
            step += 1
            print(f"\nTEST STEP {step} : Revert the LAN Mode to initial value - {initial_lan_mode}")
            print(f"EXPECTED RESULT {step} : LAN Mode should be reverted to initial value successfully")
            tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Set')
            actualresult, details = setTR181Value(tdkTestObj, "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode", initial_lan_mode, "string")
            if expectedresult in actualresult:
                print(f"ACTUAL RESULT {step} : Successfully reverted the LAN Mode to initial value - {initial_lan_mode}. Details : {details}")
                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS\n")
            else:
                print(f"ACTUAL RESULT {step}: Failed to revert the LAN Mode to initial value - {initial_lan_mode}. Details : {details}")
                tdkTestObj.setResultStatus("FAILURE")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Failed to change the LAN Mode to Bridge-Static. Details : {details}")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to get the initial LAN Mode - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
        print("[TEST EXECUTION RESULT] : FAILURE")
    tr181obj.unloadModule("tdkbtr181")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
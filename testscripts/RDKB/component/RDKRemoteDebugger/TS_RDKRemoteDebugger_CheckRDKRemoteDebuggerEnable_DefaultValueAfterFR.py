##########################################################################
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
from tdkbRRDUtility import *
from time import sleep

# Test component to be tested
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

tr181obj.configureTestCase(ip,port,'TS_RDKRemoteDebugger_CheckRDKRemoteDebuggerEnable_DefaultValueAfterFR')
sysobj.configureTestCase(ip,port,'TS_RDKRemoteDebugger_CheckRDKRemoteDebuggerEnable_DefaultValueAfterFR')
# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

if expectedresult in loadmodulestatus_tr181.upper() and expectedresult in loadmodulestatus_sys.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    step = 1
    #Factory Reset the device
    print("\nTEST STEP %d: Initiate Factory Reset on the DUT" %step)
    print("EXPECTED RESULT %d: Factory Reset should be triggered successfully" %step)
    sysobj.saveCurrentState()

    tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly')
    actualresult, details = setTR181Value(tdkTestObj, "Device.X_CISCO_COM_DeviceControl.FactoryReset", "Router,Wifi,VoIP,Dect,MoCA", "string")

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Factory Reset triggered successfully. Details : %s" %(step, details))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        sleep(300)
        #Restore the device state saved before reboot
        sysobj.restorePreviousStateAfterReboot()
        print("Device is UP after Factory Reset...")

        step += 1
        #Get the default value of RDKRemoteDebugger Enable
        tdkTestObj, get_flag, default_value = getRDKRemoteDebuggerEnable(tr181obj, step)
        if get_flag:
            print(f"Successfully got the default value of RDKRemoteDebugger Enable: {default_value}.")
        else:
            print("Failed to get the default value of RDKRemoteDebugger Enable")
    else:
        print("ACTUAL RESULT %d: Factory Reset could not be triggered. Details : %s" %(step, details))
        print("[TEST EXECUTION RESULT] : FAILURE")

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
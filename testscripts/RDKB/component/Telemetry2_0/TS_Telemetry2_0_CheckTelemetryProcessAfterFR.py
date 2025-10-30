##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2025 RDK Management
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
from tdkutility import *

# Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckTelemetryProcessAfterFR')
sysobj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckTelemetryProcessAfterFR')
# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus_sys.upper():
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1
    #Factory Reset the device
    print("\nTEST STEP %d: Initiate Factory Reset on the DUT" %step)
    print("EXPECTED RESULT %d: Factory Reset should be triggered successfully" %step)
    sysobj.saveCurrentState()

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_SetOnly')
    actualresult, details = setTR181Value(tdkTestObj, "Device.X_CISCO_COM_DeviceControl.FactoryReset", "Router,Wifi,VoIP,Dect,MoCA", "string")

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Factory Reset triggered successfully. Details : %s" %(step, details))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        #Restore the device state saved before reboot
        sysobj.restorePreviousStateAfterReboot()

        step += 1
        #Check if Telemetry2.0 process is running after Factory Reset
        print("\nTEST STEP %d: Check if Telemetry2.0 process is running after Factory Reset" %step)
        print("EXPECTED RESULT %d: Telemetry2.0 process should be running" %step)

        tdkTestObj = sysobj.createTestStep('ExecuteCmd')
        cmd = "pidof 'telemetry2_0'"
        actualresult,details = getPID(tdkTestObj, cmd)

        if expectedresult in actualresult and details != "":
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Telemetry2.0 process is running after Factory Reset. Details : %s" %(step, details))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Telemetry2.0 process is not running after Factory Reset. Details : %s" %(step, details))
            print("[TEST EXECUTION RESULT] : FAILURE")

    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Factory Reset triggering failed. Details : %s" %(step, details))
        print("[TEST EXECUTION RESULT] : FAILURE")
    print("\n")
    #Unload the modules loaded
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")


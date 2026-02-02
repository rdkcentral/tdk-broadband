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
from time import sleep

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1")
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_GetAsteriskServerAndTelcoVoiceManagerStatusAfterFR')
tr181obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_GetAsteriskServerAndTelcoVoiceManagerStatusAfterFR')
# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatustr181 = tr181obj.getLoadModuleResult()
if expectedresult in loadmodulestatus.upper() and expectedresult in loadmodulestatustr181.upper():
    obj.setLoadModuleStatus("SUCCESS")
    tr181obj.setLoadModuleStatus("SUCCESS")

    step = 1
    #Initiate Factory Reset
    print(f"\nTEST STEP {step}: Initiate Factory Reset on the DUT.")
    print(f"EXPECTED RESULT {step}: Factory Reset should be triggered successfully.")
    obj.saveCurrentState()
    tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly')
    actualresult, details = setTR181Value(tdkTestObj, "Device.X_CISCO_COM_DeviceControl.FactoryReset", "Router,Wifi,VoIP,Dect,MoCA", "string")
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Factory Reset triggered successfully. Details : {details}.")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        print("\nWaiting for 300 seconds for the device to be up...")
        sleep(300)
        #Restore the device state saved before reboot
        obj.restorePreviousStateAfterReboot()

        step += 1
        #Check the status of RdkTelcoVoiceManager.service
        print(f"\nTEST STEP {step}: Check the status of RdkTelcoVoiceManager.service.")
        print(f"EXPECTED RESULT {step}: RdkTelcoVoiceManager.service should be up and running.")
        command = "systemctl status RdkTelcoVoiceManager.service | grep Active | awk '{print $2}'"
        print(f"Command : {command}")
        tdkTestObj = obj.createTestStep('ExecuteCmd')
        actualresult, details = doSysutilExecuteCommand(tdkTestObj, command)
        if expectedresult in actualresult and details == "active":
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: RdkTelcoVoiceManager.service is up and running")
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            #Get the PID of RdkTelcoVoiceManager.service
            print(f"\nTEST STEP {step}: Get the PID of RdkTelcoVoiceManager.service.")
            print(f"EXPECTED RESULT {step}: Successfully obtained the PID of RdkTelcoVoiceManager.service.")
            tdkTestObj = obj.createTestStep('ExecuteCmd')
            actualresult, details = getPID(tdkTestObj, "telcovoice_manager")
            if expectedresult in actualresult and details !=0:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Successfully obtained the PID of RdkTelcoVoiceManager service. The pid is {details}.")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                #Check whether asterisk server is up by getting its PID
                step += 1
                print(f"\nTEST STEP {step}: Check whether Asterisk server is up by getting its PID.")
                print(f"EXPECTED RESULT {step}: Asterisk server should be up and running.")
                tdkTestObj = obj.createTestStep('ExecuteCmd')
                actualresult, details = getPID(tdkTestObj, "hal-voice-asterisk")
                if expectedresult in actualresult and details != "":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Asterisk server is up and running. The PID of asterisk server is {details}.")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Asterisk server is down. Failed to get the PID of Asterisk server.")
                    print("[TEST EXECUTION RESULT] : FAILURE")

            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Failed to get the PID of RdkTelcoVoiceManager service.")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Failed to get the status of RdkTelcoVoiceManager.service.")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to trigger Factory Reset. Details : {details}.")
        print("[TEST EXECUTION RESULT] : FAILURE")
    obj.unloadModule("sysutil")
    tr181obj.unloadModule("tdkbtr181")
else:
    print("\nFailed to load the modules")
    obj.setLoadModuleStatus("FAILURE")
    tr181obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

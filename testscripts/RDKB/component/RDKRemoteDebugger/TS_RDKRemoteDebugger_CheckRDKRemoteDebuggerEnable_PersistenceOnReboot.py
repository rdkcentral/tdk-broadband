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
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

sysobj.configureTestCase(ip,port,'TS_RDKRemoteDebugger_CheckRDKRemoteDebuggerEnable_PersistenceOnReboot')
tr181obj.configureTestCase(ip,port,'TS_RDKRemoteDebugger_CheckRDKRemoteDebuggerEnable_PersistenceOnReboot')
# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()

if expectedresult in loadmodulestatus_tr181.upper() and expectedresult in loadmodulestatus_sys.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    tr181obj.setLoadModuleStatus("SUCCESS")

    step = 1
    #Get the value of RDKRemoteDebugger Enable
    tdkTestObj, get_flag, initial_value = getRDKRemoteDebuggerEnable(tr181obj, step)
    if get_flag:
        print(f"Successfully got the initial value of RDKRemoteDebugger Enable: {initial_value}")

        # Set the value of RDKRemoteDebugger Enable to a different value
        step += 1
        if initial_value.lower() == "true":
            pre_reboot_value = "false"
        else:
            pre_reboot_value = "true"
        set_flag = 0
        print(f"Setting the value of RDKRemoteDebugger Enable to {pre_reboot_value}.")
        set_flag = setRDKRemoteDebuggerEnable(tr181obj, pre_reboot_value, step)

        if set_flag:
            print(f"Successfully set the value of RDKRemoteDebugger Enable to {pre_reboot_value}.")
            print("\n********************Rebooting the Device********************")
            sysobj.initiateReboot()
            print("Sleeping for 300s")
            sleep(300)
            print("\n********************Device Up after reboot********************")

            #Get the value of RDKRemoteDebugger Enable after reboot
            step += 1
            tdkTestObj, get_flag, post_reboot_value = getRDKRemoteDebuggerEnable(tr181obj, step)
            if get_flag:
                print(f"Successfully got the value of RDKRemoteDebugger Enable after reboot.")

                #Compare the values of RDKRemoteDebugger Enable before and after reboot and check persistence
                step += 1
                print(f"\nTEST STEP {step} : Check whether the value of RDKRemoteDebugger Enable is persistent across reboot")
                print(f"EXPECTED RESULT {step} : The value of RDKRemoteDebugger Enable should be persistent across reboot")
                if pre_reboot_value.lower() == post_reboot_value.lower():
                    print(f"ACTUAL RESULT {step} : The value of RDKRemoteDebugger Enable is persistent across reboot. Value before reboot: {pre_reboot_value} and Value after reboot: {post_reboot_value}")
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"TEST EXECUTION RESULT : SUCCESS")
                else:
                    print(f"ACTUAL RESULT {step} : The value of RDKRemoteDebugger Enable is not persistent across reboot. Value before reboot: {pre_reboot_value} and Value after reboot: {post_reboot_value}")
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"TEST EXECUTION RESULT : FAILURE")

                #Revert the value of RDKRemoteDebugger Enable to its initial value
                step += 1
                print(f"\nReverting the value of RDKRemoteDebugger Enable to its initial value {initial_value}.")
                set_flag = setRDKRemoteDebuggerEnable(tr181obj, initial_value, step)
                if set_flag:
                    print(f"Successfully reverted the value of RDKRemoteDebugger Enable to its initial value {initial_value}.")
                else:
                    print(f"Failed to revert the value of RDKRemoteDebugger Enable to its initial value {initial_value}.")
            else:
                print(f"Failed to get the value of RDKRemoteDebugger Enable after reboot")
        else:
            print(f"Failed to set the value of RDKRemoteDebugger Enable to {pre_reboot_value}.")
    else:
        print("Failed to get the initial value of RDKRemoteDebugger Enable")

    sysobj.unloadModule("sysutil")
    tr181obj.unloadModule("tdkbtr181")

else:
    print("\nFailed to load the module")
    sysobj.setLoadModuleStatus("FAILURE")
    tr181obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
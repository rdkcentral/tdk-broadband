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

# Test component to be tested
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

tr181obj.configureTestCase(ip,port,'TS_RDKRemoteDebugger_ValidateRDKRemoteDebuggerEnable_Toggling')
# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()

if expectedresult in loadmodulestatus_tr181.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")

    step = 1
    #Get the value of RDKRemoteDebugger Enable
    tdkTestObj, get_flag, initial_value = getRDKRemoteDebuggerEnable(tr181obj, step)
    if get_flag:
        print(f"Successfully got the initial value of RDKRemoteDebugger Enable.")

        #Set the value of RDKRemoteDebugger Enable to the opposite of its initial value
        step += 1
        new_value = "false" if initial_value.lower() == "true" else "true"
        set_flag = setRDKRemoteDebuggerEnable(tr181obj, new_value, step)
        if set_flag:
            print(f"Successfully set the value of RDKRemoteDebugger Enable to {new_value}.")
            #Revert the value of RDKRemoteDebugger Enable to its initial value
            print("\nReverting the value of RDKRemoteDebugger Enable to its initial value.")
            step += 1
            set_flag = setRDKRemoteDebuggerEnable(tr181obj, initial_value, step)
            if set_flag:
                print("Successfully reverted the value of RDKRemoteDebugger Enable to its initial value.")
            else:
                print("Failed to revert the value of RDKRemoteDebugger Enable to its initial value.")

        else:
            print(f"Failed to set the value of RDKRemoteDebugger Enable to {new_value}.")

    else:
        print("Failed to get the initial value of RDKRemoteDebugger Enable")


    tr181obj.unloadModule("tdkbtr181")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
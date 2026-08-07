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
from tdkutility import *

# Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

sysobj.configureTestCase(ip,port,'TS_IPV6_CheckDibblerServerStatus')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()

expectedresult = "SUCCESS"

if expectedresult in loadmodulestatus_sys.upper():
    sysobj.setLoadModuleStatus("SUCCESS")

    #Check whether the dibbler server is running using ps command
    step = 1
    print(f"\nTEST STEP {step} : Check whether the dibbler server process is active via ps command")
    print(f"EXPECTED RESULT {step} : Dibbler server process should be active")
    command = "ps | grep dibbler-server | grep -v grep"
    print(f"Command: {command}")
    tdkTestObj = sysobj.createTestStep('ExecuteCmd')
    actualresult, details = doSysutilExecuteCommand(tdkTestObj, command)
    print(f"Command output: {details}")
    if expectedresult in actualresult and details != "":
        print(f"ACTUAL RESULT {step} : Dibbler server is active")
        tdkTestObj.setResultStatus("SUCCESS")
        print("[TEST EXECUTION RESULT] : SUCCESS\n")

        #Check the dibbler-server status and validate it is RUNNING and get its PID
        step += 1
        print(f"TEST STEP {step} : Check the dibbler-server status and validate it is RUNNING and get its PID")
        print(f"EXPECTED RESULT {step} : Dibbler-server status should be RUNNING and PID should be obtained")
        command = "dibbler-server status | grep 'Dibbler server'"
        print(f"Command: {command}")
        tdkTestObj = sysobj.createTestStep('ExecuteCmd')
        actualresult, details = doSysutilExecuteCommand(tdkTestObj, command)
        print(f"Command output: {details}")
        pid = details.split("pid=")[1].strip() if "pid=" in details else ""
        if expectedresult in actualresult and 'Dibbler server: RUNNING' in details and pid != "":
            print(f"ACTUAL RESULT {step} : Successfully checked the dibbler-server status and obtained its PID")
            tdkTestObj.setResultStatus("SUCCESS")
            print("[TEST EXECUTION RESULT] : SUCCESS\n")
        else:
            print(f"ACTUAL RESULT {step} : Failed to check the dibbler-server status and obtain its PID")
            tdkTestObj.setResultStatus("FAILURE")
            print("[TEST EXECUTION RESULT] : FAILURE\n")
    else:
        print(f"ACTUAL RESULT {step} : Dibbler server is not active")
        tdkTestObj.setResultStatus("FAILURE")
        print("[TEST EXECUTION RESULT] : FAILURE\n")

    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
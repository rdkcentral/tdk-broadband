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
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

tr181obj.configureTestCase(ip,port,'TS_RDKRemoteDebugger_StaticProfile_ValidateDebugReportGeneration')
sysobj.configureTestCase(ip,port,'TS_RDKRemoteDebugger_StaticProfile_ValidateDebugReportGeneration')
# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

if expectedresult in loadmodulestatus_tr181.upper() and expectedresult in loadmodulestatus_sys.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    print("Pre-requisite : Install the Download Server and host the static profile in Download server path  ")
    step = 1
    # Get the value of RDKRemoteDebugger IssueType
    tdkTestObj, get_flag, initial_value = getRDKRemoteDebuggerIssueType(tr181obj, step)
    if get_flag:
        print("Successfully obtained the value of RDKRemoteDebugger IssueType")

        step += 1
        # Set the value of RDKRemoteDebugger IssueType
        set_flag = setRDKRemoteDebuggerIssueType(tr181obj, step, "Device.Uptime")
        if set_flag:
            print("Successfully set the value of RDKRemoteDebugger IssueType.")

            step += 1
            # Check if the static debug report is generated
            tdkTestObj, report_flag = checkDebugReportGenerated(sysobj, "static", step)
            if report_flag:
                tdkTestObj.setResultStatus("SUCCESS")
                print("TEST EXECUTION RESULT : SUCCESS")
                print("The static debug report is generated successfully.")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("TEST EXECUTION RESULT : FAILURE")
                print("The static debug report is not generated as expected.")

            # Revert the value of RDKRemoteDebugger IssueType to its initial value
            print("\nReverting the value of RDKRemoteDebugger IssueType to its initial value.")
            step += 1
            set_flag = setRDKRemoteDebuggerIssueType(tr181obj, step, initial_value)
            if set_flag:
                print("Successfully reverted the value of RDKRemoteDebugger IssueType to its initial value.")
            else:
                print("Failed to revert the value of RDKRemoteDebugger IssueType to its initial value.")

        else:
            print("Failed to set the value of RDKRemoteDebugger IssueType.")
    else:
        print("Failed to get RDKRemoteDebugger IssueType")

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
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

tr181obj.configureTestCase(ip,port,'TS_RDKRemoteDebugger_StaticProfile_ValidateDebugReportGeneration')
sysobj.configureTestCase(ip,port,'TS_RDKRemoteDebugger_StaticProfile_ValidateDebugReportGeneration')
# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
issueType = "Device.Uptime"
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

if expectedresult in loadmodulestatus_tr181.upper() and expectedresult in loadmodulestatus_sys.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    step = 1
    profile_type = "static"
    # Prerequisite checks
    prereq_flag, revert_flag, step = checkRRDPrerequisites(tr181obj, sysobj, step, profile_type)
    if prereq_flag:
        print("Successfully completed the prerequisite checks.")
        step += 1
        # Get the value of RDKRemoteDebugger IssueType
        tdkTestObj, get_flag, initial_value = getRDKRemoteDebuggerIssueType(tr181obj, step)
        if get_flag:
            print("Successfully obtained the value of RDKRemoteDebugger IssueType")

            step += 1
            # Set the value of RDKRemoteDebugger IssueType
            set_flag = setRDKRemoteDebuggerIssueType(tr181obj, step, issueType)
            if set_flag:
                print("Successfully set the value of RDKRemoteDebugger IssueType.")

                sleep(5)
                step += 1
                # Check whether json file is available in the designated location
                tdkTestObj, file_flag = checkJsonProfileAvailable(sysobj, profile_type, issueType, step)
                if file_flag:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("TEST EXECUTION RESULT : SUCCESS")
                    print(f"The {profile_type} json profile is available as expected.")

                    # Check if the debug report is generated
                    step += 1
                    tdkTestObj, report_flag = checkDebugReportGenerated(sysobj, profile_type, step)
                    if report_flag:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("TEST EXECUTION RESULT : SUCCESS")
                        print(f"The {profile_type} debug report is generated successfully.")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("TEST EXECUTION RESULT : FAILURE")
                        print(f"The {profile_type} debug report is not generated as expected.")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("TEST EXECUTION RESULT : FAILURE")
                    print(f"The {profile_type} json profile is not available as expected.")

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
    else:
        print("Failed to complete the prerequisite checks. Cannot proceed with the test execution.")
    if revert_flag:
        #Revert the value of RDKRemoteDebugger Enable to its initial value
        step += 1
        value = "false"
        print(f"\nReverting the value of RDKRemoteDebugger Enable to its initial value {value}.")
        set_flag = setRDKRemoteDebuggerEnable(tr181obj, value, step)
        if set_flag:
            print(f"Successfully reverted the value of RDKRemoteDebugger Enable to its initial value {value}.")
        else:
            print(f"Failed to revert the value of RDKRemoteDebugger Enable to its initial value {value}.")

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

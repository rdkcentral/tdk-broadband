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

tr181obj.configureTestCase(ip,port,'TS_RDKRemoteDebugger_DynamicProfile_ValidateDynamicJsonProfileCreation')
sysobj.configureTestCase(ip,port,'TS_RDKRemoteDebugger_DynamicProfile_ValidateDynamicJsonProfileCreation')
# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
issueType = "Device.wifi"
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

if expectedresult in loadmodulestatus_tr181.upper() and expectedresult in loadmodulestatus_sys.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    print("Pre-requisite : Install the Download Server and host the dynamic profile in Download server path  ")

    step = 1
    profile_type = "dynamic"
    # Prerequisite checks before starting the test execution
    prereq_flag, revert_flag, step = checkRRDPrerequisites(tr181obj, sysobj, step, profile_type)

    if prereq_flag:
        print("Successfully completed the prerequisite checks.")
        step += 1
        # Get the value of RDKRemoteDebugger IssueType
        tdkTestObj, get_flag, initial_value = getRDKRemoteDebuggerIssueType(tr181obj, step)
        if get_flag:
            print(f"Successfully obtained the initial value of RDKRemoteDebugger IssueType {initial_value}")

            #Get the value of RDKRemoteDebugger CDL Module URL
            step += 1
            tdkTestObj, get_flag, cdl_url = getRDKRemoteDebuggerCDLModuleURL(tr181obj, step)
            if get_flag:
                print(f"Successfully obtained the initial value of RDKRemoteDebugger CDL Module URL {cdl_url}")
                # Set the value of RDKRemoteDebugger CDL Module URL to the download server
                step += 1
                set_flag = setRDKRemoteDebuggerCDLModuleURL(tr181obj, server_url,step)
                if set_flag:
                    print(f"Successfully set the value of RDKRemoteDebugger CDL Module URL to {server_url}.")

                    step += 1
                    # Set the value of RDKRemoteDebugger IssueType to trigger the debug report generation
                    set_flag = setRDKRemoteDebuggerIssueType(tr181obj, step, issueType)
                    if set_flag:
                        print("Successfully set the value of RDKRemoteDebugger IssueType to trigger the debug report generation.")
                        step += 1
                        sleep(5)
                        # Check whether json file is available in the designated location
                        tdkTestObj, file_flag = checkJsonProfileAvailable(sysobj, "dynamic", issueType, step)
                        if file_flag:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("TEST EXECUTION RESULT : SUCCESS")
                            print("The dynamic json profile is available as expected.")

                            sleep(5)
                            #Validate if the dynamic debug report is generated
                            step += 1
                            tdkTestObj, report_flag = checkDebugReportGenerated(sysobj, "dynamic", step)
                            if report_flag:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("TEST EXECUTION RESULT : SUCCESS")
                                print("Successfully verified that the dynamic debug report is generated.")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("TEST EXECUTION RESULT : FAILURE")
                                print("Failed to generate the dynamic debug report.")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("TEST EXECUTION RESULT : FAILURE")
                            print("The dynamic json profile is not available as expected.")

                        #Revert the value of RDKRemoteDebugger IssueType to its initial value
                        print("\nReverting the value of RDKRemoteDebugger IssueType to its initial value.")
                        step += 1
                        set_flag = setRDKRemoteDebuggerIssueType(tr181obj, step, initial_value)
                        if set_flag:
                            print("Successfully reverted the value of RDKRemoteDebugger IssueType to its initial value.")
                        else:
                            print("Failed to revert the value of RDKRemoteDebugger IssueType to its initial value.")

                    else:
                        print("Failed to set the value of RDKRemoteDebugger IssueType to trigger the debug report generation.")

                #Revert the value of RDKRemoteDebugger CDL Module URL to its initial value
                print("\nReverting the value of CDL Module URL to its initial value.")
                step += 1
                set_flag = setRDKRemoteDebuggerCDLModuleURL(tr181obj, cdl_url, step)
                if set_flag:
                    print("Successfully reverted the value of RDKRemoteDebugger CDL Module URL to its initial value.")
                else:
                    print("Failed to revert the value of RDKRemoteDebugger CDL Module URL to its initial value.")
            else:
                print(f"Failed to obtain the initial value of RDKRemoteDebugger CDL Module URL")
        else:
            print(f"Failed to obtain the initial value of RDKRemoteDebugger IssueType")
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
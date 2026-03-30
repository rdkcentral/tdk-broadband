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

tr181obj.configureTestCase(ip,port,'TS_RDKRemoteDebugger_DynamicProfile_ValidateDebugReportUpload')
sysobj.configureTestCase(ip,port,'TS_RDKRemoteDebugger_DynamicProfile_ValidateDebugReportUpload')
# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
issueType = "Device.wifi"
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

if expectedresult in loadmodulestatus_tr181.upper() and expectedresult in loadmodulestatus_sys.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    print("Pre-requisite : Install the Download Server and host the dynamic profile in Download server path  ")
    # Prerequisite check: Clear the RRD log file and delete the existing debug reports before starting the test execution
    prereq_flag = clearLogsAndDebugReports(sysobj)
    if prereq_flag:
        print("Successfully cleared the RRD log file and deleted the existing debug reports. Proceeding with the test execution.")

        step = 1
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
                set_flag = setRDKRemoteDebuggerCDLModuleURL(tr181obj, server_url, step)
                if set_flag:
                    print(f"Successfully set the value of RDKRemoteDebugger CDL Module URL to {server_url}.")

                    step += 1
                    # Set the value of RDKRemoteDebugger IssueType to trigger the debug report generation
                    set_flag = setRDKRemoteDebuggerIssueType(tr181obj, step, issueType)
                    if set_flag:
                        print("Successfully set the value of RDKRemoteDebugger IssueType to trigger the debug report generation.")

                        sleep(5)
                        step += 1
                        # Check whether json file is available in the designated location
                        tdkTestObj, file_flag = checkJsonProfileAvailable(sysobj, "dynamic", issueType, step)
                        if file_flag:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("TEST EXECUTION RESULT : SUCCESS")
                            print("The dynamic json profile is available as expected.")


                            #Validate if the dynamic debug report is generated
                            step += 1
                            tdkTestObj, report_flag = checkDebugReportGenerated(sysobj, "dynamic", step)
                            if report_flag:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("TEST EXECUTION RESULT : SUCCESS")
                                print("Successfully verified that the dynamic debug report is generated.")

                                # Set the value of RDKRemoteDebugger IssueType again to trigger the debug report upload
                                step += 1
                                set_flag = setRDKRemoteDebuggerIssueType(tr181obj, step, issueType)
                                if set_flag:
                                    print("Successfully set the value of RDKRemoteDebugger IssueType again to trigger the debug report upload.")

                                    # Check if the dynamic debug report is uploaded to the server
                                    step += 1
                                    tdkTestObj, upload_flag = validateDebugReportUpload(sysobj, "dynamic", server_url, rrd_log_file, step)
                                    if upload_flag:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("TEST EXECUTION RESULT : SUCCESS")
                                        print("The dynamic debug report is uploaded to the server successfully.")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("TEST EXECUTION RESULT : FAILURE")
                                        print("The dynamic debug report is not uploaded to the server as expected.")

                                else:
                                    print("Failed to set the value of RDKRemoteDebugger IssueType again to trigger the debug report upload.")
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
                print("\nReverting the value of RDKRemoteDebugger CDL Module URL to its initial value.")

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
        print("Failed to clear the RRD log file and delete the existing debug reports. Cannot proceed with the test execution.")

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
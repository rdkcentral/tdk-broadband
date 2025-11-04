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
import tdklib
from time import sleep
from CrashUploadVariables import *
from CrashUploadUtility import *
from tdkutility import *
from tdkbVariables import *

# Test components to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")

# IP and Port of box, No need to change, will be replaced with DUT details
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_CrashUpload_VerifyDefaultPortalUpload')
obj.configureTestCase(ip,port,'TS_CrashUpload_VerifyDefaultPortalUpload')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus_tr181 = obj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus_sys.upper() and "SUCCESS" in loadmodulestatus_tr181.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1
    process_name = NON_CCSP_PROCESS
    old_pid = ""
    dmp_filename = ""
    initial_minidump_count = "0"
    initial_ulimit = ""
    MAX_RETRY = 6

    # Verify crash portal URL
    print("\nTEST STEP %d: Verify crash portal URL is set to default" % step)
    print("EXPECTED RESULT %d: The crash portal URL should be retrieved successfully" % step)
    param = CRASH_PORTAL_DM_PARAM
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    actualresult, initial_value = getTR181Value(tdkTestObj, param)
    if actualresult in expectedresult and DEFAULT_CRASH_PORTAL_URL in initial_value.strip():
        initial_value = initial_value.strip()
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Crash portal URL retrieved: %s" % (step, initial_value))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Clear core_log.txt for clean logging
        print("\nTEST STEP %d: Clear %s to ensure clean logging" % (step, CORE_LOG_TXT))
        print("EXPECTED RESULT %d: The %s file should be cleared successfully" % (step, CORE_LOG_TXT))
        command = f"echo '' > {CORE_LOG_TXT}"
        tdkTestObj = sysobj.createTestStep('ExecuteCmd')
        actualresult, details = doSysutilExecuteCommand(tdkTestObj, command)
        if "SUCCESS" in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: The %s file cleared successfully" % (step, CORE_LOG_TXT))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to clear %s" % (step, CORE_LOG_TXT))
            print("[TEST EXECUTION RESULT] : FAILURE")

        step += 1
        # Set ulimit to unlimited
        print("\nTEST STEP %d: Set core dump size to unlimited" % step)
        print("EXPECTED RESULT %d: Core dump size should be set to unlimited" % step)
        tdkTestObj, actualresult, details, initial_ulimit = set_ulimit_core_unlimited(sysobj)
        if expectedresult in actualresult and details == "unlimited":
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Core dump size set successfully: %s (Initial value: %s)" % (step, details, initial_ulimit))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Verify COREDUMP_PATH_UNIT is active (waiting)
            print("\nTEST STEP %d: Verify %s is in active (waiting) state" % (step, COREDUMP_PATH_UNIT))
            print("EXPECTED RESULT %d: Path unit should be active (waiting)" % step)
            tdkTestObj, actualresult, state = get_active_state(sysobj, COREDUMP_PATH_UNIT)
            if expectedresult in actualresult and "active (waiting)" in state:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Path unit is active (waiting): %s" % (step, state))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                # Get the initial count of dmp files in MINIDUMPS_DIR directory
                print("\nTEST STEP %d: Get initial count of .dmp files in %s directory" % (step, MINIDUMPS_DIR))
                print("EXPECTED RESULT %d: Should get count of existing .dmp files" % step)
                tdkTestObj, actualresult, initial_minidump_count = check_directory_filecount(sysobj, MINIDUMPS_DIR)
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Initial .dmp file count: %s" % (step, initial_minidump_count))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to get initial .dmp file count" % step)
                    print("[TEST EXECUTION RESULT] : FAILURE")

                step += 1
                # Get process PID
                print("\nTEST STEP %d: Get PID of %s process" % (step, process_name))
                print("EXPECTED RESULT %d: Should get valid PID" % step)
                query = "sh %s/tdk_platform_utility.sh checkProcess %s" % (TDK_PATH, process_name)
                print("Command: %s" % query)
                tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                tdkTestObj.addParameter("command", query)
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                old_pid = tdkTestObj.getResultDetails().strip().replace("\\n", "")
                if expectedresult in actualresult and old_pid:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Process PID obtained: %s" % (step, old_pid))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step += 1
                    # Kill the process with SIGSEGV
                    print("\nTEST STEP %d: Kill %s process (PID: %s) with SIGSEGV signal" % (step, process_name, old_pid))
                    print("EXPECTED RESULT %d: Process should be killed successfully" % step)
                    query = "kill -11 %s" % old_pid
                    print("Command: %s" % query)
                    tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                    tdkTestObj.addParameter("command", query)
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Process killed successfully" % step)
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        step += 1
                        # Verify minidump file created and store filename
                        print("\nTEST STEP %d: Verify minidump file created in %s and store filename" % (step, MINIDUMPS_DIR))
                        print("EXPECTED RESULT %d: .dmp file count should be increased" % step)
                        tdkTestObj, actualresult, dmp_filename = verify_minidump_file_created(sysobj, initial_minidump_count, MINIDUMPS_DIR)
                        if expectedresult in actualresult and dmp_filename != "":
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: Minidump file created: %s" % (step, dmp_filename))
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                            base_dmp_filename = dmp_filename.replace(".dmp", "")

                            print("\nWaiting 10 seconds for upload process...")
                            sleep(10)

                            step += 1
                            # Verify compressed .tgz filename in core_log.txt contains .dmp filename
                            print("\nTEST STEP %d: Verify compressed .tgz filename in %s contains .dmp filename" % (step, CORE_LOG_TXT))
                            print("EXPECTED RESULT %d: .tgz filename should contain %s" % (step, base_dmp_filename))
                            tdkTestObj, actualresult, log_details = verify_log_pattern(sysobj, CORE_LOG_TXT, "DEBUG S3 File Name")
                            if expectedresult in actualresult and base_dmp_filename in log_details:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: .tgz filename contains .dmp filename: %s" % (step, log_details))
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                step += 1
                                # Verify Signing URL
                                print("\nTEST STEP %d: Verify Signing URL in %s" % (step, CORE_LOG_TXT))
                                print("EXPECTED RESULT %d: Signing URL should match configured URL: %s" % (step, DEFAULT_CRASH_PORTAL_URL))
                                tdkTestObj, actualresult, url_details = verify_log_pattern(sysobj, CORE_LOG_TXT, "Signing URL")
                                url_details = url_details.strip()

                                if expectedresult in actualresult and DEFAULT_CRASH_PORTAL_URL in url_details:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print("ACTUAL RESULT %d: Signing URL matches: %s" % (step, url_details))
                                    print("[TEST EXECUTION RESULT] : SUCCESS")

                                    step += 1
                                     # Check HTTP response code 200 for confirming Log Upload
                                    print("\nTEST STEP %d: Verify HTTP response code 200 in %s" % (step, CORE_LOG_TXT))
                                    print("EXPECTED RESULT %d: HTTP Response code should be 200" % step)
                                    tdkTestObj, actualresult, http_response = verify_log_pattern(sysobj, CORE_LOG_TXT, "HTTP Response code: 200")
                                    if expectedresult in actualresult:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: HTTP Response code 200 found: %s" % (step, http_response))
                                        print("[TEST EXECUTION RESULT] : SUCCESS")

                                        step += 1
                                        # Monitor for upload success logs
                                        print("\nTEST STEP %d: Monitor %s for upload success logs" % (step, CORE_LOG_TXT))
                                        print("EXPECTED RESULT %d: Upload success log should be present" % step)
                                        tdkTestObj, actualresult, success_log = verify_log_pattern(sysobj, CORE_LOG_TXT, "minidump Upload is successful")
                                        if expectedresult in actualresult:
                                            tdkTestObj.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT %d: Upload success log found: %s" % (step, success_log))
                                            print("[TEST EXECUTION RESULT] : SUCCESS")
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT %d: Upload success log not found" % step)
                                            print("[TEST EXECUTION RESULT] : FAILURE")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: HTTP Response code 200 not found" % step)
                                        print("[TEST EXECUTION RESULT] : FAILURE")

                                    # Verify minidump deleted after upload attempt
                                    step += 1
                                    print("\nTEST STEP %d: Verify minidump file deleted from %s after upload" % (step, MINIDUMPS_DIR))
                                    print("EXPECTED RESULT %d: .dmp file count should match initial count" % step)
                                    tdkTestObj, actualresult, final_minidump_count = check_directory_filecount(sysobj, MINIDUMPS_DIR)
                                    if expectedresult in actualresult and final_minidump_count == initial_minidump_count:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: Minidump deleted, file count matches initial: %s" % (step, final_minidump_count))
                                        print("[TEST EXECUTION RESULT] : SUCCESS")

                                        step += 1
                                        # Verify process restarted
                                        print("\nTEST STEP %d: Verify %s process restarted with new PID" % (step, process_name))
                                        print("EXPECTED RESULT %d: Process should be running with different PID" % step)
                                        tdkTestObj, actualresult, new_pid = verify_process_restart(sysobj, process_name, old_pid, MAX_RETRY)
                                        if expectedresult in actualresult and new_pid and new_pid != old_pid:
                                            tdkTestObj.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT %d: Process restarted successfully. Old PID: %s, New PID: %s" % (step, old_pid, new_pid))
                                            print("[TEST EXECUTION RESULT] : SUCCESS")
                                        elif new_pid == old_pid:
                                            tdkTestObj.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT %d: Process PID unchanged: %s (process may not have crashed)" % (step, new_pid))
                                            print("[TEST EXECUTION RESULT] : FAILURE")
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT %d: Process not running after crash" % step)
                                            print("[TEST EXECUTION RESULT] : FAILURE")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: Minidump not deleted. Initial count: %s, Final count: %s" % (step, initial_minidump_count, final_minidump_count))
                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("ACTUAL RESULT %d: Signing URL does not match: %s" % (step, url_details))
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: .tgz filename does not contain .dmp filename: %s" % (step, log_details))
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Minidump file not created" % step)
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Failed to kill process" % step)
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to get process PID" % step)
                    print("[TEST EXECUTION RESULT] : FAILURE")

                # Revert ulimit
                if initial_ulimit:
                    step += 1
                    print("\nTEST STEP %d: Revert core dump size to initial value: %s" % (step, initial_ulimit))
                    print("EXPECTED RESULT %d: Core dump size should be reverted to: %s" % (step, initial_ulimit))
                    tdkTestObj, actualresult, details = revert_ulimit_core(sysobj, initial_ulimit)
                    if expectedresult in actualresult and details == initial_ulimit:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Core dump size reverted successfully: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Failed to revert core dump size. Current value: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Path unit not in active (waiting) state: %s" % (step, state))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to set core dump size: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Crash portal URL is incorrect: %s" % (step, initial_value))
        print("[TEST EXECUTION RESULT] : FAILURE")

    sysobj.unloadModule("sysutil")
    obj.unloadModule("tdkbtr181")
else:
    print("Failed to load the module")
    sysobj.setLoadModuleStatus("FAILURE")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

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
sysobj.configureTestCase(ip,port,'TS_CrashUpload_VerifyMultipleCrashUpload')
obj.configureTestCase(ip,port,'TS_CrashUpload_VerifyMultipleCrashUpload')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus_tr181 = obj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus_sys.upper() and "SUCCESS" in loadmodulestatus_tr181.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1
    process_names = [NON_CCSP_PROCESS, WAN_MANAGER_PROCESS]
    old_pids = {}
    dmp_filenames = []
    initial_minidump_count = "0"
    initial_ulimit = ""
    initial_crash_portal_url = ""
    url_changed = False
    MAX_RETRY = 6

    # Pre-requisite: Local server should be up and running
    print("\n" + "="*80)
    print("PRE-REQUISITE: Local server should be up and running")
    print("Server Details: %s:%s" % (LOCAL_SERVER_IP, LOCAL_SERVER_PORT))
    print("Upload URL: %s" % LOCAL_UPLOAD_URL)
    print("Please ensure the local server is accessible before proceeding with the test")
    print("="*80 + "\n")

    # Get initial crash portal URL
    print("\nTEST STEP %d: Get initial crash portal URL" % step)
    print("EXPECTED RESULT %d: Should retrieve the current crash portal URL" % step)
    param = CRASH_PORTAL_DM_PARAM
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    actualresult, initial_crash_portal_url = getTR181Value(tdkTestObj, param)
    if expectedresult in actualresult and initial_crash_portal_url:
        initial_crash_portal_url = initial_crash_portal_url.strip()
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Initial crash portal URL retrieved: %s" % (step, initial_crash_portal_url))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Set crash portal URL to local server
        print("\nTEST STEP %d: Set crash portal URL to local server %s" % (step, LOCAL_UPLOAD_URL))
        print("EXPECTED RESULT %d: Crash portal URL should be set successfully" % step)
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
        tdkTestObj.addParameter("ParamName", CRASH_PORTAL_DM_PARAM)
        tdkTestObj.addParameter("ParamValue", LOCAL_UPLOAD_URL)
        tdkTestObj.addParameter("Type", "string")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails().strip()
        if expectedresult in actualresult:
            url_changed = True
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Crash portal URL set successfully: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Verify crash portal URL
            print("\nTEST STEP %d: Verify crash portal URL is set to local server" % step)
            print("EXPECTED RESULT %d: The crash portal URL should be %s" % (step, LOCAL_UPLOAD_URL))
            param = CRASH_PORTAL_DM_PARAM
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
            actualresult, current_value = getTR181Value(tdkTestObj, param)
            if actualresult in expectedresult and LOCAL_UPLOAD_URL in current_value.strip():
                current_value = current_value.strip()
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Crash portal URL retrieved: %s" % (step, current_value))
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

                        # Get PIDs for all processes
                        all_pids_obtained = True
                        for process_name in process_names:
                            step += 1
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
                                old_pids[process_name] = old_pid
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: Process PID obtained: %s" % (step, old_pid))
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                all_pids_obtained = False
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: Failed to get process PID for %s" % (step, process_name))
                                print("[TEST EXECUTION RESULT] : FAILURE")

                        if all_pids_obtained:
                            # Kill all processes with SIGSEGV
                            all_processes_killed = True
                            for process_name in process_names:
                                step += 1
                                old_pid = old_pids[process_name]
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
                                else:
                                    all_processes_killed = False
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("ACTUAL RESULT %d: Failed to kill process %s" % (step, process_name))
                                    print("[TEST EXECUTION RESULT] : FAILURE")

                            if all_processes_killed:
                                step += 1
                                # Verify multiple minidump files created and store filenames
                                print("\nTEST STEP %d: Verify multiple minidump files created in %s and store filenames" % (step, MINIDUMPS_DIR))
                                print("EXPECTED RESULT %d: .dmp file count should be increased by %d" % (step, len(process_names)))
                                command = f"ls {MINIDUMPS_DIR} | grep '.dmp' | xargs"
                                print("Command: %s" % command)
                                tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                                actualresult, details = doSysutilExecuteCommand(tdkTestObj, command)
                                if "SUCCESS" in actualresult and details.strip():
                                    dmp_filenames = details.strip().split()
                                    if len(dmp_filenames) >= len(process_names):
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: Multiple minidump files created: %s" % (step, dmp_filenames))
                                        print("[TEST EXECUTION RESULT] : SUCCESS")
                                        # Extract base filenames without extensions
                                        base_dmp_filenames = []
                                        for filename in dmp_filenames:
                                            base_dmp_filenames.append(filename.replace(".dmp", ""))

                                        print("\nWaiting 10 seconds for upload process...")
                                        sleep(10)

                                        # Verify all compressed .tgz filenames in core_log.txt
                                        step += 1
                                        print("\nTEST STEP %d: Verify all compressed .tgz filenames in %s" % (step, CORE_LOG_TXT))
                                        print("EXPECTED RESULT %d: All .tgz filenames should be present in log" % step)
                                        all_filenames_found = True
                                        for base_filename in base_dmp_filenames:
                                            tdkTestObj, actualresult, log_details = verify_log_pattern(sysobj, CORE_LOG_TXT, base_filename)
                                            if expectedresult not in actualresult:
                                                all_filenames_found = False
                                                print("WARNING: Filename %s not found in log" % base_filename)

                                        if all_filenames_found:
                                            tdkTestObj.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT %d: All .tgz filenames found in core_log.txt" % step)
                                            print("[TEST EXECUTION RESULT] : SUCCESS")

                                            step += 1
                                            # Verify Signing URL
                                            print("\nTEST STEP %d: Verify Signing URL in %s" % (step, CORE_LOG_TXT))
                                            print("EXPECTED RESULT %d: Signing URL should match configured URL: %s" % (step, LOCAL_UPLOAD_URL))
                                            tdkTestObj, actualresult, url_details = verify_log_pattern(sysobj, CORE_LOG_TXT, "Signing URL")
                                            url_details = url_details.strip()

                                            if expectedresult in actualresult and LOCAL_UPLOAD_URL in url_details:
                                                tdkTestObj.setResultStatus("SUCCESS")
                                                print("ACTUAL RESULT %d: Signing URL matches: %s" % (step, url_details))
                                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                                step += 1
                                                # Check HTTP response code 200 for all uploads
                                                print("\nTEST STEP %d: Verify HTTP response code 200 for all uploads in %s" % (step, CORE_LOG_TXT))
                                                print("EXPECTED RESULT %d: HTTP Response code 200 should be present for all uploads" % step)

                                                command = f"grep 'HTTP Response code: 200' {CORE_LOG_TXT} | wc -l"
                                                tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                                                actualresult, details = doSysutilExecuteCommand(tdkTestObj, command)
                                                response_count = details.strip()

                                                if "SUCCESS" in actualresult and response_count.isdigit() and int(response_count) >= len(process_names):
                                                    tdkTestObj.setResultStatus("SUCCESS")
                                                    print("ACTUAL RESULT %d: HTTP Response code 200 found %s times (expected at least %d)" % (step, response_count, len(process_names)))
                                                    print("[TEST EXECUTION RESULT] : SUCCESS")

                                                    step += 1
                                                    # Monitor for upload success logs
                                                    print("\nTEST STEP %d: Monitor %s for upload success logs" % (step, CORE_LOG_TXT))
                                                    print("EXPECTED RESULT %d: Upload success logs should be present for all minidumps" % step)

                                                    command = f"grep 'minidump Upload is successful' {CORE_LOG_TXT} | wc -l"
                                                    tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                                                    actualresult, details = doSysutilExecuteCommand(tdkTestObj, command)
                                                    success_count = details.strip()
                                                    if "SUCCESS" in actualresult and success_count.isdigit() and int(success_count) >= len(process_names):
                                                        tdkTestObj.setResultStatus("SUCCESS")
                                                        print("ACTUAL RESULT %d: Upload success logs found %s times (expected at least %d)" % (step, success_count, len(process_names)))
                                                        print("[TEST EXECUTION RESULT] : SUCCESS")
                                                    else:
                                                        tdkTestObj.setResultStatus("FAILURE")
                                                        print("ACTUAL RESULT %d: Upload success logs found %s times (expected at least %d)" % (step, success_count, len(process_names)))
                                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                                else:
                                                    tdkTestObj.setResultStatus("FAILURE")
                                                    print("ACTUAL RESULT %d: HTTP Response code 200 found %s times (expected at least %d)" % (step, response_count, len(process_names)))
                                                    print("[TEST EXECUTION RESULT] : FAILURE")

                                                # Verify minidumps deleted after upload attempt
                                                step += 1
                                                print("\nTEST STEP %d: Verify minidump files deleted from %s after upload" % (step, MINIDUMPS_DIR))
                                                print("EXPECTED RESULT %d: .dmp file count should match initial count" % step)
                                                tdkTestObj, actualresult, final_minidump_count = check_directory_filecount(sysobj, MINIDUMPS_DIR)
                                                if expectedresult in actualresult and final_minidump_count == initial_minidump_count:
                                                    tdkTestObj.setResultStatus("SUCCESS")
                                                    print("ACTUAL RESULT %d: Minidumps deleted, file count matches initial: %s" % (step, final_minidump_count))
                                                    print("[TEST EXECUTION RESULT] : SUCCESS")

                                                    # Verify all processes restarted
                                                    all_processes_restarted = True
                                                    for process_name in process_names:
                                                        step += 1
                                                        old_pid = old_pids[process_name]
                                                        print("\nTEST STEP %d: Verify %s process restarted with new PID" % (step, process_name))
                                                        print("EXPECTED RESULT %d: Process should be running with different PID" % step)
                                                        tdkTestObj, actualresult, new_pid = verify_process_restart(sysobj, process_name, old_pid, MAX_RETRY)
                                                        if expectedresult in actualresult and new_pid and new_pid != old_pid:
                                                            tdkTestObj.setResultStatus("SUCCESS")
                                                            print("ACTUAL RESULT %d: Process restarted successfully. Old PID: %s, New PID: %s" % (step, old_pid, new_pid))
                                                            print("[TEST EXECUTION RESULT] : SUCCESS")
                                                        elif new_pid == old_pid:
                                                            all_processes_restarted = False
                                                            tdkTestObj.setResultStatus("FAILURE")
                                                            print("ACTUAL RESULT %d: Process PID unchanged: %s (process may not have crashed)" % (step, new_pid))
                                                            print("[TEST EXECUTION RESULT] : FAILURE")
                                                        else:
                                                            all_processes_restarted = False
                                                            tdkTestObj.setResultStatus("FAILURE")
                                                            print("ACTUAL RESULT %d: Process not running after crash" % step)
                                                            print("[TEST EXECUTION RESULT] : FAILURE")
                                                else:
                                                    tdkTestObj.setResultStatus("FAILURE")
                                                    print("ACTUAL RESULT %d: Minidumps not deleted. Initial count: %s, Final count: %s" % (step, initial_minidump_count, final_minidump_count))
                                                    print("[TEST EXECUTION RESULT] : FAILURE")
                                            else:
                                                tdkTestObj.setResultStatus("FAILURE")
                                                print("ACTUAL RESULT %d: Signing URL does not match: %s" % (step, url_details))
                                                print("[TEST EXECUTION RESULT] : FAILURE")
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT %d: Not all .tgz filenames found in core_log.txt" % step)
                                            print("[TEST EXECUTION RESULT] : FAILURE")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: Minidump files created: %d (expected at least %d)" % (step, len(dmp_filenames), len(process_names)))
                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("ACTUAL RESULT %d: Failed to list minidump files" % step)
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

                # Revert crash portal URL to initial value (only if it was changed)
                if url_changed:
                    step += 1
                    print("\nTEST STEP %d: Revert crash portal URL to initial value" % step)
                    print("EXPECTED RESULT %d: Crash portal URL should be reverted to %s" % (step, initial_crash_portal_url))
                    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
                    tdkTestObj.addParameter("ParamName", CRASH_PORTAL_DM_PARAM)
                    tdkTestObj.addParameter("ParamValue", initial_crash_portal_url)
                    tdkTestObj.addParameter("Type", "string")
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    details = tdkTestObj.getResultDetails().strip()
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Crash portal URL reverted successfully: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        step += 1
                        # Verify crash portal URL reverted
                        print("\nTEST STEP %d: Verify crash portal URL is reverted to initial value" % step)
                        print("EXPECTED RESULT %d: The crash portal URL should be %s" % (step, initial_crash_portal_url))
                        param = CRASH_PORTAL_DM_PARAM
                        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                        actualresult, final_value = getTR181Value(tdkTestObj, param)
                        if actualresult in expectedresult and initial_crash_portal_url in final_value.strip():
                            final_value = final_value.strip()
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: Crash portal URL verified: %s" % (step, final_value))
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Crash portal URL mismatch: %s" % (step, final_value))
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Failed to revert crash portal URL: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Crash portal URL is incorrect: %s" % (step, current_value))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to set crash portal URL: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to retrieve initial crash portal URL: %s" % (step, initial_crash_portal_url))
        print("[TEST EXECUTION RESULT] : FAILURE")

    sysobj.unloadModule("sysutil")
    obj.unloadModule("tdkbtr181")
else:
    print("Failed to load the module")
    sysobj.setLoadModuleStatus("FAILURE")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

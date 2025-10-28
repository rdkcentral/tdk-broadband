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
obj = tdklib.TDKScriptingLibrary("tdkbtr181", "1")
sysobj = tdklib.TDKScriptingLibrary("sysutil", "1")

# IP and Port of box, No need to change, will be replaced with DUT details
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CrashUpload_VerifyMultipleCrashUpload')
sysobj.configureTestCase(ip,port,'TS_CrashUpload_VerifyMultipleCrashUpload')

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus_sys.upper():
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1
    process_names = ["fwupgrademanager", "wanmanager"]
    old_pids = {}
    dmp_filenames = []
    base_dmp_filenames = []
    initial_crash_portal_url = ""
    url_changed = False

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
                # Set ulimit to unlimited
                print("\nTEST STEP %d: Set core dump size to unlimited" % step)
                print("EXPECTED RESULT %d: Core dump size should be set to unlimited" % step)
                tdkTestObj, actualresult, details = set_ulimit_core_unlimited(sysobj)
                if expectedresult in actualresult and details == "unlimited":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Core dump size set successfully: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step += 1
                    # Verify coredump-upload.path is in active waiting state
                    print("\nTEST STEP %d: Verify %s unit is in active waiting state" % (step, COREDUMP_PATH_UNIT))
                    print("EXPECTED RESULT %d: %s should be in active (waiting) state" % (step, COREDUMP_PATH_UNIT))
                    tdkTestObj, actualresult, state = get_active_state(sysobj, COREDUMP_PATH_UNIT)
                    if expectedresult in actualresult and "waiting" in state.lower():
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: %s is in active waiting state: %s" % (step, COREDUMP_PATH_UNIT, state))
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        step += 1
                        # Check if /minidumps is empty
                        print("\nTEST STEP %d: Check if %s directory is empty" % (step, MINIDUMPS_DIR))
                        print("EXPECTED RESULT %d: Directory should be empty initially" % step)
                        tdkTestObj, actualresult, details = check_directory_empty(sysobj, MINIDUMPS_DIR)
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: Directory is empty" % step)
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: Directory not empty (contains: %s), proceeding with test" % (step, details))
                            print("[TEST EXECUTION RESULT] : SUCCESS (Non-critical)")

                        step += 1
                        # Delete core_log.txt for clean logging
                        print("\nTEST STEP %d: Delete %s to ensure clean logging" % (step, CORE_LOG_TXT))
                        print("EXPECTED RESULT %d: The %s file should be deleted successfully" % (step, CORE_LOG_TXT))
                        command = f"rm -f {CORE_LOG_TXT}"
                        tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                        actualresult, details = doSysutilExecuteCommand(tdkTestObj, command)
                        if "SUCCESS" in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: The %s file deleted successfully. Details: %s" % (step, CORE_LOG_TXT, details))
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: Command executed (file may not have existed). Details: %s" % (step, details))
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                        step += 1
                        # Get PIDs for both processes
                        print("\nTEST STEP %d: Get PIDs of %s processes" % (step, process_names))
                        print("EXPECTED RESULT %d: Should get valid PIDs for both processes" % step)
                        all_pids_found = True
                        for process_name in process_names:
                            query = f"sh {TDK_PATH}/tdk_platform_utility.sh checkProcess {process_name}"
                            print("Command: %s" % query)
                            tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                            tdkTestObj.addParameter("command", query)
                            tdkTestObj.executeTestCase(expectedresult)
                            actualresult = tdkTestObj.getResult()
                            pid = tdkTestObj.getResultDetails().strip().replace("\\n", "")
                            if expectedresult in actualresult and pid:
                                old_pids[process_name] = pid
                                print("ACTUAL RESULT %d: %s PID obtained: %s" % (step, process_name, pid))
                            else:
                                all_pids_found = False
                                print("ACTUAL RESULT %d: Failed to get PID for %s" % (step, process_name))
                                print("[TEST EXECUTION RESULT] : FAILURE")
                                tdkTestObj.setResultStatus("FAILURE")
                                break
                        if all_pids_found:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: All PIDs obtained: %s" % (step, old_pids))
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                            step += 1
                            # Kill both processes with SIGSEGV
                            print("\nTEST STEP %d: Kill processes %s with SIGSEGV signal" % (step, process_names))
                            print("EXPECTED RESULT %d: Processes should be killed successfully" % step)
                            all_killed = True
                            for process_name, pid in old_pids.items():
                                query = f"kill -11 {pid}"
                                print("Command: %s" % query)
                                tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                                tdkTestObj.addParameter("command", query)
                                tdkTestObj.executeTestCase(expectedresult)
                                actualresult = tdkTestObj.getResult()
                                if expectedresult in actualresult:
                                    print("ACTUAL RESULT %d: %s killed successfully" % (step, process_name))
                                else:
                                    all_killed = False
                                    print("ACTUAL RESULT %d: Failed to kill %s" % (step, process_name))
                                    tdkTestObj.setResultStatus("FAILURE")
                                    break
                            if all_killed:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: All processes killed successfully" % step)
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                                try:
                                    step += 1
                                    # Verify multiple minidump files created and store filenames
                                    print("\nTEST STEP %d: Verify minidump files created in %s and store filenames" % (step, MINIDUMPS_DIR))
                                    print("EXPECTED RESULT %d: Multiple .dmp or .tgz files should be created" % step)
                                    command = f"ls {MINIDUMPS_DIR} | grep -E '.dmp|.tgz' | xargs"
                                    tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                                    tdkTestObj.addParameter("command", command)
                                    tdkTestObj.executeTestCase(expectedresult)
                                    actualresult = tdkTestObj.getResult()
                                    raw_output = tdkTestObj.getResultDetails()
                                    if expectedresult in actualresult and raw_output.strip():
                                        # Clean escaped newlines and split properly
                                        cleaned = raw_output.replace("\\n", "\n").strip()
                                        dmp_filenames = [f for f in cleaned.split() if f]
                                        dmp_filenames = [f for f in dmp_filenames if f.endswith('.dmp')]
                                        if len(dmp_filenames) >= 2:
                                            tdkTestObj.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT %d: Minidump files created: %s" % (step, dmp_filenames))
                                            print("[TEST EXECUTION RESULT] : SUCCESS")
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT %d: Insufficient minidump files: %s" % (step, dmp_filenames))
                                            print("[TEST EXECUTION RESULT] : FAILURE")
                                            dmp_filenames = []
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: No minidump files created" % step)
                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                        dmp_filenames = []
                                    if dmp_filenames:
                                        base_dmp_filenames = [f.rsplit('.', 1)[0] for f in dmp_filenames]
                                        # Wait and poll for log entries
                                        print("\nWaiting up to 10 seconds for upload logs to appear...")
                                        max_wait = 10
                                        poll_interval = 5
                                        elapsed = 0
                                        all_logs_found = False

                                        while elapsed < max_wait:
                                            missing = []
                                            for base in base_dmp_filenames:
                                                cmd = f"grep 'DEBUG S3 File Name' {CORE_LOG_TXT} | grep {base}"
                                                tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                                                tdkTestObj.addParameter("command", cmd)
                                                tdkTestObj.executeTestCase(expectedresult)
                                                if base not in tdkTestObj.getResultDetails():
                                                    missing.append(base)
                                            if not missing:
                                                all_logs_found = True
                                                break
                                            print(f"   Still waiting for: {missing} (elapsed: {elapsed}s)")
                                            sleep(poll_interval)
                                            elapsed += poll_interval

                                        step += 1
                                        print("\nTEST STEP %d: Verify compressed .tgz filenames in %s contain .dmp filenames" % (step, CORE_LOG_TXT))
                                        print("EXPECTED RESULT %d: .tgz filenames should contain %s" % (step, base_dmp_filenames))

                                        all_found = True
                                        for base_name in base_dmp_filenames:
                                            grep_cmd = f"grep 'DEBUG S3 File Name' {CORE_LOG_TXT} | grep {base_name}"
                                            tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                                            tdkTestObj.addParameter("command", grep_cmd)
                                            tdkTestObj.executeTestCase(expectedresult)
                                            actualresult = tdkTestObj.getResult()
                                            log_line = tdkTestObj.getResultDetails().strip()
                                            if expectedresult in actualresult and base_name in log_line:
                                                print("ACTUAL RESULT %d: .tgz filename contains .dmp name for %s: %s"
                                                      % (step, base_name, log_line))
                                            else:
                                                all_found = False
                                                print("ACTUAL RESULT %d: .tgz filename MISSING .dmp name for %s: %s"
                                                      % (step, base_name, log_line))
                                        if all_found and all_logs_found:
                                            tdkTestObj.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT %d: All .tgz filenames verified in logs" % step)
                                            print("[TEST EXECUTION RESULT] : SUCCESS")
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT %d: One or more .tgz filenames not verified" % step)
                                            print("[TEST EXECUTION RESULT] : FAILURE")

                                        step += 1
                                        # Verify S3 Amazon Signing URL
                                        print("\nTEST STEP %d: Verify S3 Amazon Signing URL in %s" % (step, CORE_LOG_TXT))
                                        print("EXPECTED RESULT %d: S3 URL should match configured URL: %s" % (step, LOCAL_UPLOAD_URL))
                                        tdkTestObj, actualresult, url_details = verify_log_pattern(sysobj, CORE_LOG_TXT, "S3 Amazon Signing URL")
                                        url_details = url_details.strip()
                                        if expectedresult in actualresult and LOCAL_UPLOAD_URL in url_details:
                                            tdkTestObj.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT %d: S3 URL matches: %s" % (step, url_details))
                                            print("[TEST EXECUTION RESULT] : SUCCESS")
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT %d: S3 URL does not match: %s" % (step, url_details))
                                            print("[TEST EXECUTION RESULT] : FAILURE")

                                        step += 1
                                        # Check HTTP response code 200
                                        print("\nTEST STEP %d: Verify HTTP response code 200 in %s" % (step, CORE_LOG_TXT))
                                        print("EXPECTED RESULT %d: HTTP Response code should be 200" % step)
                                        tdkTestObj, actualresult, http_response = verify_log_pattern(sysobj, CORE_LOG_TXT, "HTTP Response code: 200")
                                        if expectedresult in actualresult:
                                            tdkTestObj.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT %d: HTTP Response code 200 found: %s" % (step, http_response))
                                            print("[TEST EXECUTION RESULT] : SUCCESS")
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT %d: HTTP Response code 200 not found" % step)
                                            print("[TEST EXECUTION RESULT] : FAILURE")

                                        step += 1
                                        # Monitor for upload success logs
                                        print("\nTEST STEP %d: Monitor %s for upload success logs" % (step, CORE_LOG_TXT))
                                        print("EXPECTED RESULT %d: Upload success log should be present" % step)
                                        tdkTestObj, actualresult, success_log = verify_log_pattern(sysobj, CORE_LOG_TXT, "S3 minidump Upload is successful")
                                        if expectedresult in actualresult:
                                            tdkTestObj.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT %d: Upload success log found: %s" % (step, success_log))
                                            print("[TEST EXECUTION RESULT] : SUCCESS")
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT %d: Upload success log not found" % step)
                                            print("[TEST EXECUTION RESULT] : FAILURE")

                                finally:
                                    # Verify minidump deleted after upload
                                    step += 1
                                    print("\nTEST STEP %d: Verify minidump file deleted from %s after upload attempt" % (step, MINIDUMPS_DIR))
                                    print("EXPECTED RESULT %d: Directory should be empty or deletion log present" % step)
                                    tdkTestObj, actualresult, details = check_directory_empty(sysobj, MINIDUMPS_DIR)
                                    if expectedresult in actualresult:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: Minidump deleted, directory is empty" % step)
                                        print("[TEST EXECUTION RESULT] : SUCCESS")
                                    else:
                                        tdkTestObj, actualresult, delete_log = verify_log_pattern(sysobj, CORE_LOG_TXT, "Removing uploaded minidump file")
                                        if expectedresult in actualresult:
                                            tdkTestObj.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT %d: Deletion log found: %s" % (step, delete_log))
                                            print("[TEST EXECUTION RESULT] : SUCCESS")
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT %d: Minidump not deleted" % step)
                                            print("[TEST EXECUTION RESULT] : FAILURE")

                                    # Verify process restarted
                                    step += 1
                                    print("\nTEST STEP %d: Verify %s processes restarted with new PIDs" % (step, process_names))
                                    print("EXPECTED RESULT %d: Processes should restart with different PIDs" % step)
                                    all_restarted = True
                                    for process_name in process_names:
                                        query = f"sh {TDK_PATH}/tdk_platform_utility.sh checkProcess {process_name}"
                                        print("Command: %s" % query)
                                        tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                                        tdkTestObj.addParameter("command", query)
                                        MAX_RETRY = 6
                                        retryCount = 0
                                        new_pid = ""
                                        print("Check every 5 seconds whether %s is up" % process_name)
                                        while retryCount < MAX_RETRY:
                                            tdkTestObj.executeTestCase(expectedresult)
                                            actualresult = tdkTestObj.getResult()
                                            new_pid = tdkTestObj.getResultDetails().strip().replace("\\n", "")
                                            if expectedresult in actualresult and new_pid:
                                                break
                                            else:
                                                sleep(5)
                                                retryCount += 1
                                        if expectedresult in actualresult and new_pid and new_pid != old_pids[process_name]:
                                            print("ACTUAL RESULT %d: %s restarted successfully. Old PID: %s, New PID: %s"
                                                  % (step, process_name, old_pids[process_name], new_pid))
                                        else:
                                            all_restarted = False
                                            print("ACTUAL RESULT %d: %s restart failed. Old PID: %s, New PID: %s"
                                                  % (step, process_name, old_pids[process_name], new_pid))
                                            tdkTestObj.setResultStatus("FAILURE")
                                    if all_restarted:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: All processes restarted successfully" % step)
                                        print("[TEST EXECUTION RESULT] : SUCCESS")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: One or more processes failed to restart" % step)
                                        print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                print("ACTUAL RESULT %d: Failed to kill one or more processes" % step)
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            print("ACTUAL RESULT %d: Failed to get one or more process PIDs" % step)
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: %s is not in active waiting state: %s" % (step, COREDUMP_PATH_UNIT, state))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to set core dump size: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Crash portal URL is incorrect: %s" % (step, current_value))
                print("[TEST EXECUTION RESULT] : FAILURE")

            # Revert crash portal URL
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
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to revert crash portal URL: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : FAILURE")

                step += 1
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
                print("\nSkipping URL revert as it was not successfully changed")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to set crash portal URL: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to retrieve initial crash portal URL: %s" % (step, initial_crash_portal_url))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload the modules
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

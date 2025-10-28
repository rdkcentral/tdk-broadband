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
        # Set ulimit to unlimited
        print("\nTEST STEP %d: Set core dump size to unlimited" % step)
        print("EXPECTED RESULT %d: Core dump size should be set to unlimited" % step)
        tdkTestObj, actualresult, details = set_ulimit_core_unlimited(sysobj)
        if expectedresult in actualresult and details == "unlimited":
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Core dump size set successfully: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Verify coredump-upload.path is active (waiting)
            print("\nTEST STEP %d: Verify coredump-upload.path is in active (waiting) state" % step)
            print("EXPECTED RESULT %d: Path unit should be active (waiting)" % step)
            tdkTestObj, actualresult, state = get_active_state(sysobj, COREDUMP_PATH_UNIT)
            if expectedresult in actualresult and "active (waiting)" in state:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Path unit is active (waiting): %s" % (step, state))
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
                    # Directory not empty, but we can continue
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
                        try:
                            step += 1
                            # Verify minidump file created and store filename
                            print("\nTEST STEP %d: Verify minidump file created in %s and store filename" % (step, MINIDUMPS_DIR))
                            print("EXPECTED RESULT %d: .dmp or .tgz file should be created" % step)
                            tdkTestObj, actualresult, dmp_filename = verify_minidump_file_created(sysobj, MINIDUMPS_DIR)
                            if expectedresult in actualresult and dmp_filename != "":
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: Minidump file created: %s" % (step, dmp_filename))
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                # Extract .dmp filename without extension if .tgz
                                if ".tgz" in dmp_filename:
                                    base_dmp_filename = dmp_filename.replace(".tgz", "")
                                else:
                                    base_dmp_filename = dmp_filename.replace(".dmp", "")
                                # Wait for upload process
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
                                    # Verify S3 Amazon Signing URL
                                    print("\nTEST STEP %d: Verify S3 Amazon Signing URL in %s" % (step, CORE_LOG_TXT))
                                    print("EXPECTED RESULT %d: S3 URL should match configured URL: %s" % (step, DEFAULT_CRASH_PORTAL_URL))
                                    tdkTestObj, actualresult, url_details = verify_log_pattern(sysobj, CORE_LOG_TXT, "S3 Amazon Signing URL")
                                    # Normalize url_details by stripping whitespace and newlines
                                    url_details = url_details.strip()
                                    if expectedresult in actualresult and DEFAULT_CRASH_PORTAL_URL in url_details:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: S3 URL matches: %s" % (step, url_details))
                                        print("[TEST EXECUTION RESULT] : SUCCESS")

                                        step += 1
                                        # Check HTTP response code 200
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
                                            tdkTestObj, actualresult, success_log = verify_log_pattern(sysobj, CORE_LOG_TXT, "S3 minidump Upload is successful")
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
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: S3 URL does not match: %s" % (step, url_details))
                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("ACTUAL RESULT %d: .tgz filename does not contain .dmp filename: %s" % (step, log_details))
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                        finally:
                            # Verify minidump deleted after upload attempt
                            step += 1
                            print("\nTEST STEP %d: Verify minidump file deleted from %s after upload attempt" % (step, MINIDUMPS_DIR))
                            print("EXPECTED RESULT %d: Directory should be empty or deletion log present" % step)
                            tdkTestObj, actualresult, details = check_directory_empty(sysobj, MINIDUMPS_DIR)
                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: Minidump deleted, directory is empty" % step)
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                # Check deletion log
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
                            print("\nTEST STEP %d: Verify %s process restarted with new PID" % (step, process_name))
                            print("EXPECTED RESULT %d: Process should restart with different PID" % step)
                            query = "sh %s/tdk_platform_utility.sh checkProcess %s" % (TDK_PATH, process_name)
                            print("Command: %s" % query)
                            tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                            tdkTestObj.addParameter("command", query)
                            # Retry logic for process restart
                            MAX_RETRY = 6
                            retryCount = 0
                            new_pid = ""
                            print("Check every 5 seconds whether the process is up")
                            while retryCount < MAX_RETRY:
                                tdkTestObj.executeTestCase(expectedresult)
                                actualresult = tdkTestObj.getResult()
                                new_pid = tdkTestObj.getResultDetails().strip().replace("\\n", "")
                                if expectedresult in actualresult and new_pid:
                                    break
                                else:
                                    sleep(5)
                                    retryCount = retryCount + 1
                            if expectedresult in actualresult and new_pid and new_pid != old_pid:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: Process restarted successfully. Old PID: %s, New PID: %s" % (step, old_pid, new_pid))
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: Process restart verification failed. Old PID: %s, New PID: %s" % (step, old_pid, new_pid))
                                print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Failed to kill process" % step)
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to get process PID" % step)
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

    # Unload the modules
    sysobj.unloadModule("sysutil")
    obj.unloadModule("tdkbtr181")
else:
    print("Failed to load the module")
    sysobj.setLoadModuleStatus("FAILURE")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")


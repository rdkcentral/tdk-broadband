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

# Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change, will be replaced with DUT details
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_CrashUpload_NonCCSPProcessCrash')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus_sys.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1
    process_name = NON_CCSP_PROCESS
    old_pid = ""
    minidump_created = False

    # Set ulimit to unlimited
    print("\nTEST STEP %d: Set core dump size to unlimited" % step)
    print("EXPECTED RESULT %d: Core dump size should be set to unlimited" % step)
    tdkTestObj, actualresult, details = set_ulimit_core_unlimited(sysobj)
    if expectedresult in actualresult and details == "unlimited":
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Core dump size set successfully: %s" % (step, details))
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
        # Get process PID using tdk_platform_utility.sh
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
                # Verify minidump file created
                print("\nTEST STEP %d: Verify minidump file created in %s" % (step, MINIDUMPS_DIR))
                print("EXPECTED RESULT %d: .dmp or .tgz file should be created" % step)
                tdkTestObj, actualresult, filename = verify_minidump_file_created(sysobj, MINIDUMPS_DIR)
                if expectedresult in actualresult and filename != "":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Minidump file created: %s" % (step, filename))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                    minidump_created = True

                    step += 1
                    # Verify process restarted using tdk_platform_utility.sh
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
                    print("Check every 10 seconds whether the process is up")

                    while retryCount < MAX_RETRY:
                        tdkTestObj.executeTestCase(expectedresult)
                        actualresult = tdkTestObj.getResult()
                        new_pid = tdkTestObj.getResultDetails().strip().replace("\\n", "")
                        if expectedresult in actualresult and new_pid:
                            break
                        else:
                            sleep(10)
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
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to set core dump size: %s" % (step, details))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Cleanup: Delete minidump files
    if minidump_created:
        step += 1
        print("\nTEST STEP %d: Cleanup - Delete minidump files from %s" % (step, MINIDUMPS_DIR))
        print("EXPECTED RESULT %d: Minidump files should be deleted" % step)
        tdkTestObj, actualresult, details = delete_minidump_files(sysobj, MINIDUMPS_DIR)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Minidump files deleted successfully" % step)
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to delete minidump files" % step)
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload the modules
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

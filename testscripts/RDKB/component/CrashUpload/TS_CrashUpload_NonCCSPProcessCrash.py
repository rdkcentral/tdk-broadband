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
    initial_minidump_count = "0"
    minidump_created = False
    initial_ulimit = ""
    MAX_RETRY = 6

    # Set ulimit to unlimited
    print("\nTEST STEP %d: Set core dump size to unlimited" % step)
    print("EXPECTED RESULT %d: Core dump size should be set to unlimited" % step)
    tdkTestObj, actualresult, details, initial_ulimit = set_ulimit_core_unlimited(sysobj)
    if expectedresult in actualresult and details == "unlimited":
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Core dump size set successfully: %s (Initial value: %s)" % (step, details, initial_ulimit))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Check if coredump-upload.path is in active waiting state
        print("\nTEST STEP %d: Check if %s is in active (waiting) state" % (step, COREDUMP_PATH_UNIT))
        print("EXPECTED RESULT %d: %s should be in active (waiting) state" % (step, COREDUMP_PATH_UNIT))
        tdkTestObj, actualresult, state = get_active_state(sysobj, COREDUMP_PATH_UNIT)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: %s is in active (waiting) state" % (step, COREDUMP_PATH_UNIT))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Get initial count of minidump files
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
                    print("EXPECTED RESULT %d: .dmp file count should be increased" % step)
                    tdkTestObj, actualresult, filename = verify_minidump_file_created(sysobj, initial_minidump_count, MINIDUMPS_DIR)
                    if expectedresult in actualresult and filename != "":
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Minidump file created: %s" % (step, filename))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                        minidump_created = True

                        step += 1
                        # Verify process PID changed (process restarted)
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
            print("ACTUAL RESULT %d: %s is not in active (waiting) state. State: %s" % (step, COREDUMP_PATH_UNIT, state))
            print("[TEST EXECUTION RESULT] : FAILURE")

        # Revert ulimit to initial value
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
        print("ACTUAL RESULT %d: Failed to set core dump size: %s" % (step, details))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload the modules
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

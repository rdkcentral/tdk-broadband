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
from DACVariables import *
from DACUtility import *
from tdkutility import *

# Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change, will be replaced with DUT details
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_DAC_VerifyBundleDownloadAndExecution')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus_sys.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Create DAC testing directory
    print("\nTEST STEP %d: Create directory %s for DAC testing" % (step, DAC_TEST_DIR))
    print("EXPECTED RESULT %d: Directory should be created successfully" % step)
    tdkTestObj, actualresult, details = create_directory(sysobj, DAC_TEST_DIR)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Directory created successfully" % step)
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Download OCI bundle
        print("\nTEST STEP %d: Download OCI bundle from local HTTP file server" % step)
        print("EXPECTED RESULT %d: Bundle should be downloaded successfully" % step)
        tdkTestObj, actualresult, details = download_file(sysobj, BUNDLE_DOWNLOAD_URL, DAC_TEST_DIR)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Bundle downloaded successfully" % step)
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Extract OCI bundle
            print("\nTEST STEP %d: Extract OCI bundle in %s directory" % (step, DAC_TEST_DIR))
            print("EXPECTED RESULT %d: Bundle should be extracted successfully" % step)
            tar_file_path = f"{DAC_TEST_DIR}/{OCI_BUNDLE_NAME}"
            tdkTestObj, actualresult, details = extract_tar_bundle(sysobj, OCI_BUNDLE_NAME, DAC_TEST_DIR)
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Bundle extracted successfully" % step)
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                # Verify bundle structure
                print("\nTEST STEP %d: Verify bundle structure" % step)
                print("EXPECTED RESULT %d: Bundle should have config.json and rootfs directory" % step)
                expected_files = ["config.json", "rootfs"]
                tdkTestObj, actualresult, details = verify_bundle_structure(sysobj, DAC_TEST_DIR, expected_files)
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Bundle structure verified. Details: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step += 1
                    # Verify iperf3 binary exists
                    print("\nTEST STEP %d: Verify iperf3 binary in rootfs" % step)
                    print("EXPECTED RESULT %d: iperf3 binary should exist" % step)
                    iperf3_check_path = f"{DAC_TEST_DIR}/rootfs/usr/bin"
                    expected_binaries = ["iperf3", "update-alternatives"]
                    tdkTestObj, actualresult, details = verify_bundle_structure(sysobj, iperf3_check_path, expected_binaries)
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: iperf3 binary verified. Details: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        step += 1
                        # Launch iperf3 server container
                        print("\nTEST STEP %d: Launch iperf3 server in DAC container" % step)
                        print("EXPECTED RESULT %d: Server container should start successfully" % step)
                        server_cmd = f"{IPERF3_BINARY_PATH} -s"
                        tdkTestObj, actualresult, details = start_dobby_container(sysobj, IPERF3_SERVER_CONTAINER, DAC_TEST_DIR, server_cmd)
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: Server container started. Details: %s" % (step, details))
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                            step += 1
                            # Confirm server container is running
                            print("\nTEST STEP %d: Confirm server container is running" % step)
                            print("EXPECTED RESULT %d: Server container should be in running state" % step)
                            tdkTestObj, actualresult, details = verify_container_running(sysobj, IPERF3_SERVER_CONTAINER)
                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: Server container is running. Details: %s" % (step, details))
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                step += 1
                                # Execute iperf3 client
                                print("\nTEST STEP %d: Execute iperf3 client inside container" % step)
                                print("EXPECTED RESULT %d: Client should execute and show performance results" % step)
                                client_cmd = f"{IPERF3_BINARY_PATH} -c {CONTAINER_IP} -t 60 -b 100M -P 4"
                                tdkTestObj, actualresult, details = start_dobby_container(sysobj, IPERF3_CLIENT_CONTAINER, DAC_TEST_DIR, client_cmd)
                                if expectedresult in actualresult:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print("ACTUAL RESULT %d: Client container started. Details: %s" % (step, details))
                                    print("[TEST EXECUTION RESULT] : SUCCESS")

                                    step += 1
                                    # Confirm both containers are running
                                    print("\nTEST STEP %d: Confirm both server and client containers are running" % step)
                                    print("EXPECTED RESULT %d: Both containers should be in running state" % step)
                                    sleep(2)
                                    container_list = [IPERF3_SERVER_CONTAINER, IPERF3_CLIENT_CONTAINER]
                                    tdkTestObj, actualresult, details = verify_multiple_containers_running(sysobj, container_list)
                                    if expectedresult in actualresult:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: Both containers are running. Details: %s" % (step, details))
                                        print("[TEST EXECUTION RESULT] : SUCCESS")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: Not all containers are running. Details: %s" % (step, details))
                                        print("[TEST EXECUTION RESULT] : FAILURE")

                                    step += 1
                                    # Stop server container
                                    print("\nTEST STEP %d: Stop the server container" % step)
                                    print("EXPECTED RESULT %d: Server container should stop successfully" % step)
                                    tdkTestObj, actualresult, details = stop_dobby_container(sysobj, IPERF3_SERVER_CONTAINER)
                                    if expectedresult in actualresult:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: Server container stopped. Details: %s" % (step, details))
                                        print("[TEST EXECUTION RESULT] : SUCCESS")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: Failed to stop server container. Details: %s" % (step, details))
                                        print("[TEST EXECUTION RESULT] : FAILURE")

                                    step += 1
                                    # Remove DAC directory
                                    print("\nTEST STEP %d: Remove the DAC directory" % step)
                                    print("EXPECTED RESULT %d: Directory should be removed successfully" % step)
                                    tdkTestObj, actualresult, details = remove_directory(sysobj, DAC_TEST_DIR)
                                    if expectedresult in actualresult:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: DAC directory removed successfully" % step)
                                        print("[TEST EXECUTION RESULT] : SUCCESS")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: Failed to remove DAC directory" % step)
                                        print("[TEST EXECUTION RESULT] : FAILURE")

                                    step += 1
                                    # Confirm no containers
                                    print("\nTEST STEP %d: Confirm no containers are running" % step)
                                    print("EXPECTED RESULT %d: Should show 'no containers'" % step)
                                    tdkTestObj, actualresult, details = verify_no_containers(sysobj)
                                    if expectedresult in actualresult:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: No containers running. Details: %s" % (step, details))
                                        print("[TEST EXECUTION RESULT] : SUCCESS")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: Containers still running. Details: %s" % (step, details))
                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("ACTUAL RESULT %d: Failed to start client container. Details: %s" % (step, details))
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: Server container is not running. Details: %s" % (step, details))
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Failed to start server container. Details: %s" % (step, details))
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: iperf3 binary not found. Details: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Bundle structure verification failed. Details: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to extract bundle. Details: %s" % (step, details))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to download bundle. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to create directory. Details: %s" % (step, details))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload the module
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

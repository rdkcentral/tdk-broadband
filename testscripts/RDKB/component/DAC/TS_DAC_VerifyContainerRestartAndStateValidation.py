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
sysobj.configureTestCase(ip,port,'TS_DAC_VerifyContainerRestartAndStateValidation')

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
        print("\nTEST STEP %d: Download OCI bundle from local file server" % step)
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
            tdkTestObj, actualresult, details = extract_tar_bundle(sysobj, OCI_BUNDLE_NAME, DAC_TEST_DIR)
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Bundle extracted successfully" % step)
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                # Verify bundle structure
                print("\nTEST STEP %d: Verify bundle structure" % step)
                print("EXPECTED RESULT %d: iperf3 and update-alternatives binaries should exist" % step)
                iperf3_check_path = f"{DAC_TEST_DIR}/rootfs/usr/bin/"
                expected_binaries = ["iperf3", "update-alternatives"]
                tdkTestObj, actualresult, details = verify_bundle_structure(sysobj, iperf3_check_path, expected_binaries)
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Bundle structure verified. Details: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step += 1
                    # Launch iperf3 server container with initial name
                    print("\nTEST STEP %d: Launch iperf3 server container with initial name" % step)
                    print("EXPECTED RESULT %d: Server container should start successfully" % step)
                    server_cmd = f"{IPERF3_BINARY_PATH} -s"
                    tdkTestObj, actualresult, details = start_dobby_container(sysobj, IPERF3_SERVER_CONTAINER, DAC_TEST_DIR, server_cmd)
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Server container started. Details: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        step += 1
                        # Verify server container is running
                        print("\nTEST STEP %d: Verify server container is running" % step)
                        print("EXPECTED RESULT %d: Server should be in running state with assigned descriptor" % step)
                        tdkTestObj, actualresult, details = verify_container_running(sysobj, IPERF3_SERVER_CONTAINER)
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: Server container is running. Details: %s" % (step, details))
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                            step += 1
                            # Test initial server functionality
                            print("\nTEST STEP %d: Test initial server functionality using crun exec" % step)
                            print("EXPECTED RESULT %d: Should show successful iperf3 test results" % step)
                            tdkTestObj, actualresult, details = execute_iperf_test(sysobj, IPERF3_SERVER_CONTAINER, CONTAINER_IP, 5)
                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: iperf3 test successful. Details: %s" % (step, details))
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                step += 1
                                # Stop the server container
                                print("\nTEST STEP %d: Stop the server container" % step)
                                print("EXPECTED RESULT %d: Container should stop successfully" % step)
                                tdkTestObj, actualresult, details = stop_dobby_container(sysobj, IPERF3_SERVER_CONTAINER)
                                if expectedresult in actualresult:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print("ACTUAL RESULT %d: Server container stopped. Details: %s" % (step, details))
                                    print("[TEST EXECUTION RESULT] : SUCCESS")

                                    step += 1
                                    # Verify container stopped and state cleared
                                    print("\nTEST STEP %d: Verify container stopped and state cleared" % step)
                                    print("EXPECTED RESULT %d: Should show 'no containers'" % step)
                                    tdkTestObj, actualresult, details = verify_no_containers(sysobj)
                                    if expectedresult in actualresult:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        print("ACTUAL RESULT %d: Container state cleared. Details: %s" % (step, details))
                                        print("[TEST EXECUTION RESULT] : SUCCESS")

                                        step += 1
                                        # Restart server container with same name
                                        print("\nTEST STEP %d: Restart server container with same name" % step)
                                        print("EXPECTED RESULT %d: Server should restart successfully" % step)
                                        tdkTestObj, actualresult, details = start_dobby_container(sysobj, IPERF3_SERVER_CONTAINER, DAC_TEST_DIR, server_cmd)
                                        if expectedresult in actualresult:
                                            tdkTestObj.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT %d: Server container restarted. Details: %s" % (step, details))
                                            print("[TEST EXECUTION RESULT] : SUCCESS")

                                            step += 1
                                            # Verify server restarted with new descriptor
                                            print("\nTEST STEP %d: Verify server restarted successfully with new descriptor" % step)
                                            print("EXPECTED RESULT %d: Server should be running with new descriptor" % step)
                                            tdkTestObj, actualresult, details = verify_container_running(sysobj, IPERF3_SERVER_CONTAINER)
                                            if expectedresult in actualresult:
                                                tdkTestObj.setResultStatus("SUCCESS")
                                                print("ACTUAL RESULT %d: Server restarted with new descriptor. Details: %s" % (step, details))
                                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                                step += 1
                                                # Test restarted server functionality
                                                print("\nTEST STEP %d: Test restarted server functionality" % step)
                                                print("EXPECTED RESULT %d: Server should operate normally after restart" % step)
                                                tdkTestObj, actualresult, details = execute_iperf_test(sysobj, IPERF3_SERVER_CONTAINER, CONTAINER_IP, 5)
                                                if expectedresult in actualresult:
                                                    tdkTestObj.setResultStatus("SUCCESS")
                                                    print("ACTUAL RESULT %d: Restarted server functioning normally. Details: %s" % (step, details))
                                                    print("[TEST EXECUTION RESULT] : SUCCESS")

                                                    step += 1
                                                    # Launch client container
                                                    print("\nTEST STEP %d: Launch client container to verify server-client communication" % step)
                                                    print("EXPECTED RESULT %d: Client container should start successfully" % step)
                                                    client_cmd = f"{IPERF3_BINARY_PATH} -c {CONTAINER_IP} -t 10"
                                                    tdkTestObj, actualresult, details = start_dobby_container(sysobj, IPERF3_CLIENT_CONTAINER, DAC_TEST_DIR, client_cmd)
                                                    if expectedresult in actualresult:
                                                        tdkTestObj.setResultStatus("SUCCESS")
                                                        print("ACTUAL RESULT %d: Client container started. Details: %s" % (step, details))
                                                        print("[TEST EXECUTION RESULT] : SUCCESS")

                                                        step += 1
                                                        # Verify both containers running
                                                        print("\nTEST STEP %d: Verify both server and client containers are running" % step)
                                                        print("EXPECTED RESULT %d: Both containers should be in running state" % step)
                                                        sleep(2)
                                                        container_list = [IPERF3_SERVER_CONTAINER, IPERF3_CLIENT_CONTAINER]
                                                        tdkTestObj, actualresult, details = verify_multiple_containers_running(sysobj, container_list)
                                                        if expectedresult in actualresult:
                                                            tdkTestObj.setResultStatus("SUCCESS")
                                                            print("ACTUAL RESULT %d: Both containers running. Details: %s" % (step, details))
                                                            print("[TEST EXECUTION RESULT] : SUCCESS")

                                                            step += 1
                                                            # Wait for client to complete
                                                            print("\nTEST STEP %d: Wait for client container to complete its test" % step)
                                                            print("EXPECTED RESULT %d: Client should complete after waiting" % step)
                                                            print("Waiting %d seconds for client to complete..." % CLIENT_COMPLETION_WAIT_TIME)
                                                            sleep(CLIENT_COMPLETION_WAIT_TIME)
                                                            tdkTestObj.setResultStatus("SUCCESS")
                                                            print("ACTUAL RESULT %d: Wait completed" % step)
                                                            print("[TEST EXECUTION RESULT] : SUCCESS")

                                                            step += 1
                                                            # Verify client auto-stopped
                                                            print("\nTEST STEP %d: Verify client auto-stopped after completion, server still running" % step)
                                                            print("EXPECTED RESULT %d: Only server should be running" % step)
                                                            # Verify server is still running
                                                            tdkTestObj, actualresult_server, details_server = verify_container_running(sysobj, IPERF3_SERVER_CONTAINER)
                                                            # Verify client is not running
                                                            tdkTestObj, actualresult_client, details_client = verify_container_running(sysobj, IPERF3_CLIENT_CONTAINER)
                                                            if actualresult_server == "SUCCESS" and actualresult_client == "FAILURE":
                                                                tdkTestObj.setResultStatus("SUCCESS")
                                                                print("ACTUAL RESULT %d: Client auto-stopped, server still running - Server: running, Client: stopped" % step)
                                                                print("[TEST EXECUTION RESULT] : SUCCESS")
                                                            else:
                                                                tdkTestObj.setResultStatus("FAILURE")
                                                                print("ACTUAL RESULT %d: Unexpected container state - Server: %s, Client: %s" % (step, actualresult_server, actualresult_client))
                                                                print("[TEST EXECUTION RESULT] : FAILURE")

                                                            step += 1
                                                            # Stop server container
                                                            print("\nTEST STEP %d: Cleanup - Stop the server container" % step)
                                                            print("EXPECTED RESULT %d: Server should stop successfully" % step)
                                                            tdkTestObj, actualresult, details = stop_dobby_container(sysobj, IPERF3_SERVER_CONTAINER)
                                                            if expectedresult in actualresult:
                                                                tdkTestObj.setResultStatus("SUCCESS")
                                                                print("ACTUAL RESULT %d: Server stopped. Details: %s" % (step, details))
                                                                print("[TEST EXECUTION RESULT] : SUCCESS")
                                                            else:
                                                                tdkTestObj.setResultStatus("FAILURE")
                                                                print("ACTUAL RESULT %d: Failed to stop server. Details: %s" % (step, details))
                                                                print("[TEST EXECUTION RESULT] : FAILURE")

                                                            step += 1
                                                            # Remove DAC directory
                                                            print("\nTEST STEP %d: Remove the DAC directory" % step)
                                                            print("EXPECTED RESULT %d: Directory should be removed successfully" % step)
                                                            tdkTestObj, actualresult, details = remove_directory(sysobj, DAC_TEST_DIR)
                                                            if expectedresult in actualresult:
                                                                tdkTestObj.setResultStatus("SUCCESS")
                                                                print("ACTUAL RESULT %d: DAC directory removed" % step)
                                                                print("[TEST EXECUTION RESULT] : SUCCESS")
                                                            else:
                                                                tdkTestObj.setResultStatus("FAILURE")
                                                                print("ACTUAL RESULT %d: Failed to remove directory" % step)
                                                                print("[TEST EXECUTION RESULT] : FAILURE")

                                                            step += 1
                                                            # Confirm all containers cleaned up
                                                            print("\nTEST STEP %d: Confirm all containers cleaned up" % step)
                                                            print("EXPECTED RESULT %d: Should show 'no containers'" % step)
                                                            tdkTestObj, actualresult, details = verify_no_containers(sysobj)
                                                            if expectedresult in actualresult:
                                                                tdkTestObj.setResultStatus("SUCCESS")
                                                                print("ACTUAL RESULT %d: All containers cleaned up. Details: %s" % (step, details))
                                                                print("[TEST EXECUTION RESULT] : SUCCESS")
                                                            else:
                                                                tdkTestObj.setResultStatus("FAILURE")
                                                                print("ACTUAL RESULT %d: Containers still present. Details: %s" % (step, details))
                                                                print("[TEST EXECUTION RESULT] : FAILURE")
                                                        else:
                                                            tdkTestObj.setResultStatus("FAILURE")
                                                            print("ACTUAL RESULT %d: Both containers not running - Server: %s, Client: %s" % (step, actualresult_server, actualresult_client))
                                                            print("[TEST EXECUTION RESULT] : FAILURE")
                                                    else:
                                                        tdkTestObj.setResultStatus("FAILURE")
                                                        print("ACTUAL RESULT %d: Failed to start client container. Details: %s" % (step, details))
                                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                                else:
                                                    tdkTestObj.setResultStatus("FAILURE")
                                                    print("ACTUAL RESULT %d: Restarted server not functioning. Details: %s" % (step, details))
                                                    print("[TEST EXECUTION RESULT] : FAILURE")
                                            else:
                                                tdkTestObj.setResultStatus("FAILURE")
                                                print("ACTUAL RESULT %d: Server not running after restart. Details: %s" % (step, details))
                                                print("[TEST EXECUTION RESULT] : FAILURE")
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT %d: Failed to restart server. Details: %s" % (step, details))
                                            print("[TEST EXECUTION RESULT] : FAILURE")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("ACTUAL RESULT %d: Container state not cleared. Details: %s" % (step, details))
                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("ACTUAL RESULT %d: Failed to stop server. Details: %s" % (step, details))
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: Initial server test failed. Details: %s" % (step, details))
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Server not running. Details: %s" % (step, details))
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Failed to start server. Details: %s" % (step, details))
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

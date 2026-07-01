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
import time
import tdkbE2EUtility
from tdkbE2EUtility import *
from tdkbStabilityVariables import *
from tdkbStabilityUtility import *

#Test component to be tested
obj1 = tdklib.TDKScriptingLibrary("sysutil","1")
obj2 = tdklib.TDKScriptingLibrary("tdkb_e2e","1")
obj3 = tdklib.TDKScriptingLibrary("tdkbtr181","1")

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj1.configureTestCase(ip,port,'TS_STABILITY_E2E_LongRunIPV4ConnectivityfromLanClient')
obj2.configureTestCase(ip,port,'TS_STABILITY_E2E_LongRunIPV4ConnectivityfromLanClient')
obj3.configureTestCase(ip,port,'TS_STABILITY_E2E_LongRunIPV4ConnectivityfromLanClient')

#Get the result of connection with test component
loadmodulestatus1 = obj1.getLoadModuleResult()
loadmodulestatus2 = obj2.getLoadModuleResult()
loadmodulestatus3 = obj3.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus1)
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus2)
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus3)

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper() and "SUCCESS" in loadmodulestatus3.upper():
    obj1.setLoadModuleStatus("SUCCESS")
    obj2.setLoadModuleStatus("SUCCESS")
    obj3.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"

    #Parse the device configuration file
    status = parseDeviceConfig(obj2)
    if expectedresult in status:
        obj2.setLoadModuleStatus("SUCCESS")
        print("Parsed the device configuration file successfully")
        step = 0
        testFailed = False
        failureReason = ""
        configFailed = False
        iteration = 0

        #Get the list of critical processes from configuration file
        step,processList,configFailed = get_processList_configFile(obj1,step)

        if not configFailed:
            #Get the current gateway ip address
            step += 1
            print(f"TEST STEP {step}: Get the current GW IP address")
            print(f"EXPECTED RESULT {step}: Should get the current GW IP address")
            param = "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress"
            tdkTestObj,status,curIPAddress = getParameterValue(obj2,param)
            if expectedresult in status and curIPAddress:
                print(f"ACTUAL RESULT {step}: Got the current GW IP address : {curIPAddress}")
                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                testFailed = True
                print(f"ACTUAL RESULT {step}: Failed to get the current GW IP address")
                failureReason = "gateway_ip_fetch_failed"
                tdkTestObj.setResultStatus("FAILURE")
                print("[TEST EXECUTION RESULT] : FAILURE")

        if not testFailed:
            print("\n" + "=" * 90)
            print(f"\nPing a IPV4 IP for {CONNECTIVITY_DURATION} seconds\n")
            print("=" * 90)

            #Send the ping command from lan client
            step += 1
            print(f"TEST STEP {step}: Start IPV4 ping from lan client for {CONNECTIVITY_DURATION} seconds")
            print(f"EXPECTED RESULT {step}: Ping should start successfully and run in background")
            status = verifyLongRunNetworkConnectivity(PUBLIC_IPV4,"PING_TO_IPV4",tdkbE2EUtility.lan_ip,curIPAddress)
            if expectedresult in status:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Ping started and output will be written to {PING_OUTPUT_FILE}")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                cpu_check_phase = "pre"
                health_check_phase = "pre"
                preCpuUsage = -1.0
                preFreeMemory = -1.0
                #Check the device health during test
                print("\n********Device Health check during ping test*******")
                for iteration in range(1, CONNECTIVITY_DURATION + 1):
                    if iteration % 10 == 0:
                        #Check if all critical processes are up
                        print(f"Check if all critical processes are up at iteration {iteration}")
                        step, testFailed, failureReason = get_status_processes(obj1, obj3, step, processList)
                        if testFailed:
                            break

                        if health_check_phase == "pre":
                            # Capture baseline values in free memory
                            print(f"Periodic pre memory check at iteration {iteration}")
                            step, testFailed, failureReason, preFreeMemory = get_freeMemory(obj1,step)
                            if testFailed:
                                failureReason = f"pre_{failureReason}"
                                break
                            health_check_phase = "post"
                        elif health_check_phase == "post":
                            # Capture next checkpoint as post and compare against previous baseline.
                            print(f"Periodic post memory check at iteration {iteration}")
                            step, testFailed, failureReason, postFreeMemory = get_freeMemory(obj1,step)
                            if testFailed:
                                failureReason = f"post_{failureReason}"
                                break
                            #compare pre and post values of free memory
                            step += 1
                            print(f"\nTEST STEP {step}: Verify that there's no memory leak")
                            print(f"EXPECTED RESULT {step} : There should not be any memory leak")
                            if preFreeMemory < 0 or postFreeMemory < 0:
                                testFailed = True
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: Memory parsing failed (pre={preFreeMemory}, post={postFreeMemory})")
                                print("[TEST EXECUTION RESULT] : FAILURE")
                                failureReason = "memory_parse_failed"
                                break
                            memoryThreshold = preFreeMemory * 0.90
                            memoryLoss = preFreeMemory - postFreeMemory
                            print(f"Memory: Pre={preFreeMemory}MB, Post={postFreeMemory}MB, Loss={memoryLoss}MB, Threshold={memoryThreshold}MB")
                            if postFreeMemory >= memoryThreshold:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("Confirms that there's no memory leak(memory loss <= 10%)")
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                testFailed = True
                                failureReason = "memory_leak_detected"
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"Failed to confirm that there's no memory leak(memory loss > 10%: {memoryLoss}MB lost)")
                                print("[TEST EXECUTION RESULT] : FAILURE")
                                break
                            health_check_phase = "pre"
                        #compare pre and post values of CPU Usage
                        if iteration % 50 == 0:
                            if cpu_check_phase == "pre":
                                print(f"Periodic pre CPU Usage check at iteration {iteration}")
                                step, testFailed, failureReason, preCpuUsage = get_device_CPUUsage(obj1, step)
                                if testFailed:
                                    failureReason = f"pre_{failureReason}"
                                    break
                                cpu_check_phase = "post"
                            elif cpu_check_phase == "post":
                                print(f"Periodic post CPU Usage check at iteration {iteration}")
                                step, testFailed, failureReason, postCpuUsage = get_device_CPUUsage(obj1, step)
                                if testFailed:
                                    failureReason = f"post_{failureReason}"
                                    break

                                step += 1
                                print(f"\nTEST STEP {step}: Verify that CPU did not spike during ping")
                                print(f"EXPECTED RESULT {step}: CPU usage should remain in safe limits")
                                cpuDelta = postCpuUsage - preCpuUsage
                                print(f"CPU: Pre={preCpuUsage}%, Post={postCpuUsage}%, Delta={cpuDelta:+.1f}%")
                                hardSpikeDetected = postCpuUsage > 90
                                softSpikeDetected = cpuDelta > 20 and postCpuUsage > 70
                                if not hardSpikeDetected and not softSpikeDetected:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print(f"ACTUAL RESULT {step}: CPU usage remained within the acceptable threshold")
                                    print("[TEST EXECUTION RESULT] : SUCCESS")
                                else:
                                    testFailed = True
                                    failureReason = "cpu_spike_detected"
                                    tdkTestObj.setResultStatus("FAILURE")
                                    if hardSpikeDetected:
                                        print("CPU hard-fail threshold exceeded (post CPU > 90%)")
                                    else:
                                        print("CPU soft-spike threshold exceeded (delta > 20 and post CPU > 70%)")
                                    print(f"ACTUAL RESULT {step}:Failed to confirm that CPU usage stayed within the acceptable threshold")
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                                    break
                                cpu_check_phase = "pre"
                    # Keep loop duration aligned with CONNECTIVITY_DURATION seconds.
                    time.sleep(1)

                if not testFailed:
                    # validate the output of ping command
                    step += 1
                    print(f"\nTEST STEP {step}: Validate long-run IPV4 ping output file")
                    print(f"EXPECTED RESULT {step}: 0% packet loss in ping output")
                    status = verifyLongRunNetworkConnectivity(PUBLIC_IPV4,"PING_TO_IPV4",tdkbE2EUtility.lan_ip,curIPAddress,"CHECK")
                    if expectedresult in status:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Ping output validation passed - {status}")
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        testFailed = True
                        failureReason = "ping_output_validation_failed"
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Ping output validation failed - {status}")
                        print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                testFailed = True
                failureReason = "ping_ipv4_failed"
                tdkTestObj.setResultStatus("FAILURE")
                print("Failed to ping from LAN to public IPV4")
                print("[TEST EXECUTION RESULT] : FAILURE")
        #On first failure, upload the device artifact to the upload server
        if testFailed:
            stability_type = "LongRunIPV4Connectivity"
            print("\n[ITERATION FAILURE] iteration=%d reason=%s" % (iteration, failureReason))
            status, artifact_details = collect_failure_artifacts(obj1, stability_type, iteration, failureReason, UPLOAD_SERVER_URL, FAILURE_ARTIFACT_ROOT)
            print("[ARTIFACT] Result: %s" % artifact_details['summary'])
            if status:
                print("[ARTIFACT] Tar file uploaded: %s" % artifact_details['tar_file'])
            else:
                print("[ARTIFACT] Collection or upload failed: %s" % artifact_details.get('details', 'No additional details'))
                print("[ARTIFACT] Failed command: %s" % artifact_details.get('failed_command', 'NA'))
            print("[STOP POLICY] Stopping test on first failure after artifact upload")
        else:
            print("\n[ITERATION PASS] iteration=%d completed successfully" % iteration)
    else:
        obj2.setLoadModuleStatus("FAILURE")
        print("Failed to parse the device configuration file")
    obj1.unloadModule("sysutil")
    obj2.unloadModule("tdkb_e2e")
    obj3.unloadModule("tdkbtr181")
else:
    print("Failed to load sysutil, tdkb_e2e and tdkbtr181 module")
    obj1.setLoadModuleStatus("FAILURE")
    obj2.setLoadModuleStatus("FAILURE")
    obj3.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

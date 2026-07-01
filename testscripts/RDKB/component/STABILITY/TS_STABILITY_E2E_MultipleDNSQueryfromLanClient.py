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
obj1.configureTestCase(ip,port,'TS_STABILITY_E2E_MultipleDNSQueryfromLanClient')
obj2.configureTestCase(ip,port,'TS_STABILITY_E2E_MultipleDNSQueryfromLanClient')
obj3.configureTestCase(ip,port,'TS_STABILITY_E2E_MultipleDNSQueryfromLanClient')

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
            #Get the primary DNS server
            dnsServer = "Device.DNS.Client.Server.1.DNSServer"
            step += 1
            print(f"\nTEST STEP {step}: Get the current value of DNS Server")
            print(f"EXPECTED RESULT {step}: Should retrieve the current value of DNS Server")
            tdkTestObj,status,dnsServerIp = getParameterValue(obj2,dnsServer)
            if expectedresult in status and dnsServerIp != "":
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: {dnsServerIp}")
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                testFailed = True
                failureReason = "dns_server_fetch_failed"
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step} : Failed to get current value of DNS Server")
                print("[TEST EXECUTION RESULT] : FAILURE")

        if not testFailed :
            for iteration in range(1, CONNECTIVITY_ITERATIONS + 1):
                #Check the device health before test
                print("\n *****Pre checks on Device Health*****")
                # Periodic post CPU Usage check on every 10 iterations
                if iteration % 10 == 0:
                    step += 1
                    print(f"Periodic pre CPU Usage check at iteration {iteration}")
                    step,testFailed,failureReason,preCpuUsage = get_device_CPUUsage(obj1,step)
                    if testFailed:
                        failureReason = f"pre_{failureReason}"
                        break
                #Get the status of dns process
                step+=1
                step,testFailed,failureReason,prePid = get_process_status(obj1,step,DNS_PROCESS)
                if testFailed:
                    failureReason = f"pre_{failureReason}"
                    break
                #Get the free memory of the device
                step,testFailed,failureReason,preFreeMemory = get_freeMemory(obj1,step)
                if testFailed:
                    failureReason = f"pre_{failureReason}"
                    break
                #Send the DNS query
                print("\n" + "=" * 90)
                print(f"\nSending DNS QUERY : {iteration}\n")
                print("=" * 90)

                #Resolving domain name with nslookup in LAN Client
                step += 1
                print(f"TEST STEP {step}:Connect to LAN Client and do NSLookup")
                status=nslookupInClient(tdkbE2EUtility.nslookup_domain_name,dnsServerIp,'LAN')
                if expectedresult in status:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("DNS Primary Server successfully resolves the DNS query")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    #Check the device health after test
                    print("\n *****Post checks on Device Health*****")
                    # Periodic post CPU Usage check on every 10 iterations
                    if iteration % 10 == 0:
                        step += 1
                        print(f"Periodic post CPU Usage check at iteration {iteration}")
                        step,testFailed,failureReason,postCpuUsage = get_device_CPUUsage(obj1,step)
                        if testFailed:
                            failureReason = f"post_{failureReason}"
                            break
                    #Get the status of dns process
                    step+=1
                    step,testFailed,failureReason,postPid = get_process_status(obj1,step,DNS_process)
                    if testFailed:
                        failureReason = f"post_{failureReason}"
                        break
                    #Get the free memory of the device
                    step,testFailed,failureReason,postFreeMemory = get_freeMemory(obj1,step)
                    if testFailed:
                        failureReason = f"post_{failureReason}"
                        break
                    #Check if all critical processes are up
                    step+=1
                    step,testFailed,failureReason = get_status_processes(obj1,obj3,step,processList)
                    if testFailed:
                        break
                    #compare the pre and post values of process PID, memory and CPU Usage
                    step += 1
                    print(f"\nTEST STEP {step} : Verify that DNS process didn't crash")
                    print(f"EXPECTED RESULT {step}: DNS process should not crash")
                    if prePid == postPid:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("Same PID confirms that there's no DNS process crash")
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        testFailed = True
                        failureReason = "processPID_compare_failed"
                        tdkTestObj.setResultStatus("FAILURE")
                        print("Failed to confirm that DNS process didn't crash")
                        print("[TEST EXECUTION RESULT] : FAILURE")
                        break

                    if iteration % 10 == 0:
                        step += 1
                        print(f"\nTEST STEP {step}: Verify that CPU did not spike during the DNS query")
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

                    step += 1
                    print(f"\nTEST STEP {step}: Verify that there's no memory leak")
                    print(f"EXPECTED RESULT {step} : There should not be any memory leak")
                    if preFreeMemory < 0 or postFreeMemory < 0:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Memory parsing failed (pre={preFreeMemory}, post={postFreeMemory})")
                        print("[TEST EXECUTION RESULT] : FAILURE")
                        iterationFailed = True
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
                else:
                    testFailed = True
                    failureReason = "dns_query_failed"
                    tdkTestObj.setResultStatus("FAILURE")
                    print("DNS Primary Server failed to resolve the DNS query")
                    print("[TEST EXECUTION RESULT] : FAILURE")
                    break
        #On first failure, upload the device artifact to the upload server
        if testFailed:
            stability_type = "MultipleDNSQueryStability"
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
    print("Failed to load sysutil,tdkb e2e and tdkbtr181 module")
    obj1.setLoadModuleStatus("FAILURE")
    obj2.setLoadModuleStatus("FAILURE")
    obj3.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

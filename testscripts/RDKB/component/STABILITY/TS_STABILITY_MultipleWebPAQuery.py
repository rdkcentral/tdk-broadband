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
from tdkbVariables import *
from tdkbStabilityVariables import *
from tdkbStabilityUtility import *
from webpaUtility import *

def create_webpa_test_step(obj):
    tdkTestObj = obj.createTestStep('ExecuteCmd')
    tdkTestObj.executeTestCase("SUCCESS")
    return tdkTestObj

def get_webpa_parameter_value(obj, step, dmConfig, actionLabel):
    step += 1
    failureReason = ""
    testFailed = False
    value = ""
    parameterName = dmConfig["name"]
    print(f"\nTEST STEP {step}: {actionLabel} for {parameterName}")
    print(f"EXPECTED RESULT {step}: Should get a valid value for {parameterName}")
    queryParam = {"name": parameterName}
    queryResponse = webpaQuery(obj, queryParam)
    parsedResponse = parseWebpaResponse(queryResponse, 1)
    tdkTestObj = create_webpa_test_step(obj)
    if "SUCCESS" in parsedResponse[0] and parsedResponse[1] != "":
        value = dmConfig["normalize"](parsedResponse[1].strip())
        if value in dmConfig["validValues"]:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: {parameterName} = {value}")
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            testFailed = True
            failureReason = f"invalid_value_{stability_sanitize_tag(parameterName)}"
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Invalid value received for {parameterName}: {value}")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        testFailed = True
        failureReason = f"get_failed_{stability_sanitize_tag(parameterName)}"
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to get {parameterName}")
        print("[TEST EXECUTION RESULT] : FAILURE")
    return step, testFailed, failureReason, value

def set_and_verify_webpa_parameter(obj, step, dmConfig, setValue):
    step += 1
    failureReason = ""
    testFailed = False
    parameterName = dmConfig["name"]
    print(f"\nTEST STEP {step}: Set {parameterName} to {setValue}")
    print(f"EXPECTED RESULT {step}: {parameterName} should be set successfully")
    queryParam = {"name": parameterName, "value": setValue, "dataType": dmConfig["dataType"]}
    queryResponse = webpaQuery(obj, queryParam, "set")
    parsedResponse = parseWebpaResponse(queryResponse, 1, "set")
    tdkTestObj = create_webpa_test_step(obj)
    if "SUCCESS" in parsedResponse[0]:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Set operation succeeded for {parameterName}")
        print("[TEST EXECUTION RESULT] : SUCCESS")
        time.sleep(90)
        step, testFailed, failureReason, verifiedValue = get_webpa_parameter_value(obj, step, dmConfig, f"Verify the set value of {parameterName}")
        if not testFailed and verifiedValue == setValue:
            print(f"Verified that {parameterName} is updated to {verifiedValue}")
        elif not testFailed:
            testFailed = True
            failureReason = f"verify_failed_{stability_sanitize_tag(parameterName)}"
            tdkTestObj.setResultStatus("FAILURE")
            print(f"Failed to verify the set value for {parameterName}. Expected {setValue}, got {verifiedValue}")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        testFailed = True
        failureReason = f"set_failed_{stability_sanitize_tag(parameterName)}"
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to set {parameterName}")
        print("[TEST EXECUTION RESULT] : FAILURE")
    return step, testFailed, failureReason

def revert_original_values(obj, step, dmConfigList, originalValues):
    revertFailed = False
    failureReason = ""
    for dmConfig in dmConfigList:
        parameterName = dmConfig["name"]
        originalValue = originalValues.get(parameterName)
        if originalValue is None:
            continue
        step, currentFailed, currentReason, currentValue = get_webpa_parameter_value(obj, step, dmConfig, f"Get current value before reverting {parameterName}")
        if currentFailed:
            return step, True, f"revert_{currentReason}"
        if currentValue == originalValue:
            print(f"{parameterName} is already at its original value {originalValue}")
            continue
        step, revertFailed, failureReason = set_and_verify_webpa_parameter(obj, step, dmConfig, originalValue)
        if revertFailed:
            return step, True, f"revert_{failureReason}"
    return step, False, ""

#Test component to be tested
obj1 = tdklib.TDKScriptingLibrary("sysutil","1")
obj2 = tdklib.TDKScriptingLibrary("tdkbtr181","1")

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj1.configureTestCase(ip,port,'TS_STABILITY_MultipleWebPAQuery')
obj2.configureTestCase(ip,port,'TS_STABILITY_MultipleWebPAQuery')

#Get the result of connection with test component
loadmodulestatus1 = obj1.getLoadModuleResult()
loadmodulestatus2 = obj2.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus1)
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus2)

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    obj1.setLoadModuleStatus("SUCCESS")
    obj2.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"

    step = 0
    testFailed = False
    failureReason = ""
    currentIteration = 0
    webpaProcess = "webpa"
    parodusProcess = "parodus"
    originalValues = {}
    iteration = 0
    dmConfigList = [
        {
            "name": "Device.X_CISCO_COM_Security.Firewall.FirewallLevel",
            "dataType": 0,
            "validValues": {"High", "Low", "Medium"},
            "alternateValues": {"Low": "Medium", "Medium": "Low", "High": "Low"},
            "normalize": lambda value: value.strip()
        },
        {
            "name": "Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable",
            "dataType": 3,
            "validValues": {"true", "false"},
            "alternateValues": {"true": "false", "false": "true"},
            "normalize": lambda value: value.strip().lower()
        }
    ]

    tdkTestObj,preRequisiteStatus = webpaPreRequisite(obj1)
    if "SUCCESS" in preRequisiteStatus:
        configFailed = False

        #Get the list of critical processes from configuration file
        step,processList,configFailed = get_processList_configFile(obj1,step)
        #Get the status of processes
        if not configFailed :
            step, testFailed, failureReason = get_status_processes(obj1,obj2,step,processList)
            if testFailed:
                failureReason = f"pre_{failureReason}"

        if not configFailed and not testFailed:
            print("\n*****Saving original values of WebPA parameters*****")
            for dmConfig in dmConfigList:
                step, testFailed, failureReason, originalValue = get_webpa_parameter_value(obj1, step, dmConfig, f"Get the original value of {dmConfig['name']}")
                if testFailed:
                    failureReason = f"original_{failureReason}"
                    break
                originalValues[dmConfig["name"]] = originalValue

        if not configFailed and not testFailed:
            for iteration in range(1, CONNECTIVITY_ITERATIONS + 1):
                currentIteration = iteration
                preCpuUsage = -1.0
                postCpuUsage = -1.0
                #Check the device health before test
                print("\n *****Pre checks on Device Health*****")
                # Periodic pre CPU Usage check on every 10 iterations
                if iteration % 10 == 0:
                    step += 1
                    print(f"\nPeriodic pre CPU Usage check at iteration {iteration}")
                    step,testFailed,failureReason,preCpuUsage = get_device_CPUUsage(obj1,step)
                    if testFailed:
                        failureReason = f"pre_{failureReason}"
                        break

                #Periodic pre webpa process check
                step,testFailed,failureReason,prePid1 = get_process_status(obj1,step,webpaProcess)
                if testFailed:
                    failureReason = f"pre_{failureReason}"
                    break
                #Periodic pre parodus process check
                step,testFailed,failureReason,prePid2 = get_process_status(obj1,step,parodusProcess)
                if testFailed:
                    failureReason = f"pre_{failureReason}"
                    break
                #Periodic pre free memory check
                step,testFailed,failureReason,preFreeMemory = get_freeMemory(obj1,step)
                if testFailed:
                    failureReason = f"pre_{failureReason}"
                    break

                #Send Webpa configuration change query
                print("\n" + "=" * 90)
                print(f"\nSending Webpa configuration change query : {iteration}\n")
                print("=" * 90)
                dmConfig = dmConfigList[(iteration - 1) % len(dmConfigList)]
                step, testFailed, failureReason, currentValue = get_webpa_parameter_value(obj1, step, dmConfig, f"Get the current value of {dmConfig['name']}")
                if testFailed:
                    break

                newValue = dmConfig["alternateValues"].get(currentValue)
                if newValue is None:
                    testFailed = True
                    failureReason = f"alternate_value_missing_{stability_sanitize_tag(dmConfig['name'])}"
                    print(f"Failed to determine alternate value for {dmConfig['name']} from current value {currentValue}")
                    break
                #Get and set webpa parameters
                step, testFailed, failureReason = set_and_verify_webpa_parameter(obj1, step, dmConfig, newValue)
                if testFailed:
                    break

                #Check the device health after test
                print("\n *****Post checks on Device Health*****")
                # Periodic post CPU Usage check on every 10 iterations
                if iteration % 10 == 0:
                    step += 1
                    print(f"\nPeriodic post CPU Usage check at iteration {iteration}")
                    step,testFailed,failureReason,postCpuUsage = get_device_CPUUsage(obj1,step)
                    if testFailed:
                        failureReason = f"post_{failureReason}"
                        break
                #Periodic specific process check
                step,testFailed,failureReason,postPid1 = get_process_status(obj1,step,webpaProcess)
                if testFailed:
                    failureReason = f"post_{failureReason}"
                    break
                #Periodic specific process check
                step,testFailed,failureReason,postPid2 = get_process_status(obj1,step,parodusProcess)
                if testFailed:
                    failureReason = f"post_{failureReason}"
                    break
                #Periodic get free memory
                step,testFailed,failureReason,postFreeMemory = get_freeMemory(obj1,step)
                if testFailed:
                    failureReason = f"post_{failureReason}"
                    break

                #Get the status of processes
                step,testFailed,failureReason = get_status_processes(obj1,obj2,step,processList)
                if testFailed:
                    break

                tdkTestObj = create_webpa_test_step(obj1)
                #Check the status of specific processes
                step += 1
                print(f"\nTEST STEP {step}: Verify that {webpaProcess} process didn't crash")
                print(f"EXPECTED RESULT {step}: {webpaProcess} process should not crash")
                if prePid1 == postPid1:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"Same PID confirms that there's no {webpaProcess} process crash")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    testFailed = True
                    failureReason = f"{webpaProcess}_processPID_compare_failed"
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"Failed to confirm that {webpaProcess} process didn't crash")
                    print("[TEST EXECUTION RESULT] : FAILURE")
                    break

                step += 1
                print(f"\nTEST STEP {step}: Verify that {parodusProcess} process didn't crash")
                print(f"EXPECTED RESULT {step}: {parodusProcess} process should not crash")
                if prePid2 == postPid2:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"Same PID confirms that there's no {parodusProcess} process crash")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    testFailed = True
                    failureReason = f"{parodusProcess}_processPID_compare_failed"
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"Failed to confirm that {parodusProcess} process didn't crash")
                    print("[TEST EXECUTION RESULT] : FAILURE")
                    break

                if iteration % 10 == 0:
                    step += 1
                    print(f"\nTEST STEP {step}: Verify that CPU did not spike during the WebPA query")
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
                        print(f"ACTUAL RESULT {step}: Failed to confirm that CPU usage stayed within the acceptable threshold")
                        print("[TEST EXECUTION RESULT] : FAILURE")
                        break

                step += 1
                print(f"\nTEST STEP {step}: Verify that there's no memory leak")
                print(f"EXPECTED RESULT {step}: There should not be any memory leak")
                if preFreeMemory < 0 or postFreeMemory < 0:
                    testFailed = True
                    failureReason = "memory_parse_failed"
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Memory parsing failed (pre={preFreeMemory}, post={postFreeMemory})")
                    print("[TEST EXECUTION RESULT] : FAILURE")
                    break

                memoryThreshold = preFreeMemory * 0.90
                memoryLoss = preFreeMemory - postFreeMemory
                print(f"Memory: Pre={preFreeMemory}MB, Post={postFreeMemory}MB, Loss={memoryLoss}MB, Threshold={memoryThreshold}MB")
                if postFreeMemory >= memoryThreshold:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("Confirms that there's no memory leak(memory loss <= 10%)")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                    print("\n[ITERATION PASS] iteration=%d completed successfully" % iteration)
                else:
                    testFailed = True
                    failureReason = "memory_leak_detected"
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"Failed to confirm that there's no memory leak(memory loss > 10%: {memoryLoss}MB lost)")
                    print("[TEST EXECUTION RESULT] : FAILURE")
                    break

        if testFailed:
            stability_type = "MultipleWebpaQueryStability"
            print("\n[ITERATION FAILURE] iteration=%d reason=%s" % (iteration, failureReason))
            status, artifact_details = collect_failure_artifacts(obj1, stability_type, iteration, failureReason, UPLOAD_SERVER_URL, FAILURE_ARTIFACT_ROOT)
            print("[ARTIFACT] Result: %s" % artifact_details['summary'])
            if status:
                print("[ARTIFACT] Tar file uploaded: %s" % artifact_details['tar_file'])
            else:
                print("[ARTIFACT] Collection or upload failed: %s" % artifact_details.get('details', 'No additional details'))
                print("[ARTIFACT] Failed command: %s" % artifact_details.get('failed_command', 'NA'))
            print("[STOP POLICY] Stopping test on first failure after artifact upload")

        if originalValues:
            print("\n*****Reverting WebPA parameters to original values*****")
            step, revertFailed, revertFailureReason = revert_original_values(obj1, step, dmConfigList, originalValues)
            if revertFailed:
                if not testFailed:
                    testFailed = True
                    failureReason = revertFailureReason
                    upload_failure_artifacts(obj1, currentIteration, failureReason)
                else:
                    print(f"Failed to revert parameters after primary failure. Reason: {revertFailureReason}")
    else:
        testFailed = True
        failureReason = "webpa_prerequisite_failed"
        tdkTestObj.setResultStatus("FAILURE")
        print("Webpa Pre-requisite failed. Please check parodus and webpa processes are running in device")
        upload_failure_artifacts(obj1, currentIteration, failureReason)
    obj1.unloadModule("sysutil")
    obj2.unloadModule("tdkbtr181")
else:
    print("Failed to load tdkbtr181 and sysutil module")
    obj1.setLoadModuleStatus("FAILURE")
    obj2.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
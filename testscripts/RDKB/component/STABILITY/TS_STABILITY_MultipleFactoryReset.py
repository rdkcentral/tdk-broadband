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
from tdkutility import *
from tdkbStabilityVariables import *
from tdkbStabilityUtility import *

#Test component to be tested
obj1 = tdklib.TDKScriptingLibrary("sysutil","1")
obj2 = tdklib.TDKScriptingLibrary("tdkbtr181","1")

#IP and Port of device type, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj1.configureTestCase(ip,port,'TS_STABILITY_MultipleFactoryReset')
obj2.configureTestCase(ip,port,'TS_STABILITY_MultipleFactoryReset')

#Get the result of connection with test component and DUT
loadmodulestatus1 = obj1.getLoadModuleResult()
loadmodulestatus2 = obj2.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus1)
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus2)

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    obj1.setLoadModuleStatus("SUCCESS")
    obj2.setLoadModuleStatus("SUCCESS")
    step=0
    expectedresult="SUCCESS"
    testFailed = False
    iterationFailed = False
    iteration = 0

    #Get the max wait time of any process from configuration file
    step,waitTime,testFailed = get_waitTime_configFile(obj1,step)
    if not testFailed:
        #Get the list of interfaces from configuration file
        step,interfaceList,testFailed = get_interfaceList_configFile(obj1,step)
    if not testFailed:
        #Get the list of critical processes from configuration file
        step,processList,testFailed = get_processList_configFile(obj1,step)

    if not testFailed:
        for iteration in range(1, TOTAL_ITERATIONS + 1):
            failureReason = ""
            #save device's current state before it goes for reboot
            obj1.saveCurrentState()
            print("\n" + "=" * 90)
            print(f"\nFactory resetting the device: {iteration}")
            print("=" * 90)

            tdkTestObj = obj2.createTestStep('TDKB_TR181Stub_SetOnly')
            actualresult ,details = setTR181Value(tdkTestObj,"Device.X_CISCO_COM_DeviceControl.FactoryReset","Router,Wifi,VoIP,Dect,MoCA","string")
            if expectedresult in actualresult:
                print("Factory resetted the device successfully")
                tdkTestObj.setResultStatus("SUCCESS")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                #Restore the device state saved before reboot
                obj1.restorePreviousStateAfterReboot()
                sleep(300)

                print("\n ******* Device Health checks post Factory Reset *******")
                #Get uptime of the device
                step,upTime,iterationFailed,failureReason = get_device_uptime(obj2,step)
                if iterationFailed:
                    break
                #Check if the uptime matches with the wait time , else wait till the wait time
                if not iterationFailed and int(upTime) < int(waitTime):
                    sleepTime = (int(waitTime) - int(upTime))
                    print(f" *********Sleeping for {sleepTime}sec to check if the processes are up to reach a wait time of {waitTime} sec ****")
                    sleep(sleepTime)
                #Check the status of interfaces
                if not iterationFailed:
                    step,iterationFailed,failureReason = get_status_interfaces(obj1,step,interfaceList)
                    if iterationFailed:
                        break
                #Check the status of critical processes
                if not iterationFailed:
                    step,iterationFailed,failureReason = get_status_processes(obj1,obj2,step,processList)
                    if iterationFailed:
                        break
            else:
                iterationFailed = True
                print("Failed to factory reset the device")
                failureReason = "factory_reset_failed"
                tdkTestObj.setResultStatus("FAILURE")
                print("[TEST EXECUTION RESULT] : FAILURE")
                break
    #On first failure, upload the device artifact to the upload server
    if iterationFailed:
        stability_type = "MultipleFactoryResetStability"
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

    obj1.unloadModule("sysutil")
    obj2.unloadModule("tdkbtr181")
else:
    print("Failed to load module")
    obj1.setLoadModuleStatus("FAILURE")
    obj2.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
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


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
from tdkbVariables import *
import time
from time import sleep
from xfinityWiFiLib import *
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1")
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1")
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckProcessUptimeAfterFactoryRest')
obj1.configureTestCase(ip,port,'TS_SANITY_CheckProcessUptimeAfterFactoryReset')

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult()
loadmodulestatus1 =obj1.getLoadModuleResult()


if "SUCCESS" in loadmodulestatus.upper() and loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")

    step = 1
    tdkTestObj = obj.createTestStep('ExecuteCmd')
    expectedresult ="SUCCESS"
    cmd = f"sh {TDK_PATH}/tdk_utility.sh parseConfigFile MAX_PROCESSUP_WAITTIME"
    tdkTestObj.addParameter("command",cmd)
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    WaitTime  = tdkTestObj.getResultDetails().strip().replace("\\n", "")
    print(f"TEST STEP {step}: Get the Wait time to Check if the processes are up")
    print(f"EXPECTED RESULT {step}: Should get the Wait time to Check if the processes are up")
    if expectedresult in actualresult and WaitTime!="":
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: ",WaitTime)
        print("[TEST EXECUTION RESULT] : SUCCESS")
        print("****DUT is going for a Factory Reset and will be up after FR*****")

        step = step + 1
        print(f"TEST STEP {step}: Initiate factory reset ")
        print(f"EXPECTED RESULT {step}: Should initiate factory reset ")

        #Initiate a device FR
        obj1.saveCurrentState()
        tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_SetOnly')
        tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset")
        tdkTestObj.addParameter("ParamValue","Router,Wifi,VoIP,Dect,MoCA")
        tdkTestObj.addParameter("Type","string")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step} : SUCCESS")
            obj1.restorePreviousStateAfterReboot()

            tdkTestObj = obj.createTestStep('ExecuteCmd')
            cmd = "uptime"
            tdkTestObj.addParameter("command",cmd)
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            upTimeRaw  = tdkTestObj.getResultDetails().strip().replace("\\n", "")

            step = step + 1
            print(f"TEST STEP {step}: Get the Uptime of the DUT")
            print(f"EXPECTED RESULT {step}: Should get the Uptime of the DUT")
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                parts = upTimeRaw.split()
                if "up" in parts:
                    index = parts.index("up")
                    uptime_min = int(parts[index + 1])
                    upTime = uptime_min * 60
                    print(f"Uptime in seconds is {upTime}")
                else:
                    print("unknown error occured while converting uptime to seconds")
                print(f"ACTUAL RESULT {step}: Uptime of the DUT is :",upTime)
                print("[TEST EXECUTION RESULT] : SUCCESS")

                if int(upTime) < int(WaitTime):
                    sleepTime = (int(WaitTime) -int(upTime))
                    print(f" *********Sleeping for {sleepTime} sec to check if the processes are up to reach a wait time of {WaitTime} sec ****")
                    sleep(sleepTime)

                tdkTestObj = obj.createTestStep('ExecuteCmd')
                List = ["CCSP_PROCESS","SNMP_PROCESS","WEBPA_PROCESS","LIGHTTPD_PROCESS","DROPBEAR_PROCESS","NOTIFYCOMP_PROCESS","WEBCONFIG_PROCESS","PSM_PROCESS","TELEMETRY_PROCESS","WIFI_PROCESS"]
                process_List = []
                for item in List :
                    Process= f"sh {TDK_PATH}/tdk_utility.sh parseConfigFile {item}"
                    print(Process)
                    expectedresult="SUCCESS"
                    tdkTestObj.addParameter("command",Process)
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    getProcess = tdkTestObj.getResultDetails().strip()
                    getProcess = getProcess.replace("\\n", "")

                    if "Invalid Argument passed" in getProcess or getProcess == "":
                        print(f"[INFO] {item} not defined in platform properties. Skipping...")
                        continue
                    if getProcess !="":
                        getProcess=getProcess.split(",")
                        process_List.append(getProcess)

                processList = []
                processList = [ item for elem in process_List for item in elem]

                step = step + 1
                print(f"TEST STEP {step}: Get the list of processes ")
                print(f"EXPECTED RESULT {step}: Should get the list of processes")
                if processList != "":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: List of process: {processList}")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    for item in processList:
                        if item == "CcspHotspot":
                            tdkTestObj= obj1.createTestStep('TDKB_TR181Stub_Get')
                            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable")
                            expectedresult="SUCCESS"
                            tdkTestObj.executeTestCase(expectedresult)
                            actualresult = tdkTestObj.getResult()
                            details = tdkTestObj.getResultDetails()

                            if expectedresult in  actualresult and details == "true":
                                command1 = f"pidof {item}"
                                tdkTestObj = obj.createTestStep('ExecuteCmd')
                                tdkTestObj.addParameter("command", command1)
                                tdkTestObj.executeTestCase(expectedresult)
                                actualresult = tdkTestObj.getResult()
                                details = tdkTestObj.getResultDetails().strip()
                                details = details.replace("\\n", "")
                                if expectedresult in actualresult and "" != details:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print(f"Process Name : {item}")
                                    print(f"PID : {details}")
                                    print(f"{item} with process ID {details} is running")
                                    print("[TEST EXECUTION RESULT] : SUCCESS")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print(f"Process Name : {item}")
                                    print(f"{item} is not running")
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("Since xfinitywifi is disabled CcspHotspot is not running")
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                        else:
                            command1 = "pidof %s" %item
                            tdkTestObj = obj.createTestStep('ExecuteCmd')
                            tdkTestObj.addParameter("command", command1)
                            tdkTestObj.executeTestCase(expectedresult)
                            actualresult = tdkTestObj.getResult()
                            details = tdkTestObj.getResultDetails().strip()
                            details = details.replace("\\n", "")
                            if expectedresult in actualresult and "" != details:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"Process Name : {item}")
                                print(f"PID : {details}")
                                print(f"{item} with process ID {details} is running")
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"Process Name : {item}")
                                print(f"{item} is not running")
                                print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Process list returned empty.ProcessList :{processList}")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Uptime of the DUT is :",upTimeRaw)
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: {details}")
            print("[TEST EXECUTION RESULT] :FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: ",WaitTime)
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("sysutil")
    obj1.unloadModule("tdkbtr181")
else:
    print("Failed to load sysutil and tdkbtr181 module")
    obj.setLoadModuleStatus("FAILURE")
    obj1.setLoadModuleStatus("FAILURE")
    print("Module loading failed")


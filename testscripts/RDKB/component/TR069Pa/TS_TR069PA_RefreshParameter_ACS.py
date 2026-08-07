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
from tr69ACSUtility import *
from time import sleep

#Test component to be tested
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

#IP and Port of device type, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
tr181obj.configureTestCase(ip,port,'TS_TR069PA_RefreshParameter_ACS')
sysobj.configureTestCase(ip,port,'TS_TR069PA_RefreshParameter_ACS')

#Get the result of connection with test component and DUT
loadmodulestatus=tr181obj.getLoadModuleResult()
loadmodulestatus1=sysobj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    tr181obj.setLoadModuleStatus("SUCCESS")

    #Check for prerequisites
    tdkTestObj,username,initialValues,preRequisiteStatus = tr069ACSPreRequisite(tr181obj,sysobj)
    if "SUCCESS" in preRequisiteStatus:
        step = 0
        queryParam = {"name":"Device.Time"}
        name = queryParam.get("name")

        #Perform Refresh task request for the parameter
        step += 1
        print("\nTEST STEP %d: Send RefreshObject task on %s via ACS." %(step,name))
        print("EXPECTED RESULT %d: Send RefreshObject task on %s via ACS successfully." %(step,name))
        status, queryResponse = tr069ACSQuery(username, queryParam, method="RefreshObject")
        if status == 200 and queryResponse is not None:
            # Task executed synchronously - proceed directly
            print("ACTUAL RESULT %d: RefreshObject Task successful for %s via ACS server." % (step,name))
            if queryResponse.get("objectName") == name:
                tdkTestObj.setResultStatus("SUCCESS")
                print("Refresh object name matches.")
                print("[TEST EXECUTION RESULT] : SUCCESS")
                print("Wait for 1 minute to complete the refreshing of the parameter.")
                sleep(60)
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("Refresh object name failed to  match.")
                print("[TEST EXECUTION RESULT] : FAILURE")
        elif status == 202 and queryResponse is not None:
            # Task queued - poll to detect offline device, auth failure, or RPC fault
            if waitForTaskCompletionIfQueued(tdkTestObj, status, queryResponse, step, "RefreshObject", username):
                print("ACTUAL RESULT %d: RefreshObject Task successful for %s via ACS server." % (step,name))
                if queryResponse.get("objectName") == name:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("Refresh object name matches.")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    print("Wait for 1 minute to complete the refreshing of the parameter.")
                    sleep(60)
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("Refresh object name failed to  match.")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: RefreshObject task failed during queued execution validation." % step)
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: RefreshObject Task failed to get %s with status %d." % (step,name,status))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("tr069pa Pre-requisite failed. Please check if tr069 process is running in device or configuration is proper or connection is established.")
        print("[TEST EXECUTION RESULT] : FAILURE")

    revertPrerequisite(tr181obj,initialValues,step)

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("FAILURE to load module.")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")

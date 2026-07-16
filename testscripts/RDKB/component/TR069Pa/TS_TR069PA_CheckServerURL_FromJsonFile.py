##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TR069PA_CheckServerURL_FromJsonFile')
sysobj.configureTestCase(ip,port,'TS_TR069PA_CheckServerURL_FromJsonFile')

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult()
loadmodulestatus1=sysobj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult ="SUCCESS"
    step = 1
    print(f"\nTEST STEP {step}: Get the TR069 Managment Server URL")
    print(f"EXPECTED RESULT {step}: Should get the TR069 Managment Server URL")
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    actualresult,serverURL = getTR181Value(tdkTestObj,"Device.ManagementServer.URL")
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Got serverURL as {serverURL} successfully")
        print("TEST EXECUTION RESULT : %s" %actualresult)

        step+=1
        print(f"\nTEST STEP {step}: Check if the Server URL is present in partners_defaults.json file")
        print(f"EXPECTED RESULT {step}: partners_defaults.json file should have Managment Server URL entry")
        tdkTestObj = sysobj.createTestStep("ExecuteCmd")
        cmd = "cat /nvram/partners_defaults.json |  grep -i \"%s\"" %serverURL
        tdkTestObj.addParameter("command", cmd)
        tdkTestObj.executeTestCase(expectedresult)
        actualresult=tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails().replace("\\n", "")
        if expectedresult in actualresult and details!= "" and serverURL in details:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: Server URL is present in partners_defaults.json file")
            print("TEST EXECUTION RESULT : SUCCESS")
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Server URL is not present in partners_defaults.json file")
            print("TEST EXECUTION RESULT : FAILURE")
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to fetch serverURL")
        print("TEST EXECUTION RESULT : %s" %actualresult)
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
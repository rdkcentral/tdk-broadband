##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
import tdklib;
from tdkbVariables import *;
import os.path;
from os import path;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");


#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ETHAGENT_CheckProcessAndLogFile');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")

    #check whether the process is running or not
    query="sh %s/tdk_platform_utility.sh checkProcess CcspEthAgent" %TDK_PATH
    print("query:%s" %query)
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", query)
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase("SUCCESS");
    actualresult = tdkTestObj.getResult();
    pid = tdkTestObj.getResultDetails().strip().replace("\\n","");
    if expectedresult in actualresult and pid:
        tdkTestObj.setResultStatus("SUCCESS");
        print("TEST STEP 1:Check CcspEthAgent process");
        print("EXPECTED RESULT 1: CcspEthAgent process should be running");
        print("ACTUAL RESULT 1: PID of CcspEthAgent %s" %pid);
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : SUCCESS");
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        cmd = "[ -f /rdklogs/logs/ETHAGENTLog.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        if details == "File exist":
            tdkTestObj.setResultStatus("SUCCESS");
            print("TEST STEP 2:Check ETHAGENTLog.txt.0 log file is created");
            print("EXPECTED RESULT 2: ETHAGENTLog.txt.0 log file should be created");
            print("ACTUAL RESULT 2: ETHAGENTLog.txt.0 log file is created");
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : SUCCESS");
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print("TEST STEP 2:Check ETHAGENTLog.txt.0 log file is created");
            print("EXPECTED RESULT 2: ETHAGENTLog.txt.0 log file should be created");
            print("ACTUAL RESULT 2: ETHAGENTLog.txt.0 log file is not created");
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : FAILURE");
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print("TEST STEP 1:Check CcspEthAgent process");
        print("EXPECTED RESULT 1: CcspEthAgent process should be running");
        print("ACTUAL RESULT 1: CcspEthAgent process is not running");
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : FAILURE");
    obj.unloadModule("sysutil");
else:
    print("Failed to load module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");

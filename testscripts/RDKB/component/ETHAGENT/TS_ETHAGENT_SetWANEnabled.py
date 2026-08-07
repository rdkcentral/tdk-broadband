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

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");


#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ETHAGENT_SetWANEnabled.py');
obj1.configureTestCase(ip,port,'TS_ETHAGENT_SetWANEnabled.py');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    command= "sh %s/tdk_utility.sh parseConfigFile DEVICETYPE" %TDK_PATH;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    devicetype = tdkTestObj.getResultDetails().strip().replace("\\n","");
    if expectedresult in actualresult and devicetype != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print("TEST STEP 1: Get the DEVICE TYPE")
        print("EXPECTED RESULT 1: Should get the device type");
        print("ACTUAL RESULT 1:Device type  %s" %devicetype);
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : SUCCESS");
        if devicetype == "RPI":
            tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled");
            tdkTestObj.addParameter("ParamValue","false");
            tdkTestObj.addParameter("Type","string");

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult not in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print("TEST STEP 2: Set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to false");
                print("EXPECTED RESULT 2 : Should not set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to false")
                print("ACTUAL RESULT 2 :%s" %details);
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS");
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print("TEST STEP 2:Set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to false");
                print("EXPECTED RESULT 2: Should not set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to false");
                print("ACTUAL RESULT 2: Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled is set to false");
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE");
        else:
            tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled");
            tdkTestObj.addParameter("ParamValue","true");
            tdkTestObj.addParameter("Type","string");

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult not in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print("TEST STEP 2: Set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to true");
                print("EXPECTED RESULT 2: Should not set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to true")
                print("ACTUAL RESULT 2 :%s" %details);
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS");
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print("TEST STEP 2:Set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to true");
                print("EXPECTED RESULT 2: Should not set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to true");
                print("ACTUAL RESULT 2: Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to true");
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE");
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print("TEST STEP 1: Get the DEVICE TYPE");
        print("EXPECTED RESULT 1: Should get the DEVICE TYPE");
        print("ACTUAL RESULT 1:Failed to get DEVICE TYPE");
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : FAILURE");
    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
else:
    print("Failed to load module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");

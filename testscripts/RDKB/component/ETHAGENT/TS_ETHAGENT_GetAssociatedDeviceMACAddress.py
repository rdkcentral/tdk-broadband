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
retryCount =0;
MAX_RETRY=4;
#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ETHAGENT_GetAssociatedDeviceMACAddress');
obj1.configureTestCase(ip,port,'TS_ETHAGENT_GetAssociatedDeviceMACAddress');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")

    expectedresult="SUCCESS";
    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.Hosts.HostNumberOfEntries");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    NoofHost=tdkTestObj.getResultDetails().strip().replace("\\n", "");

    if expectedresult in actualresult and int(NoofHost) >0:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print("TEST STEP 1: Get the no of LAN clients connected");
        print("EXPECTED RESULT 1: Should get the no of LAN clients connected")
        print("ACTUAL RESULT 1:%s" %NoofHost)
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : SUCCESS");

        Ethclientfound = 0;

        for i in range (1,int(NoofHost)+1):
            expectedresult="SUCCESS";
            tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%s.Layer1Interface"%(i));
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details=tdkTestObj.getResultDetails().strip().replace("\\n", "");
            print("Device.Hosts.Host.%s.Layer1Interface value is %s" %(i,details));
            if expectedresult in actualresult and details == "Ethernet":
                tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
                tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%s.Active"%(i));
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details=tdkTestObj.getResultDetails().strip().replace("\\n", "");
                print("Device.Hosts.Host.%s.Active value is %s" %(i,details));
                if  expectedresult in actualresult and details == "true":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("TEST STEP 2: Check if the connected LAN client is active");
                    print("EXPECTED RESULT 2: Should get the connected LAN client as active");
                    print("ACTUAL RESULT 2:%s" %details);
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : SUCCESS");

                    Ethclientfound = 1;
                    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
                    tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%s.PhysAddress"%(i));

                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    macAddress = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                    if expectedresult in actualresult :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print("TEST STEP 3: Get the lan client mac");
                        print("EXPECTED RESULT 3: Should get the lan client mac")
                        print("ACTUAL RESULT 3:LAN client connected mac is:%s" %macAddress)
                        #Get the result of execution
                        print("[TEST EXECUTION RESULT] : SUCCESS");
                        mac = macAddress.upper();
                        break;

        if  Ethclientfound == 1:
            for i in range (1,5):
                tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
                tdkTestObj.addParameter("ParamName","Device.Ethernet.Interface.%s.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress"%i);
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                associatedMACAddress = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if expectedresult in actualresult and associatedMACAddress == mac:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("TEST STEP 3: Get the MAC address of the Ethernet interface");
                    print("EXPECTED RESULT 3: Should get the MAC address of the Ethernet interface")
                    print("ACTUAL RESULT 3:Device.Ethernet.Interface.%s.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress is %s" %(i,associatedMACAddress));
                    print("LAN client interafce connected at :%s" %i)
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : SUCCESS");
                    interface = i;
                    print("AssociatedDeviceMACAddress is %s" %associatedMACAddress)
                    break;
                else:
                    retryCount = retryCount + 1;
        if retryCount == MAX_RETRY:
            tdkTestObj.setResultStatus("FAILURE");
            print("TEST STEP 2: Get the active LAN client MAC")
            print("EXPECTED RESULT 2: Should get the active LAN client MAC")
            print("ACTUAL RESULT 2:Failed to get active LAN client MAC");
            print("[TEST EXECUTION RESULT] : FAILURE");

        if Ethclientfound == 0:
            tdkTestObj.setResultStatus("FAILURE");
            print("TEST STEP 2: Get the active lan client connected interface")
            print("EXPECTED RESULT 2: Should get the active lan client connected interface")
            print("ACTUAL RESULT 2:No Ethernet client connected to DUT");
            print("[TEST EXECUTION RESULT] : FAILURE");
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print("TEST STEP 1: Get the no of LAN clients connected");
        print("EXPECTED RESULT 1: Should get the no of LAN clients connected")
        print("ACTUAL RESULT 1:No clients associated with DUT %s" %NoofHost)
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : FAILURE");

    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
else:
    print("Failed to load module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");

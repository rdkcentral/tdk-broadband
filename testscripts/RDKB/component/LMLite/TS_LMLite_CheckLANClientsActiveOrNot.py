##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("lmlite","1")

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_LMLite_CheckLANClientsActiveOrNot')

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS"

    step = 1
    print(f"\nTEST STEP {step}: Get the number of active clients connected")
    print(f"EXPECTED RESULT {step}: Should get the number of active clients connected as greater than zero")
    #Get the number of clients connected. Should be greater than zero
    tdkTestObj = obj.createTestStep('LMLiteStub_Get')
    tdkTestObj.addParameter("paramName","Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber")
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    NoOfClients = tdkTestObj.getResultDetails()
    if expectedresult in actualresult and int(NoOfClients)>0:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Number of active clients connected :{NoOfClients}")
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        print(f"\nTEST STEP {step}: Get the number of hosts")
        print(f"EXPECTED RESULT {step}: Should get the number of hosts")
        tdkTestObj = obj.createTestStep('LMLiteStub_Get')
        tdkTestObj.addParameter("paramName","Device.Hosts.HostNumberOfEntries")
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        NoOfHosts = tdkTestObj.getResultDetails()
        if expectedresult in actualresult and int(NoOfHosts)>0:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: Number of hosts: {NoOfHosts}")
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : SUCCESS")
            #Find the active hosts among the listed Hosts. List will contains the ids of active hosts
            List=[]
            for i in range(1,int(NoOfHosts)+1):
                tdkTestObj.addParameter("paramName","Device.Hosts.Host.%d.Active" %i)
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                Status = tdkTestObj.getResultDetails()
                if expectedresult in actualresult and "true" in Status.lower():
                    List.append(str(i))
            step += 1
            print(f"\nTEST STEP {step}: Check if the number of active client list is same as ConnectedDeviceNumber")
            print(f"EXPECTED RESULT {step}: The number of active client list should be same as ConnectedDeviceNumber")
            if len(List)== int(NoOfClients):
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Number of active client list is same as ConnectedDeviceNumber and Active clients are :{List}")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: The number of items in the active client list is not same as ConnectedDeviceNumber : {List}" )
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Number of hosts: {NoOfHosts}")
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Number of active clients: {NoOfClients}")
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : FAILURE")
    obj.unloadModule("lmlite")
else:
    print("Failed to load lmlite module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
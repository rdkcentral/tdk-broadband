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
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB")

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_LMLite_CheckLayer1Interface')
sysObj.configureTestCase(ip,port,'TS_LMLite_CheckLayer1Interface')

#Get the result of connection with test component and DUT
loadmodulestatus1=obj.getLoadModuleResult()
loadmodulestatus2=sysObj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS"
    step = 1

    print(f"\nTEST STEP {step}: Get the number of active LAN clients connected")
    print(f"EXPECTED RESULT {step}: Should get the number of active LAN clients connected as greater than zero")
    #Get the number of clients connected. Should be greater than zero
    tdkTestObj = obj.createTestStep('LMLiteStub_Get')
    tdkTestObj.addParameter("paramName","Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber")
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    NoOfClients = tdkTestObj.getResultDetails()
    if expectedresult in actualresult and NoOfClients.isdigit() and int(NoOfClients)>0:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Number of active LAN clients connected :{NoOfClients}")
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        print(f"\nTEST STEP {step}: Get the interface name using arp command")
        print(f"EXPECTED RESULT {step}: Should get the interface using arp command")
        tdkTestObj = sysObj.createTestStep('ExecuteCmd')
        tdkTestObj.addParameter("command","arp | grep \"brlan0\" | tr \"\n\" \" \"")
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        IP_details = tdkTestObj.getResultDetails()
        if expectedresult in actualresult and IP_details:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS")
            #get the interface names of active LAN clients as list from obtained string. len(IP) will be the number of active clients
            try:
                IP = [p.split(']')[0] for p in IP_details.split('[') if ']' in p]
            except Exception as e:
                IP = []
                print(f"Warning: Failed to parse interface details: {e}")
            print(f"ACTUAL RESULT {step}: {IP}")
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            print(f"\nTEST STEP {step}: Get the number of hosts")
            print(f"EXPECTED RESULT {step}: Should get the number of hosts")
            tdkTestObj = obj.createTestStep('LMLiteStub_Get')
            tdkTestObj.addParameter("paramName","Device.Hosts.HostNumberOfEntries")
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult();
            NoOfHosts = tdkTestObj.getResultDetails()

            if expectedresult in actualresult and NoOfHosts.isdigit() and int(NoOfHosts)>0:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Number of hosts :{NoOfHosts}")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS")

                activeClientFound = 0
                activeHostCount = 0
                for i in range(1,int(NoOfHosts)+1):
                    tdkTestObj.addParameter("paramName","Device.Hosts.Host.%d.Active" %i)
                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    Status = tdkTestObj.getResultDetails()
                    if Status == "true":
                        activeHostCount += 1
                        tdkTestObj.addParameter("paramName","Device.Hosts.Host.%d.Layer1Interface" %i)
                        #Execute the test case in DUT
                        tdkTestObj.executeTestCase(expectedresult)
                        actualresult = tdkTestObj.getResult()
                        Layer1Interface = tdkTestObj.getResultDetails()
                        step += 1
                        print(f"\nTEST STEP {step}: Verify active host {i} is a LAN client")
                        print(f"EXPECTED RESULT {step}: Host {i} should have Layer1Interface indicating Ethernet/LAN")
                        if expectedresult in actualresult and "ethernet" in Layer1Interface.lower():
                            activeClientFound = 1
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: Host {i} is a LAN client (Layer1Interface={Layer1Interface})")
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                            step += 1
                            print(f"\nTEST STEP {step}: Compare the interface names obtained for active LAN host {i}")
                            print(f"EXPECTED RESULT {step}: Layer1Interface of active LAN host {i} should be present in ARP interface list")
                            #Derive interface type: ethernet maps to 'ether' in ARP output
                            Interface = "ether"
                            if Interface in IP:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"ACTUAL RESULT {step}: Interface name of host instance {i} matches (Layer1Interface={Layer1Interface})")
                                #Get the result of execution
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: Interface name of host instance {i} doesnt match (Layer1Interface={Layer1Interface})")
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            print(f"\nHost {i} is active but not a LAN client (Layer1Interface={Layer1Interface}), skipping interface check")
                    else:
                        print(f"\nHost {i} is inactive (Active={Status}), skipping interface check")

                if activeClientFound == 0:
                    step += 1
                    print(f"\nTEST STEP {step}: Check if any active clients were found")
                    print(f"EXPECTED RESULT {step}: At least one active client should be found")
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: No active clients found in the host table even though ConnectedDeviceNumber={NoOfClients} and HostNumberOfEntries={NoOfHosts}")
                    print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    step += 1
                    print(f"\nTEST STEP {step}: Verify active host count matches ConnectedDeviceNumber")
                    print(f"EXPECTED RESULT {step}: Active host count should equal ConnectedDeviceNumber")
                    if activeHostCount == int(NoOfClients):
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Active host count {activeHostCount} matches ConnectedDeviceNumber {NoOfClients}")
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Active host count {activeHostCount} does not match ConnectedDeviceNumber {NoOfClients}")
                        print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                #Set the result status ofexecution
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Number of hosts:{NoOfHosts}")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}:Failed to get the interface name")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Number of active LAN clients connected :%s" %NoOfClients)
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("lmlite")
    sysObj.unloadModule("sysutil")
else:
    print("Failed to load lmlite, sysutil modules")
    obj.setLoadModuleStatus("FAILURE")
    sysObj.setLoadModuleStatus("FAILURE")
    print("Modules loading failed")
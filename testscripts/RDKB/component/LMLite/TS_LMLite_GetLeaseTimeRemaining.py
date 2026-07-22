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
obj.configureTestCase(ip,port,'TS_LMLite_GetLeaseTimeRemaining')

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS"

    #Get the number of hosts
    tdkTestObj = obj.createTestStep('LMLiteStub_Get')
    tdkTestObj.addParameter("paramName","Device.Hosts.HostNumberOfEntries")
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    NoOfHosts = tdkTestObj.getResultDetails()
    step = 1
    print(f"\nTEST STEP {step}: Get the number of hosts")
    print(f"EXPECTED RESULT {step}: Should get the number of hosts")
    if expectedresult in actualresult and int(NoOfHosts)>0:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Number of hosts:{NoOfHosts}")
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : SUCCESS")
        ethernetHostFound = 0
        for i in range(1,int(NoOfHosts)+1):
            tdkTestObj.addParameter("paramName","Device.Hosts.Host.%d.Layer1Interface" %i)
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            Layer1Interface = tdkTestObj.getResultDetails()

            if expectedresult in actualresult and "ethernet" in Layer1Interface.lower():
                tdkTestObj.addParameter("paramName","Device.Hosts.Host.%d.Active" %i)
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                Status = tdkTestObj.getResultDetails()

                step += 1
                print(f"\nTEST STEP {step}: Check Active status for Ethernet host {i}")
                print(f"EXPECTED RESULT {step}: Ethernet host should be active")
                if expectedresult in actualresult and "true" in Status.lower():
                    ethernetHostFound = 1
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Host {i} has Layer1Interface={Layer1Interface} and Active={Status}")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step += 1
                    print(f"\nTEST STEP {step}: Get the Address source for Ethernet host {i}")
                    print(f"EXPECTED RESULT {step}: Should get the Address source for Ethernet host {i}")
                    tdkTestObj.addParameter("paramName","Device.Hosts.Host.%d.AddressSource" %i)
                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    Addr_src = tdkTestObj.getResultDetails()
                    if expectedresult in actualresult and Addr_src !="":
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Address source of host number {i} is {Addr_src}")
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        step += 1
                        print(f"\nTEST STEP {step}: Get the Lease time remaining for Ethernet host {i}")
                        print(f"EXPECTED RESULT {step}: Should get the Lease time remaining for Ethernet host {i}")
                        tdkTestObj.addParameter("paramName","Device.Hosts.Host.%d.LeaseTimeRemaining" %i)
                        #Execute the test case in DUT
                        tdkTestObj.executeTestCase(expectedresult)
                        actualresult = tdkTestObj.getResult()
                        LeaseTime = tdkTestObj.getResultDetails()
                        if expectedresult in actualresult and LeaseTime.isdigit():
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: Lease time remaining of host number {i} is {LeaseTime}")
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                            step += 1
                            print(f"\nTEST STEP {step}: Check AddressSource and LeaseTimeRemaining for Ethernet host {i}")
                            print(f"EXPECTED RESULT {step}: If AddressSource is DHCP, LeaseTimeRemaining should be greater than zero; otherwise it should be zero")
                            if "DHCP" in Addr_src and int(LeaseTime) > 0:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"ACTUAL RESULT {step}: DHCP host {i} has valid lease time remaining {LeaseTime}")
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            elif "DHCP" in Addr_src and int(LeaseTime) <= 0:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: DHCP host {i} has invalid lease time remaining {LeaseTime}")
                                print("[TEST EXECUTION RESULT] : FAILURE")
                            elif int(LeaseTime) == 0:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"ACTUAL RESULT {step}: Non-DHCP host {i} has valid lease time remaining {LeaseTime}")
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: Non-DHCP host {i} has invalid lease time remaining {LeaseTime}")
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: Failure in getting Lease time for Ethernet host {i}")
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Failure in getting address source for Ethernet host {i}")
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Host {i} has Layer1Interface={Layer1Interface} and Active={Status}")
                    print("[TEST EXECUTION RESULT] : FAILURE")

        if ethernetHostFound == 0:
            tdkTestObj.setResultStatus("FAILURE")
            print(" No active Ethernet host found in the host table")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        #Set the result status ofexecution
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Number of hosts:{NoOfHosts}")
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("lmlite")
else:
    print("Failed to load lmlite module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

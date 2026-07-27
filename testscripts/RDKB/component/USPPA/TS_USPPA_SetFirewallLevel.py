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
import tdklib;
from usppaUtility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1")

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_USPPA_SetFirewallLevel')

#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult()

print("[LIB LOAD STATUS]  :  %s" %result)

if "SUCCESS" in result.upper():
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS")

    #Check for prerequisites
    tdkTestObj,agentID,preRequisiteStatus = usppaPreRequisite(obj)
    if "SUCCESS" in preRequisiteStatus:
        firewallLevelList =  {"High", "Low", "Medium"}
        #get the current firewall level
        print("\nTEST STEP 1: Send GET request to get the current firewall level and receive a valid response via USP protocol")
        print("EXPECTED RESULT 1: Send GET request to get current firewall level and receive a valid response successfully via USP protocol")
        queryParam = {"name":"Device.X_CISCO_COM_Security.Firewall.FirewallLevel"}
        status,queryResponse = usppaQuery(agentID,queryParam)
        if status == 200:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT 1: Sent GET request to get the Firewall level successfully via USP protocol")
            #Parse the response from get operation
            parsedResponse = parseUsppaResponse(queryResponse)
            if "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                tdkTestObj.setResultStatus("SUCCESS")
                orgLevel = parsedResponse[1]
                print(" Got the Firewall level as %s successfully via USP protocol" %orgLevel)
                print("[TEST EXECUTION RESULT] : SUCCESS")

                for newLevel in firewallLevelList:
                    if newLevel == orgLevel :
                        continue
                    else:
                        #set the firewall level
                        print("\n TEST STEP 2:  Send SET request to set %s as new firewall level via USP protocol " %newLevel)
                        print("EXPECTED RESULT 2: Send SET request to set %s as new firewall level successfully via USP protocol" %newLevel)
                        queryParam = {"name":"Device.X_CISCO_COM_Security.Firewall.FirewallLevel","value":newLevel}
                        status,queryResponse = usppaQuery(agentID,queryParam,"set")
                        if status == 200 :
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT 2: Send SET request to set firewall level successfully via USP protocol")
                            #Parse the response from set operation
                            parsedResponse = parseUsppaResponse(queryResponse,"set")
                            if "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                                tdkTestObj.setResultStatus("SUCCESS")
                                setLevel = parsedResponse[1]
                                print(" Agent processed correctly the SET request to set the Firewall level as %s successfully via USP protocol" %setLevel)
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                #Check if set and get value of firewall level matches
                                print("\nTEST STEP 3: Check if set and get value of firewall level matches")
                                print("EXPECTED RESULT 3: Set and get value of firewall level should match")
                                print("Send GET request to get the current firewall level via USP protocol")
                                queryParam = {"name":"Device.X_CISCO_COM_Security.Firewall.FirewallLevel"}
                                status,queryResponse = usppaQuery(agentID,queryParam)
                                if status == 200:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print("Sent GET request to get Firewall level  successfully via USP protocol")
                                    #Parse the response from get operation
                                    parsedResponse = parseUsppaResponse(queryResponse)
                                    if "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                                        tdkTestObj.setResultStatus("SUCCESS")
                                        getLevel = parsedResponse[1]
                                        print("Got Firewall level as %s successfully via USP protocol" %getLevel)
                                        if setLevel == getLevel:
                                            tdkTestObj.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT 3 : Set and get value of firewall level matches")
                                            print("[TEST EXECUTION RESULT] : SUCCESS")
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT 3 : Set and get value of firewall level mismatch")
                                            print("[TEST EXECUTION RESULT] : FAILURE")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("Failed to get Firewall level via USP protocol")
                                        print("[TEST EXECUTION RESULT] : FAILURE")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    if status == "FAILURE":
                                        print(" Token Generation failed during get operation of get and set value check")
                                    print(f"Failed to send GET request to get value of firewall level via USP protocol with status: {status} ")
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(" Agent failed to process the SET request to set the Firewall level  via USP protocol")
                                print("[TEST EXECUTION RESULT] : FAILURE")

                            #Revert to original value
                            print("\nTEST STEP 4: Revert to the original value of firewall level as %s via USP protocol" %orgLevel)
                            print("EXPECTED RESULT 4: The value of firewall level should be reverted successfully via USP protocol")
                            queryParam = {"name":"Device.X_CISCO_COM_Security.Firewall.FirewallLevel","value":orgLevel}
                            status,queryResponse = usppaQuery(agentID,queryParam,"set")
                            if status == 200 :
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT 4: Sent SET request to revert the firewall level successfully via USP protocol")
                                #Parse the response from get operation
                                parsedResponse = parseUsppaResponse(queryResponse,"set")
                                if "SUCCESS" in parsedResponse[0] and parsedResponse[1]:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    getLevel = parsedResponse[1]
                                    print("Reverted Firewall level as %s successfully via USP protocol" %getLevel)
                                    print("[TEST EXECUTION RESULT] : SUCCESS")
                                    break
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("Failed to get Firewall level via USP protocol")
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                if status == "FAILURE":
                                    print(" Token Generation failed during revert operation")
                                print(f" ACTUAL RESULT 4: The revert operation returned failure via USP protocol with status: {status}")
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT 2: Failed to send SET request to set Firewall level via USP protocol with status: {status}")
                            print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("Failed to get Firewall level via USP protocol")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            if status == "FAILURE":
                print(" Token Generation failed during get operation")
            print(f"ACTUAL RESULT 1: Failed to send GET request to get the value of firewall level via USP protocol with status: {status}")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("Usppa Pre-requisite failed. Please check if usppa processes are running in device or controller setup is ready or agent ID failed to fetch \n")
        print("[TEST EXECUTION RESULT] : FAILURE")
    obj.unloadModule("sysutil")
else:
    print("FAILURE to load module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading FAILURE")

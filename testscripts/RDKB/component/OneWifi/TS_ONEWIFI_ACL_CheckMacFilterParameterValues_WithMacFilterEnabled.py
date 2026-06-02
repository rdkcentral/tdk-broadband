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

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent",1)

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_ACL_CheckMacFilterParameterValues_WithMacFilterEnabled')

#Get Module loading status
loadmodulestatus = obj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")

    step = 1
    expectedresult="SUCCESS"
    for index in range(1,4):
        print(f"\n***************For radio index : {index}*********************")
        param1 = "Device.WiFi.AccessPoint." + str(index) + ".X_CISCO_COM_MACFilter.Enable"
        print(f"\nTEST STEP {step}: Set Mac Filter Enable {param1} to true." )
        print(f"EXPECTED RESULT {step}: Should set Mac Filter Enable {param1} to true successfully.")
        tdkTestObj = obj.createTestStep("WIFIAgent_Set_Get")
        tdkTestObj.addParameter("paramName",param1)
        tdkTestObj.addParameter("paramValue","true")
        tdkTestObj.addParameter("paramType","bool")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: Set Mac Filter Enable {param1} to true successfully.")
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step+=1
            param2 = "Device.WiFi.AccessPoint." + str(index) + ".X_CISCO_COM_MACFilter.FilterAsBlackList"
            print(f"\nTEST STEP {step}: Verify that Mac FilterAsBlacklist {param2} is 'true' when Mac filter is enabled.")
            print(f"EXPECTED RESULT {step}: Mac FilterAsBlacklist {param2} should be 'true' when Mac filter is enabled.")
            tdkTestObj = obj.createTestStep("WIFIAgent_Get")
            tdkTestObj.addParameter("paramName",param2)
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()
            status=details.split("VALUE:")[1].split(' ')[0]
            if expectedresult in actualresult  and status == "true" :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Mac FilterAsBlacklist {param2} is '{status}' when Mac filter is enabled successfully.")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Mac FilterAsBlacklist {param2} is '{status}' which is not expected when Mac filter is enabled.")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE")

            step+=1
            param3 = "Device.WiFi.AccessPoint." + str(index) + ".X_COMCAST-COM_MAC_FilteringMode"
            print(f"\nTEST STEP {step}: Verify that Mac Filtering mode {param3} is 'Deny' when Mac filter is enabled.")
            print(f"EXPECTED RESULT {step}: Mac Filtering mode {param3} should be 'Deny' when Mac filter is enabled successfully.")
            tdkTestObj = obj.createTestStep("WIFIAgent_Get")
            tdkTestObj.addParameter("paramName",param3)
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()
            mode=details.split("VALUE:")[1].split(' ')[0]
            if expectedresult in actualresult  and mode == "Deny" :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Mac Filtering mode {param3} is '{mode}' when Mac filter is enabled successfully.")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Mac Filtering mode {param3} is '{mode}' which is not expected when Mac filter is enabled.")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE")

            #Revert the Mac Filter Enable to original value
            step += 1
            print(f"\nTEST STEP {step}: Revert the Mac Filter Enable {param1} to false.")
            print(f"EXPECTED RESULT {step}: Should revert the Mac Filter Enable {param1} to false successfully")
            tdkTestObj = obj.createTestStep("WIFIAgent_Set_Get")
            tdkTestObj.addParameter("paramName",param1)
            tdkTestObj.addParameter("paramValue","false")
            tdkTestObj.addParameter("paramType","bool")
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()
            if expectedresult in actualresult and details != "":
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Successfully reverted the Mac Filter Enable {param1} to false.")
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Failed to set the Mac Filter Enable {param1} to false.")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Failed to set Mac Filter Enable {param1} to true.")
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : FAILURE")
        step+=1
    obj.unloadModule("wifiagent")
else:
    print("Failed to load wifiagent module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
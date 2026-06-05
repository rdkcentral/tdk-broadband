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
from  tdkutility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1")

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_ACL_CheckMacFilteringMode_DisabledFilterAsBlackList')

#Get Module loading status
loadmodulestatus = obj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")

    step = 1
    expectedresult="SUCCESS"
    #Get the number of radios
    print(f"\nTEST STEP {step} : Get the number of radio entries.")
    print(f"EXPECTED RESULT {step} : Should get the number of radio entries.")
    tdkTestObj,actualresult,radioCount = wifi_GetParam(obj,"Device.WiFi.RadioNumberOfEntries")
    if expectedresult in actualresult and radioCount != "" :
        #Set the result of execution
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Got the number of radio entries as {radioCount} successfully.")
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : SUCCESS")

        radioCount = int(radioCount)
        #Get the accesspoint indexes of Radios supported
        if radioCount == 3:
            ap_indices = [1,2,17]
        elif radioCount == 2:
            ap_indices = [1,2]
        elif radioCount == 1:
            ap_indices = [1]
        else:
            raise ValueError(f"Unknown radio count: {radioCount}")

        for index in ap_indices:
            setflag1 = 0
            setflag2 = 0
            step+=1
            print(f"\n***************For radio index : {index}*********************")
            param1 = "Device.WiFi.AccessPoint." + str(index) + ".X_CISCO_COM_MACFilter.Enable"
            print(f"\nTEST STEP {step} : Get the Mac Filter Enable {param1} value.")
            print(f"EXPECTED RESULT {step} :Should get the Mac Filter Enable {param1} value.")
            tdkTestObj,actualresult,orgMacFilterEnable = wifi_GetParam(obj,param1)
            if expectedresult in actualresult and orgMacFilterEnable!="" :
                #Set the result of execution
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Got the Mac Filter Enable {param1}value as  {orgMacFilterEnable} successfully.")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS")
                if orgMacFilterEnable == "true":
                    print("\n Mac Filter Enable is already 'true', so skipping the set operation of Mac Filter Enable to 'true'.")
                    setflag1 = 1
                else:
                    step+=1
                    print(f"\nTEST STEP {step}: Set Mac Filter Enable {param1} to true" )
                    print(f"EXPECTED RESULT {step}: Should set Mac Filter Enable {param1} to true successfully")
                    tdkTestObj = obj.createTestStep("WIFIAgent_Set_Get")
                    tdkTestObj.addParameter("paramName",param1)
                    tdkTestObj.addParameter("paramValue","true")
                    tdkTestObj.addParameter("paramType","bool")
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    details = tdkTestObj.getResultDetails()
                    if expectedresult in actualresult :
                        setflag1=1
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Set Mac Filter Enable {param1} to true successfully")
                        #Get the result of execution
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Failed to set Mac Filter Enable {param1} to true.")
                        #Get the result of execution
                        print("[TEST EXECUTION RESULT] : FAILURE")
                if setflag1:
                    step+=1
                    param2 = "Device.WiFi.AccessPoint." + str(index) + ".X_CISCO_COM_MACFilter.FilterAsBlackList"
                    print(f"\nTEST STEP {step}: Get the Mac FilterAsBlacklist {param2} value")
                    print(f"EXPECTED RESULT {step} : Should get the Mac FilterAsBlacklist {param2} value")
                    tdkTestObj,actualresult,orgFilterAsBlacklist = wifi_GetParam(obj,param2)
                    if expectedresult in actualresult and orgFilterAsBlacklist !="" :
                        #Set the result of execution
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Got the Mac FilterAsBlacklist {param2} value as {orgFilterAsBlacklist} successfully.")
                        #Get the result of execution
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                        if orgFilterAsBlacklist == "false":
                            print("\n Mac Filter Enable is already 'false', so skipping the set operation of Mac FilterAsBlacklist to 'false'.")
                            setflag2 = 1
                        else:
                            step+=1
                            print(f"\nTEST STEP {step}: Set Mac FilterAsBlacklist {param2} to false ")
                            print(f" EXPECTED RESULT {step}: Should set Mac FilterAsBlacklist {param2} to false successfully")
                            tdkTestObj = obj.createTestStep("WIFIAgent_Set_Get")
                            tdkTestObj.addParameter("paramName",param2)
                            tdkTestObj.addParameter("paramValue","false")
                            tdkTestObj.addParameter("paramType","bool")
                            tdkTestObj.executeTestCase(expectedresult)
                            actualresult = tdkTestObj.getResult()
                            details = tdkTestObj.getResultDetails()
                            if expectedresult in actualresult:
                                setflag2 = 1
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"ACTUAL RESULT {step}: Set Mac FilterAsBlacklist {param2} to false successfully")
                                #Get the result of execution
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: Failed to set Mac FilterAsBlacklist {param2} to false.")
                                #Get the result of execution
                                print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"\nFailed to set Mac Filter Enable to true even after set operation.")

                if setflag2:
                    step+=1
                    param3 = "Device.WiFi.AccessPoint." + str(index) + ".X_COMCAST-COM_MAC_FilteringMode"
                    print(f"\nTEST STEP {step}: Verify that Mac Filtering mode {param3} is 'Allow' when Mac filter is enabled and FilterAsBlacklist set to false")
                    print(f"EXPECTED RESULT {step}: Mac Filtering mode {param3} should be 'Allow' when Mac filter is enabled and FilterAsBlacklist set to false successfully")
                    tdkTestObj,actualresult,mode = wifi_GetParam(obj,param3)
                    if expectedresult in actualresult  and mode == "Allow" :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Mac Filtering mode {param3} is '{mode}' when Mac filter is enabled and FilterAsBlacklist set to false successfully")
                        #Get the result of execution
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Mac Filtering mode {param3} is '{mode}' which is not expected when Mac filter is enabled and FilterAsBlacklist set to false.")
                        #Get the result of execution
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else :
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"\nFailed to set FilterAsBlacklist to false even after set operation ")

                if setflag2 and orgFilterAsBlacklist == "true":
                    #Revert the FilterAsBlackList to original value
                    step += 1
                    print(f"\nTEST STEP {step}: Revert the Mac FilterAsBlackList {param2} to {orgFilterAsBlacklist}")
                    print(f"EXPECTED RESULT {step}: Should revert the Mac FilterAsBlackList {param2} to {orgFilterAsBlacklist} successfully")
                    tdkTestObj = obj.createTestStep("WIFIAgent_Set_Get")
                    tdkTestObj.addParameter("paramName",param2)
                    tdkTestObj.addParameter("paramValue",orgFilterAsBlacklist)
                    tdkTestObj.addParameter("paramType","bool")
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    details = tdkTestObj.getResultDetails()
                    if expectedresult in actualresult :
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Successfully reverted the Mac FilterAsBlackList {param2} to {orgFilterAsBlacklist}.")
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Failed to revert Mac FilterAsBlacklist {param2} to {orgFilterAsBlacklist}.")
                        print("[TEST EXECUTION RESULT] : FAILURE")
                if setflag1 and orgMacFilterEnable == "false":
                    #Revert the Mac Filter Enable to original value
                    step += 1
                    print(f"\nTEST STEP {step}: Revert the Mac Filter Enable {param1} to {orgMacFilterEnable}.")
                    print(f"EXPECTED RESULT {step}: Should revert the Mac Filter Enable {param1} to {orgMacFilterEnable} successfully")
                    tdkTestObj = obj.createTestStep("WIFIAgent_Set_Get")
                    tdkTestObj.addParameter("paramName",param1)
                    tdkTestObj.addParameter("paramValue",orgMacFilterEnable)
                    tdkTestObj.addParameter("paramType","bool")
                    tdkTestObj.executeTestCase(expectedresult)
                    actualresult = tdkTestObj.getResult()
                    details = tdkTestObj.getResultDetails()
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: Successfully reverted the Mac Filter Enable {param1} to {orgMacFilterEnable}.")
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Failed to revert the Mac Filter Enable {param1} to {orgMacFilterEnable}.")
                        print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Failed to get Mac Filter Enable ")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        #Set the result of execution
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to get the number of radio entries .")
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : FAILURE")
    obj.unloadModule("wifiagent")
else:
    print("Failed to load wifiagent module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
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
import time
import sys
from tdkutility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1")

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_ACL_CheckMacFilterParameterValues_WithMacFilterEnabled_AfterFactoryReset')

#Get Module loading status
loadmodulestatus = obj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")

    step = 1
    expectedresult="SUCCESS"
    #save device's current state before it goes for reboot
    obj.saveCurrentState()

    #Initiate Factory reset
    print(f"\nTEST STEP {step}: Initiate factory reset on DUT")
    print(f"EXPECTED RESULT {step}: Factory reset  should be initiated on DUT succesfully")
    tdkTestObj = obj.createTestStep('WIFIAgent_Set')
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.FactoryReset")
    tdkTestObj.addParameter("paramValue","Router,Wifi,VoIP,Dect,MoCA")
    tdkTestObj.addParameter("paramType","string")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()
    if expectedresult in actualresult:
        #Set the result of executionDetails
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Initiated factory reset on the DUT successfully")
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : SUCCESS")

        #Restore the device state saved before reboot
        obj.restorePreviousStateAfterReboot()
        #Wait upto 5 min for DUT to come up
        print("Sleeping 5 min for DUT to come up")
        time.sleep(300)

        #Get the last reboot reason
        step+=1
        print(f"\nTEST STEP {step}: Verify that the last reboot reason is 'factory-reset'")
        print(f"EXPECTED RESULT {step}: The last reboot reason should be 'factory-reset'" )
        tdkTestObj,actualresult,rebootReason = wifi_GetParam(obj,"Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason")
        if expectedresult in actualresult and rebootReason == "factory-reset":
            #Set the result of execution
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: Got the last reboot reason as '{rebootReason}' confirmed the DUT's factory reset." )
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : SUCCESS")

            #Get the number of radios
            step+=1
            print(f"\nTEST STEP {step} : Get the number of radio entries.")
            print(f"EXPECTED RESULT {step} : Should get the number of radio entries.")
            tdkTestObj,actualresult,radioCount = wifi_GetParam(obj,"Device.WiFi.RadioNumberOfEntries")
            if expectedresult in actualresult and radioCount!="":
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
                else:
                    print(f"Unknown radio count: {radioCount}")
                    obj.unloadModule("wifiagent")
                    sys.exit(0)
                for index in ap_indices:
                    setflag = 0
                    print(f"\n***************For radio index : {index}*********************")
                    step+=1
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
                            setflag =1
                        else:
                            step+=1
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
                                setflag = 1
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: Failed to set Mac Filter Enable {param1} to true.")
                                #Get the result of execution
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        if setflag:
                            step+=1
                            param2 = "Device.WiFi.AccessPoint." + str(index) + ".X_CISCO_COM_MACFilter.FilterAsBlackList"
                            print(f"\nTEST STEP {step}: Verify that Mac FilterAsBlacklist {param2} is 'true' when Mac filter is enabled.")
                            print(f"EXPECTED RESULT {step}: Mac FilterAsBlacklist {param2} should be 'true' when Mac filter is enabled.")
                            tdkTestObj,actualresult,orgFilterAsBlacklist = wifi_GetParam(obj,param2)
                            if expectedresult in actualresult  and orgFilterAsBlacklist == "true" :
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"ACTUAL RESULT {step}: Mac FilterAsBlacklist {param2} is '{orgFilterAsBlacklist}' when Mac filter is enabled successfully.")
                                #Get the result of execution
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                step+=1
                                param3 = "Device.WiFi.AccessPoint." + str(index) + ".X_COMCAST-COM_MAC_FilteringMode"
                                print(f"\nTEST STEP {step}: Verify that Mac Filtering mode {param3} is 'Deny' when Mac filter is enabled.")
                                print(f"EXPECTED RESULT {step}: Mac Filtering mode {param3} should be 'Deny' when Mac filter is enabled successfully.")
                                tdkTestObj,actualresult,mode =wifi_GetParam(obj,param3)
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
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: Mac FilterAsBlacklist {param2} is '{orgFilterAsBlacklist}' which is not expected when Mac filter is enabled.")
                                #Get the result of execution
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"\nFailed to get Mac filterABlacklist as true even after set operation")

                        #Revert the Mac Filter Enable to original value
                        if orgMacFilterEnable == "false"and setflag:
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
                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print(f"ACTUAL RESULT {step}: Successfully reverted the Mac Filter Enable {param1} to false.")
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print(f"ACTUAL RESULT {step}: Failed to revert the Mac Filter Enable {param1} to false.")
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            print(f"\n Revert operation is not required for Mac Filter Enable.")
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Failed to get Mac Filter Enable {param1}.")
                        #Get the result of execution
                        print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                #Set the result of execution
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Failed to get the number of radio entries.")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            #Set the result of execution
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}:Failed to get reboot reason as expected : {rebootReason}." )
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        #Set the result of execution
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}:Failed to initiate Factory reset." )
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : FAILURE")
    obj.unloadModule("wifiagent")
else:
    print("Failed to load wifiagent module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

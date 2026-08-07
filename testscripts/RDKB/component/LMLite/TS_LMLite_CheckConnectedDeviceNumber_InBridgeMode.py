##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2017 RDK Management
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
from time import sleep

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("lmlite","1")

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_LMLite_CheckConnectedDeviceNumber_InBridgeMode')

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS"
    exitFlag = 0
    revertFlag = 0

    #Check if device is in bridge mode or not
    step = 1
    print(f"\nTEST STEP {step}: Get the Lan Mode of the device")
    print(f"EXPECTED RESULT {step}: Should get the lan mode of device")
    tdkTestObj = obj.createTestStep('LMLiteStub_Get')
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    Initial_Mode = tdkTestObj.getResultDetails()
    if expectedresult in actualresult and Initial_Mode:
        if "router" not in Initial_Mode:
            Mode = "bridge mode"
        else:
            Mode = "Router mode"
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: LanMode is {Mode}")
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        print(f"\nTEST STEP {step}: Set the lan mode to 'bridge-static' if not already")
        print(f"EXPECTED RESULT {step}: Should set the lan mode to 'bridge-static' if not already")
        if "bridge mode" not in Mode:
            tdkTestObj = obj.createTestStep('LMLiteStub_Set')
            tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
            tdkTestObj.addParameter("ParamValue","bridge-static")
            tdkTestObj.addParameter("Type","string")
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: {details}")
                Mode = "bridge mode"
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS")
                revertFlag = 1
                #Wait for few seconds for the Lan mode to get reflected
                print("\nWait for some seconds for the Lan mode to get reflected")
                sleep(90)
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: {details}")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE")
                exitFlag = 1
        else:
            print(f"The device is already in bridge mode, no set operation required")
        # continue with next steps only if no failure occurs in setting the lan mode as bridge-static
        if exitFlag != 1:
            step += 1
            print(f"\nTEST STEP {step}: Get the number of active clients")
            print(f"EXPECTED RESULT {step}: Should get the number of active clients")
            tdkTestObj = obj.createTestStep('LMLiteStub_Get')
            tdkTestObj.addParameter("paramName","Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber")
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            NoOfClients = tdkTestObj.getResultDetails()
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Got the number of clients as {NoOfClients}")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                print(f"\nTEST STEP {step}:Check if the number of connected devices is zero in bridge mode")
                print(f"EXPECTED RESULT {step}: The number of connected devices should be zero if device is in bridge mode")
                if NoOfClients.isdigit() and int(NoOfClients) == 0:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Number of Clients is zero as expected")
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Failed to get number of Clients as zero and Number of Clients is {NoOfClients}")
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: No of Clients is {NoOfClients}")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE")
        if revertFlag == 1:
            step += 1
            print(f"\nTEST STEP {step}: Set the LanMode to original value")
            print(f"EXPECTED RESULT {step}: Should set the LanMode to original value")
            #set original LanMode
            tdkTestObj = obj.createTestStep('LMLiteStub_Set')
            tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
            tdkTestObj.addParameter("ParamValue",Initial_Mode)
            tdkTestObj.addParameter("Type","string")
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT : {details}")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS")
                #Wait for few seconds for the Lan mode to get reflected
                print("\nWait for some seconds for the Lan mode to get reflected\n")
                sleep(90)
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step} : {details}")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            print(f"\nRevert operation is not required\n")
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: LanMode is {Initial_Mode}")
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : FAILURE")
    obj.unloadModule("lmlite")
else:
    print("Failed to load module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")
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
import tdklib

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1")

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_6GHZ_RadioLastChange')

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus)

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS"
    step = 1

    #Get the Radio Enable state for 6ghz
    tdkTestObj = obj.createTestStep('WIFIAgent_Get')
    tdkTestObj.addParameter("paramName","Device.WiFi.Radio.3.Enable")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    print(f"TEST STEP {step}: Get the Radio Enable state for 6ghz")
    print(f"EXPECTED RESULT {step}: Should get the Radio Enable state for 6ghz")

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        orgState = details.split("VALUE:")[1].split(' ')[0]
        print(f"ACTUAL RESULT {step}: Radio Enable is {orgState}" )
        print("[TEST EXECUTION RESULT] : SUCCESS")

        #Get and save the LastChange value
        step = step + 1
        tdkTestObj = obj.createTestStep('WIFIAgent_Get')
        tdkTestObj.addParameter("paramName","Device.WiFi.Radio.3.LastChange")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print(f"TEST STEP {step}: Get LastChange value")
        print(f"EXPECTED RESULT {step}: Should get LastChange value")

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            lastChange = int(details.split("VALUE:")[1].split(' ')[0])
            print(f"ACTUAL RESULT {step}: lastchange value is {lastChange} " )
            print("[TEST EXECUTION RESULT] : SUCCESS")

            #toggle Device.WiFi.Radio.3.Enable value
            if orgState == "false":
                toggle = "true"
            else:
                toggle = "false"

            step = step + 1
            tdkTestObj = obj.createTestStep('WIFIAgent_Set')
            tdkTestObj.addParameter("paramName","Device.WiFi.Radio.3.Enable")
            tdkTestObj.addParameter("paramValue",toggle)
            tdkTestObj.addParameter("paramType","boolean")
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()
            details = tdkTestObj.getResultDetails()

            print(f"TEST STEP {step}: Toggle Radio Enable state for 6ghz")
            print(f"EXPECTED RESULT {step}: Should toggle Radio Enable state for 6ghz")

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}:Set operation is successfull. Details: {details}" )
                print("[TEST EXECUTION RESULT] : SUCCESS")

                #check lastchange value after toggling
                step = step + 1
                tdkTestObj = obj.createTestStep('WIFIAgent_Get')
                tdkTestObj.addParameter("paramName","Device.WiFi.Radio.3.LastChange")
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails()

                print(f"TEST STEP {step}: Get Current lastchange value")
                print(f"EXPECTED RESULT {step}: Should get current lastchange value")

                if expectedresult in actualresult and details != "":
                    tdkTestObj.setResultStatus("SUCCESS")
                    lastChange2 = int(details.split("VALUE:")[1].split(' ')[0])
                    print(f"ACTUAL RESULT {step}: Current lastchange value: {lastChange2}")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step += 1
                    print(f"TEST STEP {step}: Check current lastchange value is less than previous value")
                    print(f"EXPECTED RESULT {step}: Current lastchange should be less than its previous value")

                    if lastChange2 < lastChange:
                        tdkTestObj.setResultStatus("SUCCESS")
                        lastChange2 = int(details.split("VALUE:")[1].split(' ')[0])
                        print(f"ACTUAL RESULT {step}: Current lastchange value: {lastChange2}, Previous lastchange value {lastChange}")
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: Current last change value is not less than previous value. Details {details}")
                        print(f"ACTUAL RESULT {step}: Current lastchange value: {lastChange2}, Previous lastchange value {lastChange}")
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Get operation Failed. Details: {details}")
                    print("[TEST EXECUTION RESULT] : FAILURE")

                #Change the Radio.3 state to its previous value
                step = step + 1
                tdkTestObj = obj.createTestStep('WIFIAgent_Set')
                tdkTestObj.addParameter("paramName","Device.WiFi.Radio.3.Enable")
                tdkTestObj.addParameter("paramValue",orgState)
                tdkTestObj.addParameter("paramType","boolean")
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails()

                print(f"TEST STEP {step}: Restore Radio Enable to previous value")
                print(f"EXPECTED RESULT {step}: Should Restore Radio Enable to previous value")

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Revert operation success. Details: {details} ")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Revert operation Failed. Details: {details} ")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}:Set operation failed. Details: {details}" )
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            lastChange = int(details.split("VALUE:")[1].split(' ')[0])
            print(f"ACTUAL RESULT {step}: Failed to get lastchange value. Details {details} " )
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        orgState = details.split("VALUE:")[1].split(' ')[0]
        print(f"ACTUAL RESULT {step}: Get operation Failed. Details {details}" )
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("wifiagent")

else:
    print("Failed to load wifi module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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

# use tdklib library, which provides a wrapper for tdk testcase script
import tdklib
from time import sleep

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB")

# IP and Port of box, No need to change
# This will be replaced with corresponding DUT IP and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ONEWIFI_SetWiFiTelemetryTxRxRateList')

# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus)

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1
    proceed_flag = 1
    revert_flag = 0

    # Get the number of radio entries
    tdkTestObj = obj.createTestStep('WIFIAgent_Get')
    tdkTestObj.addParameter("paramName","Device.WiFi.RadioNumberOfEntries")
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    print("TEST STEP %d: Get the number of WiFi radio entries" %step)
    print("EXPECTED RESULT %d: Should get a valid number of WiFi radio entries" %step)

    if expectedresult in actualresult and "VALUE:" in details:
        radioCount = details.split("VALUE:")[1].split(" ")[0].strip()
        if radioCount.isdigit() and int(radioCount) in [2,3]:
            radioCount = int(radioCount)
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Number of WiFi radio entries is %d" %(step,radioCount))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            proceed_flag = 0
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Unsupported RadioNumberOfEntries value: %s" %(step,radioCount))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        proceed_flag = 0
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get RadioNumberOfEntries. Details: %s" %(step,details))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Create the private AP list based on the number of radios
    if proceed_flag == 1:
        if radioCount == 3:
            ap_indices = [1,2,17]
        else:
            ap_indices = [1,2]

        newTxRxRateListTobeset = ",".join(str(index) for index in ap_indices)
        step += 1
        print("TEST STEP %d: Generate the Private WiFi AP list based on the number of radios" %step)
        print("EXPECTED RESULT %d: Should generate the applicable Private WiFi AP list" %step)
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Private WiFi AP list is %s" %(step,newTxRxRateListTobeset))
        print("[TEST EXECUTION RESULT] : SUCCESS")

    # Get the initial TxRxRateList
    if proceed_flag == 1:
        step += 1
        paramName = "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.TxRxRateList"
        tdkTestObj = obj.createTestStep('WIFIAgent_Get')
        tdkTestObj.addParameter("paramName",paramName)
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Get the current TxRxRateList value" %step)
        print("EXPECTED RESULT %d: Should get the current TxRxRateList value" %step)

        if expectedresult in actualresult and "VALUE:" in details:
            orgTxRxvalue = details.split("VALUE:")[1].split("TYPE:")[0].strip()
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Current TxRxRateList value is %s" %(step,orgTxRxvalue))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            proceed_flag = 0
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get the current TxRxRateList value. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Set TxRxRateList with applicable Private WiFi AP indexes
    if proceed_flag == 1:
        step += 1
        tdkTestObj = obj.createTestStep('WIFIAgent_Set')
        tdkTestObj.addParameter("paramName",paramName)
        tdkTestObj.addParameter("paramValue",newTxRxRateListTobeset)
        tdkTestObj.addParameter("paramType","string")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Set TxRxRateList with the applicable Private WiFi AP list" %step)
        print("EXPECTED RESULT %d: Should set TxRxRateList to %s" %(step,newTxRxRateListTobeset))

        if expectedresult in actualresult:
            revert_flag = 1
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Set operation was successful. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : SUCCESS")
            sleep(5)
        else:
            proceed_flag = 0
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Set operation failed. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Validate the TxRxRateList SET operation
    if proceed_flag == 1:
        step += 1
        tdkTestObj = obj.createTestStep('WIFIAgent_Get')
        tdkTestObj.addParameter("paramName",paramName)
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Get and validate the TxRxRateList value after SET" %step)
        print("EXPECTED RESULT %d: TxRxRateList should be %s" %(step,newTxRxRateListTobeset))

        if expectedresult in actualresult and "VALUE:" in details:
            newTxRxvalue = details.split("VALUE:")[1].split("TYPE:")[0].strip()
            if newTxRxvalue == newTxRxRateListTobeset:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: TxRxRateList value after SET is %s" %(step,newTxRxvalue))
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Expected %s, but retrieved %s" %(step,newTxRxRateListTobeset,newTxRxvalue))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to get TxRxRateList after SET. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Restore the initial TxRxRateList
    if revert_flag == 1:
        step += 1
        tdkTestObj = obj.createTestStep('WIFIAgent_Set')
        tdkTestObj.addParameter("paramName",paramName)
        tdkTestObj.addParameter("paramValue",orgTxRxvalue)
        tdkTestObj.addParameter("paramType","string")
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Restore the initial TxRxRateList value" %step)
        print("EXPECTED RESULT %d: Should restore TxRxRateList to %s" %(step,orgTxRxvalue))

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: TxRxRateList was restored successfully. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to restore TxRxRateList. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        print("TxRxRateList revert operation is not required")

    obj.unloadModule("wifiagent")
else:
    print("Failed to load wifiagent module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")


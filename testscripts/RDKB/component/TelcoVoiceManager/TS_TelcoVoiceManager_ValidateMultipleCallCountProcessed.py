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
from tdkutility import *
from time import sleep
from tdkbTelcoVoiceManagerVariables import *
from tdkbTelcoVoiceManagerUtility import *

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1")
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_ValidateMultipleCallCountProcessed')
tr181obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_ValidateMultipleCallCountProcessed')

# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
if expectedresult in loadmodulestatus.upper() and expectedresult in loadmodulestatus_tr181.upper():
    obj.setLoadModuleStatus("SUCCESS")
    tr181obj.setLoadModuleStatus("SUCCESS")

    print(f"Prerequisite : Two SIP clients need to be activated within the same WAN network using the default usernames and passwords specified in {pjsip_conf_file}.")

    # Get the current total number of calls processed before multiple call attempts
    step = 'A'
    print(f"\nTEST STEP {step}: Get the total number of calls processed from the asterisk server before multiple call attempts.")
    print(f"EXPECTED RESULT {step}: Should get the total number of calls processed from the asterisk server and it should be an integer value.")
    tdkTestObj, actualresult, initial_call_count = getTotalCallsProcessed(obj)
    if expectedresult in actualresult and type(initial_call_count) is int:
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Initial number of calls processed before multiple call attempts is {initial_call_count}.")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        for attempt in range(1, max_call_attempt+1):
            # Call Initiation between inbound SIP Clients
            print(f"\nAttempt {attempt} : Initiating a call between the SIP clients configured in the same WAN network")
            dialplan_context = "internal"
            initiate_call_status = initiateCall(obj, client1_username, client2_username, dialplan_context, attempt)
            if initiate_call_status:
                print("Call has been initiated successfully between the SIP clients in the same WAN network")
                sleep(5)
                print("\nDisconnecting the call between the SIP clients in the same WAN network")
                hangup_status = callHangup(obj, attempt)
                if hangup_status:
                    print("Call has been disconnected successfully.")
                else:
                    print("Failed to disconnect the call.")
            else:
                print("Failed to initiate the call between the SIP clients in the same WAN network")
        #Get the total number of calls processed
        step = 'B'
        print(f"\nTEST STEP {step}: Get the total number of calls processed from the asterisk server after multiple call attempts.")
        print(f"EXPECTED RESULT {step}: Should get the total number of calls processed from the asterisk server and it should be equal to the number of call attempts.")
        tdkTestObj, actualresult, final_call_count = getTotalCallsProcessed(obj)
        total_calls_processed = final_call_count - initial_call_count
        if expectedresult in actualresult and type(total_calls_processed) is int and total_calls_processed == max_call_attempt:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: Total number of calls processed after multiple call attempts is {total_calls_processed} which is equal to the number of call attempts.")
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Total number of calls processed after multiple call attempts is {total_calls_processed} which is not equal to the number of call attempts.")
            print("[TEST EXECUTION RESULT] : FAILURE")

    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to get the total number of calls processed from the asterisk server before multiple call attempts. Details: {initial_call_count}")
        print("[TEST EXECUTION RESULT] : FAILURE")
    obj.unloadModule("sysutil")
    tr181obj.unloadModule("tdkbtr181")
else:
    print("\nFailed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    tr181obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

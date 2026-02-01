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
from tdkutility import *
from time import sleep
from tdkbTelcoVoiceManagerVariables import *
from tdkbTelcoVoiceManagerUtility import *

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1")
# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_ValidateActiveInboundCallCount')
# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
step = 1
loadmodulestatus = obj.getLoadModuleResult()
if expectedresult in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    print("Prerequisite : Two SIP clients need to be activated within the same WAN network using the default usernames and passwords specified in /etc/asterisk/pjsip.conf.")
    
    #Get the initial active call count
    print(f"\nTEST STEP {step}: Get the initial active call count from the asterisk server.")
    print(f"EXPECTED RESULT {step}: Should get the active call count from the asterisk server.")
    tdkTestObj, actualresult, initial_call_count = getActiveCallCount(obj)
    if expectedresult in actualresult and initial_call_count.strip().isdigit():
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Initial active call count is {initial_call_count.strip()}")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step +=1
        # Call Initiation between inbound SIP Clients
        print("\nInitiating a call between the SIP clients configured in the same WAN network")
        dialplan_context = "internal"
        initiate_call_status = initiateCall(obj, client1_username, client2_username, dialplan_context, step)
        if initiate_call_status:
            print("Call has been initiated successfully between the SIP clients in the same WAN network")

            step += 1
            sleep(20)
            #Get the active call count after call initiation
            print(f"\nTEST STEP {step}: Get the active call count from the asterisk server after call initiation.")
            print(f"EXPECTED RESULT {step}: Active call count should be incremented by 1 after call initiation.")
            tdkTestObj, actualresult, call_count = getActiveCallCount(obj)
            if expectedresult in actualresult and int(call_count.strip()) == int(initial_call_count.strip()) + 1:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: The active call count is incremented by 1 after call initiation. Current active call count is {call_count.strip()}")
                print("[TEST EXECUTION RESULT] : SUCCESS")
                        
                step += 1
                print("\nDisconnecting the call between the SIP clients in the same WAN network")
                hangup_status = callHangup(obj, step)
                if hangup_status:
                    print("Call has been disconnected successfully.")

                    #Validate the active call count after hanging up the call
                    step += 1
                    print(f"\nTEST STEP {step}: Get the active call count from the asterisk server after hanging up the call.")
                    print(f"EXPECTED RESULT {step}: Active call count should be equal to the initial active call count.")
                    tdkTestObj, actualresult, final_call_count = getActiveCallCount(obj)
                    if expectedresult in actualresult and int(final_call_count.strip()) == int(initial_call_count.strip()):
                        tdkTestObj.setResultStatus("SUCCESS")
                        print(f"ACTUAL RESULT {step}: The active call count is equal to the initial active call count after hanging up the call. Current active call count is {final_call_count.strip()}")
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print(f"ACTUAL RESULT {step}: The active call count is not equal to the initial active call count after hanging up the call. Current active call count is {final_call_count.strip()}")
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    print("Failed to disconnect the call.")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: The active call count is not incremented by 1 after call initiation. Current active call count is {call_count.strip()}")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            print("Failed to initiate the call between the SIP clients in the same WAN network")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to get the initial active call count from the asterisk server. Details: {initial_call_count}")
        print("[TEST EXECUTION RESULT] : FAILURE")
    obj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

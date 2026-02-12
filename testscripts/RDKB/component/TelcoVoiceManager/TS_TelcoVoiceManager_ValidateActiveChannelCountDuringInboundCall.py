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
# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_ValidateActiveChannelCountDuringInboundCall')
# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
step = 1
loadmodulestatus = obj.getLoadModuleResult()
if expectedresult in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    print(f"Prerequisite : Two SIP clients need to be activated within the same WAN network using the default usernames and passwords specified in {pjsip_conf_file}.")

    #Cleaning up the existing calls if any before starting the test execution
    print("\nCleaning up the existing calls if any before starting the test execution")
    hangup_status = callHangup(obj, step, prereq=True)
    if hangup_status:
        print("Existing calls if any are cleaned up successfully before starting the test execution")

        step += 1
        #Get the initial active channel count
        print(f"\nTEST STEP {step}: Get the initial active channel count from the asterisk server.")
        print(f"EXPECTED RESULT {step}: Should get the active channel count from the asterisk server as zero.")
        tdkTestObj, actualresult, initial_channel_count = getActiveChannelCount(obj)
        if expectedresult in actualresult and type(initial_channel_count) is int and initial_channel_count == 0:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: Initial active channel count is {initial_channel_count}")
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step +=1
            # Call Initiation between inbound SIP Clients
            print("\nInitiating a call between the SIP clients configured in the same WAN network")
            dialplan_context = "internal"
            initiate_call_status = initiateCall(obj, client1_username, client2_username, dialplan_context, step)
            if initiate_call_status:
                print("Call has been initiated successfully between the SIP clients in the same WAN network")

                step += 1
                sleep(5)
                #Get the active channel count after call initiation
                print(f"\nTEST STEP {step}: Get the active channel count from the asterisk server after call initiation.")
                print(f"EXPECTED RESULT {step}: Active channel count should be incremented by 2 after call initiation.")
                tdkTestObj, actualresult, channel_count = getActiveChannelCount(obj)
                if expectedresult in actualresult  and type(channel_count) is int and channel_count == initial_channel_count + 2:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: The active channel count is incremented by 2 after call initiation. Current active channel count is {channel_count}")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step += 1
                    print("\nDisconnecting the call between the SIP clients in the same WAN network")
                    hangup_status = callHangup(obj, step)
                    if hangup_status:
                        print("Call has been disconnected successfully.")

                        #Validate the active channel count after hanging up the call
                        step += 1
                        print(f"\nTEST STEP {step}: Get the active channel count from the asterisk server after hanging up the call.")
                        print(f"EXPECTED RESULT {step}: Active channel count should be equal to the initial active channel count.")
                        tdkTestObj, actualresult, final_channel_count = getActiveChannelCount(obj)
                        if expectedresult in actualresult and type(final_channel_count) is int and final_channel_count == initial_channel_count:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: The active channel count is equal to the initial active channel count after hanging up the call. Current active channel count is {final_channel_count}")
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: The active channel count is not equal to the initial active channel count after hanging up the call. Current active channel count is {final_channel_count}")
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        print("Failed to disconnect the call.")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: The active channel count is not incremented by 2 after call initiation. Current active channel count is {channel_count}")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                print("Failed to initiate the call between the SIP clients in the same WAN network")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: The initial active channel count is not same as the expected value. Details: {initial_channel_count}")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        print("Failed to clean up the existing calls if any before starting the test execution")
    obj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

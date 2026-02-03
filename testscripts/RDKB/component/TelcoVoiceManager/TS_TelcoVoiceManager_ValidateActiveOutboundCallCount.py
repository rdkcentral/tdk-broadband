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

obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_ValidateActiveOutboundCallCount')
tr181obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_ValidateActiveOutboundCallCount')

# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
step = 1
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus1 = tr181obj.getLoadModuleResult()

if expectedresult in loadmodulestatus.upper() and expectedresult in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS")
    tr181obj.setLoadModuleStatus("SUCCESS")

    print("Prerequisite : One SIP client need to be activated within the same WAN network using the default usernames and passwords specified in /etc/asterisk/pjsip.conf.\n Another external SIP client endpoint needs to be configured in subscribe.linphone.org")

    #Cleaning up the existing calls if any before starting the test execution
    print("\nCleaning up the existing calls if any before starting the test execution")
    hangup_status = callHangup(obj, step, prereq=True)
    if hangup_status:
        print("Existing calls if any are cleaned up successfully before starting the test execution")

        step += 1

        #Get the outbound call configurations
        get_flag, initial_values = getTelcoOutboundConfigs(tr181obj, step)
        if get_flag:
            #Set the outbound call configurations
            step += 1
            valueList = [outbound_line_enable, outbound_proxy, outbound_port, outbound_client_username, outbound_client_password]
            set_flag = setTelcoOutboundConfigs(tr181obj, valueList, step)

            if set_flag:
                step += 1
                #Get the initial active call count
                print(f"\nTEST STEP {step}: Get the initial active call count from the asterisk server.")
                print(f"EXPECTED RESULT {step}: Should get the active call count from the asterisk server.")
                tdkTestObj, actualresult, initial_call_count = getActiveCallCount(obj)
                if expectedresult in actualresult and type(initial_call_count) is int and initial_call_count == 0:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: Initial active call count is {initial_call_count}")
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    step +=1
                    # Call Initiation between outbound SIP Clients
                    print("\nInitiating an outbound call from the SIP Client in the same WAN network to an external endpoint")
                    dialplan_context = "external"
                    initiate_call_status = initiateCall(obj, client1_username, outbound_client_username, dialplan_context, step)
                    if initiate_call_status:
                        print("Call has been initiated successfully between the SIP clients")

                        step += 1
                        sleep(10)
                        #Get the active call count after call initiation
                        print(f"\nTEST STEP {step}: Get the active call count from the asterisk server after call initiation.")
                        print(f"EXPECTED RESULT {step}: Active call count should be incremented by 1 after call initiation.")
                        tdkTestObj, actualresult, call_count = getActiveCallCount(obj)
                        if expectedresult in actualresult and type(call_count) is int and call_count == initial_call_count + 1:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print(f"ACTUAL RESULT {step}: The active call count is incremented by 1 after call initiation. Current active call count is {call_count}")
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                            step += 1
                            print("\nDisconnecting the call between the configured SIP clients")
                            hangup_status = callHangup(obj, step)
                            if hangup_status:
                                print("Call has been disconnected successfully.")

                                #Validate the active call count after hanging up the call
                                step += 1
                                print(f"\nTEST STEP {step}: Get the active call count from the asterisk server after hanging up the call.")
                                print(f"EXPECTED RESULT {step}: Active call count should be equal to the initial active call count.")
                                tdkTestObj, actualresult, final_call_count = getActiveCallCount(obj)
                                if expectedresult in actualresult and type(final_call_count) is int and final_call_count == initial_call_count:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print(f"ACTUAL RESULT {step}: The active call count is equal to the initial active call count after hanging up the call. Current active call count is {final_call_count}")
                                    print("[TEST EXECUTION RESULT] : SUCCESS")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print(f"ACTUAL RESULT {step}: The active call count is not equal to the initial active call count after hanging up the call. Current active call count is {final_call_count}")
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                print("Failed to disconnect the call.")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print(f"ACTUAL RESULT {step}: The active call count is not incremented by 1 after call initiation. Current active call count is {call_count}")
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        print("Failed to initiate the call between the SIP clients configured")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: Failed to get the initial active call count from the asterisk server. Details: {initial_call_count}")
                    print("[TEST EXECUTION RESULT] : FAILURE")

                #Revert the outbound call configurations to initial values
                step += 1
                print(f"Reverting the outbound call configurations to initial values.")
                revert_flag = setTelcoOutboundConfigs(tr181obj, initial_values, step)
                if revert_flag:
                    print("Successfully reverted the outbound call configurations to initial values.")
                else:
                    print("Failed to revert the outbound call configurations to initial values.")
            else:
                print(f"The outbound call configurations are not updated properly.")
        else:
            print(f"The outbound call configurations are not retrieved successfully.")
    else:
        print("Failed to clean up the existing calls if any before starting the test execution")

    obj.unloadModule("sysutil")
    tr181obj.unloadModule("tdkbtr181")

else:
    print("\nFailed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    tr181obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

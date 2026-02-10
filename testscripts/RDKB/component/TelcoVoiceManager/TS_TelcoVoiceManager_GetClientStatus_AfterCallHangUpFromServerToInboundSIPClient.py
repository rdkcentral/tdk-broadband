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
from tdkbTelcoVoiceManagerVariables import *
from tdkbTelcoVoiceManagerUtility import *

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1")
# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_GetClientStatus_AfterCallHangUpFromServerToInboundSIPClient')
# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
step = 1
loadmodulestatus = obj.getLoadModuleResult()
if expectedresult in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    print("Prerequisite : One SIP client need to be activated within the same WAN network using the default usernames and passwords specified in /etc/asterisk/pjsip.conf.")

    #Cleaning up the existing calls if any before starting the test execution
    print("\nCleaning up the existing calls if any before starting the test execution")
    hangup_status = callHangup(obj, step, prereq=True)
    if hangup_status:
        print("Existing calls if any are cleaned up successfully before starting the test execution")

        step += 1
        # Call Initiation between from asterisk server to inbound SIP client
        print(f"\nInitiating a call from the Asterisk Server the SIP client {client1_username} configured in the same WAN network")
        dialplan_context = "internal"
        initiate_call_status = initiateCall(obj, client1_username, client1_username, dialplan_context, step)
        if initiate_call_status:
            print("Call has been initiated successfully from the Asterisk Server the inbound SIP client ")

            step += 1
            print("\nDisconnecting the call from asterisk server to the inbound SIP client")
            hangup_status = callHangup(obj, step)
            if hangup_status:
                print("Call has been disconnected successfully.")

                step += 1
                #Client1 Status after hangup
                print(f"\nTEST STEP {step}: Check whether the SIP client status is 'Not in use' after hangup in client - {client1_username}.")
                print(f"EXPECTED RESULT {step}: The SIP Client status should be 'Not in Use', indicating hung up call in client.")
                tdkTestObj, actualresult, status = clientStatus(obj, client1_username)
                if expectedresult in actualresult and "Not in use" in status:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: The call is hung up and SIP client status is {status}")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: The SIP client status is {status}")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                print("Failed to disconnect the call.")
        else:
            print("Failed to initiate the call between the SIP clients in the same WAN network")
    else:
        print("Failed to clean up the existing calls if any before starting the test execution")

    obj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

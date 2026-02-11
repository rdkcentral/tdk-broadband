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

obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_GetInvalidClientStatusDuringInboundCall')
# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
invalid_client = "9001"
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
        # Call Initiation between valid to invalid inbound SIP Clients
        print("\nInitiating a call the valid inbound SIP client to the invalid inbound SIP client")
        dialplan_context = "internal"
        initiate_call_status = initiateCall(obj, client1_username, invalid_client, dialplan_context, step)
        if initiate_call_status:
            print("Call has been initiated successfully between the SIP clients.")

            step += 1
            # Client1 Status after connecting client
            print(f"\nTEST STEP {step}: Check whether the call between SIP clients failed in client 1 - {client1_username}.")
            print(f"EXPECTED RESULT {step}: The SIP Client status should be Not in use, indicating failed in client 1.")
            tdkTestObj, actualresult, status = clientStatus(obj, client1_username)
            if expectedresult in actualresult and "Not in use" in status:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: The call connection failed and SIP client 1 status is {status}")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                #Check whether invalid client failed to exist the endpoint list
                print(f"\nTEST STEP {step}: Check whether the client 2 - {invalid_client} is listed as an endpoint.")
                print(f"EXPECTED RESULT {step}: The invalid SIP client, {invalid_client} is not listed as an endpoint.")
                tdkTestObj, actualresult, status = clientStatus(obj, invalid_client)
                if expectedresult in actualresult and "" in status:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print(f"ACTUAL RESULT {step}: The invalid SIP client - {invalid_client} is not listed as an endpoint")
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print(f"ACTUAL RESULT {step}: The invalid SIP client - {invalid_client} is listed as an endpoint")
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: The SIP client 1 status is {status}")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            print("Failed to initiate the call between valid inbound SIP client to invalid SIP client")
    else:
        print("Failed to clean up the existing calls if any before starting the test execution")
    obj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

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
from time import sleep

# Test component to be tested
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

tr181obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_GetVoiceProfileLineStatusAfterInvalidOutboundCallConfiguration')

# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
invalid_client_username = "dummy123"
invalid_client_password = "dummy123#"
step = 1
loadmodulestatus = tr181obj.getLoadModuleResult()

if expectedresult in loadmodulestatus.upper():
    tr181obj.setLoadModuleStatus("SUCCESS")

    print("Prerequisite : One SIP client need to be activated within the same WAN network using the default usernames and passwords specified in /etc/asterisk/pjsip.conf.\n Another external SIP client endpoint needs to be configured in subscribe.linphone.org")

    #Get the outbound call configurations
    get_flag, initial_values = getTelcoOutboundConfigs(tr181obj, step)
    if get_flag:
        #Set the outbound call configurations with invalid outbound endpoint credentials
        step += 1
        print("\nSetting the outbound call configurations with invalid outbound endpoint credentials")
        valueList = [outbound_line_enable, outbound_proxy, outbound_port, invalid_client_username, invalid_client_password]
        set_flag = setTelcoOutboundConfigs(tr181obj, valueList, step)

        if set_flag:
            print("Outbound call configurations are set with invalid outbound endpoint credentials successfully")
            sleep(5)
            #Get the  Voice Call Line status
            step += 1
            print(f"\nTEST STEP {step}: Get the Line Status once the invalid configurations are updated")
            print(f"EXPECTED RESULT {step}: Should get the Line Status once the invalid configurations are updated")
            tdkTestObj, actualresult, status = getLineStatus(tr181obj)
            if expectedresult in actualresult and status == "Error":
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: Successfully got the Line Status once the invalid configurations are updated as {status}")
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: Failed to get the Line Status once the invalid configurations are updated. Status: {status}")
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

    tr181obj.unloadModule("tdkbtr181")

else:
    print("\nFailed to load the module")
    tr181obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

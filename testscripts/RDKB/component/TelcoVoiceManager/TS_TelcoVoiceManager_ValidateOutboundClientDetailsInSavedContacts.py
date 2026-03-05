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
from tdkbTelcoVoiceManagerVariables import *
from tdkbTelcoVoiceManagerUtility import *
import re

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1")
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_ValidateOutboundClientDetailsInSavedContacts')
tr181obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_ValidateOutboundClientDetailsInSavedContacts')

print(f"Prerequisite : One external SIP client endpoint needs to be configured in subscribe.linphone.org.")


# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
step = 1
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_tr181 = tr181obj.getLoadModuleResult()
if expectedresult in loadmodulestatus.upper() and expectedresult in loadmodulestatus_tr181.upper():
    obj.setLoadModuleStatus("SUCCESS")

    #Get the outbound call configurations
    print("\nGetting the outbound call configurations")
    get_flag, initial_values = getTelcoOutboundConfigs(tr181obj, step)
    if get_flag:
        print("Successfully retrieved the outbound call configurations")
        #Set the outbound call configurations
        step += 1
        print("\nSetting the outbound call configurations")
        valueList = [outbound_line_enable, outbound_proxy, outbound_port, outbound_client_username, outbound_client_password]
        set_flag = setTelcoOutboundConfigs(tr181obj, valueList, step)

        if set_flag:
            print("Outbound call configurations are set successfully")
            step += 1
            #Check whether the outbound Client details are saved in contact list
            print(f"\nChecking whether the outbound Client details are saved in contact list.")

            available_flag = isAvailableInContactList(obj, [outbound_client_username], step)
            if available_flag:
                print("The outbound Client details are saved in contact list.")
            else:
                print("The outbound Client details are NOT saved in contact list.")

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
    obj.unloadModule("sysutil")
    tr181obj.unloadModule("tdkbtr181")
else:
    print("\nFailed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    tr181obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

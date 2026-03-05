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
# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_ValidateInboundClientDetailsInSavedContacts')
# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
step = 1
loadmodulestatus = obj.getLoadModuleResult()
if expectedresult in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")

    #Check the existence pjsip configuration file
    print(f"TEST STEP {step}: Check for the existence of pjsip configuration file at {pjsip_conf_file}.")
    print(f"EXPECTED RESULT {step}: The pjsip configuration file should exist.")
    tdkTestObj = obj.createTestStep('ExecuteCmd')
    actualresult, details = isFilePresent(tdkTestObj, pjsip_conf_file)
    if expectedresult in actualresult and details != "":
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: The pjsip configuration file found at {pjsip_conf_file}. Details: {details}")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        #Validate Inbound Client details in pjsip configuration file
        print(f"\nTEST STEP {step}: Get the Inbound Client details in pjsip configuration file.")
        print(f"EXPECTED RESULT {step}: Should get the Inbound Client details in pjsip configuration file.")
        tdkTestObj = obj.createTestStep('ExecuteCmd')
        command = f"cat {pjsip_conf_file} | grep 'username' | xargs"
        print(f"Command: {command}")
        actualresult, details = doSysutilExecuteCommand(tdkTestObj, command)
        print(f"Command Output: {details}")
        conf_clients = re.findall(r'username=(\S+)', details)

        if actualresult in expectedresult and "" not in conf_clients:
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: The Inbound Client details are present in pjsip configuration file. SIP Clients : {conf_clients}.")
            print("[TEST EXECUTION RESULT] : SUCCESS")

            #Get the primary endpoints and check whether they match with the Inbound Client details in configuration file
            step += 1
            print(f"\nTEST STEP {step}: Get the primary endpoints and check whether they match with the Inbound Client details in configuration file.")
            print(f"EXPECTED RESULT {step}: The primary endpoints should match with the Inbound Client details in configuration file.")
            tdkTestObj = obj.createTestStep('ExecuteCmd')
            command = f"asterisk -rx 'pjsip show endpoints' | awk '/Endpoint:/ && $2 !~ /</ {{print $2}}' | xargs"
            print(f"Command: {command}")
            actualresult, details = doSysutilExecuteCommand(tdkTestObj, command)
            print(f"Command Output: {details}")
            endpoints = details.strip().split(" ")
            if actualresult in expectedresult and "" not in endpoints and endpoints == conf_clients:
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: The primary endpoints match with the Inbound Client details in configuration file. Client Endpoint Details : {endpoints}.")
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                #Check whether the Inbound Client details are saved in contact list
                print(f"\nChecking whether the Inbound Client details are saved in contact list.")

                available_flag = isAvailableInContactList(obj, conf_clients, step)
                if available_flag:
                    print("The Inbound Client details are saved in contact list.")
                else:
                    print("The Inbound Client details are NOT saved in contact list.")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: The primary endpoints do NOT match with the Inbound Client details in configuration file. Client Endpoint Details : {endpoints}.")
                print("[TEST EXECUTION RESULT] : FAILURE")

        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: The Inbound Client details are NOT present in pjsip configuration file. SIP Clients : {conf_clients}.")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: The pjsip configuration file not found at {pjsip_conf_file}. Details: {details}")
        print("[TEST EXECUTION RESULT] : FAILURE")
    obj.unloadModule("sysutil")
else:
    print("\nFailed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

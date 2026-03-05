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
from tdkutility import *

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_TelcoVoiceManager_ValidateVoiceProfileLineStatusEnabled')
# Get the result of connection with test component and DUT
expectedresult = "SUCCESS"
step = 1
loadmodulestatus = obj.getLoadModuleResult()
if expectedresult in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")
    #Get the value of Voice Profile Line Enable
    print(f"\nTEST STEP {step}: Get the value of Voice Profile Line Enable")
    print(f"EXPECTED RESULT {step}: Should get the value of Voice Profile Line Enable")
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    actualresult, line_enable = getTR181Value(tdkTestObj, "Device.Services.VoiceService.1.VoiceProfile.1.Line.1.Enable")
    if expectedresult in actualresult and line_enable != "":
        tdkTestObj.setResultStatus("SUCCESS")
        print(f"ACTUAL RESULT {step}: Successfully got the value of Voice Profile Line Enable: {line_enable}")
        print("[TEST EXECUTION RESULT] : SUCCESS")

        #Set the Voice Profile Line Enable to Enabled
        step += 1
        print(f"\nTEST STEP {step}: Set the value of Voice Profile Line Enable to Enabled")
        print(f"EXPECTED RESULT {step}: Should set the value of Voice Profile Line Enable to Enabled successfully")
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
        actualresult, details = setTR181Value(tdkTestObj, "Device.Services.VoiceService.1.VoiceProfile.1.Line.1.Enable", "Enabled", "string")
        if expectedresult in actualresult and details != "":
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"ACTUAL RESULT {step}: Successfully set the value of Voice Profile Line Enable to Enabled. Details: {details}")
            print("[TEST EXECUTION RESULT] : SUCCESS")

            #Validate whether the Voice Profile Line status is Initializing after the Line is enabled
            step += 1
            print(f"\nTEST STEP {step}: Validate whether the Voice Profile Line status is Initializing after the Line is enabled")
            print(f"EXPECTED RESULT {step}: The Voice Profile Line status should be Initializing after the Line is enabled")
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
            actualresult, details = getTR181Value(tdkTestObj, "Device.Services.VoiceService.1.VoiceProfile.1.Line.1.Status")
            if expectedresult in actualresult and details == "Initializing":
                tdkTestObj.setResultStatus("SUCCESS")
                print(f"ACTUAL RESULT {step}: The Voice Profile Line status is Initializing after the Line is enabled as expected. Details: {details}")
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(f"ACTUAL RESULT {step}: The Voice Profile Line status is not Initializing after the Line is enabled. Details: {details}")
                print("[TEST EXECUTION RESULT] : FAILURE")
        #Revert the Voice Profile Line Enable to initial value
        step += 1
        print(f"\nTEST STEP {step}: Revert the Voice Profile Line Enable to initial value")
        print(f"EXPECTED RESULT {step}: Should revert the Voice Profile Line Enable to initial value successfully")
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
        actualresult, details = setTR181Value(tdkTestObj, "Device.Services.VoiceService.1.VoiceProfile.1.Line.1.Enable", line_enable, "string")
        if expectedresult in actualresult and details != "":
            tdkTestObj.setResultStatus("SUCCESS")
            print(f"Successfully reverted the Voice Profile Line Enable to initial value. Details: {details}")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(f"ACTUAL RESULT {step}: Failed to set the value of Voice Profile Line Enable to Enabled. Details: {details}")
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(f"ACTUAL RESULT {step}: Failed to get the value of Voice Profile Line Enable. Details: {line_enable}")
        print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("tdkbtr181")
else:
    print("\nFailed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

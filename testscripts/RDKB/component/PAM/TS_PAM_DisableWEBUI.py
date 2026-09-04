##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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

# Use tdklib library, which provides a wrapper for TDK test case scripts
import tdklib
from time import sleep

# Test component to be tested
pamObj = tdklib.TDKScriptingLibrary("pam", "RDKB")

# IP and Port of box, no need to change
# These values will be replaced with the corresponding DUT IP and port
ip = <ipaddress>
port = <port>

pamObj.configureTestCase(ip,port,"TS_PAM_DisableWEBUI")

expectedresult = "SUCCESS"

WEBUI_PARAM = "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable"
HTTP_ENABLE_PARAM = "Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable"


def getParameterValue(pamObj, paramName):
    tdkTestObj = pamObj.createTestStep("pam_GetParameterValues")
    tdkTestObj.addParameter("ParamName",paramName)
    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails().strip()

    return tdkTestObj, actualresult, details


def setParameterValue(pamObj, paramName, paramValue, paramType):
    tdkTestObj = pamObj.createTestStep("pam_SetParameterValues")
    tdkTestObj.addParameter("ParamName",paramName)
    tdkTestObj.addParameter("ParamValue",paramValue)
    tdkTestObj.addParameter("Type",paramType)
    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    return tdkTestObj, actualresult, details


# Get the result of connection with the test component and DUT
loadmodulestatus = pamObj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus)

if "SUCCESS" in loadmodulestatus.upper():
    pamObj.setLoadModuleStatus("SUCCESS")

    proceed_flag = 1
    webui_revert_flag = 0
    default_webui = ""
    default_http = ""

    # Get the initial WEBUI Enable value
    tdkTestObj, webui_result, default_webui = getParameterValue(
        pamObj,
        WEBUI_PARAM
    )

    # Get the initial Remote Access HTTP Enable value
    tdkTestObj, http_result, default_http = getParameterValue(
        pamObj,
        HTTP_ENABLE_PARAM
    )

    print("TEST STEP 1: Get the current WEBUI config and HTTP Enable status")
    print("EXPECTED RESULT 1: Should get the WEBUI config and HTTP Enable status")

    if (
        expectedresult in webui_result
        and expectedresult in http_result
        and default_webui != ""
        and default_http in ["true","false"]
    ):
        tdkTestObj.setResultStatus("SUCCESS")
        print(
            "ACTUAL RESULT 1: WEBUI config is %s, HTTP Enable status is %s"
            %(default_webui,default_http)
        )
        print("[TEST EXECUTION RESULT] : SUCCESS")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(
            "ACTUAL RESULT 1: WEBUI config is %s, HTTP Enable status is %s"
            %(default_webui,default_http)
        )
        print("[TEST EXECUTION RESULT] : FAILURE")
        proceed_flag = 0

    # Enable Remote Access HTTP if it is disabled
    if proceed_flag == 1:
        print("TEST STEP 2: Check if Remote Access HTTP Enable status is true, else enable it")
        print("EXPECTED RESULT 2: Remote Access HTTP Enable status should be true")

        if default_http != "true":
            tdkTestObj, actualresult, details = setParameterValue(
                pamObj,
                HTTP_ENABLE_PARAM,
                "true",
                "bool"
            )

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print(
                    "ACTUAL RESULT 2: Remote Access HTTP Enable status was enabled successfully. Details: %s"
                    %details
                )
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print(
                    "ACTUAL RESULT 2: Failed to enable Remote Access HTTP Enable status. Details: %s"
                    %details
                )
                print("[TEST EXECUTION RESULT] : FAILURE")
                proceed_flag = 0
        else:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT 2: Remote Access HTTP Enable status is already true")
            print("[TEST EXECUTION RESULT] : SUCCESS")

    # Validate that Remote Access HTTP Enable is true
    if proceed_flag == 1:
        tdkTestObj, actualresult, current_http = getParameterValue(
            pamObj,
            HTTP_ENABLE_PARAM
        )

        if expectedresult in actualresult and current_http == "true":
            tdkTestObj.setResultStatus("SUCCESS")
            print("Remote Access HTTP Enable status is now true")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(
                "Remote Access HTTP Enable status is not true. Current value: %s"
                %current_http
            )
            proceed_flag = 0

    # Set WEBUI Enable to Disable
    if proceed_flag == 1:
        tdkTestObj, actualresult, details = setParameterValue(
            pamObj,
            WEBUI_PARAM,
            "Disable",
            "string"
        )

        print("TEST STEP 3: Set the WEBUI Enable status to Disable")
        print("EXPECTED RESULT 3: Should set the WEBUI Enable status to Disable")

        if expectedresult in actualresult:
            webui_revert_flag = 1
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT 3: %s" %details)
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT 3: %s" %details)
            print("[TEST EXECUTION RESULT] : FAILURE")
            proceed_flag = 0

    # Verify that Remote Access HTTP Enable becomes false
    if proceed_flag == 1:
        sleep(10)

        tdkTestObj, actualresult, current_http = getParameterValue(
            pamObj,
            HTTP_ENABLE_PARAM
        )

        print("TEST STEP 4: Check if Remote Access HTTP Enable is disabled after WEBUI is disabled")
        print("EXPECTED RESULT 4: Should get Remote Access HTTP Enable as disabled after WEBUI is disabled")

        if expectedresult in actualresult and current_http == "false":
            tdkTestObj.setResultStatus("SUCCESS")
            print(
                "ACTUAL RESULT 4: Remote Access HTTP Enable status is %s"
                %current_http
            )
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(
                "ACTUAL RESULT 4: Remote Access HTTP Enable status is %s"
                %current_http
            )
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Revert WEBUI Enable to the initial value
    if webui_revert_flag == 1:
        tdkTestObj, actualresult, details = setParameterValue(
            pamObj,
            WEBUI_PARAM,
            default_webui,
            "string"
        )

        print("TEST STEP 5: Revert the WEBUI Enable feature")
        print("EXPECTED RESULT 5: Revert operation should be successful")

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT 5: %s" %details)
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT 5: %s" %details)
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        print("Reverting the WEBUI Enable feature is not required")

    # Revert Remote Access HTTP Enable to the initial value
    if default_http in ["true","false"]:
        tdkTestObj, actualresult, details = setParameterValue(
            pamObj,
            HTTP_ENABLE_PARAM,
            default_http,
            "bool"
        )

        print("TEST STEP 6: Revert the Remote Access HTTP Enable status")
        print(
            "EXPECTED RESULT 6: Remote Access HTTP Enable status should be restored to %s"
            %default_http
        )

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT 6: %s" %details)
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT 6: %s" %details)
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        print(
            "Reverting the Remote Access HTTP Enable status is not possible "
            "because the initial value was not retrieved"
        )

    pamObj.unloadModule("pam")

else:
    print("Failed to load pam module")
    pamObj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

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
#'
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##########################################################################

# Import statements
import tdklib
from time import sleep

# Test component to be tested
pamObj = tdklib.TDKScriptingLibrary("pam", "RDKB")

# IP and Port of box, No need to change
# This will be replaced with corresponding Box IP and port while executing script
ip = <ipaddress>
port = <port>

pamObj.configureTestCase(ip,port, "TS_PAM_MSOonlyWEBUI")

WEBUI_PARAM = "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable"
HTTP_ENABLE_PARAM = "Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable"
EXPECTED_RESULT = "SUCCESS"


def get_parameter_value(pamObj, parameter):
    tdkTestObj = pamObj.createTestStep("pam_GetParameterValues")
    tdkTestObj.addParameter("ParamName", parameter)
    tdkTestObj.executeTestCase(EXPECTED_RESULT)

    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails().strip()

    return tdkTestObj, actualresult, details


def set_parameter_value(pamObj, parameter, value, param_type):
    tdkTestObj = pamObj.createTestStep("pam_SetParameterValues")
    tdkTestObj.addParameter("ParamName", parameter)
    tdkTestObj.addParameter("ParamValue", value)
    tdkTestObj.addParameter("Type", param_type)
    tdkTestObj.executeTestCase(EXPECTED_RESULT)

    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    return tdkTestObj, actualresult, details


def print_get_result(step, description, expected_description,
                     actualresult, details):
    print("\nTEST STEP %d: %s" % (step, description))
    print("EXPECTED RESULT %d: %s" % (step, expected_description))

    if EXPECTED_RESULT in actualresult:
        print("ACTUAL RESULT %d: %s" % (step, details))
        print("[TEST EXECUTION RESULT] : SUCCESS")
    else:
        print("ACTUAL RESULT %d: %s" % (step, details))
        print("[TEST EXECUTION RESULT] : FAILURE")


def print_set_result(step, description, expected_description,
                     actualresult, details):
    print("\nTEST STEP %d: %s" % (step, description))
    print("EXPECTED RESULT %d: %s" % (step, expected_description))

    if EXPECTED_RESULT in actualresult:
        print("ACTUAL RESULT %d: %s" % (step, details))
        print("[TEST EXECUTION RESULT] : SUCCESS")
    else:
        print("ACTUAL RESULT %d: %s" % (step, details))
        print("[TEST EXECUTION RESULT] : FAILURE")


# Get the result of connection with test component and DUT
loadmodulestatus = pamObj.getLoadModuleResult()
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus)

if "SUCCESS" in loadmodulestatus.upper():
    pamObj.setLoadModuleStatus("SUCCESS")

    step = 1
    proceed_flag = 1
    http_revert_flag = 0
    webui_revert_flag = 0
    default_webui = ""
    default_http = ""

    # Get initial WEBUI configuration
    tdkTestObj, webui_get_result, default_webui = get_parameter_value(
        pamObj,
        WEBUI_PARAM
    )

    # Get initial Remote Access HTTP Enable status
    tdkTestObj, http_get_result, default_http = get_parameter_value(
        pamObj,
        HTTP_ENABLE_PARAM
    )

    print("\nTEST STEP %d: Get the current WEBUI configuration and Remote Access HTTP Enable status" % step)
    print("EXPECTED RESULT %d: Should get the WEBUI configuration and Remote Access HTTP Enable status" % step)

    if (
        EXPECTED_RESULT in webui_get_result
        and EXPECTED_RESULT in http_get_result
        and default_webui != ""
        and default_http != ""
    ):
        tdkTestObj.setResultStatus("SUCCESS")
        print(
            "ACTUAL RESULT %d: WEBUI configuration is %s and "
            "Remote Access HTTP Enable status is %s"
            % (step, default_webui, default_http)
        )
        print("[TEST EXECUTION RESULT] : SUCCESS")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print(
            "ACTUAL RESULT %d: Failed to get the WEBUI configuration "
            "or Remote Access HTTP Enable status. WEBUI: %s, HTTP Enable: %s"
            % (step, default_webui, default_http)
        )
        print("[TEST EXECUTION RESULT] : FAILURE")
        proceed_flag = 0

    # Enable Remote Access HTTP if initially disabled
    if proceed_flag == 1:
        step += 1

        if default_http != "true":
            tdkTestObj, actualresult, details = set_parameter_value(
                pamObj,
                HTTP_ENABLE_PARAM,
                "true",
                "bool"
            )

            print_set_result(
                step,
                "Set the Remote Access HTTP Enable status to true",
                "Should set the Remote Access HTTP Enable status to true",
                actualresult,
                details
            )

            if EXPECTED_RESULT in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                http_revert_flag = 1
            else:
                tdkTestObj.setResultStatus("FAILURE")
                proceed_flag = 0
        else:
            tdkTestObj.setResultStatus("SUCCESS")
            print("\nTEST STEP %d: Check whether Remote Access HTTP Enable is already true" % step)
            print("EXPECTED RESULT %d: Remote Access HTTP Enable should be true" % step)
            print("ACTUAL RESULT %d: Remote Access HTTP Enable is already true" % step)
            print("[TEST EXECUTION RESULT] : SUCCESS")

    # Validate Remote Access HTTP Enable status
    if proceed_flag == 1:
        step += 1

        tdkTestObj, actualresult, current_http = get_parameter_value(
            pamObj,
            HTTP_ENABLE_PARAM
        )

        print("\nTEST STEP %d: Verify the Remote Access HTTP Enable status" % step)
        print("EXPECTED RESULT %d: Remote Access HTTP Enable status should be true" % step)

        if EXPECTED_RESULT in actualresult and current_http == "true":
            tdkTestObj.setResultStatus("SUCCESS")
            print(
                "ACTUAL RESULT %d: Remote Access HTTP Enable status is %s"
                % (step, current_http)
            )
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(
                "ACTUAL RESULT %d: Remote Access HTTP Enable status is %s"
                % (step, current_http)
            )
            print("[TEST EXECUTION RESULT] : FAILURE")
            proceed_flag = 0

    # Set WEBUI Enable to MSOonly
    if proceed_flag == 1:
        step += 1

        tdkTestObj, actualresult, details = set_parameter_value(
            pamObj,
            WEBUI_PARAM,
            "MSOonly",
            "string"
        )

        print_set_result(
            step,
            "Set the WEBUI Enable status to MSOonly",
            "Should set the WEBUI Enable status to MSOonly",
            actualresult,
            details
        )

        if EXPECTED_RESULT in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            webui_revert_flag = 1
        else:
            tdkTestObj.setResultStatus("FAILURE")
            proceed_flag = 0

    # Verify that HTTP Enable becomes false after setting MSOonly
    if proceed_flag == 1:
        sleep(10)
        step += 1

        tdkTestObj, actualresult, current_http = get_parameter_value(
            pamObj,
            HTTP_ENABLE_PARAM
        )

        print("\nTEST STEP %d: Check whether Remote Access HTTP Enable is disabled after WEBUI is configured as MSOonly" % step)
        print("EXPECTED RESULT %d: Remote Access HTTP Enable should be false after WEBUI is configured as MSOonly" % step)

        if EXPECTED_RESULT in actualresult and current_http == "false":
            tdkTestObj.setResultStatus("SUCCESS")
            print(
                "ACTUAL RESULT %d: Remote Access HTTP Enable status after "
                "WEBUI is configured as MSOonly is %s"
                % (step, current_http)
            )
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print(
                "ACTUAL RESULT %d: Remote Access HTTP Enable status after "
                "WEBUI is configured as MSOonly is %s"
                % (step, current_http)
            )
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Revert WEBUI Enable to its initial value
    if webui_revert_flag == 1:
        step += 1

        tdkTestObj, actualresult, details = set_parameter_value(
            pamObj,
            WEBUI_PARAM,
            default_webui,
            "string"
        )

        print_set_result(
            step,
            "Revert the WEBUI Enable feature to its initial value",
            "Should revert the WEBUI Enable feature to %s" % default_webui,
            actualresult,
            details
        )

        if EXPECTED_RESULT in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
    else:
        print("WEBUI Enable revert operation is not required")

    # Revert Remote Access HTTP Enable to its initial value
    if http_revert_flag == 1:
        step += 1

        tdkTestObj, actualresult, details = set_parameter_value(
            pamObj,
            HTTP_ENABLE_PARAM,
            default_http,
            "bool"
        )

        print_set_result(
            step,
            "Revert the Remote Access HTTP Enable status to its initial value",
            "Should revert the Remote Access HTTP Enable status to %s"
            % default_http,
            actualresult,
            details
        )

        if EXPECTED_RESULT in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
    else:
        print("Remote Access HTTP Enable revert operation is not required")

    pamObj.unloadModule("pam")

else:
    print("Failed to load pam module")
    pamObj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

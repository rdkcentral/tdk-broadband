##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2025 RDK Management
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
import json
import tdklib
from tdkutility import *
from tdkbTelemetry2_0_Variables import *
from tdkbTelemetry2_0Utility import *

# Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_Telemetry2_0_T2Report_InvalidLogUploadURL')
sysobj.configureTestCase(ip,port,'TS_Telemetry2_0_T2Report_InvalidLogUploadURL')
wifiobj.configureTestCase(ip,port,'TS_Telemetry2_0_T2Report_InvalidLogUploadURL')
# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus_wifi = wifiobj.getLoadModuleResult()
expectedresult = "SUCCESS"
if expectedresult in loadmodulestatus.upper() and expectedresult in loadmodulestatus_sys.upper() and expectedresult in loadmodulestatus_wifi.upper():
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    wifiobj.setLoadModuleStatus("SUCCESS")

    step = 1
    profileType = "JSON"
    numProfiles = 1
    flag = 0
    t2_config = [TELEMETRY_ENABLE, TELEMETRY_CONFIG_URL, TELEMETRY_VERSION]
    print("Telemetry2.0 Prerequisite values are : Enable = %s, ConfigURL = %s, Version = %s" %(TELEMETRY_ENABLE, TELEMETRY_CONFIG_URL, TELEMETRY_VERSION))

    #Get Telemetry Prerequisite configs and validate whether prerequisites are met
    print("\nTEST STEP %d: Get the initial Telemetry2.0 configuration values" %step)
    print("EXPECTED RESULT %d: Should get the Telemetry2.0 configuration values" %step)
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    getStatus,defTelEnable,defURL,defVersion = getinitialTelemetry2_0Values(tdkTestObj)
    print("Initial Telemetry2.0 values : Enable = %s, ConfigURL = %s, Version = %s" %(defTelEnable, defURL, defVersion))

    if getStatus == 1:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Successfully got the Telemetry2.0 configuration values" %step)
        print("[TEST EXECUTION RESULT] : SUCCESS")

        #Validate the prerequisite values
        if t2_config != [defTelEnable, defURL, defVersion]:
            print("Telemetry2.0 Prerequisite values are not met. Hence setting the prerequisite values")

            #Set the Telemetry2.0 prerequisite configs
            step += 1
            print("\nTEST STEP %d: Set the Telemetry2.0 prerequisite configuration values" %step)
            print("EXPECTED RESULT %d: Should set the Telemetry2.0 prerequisite configuration values" %step)
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
            setStatus = setTelemetry2_0Values(tdkTestObj, TELEMETRY_ENABLE, TELEMETRY_CONFIG_URL, TELEMETRY_VERSION)

            if setStatus == 1:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Successfully set the Telemetry2.0 prerequisite configuration values" %step)
                print("[TEST EXECUTION RESULT] : SUCCESS")
            else:
                flag = 1
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to set the Telemetry2.0 prerequisite configuration values" %step)
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            print("Telemetry2.0 Prerequisite values are already set. Proceeding with the test")

        if flag == 0:
            #Get the Report Profile with invalid LogUpload Location URL
            step += 1
            reportProfilesJSON = createReportProfilesJSON(numProfiles, profileType, scenario="invalid_upload_url")
            profile_names = [profile["name"] for profile in reportProfilesJSON["profiles"]]

            report = json.dumps(reportProfilesJSON)
            print("\nReport Profile JSON body to be set : %s" %report)

            print("\n**********************************************************")
            print("Setting Report Profiles with invalid LogUploadURL")
            print("**********************************************************\n")
            check_flag, initial_report_profiles, param_name, step = SetReportProfiles(wifiobj, report, profileType, numProfiles, step)

            if check_flag == 1:
                print("The profile setting has been completed.")
                #Check whether the profile is created in /nvram/.t2reportprofiles/
                step += 1
                print("\nTEST STEP %d: Check whether the profile is created in /nvram/.t2reportprofiles/" %step)
                print("EXPECTED RESULT %d: Profile should be created in /nvram/.t2reportprofiles/" %step)
                print("Profile to be checked : %s" %profile_names)
                tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                profile_check = isProfileFileExist(tdkTestObj, profile_names)
                if not profile_check:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Profile is not created in /nvram/.t2reportprofiles/" %step)
                    print("[TEST EXECUTION RESULT] : FAILURE")

                    #Check whether the report is available under cached folder /nvram/.t2cachedmessages

                    step += 1
                    print("\nTEST STEP %d: Check whether the report is available under cached folder /nvram/.t2cachedmessages" %step)
                    print("EXPECTED RESULT %d: Report should be available under cached folder /nvram/.t2cachedmessages when invalid log upload url is provided" %step)
                    cmd = f"ls /nvram/.t2cachedmessages/ | grep {profile_names[0]}"
                    print("Command : %s" %cmd)
                    tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                    actualresult, details = doSysutilExecuteCommand(tdkTestObj, cmd)
                    if expectedresult in actualresult and profile_names[0] in details:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Report is available under cached folder /nvram/.t2cachedmessages. Details : %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Report is not available under cached folder /nvram/.t2cachedmessages. Details : %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Profile is created in /nvram/.t2reportprofiles/" %step)
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                #Revert to initial value
                step += 1
                print("\nTEST STEP %d: Revert %s to the initial value %s" % (step, param_name, initial_report_profiles))
                print("EXPECTED RESULT %d: Should revert %s to the initial value" % (step, param_name))
                tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set_LargeValue')
                tdkTestObj.addParameter("ParamName",param_name)
                tdkTestObj.addParameter("ParamValue",initial_report_profiles)
                tdkTestObj.addParameter("ParamType","string")
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "")
                if expectedresult in actualresult and "success" in details.lower():
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Successfully reverted %s to initial value. Details : %s" % (step, param_name, details))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to revert %s to initial value. Details : %s" % (step, param_name, details))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                print("Failed to set the profile")
        else:
            print("\nTelemetry2.0 Prerequisite values setting failed.")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get the Telemetry2.0 configuration values" %step)
        print("[TEST EXECUTION RESULT] : FAILURE")
    print("\n")
    #Unload the modules loaded
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
    wifiobj.unloadModule("wifiagent")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    wifiobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")


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
import re
from time import sleep

# Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_Telemetry2_0_ValidateReportGeneration_PerReportingInterval')
sysobj.configureTestCase(ip,port,'TS_Telemetry2_0_ValidateReportGeneration_PerReportingInterval')
wifiobj.configureTestCase(ip,port,'TS_Telemetry2_0_ValidateReportGeneration_PerReportingInterval')
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
            step += 1
            reportProfilesJSON = createReportProfilesJSON(numProfiles, profileType)
            profile_names = [profile["name"] for profile in reportProfilesJSON["profiles"]]
            report = json.dumps(reportProfilesJSON)
            print("Report Profile JSON body to be set : %s" %report)

            check_flag, initial_report_profiles, param_name, step = SetReportProfiles(wifiobj, report, profileType, numProfiles, step)

            if check_flag == 1:
                print("The profile setting has been completed.")
                #Check whether the profile is created in /nvram/.t2reportprofiles/
                step += 1
                print("\nTEST STEP %d: Check whether the profile is created in /nvram/.t2reportprofiles/" %step)
                print("EXPECTED RESULT %d: Profiles should be created in /nvram/.t2reportprofiles/" %step)
                print("Profiles to be checked : %s" %profile_names)
                tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                profile_check = isProfileFileExist(tdkTestObj, profile_names)
                if profile_check:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Profile is created in /nvram/.t2reportprofiles/" %step)
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    sleep(ACTIVATION_TIMEOUT)
                    sleep(10)

                    #Check whether the cJSON report is getting generated in the telemetry2.0 logs
                    step += 1
                    print("\nTEST STEP %d: Check whether the cJSON report is getting generated in the telemetry2.0 logs" %step)
                    print("EXPECTED RESULT %d: cJSON report should be generated in the telemetry2.0 logs" %step)
                    tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                    log_check, report_list = checkReportGenerated(tdkTestObj, profile_names)
                    print("Reports generated in the logs : %s" %report_list)
                    if log_check:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: cJSON report is generated in the telemetry2.0 logs." %step)
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        #Check whether the reports are getting created as per the Reporting Interval
                        step += 1
                        print("\nTEST STEP %d: Validate whether the reports are getting created as per the Reporting Interval of %d seconds" %(step, REPORTING_INTERVAL))
                        print("EXPECTED RESULT %d: Reports should be created as per the Reporting Interval of %d seconds" %(step, REPORTING_INTERVAL))
                        cmd = f"grep {profile_names[0]} /rdklogs/logs/telemetry2_0.txt.0 | grep -i cJSON | sed -n 's/.*\"UPTIME\":\"\\([0-9]*\\)\".*/\\1/p' | xargs"
                        print("Command : %s" %cmd)
                        tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                        actualresult, details = doSysutilExecuteCommand(tdkTestObj, cmd)
                        uptime_list = list(map(int, details.split()))
                        print("Uptime values extracted from the logs: %s" %uptime_list)
                        intervals = [uptime_list[i+1] - uptime_list[i] for i in range(len(uptime_list)-1)]
                        print("Intervals between consecutive reports: %s" %intervals)
                        if all(interval == REPORTING_INTERVAL for interval in intervals):
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: Reports are created as per the Reporting Interval of %d seconds." % (step, REPORTING_INTERVAL))
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Reports are NOT created as per the Reporting Interval of %d seconds." % (step, REPORTING_INTERVAL))
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: cJSON report is not generated in the telemetry2.0 logs." % step)
                        print("[TEST EXECUTION RESULT] : FAILURE")      
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Profile is not created in /nvram/.t2reportprofiles/" %step)
                    print("[TEST EXECUTION RESULT] : FAILURE")
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
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                if expectedresult in actualresult and "success" in details.lower():
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Successfully reverted %s to initial value. Details : %s" % (step, param_name, details))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Failed to revert %s to initial value. Details : %s" % (step, param_name, details))
                    print("[TEST EXECUTION RESULT] : FAILURE")
                             
            else:
                print("Failed to set the profile.")            
        else:
            print("\nTelemetry2.0 Prerequisite values setting failed.")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get the Telemetry2.0 configuration values" %step)
        print("[TEST EXECUTION RESULT] : FAILURE")

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


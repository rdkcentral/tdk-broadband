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
from tr69ACSUtility import *

#Test component to be tested
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

#IP and Port of device type, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
tr181obj.configureTestCase(ip,port,'TS_TR069PA_SetNTPServer_ACS')
sysobj.configureTestCase(ip,port,'TS_TR069PA_SetNTPServer_ACS')

#Get the result of connection with test component and DUT
loadmodulestatus=tr181obj.getLoadModuleResult()
loadmodulestatus1=sysobj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper() and  "SUCCESS" in loadmodulestatus1.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    tr181obj.setLoadModuleStatus("SUCCESS")

    #Check for prerequisites
    tdkTestObj,username,preRequisiteStatus = tr069ACSPreRequisite(tr181obj,sysobj)
    if "SUCCESS" in preRequisiteStatus:
        step = 0
        queryParam = {"name":"Device.Time.NTPServer1"}
        name = queryParam.get("name")

        #Perform get task request and search query to get the value of the parameter
        getValues,step = gettr069ACS(tdkTestObj,username,queryParam,step)
        if getValues:
            # Toggle NTP server
            if getValues[0] == "pool.ntp.org":
                setValue = "time.nist.gov"
            else:
                setValue = "pool.ntp.org"
            queryParam = {"name":"Device.Time.NTPServer1","value":setValue}
            #Perform set task request  to set the value of the parameter
            queryResponse,step = settr069ACS(tdkTestObj,username,queryParam,step)
            if queryResponse:
                #Perform get task request and search query to get the value of the parameter after set
                newValues,step = gettr069ACS(tdkTestObj,username,queryParam,step)
                if newValues:
                    step += 1
                    print("\nTEST STEP %d : Check if get and set value of %s will match or not." %(step,name))
                    print("EXPECTED RESULT %d : Get and set value of %s should match." %(step,name))
                    if newValues[0] == setValue:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d : Get and set value of %s matches." %(step,name))
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        #Revert to original value
                        step += 1
                        print("\nTEST STEP %d: Revert to the original value of %s as %s via ACS server."  % (step,name, getValues[0]))
                        print("EXPECTED RESULT %d: The value of %s should be reverted successfully via ACS server." % (step,name))
                        queryParam = {"name":"Device.Time.NTPServer1","value":getValues[0]}
                        status,queryResponse = tr069ACSQuery(username,queryParam,"set")
                        if status == 200 and queryResponse:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d : Reverted %s to original value successfully." % (step,name))
                            print("[TEST EXECUTION RESULT] : SUCCESS")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d : Failed to revert %s to original value." % (step,name))
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d : Failed to match the get and set values of %s." % (step, name))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    print("Failed to fetch value of the parameter after SET operation.")
            else:
                print("Failed to set value of the parameter.")
        else:
            print("Failed to fetch value of the parameter before SET operation.")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("tr069pa Pre-requisite failed. Please check if tr069 process is running in device or configuration is proper or connection is established.")
        print("[TEST EXECUTION RESULT] : FAILURE")

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("FAILURE to load module.")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")

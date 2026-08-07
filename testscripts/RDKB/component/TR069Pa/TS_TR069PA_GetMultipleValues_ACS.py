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
tr181obj.configureTestCase(ip,port,'TS_TR069PA_GetMultipleValues_ACS')
sysobj.configureTestCase(ip,port,'TS_TR069PA_GetMultipleValues_ACS')

#Get the result of connection with test component and DUT
loadmodulestatus=tr181obj.getLoadModuleResult()
loadmodulestatus1=sysobj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    tr181obj.setLoadModuleStatus("SUCCESS")

    #Check for prerequisites
    tdkTestObj,username,initialValues,preRequisiteStatus = tr069ACSPreRequisite(tr181obj,sysobj)
    if "SUCCESS" in preRequisiteStatus:
        step = 0
        queryParam = {"name":["Device.DeviceInfo.ProductClass","Device.DeviceInfo.Manufacturer"]}
        parameters = queryParam.get("name")
        #Perform get task request and search query to get the value of multiple parameters
        getValues,step = gettr069ACS(tdkTestObj,username,queryParam,step)
        if getValues:
            #Get the multiple parameter values from DUT
            tdkTestObj,getTr181Values,step = getTr181DMValue(tr181obj,queryParam,step)
            if getTr181Values:
                for name in parameters:
                    step += 1
                    print("\nTEST STEP %d : Check if get values of %s from ACS server and DUT will match or not." % (step,name))
                    print( "EXPECTED RESULT %d : Get values of %s from ACS server and DUT should match." % (step,name))
                    if name not in getValues or name not in getTr181Values:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d : Parameter %s is missing in %s." % (step, name, "ACS response" if name not in getValues else "DUT response"))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                        continue
                    if getValues.get(name) == getTr181Values.get(name):
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d : Get values of %s from ACS server and DUT matches." % (step, name))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d : Failed to match the Get values of %s from ACS server and DUT." % (step, name))
                        print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("Failed to fetch values of the parameters.")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("Value retrieved from ACS server is empty or None.")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("tr069pa Pre-requisite failed. Please check if tr069 process is running in DUT or configuration is proper or connection is established.")
        print("[TEST EXECUTION RESULT] : FAILURE")

    revertPrerequisite(tr181obj,initialValues,step)

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("FAILURE to load module.")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
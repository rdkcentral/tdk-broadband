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
tr181obj.configureTestCase(ip,port,'TS_TR069PA_GetLanMode_ACS')
sysobj.configureTestCase(ip,port,'TS_TR069PA_GetLanMode_ACS')

#Get the result of connection with test component and DUT
loadmodulestatus=tr181obj.getLoadModuleResult()
loadmodulestatus1=sysobj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    tr181obj.setLoadModuleStatus("SUCCESS")

    #Check for prerequisites
    tdkTestObj,username,preRequisiteStatus = tr069ACSPreRequisite(tr181obj,sysobj)
    if "SUCCESS" in preRequisiteStatus:
        step = 0
        #Perform get task request and search query to get the value of the parameter
        queryParam = {"name":"Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode"}
        getValue,step = gettr069ACS(tdkTestObj,username,queryParam,step)
        if getValue :
            #Get the value from DUT
            tdkTestObj,getTr181Value,step = getTr181DMValue(tr181obj,queryParam,step)
            if getTr181Value:
                name = queryParam.get("name")
                step += 1
                print("\nTEST STEP %d : Check if get values of %s from ACS server and DUT will match or not." % (step,name))
                print( "EXPECTED RESULT %d : Get values of %s from ACS server and DUT should match." % (step,name))
                if getValue  == getTr181Value:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d : Get values of %s from ACS server and DUT matches." % (step, name))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d : Failed to match the Get values of %s from ACS server and DUT." % (step, name))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                print("Value retrieved from DUT is empty or None.")
        else:
            print("Value retrieved from ACS server is empty or None.")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("tr069pa Pre-requisite failed. Please check if tr069 process is running in DUT or configuration is proper or connection is established.")
        print("[TEST EXECUTION RESULT] : FAILURE")

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("FAILURE to load module.")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")

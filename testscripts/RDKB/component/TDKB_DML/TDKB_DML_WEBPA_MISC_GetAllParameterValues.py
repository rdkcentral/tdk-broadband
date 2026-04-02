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
import tdklib;
from tdkbVariables import *
import tdkbDmlModuleList
import tdkbDmlUtility

#Test component to be tested
obj1 = tdklib.TDKScriptingLibrary("sysutil","1")
obj2 = tdklib.TDKScriptingLibrary("tdkbtr181","1")
rbusobj = tdklib.TDKScriptingLibrary("rbus","1")

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj1.configureTestCase(ip,port,'TDKB_DML_WEBPA_MISC_GetAllParameterValues')
obj2.configureTestCase(ip,port,'TDKB_DML_WEBPA_MISC_GetAllParameterValues')
rbusobj.configureTestCase(ip,port,'TDKB_DML_WEBPA_MISC_GetAllParameterValues')

#Get the result of connection with test component and DUT
loadmodulestatus1=obj1.getLoadModuleResult()
loadmodulestatus2=obj2.getLoadModuleResult()
loadmodulestatus3=rbusobj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper() and "SUCCESS" in loadmodulestatus3.upper():
    #Set the result status of execution
    obj1.setLoadModuleStatus("SUCCESS")
    obj2.setLoadModuleStatus("SUCCESS")
    rbusobj.setLoadModuleStatus("SUCCESS")

    print("\nThe module to test is: MISC ")
    setup_type = "WEBPA"
    factoryReset = "false"
    #Invoke the utility function to validate the datatype and GET values for all configured tr181 params
    failedParams, moduleStatus = tdkbDmlUtility.getAllParams_module(tdkbDmlModuleList.MISC, setup_type, factoryReset, [obj1, obj2], rbusobj, "get")

    print("Status of MISC validation is ", moduleStatus, "\n")

    if moduleStatus == "FAILURE":
        print("The failed params are ", failedParams, "\n")

    obj1.unloadModule("sysutil")
    obj2.unloadModule("tdkbtr181")
    rbusobj.unloadModule("rbus")
else:
    print("Failed to load module")
    obj1.setLoadModuleStatus("FAILURE")
    obj2.setLoadModuleStatus("FAILURE")
    rbusobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

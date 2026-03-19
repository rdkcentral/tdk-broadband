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
from tdkbVariables import *;
import tdkbDmlModuleList
import tdkbDmlUtility

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
rbusobj = tdklib.TDKScriptingLibrary("rbus","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TDKB_DML_TR181_WANMANAGER_WriteAccessComplianceCheck');
rbusobj.configureTestCase(ip,port,'TDKB_DML_TR181_WANMANAGER_WriteAccessComplianceCheck');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=rbusobj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    rbusobj.setLoadModuleStatus("SUCCESS")

    print("\nThe module to test is: WANMANAGER ");
    setup_type = "TDK"
    factoryReset = "false"
    #Invoke the utility function to check if those parameters which are writable pass the write-access compliance test
    failedParams, moduleStatus = tdkbDmlUtility.getAllParams_module(tdkbDmlModuleList.WANMANAGER, setup_type, factoryReset, obj, rbusobj, "writeAccessCompliance");

    print("Status of WANMANAGER validation is ", moduleStatus, "\n");

    if moduleStatus == "FAILURE":
        print("The failed params are ", failedParams, "\n");

    obj.unloadModule("tdkbtr181");
    rbusobj.unloadModule("rbus");
else:
    print("Failed to load module");
    obj.setLoadModuleStatus("FAILURE");
    rbusobj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");

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
tr181obj.configureTestCase(ip,port,'TS_TR069PA_AddDeleteObject_AfterFactoryReset_ACS')
sysobj.configureTestCase(ip,port,'TS_TR069PA_AddDeleteObject_AfterFactoryReset_ACS')

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
        queryParam = {"name":""}
        #save device's current state before it goes for reboot
        sysobj.saveCurrentState()
        #Perform FactoryReset task request to reset the writable tables.
        step += 1
        print("\nTEST STEP %d : Perform FactoryReset task request to reset the writable tables via ACS." %step)
        print("EXPECTED RESULT %d : Perform FactoryReset task request to reset the writable tables via ACS successfully." %step)
        status, queryResponse = tr069ACSQuery(username,queryParam,method="FactoryReset")
        if status == 200 and queryResponse:
            #Restore the device state saved before reboot
            sysobj.restorePreviousStateAfterReboot()
            #Wait upto 5 min to establish connection between ACS and DUT
            print("Sleeping for 300s")
            sleep(300)
            print("The DUT is now up and running.")
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Performed FactoryReset task request to reset the writable tables via ACS successfully." %step)
            print("[TEST EXECUTION RESULT] : SUCCESS")
            print("\nChecking PREREQUISITES after FactoryReset")
            #Check for prerequisites after factory-reset
            tdkTestObj,username,preRequisiteStatus = tr069ACSPreRequisite(tr181obj,sysobj)
            if "SUCCESS" in preRequisiteStatus:
                #Perform get task request and search query to get the value of the parameter
                queryParam1 = {"name":"Device.NAT.PortMappingNumberOfEntries"}
                name1 = queryParam1.get("name")
                orgValue,step = gettr069ACS(tdkTestObj,username,queryParam1,step)
                if orgValue :
                    #Perform AddObject task request for the object
                    step += 1
                    queryParam2 = {"name":"Device.NAT.PortMapping"}
                    name2 = queryParam2.get("name")
                    orgvalue = orgValue.get(name1)
                    print("\nTEST STEP %d: Send AddObject task to add an object instance for %s via ACS." %(step,name2))
                    print("EXPECTED RESULT %d: Send AddObject task to add an object instance for %s via ACS successfully." %(step,name2))
                    status1, queryResponse = tr069ACSQuery(username, queryParam2, method="AddObject")
                    if status1 == 200 and queryResponse:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: AddObject Task successful for %s via ACS server." % (step,name2))
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        #Perform get task request and search query to get the value of the parameter after AddObject task
                        getValue1,step = gettr069ACS(tdkTestObj,username,queryParam1,step)
                        if getValue1 :
                            value1 = getValue1.get(name1)
                            step += 1
                            print("\nTEST STEP %d: Check if number of port mapping entries is incremented by 1 after AddObject."%step)
                            print("EXPECTED RESULT %d : Number of user entries should be incremented by 1 after AddObject." %step)
                            if  isinstance(value1, int) and isinstance(orgvalue, int) and value1 == orgvalue+1:
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: Number of port mapping entries incremented by 1 as expected after AddObject."%step)
                                print("[TEST EXECUTION RESULT] : SUCCESS")

                                #Perform DeleteObject task request for the parameter
                                newObject = f"Device.NAT.PortMapping.{value1}"
                                queryParam3 = {"name": newObject}
                                name3 = queryParam3.get("name")
                                step += 1
                                print("\nTEST STEP %d: Send DeleteObject task to delete an object instance for %s via ACS." %(step,name3))
                                print("EXPECTED RESULT %d: Send DeleteObject task to delete an object instance for %s via ACS successfully." %(step,name3))
                                status2, queryResponse = tr069ACSQuery(username, queryParam3, method="DeleteObject")
                                if status2 == 200 and queryResponse:
                                    tdkTestObj.setResultStatus("SUCCESS")
                                    print("ACTUAL RESULT %d: DeleteObject Task successful for %s via ACS server." % (step,name3))
                                    print("[TEST EXECUTION RESULT] : SUCCESS")

                                    #Perform get task request and search query to get the value of the parameter after DeleteObject task
                                    getValue2,step = gettr069ACS(tdkTestObj,username,queryParam1,step)
                                    if getValue2 :
                                        value2 = getValue2.get(name1)
                                        step += 1
                                        print("\nTEST STEP %d: Check if number of port mapping entries is decremented by 1 after DeleteObject."%step)
                                        print("EXPECTED RESULT %d : Number of port mapping entries should be decremented by 1 after DeleteObject." %step)
                                        if isinstance(value1, int) and isinstance(value2, int) and  value2== value1-1:
                                            tdkTestObj.setResultStatus("SUCCESS")
                                            print("ACTUAL RESULT %d: Number of port mapping entries decremented by 1 after DeleteObject."%step)
                                            print("[TEST EXECUTION RESULT] : SUCCESS")
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE")
                                            print("ACTUAL RESULT %d: Failed to decrement the number of port mapping entries by 1 after DeleteObject."%step)
                                            print("[TEST EXECUTION RESULT] : FAILURE")
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE")
                                        print("Value of number of port mapping entries retrieved from ACS server is empty or None after DeleteObect")
                                else:
                                    tdkTestObj.setResultStatus("FAILURE")
                                    print("ACTUAL RESULT %d: DeleteObject Task failed to delete %s with status %d." % (step,name3,status2))
                                    print("[TEST EXECUTION RESULT] : FAILURE")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d:  Failed to increment the number of port mapping entries by 1 after AddObject."%step)
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("Value of number of port mapping entries retrieved from ACS server is empty or None after AddObect")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: AddObject Task failed to add object %s with status %d." % (step,name2,status1))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("Value of number of port mapping entries retrieved from ACS server is empty or None after Factory Reset.")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("tr069pa Pre-requisite failed after factory reset of DUT. Please check if tr069 process is running in device or configuration is proper or connection is established.")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: FactoryReset Task failed to reset the writable tables via ACS with status %d." % (step,status))
            print("[TEST EXECUTION RESULT] : FAILURE")
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

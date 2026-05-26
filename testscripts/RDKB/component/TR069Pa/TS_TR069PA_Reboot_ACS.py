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
tr181obj.configureTestCase(ip,port,'TS_TR069PA_Reboot_ACS')
sysobj.configureTestCase(ip,port,'TS_TR069PA_Reboot_ACS')

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
        queryParam = {"name":""}

        #save device's current state before it goes for reboot
        sysobj.saveCurrentState()

        #Perform Reboot task request to reboot the DUT
        step += 1
        print("\nTEST STEP %d : Send Reboot task request on DUT via ACS." %step)
        print("EXPECTED RESULT %d : Send Reboot task on DUT via ACS successfully." %step)

        status, queryResponse = tr069ACSQuery(username,queryParam,method="Reboot")
        if status == 200 and queryResponse:
            #Restore the device state saved before reboot
            sysobj.restorePreviousStateAfterReboot()
            #Wait upto 5 min to establish connection between DUT and ACS
            print("Sleeping for 300s")
            sleep(300)
            print("The DUT is now up and running.")
            print("ACTUAL RESULT %d: Reboot Task successful via ACS server." %step)
            tdkTestObj.setResultStatus("SUCCESS")
            print("[TEST EXECUTION RESULT] : SUCCESS")

            print("\nChecking PREREQUISITES after Reboot")
            #Check for prerequisites after reboot
            tdkTestObj,username,initialValues,preRequisiteStatus = tr069ACSPreRequisite(tr181obj,sysobj)
            if "SUCCESS" in preRequisiteStatus:
                queryParam = {"name":"Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason"}
                name = queryParam.get("name")
                getValue,step = gettr069ACS(tdkTestObj,username,queryParam,step)

                step += 1
                #Check if DUT is rebooted successfully
                print("\nTEST STEP %d : Check if the DUT is actually rebooted and ACS-DUT connection restored by checking the last reboot reason via ACS." %step)
                print("EXPECTED RESULT %d : Get the last reboot reason as tr069-reboot to confirm the DUT's reboot and connection restored successfully via ACS."%step)
                if getValue and getValue.get(name) == "tr069-reboot":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Got the last reboot reason as %s confirmed the DUT's reboot and ACS-DUT connection restored successfully via ACS." %(step,getValue.get(name)))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Got the last reboot reason as %s, which does not match the expected value 'tr069-reboot' but ACS-DUT connection restored via ACS" %(step,getValue.get(name)))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("tr069pa Pre-requisite failed after reboot of DUT. Please check if tr069 process is running in device or configuration is proper or connection is established.")
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Reboot Task failed to restart the DUT with status %d." % (step,status))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("tr069pa Pre-requisite failed. Please check if tr069 process is running in device or configuration is proper or connection is established.")
        print("[TEST EXECUTION RESULT] : FAILURE")

    revertPrerequisite(tr181obj,initialValues,step)

    tr181obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("FAILURE to load module.")
    tr181obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")

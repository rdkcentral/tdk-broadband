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

# use tdklib library, which provides a wrapper for tdk testcase script
import tdklib
from RNDISVariables import *
from RNDISUtility import *
from tdkutility import *

# Test components to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")

# IP and Port of box, No need to change
# This will be replaced with corresponding DUT IP and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_RNDIS_VerifyHostTableUpdateWithWiFiClient_iPhoneUSB')
obj.configureTestCase(ip,port,'TS_RNDIS_VerifyHostTableUpdateWithWiFiClient_iPhoneUSB')

# Get the result of connection with test components and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus = obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus_sys.upper() and "SUCCESS" in loadmodulestatus.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    proceed_flag = 1
    step = 1

    # Get the WAN MAC data model value
    print("\nTEST STEP %d: Get the data model parameter %s" %(step,DM_WAN_MAC))
    print("EXPECTED RESULT %d: Should successfully retrieve the DM WAN MAC value" %step)
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    actualresult,details = getTR181Value(tdkTestObj,DM_WAN_MAC)

    if expectedresult in actualresult and details.strip() != "":
        dm_wan_mac = details.strip().replace("\\n","")
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: DM WAN MAC is %s" %(step,dm_wan_mac))
        print("[TEST EXECUTION RESULT] : SUCCESS")
    else:
        proceed_flag = 0
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to retrieve the DM WAN MAC value. Details: %s" %(step,details))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Verify the target iPhone WAN interface has an active IP address
    if proceed_flag == 1:
        step += 1
        print("\nTEST STEP %d: Verify the target WAN interface %s has an active IP address" %(step,IOS_WAN_INTERFACE))
        print("EXPECTED RESULT %d: Interface %s should have an active IP address" %(step,IOS_WAN_INTERFACE))
        tdkTestObj,actualresult,details = get_target_wan_interface(sysobj,IOS_WAN_INTERFACE)
        details = details.strip().replace("\\n","")

        if expectedresult in actualresult and details != "":
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: WAN interface %s has an active IP address: %s" %(step,IOS_WAN_INTERFACE,details))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            proceed_flag = 0
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to verify that WAN interface %s has an active IP address. Details: %s" %(step,IOS_WAN_INTERFACE,details))
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Get the number of Host entries
    if proceed_flag == 1:
        step += 1
        print("\nTEST STEP %d: Get the number of Host entries" %step)
        print("EXPECTED RESULT %d: Should successfully retrieve Device.Hosts.HostNumberOfEntries" %step)
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
        actualresult,details = getTR181Value(tdkTestObj,DM_HOSTS_HOST_NUMBER_OF_ENTRIES)
        hostEntriesOutput = details.strip().replace("\\n","")

        if expectedresult in actualresult and hostEntriesOutput.isdigit():
            hostEntries = int(hostEntriesOutput)
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: HostNumberOfEntries is %d" %(step,hostEntries))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            proceed_flag = 0
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to retrieve a valid HostNumberOfEntries value. Details: %s" %(step,details))
            print("[TEST EXECUTION RESULT] : FAILURE")

    # Iterate through the Host table and find an active WiFi client
    if proceed_flag == 1:
        clientDetected = False
        clientIndex = None
        clientLayer1Interface = ""

        for hostIndex in range(1,hostEntries + 1):
            step += 1
            layer1Param = "Device.Hosts.Host.%d.Layer1Interface" %hostIndex
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
            actualresult,layer1Interface = getTR181Value(tdkTestObj,layer1Param)
            layer1Interface = layer1Interface.strip().replace("\\n","")

            print("\nTEST STEP %d: Get %s and check whether it contains a WiFi SSID interface path" %(step,layer1Param))
            print("EXPECTED RESULT %d: The Layer1Interface value should be retrieved successfully" %step)

            if expectedresult in actualresult and layer1Interface != "":
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: %s is %s" %(step,layer1Param,layer1Interface))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                if "Device.WiFi.SSID." in layer1Interface:
                    step += 1
                    activeParam = "Device.Hosts.Host.%d.Active" %hostIndex
                    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                    actualresult,activeStatus = getTR181Value(tdkTestObj,activeParam)
                    activeStatus = activeStatus.strip().replace("\\n","")

                    print("\nTEST STEP %d: Get the Active status of the WiFi client at Host.%d" %(step,hostIndex))
                    print("EXPECTED RESULT %d: %s should be true" %(step,activeParam))

                    if expectedresult in actualresult and activeStatus == "true":
                        clientDetected = True
                        clientIndex = hostIndex
                        clientLayer1Interface = layer1Interface
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Active WiFi client found at Host.%d with Layer1Interface %s" %(step,hostIndex,layer1Interface))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                        break
                    elif expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: WiFi client at Host.%d is not active. Active status is %s" %(step,hostIndex,activeStatus))
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Failed to get the Active status for Host.%d. Details: %s" %(step,hostIndex,activeStatus))
                        print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to get a valid value for %s. Details: %s" %(step,layer1Param,layer1Interface))
                print("[TEST EXECUTION RESULT] : FAILURE")

        # Check whether an active WiFi client was found
        step += 1
        print("\nTEST STEP %d: Check whether an active WiFi client is present in the Host table" %step)
        print("EXPECTED RESULT %d: At least one active WiFi client should be present in the Host table" %step)

        if clientDetected:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Active WiFi client found at Host.%d with Layer1Interface %s" %(step,clientIndex,clientLayer1Interface))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: No active WiFi client was found in the Host table" %step)
            print("[TEST EXECUTION RESULT] : FAILURE")

    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load sysutil or tdkbtr181 module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")

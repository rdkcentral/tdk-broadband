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
import tdklib
from tdkutility import *

# Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckTelemetryProcessAfterDisable')
sysobj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckTelemetryProcessAfterDisable')
# Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus_sys.upper():
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1
    #Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable
    print("\nTEST STEP %d: Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable" %step)
    print("EXPECTED RESULT %d: Should get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable successfully" %step)

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    actualresult, initial_telemetry_enable = getTR181Value(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable")

    if expectedresult in actualresult and initial_telemetry_enable != "":
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Successfully got the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable. Details : %s" %(step, initial_telemetry_enable))
        print("[TEST EXECUTION RESULT] : SUCCESS")

        step += 1
        # Set Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to false
        print("\nTEST STEP %d: Set the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to false" %step)
        print("EXPECTED RESULT %d: Should set the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to false successfully" %step)

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
        actualresult, details = setTR181Value(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable", "false", "boolean")

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Successfully set the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to false" %step)
            print("[TEST EXECUTION RESULT] : SUCCESS")

            #Reboot the device to get the changes applied and check whether the DUT is up
            step += 1
            print("\nTEST STEP %d: Reboot the device to apply changes" %step)
            print("EXPECTED RESULT %d: Device should reboot successfully" %step)

            print("****DUT is going for a reboot and will be up after 300 seconds*****")
            obj.initiateReboot()
            sleep(300)
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
            actualresult, uptime = getTR181Value(tdkTestObj, "Device.DeviceInfo.UpTime")
            if expectedresult in actualresult and int(uptime) > 0:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: Device rebooted successfully. Uptime after reboot is : %s" %(step, uptime))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                #Check if Telemetry2.0 process is down
                print("\nTEST STEP %d: Check whether the Telemetry2.0 process state is down after reboot" %step)
                print("EXPECTED RESULT %d: Telemetry2.0 process state after reboot should be down" %step)

                tdkTestObj = sysobj.createTestStep('ExecuteCmd')

                actualresult,details = getPID(tdkTestObj, 'telemetry2_0')

                if expectedresult in actualresult and details == "":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Telemetry2.0 process is down after setting Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to false. Details : %s" %(step, details))
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    # Reverting Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to initial value
                    step += 1
                    print("\nTEST STEP %d: Revert the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to initial value" %step)
                    print("EXPECTED RESULT %d: Should set the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to initial value successfully" %step)

                    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
                    actualresult, details = setTR181Value(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable", initial_telemetry_enable, "boolean")

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Successfully set the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to %s" % (step, initial_telemetry_enable))
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        #Reboot the device to get the changes applied
                        step += 1
                        print("\nTEST STEP %d: Reboot the device" %step)
                        print("EXPECTED RESULT %d: Device should reboot successfully" %step)
                        print("****DUT is going for a reboot and will be up after 300 seconds*****")
                        obj.initiateReboot()
                        sleep(300)
                        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
                        actualresult, uptime = getTR181Value(tdkTestObj, "Device.DeviceInfo.UpTime")
                        if expectedresult in actualresult and int(uptime) > 0:
                            tdkTestObj.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: Device is up after reboot. Uptime : %s" %(step, uptime))
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                            #Check the Telemetry2.0 process state
                            step += 1
                            print("\nTEST STEP %d: Check whether the Telemetry2.0 process state is up after restart" %step)
                            print("EXPECTED RESULT %d: Telemetry2.0 process state after restart should be up" %step)
                            tdkTestObj = sysobj.createTestStep('ExecuteCmd')
                            actualresult,details = getPID(tdkTestObj, 'telemetry2_0')
                            if expectedresult in actualresult and details != "":
                                tdkTestObj.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: Telemetry2.0 process is running after reverting Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to %s. Details : %s" %(step, initial_telemetry_enable,details))
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: Telemetry2.0 process is down. Details : %s" %(step, details))
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: Failed to reboot the device" %step)
                            print("[TEST EXECUTION RESULT] : FAILURE")

                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Failed to set the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to initial value. Details : %s" %(step, details))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Telemetry2.0 process is running. Details : %s" %(step, details))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to reboot the device. Details : %s" %(step, uptime))
                print("[TEST EXECUTION RESULT] : FAILURE")

        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Failed to set the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to false" %step)
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Failed to get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable. Details : %s" %(step, details))
        print("[TEST EXECUTION RESULT] : FAILURE")
    print("\n")
    #Unload the modules loaded
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")


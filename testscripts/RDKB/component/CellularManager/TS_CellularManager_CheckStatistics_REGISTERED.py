##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2024 RDK Management
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
from time import sleep

# Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")

# IP and Port of box, No need to change,
# This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_CellularManager_CheckStatistics_REGISTERED')
sysobj.configureTestCase(ip,port,'TS_CellularManager_CheckStatistics_REGISTERED')

# Load modules
loadmodulestatus = obj.getLoadModuleResult()
loadmodulestatus_sys = sysobj.getLoadModuleResult()

print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus)
print("[LIB LOAD STATUS]  :  %s" % loadmodulestatus_sys)

print("Loading sysutil and tdkb-tr181 modules")

if "SUCCESS" in loadmodulestatus.upper() and \
   "SUCCESS" in loadmodulestatus_sys.upper():

    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    expectedresult = "SUCCESS"
    enableModified = False
    step = 1

    ############################################################
    # STEP 1 : Get Interface Enable State
    ############################################################

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.Interface.1.Enable"
    )

    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    initialEnable = tdkTestObj.getResultDetails().strip()

    print("TEST STEP %d: Get Device.Cellular.Interface.1.Enable" % step)
    print("EXPECTED RESULT %d: Should get Device.Cellular.Interface.1.Enable value" % step)
    print("ACTUAL RESULT %d: Device.Cellular.Interface.1.Enable is %s" %
          (step, initialEnable))

    if expectedresult in actualresult and initialEnable in ["true", "false"]:

        tdkTestObj.setResultStatus("SUCCESS")
        print("[TEST EXECUTION RESULT] : SUCCESS")

    else:

        tdkTestObj.setResultStatus("FAILURE")
        print("[TEST EXECUTION RESULT] : FAILURE")

        obj.unloadModule("tdkbtr181")
        sysobj.unloadModule("sysutil")
        exit()

    ############################################################
    # STEP 2 : Enable Interface If Required
    ############################################################

    step += 1

    if initialEnable == "false":

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.Enable"
        )
        tdkTestObj.addParameter(
            "ParamValue",
            "true"
        )
        tdkTestObj.addParameter(
            "Type",
            "bool"
        )

        tdkTestObj.executeTestCase(expectedresult)

        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Set Device.Cellular.Interface.1.Enable to true" % step)
        print("EXPECTED RESULT %d: Device.Cellular.Interface.1.Enable should be set to true" % step)
        print("ACTUAL RESULT %d: %s" % (step, details))

        if expectedresult in actualresult:

            enableModified = True
            tdkTestObj.setResultStatus("SUCCESS")
            print("[TEST EXECUTION RESULT] : SUCCESS")

            sleep(10)

        else:

            tdkTestObj.setResultStatus("FAILURE")
            print("[TEST EXECUTION RESULT] : FAILURE")

    else:

        print("TEST STEP %d: Cellular interface already enabled" % step)
        print("EXPECTED RESULT %d: No configuration change required" % step)
        print("ACTUAL RESULT %d: Device.Cellular.Interface.1.Enable is already true" % step)
        print("[TEST EXECUTION RESULT] : SUCCESS")

    ############################################################
    # STEP 3 : Verify Cellular Status is CONNECTED
    ############################################################

    step += 1

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.X_RDK_Status"
    )

    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    print("TEST STEP %d: Verify Device.Cellular.X_RDK_Status" % step)
    print("EXPECTED RESULT %d: Device.Cellular.X_RDK_Status should be CONNECTED" % step)
    print("ACTUAL RESULT %d: Status is %s" % (step, details))

    if expectedresult in actualresult and details == "CONNECTED":

        tdkTestObj.setResultStatus("SUCCESS")
        print("[TEST EXECUTION RESULT] : SUCCESS")

    else:

        tdkTestObj.setResultStatus("FAILURE")
        print("[TEST EXECUTION RESULT] : FAILURE")

    ############################################################
    # STEP 4 : Power OFF SIM
    ############################################################

    step += 1

    tdkTestObj = sysobj.createTestStep('ExecuteCmd')
    tdkTestObj.addParameter(
        "command",
        "qmicli -p -d /dev/cdc-wdm0 --uim-sim-power-off=1"
    )

    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    print("TEST STEP %d: Power off SIM using qmicli command" % step)
    print("EXPECTED RESULT %d: SIM power off should be successful" % step)
    print("ACTUAL RESULT %d: %s" % (step, details))

    if expectedresult in actualresult and details != "":

        tdkTestObj.setResultStatus("SUCCESS")
        print("[TEST EXECUTION RESULT] : SUCCESS")

    else:

        tdkTestObj.setResultStatus("FAILURE")
        print("[TEST EXECUTION RESULT] : FAILURE")

    ############################################################
    # STEP 5 : Verify Status is DOWN
    ############################################################

    sleep(5)
    step += 1

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.X_RDK_Status"
    )

    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    print("TEST STEP %d: Verify Device.Cellular.X_RDK_Status" % step)
    print("EXPECTED RESULT %d: Device.Cellular.X_RDK_Status should be DOWN" % step)
    print("ACTUAL RESULT %d: Status is %s" % (step, details))

    if expectedresult in actualresult and details == "DOWN":

        tdkTestObj.setResultStatus("SUCCESS")
        print("[TEST EXECUTION RESULT] : SUCCESS")

    else:

        tdkTestObj.setResultStatus("FAILURE")
        print("[TEST EXECUTION RESULT] : FAILURE")

    ############################################################
    # STEP 6 : Power ON SIM
    ############################################################

    step += 1

    tdkTestObj = sysobj.createTestStep('ExecuteCmd')
    tdkTestObj.addParameter(
        "command",
        "qmicli -p -d /dev/cdc-wdm0 --uim-sim-power-on=1"
    )

    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    print("TEST STEP %d: Power on SIM using qmicli command" % step)
    print("EXPECTED RESULT %d: SIM power on should be successful" % step)
    print("ACTUAL RESULT %d: %s" % (step, details))

    if expectedresult in actualresult and details != "":

        tdkTestObj.setResultStatus("SUCCESS")
        print("[TEST EXECUTION RESULT] : SUCCESS")

    else:

        tdkTestObj.setResultStatus("FAILURE")
        print("[TEST EXECUTION RESULT] : FAILURE")

    ############################################################
    # STEP 7 : Verify REGISTERED State
    ############################################################

    step += 1

    print("TEST STEP %d: Verify Device.Cellular.X_RDK_Status becomes REGISTERED or CONNECTED" % step)
    print("EXPECTED RESULT %d: Device.Cellular.X_RDK_Status should become REGISTERED or CONNECTED" % step)

    max_tries = 60
    registered = False

    for attempt in range(max_tries):

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.X_RDK_Status"
        )

        tdkTestObj.executeTestCase(expectedresult)

        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("Attempt %d Status : %s" % (attempt, details))

        if expectedresult in actualresult and details in ["REGISTERED","CONNECTED"]:

            registered = True
            break

        sleep(2)

    if registered:

        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Status is %s" % (step, details))
        print("[TEST EXECUTION RESULT] : SUCCESS")

    else:

        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Status did not become REGISTERED" % step)
        print("[TEST EXECUTION RESULT] : FAILURE")

    ############################################################
    # STEP 8 : Verify BytesSent
    ############################################################

    step += 1

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.Interface.1.X_RDK_Statistics.BytesSent"
    )

    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    print("TEST STEP %d: Get Device.Cellular.Interface.1.X_RDK_Statistics.BytesSent" % step)
    print("EXPECTED RESULT %d: BytesSent should be 0" % step)
    print("ACTUAL RESULT %d: BytesSent is %s" % (step, details))

    if expectedresult in actualresult and details == "0":

        tdkTestObj.setResultStatus("SUCCESS")
        print("[TEST EXECUTION RESULT] : SUCCESS")

    else:

        tdkTestObj.setResultStatus("FAILURE")
        print("[TEST EXECUTION RESULT] : FAILURE")

    ############################################################
    # STEP 9 : Verify BytesReceived
    ############################################################

    step += 1

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get')
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.Interface.1.X_RDK_Statistics.BytesReceived"
    )

    tdkTestObj.executeTestCase(expectedresult)

    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    print("TEST STEP %d: Get Device.Cellular.Interface.1.X_RDK_Statistics.BytesReceived" % step)
    print("EXPECTED RESULT %d: BytesReceived should be 0" % step)
    print("ACTUAL RESULT %d: BytesReceived is %s" % (step, details))

    if expectedresult in actualresult and details == "0":

        tdkTestObj.setResultStatus("SUCCESS")
        print("[TEST EXECUTION RESULT] : SUCCESS")

    else:

        tdkTestObj.setResultStatus("FAILURE")
        print("[TEST EXECUTION RESULT] : FAILURE")

    ############################################################
    # STEP 10 : Revert Enable State
    ############################################################

    if enableModified:

        step += 1

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set')
        tdkTestObj.addParameter(
            "ParamName",
            "Device.Cellular.Interface.1.Enable"
        )
        tdkTestObj.addParameter(
            "ParamValue",
            initialEnable
        )
        tdkTestObj.addParameter(
            "Type",
            "bool"
        )

        tdkTestObj.executeTestCase(expectedresult)

        actualresult = tdkTestObj.getResult()
        details = tdkTestObj.getResultDetails()

        print("TEST STEP %d: Revert Device.Cellular.Interface.1.Enable to original value" % step)
        print("EXPECTED RESULT %d: Device.Cellular.Interface.1.Enable should be restored to %s" %
              (step, initialEnable))
        print("ACTUAL RESULT %d: %s" % (step, details))

        if expectedresult in actualresult:

            tdkTestObj.setResultStatus("SUCCESS")
            print("[TEST EXECUTION RESULT] : SUCCESS")

    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")

else:

    print("Failed to load module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")



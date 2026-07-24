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
import tdklib;
import time;
from time import sleep;

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_CellularManager_X_RDK_EnablePersistenceOnReboot');
obj.configureTestCase(ip,port,'TS_CellularManager_X_RDK_EnablePersistenceOnReboot');

#Get the result of connection with test component and DUT
loadmodulestatus_sys =sysobj.getLoadModuleResult();
loadmodulestatus =obj.getLoadModuleResult();
print ("[LIB LOAD STATUS]  :  %s" %loadmodulestatus_sys);
print ("[LIB LOAD STATUS]  :  %s" %loadmodulestatus);

print("Loading Cellular Manager module")
if "SUCCESS" in loadmodulestatus.upper() and loadmodulestatus_sys.upper():
    sysobj.setLoadModuleStatus("SUCCESS");
    obj.setLoadModuleStatus("SUCCESS");

    step = 1;

############################################################
# STEP 1 : Verify Device.Cellular.Interface.1.Enable
############################################################

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.Interface.1.Enable"
    );

    expectedresult = "SUCCESS";

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    interfaceEnable = tdkTestObj.getResultDetails().strip();

    print("TEST STEP %d: Get Device.Cellular.Interface.1.Enable" %step);
    print("EXPECTED RESULT %d: Device.Cellular.Interface.1.Enable should be true" %step);
    print("ACTUAL RESULT %d: Value is %s" %(step,interfaceEnable));

    if expectedresult in actualresult and interfaceEnable == "true":

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    step = step + 1;

############################################################
# STEP 2 : Verify Device.Cellular.X_RDK_Status
############################################################

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter(
        "ParamName",
        "Device.Cellular.X_RDK_Status"
    );

    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    status = tdkTestObj.getResultDetails();

    print("TEST STEP %d: Verify Device.Cellular.X_RDK_Status" %step);
    print("EXPECTED RESULT %d: Device.Cellular.X_RDK_Status should be CONNECTED" %step);
    print("ACTUAL RESULT %d: Status is %s" %(step,status));

    if expectedresult in actualresult and status == "CONNECTED":

        tdkTestObj.setResultStatus("SUCCESS");
        print("[TEST EXECUTION RESULT] : SUCCESS");

    else:

        tdkTestObj.setResultStatus("FAILURE");
        print("[TEST EXECUTION RESULT] : FAILURE");

    step = step + 1;

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.Cellular.X_RDK_Enable");
    expectedresult="SUCCESS";

    #Execute testcase in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    initialvalue = tdkTestObj.getResultDetails();
    print("TEST STEP %d: Get the Device.Cellular.X_RDK_Enable" %step);
    print("EXPECTED RESULT %d: Should get the Device.Cellular.X_RDK_Enable" %step);
    print("ACTUAL RESULT %d: Value is %s" %(step,initialvalue));

    if expectedresult in actualresult and initialvalue != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : SUCCESS");


        step = step + 1;
        setVal = "false";
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
        tdkTestObj.addParameter("ParamName","Device.Cellular.X_RDK_Enable");
        tdkTestObj.addParameter("ParamValue",setVal);
        tdkTestObj.addParameter("Type","bool");
        expectedresult="SUCCESS";

        #Execute testcase in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        setvalue = tdkTestObj.getResultDetails();

        print("TEST STEP %d: Set the Device.Cellular.X_RDK_Enable" %step);
        print("EXPECTED RESULT %d: Should set the Device.Cellular.X_RDK_Enable as %s" %(step,setVal));
        print("ACTUAL RESULT %d: Value is %s" %(step,setvalue));

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : SUCCESS");

            #rebooting the device
            sysobj.initiateReboot();
            sleep(60);

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter("ParamName","Device.Cellular.X_RDK_Enable");
            expectedresult="SUCCESS";

            step = step + 1;
            #Execute testcase in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            newvalue = tdkTestObj.getResultDetails();
            print("TEST STEP %d: Get the Device.Cellular.X_RDK_Enable after Reboot" %step);
            print("EXPECTED RESULT %d:  Should get the  Device.Cellular.X_RDK_Enable value " %step);
            print("ACTUAL RESULT %d: Value is %s" %(step,newvalue));

            if expectedresult in actualresult and newvalue != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS");

                print("TEST STEP %d: Check persistence of Device.Cellular.X_RDK_Enable value after Reboot"%step);
                print("EXPECTED RESULT %d:  The value of Device.Cellular.X_RDK_Enable should persist after reboot"%step);
                print("ACTUAL RESULT %d: Value is %s" %(step,newvalue));

                #Check if the value persists after reboot
                if newvalue == setvalue :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : SUCCESS");
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : FAILURE");
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE");
            #Reverting the value of Device.Cellular.X_RDK_Enable to initial one
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.Cellular.X_RDK_Enable");
            tdkTestObj.addParameter("ParamValue",initialvalue);
            tdkTestObj.addParameter("Type","bool");
            expectedresult="SUCCESS";

            #Execute testcase in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            setvalue = tdkTestObj.getResultDetails();
            print("Reverted the value of Device.Cellular.X_RDK_Enable to initial value");

        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : FAILURE");
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : FAILURE");
    obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print("Failed to load module");
    sysobj.setLoadModuleStatus("FAILURE");
    obj.setLoadModuleStatus("FAILURE");

##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("lmlite","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_LMLite_NWDeviceStatus_GetPollingPeriodAfterOverrideTTL');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus) ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('LMLiteStub_Get');

    tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    reportingPeriod = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print("\nTEST STEP 1: Get the current reportingPeriod of NetworkDevicesStatus");
        print("EXPECTED RESULT 1: Should get the current reportingPeriod of NetworkDevicesStatus");
        print("ACTUAL RESULT 1: %s" %reportingPeriod);
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : SUCCESS");

        tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Default.PollingPeriod");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        default_polling = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print("\nTEST STEP 1: Get default PollingPeriod of NetworkDevicesStatus");
            print("EXPECTED RESULT 1: Should get default  PollingPeriod of NetworkDevicesStatus");
            print("ACTUAL RESULT 1: %s" %default_polling);
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : SUCCESS");

            tdkTestObj = obj.createTestStep('LMLiteStub_Get');
            tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Default.OverrideTTL");
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            override=int(details);

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print("\nTEST STEP 2: Get the OverrideTTL of NetworkDevicesStatus");
                print("EXPECTED RESULT 2: Should get OverrideTTL for NetworkDevicesStatus");
                print("ACTUAL RESULT 2: OverrideTTL of NetworkDevicesStatus :%s" %details);
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS");

                tdkTestObj = obj.createTestStep('LMLiteStub_Get');
                tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled");
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                status = tdkTestObj.getResultDetails();
                if expectedresult in (actualresult):
                #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("\nTEST STEP 3 : Get the status of the NetworkDevices");
                    print("EXPECTED RESULT 3 : Should get the  status of the NetworkDevices");
                    print("ACTUAL RESULT 3 : status is %s" %status);
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : SUCCESS");

                    tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod");
                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    Polling_Time = tdkTestObj.getResultDetails();
                    if expectedresult in (actualresult):
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print("\nTEST STEP 4: Get the current Polling period of NetworkDevicesStatus");
                        print("EXPECTED RESULT 4: Should get current Polling period of NetworkDevicesStatus");
                        print("ACTUAL RESULT 4: current Polling period of NetworkDevicesStatus are : %s" %Polling_Time);
                        #Get the result of execution
                        print("[TEST EXECUTION RESULT] : SUCCESS");

                        #check if current polling period is default polling period or not
                        if int(Polling_Time) == int(default_polling):

                            #set the NetworkDevice status as disabled to set a higher polling time
                            tdkTestObj = obj.createTestStep('LMLiteStub_Set');
                            tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled");
                            tdkTestObj.addParameter("ParamValue","false");
                            tdkTestObj.addParameter("Type","bool");

                            #Execute the test case in DUT
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();
                            if expectedresult in actualresult:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print("\nTEST STEP 5: Set the status of the NetworkDevices as disabled");
                                print("EXPECTED RESULT 5: Should disable NetworkDevices");
                                print("ACTUAL RESULT 5:  %s" %details);
                                #Get the result of execution
                                print("[TEST EXECUTION RESULT] : SUCCESS");

                                #change the polling period to a different value
                                PollTimeList = {5,10,15,30,60,300,900,1800,3600,10800,21600, 43200,86400};
                                for newPollTime in PollTimeList:
                                    if newPollTime <= int(reportingPeriod):
                                        #newPollTime = temp
                                        break;
                                print("New poll ",newPollTime)
                                print(("Setting new poll time as " + str(newPollTime)))
                                tdkTestObj = obj.createTestStep('LMLiteStub_Set');
                                tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod");
                                #tdkTestObj.addParameter("ParamValue","300");
                                tdkTestObj.addParameter("ParamValue",  str(newPollTime));
                                tdkTestObj.addParameter("Type","unsignedint");

                                #Execute the test case in DUT
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails();
                                if expectedresult in actualresult:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print("\nTEST STEP 6: Change the polling period to a different value");
                                    print("EXPECTED RESULT 6: Should change the polling period");
                                    print("ACTUAL RESULT 6:  %s" %details);
                                    #Get the result of execution
                                    print("[TEST EXECUTION RESULT] : SUCCESS");
                                else:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print("\nTEST STEP 6: Change the polling period to a different value");
                                    print("EXPECTED RESULT 6: Should change the polling period");
                                    print("ACTUAL RESULT 6:  %s" %details);
                                    #Get the result of execution
                                    print("[TEST EXECUTION RESULT] : FAILURE");
                                    obj.unloadModule("lmlite");
                                    exit();
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print("\nTEST STEP 5: Set the status of the NetworkDevices as disabled");
                                print("EXPECTED RESULT 5: Should disable NetworkDevices");
                                print("ACTUAL RESULT 5:  %s" %details);
                                #Get the result of execution
                                print("[TEST EXECUTION RESULT] : FAILURE");
                                obj.unloadModule("lmlite");
                                exit();
                        else:
                            print("Polling period is already different from default polling time")

                        tdkTestObj = obj.createTestStep('LMLiteStub_Set');
                        tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled");
                        tdkTestObj.addParameter("ParamValue","true");
                        tdkTestObj.addParameter("Type","bool");
                        expectedresult="SUCCESS";

                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print("\nTEST STEP : Enabling the NetworkDevices");
                            print("EXPECTED RESULT : Should enable the NetworkDevices");
                            print("ACTUAL RESULT : %s" %details);
                            #Get the result of execution
                            print("[TEST EXECUTION RESULT] : SUCCESS");

                            ##sleep till override time or reportingPeriod, whichever is greater and check if polling period changes back to its default value
                            if int(override) > int(reportingPeriod):
                                print("Sleeping for ",override)
                                time.sleep(override + 10);
                            else:
                                print("Sleeping for ",reportingPeriod)
                                time.sleep(int(reportingPeriod) + 10)

                            tdkTestObj = obj.createTestStep('LMLiteStub_Get');
                            tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod");
                            expectedresult="SUCCESS";

                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();

                            if expectedresult in actualresult and int(details)==int(default_polling):
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print("\nTEST STEP : Get PollingPeriod as default value");
                                print("EXPECTED RESULT : Should get PollingPeriod as default value after the override TTL period expired");
                                print("ACTUAL RESULT : %s" %details);
                                #Get the result of execution
                                print("[TEST EXECUTION RESULT] : SUCCESS");

                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print("\nTEST STEP : Get PollingPeriod as default value");
                                print("EXPECTED RESULT : Should get PollingPeriod as default value after the override TTL period expired");
                                print("ACTUAL RESULT : %s" %details);
                                #Get the result of execution
                                print("[TEST EXECUTION RESULT] : FAILURE");
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print("\nTEST STEP : Enabling the NetworkDevices");
                            print("EXPECTED RESULT : Should enable the NetworkDevices");
                            print("ACTUAL RESULT : %s" %details);
                            #Get the result of execution
                            print("[TEST EXECUTION RESULT] : FAILURE");
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print("\nTEST STEP 4: Get the current Polling period of NetworkDevicesStatus");
                        print("EXPECTED RESULT 4: Should get current Polling period of NetworkDevicesStatus");
                        print("ACTUAL RESULT 4: current Polling period of NetworkDevicesStatus are : %s" %Polling_Time);
                        #Get the result of execution
                        print("[TEST EXECUTION RESULT] : FAILURE");
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print("\nTEST STEP 3 : Get the status of the NetworkDevices");
                    print("EXPECTED RESULT 3 : Should get the  status of the NetworkDevices");
                    print("ACTUAL RESULT 3 : status is %s" %status);
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : FAILURE");
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print("\nTEST STEP 2: Get the OverrideTTL of NetworkDevicesStatus");
                print("EXPECTED RESULT 2: Should get OverrideTTL for NetworkDevicesStatus");
                print("ACTUAL RESULT 2: OverrideTTL of NetworkDevicesStatus :%s" %details);
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE");

            #set default value to polling period
            tdkTestObj = obj.createTestStep('LMLiteStub_Set');
            tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod");
            tdkTestObj.addParameter("ParamValue",Polling_Time);
            tdkTestObj.addParameter("Type","unsignedint");
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print("\nTEST STEP : Set PollingPeriod to default value");
                print("EXPECTED RESULT : Should set PollingPeriod to default value");
                print("ACTUAL RESULT : %s" %details);
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS");

            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print("\nTEST STEP : Set PollingPeriod to default value");
                print("EXPECTED RESULT : Should set PollingPeriod to default value");
                print("ACTUAL RESULT : %s" %details);
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE");

            #set default value to NetworkDevices status
            tdkTestObj = obj.createTestStep('LMLiteStub_Set');
            tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled");
            tdkTestObj.addParameter("ParamValue",status);
            tdkTestObj.addParameter("Type","bool");
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print("\nTEST STEP : Set NetworkDevices to default value");
                print("EXPECTED RESULT : Should set NetworkDevices to default value");
                print("ACTUAL RESULT : %s" %details);
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS");

            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print("\nTEST STEP : Set NetworkDevices to default value");
                print("EXPECTED RESULT : Should set NetworkDevices to default value");
                print("ACTUAL RESULT : %s" %details);
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE");

        else:
             #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print("\nTEST STEP 1: Get PollingPeriod of NetworkDevicesStatus");
            print("EXPECTED RESULT 1: Should get the Polling period of NetworkDevicesStatus");
            print("ACTUAL RESULT 1: %s" %default_polling);
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : FAILURE");
        obj.unloadModule("lmlite");

else:
    print("Failed to load lmlite module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");

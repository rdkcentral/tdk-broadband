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
obj.configureTestCase(ip,port,'TS_LMLite_NWDeviceStatus_GetReportingPeriodAfterOverrideTTL');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus) ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('LMLiteStub_Get');
    tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Default.ReportingPeriod");
    expectedresult="SUCCESS";

    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    default_reporting = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print("\nTEST STEP 1: Get default ReportingPeriod of NetworkDeviceStatus");
        print("EXPECTED RESULT 1: Should get the default ReportingPeriod of NetworkDevicesStatus");
        print("ACTUAL RESULT 1: %s" %default_reporting);
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

                tdkTestObj = obj.createTestStep('LMLiteStub_Get');
                tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod");
                expectedresult="SUCCESS";
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult1 = tdkTestObj.getResult();
                Reporting_Time = tdkTestObj.getResultDetails();
                RP = Reporting_Time

                tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod");
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult2 = tdkTestObj.getResult();
                Polling_Time = tdkTestObj.getResultDetails();

                if expectedresult in (actualresult1 and actualresult2):
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("\nTEST STEP 4: Get the current Reporting period and Polling period of NetworkDevicesStatus");
                    print("EXPECTED RESULT 4: Should get current Reporting period and Polling period of NetworkDevicesStatus");
                    print("ACTUAL RESULT 4: current Reporting period and Polling period of NetworkDevicesStatus are : %s and %s" %(Reporting_Time,Polling_Time));
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : SUCCESS");

                    Reporting_List=[5,10,15,30,60,300,900,1800,3600,10800,21600,43200,86400];
                    Min_Poll_Time = Reporting_List[0];
                    Max_Poll_Time = Reporting_List[-1];
                    Previous_item =  Reporting_List[(Reporting_List.index(int(Reporting_Time)) - 1) % len(Reporting_List)];
                    Next_item =  Reporting_List[(Reporting_List.index(int(Reporting_Time)) - 1) % len(Reporting_List)];
                    items= [Previous_item,Next_item];
                    if int(Polling_Time) == int(Reporting_Time) or int(Polling_Time) == Max_Poll_Time or int(Polling_Time) in items:
                        tdkTestObj = obj.createTestStep('LMLiteStub_Set');
                        tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod");
                        tdkTestObj.addParameter("ParamValue",str(Min_Poll_Time));
                        tdkTestObj.addParameter("Type","unsignedint");

                        expectedresult="SUCCESS";
                        #Execute the test case in DUT
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print("\nTEST STEP : Set the Polling period to lower value");
                            print("EXPECTED RESULT : Should set the Polling period to lower value if it is the max value or equal to current reporting period");
                            print("ACTUAL RESULT : %s" %details);
                            #Get the result of execution
                            print("[TEST EXECUTION RESULT] : SUCCESS");
                            Polling_Time = "30";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print("\nTEST STEP : Set the Polling period to lower value");
                            print("EXPECTED RESULT : Should set the Polling period to lower value if it is the max value or equal to current reporting period");
                            print("ACTUAL RESULT : %s" %details);
                            #Get the result of execution
                            print("[TEST EXECUTION RESULT] : FAILURE");
                            obj.unloadModule("lmlite");
                            exit();

                    if int(Reporting_Time) == int(default_reporting):
                        for i in range(0,len(Reporting_List)):
                            RP = Reporting_List[i];
                            if ((RP < int(Reporting_Time)) and (RP > int(Polling_Time))):
                                print(RP);
                                break;
                        tdkTestObj = obj.createTestStep('LMLiteStub_Set');
                        tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod");
                        tdkTestObj.addParameter("ParamValue",str(RP));
                        tdkTestObj.addParameter("Type","unsignedint");
                        expectedresult="SUCCESS";
                        #Execute the test case in DUT
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print("\nTEST STEP 5: Set ReportingPeriod to a  valid value");
                            print("EXPECTED RESULT 5: Should set ReportingPeriod to a valid value");
                            print("ACTUAL RESULT 5: %s" %details);
                            #Get the result of execution
                            print("[TEST EXECUTION RESULT] : SUCCESS");
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print("\nTEST STEP 5: Set ReportingPeriod to a  valid value");
                            print("EXPECTED RESULT 5: Should set ReportingPeriod to a valid value");
                            print("ACTUAL RESULT 5: %s" %details);
                            #Get the result of execution
                            print("[TEST EXECUTION RESULT] : FAILURE");
                            obj.unloadModule("lmlite");
                            exit();
                    else:
                        print("Current reporting period is already different from default reporting period")

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

                        ##sleep till override time or reportingPeriod, whichever is greater and check if polling period changes back to its default value^M
                        if int(override) > int(RP):
                            print("Sleeping for ",override)
                            time.sleep(override + 10);
                        else:
                            print("Sleeping for ",RP)
                            time.sleep(int(RP) + 10)

                        tdkTestObj = obj.createTestStep('LMLiteStub_Get');
                        tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod");
                        expectedresult="SUCCESS";
                        #Execute the test case in DUT
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult and int(details)==int(default_reporting):
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print("\nTEST STEP 6: Get ReportingPeriod as default value");
                            print("EXPECTED RESULT 6: Should get ReportingPeriod as default value after the override TTL period expired");
                            print("ACTUAL RESULT 6: %s" %details);
                            #Get the result of execution
                            print("[TEST EXECUTION RESULT] : SUCCESS");

                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print("\nTEST STEP 6: Get ReportingPeriod as default value");
                            print("EXPECTED RESULT 6: Should get ReportingPeriod as default value after the override TTL period expired");
                            print("ACTUAL RESULT 6: %s" %details);
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
                    print("\nTEST STEP 4: Get the current Reporting period and Polling period of NetworkDevicesStatus");
                    print("EXPECTED RESULT 4: Should get current Reporting period and Polling period of NetworkDevicesStatus");
                    print("ACTUAL RESULT 4: current Reporting period and Polling period of NetworkDevicesStatus are : %s and %s" %(Reporting_Time,Polling_Time));
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

        #Set default values
        tdkTestObj = obj.createTestStep('LMLiteStub_Set');
        tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod");
        tdkTestObj.addParameter("ParamValue",Reporting_Time);
        tdkTestObj.addParameter("Type","unsignedint");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult1 = tdkTestObj.getResult();

        tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod");
        tdkTestObj.addParameter("ParamValue",Polling_Time);
        tdkTestObj.addParameter("Type","unsignedint");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult2 = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in (actualresult1 and actualresult2):
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print("\nTEST STEP : Set ReportingPeriod and polling period to default value");
            print("EXPECTED RESULT : Should set ReportingPeriod and Polling Periodto default value");
            print("ACTUAL RESULT : %s" %details);
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : SUCCESS");

        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print("\nTEST STEP : Set ReportingPeriod and polling period to default value");
            print("EXPECTED RESULT : Should set ReportingPeriod and polling period to default value");
            print("ACTUAL RESULT : %s" %details);
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : FAILURE");
        #set default value to NetworkDevices
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
        print("\nTEST STEP 1: Get default ReportingPeriod of NetworkDeviceStatus");
        print("EXPECTED RESULT 1: Should get the default ReportingPeriod of NetworkDevicesStatus");
        print("ACTUAL RESULT 1: %s" %default_reporting);
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : FAILURE");

    obj.unloadModule("lmlite");

else:
    print("Failed to load lmlite module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");

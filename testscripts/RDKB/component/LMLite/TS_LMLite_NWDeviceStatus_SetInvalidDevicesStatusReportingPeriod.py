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

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("lmlite","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_LMLite_NWDeviceStatus_SetInvalidDevicesStatusReportingPeriod');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus) ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('LMLiteStub_Get');
    tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod");
    expectedresult="SUCCESS";

    PollingPeriod_list={'5','10','15','30','60','300','900','1800','3600','10800','21600','43200','86400'};

    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details_reporting = tdkTestObj.getResultDetails();

    if expectedresult in actualresult and details_reporting in PollingPeriod_list:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print("\nTEST STEP 1: Get the ReportingPeriod of NetworkDevicesStatus");
        print("EXPECTED RESULT 1: Should get a valid ReportingPeriod for NetworkDevicesStatus");
        print("ACTUAL RESULT 1: ReportingPeriod of NetworkDevicesStatus :%s" %details_reporting);
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : SUCCESS");
        tdkTestObj = obj.createTestStep('LMLiteStub_Set');
        tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod");
        tdkTestObj.addParameter("ParamValue","100");
        tdkTestObj.addParameter("Type","unsignedint");
        expectedresult="FAILURE";

        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print("\nTEST STEP 2: Set an invalid ReportingPeriod of NetworkDevicesStatus");
            print("EXPECTED RESULT 2: Should not set an invalid ReportingPeriod for NetworkDevicesStatus");
            print("ACTUAL RESULT 2: %s" %details);
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : SUCCESS");
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print("\nTEST STEP 2: Set an invalid ReportingPeriod of NetworkDevicesStatus");
            print("EXPECTED RESULT 2: Should not set an invalid ReportingPeriod for NetworkDevicesStatus");
            print("ACTUAL RESULT 2: %s" %details);
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : FAILURE");

        tdkTestObj = obj.createTestStep('LMLiteStub_Set');
        tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod");
        tdkTestObj.addParameter("ParamValue",details_reporting);
        tdkTestObj.addParameter("Type","unsignedint");
        expectedresult="SUCCESS";

        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print("\nTEST STEP 3: Set the ReportingPeriod of NetworkDevicesStatus to default value");
            print("EXPECTED RESULT 3: Should Set  ReportingPeriod for NetworkDevicesStatus to default value");
            print("ACTUAL RESULT 3: ReportingPeriod of NetworkDevicesStatus :%s" %details);
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : SUCCESS");

        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print("\nTEST STEP 3: Set the ReportingPeriod of NetworkDevicesStatus to default value");
            print("EXPECTED RESULT 3: Should Set  ReportingPeriod for NetworkDevicesStatus to default value");
            print("ACTUAL RESULT 3: ReportingPeriod of NetworkDevicesStatus :%s" %details);
            #Get the result of execution
            print("[TEST EXECUTION RESULT] : FAILURE");

    else:
        tdkTestObj.setResultStatus("FAILURE");
        print("\nTEST STEP 1: Get the ReportingPeriod of NetworkDevicesStatus");
        print("EXPECTED RESULT 1: Should get a valid ReportingPeriod for NetworkDevicesStatus");
        print("ACTUAL RESULT 1: ReportingPeriod of NetworkDevicesStatus :%s" %details_reporting);
        print("[TEST EXECUTION RESULT] : FAILURE");
    obj.unloadModule("lmlite");

else:
    print("Failed to load lmlite module");
    obj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");

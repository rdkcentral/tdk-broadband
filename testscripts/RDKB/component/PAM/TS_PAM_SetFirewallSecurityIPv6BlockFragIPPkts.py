##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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

import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");
sysobj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_SetFirewallSecurityIPv6BlockFragIPPkts');
sysobj.configureTestCase(ip,port,'TS_PAM_SetFirewallSecurityIPv6BlockFragIPPkts');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysutilloadmodulestatus =sysobj.getLoadModuleResult();
print("[LIB LOAD STATUS]  :  %s" %loadmodulestatus) ;
print("[LIB LOAD STATUS]  :  %s" %sysutilloadmodulestatus) ;

def set_firewall_security_fragIPPkts(tdkTestObj,set_value):
    tdkTestObj.addParameter("ParamName","Device.Firewall.X_RDKCENTRAL-COM_Security.V6.BlockFragIPPkts");
    tdkTestObj.addParameter("ParamValue",set_value);
    tdkTestObj.addParameter("Type","boolean");
    expectedresult="SUCCESS";
    #Execute testcase on DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    result = tdkTestObj.getResultDetails();
    return actualresult, result;

def verify_iptable_rules(tdkTestObj,enabled):
    iptable_list = ["-N FRAG_DROP","-A INPUT -m frag --fragmore -j FRAG_DROP", "-A FORWARD -m frag --fragmore -j FRAG_DROP", "-A FRAG_DROP -j DROP"]
    for list in iptable_list:
        cmd = "ip6tables -S | grep -ire \"%s\"" %list;
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        if enabled == "true":
            if expectedresult in actualresult and details == list:
                rulesFound = 1;
            else:
                rulesFound = 0;
                print("Iptable Rule %s is NOT present"%list)
                break;
        else:
            if expectedresult in actualresult and details == "":
                rulesFound = 0;
            else:
                rulesFound = 1;
                print("Iptable Rule %s is present"%list)
                break;
    return rulesFound;

if "SUCCESS" in (loadmodulestatus.upper() and sysutilloadmodulestatus.upper()):
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    revertFlag = 0;

    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.Firewall.X_RDKCENTRAL-COM_Security.V6.BlockFragIPPkts");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    initial_value = tdkTestObj.getResultDetails().strip();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print("TEST STEP 1: Get current value of IPV6 BlockFragIPPkts")
        print("EXPECTED RESULT 1: Should get current value of  IPV6 BlockFragIPPkts")
        print("ACTUAL RESULT 1: current value is %s" %initial_value);
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : SUCCESS")

        if initial_value == "true":
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            enable_verify = verify_iptable_rules(tdkTestObj,"true");

            if enable_verify == 1:
                tdkTestObj.setResultStatus("SUCCESS");
                print("TEST STEP 2: Verify iptables rules for IPV6 BlockFragIPPkts for True")
                print("EXPECTED RESULT 2: The iptables rules specific to IPV6 BlockFragIPPkts should be present")
                print("ACTUAL TEST 2: Verification on the iptables rules specific to IPV6 BlockFragIPPkts - Enabled is success")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS")

                #set to False
                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                set_disable_res,set_disable_details = set_firewall_security_fragIPPkts (tdkTestObj,"false");
                #wait upto 60 sec to complete firewall restart
                sleep(60);

                if expectedresult in set_disable_res:
                    revertFlag = 1;
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("TEST STEP 3: Set IPV6 BlockFragIPPkts value to False")
                    print("EXPECTED RESULT 3: The Set Operation should be success")
                    print("ACTUAL TEST 3: The set operation to make IPV6 BlockFragIPPkts as False was success")
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    disable_verify = verify_iptable_rules(tdkTestObj,"false");

                    if disable_verify == 0:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print("TEST STEP 4: Verify iptables rules for IPV6 BlockFragIPPkts for False")
                        print("EXPECTED RESULT 4: The iptables rules specific to IPV6 BlockFragIPPkts should not be present")
                        print("ACTUAL TEST 4: Verification on the iptables rules specific to IPV6 BlockFragIPPkts Disabled is success")
                        #Get the result of execution
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print("TEST STEP 4: Verify iptables rules for IPV6 BlockFragIPPkts for False")
                        print("EXPECTED RESULT 4: The iptables rules specific to IPV6 BlockFragIPPkts should not be present")
                        print("ACTUAL TEST 4: Verification on the iptables rules specific to IPV6 BlockFragIPPkts Disabled  is failed")
                        #Get the result of execution
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("TEST STEP 3: Set IPV6 BlockFragIPPkts value to False")
                    print("EXPECTED RESULT 3: The Set Operation should be success")
                    print("ACTUAL TEST 3: The set operation to make IPV6 BlockFragIPPkts as False was Failed")
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print("TEST STEP 2: Verify iptables rules for IPV6 BlockFragIPPkts for True")
                print("EXPECTED RESULT 2: The iptables rules specific to IPV6 BlockFragIPPkts should be present")
                print("ACTUAL TEST 2: Verification on the iptables rules specific to IPV6 BlockFragIPPkts Enabled is failed")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE")

        else:
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            disable_verify = verify_iptable_rules(tdkTestObj,"false");

            if disable_verify == 0:
                print("Iptables Rules are verified for False")
                tdkTestObj.setResultStatus("SUCCESS");
                print("TEST STEP 2: Verify iptables rules for IPV6 BlockFragIPPkts for False")
                print("EXPECTED RESULT 2: The iptables rules specific to IPV6 BlockFragIPPkts should not be present")
                print("ACTUAL TEST 2: Verification on the iptables rules specific to IPV6 BlockFragIPPkts Disabled is success")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : SUCCESS")

                #set to True
                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                set_enable_res,set_enable_details = set_firewall_security_fragIPPkts (tdkTestObj,"true");
                # wait upto 1 min to complete firewall restart
                sleep(60);

                if expectedresult in set_enable_res:
                    revertFlag = 1;
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("TEST STEP 3: Set IPV6 BlockFragIPPkts value to True")
                    print("EXPECTED RESULT 3: The Set Operation should be success")
                    print("ACTUAL TEST 3: The set operation to make IPV6 BlockFragIPPkts as True was success")
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : SUCCESS")

                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    enable_verify = verify_iptable_rules(tdkTestObj,"true");

                    if enable_verify == 1:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print("TEST STEP 4: Verify iptables rules for IPV6 BlockFragIPPkts for True")
                        print("EXPECTED RESULT 4: The iptables rules specific to IPV6 BlockFragIPPkts should be present")
                        print("ACTUAL TEST 4: Verification on the iptables rules specific to IPV6 BlockFragIPPkts Enabled is success")
                        #Get the result of execution
                        print("[TEST EXECUTION RESULT] : SUCCESS")
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print("TEST STEP 4: Verify iptables rules for IPV6 BlockFragIPPkts for True")
                        print("EXPECTED RESULT 4: The iptables rules specific to IPV6 BlockFragIPPkts should be present")
                        print("ACTUAL TEST 4: Verification on the iptables rules specific to IPV6 BlockFragIPPkts Enabled is failed")
                        #Get the result of execution
                        print("[TEST EXECUTION RESULT] : FAILURE")

                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("TEST STEP 3: Set IPV6 BlockFragIPPkts value to True")
                    print("EXPECTED RESULT 3: The Set Operation should be success")
                    print("ACTUAL TEST 3: The set operation to make IPV6 BlockFragIPPkts as True was Failed")
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : FAILURE")

            else:
                tdkTestObj.setResultStatus("FAILURE");
                print("TEST STEP 2: Verify iptables rules for IPV6 BlockFragIPPkts for False")
                print("EXPECTED RESULT 2: The iptables rules specific to IPV6 BlockFragIPPkts should not be present")
                print("ACTUAL TEST 2: Verification on the iptables rules specific to IPV6 BlockFragIPPkts Disabled is failed")
                #Get the result of execution
                print("[TEST EXECUTION RESULT] : FAILURE")

        #Revert the Value
        if revertFlag ==1:
            if initial_value == "true":
                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                revert_set_result,revert_set_details = set_firewall_security_fragIPPkts (tdkTestObj,"true");

                if expectedresult in revert_set_result:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("TEST STEP 5: Revert the value to True")
                    print("EXPECTED RESULT 5: The Set Operation for revert  should be success")
                    print("ACTUAL TEST 5: The Revert set operation was success")
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("TEST STEP 5: Revert the value to True")
                    print("EXPECTED RESULT 5: The Set Operation for revert  should be success")
                    print("ACTUAL TEST 5: The Revert set operation was Failed")
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                revert_set_result,revert_set_details = set_firewall_security_fragIPPkts (tdkTestObj,"false");

                if expectedresult in revert_set_result:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print("TEST STEP 5: Revert the value to False")
                    print("EXPECTED RESULT 5: The Set Operation for revert  should be success")
                    print("ACTUAL TEST 5: The Revert set operation was success")
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print("TEST STEP 5: Revert the value to False")
                    print("EXPECTED RESULT 5: The Set Operation for revert  should be success")
                    print("ACTUAL TEST 5: The Revert set operation was Failed")
                    #Get the result of execution
                    print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            print("Revert flag was not enabled, No need to revert the value")

    else:
        tdkTestObj.setResultStatus("FAILURE");
        print("TEST STEP 1: Get current value of BlockFragIPPkts")
        print("EXPECTED RESULT 1: Should get current value of BlockFragIPPkts")
        print("ACTUAL RESULT 1: Status is %s" %actualresult);
        #Get the result of execution
        print("[TEST EXECUTION RESULT] : FAILURE");

    obj.unloadModule("pam");
    sysobj.unloadModule("sysutil");

else:
    print("Failed to load pam/sysutil module");
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print("Module loading failed");

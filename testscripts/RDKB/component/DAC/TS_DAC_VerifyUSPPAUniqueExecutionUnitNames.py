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

import tdklib
from time import sleep
from DACVariables import *
from DACUtility import *
from tdkutility import *

# Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1")
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1")

# IP and Port of box, No need to change, will be replaced with DUT details
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_DAC_VerifyUSPPAUniqueExecutionUnitNames')
obj.configureTestCase(ip,port,'TS_DAC_VerifyUSPPAUniqueExecutionUnitNames')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus = obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus_sys.upper() and "SUCCESS" in loadmodulestatus.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Install first DAC bundle via USP-PA
    print("\nTEST STEP %d: Install first DAC bundle via USP-PA" % step)
    print("EXPECTED RESULT %d: First bundle installation should start successfully" % step)
    tdkTestObj, actualresult, details = usppa_install_bundle(sysobj, BUNDLE_DOWNLOAD_URL)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: First bundle installation started. Details: %s" % (step, details))
        print("[TEST EXECUTION RESULT] : SUCCESS")
        sleep(BUNDLE_INSTALL_WAIT_TIME)

        # Verify first bundle is present in destination directory
        step += 1
        print("\nTEST STEP %d: Verify first bundle in destination directory" % step)
        print("EXPECTED RESULT %d: First bundle directory should exist" % step)
        bundle_name_1 = OCI_BUNDLE_NAME.replace('.tar.gz', '')
        expected_items = [bundle_name_1]
        tdkTestObj, actualresult, details = verify_directory_contents(sysobj, DESTINATION_DIR, expected_items)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: First bundle present: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            # Verify DeploymentUnit.1.URL and Status are correct
            step += 1
            print("\nTEST STEP %d: Verify DeploymentUnit.1.URL and Status" % step)
            print("EXPECTED RESULT %d: URL should match and Status should be Installed" % step)
            tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
            actualresult_url, details_url = getTR181Value(tdkTestObj_tr181, DU1_URL_PARAM)
            actualresult_status, details_status = getTR181Value(tdkTestObj_tr181, DU1_STATUS_PARAM)
            if expectedresult in actualresult_url and BUNDLE_DOWNLOAD_URL in details_url and EXPECTED_DU_STATUS in details_status:
                tdkTestObj_tr181.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: DeploymentUnit.1 verified - URL: %s, Status: %s" % (step, details_url, details_status))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                # Install second DAC bundle via USP-PA
                step += 1
                print("\nTEST STEP %d: Install second DAC bundle via USP-PA" % step)
                print("EXPECTED RESULT %d: Second bundle installation should start successfully" % step)
                tdkTestObj, actualresult, details = usppa_install_bundle(sysobj, BUNDLE_DOWNLOAD_URL_2)
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: Second bundle installation started. Details: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                    sleep(BUNDLE_INSTALL_WAIT_TIME)

                    # Verify second bundle is present in destination directory
                    step += 1
                    print("\nTEST STEP %d: Verify second bundle in destination directory" % step)
                    print("EXPECTED RESULT %d: Second bundle directory should exist" % step)
                    bundle_name_2 = OCI_BUNDLE_NAME_2.replace('.tar.gz', '')
                    expected_items = [bundle_name_1, bundle_name_2]
                    tdkTestObj, actualresult, details = verify_directory_contents(sysobj, DESTINATION_DIR, expected_items)
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS")
                        print("ACTUAL RESULT %d: Second bundle present: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : SUCCESS")

                        # Verify DeploymentUnit.2.URL and Status are correct
                        step += 1
                        print("\nTEST STEP %d: Verify DeploymentUnit.2.URL and Status" % step)
                        print("EXPECTED RESULT %d: URL should match and Status should be Installed" % step)
                        actualresult_url, details_url = getTR181Value(tdkTestObj_tr181, DU2_URL_PARAM)
                        actualresult_status, details_status = getTR181Value(tdkTestObj_tr181, DU2_STATUS_PARAM)
                        if expectedresult in actualresult_url and BUNDLE_DOWNLOAD_URL_2 in details_url and EXPECTED_DU_STATUS in details_status:
                            tdkTestObj_tr181.setResultStatus("SUCCESS")
                            print("ACTUAL RESULT %d: DeploymentUnit.2 verified - URL: %s, Status: %s" % (step, details_url, details_status))
                            print("[TEST EXECUTION RESULT] : SUCCESS")

                            # Verify unique names assigned to ExecutionUnits
                            step += 1
                            print("\nTEST STEP %d: Verify unique names assigned to ExecutionUnits" % step)
                            print("EXPECTED RESULT %d: ExecutionUnit.1 and ExecutionUnit.2 should have unique names" % step)
                            actualresult_eu1, eu1_name = getTR181Value(tdkTestObj_tr181, EU1_NAME_PARAM)
                            actualresult_eu2, eu2_name = getTR181Value(tdkTestObj_tr181, EU2_NAME_PARAM)
                            if expectedresult in actualresult_eu1 and expectedresult in actualresult_eu2 and eu1_name != eu2_name:
                                tdkTestObj_tr181.setResultStatus("SUCCESS")
                                print("ACTUAL RESULT %d: Unique names assigned - EU1: %s, EU2: %s" % (step, eu1_name, eu2_name))
                                print("[TEST EXECUTION RESULT] : SUCCESS")
                            else:
                                tdkTestObj_tr181.setResultStatus("FAILURE")
                                print("ACTUAL RESULT %d: ExecutionUnit names check failed - EU1: %s, EU2: %s" % (step, eu1_name, eu2_name))
                                print("[TEST EXECUTION RESULT] : FAILURE")
                        else:
                            tdkTestObj_tr181.setResultStatus("FAILURE")
                            print("ACTUAL RESULT %d: DeploymentUnit.2 verification failed" % step)
                            print("[TEST EXECUTION RESULT] : FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE")
                        print("ACTUAL RESULT %d: Second bundle not found. Details: %s" % (step, details))
                        print("[TEST EXECUTION RESULT] : FAILURE")
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: Second bundle installation failed. Details: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj_tr181.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: DeploymentUnit.1 verification failed" % step)
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: First bundle not found. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : FAILURE")

        # Cleanup: Uninstall the Execution Units(Both first and second)
        step += 1
        print("\nTEST STEP %d: Cleanup - Uninstall first DeploymentUnit" % step)
        print("EXPECTED RESULT %d: Uninstall should start successfully" % step)
        tdkTestObj, actualresult, details = usppa_uninstall_bundle(sysobj, DU_UNINSTALL_PARAM_1)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: First bundle uninstall started. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: First bundle uninstall failed. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : FAILURE")

        step += 1
        print("\nTEST STEP %d: Cleanup - Uninstall second DeploymentUnit" % step)
        print("EXPECTED RESULT %d: Uninstall should start successfully" % step)
        tdkTestObj, actualresult, details = usppa_uninstall_bundle(sysobj, DU_UNINSTALL_PARAM_2)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Second bundle uninstall started. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Second bundle uninstall failed. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: First bundle installation failed. Details: %s" % (step, details))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload the modules
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")


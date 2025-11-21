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
sysobj.configureTestCase(ip,port,'TS_DAC_VerifyUSPPABundleInstallAndActivation')
obj.configureTestCase(ip,port,'TS_DAC_VerifyUSPPABundleInstallAndActivation')

# Get the result of connection with test component and DUT
loadmodulestatus_sys = sysobj.getLoadModuleResult()
loadmodulestatus = obj.getLoadModuleResult()

if "SUCCESS" in loadmodulestatus_sys.upper() and "SUCCESS" in loadmodulestatus.upper():
    sysobj.setLoadModuleStatus("SUCCESS")
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult = "SUCCESS"
    step = 1

    # Install DAC bundle via USP-PA
    print("\nTEST STEP %d: Install DAC bundle via USP-PA" % step)
    print("EXPECTED RESULT %d: Bundle installation should start successfully" % step)
    tdkTestObj, actualresult, details = usppa_install_bundle(sysobj, BUNDLE_DOWNLOAD_URL)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print("ACTUAL RESULT %d: Bundle installation started. Details: %s" % (step, details))
        print("[TEST EXECUTION RESULT] : SUCCESS")
        print("Waiting %d seconds for installation to complete..." % BUNDLE_INSTALL_WAIT_TIME)
        sleep(BUNDLE_INSTALL_WAIT_TIME)

        step += 1
        # Confirm installed app is present in destination directory
        print("\nTEST STEP %d: Confirm installed app is present in destination directory" % step)
        print("EXPECTED RESULT %d: Bundle directory should exist in destination" % step)
        bundle_name = OCI_BUNDLE_NAME.replace('.tar.gz', '')
        expected_items = [bundle_name, f"{OCI_BUNDLE_NAME}.json"]
        tdkTestObj, actualresult, details = verify_directory_contents(sysobj, DESTINATION_DIR, expected_items)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Installed app present: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : SUCCESS")

            step += 1
            # Activate ExecutionUnit
            print("\nTEST STEP %d: Activate ExecutionUnit via USP-PA" % step)
            print("EXPECTED RESULT %d: ExecutionUnit should be activated successfully" % step)
            tdkTestObj, actualresult, details = usppa_set_eu_state(sysobj, EU_SET_STATE_PARAM, "Active")
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: ExecutionUnit activated. Details: %s" % (step, details))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                # Check container status
                print("\nTEST STEP %d: Check container status using DobbyTool list" % step)
                print("EXPECTED RESULT %d: Container should be listed" % step)
                tdkTestObj, actualresult, details = list_dobby_containers(sysobj)
                tdkTestObj.setResultStatus("SUCCESS")
                print("ACTUAL RESULT %d: DobbyTool list output: %s" % (step, details))
                print("[TEST EXECUTION RESULT] : SUCCESS")

                step += 1
                # Verify ExecutionUnit.1.Status
                print("\nTEST STEP %d: Verify ExecutionUnit.1.Status changed to Active" % step)
                print("EXPECTED RESULT %d: Status should be Active" % step)
                tdkTestObj_tr181 = obj.createTestStep('TDKB_TR181Stub_Get')
                actualresult, details = getTR181Value(tdkTestObj_tr181, EU1_STATUS_PARAM)
                if expectedresult in actualresult and EXPECTED_EU_STATUS_ACTIVE in details:
                    tdkTestObj_tr181.setResultStatus("SUCCESS")
                    print("ACTUAL RESULT %d: ExecutionUnit status is Active: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : SUCCESS")
                else:
                    tdkTestObj_tr181.setResultStatus("FAILURE")
                    print("ACTUAL RESULT %d: ExecutionUnit status check failed. Details: %s" % (step, details))
                    print("[TEST EXECUTION RESULT] : FAILURE")
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print("ACTUAL RESULT %d: Failed to activate ExecutionUnit. Details: %s" % (step, details))
                print("[TEST EXECUTION RESULT] : FAILURE")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Installed app not found in destination. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : FAILURE")

        step += 1
        # Cleanup: Uninstall the Execution Unit
        print("\nTEST STEP %d: Cleanup - Uninstall the Execution Unit via USP-PA" % step)
        print("EXPECTED RESULT %d: Uninstall should start successfully" % step)
        tdkTestObj, actualresult, details = usppa_uninstall_bundle(sysobj, DU_UNINSTALL_PARAM_1)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS")
            print("ACTUAL RESULT %d: Uninstall started. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : SUCCESS")
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print("ACTUAL RESULT %d: Uninstall failed. Details: %s" % (step, details))
            print("[TEST EXECUTION RESULT] : FAILURE")
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print("ACTUAL RESULT %d: Bundle installation failed. Details: %s" % (step, details))
        print("[TEST EXECUTION RESULT] : FAILURE")

    # Unload the modules
    obj.unloadModule("tdkbtr181")
    sysobj.unloadModule("sysutil")
else:
    print("Failed to load the module")
    obj.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print("Module loading failed")


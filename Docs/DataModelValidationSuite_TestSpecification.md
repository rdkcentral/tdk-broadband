# Data Model Validation Suite

## Test Specification Document for Data Model Validation Suite

<strong>Version:</strong> 1.0  
<strong>Date:</strong> August 2026  
<strong>Purpose:</strong> Low-level test specification for Data Model validation.  
<strong>Maintained by:</strong> TDKB Test Automation Team

| # | Category | Description | Number of Tests |
|---|----------|-------------|-----------------|
| 1 | TR181 Validation | Low-level validation through TR-181 interface test scripts | 100 |
| 2 | WEBPA Validation | Low-level validation through WEBPA interface test scripts | 62 |

---

<details>
<summary><strong>TR181 Validation</strong></summary>

# TR181 Validation

<details>
<summary><strong>Test Case 1: Validate TR-181 get all parameter values for ADVSEC.</strong></summary>

## Test Case 1: TDKB_DML_TR181_ADVSEC_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the Advanced Security module and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_1

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for ADVSEC</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform GET on all applicable Device.* parameters under ADVSEC through the TR181 path</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 2: Validate TR-181 perform L2 set validations for ADVSEC.</strong></summary>

## Test Case 2: TDKB_DML_TR181_ADVSEC_L2SetValidations

## Objectives
To check if all the L2 SET operations are successful and to validate the corresponding use-cases under ADVSEC module.

## Test Case ID
TC_TDKB_DML_142

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device parameters under module scope (ADVSEC) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform GET on baseline values for L2-set parameters under ADVSEC through the TR181 path</small> | <small>Confirm baseline values are captured before the SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on L2-set parameters under ADVSEC to As per configuration through the TR181 path</small> | <small>Confirm parameter updates satisfy dependency and operational constraints. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Revert each modified parameter to original value</small> | <small>Verify revert operations succeed and final state is restored. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 3: Validate TR-181 verify parameter existence for ADVSEC.</strong></summary>

## Test Case 3: TDKB_DML_TR181_ADVSEC_ParameterExistenceCheck

## Objectives
To check if all the required namespaces under Advanced Security module exists.

## Test Case ID
TC_TDKB_DML_39

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform recursive parameter discovery from module root objects under ADVSEC</small> | <small>Confirm namespace discovery is successful. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Check the discovered hierarchy against expected parameter coverage</small> | <small>If all expected parameters exist PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 4: Validate TR-181 validate read-only set rejection for ADVSEC.</strong></summary>

## Test Case 4: TDKB_DML_TR181_ADVSEC_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the Advanced Security module and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_20

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (ADVSEC) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on read-only Device parameters under ADVSEC to valid values through the TR181 path</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 5: Validate TR-181 validate write-access compliance for ADVSEC.</strong></summary>

## Test Case 5: TDKB_DML_TR181_ADVSEC_WriteAccessComplianceCheck

## Objectives
To check if write operations does not return the read-only error code for all parameters in Advanced Security module which are writable.

## Test Case ID
TC_TDKB_DML_58

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (ADVSEC) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform SET on writable Device parameters under ADVSEC to current runtime value retrieved in previous step through the TR181 path</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 6: Validate TR-181 validate write-type compliance for ADVSEC.</strong></summary>

## Test Case 6: TDKB_DML_TR181_ADVSEC_WriteTypeComplianceCheck

## Objectives
To check if write operations return the expected error code for all writable parameters in Advanced Security module using an invalid type.

## Test Case ID
TC_TDKB_DML_77

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (ADVSEC) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on writable Device parameters under ADVSEC using invalid data type to invalid-type values through the TR181 path</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 7: Validate TR-181 get all parameter values for CR.</strong></summary>

## Test Case 7: TDKB_DML_TR181_CR_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the Component Register module and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_3

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for CR</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform GET on all applicable Device.* parameters under CR through the TR181 path</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 8: Validate TR-181 verify parameter existence for CR.</strong></summary>

## Test Case 8: TDKB_DML_TR181_CR_ParameterExistenceCheck

## Objectives
To check if all the required namespaces under CR module exists.

## Test Case ID
TC_TDKB_DML_41

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform recursive parameter discovery from module root objects under CR</small> | <small>Confirm namespace discovery is successful. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Check the discovered hierarchy against expected parameter coverage</small> | <small>If all expected parameters exist PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 9: Validate TR-181 validate read-only set rejection for CR.</strong></summary>

## Test Case 9: TDKB_DML_TR181_CR_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the CR module and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_22

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (CR) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on read-only Device parameters under CR to valid values through the TR181 path</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 10: Validate TR-181 validate write-access compliance for CR.</strong></summary>

## Test Case 10: TDKB_DML_TR181_CR_WriteAccessComplianceCheck

## Objectives
To check if write operations does not return the read-only error code for all parameters in CR module which are writable.

## Test Case ID
TC_TDKB_DML_60

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (CR) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform SET on writable Device parameters under CR to current runtime value retrieved in previous step through the TR181 path</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 11: Validate TR-181 validate write-type compliance for CR.</strong></summary>

## Test Case 11: TDKB_DML_TR181_CR_WriteTypeComplianceCheck

## Objectives
To check if write operations return the expected error code for all writable parameters in CR module using an invalid type.

## Test Case ID
TC_TDKB_DML_79

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (CR) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on writable Device parameters under CR using invalid data type to invalid-type values through the TR181 path</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 12: Validate TR-181 add and delete writable table rows for ETHAGENT.</strong></summary>

## Test Case 12: TDKB_DML_TR181_ETHAGENT_AddAndDeleteWritableTableRow

## Objectives
To check if adding a row to a non-rigid writable table object is success and all expected parameters under that table object instance should be created successfully for ETHAGENT module. Also check if the delete table row operation is success.

## Test Case ID
TC_TDKB_DML_137

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Child parameters of newly added table row under module scope (ETHAGENT) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform ADD on writable table row under ETHAGENT through the TR181 path</small> | <small>Confirm row addition succeeds and child parameters are present. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Set mandatory child parameters on the newly added instance to As per configuration</small> | <small>Confirm instance configuration is accepted. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform DELETE on added writable table row instance under ETHAGENT through the TR181 path</small> | <small>Verify deletion succeeds for the created instance. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 13: Validate TR-181 validate dynamic table row add behavior for ETHAGENT.</strong></summary>

## Test Case 13: TDKB_DML_TR181_ETHAGENT_AddDynamicTableRow

## Objectives
To check if adding rows to dynamic table objects under ETHAGENT module returns the expected errorcode.

## Test Case ID
TC_TDKB_DML_115

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables for the module on the target platform</small> | <small>Confirm dynamic tables are discovered for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform ADD on dynamic table row under ETHAGENT through the TR181 path</small> | <small>Verify add operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 14: Validate TR-181 validate static table row add behavior for ETHAGENT.</strong></summary>

## Test Case 14: TDKB_DML_TR181_ETHAGENT_AddStaticTableRow

## Objectives
To check if adding rows to static table objects under ETHAGENT module returns the expected error code.

## Test Case ID
TC_TDKB_DML_96

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables for the module on the target platform</small> | <small>Confirm at least one applicable table is selected for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform ADD on static table row under ETHAGENT through the TR181 path</small> | <small>Verify add operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 15: Validate TR-181 validate dynamic table row delete behavior for ETHAGENT.</strong></summary>

## Test Case 15: TDKB_DML_TR181_ETHAGENT_DeleteDynamicTableRow

## Objectives
To check if deleting rows from dynamic table objects under ETHAGENT module returns the expected error code.

## Test Case ID
TC_TDKB_DML_124

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables and candidate instance entries</small> | <small>Confirm delete preconditions are available for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform DELETE on dynamic table row under ETHAGENT through the TR181 path</small> | <small>Verify delete operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 16: Validate TR-181 validate static table row delete behavior for ETHAGENT.</strong></summary>

## Test Case 16: TDKB_DML_TR181_ETHAGENT_DeleteStaticTableRow

## Objectives
To check if deleting rows from static table objects under ETHAGENT module returns the expected errorcode.

## Test Case ID
TC_TDKB_DML_105

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables and choose a candidate instance</small> | <small>Confirm table instance context is available for deletion attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform DELETE on static table row under ETHAGENT through the TR181 path</small> | <small>Verify delete operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 17: Validate TR-181 get all parameter values for ETHAGENT.</strong></summary>

## Test Case 17: TDKB_DML_TR181_ETHAGENT_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the EthAgent module and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_4

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for ETHAGENT</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform GET on all applicable Device.* parameters under ETHAGENT through the TR181 path</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 18: Validate TR-181 perform L2 set validations for ETHAGENT.</strong></summary>

## Test Case 18: TDKB_DML_TR181_ETHAGENT_L2SetValidations

## Objectives
To check if all the L2 SET operations are successful and to validate the corresponding use-cases under ETHAGENT module.

## Test Case ID
TC_TDKB_DML_143

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device parameters under module scope (ETHAGENT) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform GET on baseline values for L2-set parameters under ETHAGENT through the TR181 path</small> | <small>Confirm baseline values are captured before the SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on L2-set parameters under ETHAGENT to As per configuration through the TR181 path</small> | <small>Confirm parameter updates satisfy dependency and operational constraints. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Revert each modified parameter to original value</small> | <small>Verify revert operations succeed and final state is restored. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 19: Validate TR-181 verify parameter existence for ETHAGENT.</strong></summary>

## Test Case 19: TDKB_DML_TR181_ETHAGENT_ParameterExistenceCheck

## Objectives
To check if all the required namespaces under ETHAGENT module exists.

## Test Case ID
TC_TDKB_DML_42

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform recursive parameter discovery from module root objects under ETHAGENT</small> | <small>Confirm namespace discovery is successful. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Check the discovered hierarchy against expected parameter coverage</small> | <small>If all expected parameters exist PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 20: Validate TR-181 validate read-only set rejection for ETHAGENT.</strong></summary>

## Test Case 20: TDKB_DML_TR181_ETHAGENT_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the Ethagent module and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_23

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (ETHAGENT) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on read-only Device parameters under ETHAGENT to valid values through the TR181 path</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 21: Validate TR-181 validate write-access compliance for ETHAGENT.</strong></summary>

## Test Case 21: TDKB_DML_TR181_ETHAGENT_WriteAccessComplianceCheck

## Objectives
To check if write operations does not return the read-only error code for all parameters in ETHAGENT module which are writable.

## Test Case ID
TC_TDKB_DML_61

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (ETHAGENT) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform SET on writable Device parameters under ETHAGENT to current runtime value retrieved in previous step through the TR181 path</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 22: Validate TR-181 validate write-type compliance for ETHAGENT.</strong></summary>

## Test Case 22: TDKB_DML_TR181_ETHAGENT_WriteTypeComplianceCheck

## Objectives
To check if write operations return the expected error code for all writable parameters in EthAgent module using an invalid type.

## Test Case ID
TC_TDKB_DML_80

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (ETHAGENT) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on writable Device parameters under ETHAGENT using invalid data type to invalid-type values through the TR181 path</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 23: Validate TR-181 add and delete dynamic writable table rows for LMLITE.</strong></summary>

## Test Case 23: TDKB_DML_TR181_LMLITE_AddAndDeleteDynamicWritableTableRow

## Objectives
To check if adding a row to a dynamic writable table object is success and all expected parameters under that table object instance should be created successfully for LMLITE module. Also check if the delete operation is success.

## Test Case ID
TC_TDKB_DML_135

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Child parameters of newly added table row under module scope (LMLITE) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform ADD on dynamic writable table row under LMLITE through the TR181 path</small> | <small>Confirm row addition succeeds and new instance index is returned. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Set mandatory child parameters on the newly added instance to As per configuration</small> | <small>Confirm child parameters are present and configurable. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform DELETE on added dynamic writable table row instance under LMLITE through the TR181 path</small> | <small>Verify deletion succeeds for the created instance. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 24: Validate TR-181 validate dynamic table row add behavior for LMLITE.</strong></summary>

## Test Case 24: TDKB_DML_TR181_LMLITE_AddDynamicTableRow

## Objectives
To check if adding rows to dynamic table objects under LMLITE module returns the expected error code.

## Test Case ID
TC_TDKB_DML_116

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables for the module on the target platform</small> | <small>Confirm dynamic tables are discovered for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform ADD on dynamic table row under LMLITE through the TR181 path</small> | <small>Verify add operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 25: Validate TR-181 validate static table row add behavior for LMLITE.</strong></summary>

## Test Case 25: TDKB_DML_TR181_LMLITE_AddStaticTableRow

## Objectives
To check if adding rows to static table objects under LMLITE module returns the expected error code.

## Test Case ID
TC_TDKB_DML_97

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables for the module on the target platform</small> | <small>Confirm at least one applicable table is selected for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform ADD on static table row under LMLITE through the TR181 path</small> | <small>Verify add operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 26: Validate TR-181 validate dynamic table row delete behavior for LMLITE.</strong></summary>

## Test Case 26: TDKB_DML_TR181_LMLITE_DeleteDynamicTableRow

## Objectives
To check if deleting rows from dynamic table objects under LMLITE module returns the expected errorcode.

## Test Case ID
TC_TDKB_DML_125

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables and candidate instance entries</small> | <small>Confirm delete preconditions are available for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform DELETE on dynamic table row under LMLITE through the TR181 path</small> | <small>Verify delete operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 27: Validate TR-181 validate static table row delete behavior for LMLITE.</strong></summary>

## Test Case 27: TDKB_DML_TR181_LMLITE_DeleteStaticTableRow

## Objectives
To check if deleting rows from static table objects under LMLITE module returns the expected errorcode.

## Test Case ID
TC_TDKB_DML_106

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables and choose a candidate instance</small> | <small>Confirm table instance context is available for deletion attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform DELETE on static table row under LMLITE through the TR181 path</small> | <small>Verify delete operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 28: Validate TR-181 get all parameter values for LMLITE.</strong></summary>

## Test Case 28: TDKB_DML_TR181_LMLITE_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the LMLITE module and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_7

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for LMLITE</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform GET on all applicable Device.* parameters under LMLITE through the TR181 path</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 29: Validate TR-181 perform L2 set validations for LMLITE.</strong></summary>

## Test Case 29: TDKB_DML_TR181_LMLITE_L2SetValidations

## Objectives
To check if all the L2 SET operations are successful and to validate the corresponding use-cases under LMLITE module.

## Test Case ID
TC_TDKB_DML_144

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device parameters under module scope (LMLITE) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform GET on baseline values for L2-set parameters under LMLITE through the TR181 path</small> | <small>Confirm baseline values are captured before the SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on L2-set parameters under LMLITE to As per configuration through the TR181 path</small> | <small>Confirm parameter updates satisfy dependency and operational constraints. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Revert each modified parameter to original value</small> | <small>Verify revert operations succeed and final state is restored. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 30: Validate TR-181 verify parameter existence for LMLITE.</strong></summary>

## Test Case 30: TDKB_DML_TR181_LMLITE_ParameterExistenceCheck

## Objectives
To check if all the required namespaces under LMLITE module exists.

## Test Case ID
TC_TDKB_DML_45

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform recursive parameter discovery from module root objects under LMLITE</small> | <small>Confirm namespace discovery is successful. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Check the discovered hierarchy against expected parameter coverage</small> | <small>If all expected parameters exist PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 31: Validate TR-181 validate read-only set rejection for LMLITE.</strong></summary>

## Test Case 31: TDKB_DML_TR181_LMLITE_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the LMLite module and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_26

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (LMLITE) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on read-only Device parameters under LMLITE to valid values through the TR181 path</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 32: Validate TR-181 validate write-access compliance for LMLITE.</strong></summary>

## Test Case 32: TDKB_DML_TR181_LMLITE_WriteAccessComplianceCheck

## Objectives
To check if write operations does not return the read-only error code for all parameters in LMLite module which are writable.

## Test Case ID
TC_TDKB_DML_64

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (LMLITE) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform SET on writable Device parameters under LMLITE to current runtime value retrieved in previous step through the TR181 path</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 33: Validate TR-181 validate write-type compliance for LMLITE.</strong></summary>

## Test Case 33: TDKB_DML_TR181_LMLITE_WriteTypeComplianceCheck

## Objectives
To check if write operations return the expected error code for all writable parameters in LMLITE module using an invalid type.

## Test Case ID
TC_TDKB_DML_83

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (LMLITE) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on writable Device parameters under LMLITE using invalid data type to invalid-type values through the TR181 path</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 34: Validate TR-181 add and delete dynamic writable table rows for PAM.</strong></summary>

## Test Case 34: TDKB_DML_TR181_PAM_AddAndDeleteDynamicWritableTableRow

## Objectives
To check if adding a row to a dynamic writable table object is success and all expected parameters under that table object instance should be created successfully for PAM module. Also check if the delete operation is success.

## Test Case ID
TC_TDKB_DML_132

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Child parameters of newly added table row under module scope (PAM) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform ADD on dynamic writable table row under PAM through the TR181 path</small> | <small>Confirm row addition succeeds and new instance index is returned. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Set mandatory child parameters on the newly added instance to As per configuration</small> | <small>Confirm child parameters are present and configurable. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform DELETE on added dynamic writable table row instance under PAM through the TR181 path</small> | <small>Verify deletion succeeds for the created instance. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 35: Validate TR-181 add and delete writable table rows for PAM.</strong></summary>

## Test Case 35: TDKB_DML_TR181_PAM_AddAndDeleteWritableTableRow

## Objectives
To check if adding a row to a non-rigid writable table object is success and all expected parameters under that table object instance should be created successfully for PAM module. Also check if the delete table row operation is success.

## Test Case ID
TC_TDKB_DML_138

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Child parameters of newly added table row under module scope (PAM) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform ADD on writable table row under PAM through the TR181 path</small> | <small>Confirm row addition succeeds and child parameters are present. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Set mandatory child parameters on the newly added instance to As per configuration</small> | <small>Confirm instance configuration is accepted. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform DELETE on added writable table row instance under PAM through the TR181 path</small> | <small>Verify deletion succeeds for the created instance. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 36: Validate TR-181 validate dynamic table row add behavior for PAM.</strong></summary>

## Test Case 36: TDKB_DML_TR181_PAM_AddDynamicTableRow

## Objectives
To check if adding rows to dynamic table objects under PAM module returns the expected error code.

## Test Case ID
TC_TDKB_DML_119

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables for the module on the target platform</small> | <small>Confirm dynamic tables are discovered for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform ADD on dynamic table row under PAM through the TR181 path</small> | <small>Verify add operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 37: Validate TR-181 validate static table row add behavior for PAM.</strong></summary>

## Test Case 37: TDKB_DML_TR181_PAM_AddStaticTableRow

## Objectives
To check if adding rows to static table objects under PAM module returns the expected error code.

## Test Case ID
TC_TDKB_DML_100

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables for the module on the target platform</small> | <small>Confirm at least one applicable table is selected for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform ADD on static table row under PAM through the TR181 path</small> | <small>Verify add operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 38: Validate TR-181 validate dynamic table row delete behavior for PAM.</strong></summary>

## Test Case 38: TDKB_DML_TR181_PAM_DeleteDynamicTableRow

## Objectives
To check if deleting rows from dynamic table objects under PAM module returns the expected errorcode.

## Test Case ID
TC_TDKB_DML_128

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables and candidate instance entries</small> | <small>Confirm delete preconditions are available for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform DELETE on dynamic table row under PAM through the TR181 path</small> | <small>Verify delete operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 39: Validate TR-181 validate static table row delete behavior for PAM.</strong></summary>

## Test Case 39: TDKB_DML_TR181_PAM_DeleteStaticTableRow

## Objectives
To check if deleting rows from static table objects under PAM module returns the expected errorcode.

## Test Case ID
TC_TDKB_DML_109

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables and choose a candidate instance</small> | <small>Confirm table instance context is available for deletion attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform DELETE on static table row under PAM through the TR181 path</small> | <small>Verify delete operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 40: Validate TR-181 get all parameter values for PAM.</strong></summary>

## Test Case 40: TDKB_DML_TR181_PAM_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the PAM module and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_19

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for PAM</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform GET on all applicable Device.* parameters under PAM through the TR181 path</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 41: Validate TR-181 perform L2 set validations for PAM.</strong></summary>

## Test Case 41: TDKB_DML_TR181_PAM_L2SetValidations

## Objectives
To check if all the L2 SET operations are successful and to validate the corresponding use-cases under PAM module.

## Test Case ID
TC_TDKB_DML_146

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device parameters under module scope (PAM) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform GET on baseline values for L2-set parameters under PAM through the TR181 path</small> | <small>Confirm baseline values are captured before the SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on L2-set parameters under PAM to As per configuration through the TR181 path</small> | <small>Confirm parameter updates satisfy dependency and operational constraints. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Revert each modified parameter to original value</small> | <small>Verify revert operations succeed and final state is restored. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 42: Validate TR-181 verify parameter existence for PAM.</strong></summary>

## Test Case 42: TDKB_DML_TR181_PAM_ParameterExistenceCheck

## Objectives
To check if all the required namespaces under PAM module exists.

## Test Case ID
TC_TDKB_DML_51

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform recursive parameter discovery from module root objects under PAM</small> | <small>Confirm namespace discovery is successful. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Check the discovered hierarchy against expected parameter coverage</small> | <small>If all expected parameters exist PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 43: Validate TR-181 validate read-only set rejection for PAM.</strong></summary>

## Test Case 43: TDKB_DML_TR181_PAM_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the PAM module and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_32

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (PAM) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on read-only Device parameters under PAM to valid values through the TR181 path</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 44: Validate TR-181 validate write-access compliance for PAM.</strong></summary>

## Test Case 44: TDKB_DML_TR181_PAM_WriteAccessComplianceCheck

## Objectives
To check if write operations does not return the read-only error code for all parameters in PAM module which are writable.

## Test Case ID
TC_TDKB_DML_70

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (PAM) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform SET on writable Device parameters under PAM to current runtime value retrieved in previous step through the TR181 path</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 45: Validate TR-181 validate write-type compliance for PAM.</strong></summary>

## Test Case 45: TDKB_DML_TR181_PAM_WriteTypeComplianceCheck

## Objectives
To check if write operations return the expected error code for all writable parameters in PAM module using an invalid type.

## Test Case ID
TC_TDKB_DML_94

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (PAM) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on writable Device parameters under PAM using invalid data type to invalid-type values through the TR181 path</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 46: Validate TR-181 add and delete dynamic writable table rows for TDM.</strong></summary>

## Test Case 46: TDKB_DML_TR181_TDM_AddAndDeleteDynamicWritableTableRow

## Objectives
To check if adding a row to a dynamic writable table object is success and all expected parameters under that table object instance should be created successfully for TDM module. Also check if the delete operation is success.

## Test Case ID
TC_TDKB_DML_134

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Child parameters of newly added table row under module scope (TDM) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform ADD on dynamic writable table row under TDM through the TR181 path</small> | <small>Confirm row addition succeeds and new instance index is returned. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Set mandatory child parameters on the newly added instance to As per configuration</small> | <small>Confirm child parameters are present and configurable. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform DELETE on added dynamic writable table row instance under TDM through the TR181 path</small> | <small>Verify deletion succeeds for the created instance. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 47: Validate TR-181 add and delete writable table rows for TDM.</strong></summary>

## Test Case 47: TDKB_DML_TR181_TDM_AddAndDeleteWritableTableRow

## Objectives
To check if adding a row to a non-rigid writable table object is success and all expected parameters under that table object instance should be created successfully for TDM module. Also check if the delete table row operation is success.

## Test Case ID
TC_TDKB_DML_139

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Child parameters of newly added table row under module scope (TDM) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform ADD on writable table row under TDM through the TR181 path</small> | <small>Confirm row addition succeeds and child parameters are present. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Set mandatory child parameters on the newly added instance to As per configuration</small> | <small>Confirm instance configuration is accepted. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform DELETE on added writable table row instance under TDM through the TR181 path</small> | <small>Verify deletion succeeds for the created instance. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 48: Validate TR-181 validate dynamic table row add behavior for TDM.</strong></summary>

## Test Case 48: TDKB_DML_TR181_TDM_AddDynamicTableRow

## Objectives
To check if adding rows to dynamic table objects under TDM module returns the expected error code.

## Test Case ID
TC_TDKB_DML_120

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables for the module on the target platform</small> | <small>Confirm dynamic tables are discovered for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform ADD on dynamic table row under TDM through the TR181 path</small> | <small>Verify add operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 49: Validate TR-181 validate static table row add behavior for TDM.</strong></summary>

## Test Case 49: TDKB_DML_TR181_TDM_AddStaticTableRow

## Objectives
To check if adding rows to static table objects under TDM module returns the expected error code.

## Test Case ID
TC_TDKB_DML_101

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables for the module on the target platform</small> | <small>Confirm at least one applicable table is selected for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform ADD on static table row under TDM through the TR181 path</small> | <small>Verify add operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 50: Validate TR-181 validate dynamic table row delete behavior for TDM.</strong></summary>

## Test Case 50: TDKB_DML_TR181_TDM_DeleteDynamicTableRow

## Objectives
To check if deleting rows from dynamic table objects under TDM module returns the expected errorcode.

## Test Case ID
TC_TDKB_DML_129

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables and candidate instance entries</small> | <small>Confirm delete preconditions are available for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform DELETE on dynamic table row under TDM through the TR181 path</small> | <small>Verify delete operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 51: Validate TR-181 validate static table row delete behavior for TDM.</strong></summary>

## Test Case 51: TDKB_DML_TR181_TDM_DeleteStaticTableRow

## Objectives
To check if deleting rows from static table objects under TDM module returns the expected errorcode.

## Test Case ID
TC_TDKB_DML_110

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables and choose a candidate instance</small> | <small>Confirm table instance context is available for deletion attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform DELETE on static table row under TDM through the TR181 path</small> | <small>Verify delete operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 52: Validate TR-181 get all parameter values for TDM.</strong></summary>

## Test Case 52: TDKB_DML_TR181_TDM_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the TDM module and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_13

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for TDM</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform GET on all applicable Device.* parameters under TDM through the TR181 path</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 53: Validate TR-181 perform L2 set validations for TDM.</strong></summary>

## Test Case 53: TDKB_DML_TR181_TDM_L2SetValidations

## Objectives
To check if all the L2 SET operations are successful and to validate the corresponding use-cases under TDM module.

## Test Case ID
TC_TDKB_DML_145

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device parameters under module scope (TDM) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform GET on baseline values for L2-set parameters under TDM through the TR181 path</small> | <small>Confirm baseline values are captured before the SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on L2-set parameters under TDM to As per configuration through the TR181 path</small> | <small>Confirm parameter updates satisfy dependency and operational constraints. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Revert each modified parameter to original value</small> | <small>Verify revert operations succeed and final state is restored. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 54: Validate TR-181 verify parameter existence for TDM.</strong></summary>

## Test Case 54: TDKB_DML_TR181_TDM_ParameterExistenceCheck

## Objectives
To check if all the required namespaces under TDM module exists.

## Test Case ID
TC_TDKB_DML_52

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform recursive parameter discovery from module root objects under TDM</small> | <small>Confirm namespace discovery is successful. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Check the discovered hierarchy against expected parameter coverage</small> | <small>If all expected parameters exist PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 55: Validate TR-181 validate read-only set rejection for TDM.</strong></summary>

## Test Case 55: TDKB_DML_TR181_TDM_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the TDM module and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_33

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (TDM) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on read-only Device parameters under TDM to valid values through the TR181 path</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 56: Validate TR-181 validate write-access compliance for TDM.</strong></summary>

## Test Case 56: TDKB_DML_TR181_TDM_WriteAccessComplianceCheck

## Objectives
To check if write operations does not return the read-only error code for all parameters in TestAndDiagnostics module which are writable.

## Test Case ID
TC_TDKB_DML_71

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (TDM) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform SET on writable Device parameters under TDM to current runtime value retrieved in previous step through the TR181 path</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 57: Validate TR-181 validate write-type compliance for TDM.</strong></summary>

## Test Case 57: TDKB_DML_TR181_TDM_WriteTypeComplianceCheck

## Objectives
To check if write operations return the expected error code for all writable parameters in TDM module using an invalid type.

## Test Case ID
TC_TDKB_DML_88

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (TDM) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on writable Device parameters under TDM using invalid data type to invalid-type values through the TR181 path</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 58: Validate TR-181 get all parameter values for TELEMETRY.</strong></summary>

## Test Case 58: TDKB_DML_TR181_TELEMETRY_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the TELEMETRY module and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_14

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for TELEMETRY</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform GET on all applicable Device.* parameters under TELEMETRY through the TR181 path</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 59: Validate TR-181 verify parameter existence for TELEMETRY.</strong></summary>

## Test Case 59: TDKB_DML_TR181_TELEMETRY_ParameterExistenceCheck

## Objectives
To check if all the required namespaces under TELEMETRY module exists.

## Test Case ID
TC_TDKB_DML_53

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform recursive parameter discovery from module root objects under TELEMETRY</small> | <small>Confirm namespace discovery is successful. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Check the discovered hierarchy against expected parameter coverage</small> | <small>If all expected parameters exist PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 60: Validate TR-181 validate read-only set rejection for TELEMETRY.</strong></summary>

## Test Case 60: TDKB_DML_TR181_TELEMETRY_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the Telemetry module and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_34

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (TELEMETRY) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on read-only Device parameters under TELEMETRY to valid values through the TR181 path</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 61: Validate TR-181 validate write-access compliance for TELEMETRY.</strong></summary>

## Test Case 61: TDKB_DML_TR181_TELEMETRY_WriteAccessComplianceCheck

## Objectives
To check if write operations does not return the read-only error code for all parameters in Telemetry module which are writable.

## Test Case ID
TC_TDKB_DML_72

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (TELEMETRY) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform SET on writable Device parameters under TELEMETRY to current runtime value retrieved in previous step through the TR181 path</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 62: Validate TR-181 validate write-type compliance for TELEMETRY.</strong></summary>

## Test Case 62: TDKB_DML_TR181_TELEMETRY_WriteTypeComplianceCheck

## Objectives
To check if write operations return the expected error code for all writable parameters in TELEMETRY module using an invalid type.

## Test Case ID
TC_TDKB_DML_89

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (TELEMETRY) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on writable Device parameters under TELEMETRY using invalid data type to invalid-type values through the TR181 path</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 63: Validate TR-181 validate static table row add behavior for VLANMANAGER.</strong></summary>

## Test Case 63: TDKB_DML_TR181_VLANMANAGER_AddStaticTableRow

## Objectives
To check if adding rows to static table objects under VLANMANAGER module returns the expected error code.

## Test Case ID
TC_TDKB_DML_102

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables for the module on the target platform</small> | <small>Confirm at least one applicable table is selected for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform ADD on static table row under VLANMANAGER through the TR181 path</small> | <small>Verify add operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 64: Validate TR-181 validate static table row delete behavior for VLANMANAGER.</strong></summary>

## Test Case 64: TDKB_DML_TR181_VLANMANAGER_DeleteStaticTableRow

## Objectives
To check if deleting rows from static table objects under VLANMANAGER module returns the expected errorcode.

## Test Case ID
TC_TDKB_DML_111

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables and choose a candidate instance</small> | <small>Confirm table instance context is available for deletion attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform DELETE on static table row under VLANMANAGER through the TR181 path</small> | <small>Verify delete operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 65: Validate TR-181 get all parameter values for VLANMANAGER.</strong></summary>

## Test Case 65: TDKB_DML_TR181_VLANMANAGER_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the VLANMANAGER module and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_15

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for VLANMANAGER</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform GET on all applicable Device.* parameters under VLANMANAGER through the TR181 path</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 66: Validate TR-181 perform L2 set validations for VLANMANAGER.</strong></summary>

## Test Case 66: TDKB_DML_TR181_VLANMANAGER_L2SetValidations

## Objectives
To check if all the L2 SET operations are successful and to validate the corresponding use-cases under VLANMANAGER module.

## Test Case ID
TC_TDKB_DML_152

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device parameters under module scope (VLANMANAGER) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform GET on baseline values for L2-set parameters under VLANMANAGER through the TR181 path</small> | <small>Confirm baseline values are captured before the SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on L2-set parameters under VLANMANAGER to As per configuration through the TR181 path</small> | <small>Confirm parameter updates satisfy dependency and operational constraints. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Revert each modified parameter to original value</small> | <small>Verify revert operations succeed and final state is restored. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 67: Validate TR-181 verify parameter existence for VLANMANAGER.</strong></summary>

## Test Case 67: TDKB_DML_TR181_VLANMANAGER_ParameterExistenceCheck

## Objectives
To check if all the required namespaces under VLANMANAGER module exists.

## Test Case ID
TC_TDKB_DML_54

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform recursive parameter discovery from module root objects under VLANMANAGER</small> | <small>Confirm namespace discovery is successful. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Check the discovered hierarchy against expected parameter coverage</small> | <small>If all expected parameters exist PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 68: Validate TR-181 validate read-only set rejection for VLANMANAGER.</strong></summary>

## Test Case 68: TDKB_DML_TR181_VLANMANAGER_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the VLANMANAGER module and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_35

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (VLANMANAGER) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on read-only Device parameters under VLANMANAGER to valid values through the TR181 path</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 69: Validate TR-181 validate write-access compliance for VLANMANAGER.</strong></summary>

## Test Case 69: TDKB_DML_TR181_VLANMANAGER_WriteAccessComplianceCheck

## Objectives
To check if write operations does not return the read-only error code for all parameters in VlanManager module which are writable.

## Test Case ID
TC_TDKB_DML_73

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (VLANMANAGER) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform SET on writable Device parameters under VLANMANAGER to current runtime value retrieved in previous step through the TR181 path</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 70: Validate TR-181 validate write-type compliance for VLANMANAGER.</strong></summary>

## Test Case 70: TDKB_DML_TR181_VLANMANAGER_WriteTypeComplianceCheck

## Objectives
To check if write operations return the expected error code for all writable parameters in VLANMANAGER module using an invalid type.

## Test Case ID
TC_TDKB_DML_90

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (VLANMANAGER) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on writable Device parameters under VLANMANAGER using invalid data type to invalid-type values through the TR181 path</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 71: Validate TR-181 add and delete writable table rows for WANMANAGER.</strong></summary>

## Test Case 71: TDKB_DML_TR181_WANMANAGER_AddAndDeleteWritableTableRow

## Objectives
To check if adding a row to a non-rigid writable table object is success and all expected parameters under that table object instance should be created successfully for WANMANAGER module. Also check if the delete table row operation is success.

## Test Case ID
TC_TDKB_DML_140

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Child parameters of newly added table row under module scope (WANMANAGER) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform ADD on writable table row under WANMANAGER through the TR181 path</small> | <small>Confirm row addition succeeds and child parameters are present. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Set mandatory child parameters on the newly added instance to As per configuration</small> | <small>Confirm instance configuration is accepted. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform DELETE on added writable table row instance under WANMANAGER through the TR181 path</small> | <small>Verify deletion succeeds for the created instance. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 72: Validate TR-181 validate dynamic table row add behavior for WANMANAGER.</strong></summary>

## Test Case 72: TDKB_DML_TR181_WANMANAGER_AddDynamicTableRow

## Objectives
To check if adding rows to dynamic table objects under WANMANAGER module returns the expected error code.

## Test Case ID
TC_TDKB_DML_121

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables for the module on the target platform</small> | <small>Confirm dynamic tables are discovered for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform ADD on dynamic table row under WANMANAGER through the TR181 path</small> | <small>Verify add operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 73: Validate TR-181 validate static table row add behavior for WANMANAGER.</strong></summary>

## Test Case 73: TDKB_DML_TR181_WANMANAGER_AddStaticTableRow

## Objectives
To check if adding rows to static table objects under WANMANAGER module returns the expected error code.

## Test Case ID
TC_TDKB_DML_103

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables for the module on the target platform</small> | <small>Confirm at least one applicable table is selected for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform ADD on static table row under WANMANAGER through the TR181 path</small> | <small>Verify add operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 74: Validate TR-181 validate dynamic table row delete behavior for WANMANAGER.</strong></summary>

## Test Case 74: TDKB_DML_TR181_WANMANAGER_DeleteDynamicTableRow

## Objectives
To check if deleting rows from dynamic table objects under WANMANAGER module returns the expected errorcode.

## Test Case ID
TC_TDKB_DML_130

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables and candidate instance entries</small> | <small>Confirm delete preconditions are available for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform DELETE on dynamic table row under WANMANAGER through the TR181 path</small> | <small>Verify delete operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 75: Validate TR-181 validate static table row delete behavior for WANMANAGER.</strong></summary>

## Test Case 75: TDKB_DML_TR181_WANMANAGER_DeleteStaticTableRow

## Objectives
To check if deleting rows from static table objects under WANMANAGER module returns the expected errorcode.

## Test Case ID
TC_TDKB_DML_112

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables and choose a candidate instance</small> | <small>Confirm table instance context is available for deletion attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform DELETE on static table row under WANMANAGER through the TR181 path</small> | <small>Verify delete operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 76: Validate TR-181 get all parameter values for WANMANAGER.</strong></summary>

## Test Case 76: TDKB_DML_TR181_WANMANAGER_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the WANMANAGER module and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_16

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for WANMANAGER</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform GET on all applicable Device.* parameters under WANMANAGER through the TR181 path</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 77: Validate TR-181 perform L2 set validations for WANMANAGER.</strong></summary>

## Test Case 77: TDKB_DML_TR181_WANMANAGER_L2SetValidations

## Objectives
To check if all the L2 SET operations are successful and to validate the corresponding use-cases under Wan Manager module.

## Test Case ID
TC_TDKB_DML_154

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device parameters under module scope (WANMANAGER) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform GET on baseline values for L2-set parameters under WANMANAGER through the TR181 path</small> | <small>Confirm baseline values are captured before the SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on L2-set parameters under WANMANAGER to As per configuration through the TR181 path</small> | <small>Confirm parameter updates satisfy dependency and operational constraints. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Revert each modified parameter to original value</small> | <small>Verify revert operations succeed and final state is restored. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 78: Validate TR-181 verify parameter existence for WANMANAGER.</strong></summary>

## Test Case 78: TDKB_DML_TR181_WANMANAGER_ParameterExistenceCheck

## Objectives
To check if all the required namespaces under WANMANAGER module exists.

## Test Case ID
TC_TDKB_DML_55

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform recursive parameter discovery from module root objects under WANMANAGER</small> | <small>Confirm namespace discovery is successful. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Check the discovered hierarchy against expected parameter coverage</small> | <small>If all expected parameters exist PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 79: Validate TR-181 validate read-only set rejection for WANMANAGER.</strong></summary>

## Test Case 79: TDKB_DML_TR181_WANMANAGER_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the WANMANAGER module and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_36

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (WANMANAGER) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on read-only Device parameters under WANMANAGER to valid values through the TR181 path</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 80: Validate TR-181 validate write-access compliance for WANMANAGER.</strong></summary>

## Test Case 80: TDKB_DML_TR181_WANMANAGER_WriteAccessComplianceCheck

## Objectives
To check if write operations does not return the read-only error code for all parameters in WanManager module which are writable.

## Test Case ID
TC_TDKB_DML_74

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (WANMANAGER) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform SET on writable Device parameters under WANMANAGER to current runtime value retrieved in previous step through the TR181 path</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 81: Validate TR-181 validate write-type compliance for WANMANAGER.</strong></summary>

## Test Case 81: TDKB_DML_TR181_WANMANAGER_WriteTypeComplianceCheck

## Objectives
To check if write operations return the expected error code for all writable parameters in WANMANAGER module using an invalid type.

## Test Case ID
TC_TDKB_DML_91

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (WANMANAGER) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on writable Device parameters under WANMANAGER using invalid data type to invalid-type values through the TR181 path</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 82: Validate TR-181 add and delete dynamic writable table rows for WIFI.</strong></summary>

## Test Case 82: TDKB_DML_TR181_WIFI_AddAndDeleteDynamicWritableTableRow

## Objectives
To check if adding a row to a dynamic writable table object is success and all expected parameters under that table object instance should be created successfully for WIFI module. Also check if the delete operation is success.

## Test Case ID
TC_TDKB_DML_133

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Child parameters of newly added table row under module scope (WIFI) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform ADD on dynamic writable table row under WIFI through the TR181 path</small> | <small>Confirm row addition succeeds and new instance index is returned. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Set mandatory child parameters on the newly added instance to As per configuration</small> | <small>Confirm child parameters are present and configurable. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform DELETE on added dynamic writable table row instance under WIFI through the TR181 path</small> | <small>Verify deletion succeeds for the created instance. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 83: Validate TR-181 add and delete writable table rows for WIFI.</strong></summary>

## Test Case 83: TDKB_DML_TR181_WIFI_AddAndDeleteWritableTableRow

## Objectives
To check if adding a row to a non-rigid writable table object is success and all expected parameters under that table object instance should be created successfully for WIFI module. Also check if the delete table row operation is success.

## Test Case ID
TC_TDKB_DML_141

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Child parameters of newly added table row under module scope (WIFI) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform ADD on writable table row under WIFI through the TR181 path</small> | <small>Confirm row addition succeeds and child parameters are present. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Set mandatory child parameters on the newly added instance to As per configuration</small> | <small>Confirm instance configuration is accepted. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform DELETE on added writable table row instance under WIFI through the TR181 path</small> | <small>Verify deletion succeeds for the created instance. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 84: Validate TR-181 validate dynamic table row add behavior for WIFI.</strong></summary>

## Test Case 84: TDKB_DML_TR181_WIFI_AddDynamicTableRow

## Objectives
To check if adding rows to dynamic table objects under WIFI module returns the expected error code.

## Test Case ID
TC_TDKB_DML_122

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables for the module on the target platform</small> | <small>Confirm dynamic tables are discovered for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform ADD on dynamic table row under WIFI through the TR181 path</small> | <small>Verify add operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 85: Validate TR-181 validate static table row add behavior for WIFI.</strong></summary>

## Test Case 85: TDKB_DML_TR181_WIFI_AddStaticTableRow

## Objectives
To check if adding rows to static table objects under WIFI module returns the expected error code.

## Test Case ID
TC_TDKB_DML_104

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables for the module on the target platform</small> | <small>Confirm at least one applicable table is selected for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform ADD on static table row under WIFI through the TR181 path</small> | <small>Verify add operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 86: Validate TR-181 validate dynamic table row delete behavior for WIFI.</strong></summary>

## Test Case 86: TDKB_DML_TR181_WIFI_DeleteDynamicTableRow

## Objectives
To check if deleting rows from dynamic table objects under WIFI module returns the expected errorcode.

## Test Case ID
TC_TDKB_DML_131

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables and candidate instance entries</small> | <small>Confirm delete preconditions are available for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform DELETE on dynamic table row under WIFI through the TR181 path</small> | <small>Verify delete operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 87: Validate TR-181 validate static table row delete behavior for WIFI.</strong></summary>

## Test Case 87: TDKB_DML_TR181_WIFI_DeleteStaticTableRow

## Objectives
To check if deleting rows from static table objects under WIFI module returns the expected errorcode.

## Test Case ID
TC_TDKB_DML_113

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables and choose a candidate instance</small> | <small>Confirm table instance context is available for deletion attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform DELETE on static table row under WIFI through the TR181 path</small> | <small>Verify delete operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 88: Validate TR-181 get all parameter values for WIFI.</strong></summary>

## Test Case 88: TDKB_DML_TR181_WIFI_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the WIFI module and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_17

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for WIFI</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform GET on all applicable Device.* parameters under WIFI through the TR181 path</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 89: Validate TR-181 perform L2 set validations for WIFI.</strong></summary>

## Test Case 89: TDKB_DML_TR181_WIFI_L2SetValidations

## Objectives
To check if all the L2 SET operations are successful and to validate the corresponding use-cases under WIFI module.

## Test Case ID
TC_TDKB_DML_156

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device parameters under module scope (WIFI) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform GET on baseline values for L2-set parameters under WIFI through the TR181 path</small> | <small>Confirm baseline values are captured before the SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on L2-set parameters under WIFI to As per configuration through the TR181 path</small> | <small>Confirm parameter updates satisfy dependency and operational constraints. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Revert each modified parameter to original value</small> | <small>Verify revert operations succeed and final state is restored. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 90: Validate TR-181 verify parameter existence for WIFI.</strong></summary>

## Test Case 90: TDKB_DML_TR181_WIFI_ParameterExistenceCheck

## Objectives
To check if all the required namespaces under WIFI module exists.

## Test Case ID
TC_TDKB_DML_56

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform recursive parameter discovery from module root objects under WIFI</small> | <small>Confirm namespace discovery is successful. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Check the discovered hierarchy against expected parameter coverage</small> | <small>If all expected parameters exist PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 91: Validate TR-181 validate read-only set rejection for WIFI.</strong></summary>

## Test Case 91: TDKB_DML_TR181_WIFI_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the WIFI module and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_37

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (WIFI) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on read-only Device parameters under WIFI to valid values through the TR181 path</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 92: Validate TR-181 validate write-access compliance for WIFI.</strong></summary>

## Test Case 92: TDKB_DML_TR181_WIFI_WriteAccessComplianceCheck

## Objectives
To check if write operations does not return the read-only error code for all parameters in WIFI module which are writable.

## Test Case ID
TC_TDKB_DML_75

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (WIFI) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform SET on writable Device parameters under WIFI to current runtime value retrieved in previous step through the TR181 path</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 93: Validate TR-181 validate write-type compliance for WIFI.</strong></summary>

## Test Case 93: TDKB_DML_TR181_WIFI_WriteTypeComplianceCheck

## Objectives
To check if write operations return the expected error code for all writable parameters in WIFI module using an invalid type.

## Test Case ID
TC_TDKB_DML_92

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (WIFI) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on writable Device parameters under WIFI using invalid data type to invalid-type values through the TR181 path</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 94: Validate TR-181 add and delete dynamic writable table rows for XDNS.</strong></summary>

## Test Case 94: TDKB_DML_TR181_XDNS_AddAndDeleteDynamicWritableTableRow

## Objectives
To check if adding a row to a dynamic writable table object is success and all expected parameters under that table object instance should be created successfully for XDNS module. Also check if the delete operation is success.

## Test Case ID
TC_TDKB_DML_136

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Child parameters of newly added table row under module scope (XDNS) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform ADD on dynamic writable table row under XDNS through the TR181 path</small> | <small>Confirm row addition succeeds and new instance index is returned. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Set mandatory child parameters on the newly added instance to As per configuration</small> | <small>Confirm child parameters are present and configurable. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform DELETE on added dynamic writable table row instance under XDNS through the TR181 path</small> | <small>Verify deletion succeeds for the created instance. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 95: Validate TR-181 get all parameter values for XDNS.</strong></summary>

## Test Case 95: TDKB_DML_TR181_XDNS_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the XDNS module and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_18

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for XDNS</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform GET on all applicable Device.* parameters under XDNS through the TR181 path</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 96: Validate TR-181 perform L2 set validations for XDNS.</strong></summary>

## Test Case 96: TDKB_DML_TR181_XDNS_L2SetValidations

## Objectives
To check if all the L2 SET operations are successful and to validate the corresponding use-cases under XDNS module.

## Test Case ID
TC_TDKB_DML_153

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device parameters under module scope (XDNS) | As per configuration |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform GET on baseline values for L2-set parameters under XDNS through the TR181 path</small> | <small>Confirm baseline values are captured before the SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on L2-set parameters under XDNS to As per configuration through the TR181 path</small> | <small>Confirm parameter updates satisfy dependency and operational constraints. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Revert each modified parameter to original value</small> | <small>Verify revert operations succeed and final state is restored. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 97: Validate TR-181 verify parameter existence for XDNS.</strong></summary>

## Test Case 97: TDKB_DML_TR181_XDNS_ParameterExistenceCheck

## Objectives
To check if all the required namespaces under XDNS module exists.

## Test Case ID
TC_TDKB_DML_57

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Perform recursive parameter discovery from module root objects under XDNS</small> | <small>Confirm namespace discovery is successful. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Check the discovered hierarchy against expected parameter coverage</small> | <small>If all expected parameters exist PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 98: Validate TR-181 validate read-only set rejection for XDNS.</strong></summary>

## Test Case 98: TDKB_DML_TR181_XDNS_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the XDNS module and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_38

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (XDNS) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on read-only Device parameters under XDNS to valid values through the TR181 path</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 99: Validate TR-181 validate write-access compliance for XDNS.</strong></summary>

## Test Case 99: TDKB_DML_TR181_XDNS_WriteAccessComplianceCheck

## Objectives
To check if write operations does not return the read-only error code for all parameters in XDNS module which are writable.

## Test Case ID
TC_TDKB_DML_76

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (XDNS) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Perform SET on writable Device parameters under XDNS to current runtime value retrieved in previous step through the TR181 path</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 100: Validate TR-181 validate write-type compliance for XDNS.</strong></summary>

## Test Case 100: TDKB_DML_TR181_XDNS_WriteTypeComplianceCheck

## Objectives
To check if write operations return the expected error code for all writable parameters in XDNS module using an invalid type.

## Test Case ID
TC_TDKB_DML_93

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (XDNS) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Perform SET on writable Device parameters under XDNS using invalid data type to invalid-type values through the TR181 path</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

</details>

---

<details>
<summary><strong>WEBPA Validation</strong></summary>

# WEBPA Validation

<details>
<summary><strong>Test Case 101: Validate WEBPA get all parameter values for ADVSEC.</strong></summary>

## Test Case 101: TDKB_DML_WEBPA_ADVSEC_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the Advanced Security module using WebPA protocol and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_157

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for ADVSEC</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA GET request for all applicable Device.* parameters under ADVSEC to the WEBPA Server</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 102: Validate WEBPA validate read-only set rejection for ADVSEC.</strong></summary>

## Test Case 102: TDKB_DML_WEBPA_ADVSEC_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the Advanced Security module using WebPA protocol and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_175

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (ADVSEC) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for read-only Device parameters under ADVSEC to valid values to the WEBPA Server</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 103: Validate WEBPA validate write-access compliance for ADVSEC.</strong></summary>

## Test Case 103: TDKB_DML_WEBPA_ADVSEC_WriteAccessComplianceCheck

## Objectives
To check if write operations using WebPA protocol does not return the read-only error code for all parameters in Advanced Security module which are writable.

## Test Case ID
TC_TDKB_DML_193

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (ADVSEC) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Send a WEBPA SET request for writable Device parameters under ADVSEC to current runtime value retrieved in previous step to the WEBPA Server</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 104: Validate WEBPA validate write-type compliance for ADVSEC.</strong></summary>

## Test Case 104: TDKB_DML_WEBPA_ADVSEC_WriteTypeComplianceCheck

## Objectives
To check if write operations via WebPA protocol return the expected error code for all writable parameters in Advanced Security module using an invalid type.

## Test Case ID
TC_TDKB_DML_211

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (ADVSEC) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for writable Device parameters under ADVSEC using invalid data type to invalid-type values to the WEBPA Server</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 105: Validate WEBPA get all parameter values for CR.</strong></summary>

## Test Case 105: TDKB_DML_WEBPA_CR_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the Component Registry module using WebPA protocol and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_159

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for CR</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA GET request for all applicable Device.* parameters under CR to the WEBPA Server</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 106: Validate WEBPA validate read-only set rejection for CR.</strong></summary>

## Test Case 106: TDKB_DML_WEBPA_CR_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the Component Registry module using WebPA protocol and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_177

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (CR) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for read-only Device parameters under CR to valid values to the WEBPA Server</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 107: Validate WEBPA validate write-access compliance for CR.</strong></summary>

## Test Case 107: TDKB_DML_WEBPA_CR_WriteAccessComplianceCheck

## Objectives
To check if write operations using WebPA protocol does not return the read-only error code for all parameters in Component Registry module which are writable.

## Test Case ID
TC_TDKB_DML_195

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (CR) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Send a WEBPA SET request for writable Device parameters under CR to current runtime value retrieved in previous step to the WEBPA Server</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 108: Validate WEBPA validate write-type compliance for CR.</strong></summary>

## Test Case 108: TDKB_DML_WEBPA_CR_WriteTypeComplianceCheck

## Objectives
To check if write operations via WebPA protocol return the expected error code for all writable parameters in Component Registry module using an invalid type.

## Test Case ID
TC_TDKB_DML_213

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (CR) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for writable Device parameters under CR using invalid data type to invalid-type values to the WEBPA Server</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 109: Validate WEBPA validate dynamic table row add behavior for ETHAGENT.</strong></summary>

## Test Case 109: TDKB_DML_WEBPA_ETHAGENT_AddDynamicTableRow

## Objectives
To check if adding rows to dynamic table objects under EthAgent module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_237

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables for the module on the target platform</small> | <small>Confirm dynamic tables are discovered for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA ADD request for dynamic table row under ETHAGENT to the WEBPA Server</small> | <small>Verify add operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 110: Validate WEBPA validate static table row add behavior for ETHAGENT.</strong></summary>

## Test Case 110: TDKB_DML_WEBPA_ETHAGENT_AddStaticTableRow

## Objectives
To check if adding rows to static table objects under ETHAGENT module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_229

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables for the module on the target platform</small> | <small>Confirm at least one applicable table is selected for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA ADD request for static table row under ETHAGENT to the WEBPA Server</small> | <small>Verify add operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 111: Validate WEBPA validate dynamic table row delete behavior for ETHAGENT.</strong></summary>

## Test Case 111: TDKB_DML_WEBPA_ETHAGENT_DeleteDynamicTableRow

## Objectives
To check if deleting rows from dynamic table objects under ETHAGENT module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_253

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables and candidate instance entries</small> | <small>Confirm delete preconditions are available for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA DELETE request for dynamic table row under ETHAGENT to the WEBPA Server</small> | <small>Verify delete operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 112: Validate WEBPA validate static table row delete behavior for ETHAGENT.</strong></summary>

## Test Case 112: TDKB_DML_WEBPA_ETHAGENT_DeleteStaticTableRow

## Objectives
To check if deleting rows from static table objects under ETHAGENT module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_245

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables and choose a candidate instance</small> | <small>Confirm table instance context is available for deletion attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA DELETE request for static table row under ETHAGENT to the WEBPA Server</small> | <small>Verify delete operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 113: Validate WEBPA get all parameter values for ETHAGENT.</strong></summary>

## Test Case 113: TDKB_DML_WEBPA_ETHAGENT_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the EthAgent module using WebPA protocol and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_160

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for ETHAGENT</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA GET request for all applicable Device.* parameters under ETHAGENT to the WEBPA Server</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 114: Validate WEBPA validate read-only set rejection for ETHAGENT.</strong></summary>

## Test Case 114: TDKB_DML_WEBPA_ETHAGENT_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the Ethernet Agent module using WebPA protocol and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_178

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (ETHAGENT) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for read-only Device parameters under ETHAGENT to valid values to the WEBPA Server</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 115: Validate WEBPA validate write-access compliance for ETHAGENT.</strong></summary>

## Test Case 115: TDKB_DML_WEBPA_ETHAGENT_WriteAccessComplianceCheck

## Objectives
To check if write operations using WebPA protocol does not return the read-only error code for all parameters in Ethernet Agent module which are writable.

## Test Case ID
TC_TDKB_DML_196

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (ETHAGENT) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Send a WEBPA SET request for writable Device parameters under ETHAGENT to current runtime value retrieved in previous step to the WEBPA Server</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 116: Validate WEBPA validate write-type compliance for ETHAGENT.</strong></summary>

## Test Case 116: TDKB_DML_WEBPA_ETHAGENT_WriteTypeComplianceCheck

## Objectives
To check if write operations via WebPA protocol return the expected error code for all writable parameters in Ethernet Agent module using an invalid type.

## Test Case ID
TC_TDKB_DML_214

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (ETHAGENT) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for writable Device parameters under ETHAGENT using invalid data type to invalid-type values to the WEBPA Server</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 117: Validate WEBPA validate dynamic table row add behavior for LMLITE.</strong></summary>

## Test Case 117: TDKB_DML_WEBPA_LMLITE_AddDynamicTableRow

## Objectives
To check if adding rows to dynamic table objects under LMLite module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_239

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables for the module on the target platform</small> | <small>Confirm dynamic tables are discovered for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA ADD request for dynamic table row under LMLITE to the WEBPA Server</small> | <small>Verify add operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 118: Validate WEBPA validate static table row add behavior for LMLITE.</strong></summary>

## Test Case 118: TDKB_DML_WEBPA_LMLITE_AddStaticTableRow

## Objectives
To check if adding rows to static table objects under LMLITE module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_230

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables for the module on the target platform</small> | <small>Confirm at least one applicable table is selected for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA ADD request for static table row under LMLITE to the WEBPA Server</small> | <small>Verify add operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 119: Validate WEBPA validate dynamic table row delete behavior for LMLITE.</strong></summary>

## Test Case 119: TDKB_DML_WEBPA_LMLITE_DeleteDynamicTableRow

## Objectives
To check if deleting rows from dynamic table objects under LMLITE module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_255

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables and candidate instance entries</small> | <small>Confirm delete preconditions are available for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA DELETE request for dynamic table row under LMLITE to the WEBPA Server</small> | <small>Verify delete operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 120: Validate WEBPA validate static table row delete behavior for LMLITE.</strong></summary>

## Test Case 120: TDKB_DML_WEBPA_LMLITE_DeleteStaticTableRow

## Objectives
To check if deleting rows from static table objects under LMLITE module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_246

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables and choose a candidate instance</small> | <small>Confirm table instance context is available for deletion attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA DELETE request for static table row under LMLITE to the WEBPA Server</small> | <small>Verify delete operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 121: Validate WEBPA get all parameter values for LMLITE.</strong></summary>

## Test Case 121: TDKB_DML_WEBPA_LMLITE_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the LMLITE module using WebPA protocol and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_163

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for LMLITE</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA GET request for all applicable Device.* parameters under LMLITE to the WEBPA Server</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 122: Validate WEBPA validate read-only set rejection for LMLITE.</strong></summary>

## Test Case 122: TDKB_DML_WEBPA_LMLITE_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the LMLite module using WebPA protocol and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_181

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (LMLITE) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for read-only Device parameters under LMLITE to valid values to the WEBPA Server</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 123: Validate WEBPA validate write-access compliance for LMLITE.</strong></summary>

## Test Case 123: TDKB_DML_WEBPA_LMLITE_WriteAccessComplianceCheck

## Objectives
To check if write operations using WebPA protocol does not return the read-only error code for all parameters in LMLite module which are writable.

## Test Case ID
TC_TDKB_DML_199

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (LMLITE) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Send a WEBPA SET request for writable Device parameters under LMLITE to current runtime value retrieved in previous step to the WEBPA Server</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 124: Validate WEBPA validate write-type compliance for LMLITE.</strong></summary>

## Test Case 124: TDKB_DML_WEBPA_LMLITE_WriteTypeComplianceCheck

## Objectives
To check if write operations via WebPA protocol return the expected error code for all writable parameters in LMLite module using an invalid type.

## Test Case ID
TC_TDKB_DML_217

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (LMLITE) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for writable Device parameters under LMLITE using invalid data type to invalid-type values to the WEBPA Server</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 125: Validate WEBPA validate dynamic table row add behavior for PAM.</strong></summary>

## Test Case 125: TDKB_DML_WEBPA_PAM_AddDynamicTableRow

## Objectives
To check if adding rows to dynamic table objects under PAM module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_242

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables for the module on the target platform</small> | <small>Confirm dynamic tables are discovered for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA ADD request for dynamic table row under PAM to the WEBPA Server</small> | <small>Verify add operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 126: Validate WEBPA validate static table row add behavior for PAM.</strong></summary>

## Test Case 126: TDKB_DML_WEBPA_PAM_AddStaticTableRow

## Objectives
To check if adding rows to static table objects under PAM module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_233

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables for the module on the target platform</small> | <small>Confirm at least one applicable table is selected for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA ADD request for static table row under PAM to the WEBPA Server</small> | <small>Verify add operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 127: Validate WEBPA validate dynamic table row delete behavior for PAM.</strong></summary>

## Test Case 127: TDKB_DML_WEBPA_PAM_DeleteDynamicTableRow

## Objectives
To check if deleting rows from dynamic table objects under PAM module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_258

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables and candidate instance entries</small> | <small>Confirm delete preconditions are available for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA DELETE request for dynamic table row under PAM to the WEBPA Server</small> | <small>Verify delete operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 128: Validate WEBPA validate static table row delete behavior for PAM.</strong></summary>

## Test Case 128: TDKB_DML_WEBPA_PAM_DeleteStaticTableRow

## Objectives
To check if deleting rows from static table objects under PAM module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_249

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables and choose a candidate instance</small> | <small>Confirm table instance context is available for deletion attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA DELETE request for static table row under PAM to the WEBPA Server</small> | <small>Verify delete operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 129: Validate WEBPA get all parameter values for PAM.</strong></summary>

## Test Case 129: TDKB_DML_WEBPA_PAM_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the PAM module using WebPA protocol and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_169

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for PAM</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA GET request for all applicable Device.* parameters under PAM to the WEBPA Server</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 130: Validate WEBPA validate read-only set rejection for PAM.</strong></summary>

## Test Case 130: TDKB_DML_WEBPA_PAM_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the PAM module using WebPA protocol and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_187

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (PAM) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for read-only Device parameters under PAM to valid values to the WEBPA Server</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 131: Validate WEBPA validate write-access compliance for PAM.</strong></summary>

## Test Case 131: TDKB_DML_WEBPA_PAM_WriteAccessComplianceCheck

## Objectives
To check if write operations using WebPA protocol does not return the read-only error code for all parameters in PAM module which are writable.

## Test Case ID
TC_TDKB_DML_205

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (PAM) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Send a WEBPA SET request for writable Device parameters under PAM to current runtime value retrieved in previous step to the WEBPA Server</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 132: Validate WEBPA validate write-type compliance for PAM.</strong></summary>

## Test Case 132: TDKB_DML_WEBPA_PAM_WriteTypeComplianceCheck

## Objectives
To check if write operations via WebPA protocol return the expected error code for all writable parameters in PAM module using an invalid type.

## Test Case ID
TC_TDKB_DML_223

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (PAM) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for writable Device parameters under PAM using invalid data type to invalid-type values to the WEBPA Server</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 133: Validate WEBPA validate dynamic table row add behavior for TDM.</strong></summary>

## Test Case 133: TDKB_DML_WEBPA_TDM_AddDynamicTableRow

## Objectives
To check if adding rows to dynamic table objects under Test and Diagnostics module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_243

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables for the module on the target platform</small> | <small>Confirm dynamic tables are discovered for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA ADD request for dynamic table row under TDM to the WEBPA Server</small> | <small>Verify add operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 134: Validate WEBPA validate static table row add behavior for TDM.</strong></summary>

## Test Case 134: TDKB_DML_WEBPA_TDM_AddStaticTableRow

## Objectives
To check if adding rows to static table objects under TDM module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_234

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables for the module on the target platform</small> | <small>Confirm at least one applicable table is selected for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA ADD request for static table row under TDM to the WEBPA Server</small> | <small>Verify add operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 135: Validate WEBPA validate dynamic table row delete behavior for TDM.</strong></summary>

## Test Case 135: TDKB_DML_WEBPA_TDM_DeleteDynamicTableRow

## Objectives
To check if deleting rows from dynamic table objects under TDM module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_259

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables and candidate instance entries</small> | <small>Confirm delete preconditions are available for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA DELETE request for dynamic table row under TDM to the WEBPA Server</small> | <small>Verify delete operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 136: Validate WEBPA validate static table row delete behavior for TDM.</strong></summary>

## Test Case 136: TDKB_DML_WEBPA_TDM_DeleteStaticTableRow

## Objectives
To check if deleting rows from static table objects under TDM module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_250

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables and choose a candidate instance</small> | <small>Confirm table instance context is available for deletion attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA DELETE request for static table row under TDM to the WEBPA Server</small> | <small>Verify delete operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 137: Validate WEBPA get all parameter values for TDM.</strong></summary>

## Test Case 137: TDKB_DML_WEBPA_TDM_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the TDM module using WebPA protocol and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_170

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for TDM</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA GET request for all applicable Device.* parameters under TDM to the WEBPA Server</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 138: Validate WEBPA validate read-only set rejection for TDM.</strong></summary>

## Test Case 138: TDKB_DML_WEBPA_TDM_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the Test and Diagnostic module using WebPA protocol and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_188

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (TDM) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for read-only Device parameters under TDM to valid values to the WEBPA Server</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 139: Validate WEBPA validate write-access compliance for TDM.</strong></summary>

## Test Case 139: TDKB_DML_WEBPA_TDM_WriteAccessComplianceCheck

## Objectives
To check if write operations using WebPA protocol does not return the read-only error code for all parameters in Test and Diagnostic module which are writable.

## Test Case ID
TC_TDKB_DML_206

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (TDM) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Send a WEBPA SET request for writable Device parameters under TDM to current runtime value retrieved in previous step to the WEBPA Server</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 140: Validate WEBPA validate write-type compliance for TDM.</strong></summary>

## Test Case 140: TDKB_DML_WEBPA_TDM_WriteTypeComplianceCheck

## Objectives
To check if write operations via WebPA protocol return the expected error code for all writable parameters in Test and Diagnostics module using an invalid type.

## Test Case ID
TC_TDKB_DML_224

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (TDM) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for writable Device parameters under TDM using invalid data type to invalid-type values to the WEBPA Server</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 141: Validate WEBPA get all parameter values for TELEMETRY.</strong></summary>

## Test Case 141: TDKB_DML_WEBPA_TELEMETRY_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the TELEMETRY module using WebPA protocol and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_171

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for TELEMETRY</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA GET request for all applicable Device.* parameters under TELEMETRY to the WEBPA Server</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 142: Validate WEBPA validate read-only set rejection for TELEMETRY.</strong></summary>

## Test Case 142: TDKB_DML_WEBPA_TELEMETRY_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the Telemetry module using WebPA protocol and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_189

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (TELEMETRY) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for read-only Device parameters under TELEMETRY to valid values to the WEBPA Server</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 143: Validate WEBPA validate write-access compliance for TELEMETRY.</strong></summary>

## Test Case 143: TDKB_DML_WEBPA_TELEMETRY_WriteAccessComplianceCheck

## Objectives
To check if write operations using WebPA protocol does not return the read-only error code for all parameters in Telemetry module which are writable.

## Test Case ID
TC_TDKB_DML_207

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (TELEMETRY) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Send a WEBPA SET request for writable Device parameters under TELEMETRY to current runtime value retrieved in previous step to the WEBPA Server</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 144: Validate WEBPA validate write-type compliance for TELEMETRY.</strong></summary>

## Test Case 144: TDKB_DML_WEBPA_TELEMETRY_WriteTypeComplianceCheck

## Objectives
To check if write operations via WebPA protocol return the expected error code for all writable parameters in Telemetry module using an invalid type.

## Test Case ID
TC_TDKB_DML_225

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (TELEMETRY) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for writable Device parameters under TELEMETRY using invalid data type to invalid-type values to the WEBPA Server</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 145: Validate WEBPA validate static table row add behavior for VLANMANAGER.</strong></summary>

## Test Case 145: TDKB_DML_WEBPA_VLANMANAGER_AddStaticTableRow

## Objectives
To check if adding rows to static table objects under VLANMANAGER module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_235

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables for the module on the target platform</small> | <small>Confirm at least one applicable table is selected for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA ADD request for static table row under VLANMANAGER to the WEBPA Server</small> | <small>Verify add operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 146: Validate WEBPA validate static table row delete behavior for VLANMANAGER.</strong></summary>

## Test Case 146: TDKB_DML_WEBPA_VLANMANAGER_DeleteStaticTableRow

## Objectives
To check if deleting rows from static table objects under VLANMANAGER module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_251

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables and choose a candidate instance</small> | <small>Confirm table instance context is available for deletion attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA DELETE request for static table row under VLANMANAGER to the WEBPA Server</small> | <small>Verify delete operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 147: Validate WEBPA get all parameter values for VLANMANAGER.</strong></summary>

## Test Case 147: TDKB_DML_WEBPA_VLANMANAGER_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the VLANMANAGER module using WebPA protocol and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_172

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for VLANMANAGER</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA GET request for all applicable Device.* parameters under VLANMANAGER to the WEBPA Server</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 148: Validate WEBPA validate read-only set rejection for VLANMANAGER.</strong></summary>

## Test Case 148: TDKB_DML_WEBPA_VLANMANAGER_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the Vlan Manager module using WebPA protocol and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_190

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (VLANMANAGER) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for read-only Device parameters under VLANMANAGER to valid values to the WEBPA Server</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 149: Validate WEBPA validate write-access compliance for VLANMANAGER.</strong></summary>

## Test Case 149: TDKB_DML_WEBPA_VLANMANAGER_WriteAccessComplianceCheck

## Objectives
To check if write operations using WebPA protocol does not return the read-only error code for all parameters in Vlan Manager module which are writable.

## Test Case ID
TC_TDKB_DML_208

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (VLANMANAGER) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Send a WEBPA SET request for writable Device parameters under VLANMANAGER to current runtime value retrieved in previous step to the WEBPA Server</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 150: Validate WEBPA validate write-type compliance for VLANMANAGER.</strong></summary>

## Test Case 150: TDKB_DML_WEBPA_VLANMANAGER_WriteTypeComplianceCheck

## Objectives
To check if write operations via WebPA protocol return the expected error code for all writable parameters in Vlan Manager module using an invalid type.

## Test Case ID
TC_TDKB_DML_226

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (VLANMANAGER) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for writable Device parameters under VLANMANAGER using invalid data type to invalid-type values to the WEBPA Server</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 151: Validate WEBPA validate dynamic table row add behavior for WANMANAGER.</strong></summary>

## Test Case 151: TDKB_DML_WEBPA_WANMANAGER_AddDynamicTableRow

## Objectives
To check if adding rows to dynamic table objects under Wan Manager module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_244

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables for the module on the target platform</small> | <small>Confirm dynamic tables are discovered for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA ADD request for dynamic table row under WANMANAGER to the WEBPA Server</small> | <small>Verify add operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 152: Validate WEBPA validate static table row add behavior for WANMANAGER.</strong></summary>

## Test Case 152: TDKB_DML_WEBPA_WANMANAGER_AddStaticTableRow

## Objectives
To check if adding rows to static table objects under WANMANAGER module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_236

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables for the module on the target platform</small> | <small>Confirm at least one applicable table is selected for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA ADD request for static table row under WANMANAGER to the WEBPA Server</small> | <small>Verify add operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 153: Validate WEBPA validate dynamic table row delete behavior for WANMANAGER.</strong></summary>

## Test Case 153: TDKB_DML_WEBPA_WANMANAGER_DeleteDynamicTableRow

## Objectives
To check if deleting rows from dynamic table objects under WANMANAGER module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_260

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable dynamic tables and candidate instance entries</small> | <small>Confirm delete preconditions are available for validation. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA DELETE request for dynamic table row under WANMANAGER to the WEBPA Server</small> | <small>Verify delete operation is rejected with expected dynamic-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 154: Validate WEBPA validate static table row delete behavior for WANMANAGER.</strong></summary>

## Test Case 154: TDKB_DML_WEBPA_WANMANAGER_DeleteStaticTableRow

## Objectives
To check if deleting rows from static table objects under WANMANAGER module using WebPA protocol returns the expected error code.

## Test Case ID
TC_TDKB_DML_252

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable static tables and choose a candidate instance</small> | <small>Confirm table instance context is available for deletion attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA DELETE request for static table row under WANMANAGER to the WEBPA Server</small> | <small>Verify delete operation is rejected with expected static-table restriction behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 155: Validate WEBPA get all parameter values for WANMANAGER.</strong></summary>

## Test Case 155: TDKB_DML_WEBPA_WANMANAGER_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the WANMANAGER module using WebPA protocol and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_173

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for WANMANAGER</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA GET request for all applicable Device.* parameters under WANMANAGER to the WEBPA Server</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 156: Validate WEBPA validate read-only set rejection for WANMANAGER.</strong></summary>

## Test Case 156: TDKB_DML_WEBPA_WANMANAGER_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the Wan Manager module using WebPA protocol and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_191

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (WANMANAGER) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for read-only Device parameters under WANMANAGER to valid values to the WEBPA Server</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 157: Validate WEBPA validate write-access compliance for WANMANAGER.</strong></summary>

## Test Case 157: TDKB_DML_WEBPA_WANMANAGER_WriteAccessComplianceCheck

## Objectives
To check if write operations using WebPA protocol does not return the read-only error code for all parameters in Wan Manager module which are writable.

## Test Case ID
TC_TDKB_DML_209

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (WANMANAGER) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Send a WEBPA SET request for writable Device parameters under WANMANAGER to current runtime value retrieved in previous step to the WEBPA Server</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 158: Validate WEBPA validate write-type compliance for WANMANAGER.</strong></summary>

## Test Case 158: TDKB_DML_WEBPA_WANMANAGER_WriteTypeComplianceCheck

## Objectives
To check if write operations via WebPA protocol return the expected error code for all writable parameters in Wan Manager module using an invalid type.

## Test Case ID
TC_TDKB_DML_227

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (WANMANAGER) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for writable Device parameters under WANMANAGER using invalid data type to invalid-type values to the WEBPA Server</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 159: Validate WEBPA get all parameter values for XDNS.</strong></summary>

## Test Case 159: TDKB_DML_WEBPA_XDNS_GetAllParameterValues

## Objectives
To get the value of all TR-181 DML parameters under the XDNS module using WebPA protocol and check if the value retrieved is from the expected values and if they are type compliant.

## Test Case ID
TC_TDKB_DML_174

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
None

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Identify applicable Device.* parameter namespaces for XDNS</small> | <small>Confirm namespace scope is available for the platform. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA GET request for all applicable Device.* parameters under XDNS to the WEBPA Server</small> | <small>Validate each returned value for type compliance and expected GET behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 160: Validate WEBPA validate read-only set rejection for XDNS.</strong></summary>

## Test Case 160: TDKB_DML_WEBPA_XDNS_SetReadOnlyParameters

## Objectives
To set all "read-only" TR-181 DML parameters under the XDNS module using WebPA protocol and check if the set operation returns the read-only error code.

## Test Case ID
TC_TDKB_DML_192

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Read-only Device parameters under module scope (XDNS) |valid values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Capture current value of each target read-only parameter</small> | <small>Confirm values are retrievable before mutation attempt. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for read-only Device parameters under XDNS to valid values to the WEBPA Server</small> | <small>Verify each SET attempt is rejected with expected read-only error behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 161: Validate WEBPA validate write-access compliance for XDNS.</strong></summary>

## Test Case 161: TDKB_DML_WEBPA_XDNS_WriteAccessComplianceCheck

## Objectives
To check if write operations using WebPA protocol does not return the read-only error code for all parameters in XDNS module which are writable.

## Test Case ID
TC_TDKB_DML_210

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (XDNS) | Current runtime value retrieved by GET in test step |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-access compliance</small> | <small>Confirm target list is prepared for execution. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Get current runtime value of each writable parameter</small> | <small>Confirm the current value is retrieved for SET operation. If the condition is met CONTINUE, else FAIL</small> |
| 3 | <small>Send a WEBPA SET request for writable Device parameters under XDNS to current runtime value retrieved in previous step to the WEBPA Server</small> | <small>Verify writable parameters do not return read-only rejection behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

<details>
<summary><strong>Test Case 162: Validate WEBPA validate write-type compliance for XDNS.</strong></summary>

## Test Case 162: TDKB_DML_WEBPA_XDNS_WriteTypeComplianceCheck

## Objectives
To check if write operations via WebPA protocol return the expected error code for all writable parameters in XDNS module using an invalid type.

## Test Case ID
TC_TDKB_DML_228

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA server - Request routing endpoint for WebPA operations |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Writable Device parameters under module scope (XDNS) | invalid-type values |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Select writable parameters mapped for write-type validation</small> | <small>Confirm targets and invalid type inputs are prepared. If the condition is met CONTINUE, else FAIL</small> |
| 2 | <small>Send a WEBPA SET request for writable Device parameters under XDNS using invalid data type to invalid-type values to the WEBPA Server</small> | <small>Verify each request fails with expected type-mismatch behavior. If the condition is met PASS, else FAIL</small> |
</details>

---

</details>

---



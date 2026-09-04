
# Device Management Validation Suite

## Test Specification Document for Device Management Validation Suite 

<strong>Version</strong>: 1.0<br>
<strong>Date</strong>: August 2026<br>
<strong>Purpose</strong>: Low-level test specification for Device Management WEBPA, USP, TR069, RFC, WEBCONFIG<br>
<strong>Maintained by</strong>: TDKB Test Automation Team

### Table of Contents

| # | Feature Name | Description | Number of Tests |
| ---- | ------- | ----------- | :---: |
| 1 | WebPA | WebPA device management | 05 |
| 2 | USP | USP (TR-369) device management | 29 |
| 3 | TR069 | CWMP / ACS device management | 11 |
| 4 | RFC (remote feature control) | Runtime enable/disable via xConf | 4 |
| 5 | WebConfig | WebConfig based device configuration | 15 |

---
<details open>
<summary><strong>WebPA</strong></summary>

# WebPA

<details open>
<summary><strong>Test Case 1: Toggle 2.4GHz MAC Filter Enable via WebPA</strong></summary>

## Test Case 1: TS_WEBPA_2.4GHzMACFilterEnable

### Objectives
Using WEBPA, get and set the state of MAC Filter for 2.4GHz.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA Server - Remote Feature Control communication server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.AccessPoint.10001.X_CISCO_COM_MACFilter.Enable | [true,false] |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that parodus and webpa processes are running on the DUT</small> | <small>Check if both parodus and webpa processes are up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Send a WEBPA GET request for Device.WiFi.AccessPoint.10001.X_CISCO_COM_MACFilter.Enable to the WEBPA Server.</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Check if the WEBPA GET response status is SUCCESS and the value returned is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a WEBPA SET request for Device.WiFi.AccessPoint.10001.X_CISCO_COM_MACFilter.Enable with the toggled value to the WEBPA Server. Wait for 30 seconds after the SET operation.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the WEBPA SET response status is SUCCESS. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a WEBPA GET request for Device.WiFi.AccessPoint.10001.X_CISCO_COM_MACFilter.Enable to the WEBPA Server to verify the toggled value.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the WEBPA GET response status is SUCCESS and the value matches the toggled value. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Send a WEBPA SET request for Device.WiFi.AccessPoint.10001.X_CISCO_COM_MACFilter.Enable to revert it to its original value to the WEBPA Server.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Check if the WEBPA SET revert response status is SUCCESS. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details open>
<summary><strong>Test Case 2: Toggle 5GHz MAC Filter Enable via WebPA</strong></summary>

## Test Case 2: TS_WEBPA_5GHzMACFilterEnable

### Objectives
Using WEBPA, get and set the state of MAC Filter for 5GHz.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA Server - Remote Feature Control communication server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.AccessPoint.10002.X_CISCO_COM_MACFilter.Enable | [true,false] |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that parodus and webpa processes are running on the DUT</small> | <small>Check if both parodus and webpa processes are up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Send a WEBPA GET request for Device.WiFi.AccessPoint.10002.X_CISCO_COM_MACFilter.Enable to the WEBPA Server.</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Check if the WEBPA GET response status is SUCCESS and the value returned is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a WEBPA SET request for Device.WiFi.AccessPoint.10002.X_CISCO_COM_MACFilter.Enable with the toggled value to the WEBPA Server. Wait for 30 seconds after the SET operation.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the WEBPA SET response status is SUCCESS. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a WEBPA GET request for Device.WiFi.AccessPoint.10002.X_CISCO_COM_MACFilter.Enable to the WEBPA Server to verify the toggled value.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the WEBPA GET response status is SUCCESS and the value matches the toggled value. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Send a WEBPA SET request for Device.WiFi.AccessPoint.10002.X_CISCO_COM_MACFilter.Enable to revert it to its original value to the WEBPA Server.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Check if the WEBPA SET revert response status is SUCCESS. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 3: Toggle 5GHz SSID Advertisement Enable via WebPA</strong></summary>

## Test Case 3: TS_WEBPA_5GHzSSIDAdvertisementEnabled

### Objectives
Using WEBPA, get and set the state of 5GHz SSID advertisement.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA Server - Remote Feature Control communication server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.AccessPoint.10101.SSIDAdvertisementEnabled | [true,false] |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that parodus and webpa processes are running on the DUT</small> | <small>Check if both parodus and webpa processes are up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Send a WEBPA GET request for Device.WiFi.AccessPoint.10101.SSIDAdvertisementEnabled to the WEBPA Server.</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Check if the WEBPA GET response status is SUCCESS and the value returned is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a WEBPA SET request for Device.WiFi.AccessPoint.10101.SSIDAdvertisementEnabled with the toggled value to the WEBPA Server. Wait for 30 seconds after the SET operation.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the WEBPA SET response status is SUCCESS. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a WEBPA GET request for Device.WiFi.AccessPoint.10101.SSIDAdvertisementEnabled to the WEBPA Server to verify the toggled value.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the WEBPA GET response status is SUCCESS and the value matches the toggled value. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Send a WEBPA SET request for Device.WiFi.AccessPoint.10101.SSIDAdvertisementEnabled to revert it to its original value to the WEBPA Server.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Check if the WEBPA SET revert response status is SUCCESS. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 4: Verify Last Reboot Reason after WebPA-Triggered Reboot</strong></summary>

## Test Case 4: TS_WEBPA_GetLastRebootReason

### Objectives
Get the last reboot reason after triggering a reboot via WEBPA and verify it is 'webpa-reboot'.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA Server - Remote Feature Control communication server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.RebootDevice | Device |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that parodus and webpa processes are running on the DUT</small> | <small>Check if both parodus and webpa processes are up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Send a WEBPA SET request for Device.X_CISCO_COM_DeviceControl.RebootDevice with value 'Device' to the WEBPA Server to trigger a reboot.</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Check if the WEBPA SET response status is SUCCESS. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a WEBPA GET request for Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason to the WEBPA Server.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the WEBPA GET response status is SUCCESS and the last reboot reason returned is 'webpa-reboot'. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 5: Verify Band Steering Capability Cannot Be Set to False via WebPA</strong></summary>

## Test Case 5: TS_WEBPA_SetBandSteeringCapability

### Objectives
To check if setting Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability to false returns failure.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WebPA Server - Remote Feature Control communication server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability | false |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that parodus and webpa processes are running on the DUT</small> | <small>Check if both parodus and webpa processes are up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Send a WEBPA GET request for Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability to the WEBPA Server.</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Check if the WEBPA GET response status is SUCCESS. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a WEBPA SET request for Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability with value 'false' to the WEBPA Server.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the WEBPA SET response returns FAILURE with status code 520, indicating that setting Capability to false is not allowed. If the condition is met PASS, else FAIL.</small> |


</details>

---

</details>

---
<details open>
<summary><strong>USP</strong></summary>

# USP

<details open>
<summary><strong>Test Case 6: Add and Delete USP Subscription with allow_partial as false</strong></summary>

## Test Case 6: TS_USPPA_AddDelete_ValidSubscription_allowpartial_false

### Objectives
To send an ADD message to add a valid agent subscription and a DELETE message to delete the subscription with allow_partial set to false and receive a valid response via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usp process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP ADD request for Device.LocalAgent.Subscription. with allow_partial set to false to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP ADD request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed ADD response contains a valid instance number and parameter list for the newly created subscription. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Send a USP GET request for the newly created Device.LocalAgent.Subscription.{i}. instance to the USP Controller.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Check if the USP GET request returns HTTP status 200 and the response contains valid parameter values for the subscription instance. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Send a USP DELETE request for Device.LocalAgent.Subscription.{i}. with allow_partial set to false to the USP Controller.</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Check if the USP DELETE request returns HTTP status 200 and the parsed response confirms the subscription instance was deleted successfully. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 7: Add and Delete USP Subscription with allow_partial=true</strong></summary>

## Test Case 7: TS_USPPA_AddDelete_ValidSubscription_allowpartial_true

### Objectives
To send an ADD message to add a valid agent subscription and a DELETE message to delete the subscription with allow_partial set to true and receive a valid response via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP ADD request for Device.LocalAgent.Subscription. with allow_partial set to true to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP ADD request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed ADD response contains a valid instance number and parameter list for the newly created subscription. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Send a USP GET request for the newly created Device.LocalAgent.Subscription.{i}. instance to the USP Controller.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Check if the USP GET request returns HTTP status 200 and the response contains valid parameter values for the subscription instance. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Send a USP DELETE request for Device.LocalAgent.Subscription.{i}. with allow_partial set to true to the USP Controller.</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Check if the USP DELETE request returns HTTP status 200 and the parsed response confirms the subscription instance was deleted successfully. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 8: Delete Non-Existent Object Instance via USP with allow_partial=false</strong></summary>

## Test Case 8: TS_USPPA_Delete_InvalidObjectInstance_allowpartial_false

### Objectives
To check if the EUT properly handles a DELETE message when allow_partial is set to false and the object instance to be deleted does not exist via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP DELETE request for Device.LocalAgent.Subscription.10. with allow_partial set to false to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP DELETE request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed DELETE response returns FAILURE with a matching parameter path and an appropriate error code indicating the object instance does not exist. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 9: Delete Non-Existent Object Instance via USP with allow_partial=true</strong></summary>

## Test Case 9: TS_USPPA_Delete_InvalidObjectInstance_allowpartial_true

### Objectives
To check if the EUT properly handles a DELETE message when allow_partial is set to true and the object instance to be deleted does not exist via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP DELETE request for Device.LocalAgent.Subscription.10. with allow_partial set to true to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP DELETE request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed DELETE response returns FAILURE with the OperSuccess element being empty, indicating the invalid object instance was handled correctly. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 10: Delete Invalid Object via USP with allow_partial=false</strong></summary>

## Test Case 10: TS_USPPA_Delete_InvalidObject_allowpartial_false

### Objectives
To check if the Agent properly handles a DELETE message when allow_partial is set to false and the object to be deleted is invalid via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP DELETE request for Device.LocalAgent.InvalidObject. with allow_partial set to false to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP DELETE request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed DELETE response returns FAILURE with a matching parameter path and an appropriate error code indicating the object is invalid. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 11: Delete Invalid Object via USP with allow_partial=true</strong></summary>

## Test Case 11: TS_USPPA_Delete_InvalidObject_allowpartial_true

### Objectives
To check if the Agent properly handles a DELETE message when allow_partial is set to true and the object to be deleted is invalid via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP DELETE request for Device.LocalAgent.InvalidObject. with allow_partial set to true to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP DELETE request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed DELETE response returns FAILURE with the OperFailure element containing a matching requested path and an appropriate error code for the invalid object. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 12: GET Controller Data Model by Object Instance Path via USP</strong></summary>

## Test Case 12: TS_USPPA_GetControllerObjectInstancePath

### Objectives
To send a GET request to get the Agent's instantiated controller data model when a path to an object instance is specified and receive a valid response via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET request for Device.LocalAgent.Controller.1. to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET response contains valid parameter values for Device.LocalAgent.Controller.1. object instance path. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 13: GET Controller Data Model by Object Path via USP</strong></summary>

## Test Case 13: TS_USPPA_GetControllerObjectPath

### Objectives
To send a GET request to get the Agent's instantiated controller data model when an object path is specified and receive a valid response via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET request for Device.LocalAgent.Controller. to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET response contains valid parameter values for Device.LocalAgent.Controller. object path. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 14: GET Controller Instances (All Levels) via USP</strong></summary>

## Test Case 14: TS_USPPA_GetInstances_Controller_firstlevelonly_false

### Objectives
To send a GET_INSTANCES request to get the instance details of the controller with first_level_only set to false and receive a valid response via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET_INSTANCES request for Device.LocalAgent.Controller. with first_level_only set to false to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET_INSTANCES request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET_INSTANCES response contains a non-empty requested path and instantiated object paths for Device.LocalAgent.Controller.. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 15: GET Controller Instances (First Level Only) via USP</strong></summary>

## Test Case 15: TS_USPPA_GetInstances_Controller_firstlevelonly_true

### Objectives
To send a GET_INSTANCES request to get the instance details of the controller with first_level_only set to true and receive a valid response via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET_INSTANCES request for Device.LocalAgent.Controller. with first_level_only set to true to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET_INSTANCES request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET_INSTANCES response contains a non-empty requested path and instantiated object paths for Device.LocalAgent.Controller.. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 16: GET IP Interface Instances (All Levels) via USP</strong></summary>

## Test Case 16: TS_USPPA_GetInstances_DeviceInterfaces_firstlevelonly_false

### Objectives
To send a GET_INSTANCES request to get the instance details of Device IP Interfaces with first_level_only set to false and receive a valid response via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET_INSTANCES request for Device.IP.Interface. with first_level_only set to false to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET_INSTANCES request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET_INSTANCES response contains a non-empty requested path and instantiated object paths for Device.IP.Interface.. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 17: GET IP Interface Instances (First Level Only) via USP</strong></summary>

## Test Case 17: TS_USPPA_GetInstances_DeviceInterfaces_firstlevelonly_true

### Objectives
To send a GET_INSTANCES request to get the instance details of Device IP Interfaces with first_level_only set to true and receive a valid response via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET_INSTANCES request for Device.IP.Interface. with first_level_only set to true to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET_INSTANCES request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET_INSTANCES response contains a non-empty requested path and instantiated object paths for Device.IP.Interface.. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 18: GET 2.4GHz SSID Name via USP</strong></summary>

## Test Case 18: TS_USPPA_GetSSIDName

### Objectives
To send a GET request to get the 2.4G SSID Name and receive a valid response via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET request for Device.WiFi.SSID.1.SSID to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET response contains a valid non-empty value for Device.WiFi.SSID.1.SSID. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 19: GET Supported DM for Controller (All Levels, All Options) via USP</strong></summary>

## Test Case 19: TS_USPPA_GetSupportedDM_Controller_firstlevelonly_false_allOptions

### Objectives
To send a GET_SUPPORTED_DM request via the USP protocol to retrieve the supported data model details of the controller instance, with first_level_only set to false and options like return_params, return_commands and return_events enabled.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET_SUPPORTED_DM request for Device.LocalAgent.Controller.1. with first_level_only set to false, return_params enabled, return_commands enabled, return_events enabled to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET_SUPPORTED_DM request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET_SUPPORTED_DM response contains the supported data model details including data model URI and metadata, and the appropriate supported types (parameters, commands, events) based on the options set. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 20: GET Supported DM for Controller (First Level, All Options) via USP</strong></summary>

## Test Case 20: TS_USPPA_GetSupportedDM_Controller_firstlevelonly_true_allOptions

### Objectives
To send a GET_SUPPORTED_DM request via the USP protocol to retrieve the supported data model details of the controller instance, with first_level_only set to true and options like return_params, return_commands and return_events enabled.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET_SUPPORTED_DM request for Device.LocalAgent.Controller.1. with first_level_only set to true, return_params enabled, return_commands enabled, return_events enabled to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET_SUPPORTED_DM request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET_SUPPORTED_DM response contains the supported data model details including data model URI and metadata, and the appropriate supported types (parameters, commands, events) based on the options set. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 21: GET Supported DM for IP Interfaces (All Levels, All Options) via USP</strong></summary>

## Test Case 21: TS_USPPA_GetSupportedDM_DeviceInterfaces_firstlevelonly_false_allOptions

### Objectives
To send a GET_SUPPORTED_DM request via the USP protocol to retrieve the supported data model details of the Device IP Interfaces, with first_level_only set to false and options like return_params, return_commands and return_events enabled.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET_SUPPORTED_DM request for Device.IP.Interface. with first_level_only set to false, return_params enabled, return_commands enabled, return_events enabled to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET_SUPPORTED_DM request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET_SUPPORTED_DM response contains the supported data model details including data model URI and metadata, and the appropriate supported types (parameters, commands, events) based on the options set. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 22: GET Supported DM for IP Interfaces (First Level, All Options) via USP</strong></summary>

## Test Case 22: TS_USPPA_GetSupportedDM_DeviceInterfaces_firstlevelonly_true_allOptions

### Objectives
To send a GET_SUPPORTED_DM request via the USP protocol to retrieve the supported data model details of Device IP Interfaces, with first_level_only set to true and options like return_params, return_commands and return_events enabled.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET_SUPPORTED_DM request for Device.IP.Interface. with first_level_only set to true, return_params enabled, return_commands enabled, return_events enabled to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET_SUPPORTED_DM request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET_SUPPORTED_DM response contains the supported data model details including data model URI and metadata, and the appropriate supported types (parameters, commands, events) based on the options set. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 23: GET Supported DM for LocalAgent Object (First Level, No Options) via USP</strong></summary>

## Test Case 23: TS_USPPA_GetSupportedDM_Object_firstlevelonly_true_noOptions

### Objectives
To send a GET_SUPPORTED_DM request via the USP protocol to retrieve the supported data model details of the root object, with first_level_only set to true and options like return_params, return_commands and return_events disabled.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET_SUPPORTED_DM request for Device.LocalAgent. with first_level_only set to true, return_params disabled, return_commands disabled, return_events disabled to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET_SUPPORTED_DM request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET_SUPPORTED_DM response contains the supported data model details including data model URI and metadata, and the appropriate supported types (parameters, commands, events) based on the options set. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 24: GET Supported DM for Root Object (All Levels, Commands Only) via USP</strong></summary>

## Test Case 24: TS_USPPA_GetSupportedDM_rootObject_firstlevelonly_false_commandsOnly

### Objectives
To send a GET_SUPPORTED_DM request via USP protocol to retrieve the details of root object, with first_level_only set to false, return_params and return_events disabled, and return_commands enabled.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET_SUPPORTED_DM request for Device. with first_level_only set to false, return_params disabled, return_commands enabled, return_events disabled to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET_SUPPORTED_DM request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET_SUPPORTED_DM response contains the supported data model details including data model URI and metadata, and the appropriate supported types (parameters, commands, events) based on the options set. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 25: GET Supported DM for Root Object (All Levels, Events Only) via USP</strong></summary>

## Test Case 25: TS_USPPA_GetSupportedDM_rootObject_firstlevelonly_false_eventsOnly

### Objectives
To send a GET_SUPPORTED_DM request via USP protocol to retrieve the details of root object, with first_level_only set to false, return_params and return_commands disabled, and return_events enabled.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET_SUPPORTED_DM request for Device. with first_level_only set to false, return_params disabled, return_commands disabled, return_events enabled to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET_SUPPORTED_DM request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET_SUPPORTED_DM response contains the supported data model details including data model URI and metadata, and the appropriate supported types (parameters, commands, events) based on the options set. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 26: GET Supported DM for Root Object (First Level, All Options) via USP</strong></summary>

## Test Case 26: TS_USPPA_GetSupportedDM_rootObject_firstlevelonly_true_allOptions

### Objectives
To send a GET_SUPPORTED_DM request via the USP protocol to retrieve the supported data model details of the root object, with first_level_only set to true and options like return_params, return_commands and return_events enabled.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET_SUPPORTED_DM request for Device. with first_level_only set to true, return_params enabled, return_commands enabled, return_events enabled to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET_SUPPORTED_DM request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET_SUPPORTED_DM response contains the supported data model details including data model URI and metadata, and the appropriate supported types (parameters, commands, events) based on the options set. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 27: GET Supported DM for Unsupported Object via USP</strong></summary>

## Test Case 27: TS_USPPA_GetSupportedDM_unsupportedObject_firstlevelonly_false_allOptions

### Objectives
To check if the Agent will correctly process a GET_SUPPORTED_DM message when the requested path is an unsupported object, with first_level_only set to false and options like return_params, return_commands and return_events enabled.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET_SUPPORTED_DM request for Device.LocalAgent.UnsupportedObject. with first_level_only set to false, return_params enabled, return_commands enabled, return_events enabled to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET_SUPPORTED_DM request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET_SUPPORTED_DM response returns FAILURE with a matching requested path and an appropriate error code for the unsupported object. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 28: GET Agent Supported USP Protocol Versions</strong></summary>

## Test Case 28: TS_USPPA_GetSupportedProtocolVersions

### Objectives
To send a GET_SUPPORTED_PROTO request to get the Agent supported protocol versions and receive a valid response via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET_SUPPORTED_PROTO request to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET_SUPPORTED_PROTO request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed response contains the agent_supported_protocol_versions field with a valid value. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 29: GET USP Agent Endpoint ID</strong></summary>

## Test Case 29: TS_USPPA_GetUSPAgentEndpointID

### Objectives
To send a GET request to get the USP agent's Endpoint ID and receive a valid response via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET request for Device.LocalAgent.EndpointID to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET response contains a valid non-empty value for Device.LocalAgent.EndpointID. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 30: GET Invalid Parameter via USP</strong></summary>

## Test Case 30: TS_USPPA_Get_InvalidParameter

### Objectives
To check if the USP Agent can properly handle a GET message when a single invalid parameter is requested via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET request for Device.LocalAgent.InvalidParameter to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed GET response returns FAILURE with a matching requested path and an appropriate error code for the invalid parameter. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 31: Reboot Device via USP OPERATE without Response</strong></summary>

## Test Case 31: TS_USPPA_OperateReboot_sendresp_false

### Objectives
To send an OPERATE message to reboot the EUT with send_resp set to false, receive no valid response back, and resume connectivity with the test system via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP OPERATE request for Device.Reboot() with send_resp set to false to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP OPERATE request returns HTTP status 200 (no response body expected since send_resp is false). If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>After reboot, verify connectivity is restored and the Agent Endpoint ID is accessible on the EUT</small> | <small>Check if the EUT has rebooted and connectivity is restored. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Send a USP GET request for Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason to the USP Controller.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Check if the USP GET request returns HTTP status 200 and the last reboot reason value is non-empty. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 32: Reboot Device via USP OPERATE with Response</strong></summary>

## Test Case 32: TS_USPPA_OperateReboot_sendresp_true

### Objectives
To send an OPERATE message to reboot the EUT with send_resp set to true and resume connectivity with the test system via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP OPERATE request for Device.Reboot() with send_resp set to true to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP OPERATE request returns HTTP status 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Check if the parsed OPERATE response contains the executed command Device.Reboot() and an empty output argument as expected. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>After reboot, verify connectivity is restored and the Agent Endpoint ID is accessible on the EUT</small> | <small>Check if the EUT has rebooted and connectivity is restored. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Send a USP GET request for Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason to the USP Controller.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Check if the USP GET request returns HTTP status 200 and the last reboot reason value is non-empty. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 33: Set Controller Periodic Notification Interval via USP</strong></summary>

## Test Case 33: TS_USPPA_SetControllerPeriodicNotifInterval

### Objectives
To send a SET request to set the Controller PeriodicNotifInterval and receive a valid response via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.LocalAgent.Controller.1.PeriodicNotifInterval | New value (different from current value) |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET request for Device.LocalAgent.Controller.1.PeriodicNotifInterval to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET request returns HTTP status 200 and the response contains a valid current PeriodicNotifInterval value. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a USP SET request for Device.LocalAgent.Controller.1.PeriodicNotifInterval with a new value to the USP Controller.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the USP SET request returns HTTP status 200 and the response confirms the new value was set. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Send a USP GET request for Device.LocalAgent.Controller.1.PeriodicNotifInterval to the USP Controller to verify the new value.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Check if the USP GET request returns HTTP status 200 and the value matches the newly set PeriodicNotifInterval. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Send a USP SET request for Device.LocalAgent.Controller.1.PeriodicNotifInterval to revert it to its original value to the USP Controller.</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Check if the USP SET revert request returns HTTP status 200 and confirms the value was reverted. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 34: Set Firewall Level via USP</strong></summary>

## Test Case 34: TS_USPPA_SetFirewallLevel

### Objectives
To send a SET request to set the firewall level of the gateway and receive a valid response via USP protocol.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| EUT - Endpoint under test |
| USP Controller - Remote Feature Control management system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | New value (different from current value) |

### Test Procedure and Expected Results
| Step Number | EUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the usppa process is running on the EUT</small> | <small>Check if the usppa process is up and running. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check if the USP Controller admin status is reachable and returns a valid response. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get the Agent Endpoint ID from the EUT using the command: UspPa -c get Device.LocalAgent.EndpointID</small> | <small>Check if the Agent Endpoint ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Send a USP GET request for Device.X_CISCO_COM_Security.Firewall.FirewallLevel to the USP Controller.</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Check if the USP GET request returns HTTP status 200 and the response contains a valid firewall level value. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a USP SET request for Device.X_CISCO_COM_Security.Firewall.FirewallLevel with a new firewall level value to the USP Controller.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the USP SET request returns HTTP status 200 and the response confirms the new value was set. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Send a USP GET request for Device.X_CISCO_COM_Security.Firewall.FirewallLevel to the USP Controller to verify the new value.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Check if the USP GET request returns HTTP status 200 and the value matches the newly set firewall level. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Send a USP SET request for Device.X_CISCO_COM_Security.Firewall.FirewallLevel to revert it to its original value to the USP Controller.</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Check if the USP SET revert request returns HTTP status 200 and confirms the value was reverted. If the condition is met PASS, else FAIL.</small> |

</details>

---

</details>

---
<details open>
<summary><strong>TR069</strong></summary>

# TR069

<details open>
<summary><strong>Test Case 35: Add and Delete NAT Port Mapping Object via ACS after Factory Reset</strong></summary>

## Test Case 35: TS_TR069PA_AddDeleteObject_AfterFactoryReset_ACS

### Objectives
To send an AddObject task to create an instance of Device.NAT.PortMapping, verify it using Device.NAT.PortMappingNumberOfEntries, then delete the instance and confirm the deletion by checking Device.NAT.PortMappingNumberOfEntries via ACS.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| ACS Server - Remote Feature Control Auto Configuration Server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.ManagementServer.EnableCWMP | true |
| Device.ManagementServer.URL | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation | As per test configuration |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the CcspTr069PaSsp tr069 process is running and listening on port 7547</small> | <small>Check if the tr069 process is up and listening on port 7547. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Set Device.ManagementServer.EnableCWMP to true</small> | <small>Check if Device.ManagementServer.EnableCWMP is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.ManagementServer.URL to the ACS server URL</small> | <small>Check if Device.ManagementServer.URL is set to the ACS server URL successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation to the TR069 certificate location</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.ManagementServer.ConnectionRequestUsername from the DUT</small> | <small>Check if the Connection Request Username is retrieved successfully and is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a TR069 FactoryReset task request to the TR069 ACS to reset writable tables.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the TR069 FactoryReset task returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>After the factory reset, wait for the DUT to come back up and restore connectivity.</small> | <small>Check if the DUT is accessible after factory reset. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>Verify that the CcspTr069PaSsp tr069 process is running and listening on port 7547</small> | <small>Check if the tr069 process is up and listening on port 7547. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>Set Device.ManagementServer.EnableCWMP to true</small> | <small>Check if Device.ManagementServer.EnableCWMP is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>11</small> | <small>Set Device.ManagementServer.URL to the ACS server URL</small> | <small>Check if Device.ManagementServer.URL is set to the ACS server URL successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>12</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation to the TR069 certificate location</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>13</small> | <small>GET Device.ManagementServer.ConnectionRequestUsername from the DUT</small> | <small>Check if the Connection Request Username is retrieved successfully and is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>14</small> | <small>&nbsp;</small> | <small>Send a TR069 GET task request for Device.NAT.PortMappingNumberOfEntries to the TR069 ACS.</small> |
| <small>15</small> | <small>&nbsp;</small> | <small>Check if the TR069 GET task request for Device.NAT.PortMappingNumberOfEntries returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>16</small> | <small>&nbsp;</small> | <small>Send a TR069 SEARCH query for Device.NAT.PortMappingNumberOfEntries to the TR069 ACS database.</small> |
| <small>17</small> | <small>&nbsp;</small> | <small>Check if the TR069 SEARCH query returns HTTP 200 and the response contains valid parameter values for Device.NAT.PortMappingNumberOfEntries. If the condition is met CONTINUE, else FAIL.</small> |
| <small>18</small> | <small>&nbsp;</small> | <small>Send a TR069 AddObject task request for Device.NAT.PortMapping to the TR069 ACS.</small> |
| <small>19</small> | <small>&nbsp;</small> | <small>Check if the TR069 AddObject task returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>20</small> | <small>&nbsp;</small> | <small>Send a TR069 GET task request for Device.NAT.PortMappingNumberOfEntries to the TR069 ACS.</small> |
| <small>21</small> | <small>&nbsp;</small> | <small>Check if the TR069 GET task request for Device.NAT.PortMappingNumberOfEntries returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>22</small> | <small>&nbsp;</small> | <small>Send a TR069 SEARCH query for Device.NAT.PortMappingNumberOfEntries to the TR069 ACS database.</small> |
| <small>23</small> | <small>&nbsp;</small> | <small>Check if the TR069 SEARCH query returns HTTP 200 and the response contains valid parameter values for Device.NAT.PortMappingNumberOfEntries. If the condition is met CONTINUE, else FAIL.</small> |
| <small>24</small> | <small>&nbsp;</small> | <small>Check if Device.NAT.PortMappingNumberOfEntries has been incremented by 1 after the AddObject operation. If the condition is met CONTINUE, else FAIL.</small> |
| <small>25</small> | <small>&nbsp;</small> | <small>Send a TR069 DeleteObject task request for the newly created Device.NAT.PortMapping instance to the TR069 ACS.</small> |
| <small>26</small> | <small>&nbsp;</small> | <small>Check if the TR069 DeleteObject task returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>27</small> | <small>&nbsp;</small> | <small>Send a TR069 GET task request for Device.NAT.PortMappingNumberOfEntries to the TR069 ACS.</small> |
| <small>28</small> | <small>&nbsp;</small> | <small>Check if the TR069 GET task request for Device.NAT.PortMappingNumberOfEntries returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>29</small> | <small>&nbsp;</small> | <small>Send a TR069 SEARCH query for Device.NAT.PortMappingNumberOfEntries to the TR069 ACS database.</small> |
| <small>30</small> | <small>&nbsp;</small> | <small>Check if the TR069 SEARCH query returns HTTP 200 and the response contains valid parameter values for Device.NAT.PortMappingNumberOfEntries. If the condition is met CONTINUE, else FAIL.</small> |
| <small>31</small> | <small>&nbsp;</small> | <small>Check if Device.NAT.PortMappingNumberOfEntries has been decremented by 1 after the DeleteObject operation, matching the original count. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 36: Verify Management Server URL Matches partners_defaults.json</strong></summary>

## Test Case 36: TS_TR069PA_CheckServerURL_FromJsonFile

### Objectives
To check if the Management Server URL from the TR181 parameter Device.ManagementServer.URL is the one configured in partners_defaults.json.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| ACS Server - Remote Feature Control Auto Configuration Server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| None | |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.ManagementServer.URL from the DUT.</small> | <small>Check if Device.ManagementServer.URL is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Run a grep command on /nvram/partners_defaults.json to check if the Management Server URL retrieved in the previous step is present in the file.</small> | <small>Check if the Management Server URL is present in /nvram/partners_defaults.json. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 37: Trigger Factory Reset via TR069 ACS and Verify</strong></summary>

## Test Case 37: TS_TR069PA_FactoryReset_ACS

### Objectives
To send a FactoryReset task request to factory reset the DUT, receive a valid response, and re-establish connectivity with the test system through ACS.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| ACS Server - Remote Feature Control Auto Configuration Server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.ManagementServer.EnableCWMP | true |
| Device.ManagementServer.URL | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation | As per test configuration |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the CcspTr069PaSsp tr069 process is running and listening on port 7547</small> | <small>Check if the tr069 process is up and listening on port 7547. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Set Device.ManagementServer.EnableCWMP to true</small> | <small>Check if Device.ManagementServer.EnableCWMP is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.ManagementServer.URL to the ACS server URL</small> | <small>Check if Device.ManagementServer.URL is set to the ACS server URL successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation to the TR069 certificate location</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.ManagementServer.ConnectionRequestUsername from the DUT</small> | <small>Check if the Connection Request Username is retrieved successfully and is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a TR069 FactoryReset task request to the TR069 ACS.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the TR069 FactoryReset task returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>After the factory reset, wait for the DUT to come back up and restore connectivity.</small> | <small>Check if the DUT is accessible after factory reset. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>Verify that the CcspTr069PaSsp tr069 process is running and listening on port 7547</small> | <small>Check if the tr069 process is up and listening on port 7547. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>Set Device.ManagementServer.EnableCWMP to true</small> | <small>Check if Device.ManagementServer.EnableCWMP is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>11</small> | <small>Set Device.ManagementServer.URL to the ACS server URL</small> | <small>Check if Device.ManagementServer.URL is set to the ACS server URL successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>12</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation to the TR069 certificate location</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>13</small> | <small>GET Device.ManagementServer.ConnectionRequestUsername from the DUT</small> | <small>Check if the Connection Request Username is retrieved successfully and is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>14</small> | <small>&nbsp;</small> | <small>Send a TR069 GET task request for Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason to the TR069 ACS.</small> |
| <small>15</small> | <small>&nbsp;</small> | <small>Check if the TR069 GET task request for Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>16</small> | <small>&nbsp;</small> | <small>Send a TR069 SEARCH query for Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason to the TR069 ACS database.</small> |
| <small>17</small> | <small>&nbsp;</small> | <small>Check if the TR069 SEARCH query returns HTTP 200 and the response contains valid parameter values for Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason. If the condition is met CONTINUE, else FAIL.</small> |
| <small>18</small> | <small>&nbsp;</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason is "factory-reset", confirming the DUT completed a factory reset via TR069 ACS. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details open>
<summary><strong>Test Case 38: Get LAN Mode via ACS and Verify against DUT</strong></summary>

## Test Case 38: TS_TR069PA_GetLanMode_ACS

### Objectives
To send a GET task request to get Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode via ACS, then retrieve and verify the value matches the DUT.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| ACS Server - Remote Feature Control Auto Configuration Server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.ManagementServer.EnableCWMP | true |
| Device.ManagementServer.URL | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation | As per test configuration |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the CcspTr069PaSsp tr069 process is running and listening on port 7547</small> | <small>Check if the tr069 process is up and listening on port 7547. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Set Device.ManagementServer.EnableCWMP to true</small> | <small>Check if Device.ManagementServer.EnableCWMP is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.ManagementServer.URL to the ACS server URL</small> | <small>Check if Device.ManagementServer.URL is set to the ACS server URL successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation to the TR069 certificate location</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.ManagementServer.ConnectionRequestUsername from the DUT</small> | <small>Check if the Connection Request Username is retrieved successfully and is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a TR069 GET task request for Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to the TR069 ACS.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the TR069 GET task request for Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Send a TR069 SEARCH query for Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to the TR069 ACS database.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Check if the TR069 SEARCH query returns HTTP 200 and the response contains valid parameter values for Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode from the DUT.</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Check if Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode is retrieved from DUT successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>12</small> | <small>&nbsp;</small> | <small>Check if the value of Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode from ACS matches the value retrieved from the DUT. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 39: GET Multiple Parameter Values via ACS and Verify against DUT</strong></summary>

## Test Case 39: TS_TR069PA_GetMultipleValues_ACS

### Objectives
To send a GET task request to get multiple values (Device.DeviceInfo.ProductClass and Device.DeviceInfo.Manufacturer) via ACS, then retrieve and verify the values match the DUT.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| ACS Server - Remote Feature Control Auto Configuration Server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.ManagementServer.EnableCWMP | true |
| Device.ManagementServer.URL | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation | As per test configuration |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the CcspTr069PaSsp tr069 process is running and listening on port 7547</small> | <small>Check if the tr069 process is up and listening on port 7547. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Set Device.ManagementServer.EnableCWMP to true</small> | <small>Check if Device.ManagementServer.EnableCWMP is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.ManagementServer.URL to the ACS server URL</small> | <small>Check if Device.ManagementServer.URL is set to the ACS server URL successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation to the TR069 certificate location</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.ManagementServer.ConnectionRequestUsername from the DUT</small> | <small>Check if the Connection Request Username is retrieved successfully and is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a TR069 GET task request for Device.DeviceInfo.ProductClass and Device.DeviceInfo.Manufacturer to the TR069 ACS.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the TR069 GET task request for Device.DeviceInfo.ProductClass and Device.DeviceInfo.Manufacturer returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Send a TR069 SEARCH query for Device.DeviceInfo.ProductClass and Device.DeviceInfo.Manufacturer to the TR069 ACS database.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Check if the TR069 SEARCH query returns HTTP 200 and the response contains valid parameter values for Device.DeviceInfo.ProductClass and Device.DeviceInfo.Manufacturer. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>GET Device.DeviceInfo.ProductClass from the DUT</small> | <small>Check if Device.DeviceInfo.ProductClass is retrieved from the DUT successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>11</small> | <small>GET Device.DeviceInfo.Manufacturer from the DUT</small> | <small>Check if Device.DeviceInfo.Manufacturer is retrieved from the DUT successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>12</small> | <small>&nbsp;</small> | <small>Check if the value of Device.DeviceInfo.ProductClass from ACS matches the value retrieved from the DUT. If the condition is met CONTINUE, else FAIL.</small> |
| <small>13</small> | <small>&nbsp;</small> | <small>Check if the value of Device.DeviceInfo.Manufacturer from ACS matches the value retrieved from the DUT. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 40: GET Device Time Object Parameters via ACS</strong></summary>

## Test Case 40: TS_TR069PA_GetObject_ACS

### Objectives
To send a GET task request to get the parameters of the Device.Time object and retrieve the value successfully via ACS.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| ACS Server - Remote Feature Control Auto Configuration Server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.ManagementServer.EnableCWMP | true |
| Device.ManagementServer.URL | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation | As per test configuration |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the CcspTr069PaSsp tr069 process is running and listening on port 7547</small> | <small>Check if the tr069 process is up and listening on port 7547. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Set Device.ManagementServer.EnableCWMP to true</small> | <small>Check if Device.ManagementServer.EnableCWMP is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.ManagementServer.URL to the ACS server URL</small> | <small>Check if Device.ManagementServer.URL is set to the ACS server URL successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation to the TR069 certificate location</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.ManagementServer.ConnectionRequestUsername from the DUT</small> | <small>Check if the Connection Request Username is retrieved successfully and is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a TR069 GET task request for Device.Time to the TR069 ACS.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the TR069 GET task request for Device.Time returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Send a TR069 SEARCH query for Device.Time to the TR069 ACS database.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Check if the TR069 SEARCH query returns HTTP 200 and the response contains valid parameter values for the Device.Time object. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 41: Trigger Device Reboot via TR069 ACS and Verify</strong></summary>

## Test Case 41: TS_TR069PA_Reboot_ACS

### Objectives
To send a Reboot task request to restart the DUT, receive a valid response, and re-establish connectivity with the test system through ACS.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| ACS Server - Remote Feature Control Auto Configuration Server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.ManagementServer.EnableCWMP | true |
| Device.ManagementServer.URL | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation | As per test configuration |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the CcspTr069PaSsp tr069 process is running and listening on port 7547</small> | <small>Check if the tr069 process is up and listening on port 7547. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Set Device.ManagementServer.EnableCWMP to true</small> | <small>Check if Device.ManagementServer.EnableCWMP is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.ManagementServer.URL to the ACS server URL</small> | <small>Check if Device.ManagementServer.URL is set to the ACS server URL successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation to the TR069 certificate location</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.ManagementServer.ConnectionRequestUsername from the DUT</small> | <small>Check if the Connection Request Username is retrieved successfully and is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a TR069 Reboot task request to the TR069 ACS.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the TR069 Reboot task returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>After the reboot, wait for the DUT to come back up and restore connectivity.</small> | <small>Check if the DUT is accessible after reboot. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>Verify that the CcspTr069PaSsp tr069 process is running and listening on port 7547</small> | <small>Check if the tr069 process is up and listening on port 7547. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>Set Device.ManagementServer.EnableCWMP to true</small> | <small>Check if Device.ManagementServer.EnableCWMP is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>11</small> | <small>Set Device.ManagementServer.URL to the ACS server URL</small> | <small>Check if Device.ManagementServer.URL is set to the ACS server URL successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>12</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation to the TR069 certificate location</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>13</small> | <small>GET Device.ManagementServer.ConnectionRequestUsername from the DUT</small> | <small>Check if the Connection Request Username is retrieved successfully and is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>14</small> | <small>&nbsp;</small> | <small>Send a TR069 GET task request for Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason to the TR069 ACS.</small> |
| <small>15</small> | <small>&nbsp;</small> | <small>Check if the TR069 GET task request for Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>16</small> | <small>&nbsp;</small> | <small>Send a TR069 SEARCH query for Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason to the TR069 ACS database.</small> |
| <small>17</small> | <small>&nbsp;</small> | <small>Check if the TR069 SEARCH query returns HTTP 200 and the response contains valid parameter values for Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason. If the condition is met CONTINUE, else FAIL.</small> |
| <small>18</small> | <small>&nbsp;</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason is "tr069-reboot", confirming the DUT rebooted via TR069 ACS. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 42: Refresh All Device Parameters via ACS</strong></summary>

## Test Case 42: TS_TR069PA_RefreshAllParameters_ACS

### Objectives
To send a RefreshObject task request to refresh all parameters and verify it successfully via ACS.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| ACS Server - Remote Feature Control Auto Configuration Server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.ManagementServer.EnableCWMP | true |
| Device.ManagementServer.URL | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation | As per test configuration |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the CcspTr069PaSsp tr069 process is running and listening on port 7547</small> | <small>Check if the tr069 process is up and listening on port 7547. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Set Device.ManagementServer.EnableCWMP to true</small> | <small>Check if Device.ManagementServer.EnableCWMP is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.ManagementServer.URL to the ACS server URL</small> | <small>Check if Device.ManagementServer.URL is set to the ACS server URL successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation to the TR069 certificate location</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.ManagementServer.ConnectionRequestUsername from the DUT</small> | <small>Check if the Connection Request Username is retrieved successfully and is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a TR069 RefreshObject task request for all device parameters (empty objectName) to the TR069 ACS.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the TR069 RefreshObject task returns HTTP 200 and the objectName in the response is empty as expected. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 43: Refresh Device Time Parameter via ACS</strong></summary>

## Test Case 43: TS_TR069PA_RefreshParameter_ACS

### Objectives
To send a RefreshObject task request to refresh the Device.Time parameter and verify it successfully via ACS.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| ACS Server - Remote Feature Control Auto Configuration Server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.ManagementServer.EnableCWMP | true |
| Device.ManagementServer.URL | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation | As per test configuration |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the CcspTr069PaSsp tr069 process is running and listening on port 7547</small> | <small>Check if the tr069 process is up and listening on port 7547. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Set Device.ManagementServer.EnableCWMP to true</small> | <small>Check if Device.ManagementServer.EnableCWMP is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.ManagementServer.URL to the ACS server URL</small> | <small>Check if Device.ManagementServer.URL is set to the ACS server URL successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation to the TR069 certificate location</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.ManagementServer.ConnectionRequestUsername from the DUT</small> | <small>Check if the Connection Request Username is retrieved successfully and is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a TR069 RefreshObject task request for Device.Time to the TR069 ACS.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the TR069 RefreshObject task returns HTTP 200 and the objectName in the response matches Device.Time. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 44: SET Multiple Parameter Values via ACS and Verify</strong></summary>

## Test Case 44: TS_TR069PA_SetMultipleValues_ACS

### Objectives
To send a SET task request to set multiple values (Device.ManagementServer.UpgradesManaged, Device.Time.Enable and Device.Time.NTPServer1) via ACS, then retrieve and verify the values are reflected successfully.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| ACS Server - Remote Feature Control Auto Configuration Server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.ManagementServer.EnableCWMP | true |
| Device.ManagementServer.URL | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation | As per test configuration |
| Device.ManagementServer.UpgradesManaged | Toggled boolean value (different from current value) |
| Device.Time.Enable | Toggled boolean value (different from current value) |
| Device.Time.NTPServer1 | pool.ntp.org or time.nist.gov (toggled from current value) |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the CcspTr069PaSsp tr069 process is running and listening on port 7547</small> | <small>Check if the tr069 process is up and listening on port 7547. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Set Device.ManagementServer.EnableCWMP to true</small> | <small>Check if Device.ManagementServer.EnableCWMP is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.ManagementServer.URL to the ACS server URL</small> | <small>Check if Device.ManagementServer.URL is set to the ACS server URL successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation to the TR069 certificate location</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.ManagementServer.ConnectionRequestUsername from the DUT</small> | <small>Check if the Connection Request Username is retrieved successfully and is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a TR069 GET task request for Device.ManagementServer.UpgradesManaged, Device.Time.Enable, Device.Time.NTPServer1 to the TR069 ACS.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the TR069 GET task request for Device.ManagementServer.UpgradesManaged, Device.Time.Enable, Device.Time.NTPServer1 returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Send a TR069 SEARCH query for Device.ManagementServer.UpgradesManaged, Device.Time.Enable, Device.Time.NTPServer1 to the TR069 ACS database.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Check if the TR069 SEARCH query returns HTTP 200 and the response contains valid parameter values for Device.ManagementServer.UpgradesManaged, Device.Time.Enable, Device.Time.NTPServer1. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Send a TR069 SET task request for Device.ManagementServer.UpgradesManaged, Device.Time.Enable, Device.Time.NTPServer1 to the TR069 ACS.</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Check if the TR069 SET task request for Device.ManagementServer.UpgradesManaged, Device.Time.Enable, Device.Time.NTPServer1 returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>12</small> | <small>&nbsp;</small> | <small>Send a TR069 GET task request for Device.ManagementServer.UpgradesManaged, Device.Time.Enable, Device.Time.NTPServer1 to the TR069 ACS.</small> |
| <small>13</small> | <small>&nbsp;</small> | <small>Check if the TR069 GET task request for Device.ManagementServer.UpgradesManaged, Device.Time.Enable, Device.Time.NTPServer1 returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>14</small> | <small>&nbsp;</small> | <small>Send a TR069 SEARCH query for Device.ManagementServer.UpgradesManaged, Device.Time.Enable, Device.Time.NTPServer1 to the TR069 ACS database.</small> |
| <small>15</small> | <small>&nbsp;</small> | <small>Check if the TR069 SEARCH query returns HTTP 200 and the response contains valid parameter values for Device.ManagementServer.UpgradesManaged, Device.Time.Enable, Device.Time.NTPServer1. If the condition is met CONTINUE, else FAIL.</small> |
| <small>16</small> | <small>&nbsp;</small> | <small>Check if the value of Device.ManagementServer.UpgradesManaged returned by ACS matches the new value that was set. If the condition is met CONTINUE, else FAIL.</small> |
| <small>17</small> | <small>&nbsp;</small> | <small>Check if the value of Device.Time.Enable returned by ACS matches the new value that was set. If the condition is met CONTINUE, else FAIL.</small> |
| <small>18</small> | <small>&nbsp;</small> | <small>Check if the value of Device.Time.NTPServer1 returned by ACS matches the new value that was set. If the condition is met CONTINUE, else FAIL.</small> |
| <small>19</small> | <small>&nbsp;</small> | <small>Send a TR069 SET task request for Device.ManagementServer.UpgradesManaged, Device.Time.Enable, Device.Time.NTPServer1 to the TR069 ACS to revert all three parameters to their original values.</small> |
| <small>20</small> | <small>&nbsp;</small> | <small>Check if the TR069 SET revert request returns HTTP 200. If the condition is met PASS, else FAIL.</small> |


</details>

---

<details open>
<summary><strong>Test Case 45: Set NTP Server via ACS and Verify</strong></summary>

## Test Case 45: TS_TR069PA_SetNTPServer_ACS

### Objectives
To send a SET task request to set Device.Time.NTPServer1 to another value, then retrieve and verify that the change is reflected successfully via ACS.

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| ACS Server - Remote Feature Control Auto Configuration Server |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.ManagementServer.EnableCWMP | true |
| Device.ManagementServer.URL | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation | As per test configuration |
| Device.Time.NTPServer1 | pool.ntp.org or time.nist.gov (toggled from current value) |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Verify that the CcspTr069PaSsp tr069 process is running and listening on port 7547</small> | <small>Check if the tr069 process is up and listening on port 7547. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Set Device.ManagementServer.EnableCWMP to true</small> | <small>Check if Device.ManagementServer.EnableCWMP is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.ManagementServer.URL to the ACS server URL</small> | <small>Check if Device.ManagementServer.URL is set to the ACS server URL successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation to the TR069 certificate location</small> | <small>Check if Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.TR69CertLocation is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.ManagementServer.ConnectionRequestUsername from the DUT</small> | <small>Check if the Connection Request Username is retrieved successfully and is non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Send a TR069 GET task request for Device.Time.NTPServer1 to the TR069 ACS.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Check if the TR069 GET task request for Device.Time.NTPServer1 returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Send a TR069 SEARCH query for Device.Time.NTPServer1 to the TR069 ACS database.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Check if the TR069 SEARCH query returns HTTP 200 and the response contains valid parameter values for Device.Time.NTPServer1. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Send a TR069 SET task request for Device.Time.NTPServer1 to the TR069 ACS.</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Check if the TR069 SET task request for Device.Time.NTPServer1 returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>12</small> | <small>&nbsp;</small> | <small>Send a TR069 GET task request for Device.Time.NTPServer1 to the TR069 ACS.</small> |
| <small>13</small> | <small>&nbsp;</small> | <small>Check if the TR069 GET task request for Device.Time.NTPServer1 returns HTTP 200. If the condition is met CONTINUE, else FAIL.</small> |
| <small>14</small> | <small>&nbsp;</small> | <small>Send a TR069 SEARCH query for Device.Time.NTPServer1 to the TR069 ACS database.</small> |
| <small>15</small> | <small>&nbsp;</small> | <small>Check if the TR069 SEARCH query returns HTTP 200 and the response contains valid parameter values for Device.Time.NTPServer1. If the condition is met CONTINUE, else FAIL.</small> |
| <small>16</small> | <small>&nbsp;</small> | <small>Check if the value of Device.Time.NTPServer1 returned by ACS matches the new value that was set. If the condition is met CONTINUE, else FAIL.</small> |
| <small>17</small> | <small>&nbsp;</small> | <small>Send a TR069 SET task request for Device.Time.NTPServer1 to the TR069 ACS to revert it to the original value.</small> |
| <small>18</small> | <small>&nbsp;</small> | <small>Check if the TR069 SET revert request for Device.Time.NTPServer1 returns HTTP 200. If the condition is met PASS, else FAIL.</small> |


</details>

---


</details>

---

<details open>
<summary><strong>RFC</strong></summary>

# RFC

<details open>
<summary><strong>Test Case 46: Toggle Multiple DM Parameters Simultaneously via RFC and XConf</strong></summary>

## Test Case 46: TS_RFC_ToggleMultipleParameters

### Objective
Validate that the RFC service restart simultaneously updates multiple DM parameters as configured in the XConf server.

### Test Type
Positive

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| XConf Server - Remote Feature Control configuration server |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Execute command to retrieve the device MAC address.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET the current values of Device.X_Comcast_com_ParentalControl.ManagedSites.Enable, Device.X_Comcast_com_ParentalControl.ManagedServices.Enable, and Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable</small> | <small>Verify that the current DM values for all three parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Check that the RFC properties file exists in the DUT. Extract RFC_CONFIG_SERVER_URL from the RFC properties file.</small> | <small>Verify that RFC properties file exists and RFC_CONFIG_SERVER_URL from the properties file matches the configured XConf server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Delete the dcmrfc.log file to ensure clean logging for the test.</small> | <small>Verify that dcmrfc.log is deleted successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>POST to the XConf server to configure the RFC feature with toggled values for all three parameters: Device.X_Comcast_com_ParentalControl.ManagedSites.Enable, Device.X_Comcast_com_ParentalControl.ManagedServices.Enable, and Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable.</small> | <small>Verify that the feature name and all parameter values are present in the response. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>POST to the XConf server to set the feature rule binding the configured feature to the device MAC address.</small> | <small>Verify that the feature name and MAC address are present in the response. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 20 seconds, then GET from the XConf server using the device MAC address.</small> | <small>Verify that the feature name and all parameter/value pairs are present in the response. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Restart the RFC service using systemctl restart rfc. Wait 10 seconds, then get the service status.</small> | <small>Verify that the RFC service status shows active (running or exited). If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>Check that the RFC feature configuration file exists at RFC_FILE_PATH and contains the configured feature name.</small> | <small>Verify that the RFC feature configuration file exists and the feature name is present in the file. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>GET Device.X_Comcast_com_ParentalControl.ManagedSites.Enable, Device.X_Comcast_com_ParentalControl.ManagedServices.Enable, and Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable</small> | <small>Verify that all three DM values have changed to their respective toggled values, each different from the corresponding initial value. If the condition is met CONTINUE, else FAIL</small> |
| <small>11</small> | <small>Check dcmrfc.log for update log entries for each parameter.</small> | <small>Verify that dcmrfc.log contains "updated for Device.X_Comcast_com_ParentalControl.ManagedSites.Enable", "updated for Device.X_Comcast_com_ParentalControl.ManagedServices.Enable", and "updated for Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable". If the condition is met CONTINUE, else FAIL</small> |
| <small>12</small> | <small>PUT the initial values of all three parameters to the XConf server to revert the RFC feature configuration.</small> | <small>Verify if the operation is success. If the condition is met CONTINUE, else FAIL</small> |
| <small>13</small> | <small>Restart the RFC service. Wait 10 seconds, then check the RFC service status.</small> | <small>Verify that the RFC service is active. If the condition is met CONTINUE, else FAIL</small> |
| <small>14</small> | <small>GET Device.X_Comcast_com_ParentalControl.ManagedSites.Enable, Device.X_Comcast_com_ParentalControl.ManagedServices.Enable, and Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable after waiting 60 seconds.</small> | <small>Verify that all three DM values have been reverted to their respective initial values. If the condition is met CONTINUE, else FAIL</small> |
| <small>15</small> | <small>DELETE the feature rule from the XConf server.</small> | <small>Verify that the response is empty indicating successful deletion. If the condition is met CONTINUE, else FAIL</small> |
| <small>16</small> | <small>DELETE the feature from the XConf server.</small> | <small>Verify that the response is empty indicating successful deletion. If the condition is met PASS, else FAIL</small> |

</details>

---


<details open>
<summary><strong>Test Case 47: Verify RFC Config Fetch and DM Update Triggered by Device Reboot</strong></summary>

## Test Case 47: TS_RFC_ToggleParameter_viaReboot

### Objective
Validate that a device reboot (without an explicit RFC service restart) triggers the RFC configuration fetch from the XConf server and updates the DM parameter to the configured value.

### Test Type
Positive

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| XConf Server - Remote Feature Control configuration server |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Execute command to retrieve the device MAC address.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET the current value of Device.X_Comcast_com_ParentalControl.ManagedSites.Enable</small> | <small>Verify that the current DM value is retrieved successfully and is either true or false. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Check that the RFC properties file exists in the DUT. Extract RFC_CONFIG_SERVER_URL from the RFC properties file.</small> | <small>Verify that RFC properties file exists and RFC_CONFIG_SERVER_URL from the properties file matches the configured XConf server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>POST to the XConf server to configure the RFC feature with the toggled value for Device.X_Comcast_com_ParentalControl.ManagedSites.Enable.</small> | <small>Verify that the feature name and parameter value are present in the response. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>POST to the XConf server to set the feature rule binding the configured feature to the device MAC address.</small> | <small>Verify that the feature name and MAC address are present in the response. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Wait 20 seconds, then GET from the XConf server using the device MAC address.</small> | <small>Verify that the feature name and parameter/value are present in the response. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Initiate a device reboot and wait 300 seconds for the DUT to come back online.</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>Check that the RFC feature configuration file exists at RFC_FILE_PATH and contains the configured feature name.</small> | <small>Verify that the RFC feature configuration file exists and the feature name is present in the file, confirming that RFC fetch occurred during the reboot cycle. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>GET Device.X_Comcast_com_ParentalControl.ManagedSites.Enable</small> | <small>Verify that the DM value has changed to the toggled value and is different from the initial value. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>PUT the initial value of Device.X_Comcast_com_ParentalControl.ManagedSites.Enable to the XConf server to revert the RFC feature configuration.</small> | <small>Verify if the operation is success. If the condition is met CONTINUE, else FAIL</small> |
| <small>11</small> | <small>Restart the RFC service. Wait 10 seconds, then check the RFC service status.</small> | <small>Verify that the RFC service is active. If the condition is met CONTINUE, else FAIL</small> |
| <small>12</small> | <small>GET Device.X_Comcast_com_ParentalControl.ManagedSites.Enable after waiting 60 seconds.</small> | <small>Verify that the DM value has been reverted to the initial value. If the condition is met CONTINUE, else FAIL</small> |
| <small>13</small> | <small>DELETE the feature rule from the XConf server.</small> | <small>Verify that the response is empty indicating successful deletion. If the condition is met CONTINUE, else FAIL</small> |
| <small>14</small> | <small>DELETE the feature from the XConf server.</small> | <small>Verify that the response is empty indicating successful deletion. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 48: Verify RFC Feature Configuration Persists after Reboot</strong></summary>

## Test Case 48: TS_RFC_RebootPersistence_afterDMToggle

### Objective
Validate that the RFC feature configuration persists across a device reboot and that the DM parameter maintains its configured value after the reboot.

### Test Type
Positive

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| XConf Server - Remote Feature Control configuration server |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Execute command to retrieve the device MAC address.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET the current value of Device.X_Comcast_com_ParentalControl.ManagedSites.Enable</small> | <small>Verify that the current DM value is retrieved successfully and is either true or false. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Check that the RFC properties file exists in the DUT. Extract RFC_CONFIG_SERVER_URL from the RFC properties file.</small> | <small>Verify that RFC properties file exists and RFC_CONFIG_SERVER_URL from the properties file matches the configured XConf server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>POST to the XConf server to configure the RFC feature with the toggled value for Device.X_Comcast_com_ParentalControl.ManagedSites.Enable.</small> | <small>Verify that the feature name and parameter value are present in the response. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>POST to the XConf server to set the feature rule binding the configured feature to the device MAC address.</small> | <small>Verify that the feature name and MAC address are present in the response. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Wait 20 seconds, then GET from the XConf server using the device MAC address.</small> | <small>Verify that the feature name and parameter/value are present in the response. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Restart the RFC service using systemctl restart rfc. Wait 10 seconds, then get the service status.</small> | <small>Verify that the RFC service status shows active (running or exited). If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Check that the RFC feature configuration file exists at RFC_FILE_PATH and contains the configured feature name.</small> | <small>Verify that the RFC feature configuration file exists and the feature name is present in the file. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>GET Device.X_Comcast_com_ParentalControl.ManagedSites.Enable</small> | <small>Verify that the DM value has changed to the toggled value and is different from the initial value. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>Initiate a device reboot and wait 300 seconds for the DUT to come back online.</small> | <small>&nbsp;</small> |
| <small>11</small> | <small>GET Device.X_Comcast_com_ParentalControl.ManagedSites.Enable after the reboot.</small> | <small>Verify that the DM value equals the toggled value, confirming that the RFC configuration persisted across the reboot. If the condition is met CONTINUE, else FAIL</small> |
| <small>12</small> | <small>PUT the initial value of Device.X_Comcast_com_ParentalControl.ManagedSites.Enable to the XConf server to revert the RFC feature configuration.</small> | <small>Verify if the operation is success. If the condition is met CONTINUE, else FAIL</small> |
| <small>13</small> | <small>Restart the RFC service. Wait 10 seconds, then check the RFC service status.</small> | <small>Verify that the RFC service is active. If the condition is met CONTINUE, else FAIL</small> |
| <small>14</small> | <small>GET Device.X_Comcast_com_ParentalControl.ManagedSites.Enable after waiting 60 seconds.</small> | <small>Verify that the DM value has been reverted to the initial value. If the condition is met CONTINUE, else FAIL</small> |
| <small>15</small> | <small>DELETE the feature rule from the XConf server.</small> | <small>Verify that the response is empty indicating successful deletion. If the condition is met CONTINUE, else FAIL</small> |
| <small>16</small> | <small>DELETE the feature from the XConf server.</small> | <small>Verify that the response is empty indicating successful deletion. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 49: Toggle Single DM Parameter via RFC and XConf</strong></summary>

## Test Case 49: TS_RFC_ToggleSingleParameter

### Objective
Validate that a single DM parameter configured through XConf is applied after RFC service restart, and can be reverted back to its original value.

### Test Type
Positive

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| XConf Server - Remote Feature Control configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| RFC DM parameter under validation | RFC_DM_1 (true or false) |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Execute command to retrieve the device MAC address.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET the current value of RFC_DM_1.</small> | <small>Verify that the current DM value is retrieved successfully and is either true or false. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Check that the RFC properties file exists in the DUT and extract RFC_CONFIG_SERVER_URL.</small> | <small>Verify that RFC properties file exists and RFC_CONFIG_SERVER_URL matches the configured XConf server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>POST to the XConf server to configure the RFC feature with the toggled value for RFC_DM_1.</small> | <small>Verify that the feature details and parameter/value are present in the response. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>POST to the XConf server to set the feature rule binding the configured feature to the device MAC address.</small> | <small>Verify that the feature rule is created successfully with the device MAC address mapping. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Wait 20 seconds, then GET from the XConf server using the device MAC address.</small> | <small>Verify that the feature name and parameter/value are present in the response. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Restart the RFC service using systemctl restart rfc. Wait 10 seconds, then get the service status.</small> | <small>Verify that the RFC service status shows active (running or exited). If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>GET RFC_DM_1 after RFC restart.</small> | <small>Verify that the DM value is toggled and different from the initial value. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>PUT the initial value of RFC_DM_1 to the XConf server to revert the RFC feature configuration.</small> | <small>Verify that the revert operation succeeds and response indicates successful update. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>Wait for RFC apply interval, then GET RFC_DM_1.</small> | <small>Verify that the DM value is reverted to the initial value. If the condition is met CONTINUE, else FAIL</small> |
| <small>11</small> | <small>DELETE the feature rule from the XConf server.</small> | <small>Verify that the response is empty indicating successful deletion. If the condition is met CONTINUE, else FAIL</small> |
| <small>12</small> | <small>DELETE the feature from the XConf server.</small> | <small>Verify that the response is empty indicating successful deletion. If the condition is met PASS, else FAIL</small> |

</details>

---

</details>

---

<details open>
<summary><strong>WebConfig</strong></summary>

# WebConfig

<details open>
<summary><strong>Test Case 50: Reject Invalid LAN Subdoc (Swapped DHCP IPs) via WebConfig</strong></summary>

## Test Case 50: TS_WEBCONFIG_PAMValidationUsingInvalidLanSubdoc

### Objective
Validate PAM via Webconfig Feature using an invalid LAN subdoc by verifying that an invalid LAN subdoc (with swapped DHCP start and end IP addresses) submitted via the webconfig server fails to update the DHCPv4 parameters on the DUT.

### Test Type
Negative

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.DHCPv4.Server.Pool.1.Enable | true |
| Device.DHCPv4.Server.Pool.1.IPRouters | 10.0.0.1 |
| Device.DHCPv4.Server.Pool.1.SubnetMask | 255.255.255.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.240 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.8 |
| Device.DHCPv4.Server.Pool.1.LeaseTime | 7200 |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET the current values of Device.DHCPv4.Server.Pool.1.Enable, Device.DHCPv4.Server.Pool.1.IPRouters, Device.DHCPv4.Server.Pool.1.SubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress, Device.DHCPv4.Server.Pool.1.MaxAddress, and Device.DHCPv4.Server.Pool.1.LeaseTime to record the baseline DHCPv4 configuration before applying the subdoc.</small> | <small>Verify that the current values of DHCPv4 parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the invalid LAN subdoc with swapped DHCP start and end IP addresses for the device MAC address.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to attempt to apply the invalid LAN subdoc.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.DHCPv4.Server.Pool.1.Enable, Device.DHCPv4.Server.Pool.1.IPRouters, Device.DHCPv4.Server.Pool.1.SubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress, Device.DHCPv4.Server.Pool.1.MaxAddress, and Device.DHCPv4.Server.Pool.1.LeaseTime to verify whether the DHCPv4 parameters remain unchanged after attempting to apply the invalid subdoc.</small> | <small>Verify that the DHCPv4 parameter values remain unchanged and equal the initial values retrieved before the test. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 51: Apply Valid LAN Subdoc and Verify DHCPv4 Update via WebConfig</strong></summary>

## Test Case 51: TS_WEBCONFIG_PAMValidationUsingLanSubdoc

### Objective
Validate PAM via Webconfig Feature using LAN subdoc by verifying that valid LAN subdoc configuration submitted via the webconfig server is successfully applied to DHCPv4 parameters on the DUT.

### Test Type
Positive

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.DHCPv4.Server.Pool.1.Enable | true |
| Device.DHCPv4.Server.Pool.1.IPRouters | 10.0.0.1 |
| Device.DHCPv4.Server.Pool.1.SubnetMask | 255.255.255.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.8 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.240 |
| Device.DHCPv4.Server.Pool.1.LeaseTime | 7200 |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET the current values of Device.DHCPv4.Server.Pool.1.Enable, Device.DHCPv4.Server.Pool.1.IPRouters, Device.DHCPv4.Server.Pool.1.SubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress, Device.DHCPv4.Server.Pool.1.MaxAddress, and Device.DHCPv4.Server.Pool.1.LeaseTime to record the baseline DHCPv4 configuration before applying the subdoc.</small> | <small>Verify that the current values of DHCPv4 parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the valid LAN subdoc containing the DHCPv4 configuration for the device MAC address.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to fetch and apply the LAN subdoc from the webconfig server.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.DHCPv4.Server.Pool.1.Enable, Device.DHCPv4.Server.Pool.1.IPRouters, Device.DHCPv4.Server.Pool.1.SubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress, Device.DHCPv4.Server.Pool.1.MaxAddress, and Device.DHCPv4.Server.Pool.1.LeaseTime to verify whether the DHCPv4 parameters were updated after applying the subdoc.</small> | <small>Verify that the DHCPv4 parameter values are updated as per the LAN subdoc configuration. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the LAN subdoc with the initial DHCPv4 parameter values to revert the configuration.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to apply the revert subdoc.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>GET Device.DHCPv4.Server.Pool.1.Enable, Device.DHCPv4.Server.Pool.1.IPRouters, Device.DHCPv4.Server.Pool.1.SubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress, Device.DHCPv4.Server.Pool.1.MaxAddress, and Device.DHCPv4.Server.Pool.1.LeaseTime to verify whether the DHCPv4 parameters have been restored to their initial values.</small> | <small>Verify that the DHCPv4 parameter values are reverted to their initial values. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 52: Reject Partial LAN Subdoc (Missing Parameter) via WebConfig</strong></summary>

## Test Case 52: TS_WEBCONFIG_PAMValidationUsingPartialLanSubdoc

### Objective
Validate PAM via Webconfig Feature using a partial LAN subdoc by verifying that a partial LAN subdoc (with one parameter removed) submitted via the webconfig server is rejected and the DHCPv4 parameters on the DUT remain unchanged.

### Test Type
Negative

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.DHCPv4.Server.Pool.1.Enable | true |
| Device.DHCPv4.Server.Pool.1.IPRouters | 10.0.0.1 |
| Device.DHCPv4.Server.Pool.1.SubnetMask | 255.255.255.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.8 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.240 |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET the current values of Device.DHCPv4.Server.Pool.1.Enable, Device.DHCPv4.Server.Pool.1.IPRouters, Device.DHCPv4.Server.Pool.1.SubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress, Device.DHCPv4.Server.Pool.1.MaxAddress, and Device.DHCPv4.Server.Pool.1.LeaseTime to record the baseline DHCPv4 configuration before applying the subdoc.</small> | <small>Verify that the current values of DHCPv4 parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the partial LAN subdoc (with one parameter removed) for the device MAC address.</small> | <small>Verify that the curl command fails and the response does not contain "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to attempt to apply the partial LAN subdoc.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.DHCPv4.Server.Pool.1.Enable, Device.DHCPv4.Server.Pool.1.IPRouters, Device.DHCPv4.Server.Pool.1.SubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress, Device.DHCPv4.Server.Pool.1.MaxAddress, and Device.DHCPv4.Server.Pool.1.LeaseTime to verify whether the DHCPv4 parameters remain unchanged after the rejected partial subdoc.</small> | <small>Verify that the DHCPv4 parameter values remain unchanged and equal the initial values retrieved before the test. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 53: Reject Invalid Port Forwarding Subdoc (Bad IP) via WebConfig</strong></summary>

## Test Case 53: TS_WEBCONFIG_PAMValidationUsingInvalidPortForwardingSubdoc

### Objective
Validate PAM via Webconfig Feature using an invalid PortForwarding subdoc by verifying that an invalid portforwarding subdoc (with an invalid InternalClient IP address) submitted via the webconfig server fails to create a port mapping profile on the DUT.

### Test Type
Negative

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_CISCO_COM_DeviceControl.FactoryReset | Router,Wifi,VoIP,Dect,MoCA |
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.NAT.PortMapping.1.InternalClient | 10:0.0.123 |
| Device.NAT.PortMapping.1.ExternalPortEndRange | 23 |
| Device.NAT.PortMapping.1.Enable | true |
| Device.NAT.PortMapping.1.Protocol | BOTH |
| Device.NAT.PortMapping.1.Description | telnet |
| Device.NAT.PortMapping.1.ExternalPort | 23 |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.X_CISCO_COM_DeviceControl.FactoryReset to "Router,Wifi,VoIP,Dect,MoCA" to perform a factory reset on the DUT and restore it to default settings. Wait 300 seconds for the DUT to restart and restore its previous state.</small> | <small>Verify that the factory reset is initiated successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the invalid portforwarding subdoc with InternalClient set to `10:0.0.123` (an invalid IP address format) for the device MAC address.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to attempt to apply the invalid portforwarding subdoc. Wait 10 seconds.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.NAT.PortMappingNumberOfEntries to verify that no port mapping profile was created after the invalid subdoc was rejected.</small> | <small>Verify that Device.NAT.PortMappingNumberOfEntries equals 0, confirming that no port mapping profile was created. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 54: Reject Partial Port Forwarding Subdoc (Missing Parameter) via WebConfig</strong></summary>

## Test Case 54: TS_WEBCONFIG_PAMValidationUsingPartialPortForwardingSubdoc

### Objective
Validate PAM via Webconfig Feature using a partial PortForwarding subdoc by verifying that a partial portforwarding subdoc (with one parameter removed) submitted via the webconfig server is rejected and no port mapping profile is created on the DUT.

### Test Type
Negative

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_CISCO_COM_DeviceControl.FactoryReset | Router,Wifi,VoIP,Dect,MoCA |
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.NAT.PortMapping.1.InternalClient | 10.0.0.111 |
| Device.NAT.PortMapping.1.ExternalPortEndRange | 23 |
| Device.NAT.PortMapping.1.Enable | true |
| Device.NAT.PortMapping.1.Protocol | BOTH |
| Device.NAT.PortMapping.1.Description | telnet |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.X_CISCO_COM_DeviceControl.FactoryReset to "Router,Wifi,VoIP,Dect,MoCA" to perform a factory reset on the DUT and restore it to default settings. Wait 300 seconds for the DUT to restart and restore its previous state.</small> | <small>Verify that the factory reset is initiated successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the partial portforwarding subdoc (with one parameter removed) for the device MAC address.</small> | <small>Verify that the curl command fails and the response does not contain "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to attempt to apply the partial portforwarding subdoc. Wait 10 seconds.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.NAT.PortMappingNumberOfEntries to verify that no port mapping profile was created after the partial subdoc was rejected.</small> | <small>Verify that Device.NAT.PortMappingNumberOfEntries equals 0, confirming that no port mapping profile was created. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 55: Apply Valid Port Forwarding Subdoc and Verify NAT Mapping via WebConfig</strong></summary>

## Test Case 55: TS_WEBCONFIG_PAMValidationUsingPortForwardingSubdoc

### Objective
Validate PAM via Webconfig Feature using a PortForwarding subdoc by verifying that a valid portforwarding subdoc submitted via the webconfig server successfully creates a port mapping profile on the DUT with the configured values.

### Test Type
Positive

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_CISCO_COM_DeviceControl.FactoryReset | Router,Wifi,VoIP,Dect,MoCA |
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.NAT.PortMapping.1.InternalClient | 10.0.0.111 |
| Device.NAT.PortMapping.1.ExternalPortEndRange | 23 |
| Device.NAT.PortMapping.1.Enable | true |
| Device.NAT.PortMapping.1.Protocol | BOTH |
| Device.NAT.PortMapping.1.Description | telnet |
| Device.NAT.PortMapping.1.ExternalPort | 23 |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.X_CISCO_COM_DeviceControl.FactoryReset to "Router,Wifi,VoIP,Dect,MoCA" to perform a factory reset on the DUT and restore it to default settings. Wait 300 seconds for the DUT to restart and restore its previous state.</small> | <small>Verify that the factory reset is initiated successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the valid portforwarding subdoc containing the port mapping configuration for the device MAC address.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to apply the portforwarding subdoc. Wait 10 seconds for the configuration to be applied.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.NAT.PortMappingNumberOfEntries to check whether a port mapping profile was created after applying the subdoc.</small> | <small>Verify that Device.NAT.PortMappingNumberOfEntries equals 1, confirming that a port mapping profile was created. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.NAT.PortMapping.1.InternalClient, Device.NAT.PortMapping.1.ExternalPortEndRange, Device.NAT.PortMapping.1.Enable, Device.NAT.PortMapping.1.Protocol, Device.NAT.PortMapping.1.Description, and Device.NAT.PortMapping.1.ExternalPort to verify the port mapping profile values.</small> | <small>Verify that the port mapping profile values match the portforwarding subdoc configuration. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>DELETE the port mapping table entry Device.NAT.PortMapping.1. from the DUT to clean up the profile created during the test.</small> | <small>Verify that the port mapping profile is deleted successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 56: Reject Invalid 2.4GHz Private SSID Subdoc (SSID Too Long) via WebConfig</strong></summary>

## Test Case 56: TS_WEBCONFIG_2G_WIFIValidationUsingInvalidPrivateSSIDSubdoc

### Objective
Validate WiFi via Webconfig Feature using an invalid 2.4GHz privatessid subdoc by verifying that an invalid privatessid subdoc (with an SSID name exceeding the maximum allowed length) submitted via the webconfig server fails to update the 2.4GHz WiFi parameters on the DUT.

### Test Type
Negative

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.WiFi.SSID.1.SSID | abcbaaba1234567ab-cabacabacabsbcagsafdgyw |
| Device.WiFi.SSID.1.Enable | True |
| Device.WiFi.AccessPoint.1.SSIDAdvertisementEnabled | True |
| Device.WiFi.AccessPoint.1.Security.X_CISCO_COM_EncryptionMethod | AES |
| Device.WiFi.AccessPoint.1.Security.ModeEnabled | WPA2-Personal |
| Device.WiFi.AccessPoint.1.Security.X_COMCAST-COM_KeyPassphrase | rdkm@1234 |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.WiFi.RadioNumberOfEntries to determine the number of radios supported on the DUT.</small> | <small>Verify that the number of radio entries is retrieved successfully and is 2 or 3. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET the current WiFi parameter values for all supported radios (2.4GHz (AP index 1) and 5GHz (AP index 2), and additionally 6GHz (AP index 17) on 3-radio platforms) to record the baseline WiFi configuration before applying the subdoc.</small> | <small>Verify that the current WiFi parameter values for all supported radios are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the invalid privatessid subdoc for the 2.4GHz radio (AP index 1) with an SSID name `abcbaaba1234567ab-cabacabacabsbcagsafdgyw` that exceeds the maximum allowed length for the device MAC address.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to attempt to apply the invalid privatessid subdoc. Wait 10 seconds.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.WiFi.SSID.1.SSID, Device.WiFi.SSID.1.Enable, Device.WiFi.AccessPoint.1.SSIDAdvertisementEnabled, Device.WiFi.AccessPoint.1.Security.X_CISCO_COM_EncryptionMethod, Device.WiFi.AccessPoint.1.Security.ModeEnabled, and Device.WiFi.AccessPoint.1.Security.X_COMCAST-COM_KeyPassphrase to verify whether the 2.4GHz WiFi parameters remain unchanged after the invalid subdoc was rejected.</small> | <small>Verify that the 2.4GHz WiFi parameter values remain unchanged and do not match the invalid subdoc values, confirming that the invalid subdoc was not applied. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 57: Reject Partial 2.4GHz Private SSID Subdoc (Missing Parameter) via WebConfig</strong></summary>

## Test Case 57: TS_WEBCONFIG_2G_WIFIValidationUsingPartialPrivateSSIDSubdoc

### Objective
Validate WiFi via Webconfig Feature using a partial 2.4GHz privatessid subdoc by verifying that a partial privatessid subdoc (with one security parameter removed) submitted via the webconfig server fails to update the 2.4GHz WiFi parameters on the DUT.

### Test Type
Negative

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.WiFi.SSID.1.SSID | PrivateSSID_2G |
| Device.WiFi.SSID.1.Enable | True |
| Device.WiFi.AccessPoint.1.SSIDAdvertisementEnabled | True |
| Device.WiFi.AccessPoint.1.Security.X_CISCO_COM_EncryptionMethod | AES |
| Device.WiFi.AccessPoint.1.Security.ModeEnabled | WPA2-Personal |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.WiFi.RadioNumberOfEntries to determine the number of radios supported on the DUT.</small> | <small>Verify that the number of radio entries is retrieved successfully and is 2 or 3. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET the current WiFi parameter values for all supported radios (2.4GHz (AP index 1) and 5GHz (AP index 2), and additionally 6GHz (AP index 17) on 3-radio platforms) to record the baseline WiFi configuration before applying the subdoc.</small> | <small>Verify that the current WiFi parameter values for all supported radios are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the partial privatessid subdoc for the 2.4GHz radio (AP index 1) with one security parameter removed for the device MAC address.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to attempt to apply the partial privatessid subdoc. Wait 10 seconds.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.WiFi.SSID.1.SSID, Device.WiFi.SSID.1.Enable, Device.WiFi.AccessPoint.1.SSIDAdvertisementEnabled, Device.WiFi.AccessPoint.1.Security.X_CISCO_COM_EncryptionMethod, Device.WiFi.AccessPoint.1.Security.ModeEnabled, and Device.WiFi.AccessPoint.1.Security.X_COMCAST-COM_KeyPassphrase to verify whether the 2.4GHz WiFi parameters remain unchanged after the partial subdoc was not applied.</small> | <small>Verify that the 2.4GHz WiFi parameter values remain unchanged and do not match the partial subdoc values, confirming that the partial subdoc was not applied. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 58: Apply Valid 2.4GHz Private SSID Subdoc and Verify WiFi Update via WebConfig</strong></summary>

## Test Case 58: TS_WEBCONFIG_2G_WIFIValidationUsingPrivateSSIDSubdoc

### Objective
Validate WiFi via Webconfig Feature using a 2.4GHz privatessid subdoc by verifying that a valid privatessid subdoc submitted via the webconfig server is successfully applied to the 2.4GHz WiFi parameters on the DUT.

### Test Type
Positive

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.WiFi.SSID.1.SSID | PrivateSSID_2G |
| Device.WiFi.SSID.1.Enable | True |
| Device.WiFi.AccessPoint.1.SSIDAdvertisementEnabled | True |
| Device.WiFi.AccessPoint.1.Security.X_CISCO_COM_EncryptionMethod | AES |
| Device.WiFi.AccessPoint.1.Security.ModeEnabled | WPA2-Personal |
| Device.WiFi.AccessPoint.1.Security.X_COMCAST-COM_KeyPassphrase | rdkm@1234 |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.WiFi.RadioNumberOfEntries to determine the number of radios supported on the DUT.</small> | <small>Verify that the number of radio entries is retrieved successfully and is 2 or 3. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET the current WiFi parameter values for all supported radios (2.4GHz (AP index 1) and 5GHz (AP index 2), and additionally 6GHz (AP index 17) on 3-radio platforms) to record the baseline WiFi configuration before applying the subdoc.</small> | <small>Verify that the current WiFi parameter values for all supported radios are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the valid privatessid subdoc targeting the 2.4GHz radio (AP index 1) with the updated WiFi configuration for the device MAC address.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to apply the privatessid subdoc. Wait 10 seconds for the configuration to be applied.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.WiFi.SSID.1.SSID, Device.WiFi.SSID.1.Enable, Device.WiFi.AccessPoint.1.SSIDAdvertisementEnabled, Device.WiFi.AccessPoint.1.Security.X_CISCO_COM_EncryptionMethod, Device.WiFi.AccessPoint.1.Security.ModeEnabled, and Device.WiFi.AccessPoint.1.Security.X_COMCAST-COM_KeyPassphrase to verify whether the 2.4GHz WiFi parameters were updated after applying the subdoc.</small> | <small>Verify that the 2.4GHz WiFi parameter values are updated as per the privatessid subdoc configuration. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the privatessid subdoc with the initial WiFi parameter values for all supported radios to revert the configuration.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to apply the revert subdoc. Wait 10 seconds.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>GET Device.WiFi.SSID.1.SSID, Device.WiFi.SSID.1.Enable, Device.WiFi.AccessPoint.1.SSIDAdvertisementEnabled, Device.WiFi.AccessPoint.1.Security.X_CISCO_COM_EncryptionMethod, Device.WiFi.AccessPoint.1.Security.ModeEnabled, and Device.WiFi.AccessPoint.1.Security.X_COMCAST-COM_KeyPassphrase to verify whether the 2.4GHz WiFi parameters have been restored to their initial values.</small> | <small>Verify that the 2.4GHz WiFi parameter values are reverted to their initial values. If the condition is met CONTINUE, else FAIL</small> |
| <small>11</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 59: Reject Invalid 5GHz Private SSID Subdoc (SSID Too Long) via WebConfig</strong></summary>

## Test Case 59: TS_WEBCONFIG_5G_WIFIValidationUsingInvalidPrivateSSIDSubdoc

### Objective
Validate WiFi via Webconfig Feature using an invalid 5GHz privatessid subdoc by verifying that an invalid privatessid subdoc (with an SSID name exceeding the maximum allowed length) submitted via the webconfig server fails to update the 5GHz WiFi parameters on the DUT.

### Test Type
Negative

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.WiFi.SSID.2.SSID | abcbaaba1234567ab-cabacabacabsbcagsafdgyw |
| Device.WiFi.SSID.2.Enable | True |
| Device.WiFi.AccessPoint.2.SSIDAdvertisementEnabled | True |
| Device.WiFi.AccessPoint.2.Security.X_CISCO_COM_EncryptionMethod | AES |
| Device.WiFi.AccessPoint.2.Security.ModeEnabled | WPA2-Personal |
| Device.WiFi.AccessPoint.2.Security.X_COMCAST-COM_KeyPassphrase | rdkm@1234 |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.WiFi.RadioNumberOfEntries to determine the number of radios supported on the DUT.</small> | <small>Verify that the number of radio entries is retrieved successfully and is 2 or 3. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET the current WiFi parameter values for all supported radios (2.4GHz (AP index 1) and 5GHz (AP index 2), and additionally 6GHz (AP index 17) on 3-radio platforms) to record the baseline WiFi configuration before applying the subdoc.</small> | <small>Verify that the current WiFi parameter values for all supported radios are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the invalid privatessid subdoc for the 5GHz radio (AP index 2) with an SSID name `abcbaaba1234567ab-cabacabacabsbcagsafdgyw` that exceeds the maximum allowed length for the device MAC address.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to attempt to apply the invalid privatessid subdoc. Wait 10 seconds.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.WiFi.SSID.2.SSID, Device.WiFi.SSID.2.Enable, Device.WiFi.AccessPoint.2.SSIDAdvertisementEnabled, Device.WiFi.AccessPoint.2.Security.X_CISCO_COM_EncryptionMethod, Device.WiFi.AccessPoint.2.Security.ModeEnabled, and Device.WiFi.AccessPoint.2.Security.X_COMCAST-COM_KeyPassphrase to verify whether the 5GHz WiFi parameters remain unchanged after the invalid subdoc was rejected.</small> | <small>Verify that the 5GHz WiFi parameter values remain unchanged and do not match the invalid subdoc values, confirming that the invalid subdoc was not applied. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 60: Reject Partial 5GHz Private SSID Subdoc (Missing Parameter) via WebConfig</strong></summary>

## Test Case 60: TS_WEBCONFIG_5G_WIFIValidationUsingPartialPrivateSSIDSubdoc

### Objective
Validate WiFi via Webconfig Feature using a partial 5GHz privatessid subdoc by verifying that a partial privatessid subdoc (with one security parameter removed) submitted via the webconfig server fails to update the 5GHz WiFi parameters on the DUT.

### Test Type
Negative

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.WiFi.SSID.2.SSID | PrivateSSID_5G |
| Device.WiFi.SSID.2.Enable | True |
| Device.WiFi.AccessPoint.2.SSIDAdvertisementEnabled | True |
| Device.WiFi.AccessPoint.2.Security.X_CISCO_COM_EncryptionMethod | AES |
| Device.WiFi.AccessPoint.2.Security.ModeEnabled | WPA2-Personal |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.WiFi.RadioNumberOfEntries to determine the number of radios supported on the DUT.</small> | <small>Verify that the number of radio entries is retrieved successfully and is 2 or 3. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET the current WiFi parameter values for all supported radios (2.4GHz (AP index 1) and 5GHz (AP index 2), and additionally 6GHz (AP index 17) on 3-radio platforms) to record the baseline WiFi configuration before applying the subdoc.</small> | <small>Verify that the current WiFi parameter values for all supported radios are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the partial privatessid subdoc for the 5GHz radio (AP index 2) with one security parameter removed for the device MAC address.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to attempt to apply the partial privatessid subdoc. Wait 10 seconds.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.WiFi.SSID.2.SSID, Device.WiFi.SSID.2.Enable, Device.WiFi.AccessPoint.2.SSIDAdvertisementEnabled, Device.WiFi.AccessPoint.2.Security.X_CISCO_COM_EncryptionMethod, Device.WiFi.AccessPoint.2.Security.ModeEnabled, and Device.WiFi.AccessPoint.2.Security.X_COMCAST-COM_KeyPassphrase to verify whether the 5GHz WiFi parameters remain unchanged after the partial subdoc was not applied.</small> | <small>Verify that the 5GHz WiFi parameter values remain unchanged and do not match the partial subdoc values, confirming that the partial subdoc was not applied. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 61: Apply Valid 5GHz Private SSID Subdoc and Verify WiFi Update via WebConfig</strong></summary>

## Test Case 61: TS_WEBCONFIG_5G_WIFIValidationUsingPrivateSSIDSubdoc

### Objective
Validate WiFi via Webconfig Feature using a 5GHz privatessid subdoc by verifying that a valid privatessid subdoc submitted via the webconfig server is successfully applied to the 5GHz WiFi parameters on the DUT.

### Test Type
Positive

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.WiFi.SSID.2.SSID | PrivateSSID_5G |
| Device.WiFi.SSID.2.Enable | True |
| Device.WiFi.AccessPoint.2.SSIDAdvertisementEnabled | True |
| Device.WiFi.AccessPoint.2.Security.X_CISCO_COM_EncryptionMethod | AES |
| Device.WiFi.AccessPoint.2.Security.ModeEnabled | WPA2-Personal |
| Device.WiFi.AccessPoint.2.Security.X_COMCAST-COM_KeyPassphrase | rdkm@1234 |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.WiFi.RadioNumberOfEntries to determine the number of radios supported on the DUT.</small> | <small>Verify that the number of radio entries is retrieved successfully and is 2 or 3. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET the current WiFi parameter values for all supported radios (2.4GHz (AP index 1) and 5GHz (AP index 2), and additionally 6GHz (AP index 17) on 3-radio platforms) to record the baseline WiFi configuration before applying the subdoc.</small> | <small>Verify that the current WiFi parameter values for all supported radios are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the valid privatessid subdoc targeting the 5GHz radio (AP index 2) with the updated WiFi configuration for the device MAC address.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to apply the privatessid subdoc. Wait 10 seconds for the configuration to be applied.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.WiFi.SSID.2.SSID, Device.WiFi.SSID.2.Enable, Device.WiFi.AccessPoint.2.SSIDAdvertisementEnabled, Device.WiFi.AccessPoint.2.Security.X_CISCO_COM_EncryptionMethod, Device.WiFi.AccessPoint.2.Security.ModeEnabled, and Device.WiFi.AccessPoint.2.Security.X_COMCAST-COM_KeyPassphrase to verify whether the 5GHz WiFi parameters were updated after applying the subdoc.</small> | <small>Verify that the 5GHz WiFi parameter values are updated as per the privatessid subdoc configuration. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the privatessid subdoc with the initial WiFi parameter values for all supported radios to revert the configuration.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to apply the revert subdoc. Wait 10 seconds.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>GET Device.WiFi.SSID.2.SSID, Device.WiFi.SSID.2.Enable, Device.WiFi.AccessPoint.2.SSIDAdvertisementEnabled, Device.WiFi.AccessPoint.2.Security.X_CISCO_COM_EncryptionMethod, Device.WiFi.AccessPoint.2.Security.ModeEnabled, and Device.WiFi.AccessPoint.2.Security.X_COMCAST-COM_KeyPassphrase to verify whether the 5GHz WiFi parameters have been restored to their initial values.</small> | <small>Verify that the 5GHz WiFi parameter values are reverted to their initial values. If the condition is met CONTINUE, else FAIL</small> |
| <small>11</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 62: Reject Invalid 6GHz Private SSID Subdoc (SSID Too Long) via WebConfig</strong></summary>

## Test Case 62: TS_WEBCONFIG_6G_WIFIValidationUsingInvalidPrivateSSIDSubdoc

### Objective
Validate WiFi via Webconfig Feature using an invalid 6GHz privatessid subdoc by verifying that an invalid privatessid subdoc (with an SSID name exceeding the maximum allowed length) submitted via the webconfig server fails to update the 6GHz WiFi parameters on the DUT.

### Test Type
Negative

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.WiFi.SSID.17.SSID | abcbaaba1234567ab-cabacabacabsbcagsafdgyw |
| Device.WiFi.SSID.17.Enable | True |
| Device.WiFi.AccessPoint.17.SSIDAdvertisementEnabled | True |
| Device.WiFi.AccessPoint.17.Security.X_CISCO_COM_EncryptionMethod | AES |
| Device.WiFi.AccessPoint.17.Security.ModeEnabled | WPA3-Personal |
| Device.WiFi.AccessPoint.17.Security.X_COMCAST-COM_KeyPassphrase | rdkm@1234 |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.WiFi.RadioNumberOfEntries to determine the number of radios supported on the DUT.</small> | <small>Verify that the number of radio entries is retrieved successfully and is 2 or 3. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET the current WiFi parameter values for all supported radios (2.4GHz (AP index 1), 5GHz (AP index 2), and 6GHz (AP index 17)) to record the baseline WiFi configuration before applying the subdoc.</small> | <small>Verify that the current WiFi parameter values for all supported radios are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the invalid privatessid subdoc for the 6GHz radio (AP index 17) with an SSID name `abcbaaba1234567ab-cabacabacabsbcagsafdgyw` that exceeds the maximum allowed length for the device MAC address.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to attempt to apply the invalid privatessid subdoc. Wait 10 seconds.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.WiFi.SSID.17.SSID, Device.WiFi.SSID.17.Enable, Device.WiFi.AccessPoint.17.SSIDAdvertisementEnabled, Device.WiFi.AccessPoint.17.Security.X_CISCO_COM_EncryptionMethod, Device.WiFi.AccessPoint.17.Security.ModeEnabled, and Device.WiFi.AccessPoint.17.Security.X_COMCAST-COM_KeyPassphrase to verify whether the 6GHz WiFi parameters remain unchanged after the invalid subdoc was rejected.</small> | <small>Verify that the 6GHz WiFi parameter values remain unchanged and do not match the invalid subdoc values, confirming that the invalid subdoc was not applied. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 63: Reject Partial 6GHz Private SSID Subdoc (Missing Parameter) via WebConfig</strong></summary>

## Test Case 63: TS_WEBCONFIG_6G_WIFIValidationUsingPartialPrivateSSIDSubdoc

### Objective
Validate WiFi via Webconfig Feature using a partial 6GHz privatessid subdoc by verifying that a partial privatessid subdoc (with one security parameter removed) submitted via the webconfig server fails to update the 6GHz WiFi parameters on the DUT.

### Test Type
Negative

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.WiFi.SSID.17.SSID | PrivateSSID_6G |
| Device.WiFi.SSID.17.Enable | True |
| Device.WiFi.AccessPoint.17.SSIDAdvertisementEnabled | True |
| Device.WiFi.AccessPoint.17.Security.X_CISCO_COM_EncryptionMethod | AES |
| Device.WiFi.AccessPoint.17.Security.ModeEnabled | WPA3-Personal |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.WiFi.RadioNumberOfEntries to determine the number of radios supported on the DUT.</small> | <small>Verify that the number of radio entries is retrieved successfully and is 2 or 3. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET the current WiFi parameter values for all supported radios (2.4GHz (AP index 1), 5GHz (AP index 2), and 6GHz (AP index 17)) to record the baseline WiFi configuration before applying the subdoc.</small> | <small>Verify that the current WiFi parameter values for all supported radios are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the partial privatessid subdoc for the 6GHz radio (AP index 17) with one security parameter removed for the device MAC address.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to attempt to apply the partial privatessid subdoc. Wait 10 seconds.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.WiFi.SSID.17.SSID, Device.WiFi.SSID.17.Enable, Device.WiFi.AccessPoint.17.SSIDAdvertisementEnabled, Device.WiFi.AccessPoint.17.Security.X_CISCO_COM_EncryptionMethod, Device.WiFi.AccessPoint.17.Security.ModeEnabled, and Device.WiFi.AccessPoint.17.Security.X_COMCAST-COM_KeyPassphrase to verify whether the 6GHz WiFi parameters remain unchanged after the partial subdoc was not applied.</small> | <small>Verify that the 6GHz WiFi parameter values remain unchanged and do not match the partial subdoc values, confirming that the partial subdoc was not applied. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details open>
<summary><strong>Test Case 64: Apply Valid 6GHz Private SSID Subdoc and Verify WiFi Update via WebConfig</strong></summary>

## Test Case 64: TS_WEBCONFIG_6G_WIFIValidationUsingPrivateSSIDSubdoc

### Objective
Validate WiFi via Webconfig Feature using a 6GHz privatessid subdoc by verifying that a valid privatessid subdoc submitted via the webconfig server is successfully applied to the 6GHz WiFi parameters on the DUT.

### Test Type
Positive

### Test Environment
| Component |
|:---|
| DUT - Device under test |
| Webconfig Server - Remote configuration server |

### Test Configuration
| Parameter | Value |
|:---|:---|
| Device.X_RDK_WebConfig.URL | As per test configuration |
| Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry | As per test configuration |
| Device.X_RDK_WebConfig.ForceSync | root |
| Device.WiFi.SSID.17.SSID | PrivateSSID_6G |
| Device.WiFi.SSID.17.Enable | True |
| Device.WiFi.AccessPoint.17.SSIDAdvertisementEnabled | True |
| Device.WiFi.AccessPoint.17.Security.X_CISCO_COM_EncryptionMethod | AES |
| Device.WiFi.AccessPoint.17.Security.ModeEnabled | WPA3-Personal |
| Device.WiFi.AccessPoint.17.Security.X_COMCAST-COM_KeyPassphrase | rdkm@1234 |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Retrieve the device MAC address from DUT.</small> | <small>Verify that the MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to check whether the webconfig server URL is already configured on the DUT. If not already configured with the webconfig server URL, SET them to point to the webconfig server.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are configured with the webconfig server URL. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.WiFi.RadioNumberOfEntries to determine the number of radios supported on the DUT.</small> | <small>Verify that the number of radio entries is retrieved successfully and is 2 or 3. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET the current WiFi parameter values for all supported radios (2.4GHz (AP index 1), 5GHz (AP index 2), and 6GHz (AP index 17)) to record the baseline WiFi configuration before applying the subdoc.</small> | <small>Verify that the current WiFi parameter values for all supported radios are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the valid privatessid subdoc targeting the 6GHz radio (AP index 17) with the updated WiFi configuration for the device MAC address.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to apply the privatessid subdoc. Wait 10 seconds for the configuration to be applied.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.WiFi.SSID.17.SSID, Device.WiFi.SSID.17.Enable, Device.WiFi.AccessPoint.17.SSIDAdvertisementEnabled, Device.WiFi.AccessPoint.17.Security.X_CISCO_COM_EncryptionMethod, Device.WiFi.AccessPoint.17.Security.ModeEnabled, and Device.WiFi.AccessPoint.17.Security.X_COMCAST-COM_KeyPassphrase to verify whether the 6GHz WiFi parameters were updated after applying the subdoc.</small> | <small>Verify that the 6GHz WiFi parameter values are updated as per the privatessid subdoc configuration. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Execute a curl POST command on the DUT to the webconfig server to submit the privatessid subdoc with the initial WiFi parameter values for all supported radios to revert the configuration.</small> | <small>Verify that the curl command executes successfully and the response contains "Request successful". If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>SET Device.X_RDK_WebConfig.ForceSync to root to trigger the webconfig service to apply the revert subdoc. Wait 10 seconds.</small> | <small>Verify that the trigger parameter is set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>GET Device.WiFi.SSID.17.SSID, Device.WiFi.SSID.17.Enable, Device.WiFi.AccessPoint.17.SSIDAdvertisementEnabled, Device.WiFi.AccessPoint.17.Security.X_CISCO_COM_EncryptionMethod, Device.WiFi.AccessPoint.17.Security.ModeEnabled, and Device.WiFi.AccessPoint.17.Security.X_COMCAST-COM_KeyPassphrase to verify whether the 6GHz WiFi parameters have been restored to their initial values.</small> | <small>Verify that the 6GHz WiFi parameter values are reverted to their initial values. If the condition is met CONTINUE, else FAIL</small> |
| <small>11</small> | <small>Revert Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry to their original values to restore the webconfig server settings to the pre-test state.</small> | <small>Verify that Device.X_RDK_WebConfig.URL and Device.X_RDK_WebConfig.SupplementaryServiceUrls.Telemetry are reverted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

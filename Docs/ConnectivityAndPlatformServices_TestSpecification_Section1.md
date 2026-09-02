# Connectivity and Platform Services Validation Suite - Section 1

## Test Specification Document for Connectivity and Platform Services Validation Suite - Section 1

<strong>Version</strong>: 1.0<br>
<strong>Date</strong>: August 2026<br>
<strong>Purpose</strong>: Low-level test specification coverage for Connectivity and Platform Services Validation.<br>
<strong>Maintained by</strong>: TDKB Test Automation Team

## Table of Contents

| # | Category | Description | Number of Tests |
|---|----------|-------------|:---:|
| 1 | ETHERNET | EthAgent process, parameter, interface, client, and telemetry validation | 10 |
| 2 | WIFI | Platform compliance, E2E connectivity, firewall, and MAC filter validation | 67 |
| 3 | Provisioning and Management | Device users, WEBUI, DNS/DHCP, RFC features, firewall security, and self-heal validation | 53 |
| 4 | Firmware Upgrade | Firmware upgrade via TR181 commands and XCONF server validation | 6 |
| 5 | Lan Manager Lite | Bridge mode, host table, NetworkDevicesStatus, and NetworkDevicesTraffic validations | 19 |
| 6 | Test And Diagnostics | Diagnostics state, IP ping, TraceRoute, NSLookup, UDP echo, and IP ping extended validations | 48 |
| 7 | DHCPv4 | LAN client DHCP configuration, IP range, lease time, subnet, and connectivity tests | 35 | 
| 8 | IPv6 | IPv6 functional, service status, behavioral and state transition validation | 22 | 
| 9 | Firewall | Packet Filtering validations | 51 |
| 10 | Cellular Manager | Interface and Connectivity, SIM validations | 14 | 

---

<details>
<summary><strong>ETHERNET</strong></summary>

# ETHERNET

<details>
<summary><strong>Process and Log Checks</strong></summary>

# Process and Log Checks

<details>
<summary><strong>Test Case 1: Verify CcspEthAgent process is running and ETHAGENTLog.txt.0 log file exists</strong></summary>

## Test Case 1: TS_ETHAGENT_CheckProcessAndLogFile

## Objectives
Validate the EthAgent component initialization by confirming the CcspEthAgent process is active and the ETHAGENTLog.txt.0 log file exists in the expected log directory.

## Test Case ID
TC_ETHAGENT_01

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| None | &nbsp; |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Check if CcspEthAgent process is running on the DUT</small> | <small>Verify CcspEthAgent process is running with a valid PID. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Check if /rdklogs/logs/ETHAGENTLog.txt.0 log file exists on the DUT</small> | <small>Verify ETHAGENTLog.txt.0 log file is present. If the condition is met PASS, else FAIL</small> |

</details>

---

</details>

---

<details>
<summary><strong>Parameter Validation</strong></summary>

# Parameter Validation

<details>
<summary><strong>Test Case 2: Verify Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled rejects unauthorized SET operations</strong></summary>

## Test Case 2: TS_ETHAGENT_SetWANEnabled

## Objectives
Validate the write-protection behavior of Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled by confirming that setting it to false on RPI and to true on real broadband devices both result in a failure response, ensuring unauthorized WAN mode changes are blocked.

## Test Case ID
TC_ETHAGENT_02

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled | false (for RPI) / true (for non-RPI devices) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get the device type from the DUT properties file</small> | <small>Verify device type is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If device type is RPI, attempt to SET Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to false; if device type is non-RPI, attempt to SET Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to true</small> | <small>Verify the SET operation returns failure (write-protection is enforced). If the condition is met PASS, else FAIL</small> |

</details>

---

</details>

---

<details>
<summary><strong>Interface and Client Checks</strong></summary>

# Interface and Client Checks

<details>
<summary><strong>Test Case 3: Verify MaxBitRate, CurrentBitRate are non-zero and DuplexMode is Full for LAN client interface</strong></summary>

## Test Case 3: TS_ETHAGENT_CheckBitRateAndDuplexMode

## Objectives
Validate Ethernet link properties by identifying the interface to which an active LAN client is connected, and confirming that MaxBitRate, CurrentBitRate are non-zero and DuplexMode is Full.

## Test Case ID
TC_ETHAGENT_03

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| None | &nbsp; |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Hosts.HostNumberOfEntries from the DUT</small> | <small>Verify at least one host is connected. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Hosts.Host.{i}.Layer1Interface for each host instance to find an Ethernet client; GET Device.Hosts.Host.{i}.Active to confirm the client is active</small> | <small>Verify an active Ethernet LAN client is found. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Hosts.Host.{i}.PhysAddress for the identified active Ethernet host instance</small> | <small>Verify MAC address of the LAN client is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress for each Ethernet interface instance and compare with the LAN client MAC</small> | <small>Verify the Ethernet interface connected to the LAN client is identified. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.Ethernet.Interface.{i}.MaxBitRate for the identified interface</small> | <small>Verify MaxBitRate is non-zero and non-empty. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.Ethernet.Interface.{i}.CurrentBitRate for the identified interface</small> | <small>Verify CurrentBitRate is non-zero and non-empty. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.Ethernet.Interface.{i}.DuplexMode for the identified interface</small> | <small>Verify DuplexMode is Full. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 4: Verify LAN client connected Ethernet interface Enable status is true and Status is Up</strong></summary>

## Test Case 4: TS_ETHAGENT_CheckInterfaceStatus

## Objectives
Validate Ethernet interface health by identifying the port serving an active LAN client and confirming that Enable is true and Status is Up via the TR-181 data model.

## Test Case ID
TC_ETHAGENT_04

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| None | &nbsp; |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Hosts.HostNumberOfEntries from the DUT</small> | <small>Verify at least one host is connected. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Hosts.Host.{i}.Layer1Interface for each host instance to find an Ethernet client; GET Device.Hosts.Host.{i}.Active to confirm the client is active</small> | <small>Verify an active Ethernet LAN client is found. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Hosts.Host.{i}.PhysAddress for the identified active Ethernet host instance</small> | <small>Verify MAC address of the LAN client is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress for each Ethernet interface instance and compare with the LAN client MAC</small> | <small>Verify the Ethernet interface connected to the LAN client is identified. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.Ethernet.Interface.{i}.Enable for the identified interface</small> | <small>Verify Enable is true. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.Ethernet.Interface.{i}.Status for the identified interface</small> | <small>Verify Status is Up. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 5: Verify AssociatedDeviceNumberOfEntries matches the count of active Ethernet LAN clients</strong></summary>

## Test Case 5: TS_ETHAGENT_CheckAssociatedDeviceNumberOfEntries

## Objectives
Validate the client count reporting of EthAgent by cross-referencing the number of active Ethernet hosts from the Host table with AssociatedDeviceNumberOfEntries for the matching interface.

## Test Case ID
TC_ETHAGENT_05

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| None | &nbsp; |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Hosts.HostNumberOfEntries from the DUT</small> | <small>Verify at least one host is connected. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Iterate through all host instances: GET Device.Hosts.Host.{i}.Layer1Interface and Device.Hosts.Host.{i}.Active to count active Ethernet clients; GET Device.Hosts.Host.{i}.PhysAddress for each active Ethernet host</small> | <small>Verify at least one active Ethernet LAN client is found and its MAC address is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress for each Ethernet interface instance and compare with the LAN client MAC</small> | <small>Verify the Ethernet interface connected to the LAN client is identified. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDeviceNumberOfEntries for the identified interface</small> | <small>Verify AssociatedDeviceNumberOfEntries equals the count of active Ethernet LAN clients identified from the Host table. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 6: Verify AssociatedDevice MAC address matches the active LAN client physical address</strong></summary>

## Test Case 6: TS_ETHAGENT_GetAssociatedDeviceMACAddress

## Objectives
Validate MAC address reporting accuracy by retrieving an active LAN client's physical address from the Host table and confirming it matches Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress on the corresponding Ethernet interface.

## Test Case ID
TC_ETHAGENT_06

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| None | &nbsp; |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Hosts.HostNumberOfEntries from the DUT</small> | <small>Verify at least one host is connected. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Hosts.Host.{i}.Layer1Interface for each host instance to find an Ethernet client; GET Device.Hosts.Host.{i}.Active to confirm the client is active</small> | <small>Verify an active Ethernet LAN client is found. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Hosts.Host.{i}.PhysAddress for the identified active Ethernet host instance</small> | <small>Verify MAC address of the LAN client is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress for each Ethernet interface instance and compare with the LAN client MAC</small> | <small>Verify Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress on the LAN client-connected interface matches the LAN client physical address. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 7: Verify active and inactive time values are non-negative for the active Ethernet LAN client</strong></summary>

## Test Case 7: TS_ETHAGENT_CheckActiveAndInActivetime

## Objectives
Validate the connection time tracking of EthAgent by identifying an active Ethernet client and confirming that X_CISCO_COM_ActiveTime and X_CISCO_COM_InactiveTime both return values greater than or equal to zero.

## Test Case ID
TC_ETHAGENT_10

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| None | &nbsp; |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Hosts.HostNumberOfEntries from the DUT</small> | <small>Verify at least one host is connected. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Hosts.Host.{i}.Layer1Interface for each host instance to find an Ethernet client; GET Device.Hosts.Host.{i}.Active to confirm the client is active</small> | <small>Verify an active Ethernet LAN client is found. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Hosts.Host.{i}.X_CISCO_COM_ActiveTime for the identified active Ethernet host instance</small> | <small>Verify X_CISCO_COM_ActiveTime value is greater than or equal to zero. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Hosts.Host.{i}.X_CISCO_COM_InactiveTime for the identified active Ethernet host instance</small> | <small>Verify X_CISCO_COM_InactiveTime value is greater than or equal to zero. If the condition is met PASS, else FAIL</small> |

</details>

---

</details>

---

<details>
<summary><strong>Telemetry Checks</strong></summary>

# Telemetry Checks

<details>
<summary><strong>Test Case 8: Verify ETH_MAC_{i} telemetry marker reports the correct client MAC address</strong></summary>

## Test Case 8: TS_ETHAGENT_CheckTelemetryMarkerWithEthClient_ETH_MAC

## Objectives
Validate Ethernet telemetry reporting by enabling Ethernet logging, setting a short log interval, and confirming the ETH_MAC_{i}: marker with a valid MAC value appears in eth_telemetry.txt for the client-connected interface index.

## Test Case ID
TC_ETHAGENT_7

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled | true (if not already enabled) |
| Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod | 10 |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Hosts.HostNumberOfEntries from the DUT</small> | <small>Verify at least one host is connected. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Hosts.Host.{i}.Layer1Interface for each host instance to find an Ethernet client; GET Device.Hosts.Host.{i}.PhysAddress for the identified Ethernet host</small> | <small>Verify an Ethernet LAN client is found and its MAC address is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Ethernet.InterfaceNumberOfEntries from the DUT</small> | <small>Verify at least one Ethernet interface is present. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress for each Ethernet interface instance and compare with the LAN client MAC</small> | <small>Verify the client-connected Ethernet interface index is identified. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled from the DUT</small> | <small>Verify the current Ethernet log enable state is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>If Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled is false, SET it to true on the DUT</small> | <small>Verify Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled is SET to true successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod from the DUT</small> | <small>Verify the current Ethernet log period is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod to 10 on the DUT</small> | <small>Verify Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod is SET to 10 successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>Check if /rdklogs/logs/eth_telemetry.txt log file exists on the DUT</small> | <small>Verify eth_telemetry.txt log file is present. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>Poll /rdklogs/logs/eth_telemetry.txt for the ETH_MAC_{i}: marker for the client-connected interface index, with polling for up to 15 minutes</small> | <small>Verify ETH_MAC_{i}: marker is found with a valid non-empty MAC value. If the condition is met CONTINUE, else FAIL</small> |
| <small>11</small> | <small>Compare MAC value retrieved from ETH_MAC_{i}: marker with Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress for the client-connected interface</small> | <small>Verify MAC value from ETH_MAC_{i}: marker matches Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress. If the condition is met PASS, else FAIL</small> |
| <small>12</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod to original value</small> | <small>&nbsp;</small> |
| <small>13</small> | <small>If Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled was changed, revert it to original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 9: Verify ETH_MAC_{i}_TOTAL_COUNT telemetry marker reports the correct connected device count</strong></summary>

## Test Case 9: TS_ETHAGENT_CheckTelemetryMarkerWithEthClient_ETH_MAC_TOTAL_COUNT

## Objectives
Validate total connected device count telemetry by enabling Ethernet logging, setting a short log interval, and confirming the ETH_MAC_{i}_TOTAL_COUNT: marker reports a non-zero value in eth_telemetry.txt for the client-connected interface.

## Test Case ID
TC_ETHAGENT_8

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled | true (if not already enabled) |
| Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod | 10 |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Hosts.HostNumberOfEntries from the DUT</small> | <small>Verify at least one host is connected. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Hosts.Host.{i}.Layer1Interface for each host instance to find an Ethernet client; GET Device.Hosts.Host.{i}.PhysAddress for the identified Ethernet host</small> | <small>Verify an Ethernet LAN client is found and its MAC address is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Ethernet.InterfaceNumberOfEntries from the DUT</small> | <small>Verify at least one Ethernet interface is present. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress for each Ethernet interface instance and compare with the LAN client MAC</small> | <small>Verify the client-connected Ethernet interface index is identified. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled from the DUT</small> | <small>Verify the current Ethernet log enable state is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>If Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled is false, SET it to true on the DUT</small> | <small>Verify Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled is SET to true successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod from the DUT</small> | <small>Verify the current Ethernet log period is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod to 10 on the DUT</small> | <small>Verify Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod is SET to 10 successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>Check if /rdklogs/logs/eth_telemetry.txt log file exists on the DUT</small> | <small>Verify eth_telemetry.txt log file is present. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>Poll /rdklogs/logs/eth_telemetry.txt for the ETH_MAC_{i}_TOTAL_COUNT: marker for the client-connected interface index, with polling for up to 15 minutes</small> | <small>Verify ETH_MAC_{i}_TOTAL_COUNT: marker is found with a valid non-empty count value. If the condition is met CONTINUE, else FAIL</small> |
| <small>11</small> | <small>GET Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDeviceNumberOfEntries for the client-connected interface; compare with count value from ETH_MAC_{i}_TOTAL_COUNT: marker</small> | <small>Verify count value from ETH_MAC_{i}_TOTAL_COUNT: marker matches Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDeviceNumberOfEntries. If the condition is met PASS, else FAIL</small> |
| <small>12</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod to original value</small> | <small>&nbsp;</small> |
| <small>13</small> | <small>If Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled was changed, revert it to original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 10: Verify ETH_PHYRATE_{i} telemetry marker reports a valid physical link rate</strong></summary>

## Test Case 10: TS_ETHAGENT_CheckTelemetryMarkerWithEthClient_ETH_PHYRATE

## Objectives
Validate physical link rate telemetry reporting by enabling Ethernet logging, setting a short log interval, and confirming the ETH_PHYRATE_{i}: marker with a valid non-empty rate value appears in eth_telemetry.txt for the client-connected interface.

## Test Case ID
TC_ETHAGENT_9

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled | true (if not already enabled) |
| Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod | 10 |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Hosts.HostNumberOfEntries from the DUT</small> | <small>Verify at least one host is connected. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Hosts.Host.{i}.Layer1Interface for each host instance to find an Ethernet client; GET Device.Hosts.Host.{i}.PhysAddress for the identified Ethernet host</small> | <small>Verify an Ethernet LAN client is found and its MAC address is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Ethernet.InterfaceNumberOfEntries from the DUT</small> | <small>Verify at least one Ethernet interface is present. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress for each Ethernet interface instance and compare with the LAN client MAC</small> | <small>Verify the client-connected Ethernet interface index is identified. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled from the DUT</small> | <small>Verify the current Ethernet log enable state is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>If Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled is false, SET it to true on the DUT</small> | <small>Verify Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled is SET to true successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod from the DUT</small> | <small>Verify the current Ethernet log period is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod to 10 on the DUT</small> | <small>Verify Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod is SET to 10 successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>Check if /rdklogs/logs/eth_telemetry.txt log file exists on the DUT</small> | <small>Verify eth_telemetry.txt log file is present. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>Poll /rdklogs/logs/eth_telemetry.txt for the ETH_PHYRATE_{i}: marker for the client-connected interface index, with polling for up to 15 minutes</small> | <small>Verify ETH_PHYRATE_{i}: marker is found with a valid non-empty rate value. If the condition is met CONTINUE, else FAIL</small> |
| <small>11</small> | <small>GET Device.Ethernet.Interface.{i}.CurrentBitRate for the client-connected interface; compare with rate value from ETH_PHYRATE_{i}: marker</small> | <small>Verify rate value from ETH_PHYRATE_{i}: marker matches Device.Ethernet.Interface.{i}.CurrentBitRate. If the condition is met PASS, else FAIL</small> |
| <small>12</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod to original value</small> | <small>&nbsp;</small> |
| <small>13</small> | <small>If Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled was changed, revert it to original value</small> | <small>&nbsp;</small> |

</details>

---

</details>

---

</details>

---

<details>
<summary><strong>WIFI</strong></summary>

# WIFI

<details>
<summary><strong>Test Case 1: Validate 2.4GHZ channel is non-overlapping</strong></summary>

## Test Case 1: TS_ONEWIFI_2.4GHZ_CheckRadioChannel_WithinNonOverlappingChannels

### Objectives
This test case is to check if 2.4GHZ Wifi Radio channel value retrieved is within the Non-overlapping Channel list

### Test Case ID
TC_ONEWIFI_114

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get the current Channel for Wi-Fi 2.4GHz using Device.WiFi.Radio.1.Channel.</small> | <small>Verify the current Channel for Wi-Fi 2.4GHz using Device.WiFi.Radio.1.Channel is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Check if the current Channel is one of the non-overlapping channel 1 or 6 or 11.</small> | <small>Verify whether the current Channel is one of the non-overlapping channel 1 or 6 or 11. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 2: Validate the 5GHz current channel is in PossibleChannels</strong></summary>

## Test Case 2: TS_ONEWIFI_5GHZ_CheckCurrentChannel

### Objectives
Verify that the 5GHz current radio channel is included in the PossibleChannels list.

### Test Case ID
TC_ONEWIFI_33

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.Radio.2.PossibleChannels.</small> | <small>Verify Device.WiFi.Radio.2.PossibleChannels is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>GET Device.WiFi.Radio.2.Channel.</small> | <small>Verify Device.WiFi.Radio.2.Channel is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Check if channel value is a subset of possible channel list.</small> | <small>Verify whether channel value is a subset of possible channel list. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 3: Validate 5GHZ channel is non-overlapping or a Non-DFS Channel</strong></summary>

## Test Case 3: TS_ONEWIFI_5GHZ_CheckRadioChannel_WithinNonOverlappingChannels

### Objectives
This test case is to Check if 5GHZ Wifi Radio channel value retrieved is within the Non-overlapping Channel list or a Non-DFS Channel

### Test Case ID
TC_ONEWIFI_115

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get the current Channel for Wi-Fi 5GHz using Device.WiFi.Radio.2.Channel.</small> | <small>Verify the current Channel for Wi-Fi 5GHz using Device.WiFi.Radio.2.Channel is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Check if the current Channel is one among the non-overlapping channel or a Non DFS Channel 36,40,44,48,149,153,157,161,165 or 52-64,100-140 respectively.</small> | <small>Verify whether the current Channel is one among the non-overlapping channel or a Non DFS Channel 36,40,44,48,149,153,157,161,165 or 52-64,100-140 respectively. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 4: Validate Radio 5GHz LastChange updates on enable or disable</strong></summary>

## Test Case 4: TS_ONEWIFI_5GHZ_RadioLastChange

### Objectives
Verify that the 5 GHz LastChange value updates when Radio 5GHz is enabled or disabled.

### Test Case ID
TC_ONEWIFI_34

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.Radio.2.Enable | [true,false] |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET and save Device.WiFi.Radio.2.Enable.</small> | <small>Verify and save Device.WiFi.Radio.2.Enable is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>GET and save Device.WiFi.Radio.2.LastChange.</small> | <small>Verify and save Device.WiFi.Radio.2.LastChange is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Toggle Device.WiFi.Radio.2.Enable.</small> | <small>Verify Device.WiFi.Radio.2.Enable is toggled successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>GET the value of Device.WiFi.Radio.2.LastChange and compare it with previous value.</small> | <small>Verify the value of Device.WiFi.Radio.2.LastChange and compare it with previous value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Check if lastchange value is less than the previously saved value.</small> | <small>Verify whether lastchange value is less than the previously saved value. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Restrore values of Device.WiFi.Radio.2.Enable, Device.WiFi.Radio.2.LastChange.</small> | <small>Verify restore values of Device.WiFi.Radio.2.Enable, Device.WiFi.Radio.2.LastChange. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 5: Validate LastChange value change on enabling/disabling 6ghz Radio</strong></summary>

## Test Case 5: TS_ONEWIFI_6GHZ_RadioLastChange

### Objectives
Check if LastChange value change on enabling/disabling 6ghz Radio

### Test Case ID
TC_ONEWIFI_286

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.Radio.3.Enable | [true/false] |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.Radio.3.Enable.</small> | <small>Verify Device.WiFi.Radio.3.Enable is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>GET Device.WiFi.Radio.3.LastChange.</small> | <small>Verify Device.WiFi.Radio.3.LastChange is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Toggle Device.WiFi.Radio.3.Enable.</small> | <small>Verify Device.WiFi.Radio.3.Enable is toggled successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>GET Device.WiFi.Radio.3.LastChange.</small> | <small>Verify Device.WiFi.Radio.3.LastChange is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Revert Device.WiFi.Radio.3.Enable to original value.</small> | <small>Verify Device.WiFi.Radio.3.Enable is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 6: Validate filtering mode is Allow when MAC filter is enabled with blacklist disabled</strong></summary>

## Test Case 6: TS_ONEWIFI_ACL_CheckMacFilteringMode_DisabledFilterAsBlackList

### Objectives
This test case verifies that when the MAC filter is enabled and the blacklist filter is set to false, the filtering mode is configured as Allow.

### Test Case ID
TC_ONEWIFI_304

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Set the mac filter enable to true for all radios if not already.</small> | <small>Verify the mac filter enable to true for all radios if not already is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Set the blacklist filter value of all radios to false if not already.</small> | <small>Verify the blacklist filter value of all radios to false if not already is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Verify if filtering mode is Allow.</small> | <small>Verify whether filtering mode is Allow. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Revert to original values of Mac Filter Enable and FilterAsBlacklist parameter if modified.</small> | <small>Verify the parameter is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 7: Validate at least one connected host is active</strong></summary>

## Test Case 7: TS_ONEWIFI_CheckHostActiveStatus_WithConnectedClient

### Objectives
Check if the Host Active status Device.Hosts.Host.{i}.Active is "true" for any connected client

### Test Case ID
TC_ONEWIFI_850

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Hosts.HostNumberOfEntries.</small> | <small>Verify Device.Hosts.HostNumberOfEntries is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>GET Device.Hosts.Host.{i}.Active.</small> | <small>Verify Device.Hosts.Host.{i}.Active is "true". If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>GET Device.Hosts.Host.{i}.HostName of active clients </small> | <small>Verify Device.Hosts.Host.{i}.HostName is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>GET Device.Hosts.Host.{i}.PhysAddress of active clients.</small> | <small>Verify Device.Hosts.Host.{i}.PhysAddress is retrieved successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 8: Validate radio reset count increments by 1 after ResetRadios</strong></summary>

## Test Case 8: TS_ONEWIFI_CheckResetCountIncrement_AfterResetRadios

### Objectives
To check if the radio reset count for all applicable radios are incremented by 1 when radio reset operation is done using Device.WiFi.X_CISCO_COM_ResetRadios.

### Test Case ID
TC_ONEWIFI_192

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.X_CISCO_COM_ResetRadios | true |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Retrieve the number of applicable radios.</small> | <small>Verify retrieve the number of applicable radios. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get the initial reset counts using Device.WiFi.Radio.{i}.RadioResetCount.</small> | <small>Verify the initial reset counts using Device.WiFi.Radio.{i}.RadioResetCount is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>SET Device.WiFi.X_CISCO_COM_ResetRadios to true.</small> | <small>Verify Device.WiFi.X_CISCO_COM_ResetRadios is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Sleep for 90s for the wifi reset to take effect.</small> | <small>Verify sleep for 90s for the wifi reset to take effect. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Retrieve the final reset counts using Device.WiFi.Radio.{i}.RadioResetCount.</small> | <small>Verify retrieve the final reset counts using Device.WiFi.Radio.{i}.RadioResetCount. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Check if the reset counts are incremented by 1.</small> | <small>Verify whether the reset counts are incremented by 1. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 9: Validate wifihealth.txt is created within 10 minutes after factory reset</strong></summary>

## Test Case 9: TS_ONEWIFI_CheckWiFiHealthLogFile

### Objectives
Validate if the file wifihealth.txt is created within 10 minutes of uptime after a factory reset.

### Test Case ID
TC_ONEWIFI_98

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.FactoryReset | Router,Wifi,VoIP,Dect,MoCA |
| Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval | 300 |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.X_CISCO_COM_DeviceControl.FactoryReset to Router,Wifi,VoIP,Dect,MoCA.</small> | <small>Verify Device.X_CISCO_COM_DeviceControl.FactoryReset is set to Router,Wifi,VoIP,Dect,MoCA successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to 300.</small> | <small>Verify Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval is set to 300 successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Check whether the wifihealth.txt file is present at /rdklogs/logs/wifihealth.txt.</small> | <small>Verify the wifihealth.txt file is present after factory reset and telemetry interval update. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 10: Validate all WiFi SSID statuses are down in bridge-static mode</strong></summary>

## Test Case 10: TS_ONEWIFI_CheckWiFiSSIDStatus_InBridgeMode

### Objectives
To verify that all WiFi SSID statuses are "down" when the DUT is set to bridge-static mode

### Test Case ID
TC_ONEWIFI_170

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode and record the initial value.</small> | <small>Verify the initial LAN mode is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>If initial LAN mode is router, SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to bridge-static.</small> | <small>Verify LAN mode transition to bridge-static succeeds. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode and confirm the value is bridge-static.</small> | <small>Verify LAN mode is bridge-static after SET. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>GET Device.WiFi.SSID.{i}.Status for all applicable radios in bridge-static mode.</small> | <small>Verify SSID statuses for all applicable radios are Down in bridge-static mode. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>If LAN mode was changed in this test, revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to the initial value.</small> | <small>Verify LAN mode revert succeeds and SSID status validation in bridge-static mode is complete. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 11: Validate bytes sent and received via telemetry marker is greater than zero</strong></summary>

## Test Case 11: TS_ONEWIFI_CheckTelemetryMarker_BytesSentAndReceived

### Objectives
Check if bytes sent and received via telemetry marker is greater than zero by changing the log interval.

### Test Case ID
TC_ONEWIFI_843

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WLAN Client - Wireless client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable | true |
| Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval | 300 |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>&nbsp;</small> | <small>Connect a WLAN client to the target SSID.</small> | <small>Verify the WLAN client is connected before continuing. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable and enable telemetry if it is disabled.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is retrieved and set to true when required. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get and store the current Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval value.</small> | <small>&nbsp;</small> | <small>Verify the current telemetry log interval is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to 300 seconds and confirm the updated value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is set to 300 seconds successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Check whether /rdklogs/logs/wifihealth.txt file is present.</small> | <small>&nbsp;</small> | <small>Verify wifihealth.txt is present before marker validation. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Check for any WIFI_BYTESSENTCLIENTS telemetry marker in wifihealth.txt and read the marker value.</small> | <small>&nbsp;</small> | <small>Verify WIFI_BYTESSENTCLIENTS marker is present and value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Verify that the WIFI_BYTESSENTCLIENTS telemetry marker value is greater than zero.</small> | <small>&nbsp;</small> | <small>Verify WIFI_BYTESSENTCLIENTS marker value is greater than zero. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>Check for any WIFI_BYTESRECEIVEDCLIENTS telemetry marker in wifihealth.txt and read the marker value.</small> | <small>&nbsp;</small> | <small>Verify WIFI_BYTESRECEIVEDCLIENTS marker is present and value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>Verify that the WIFI_BYTESRECEIVEDCLIENTS telemetry marker value is greater than zero.</small> | <small>&nbsp;</small> | <small>Verify WIFI_BYTESRECEIVEDCLIENTS marker value is greater than zero. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to its original value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is reverted successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>11</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to its original value if it was modified.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 12: Validate the macaddresses obtained from telemetry marker and host table are same</strong></summary>

## Test Case 12: TS_ONEWIFI_CheckTelemetryMarker_ConnectedClientMacaddress

### Objectives
Validate the macaddresses obtained from telemetry marker and host table are same

### Test Case ID
TC_ONEWIFI_849

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WLAN Client - Wireless client |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>&nbsp;</small> | <small>Connect a WLAN client to the target SSID.</small> | <small>Verify the WLAN client is connected before continuing. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Check whether /rdklogs/logs/wifihealth.txt file is present.</small> | <small>&nbsp;</small> | <small>Verify wifihealth.txt is present before marker validation. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Check for any WIFI_MAC_<index> telemetry marker in wifihealth.txt and read the marker value.</small> | <small>&nbsp;</small> | <small>Verify WIFI_MAC_<index> marker is present and value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Validate WIFI_MAC_<index> marker MAC value against the corresponding host table MAC address.</small> | <small>&nbsp;</small> | <small>Verify telemetry marker MAC matches the host table MAC address. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 13: Validate the error sent via telemetry marker is greater than or equal to zero</strong></summary>

## Test Case 13: TS_ONEWIFI_CheckTelemetryMarker_ErrorSent

### Objectives
This test case is to check if the error sent via telemetry marker is greater than or equal to zero by changing the log interval to 5 min

### Test Case ID
TC_ONEWIFI_840

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WLAN Client - Wireless client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable | true |
| Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval | 300 |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>&nbsp;</small> | <small>Connect a WLAN client to the target SSID.</small> | <small>Verify the WLAN client is connected before continuing. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable and enable telemetry if it is disabled.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is retrieved and set to true when required. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get and store the current Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval value.</small> | <small>&nbsp;</small> | <small>Verify the current telemetry log interval is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to 300 seconds and confirm the updated value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is set to 300 seconds successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Check whether /rdklogs/logs/wifihealth.txt file is present.</small> | <small>&nbsp;</small> | <small>Verify wifihealth.txt is present before marker validation. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Check for WIFI_ERRORSSENT telemetry marker in wifihealth.txt and read the marker value.</small> | <small>&nbsp;</small> | <small>Verify WIFI_ERRORSSENT marker is present and value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Verify that the WIFI_ERRORSSENT telemetry marker value is greater than zero.</small> | <small>&nbsp;</small> | <small>Verify WIFI_ERRORSSENT marker value is greater than zero. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to its original value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is reverted successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to its original value if it was modified.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 14: Validate the Retrans and Failed Retrans count via telemetry marker is greater than zero</strong></summary>

## Test Case 14: TS_ONEWIFI_CheckTelemetryMarker_FailedAndReTransCount

### Objectives
This test case is to check if the Retrans and Failed Retrans count via telemetry marker is greater than by changing the log interval to 5 min

### Test Case ID
TC_ONEWIFI_841

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WLAN Client - Wireless client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable | true |
| Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval | 300 |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>&nbsp;</small> | <small>Connect a WLAN client to the target SSID.</small> | <small>Verify the WLAN client is connected before continuing. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Check whether telemetry markers are enabled using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable. If disabled, enable telemetry and store the original value for revert.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is retrieved and set to true when required. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get and store the current Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval value.</small> | <small>&nbsp;</small> | <small>Verify the current telemetry log interval is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to 300 seconds and confirm the updated value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is set to 300 seconds successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Check whether /rdklogs/logs/wifihealth.txt file is present.</small> | <small>&nbsp;</small> | <small>Verify wifihealth.txt is present before marker validation. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Check for any WIFI_RETRANSCOUNT telemetry marker in wifihealth.txt and read the marker value.</small> | <small>&nbsp;</small> | <small>Verify WIFI_RETRANSCOUNT marker is present and value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Verify that the WIFI_RETRANSCOUNT telemetry marker value is greater than zero.</small> | <small>&nbsp;</small> | <small>Verify WIFI_RETRANSCOUNT marker value is greater than zero. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>Check for any WIFI_FAILEDRETRANSCOUNT telemetry marker in wifihealth.txt and read the marker value.</small> | <small>&nbsp;</small> | <small>Verify WIFI_FAILEDRETRANSCOUNT marker is present and value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>Verify that the WIFI_FAILEDRETRANSCOUNT telemetry marker value is greater than zero.</small> | <small>&nbsp;</small> | <small>Verify WIFI_FAILEDRETRANSCOUNT marker value is greater than zero. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to its original value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is reverted successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>11</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to its original value if it was modified.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 15: Validate the packets sent and received via telemetry marker is greater than zero</strong></summary>

## Test Case 15: TS_ONEWIFI_CheckTelemetryMarker_PacketsSent_PacketsReceived

### Objectives
Check if the packets sent and received via telemetry marker is greater than zero.

### Test Case ID
TC_ONEWIFI_842

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WLAN Client - Wireless client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable | true |
| Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval | 300 |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>&nbsp;</small> | <small>Connect a WLAN client to the target SSID.</small> | <small>Verify the WLAN client is connected before continuing. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable and enable telemetry if it is disabled.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is retrieved and set to true when required. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get and store the current Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval value.</small> | <small>&nbsp;</small> | <small>Verify the current telemetry log interval is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to 300 seconds and confirm the updated value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is set to 300 seconds successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Check whether /rdklogs/logs/wifihealth.txt file is present.</small> | <small>&nbsp;</small> | <small>Verify wifihealth.txt is present before marker validation. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Check for any WIFI_PACKETSSENTCLIENTS telemetry marker in wifihealth.txt and read the marker value.</small> | <small>&nbsp;</small> | <small>Verify WIFI_PACKETSSENTCLIENTS marker is present and value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Verify that the WIFI_PACKETSSENTCLIENTS telemetry marker value is greater than zero.</small> | <small>&nbsp;</small> | <small>Verify WIFI_PACKETSSENTCLIENTS marker value is greater than zero. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>Check for any WIFI_PACKETSRECEIVEDCLIENTS telemetry marker in wifihealth.txt and read the marker value.</small> | <small>&nbsp;</small> | <small>Verify WIFI_PACKETSRECEIVEDCLIENTS marker is present and value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>Verify that the WIFI_PACKETSRECEIVEDCLIENTS telemetry marker value is greater than zero.</small> | <small>&nbsp;</small> | <small>Verify WIFI_PACKETSRECEIVEDCLIENTS marker value is greater than zero. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to its original value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is reverted successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>11</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to its original value if it was modified.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 16: Validate the Retrans and Failed Retrans count via telemetry marker is greater than zero</strong></summary>

## Test Case 16: TS_ONEWIFI_CheckTelemetryMarker_RETRANSCOUNT_FAILEDRETRANSCOUNT

### Objectives
Check if the Retrans and Failed Retrans count via telemetry marker is greater than zero by changing the log interval to 5 min

### Test Case ID
TC_ONEWIFI_848

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WLAN Client - Wireless client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable | true |
| Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval | 300 |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>&nbsp;</small> | <small>Connect a WLAN client to the target SSID.</small> | <small>Verify the WLAN client is connected before continuing. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable and enable telemetry if it is disabled.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is retrieved and set to true when required. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get and store the current Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval value.</small> | <small>&nbsp;</small> | <small>Verify the current telemetry log interval is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to 300 seconds and confirm the updated value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is set to 300 seconds successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Check whether /rdklogs/logs/wifihealth.txt file is present.</small> | <small>&nbsp;</small> | <small>Verify wifihealth.txt is present before marker validation. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Check for any WIFI_RETRANSCOUNT telemetry marker in wifihealth.txt and read the marker value.</small> | <small>&nbsp;</small> | <small>Verify WIFI_RETRANSCOUNT marker is present and value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Verify that the WIFI_RETRANSCOUNT telemetry marker value is greater than zero.</small> | <small>&nbsp;</small> | <small>Verify WIFI_RETRANSCOUNT marker value is greater than zero. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>Check for any WIFI_FAILEDRETRANSCOUNT telemetry marker in wifihealth.txt and read the marker value.</small> | <small>&nbsp;</small> | <small>Verify WIFI_FAILEDRETRANSCOUNT marker is present and value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>Verify that the WIFI_FAILEDRETRANSCOUNT telemetry marker value is greater than zero.</small> | <small>&nbsp;</small> | <small>Verify WIFI_FAILEDRETRANSCOUNT marker value is greater than zero. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to its original value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is reverted successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>11</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to its original value if it was modified.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 17: Validate Retry and Multiple Retry count via telemetry marker is greater than zero</strong></summary>

## Test Case 17: TS_ONEWIFI_CheckTelemetryMarker_RetryAndMultipleRetryCount

### Objectives
Check if Retry and Multiple Retry count via telemetry marker is greater than zero by changing the log interval.

### Test Case ID
TC_ONEWIFI_845

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WLAN Client - Wireless client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable | true |
| Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval | 300 |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>&nbsp;</small> | <small>Connect a WLAN client to the target SSID.</small> | <small>Verify the WLAN client is connected before continuing. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable and enable telemetry if it is disabled.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is retrieved and set to true when required. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get and store the current Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval value.</small> | <small>&nbsp;</small> | <small>Verify the current telemetry log interval is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to 300 seconds and confirm the updated value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is set to 300 seconds successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Check whether /rdklogs/logs/wifihealth.txt file is present.</small> | <small>&nbsp;</small> | <small>Verify wifihealth.txt is present before marker validation. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Check for any WIFI_RETRYCOUNT telemetry marker in wifihealth.txt and read the marker value.</small> | <small>&nbsp;</small> | <small>Verify WIFI_RETRYCOUNT marker is present and value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Verify that the WIFI_RETRYCOUNT telemetry marker value is greater than zero.</small> | <small>&nbsp;</small> | <small>Verify WIFI_RETRYCOUNT marker value is greater than zero. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>Check for any WIFI_MULTIPLERETRYCOUNT telemetry marker in wifihealth.txt and read the marker value.</small> | <small>&nbsp;</small> | <small>Verify WIFI_MULTIPLERETRYCOUNT marker is present and value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>Verify that the WIFI_MULTIPLERETRYCOUNT telemetry marker value is greater than zero.</small> | <small>&nbsp;</small> | <small>Verify WIFI_MULTIPLERETRYCOUNT marker value is greater than zero. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to its original value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is reverted successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>11</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to its original value if it was modified.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 18: To check WIFI_ACS_ is populating correctly in wifihealth.txt</strong></summary>

## Test Case 18: TS_ONEWIFI_CheckTelemetryMarker_WIFI_ACS

### Objectives
To check WIFI_ACS_ is populating correctly in wifihealth.txt

### Test Case ID
TC_ONEWIFI_847

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable | true |
| Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval | 300 |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable and enable telemetry if it is disabled.</small> | <small>Verify telemetry enable status is retrieved and set to true when required. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get and store the current Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval value.</small> | <small>Verify the current telemetry log interval is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to 300 seconds and confirm the updated value.</small> | <small>Verify telemetry log interval is set to 300 seconds successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Check whether /rdklogs/logs/wifihealth.txt file is present.</small> | <small>Verify wifihealth.txt is present before marker validation. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Check for any WIFI_ACS_<index> telemetry marker in wifihealth.txt and read the marker value.</small> | <small>Verify WIFI_ACS_<index> marker is present and value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Validate the WIFI_ACS telemetry marker value.</small> | <small>Verify WIFI_ACS telemetry marker value is valid. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to its original value.</small> | <small>Verify telemetry log interval is reverted successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to its original value if it was modified.</small> | <small>Verify telemetry enable status is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 19: Verify WIFI_MAC_ telemetry marker in wifihealth matches the connected client MAC in the Host table</strong></summary>

## Test Case 19: TS_ONEWIFI_CheckTelemetryMarker_WIFI_MAC

### Objectives
Check the WiFi Telemetry marker WIFI_MAC_ connected client is populating in wifihealth log and verify that its value matches the MAC address in the host table

### Test Case ID
TC_ONEWIFI_846

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WLAN Client - Wireless client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable | true |
| Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval | 300 |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>&nbsp;</small> | <small>Connect a WLAN client to the target SSID.</small> | <small>Verify the WLAN client is connected before continuing. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable and enable telemetry if it is disabled.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is retrieved and set to true when required. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get and store the current Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval value.</small> | <small>&nbsp;</small> | <small>Verify the current telemetry log interval is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to 300 seconds and confirm the updated value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is set to 300 seconds successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Check whether /rdklogs/logs/wifihealth.txt file is present.</small> | <small>&nbsp;</small> | <small>Verify wifihealth.txt is present before marker validation. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Check for any WIFI_MAC_<index> telemetry marker in wifihealth.txt and read the marker value.</small> | <small>&nbsp;</small> | <small>Verify WIFI_MAC_<index> marker is present and value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Validate WIFI_MAC_<index> marker MAC value against the corresponding host table MAC address.</small> | <small>&nbsp;</small> | <small>Verify telemetry marker MAC matches the host table MAC address. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to its original value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is reverted successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to its original value if it was modified.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 20: Validate the telemetry marker WIFI_VAP_PERCENT_UP percent listed are within the range</strong></summary>

## Test Case 20: TS_ONEWIFI_CheckTelemetryMarkerVAPPERCENTUP

### Objectives
This test case is to check if the telemetry marker WIFI_VAP_PERCENT_UP percent listed are within the range by changing the log interval

### Test Case ID
TC_ONEWIFI_109

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WLAN Client - Wireless client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable | true |
| Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval | 300 |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>&nbsp;</small> | <small>Connect a WLAN client to the target SSID.</small> | <small>Verify the WLAN client is connected before continuing. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable and enable telemetry if it is disabled.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is retrieved and set to true when required. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get and store the current Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval value.</small> | <small>&nbsp;</small> | <small>Verify the current telemetry log interval is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to 300 seconds and confirm the updated value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is set to 300 seconds successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Check whether /rdklogs/logs/wifihealth.txt file is present.</small> | <small>&nbsp;</small> | <small>Verify wifihealth.txt is present before marker validation. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Check for WIFI_VAP_PERCENT_UP telemetry marker values in wifihealth.txt and read all instances.</small> | <small>&nbsp;</small> | <small>Verify WIFI_VAP_PERCENT_UP marker values are present and non-empty. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Validate all WIFI_VAP_PERCENT_UP instances are within the expected range.</small> | <small>&nbsp;</small> | <small>Verify all VAP percent values are within the valid range. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to its original value.</small> | <small>&nbsp;</small> | <small>Verify telemetry log interval is reverted successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable to its original value if it was modified.</small> | <small>&nbsp;</small> | <small>Verify telemetry enable status is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 21: Test to disable SNR telemetry markers for all VAPs</strong></summary>

## Test Case 21: TS_ONEWIFI_DisableSNRMarker_FoAllVAP

### Objectives
Test to disable SNR telemetry markers for all available Virtual access points.

### Test Case ID
TC_ONEWIFI_88

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.SNRList | "" |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get the current telemetry SNR list.</small> | <small>Verify the current telemetry SNR list is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Set the SNR list as "" to disable for all virtual access points.</small> | <small>Verify the SNR list as "" to disable for all virtual access points is set successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.SNRList after set and verify the value is "".</small> | <small>Verify SNRList after set matches the expected empty value. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.SNRList to the original value.</small> | <small>Verify the parameter is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 22: Validate setting the WiFi client MAC address to an invalid value is not allowed</strong></summary>

## Test Case 22: TS_ONEWIFI_SetInvalidReportWifiClientMacAddress

### Objectives
Verify that setting the WiFi client MAC address to an invalid value is not allowed.

### Test Case ID
TC_ONEWIFI_119

### Test Type
Negative

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WLAN Client - Wireless client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.X_RDKCENTRAL-COM_Report.WifiClient.MacAddress | FFFFFFFFFF |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>Get the current value of WifiClient Mac Address.</small> | <small>&nbsp;</small> | <small>Verify the current value of WifiClient Mac Address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Set Device.WiFi.X_RDKCENTRAL-COM_Report.WifiClient.MacAddress to invalid value FFFFFFFFFF with type unsignedint.</small> | <small>&nbsp;</small> | <small>Verify the set operation fails for invalid MAC input. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>If the invalid set operation unexpectedly succeeds, revert Device.WiFi.X_RDKCENTRAL-COM_Report.WifiClient.MacAddress to the original value.</small> | <small>&nbsp;</small> | <small>Verify original MAC value is restored successfully when revert is required. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 23: Test to enable SNR telemetry markers for all VAPs</strong></summary>

## Test Case 23: TS_ONEWIFI_SetSNRMarker_ForAllVAP

### Objectives
Test to enable SNR telemetry markers for all available Virtual access points.

### Test Case ID
TC_ONEWIFI_82

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.SNRList | Comma-separated SSID indices from 1 to Device.WiFi.SSIDNumberOfEntries |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.SNRList.</small> | <small>Verify Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.SNRList is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>GET Device.WiFi.SSIDNumberOfEntries.</small> | <small>Verify Device.WiFi.SSIDNumberOfEntries is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Generate comma-separated SNRList from SSID entries (1..SSIDNumberOfEntries) and set Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.SNRList to that generated list.</small> | <small>Verify SNRList is set successfully with all applicable SSID indices. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.SNRList and verify it matches the generated list.</small> | <small>Verify SNRList after set matches the expected generated value. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.SNRList to original value.</small> | <small>Verify Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.SNRList is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 24: Enable Tx/Rx rate telemetry markers based on AP/radio entries</strong></summary>

## Test Case 24: TS_ONEWIFI_SetWiFiTelemetryTxRxRateList

### Objectives
Enable Tx/Rx rate telemetry markers based on AP/radio entries.

### Test Case ID
TC_ONEWIFI_101

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.TxRxRateList | 1,2 for 2-radio systems; 1,2,17 for 3-radio systems |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.RadioNumberOfEntries.</small> | <small>Verify Device.WiFi.RadioNumberOfEntries is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Generate the applicable private AP list from radio count: 1,2 for 2-radio systems or 1,2,17 for 3-radio systems.</small> | <small>Verify the TxRxRateList value to be set is generated successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.TxRxRateList and store the current value.</small> | <small>Verify current TxRxRateList value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.TxRxRateList to the generated private AP list.</small> | <small>Verify TxRxRateList is set successfully with the generated list. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.TxRxRateList and verify it matches the generated private AP list.</small> | <small>Verify TxRxRateList after set matches the expected generated value. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.TxRxRateList to original value.</small> | <small>Verify Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.TxRxRateList is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 25: Verify ForceDisable reset behavior by confirming all radios return to default state after factory reset</strong></summary>

## Test Case 25: TS_ONEWIFI_ForceDisable_CheckRadioEnable_AfterFR

### Objectives
This test case is to enable WiFi Force Disable, perform a factory reset, and verify that the setting returns to its default value for all radios defined by RadioNumberOfEntries

### Test Case ID
TC_ONEWIFI_127

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable | true |
| Device.X_CISCO_COM_DeviceControl.FactoryReset | Router,Wifi,VoIP,Dect,MoCA |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable to true.</small> | <small>Verify Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>GET Device.WiFi.Radio.{i}.Enable for all radios and verify all values are false.</small> | <small>Verify all radios are disabled after enabling WiFi Force Disable. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>SET Device.X_CISCO_COM_DeviceControl.FactoryReset to Router,Wifi,VoIP,Dect,MoCA.</small> | <small>Verify Device.X_CISCO_COM_DeviceControl.FactoryReset is set to Router,Wifi,VoIP,Dect,MoCA successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>GET Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable.</small> | <small>Verify Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.WiFi.Radio.{i}.Enable for all radios and verify all values are true after factory reset.</small> | <small>Verify all radios return to enabled state after factory reset. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 26: Validate all radios defined by RadioNumberOfEntries are disabled when WiFi Force Disable is enabled in bridge mode</strong></summary>

## Test Case 26: TS_ONEWIFI_ForceDisable_CheckRadioEnable_InBridgeMode

### Objectives
This test case is to verify that all radios defined by RadioNumberOfEntries are disabled when WiFi Force Disable is enabled in bridge mode

### Test Case ID
TC_ONEWIFI_128

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode | bridge-static |
| Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable | true |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode and store the current value.</small> | <small>Verify the current LAN mode is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to bridge-static.</small> | <small>Verify LAN mode is set to bridge-static successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>GET Device.WiFi.RadioNumberOfEntries.</small> | <small>Verify Device.WiFi.RadioNumberOfEntries is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>GET and store Device.WiFi.Radio.{i}.Enable for all radios from 1 to RadioNumberOfEntries.</small> | <small>Verify initial Enable states for all radios are retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable and store the current value.</small> | <small>Verify current WiFi Force Disable state is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>SET Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable to true.</small> | <small>Verify WiFi Force Disable is enabled successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>GET Device.WiFi.Radio.{i}.Enable for all radios and verify all values are false.</small> | <small>Verify all radios are disabled in bridge mode after enabling Force Disable. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>Revert Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable to its original value.</small> | <small>Verify WiFi Force Disable is reverted successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>Restore Device.WiFi.Radio.{i}.Enable for all radios to their initial values where required.</small> | <small>Verify all radios are restored to their initial Enable states. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>GET Device.WiFi.Radio.{i}.Enable for all radios and validate values match the stored initial states.</small> | <small>Verify all radio Enable states match initial values. If the condition is met CONTINUE, else FAIL.</small> |
| <small>11</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to its original value.</small> | <small>Verify LAN mode is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 27: Validate all radios defined by RadioNumberOfEntries are disabled when WiFi Force Disable is enabled</strong></summary>

## Test Case 27: TS_ONEWIFI_ForceDisable_DisableAndCheckRadioEnable

### Objectives
This test case is to verify that all radios defined by RadioNumberOfEntries are disabled when WiFi Force Disable is enabled.

### Test Case ID
TC_ONEWIFI_125

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable | true |
| Device.WiFi.Radio.{i}.Enable | Initial runtime value per radio (stored and restored) |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.RadioNumberOfEntries.</small> | <small>Verify Device.WiFi.RadioNumberOfEntries is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>GET and store Device.WiFi.Radio.{i}.Enable for all radios from 1 to RadioNumberOfEntries.</small> | <small>Verify initial Enable states for all radios are retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>GET Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable.</small> | <small>Verify Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>SET Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable to true.</small> | <small>Verify Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.WiFi.Radio.{i}.Enable for all radios and verify all values are false.</small> | <small>Verify all radios are disabled after enabling WiFi Force Disable. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Revert Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable to original value.</small> | <small>Verify Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable is reverted successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>GET Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable and validate it matches the original value.</small> | <small>Verify Force Disable value is reverted correctly. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>SET Device.WiFi.Radio.{i}.Enable for all radios to their stored initial values.</small> | <small>Verify all radios are restored to initial Enable states successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>GET Device.WiFi.Radio.{i}.Enable for all radios and validate values match stored initial states.</small> | <small>Verify all radios returned to their initial Enable states. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 28: Verify 5GHz radio/AP/passphrase writes are blocked under ForceDisable and attempt logs are generated</strong></summary>

## Test Case 28: TS_ONEWIFI_ForceDisable_Set5GWiFiParams

### Objectives
This test case is to check if radio enable,KeyPassphrase,AccessPoint parameters for 5G are not writable when WiFi Force Disable is enabled

### Test Case ID
TC_ONEWIFI_130

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable | true |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get the current value for Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable.</small> | <small>Verify the current value for Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Enable Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable.</small> | <small>Verify enable Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Do a write operation on the following parameters "Device.WiFi.Radio.2.Enable", "Device.WiFi.AccessPoint.2.Enable", "Device.WiFi.AccessPoint.2.Security.X_COMCAST-COM_KeyPassphrase", and this write operation is expected to fail.</small> | <small>Verify write operations on these parameters fail as expected. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Check if log message WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED is present in WiFilog.txt.0 each time write operation is done.</small> | <small>Verify whether log message WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED is present in WiFilog.txt.0 each time write operation is done. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 29: Verify 6GHz radio/AP/passphrase writes are blocked under ForceDisable and attempt logs are generated</strong></summary>

## Test Case 29: TS_ONEWIFI_ForceDisable_Set6GWiFiParams

### Objectives
This test case is to verify whether 6 GHz Radio and AccessPoint parameters can be configured after ForceDisable is enabled.

### Test Case ID
TC_ONEWIFI_295

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable | true |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get the current value of Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable and save it.</small> | <small>Verify the current value of Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Set Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable to true.</small> | <small>Verify Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Now attempt to set write operations on: Device.WiFi.Radio.3.Enable, Device.WiFi.AccessPoint.17.Enable, Device.WiFi.AccessPoint.17.Security.KeyPassphrase.</small> | <small>Verify all SET operations fail as expected. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Each SET operation should fail.</small> | <small>Verify each SET operation should fail. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Check WiFiLog.txt.0 for log entry: WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED.</small> | <small>Verify log entry WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED is present in WiFiLog.txt.0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Revert ForceDisable to initial value.</small> | <small>Verify the parameter is reverted successfully. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 30: Verify SSID writes for VAP1-VAP6 are blocked under ForceDisable and original ForceDisable state is restored</strong></summary>

## Test Case 30: TS_ONEWIFI_ForceDisable_SetWiFiSSIDParams

### Objectives
This test case is to verify that SSIDs for VAP 1 through VAP 6 are not writable when WiFi Force Disable is enabled.

### Test Case ID
TC_ONEWIFI_131

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable | true |
| Device.WiFi.SSID.{1..6}.SSID | tdkbtestcase |

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable.</small> | <small>Verify Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>SET Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable to true.</small> | <small>Verify Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable is set to true successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Attempt SET operations on Device.WiFi.SSID.1.SSID through Device.WiFi.SSID.6.SSID with value tdkbtestcase while Force Disable is enabled.</small> | <small>Verify all SSID SET operations fail as expected when Force Disable is enabled. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Revert Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable to original value.</small> | <small>Verify Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable is reverted successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>GET Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable and validate it matches the original value.</small> | <small>Verify WiFi Force Disable state is restored to the original value. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 31: Verify each MLD-capable AP MLD_Addr matches the MLD interface MAC address</strong></summary>

## Test Case 31: TS_ONEWIFI_WIFI7_CheckMLDAddrAlignment

### Objectives
To verify that the MLD_Addr reported in TR-181 for every MLD-capable AccessPoint matches the hardware address of the MLD interface.

### Test Case ID
TS_ONEWIFI_WIFI7_009

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get the hardware address of MLD Interface.</small> | <small>Verify the hardware address of MLD Interface is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get RadioNumberOfEntries.</small> | <small>Verify RadioNumberOfEntries is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get MLD AP index list.</small> | <small>Verify MLD AP index list is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Get MLD Address and compare with MLD Interface hardware address.</small> | <small>Verify MLD Address matches MLD Interface hardware address. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 32: Verify the MLD interface is bridged to brlan0 and remains in UP state</strong></summary>

## Test Case 32: TS_ONEWIFI_WIFI7_CheckMLDBridgeStatus

### Objectives
To check if the MLD interface is added to the brlan0 bridge and its state is UP

### Test Case ID
TS_ONEWIFI_WIFI7_002

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get MLD Interface bridge and state info.</small> | <small>Verify MLD Interface bridge and state info is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Check if MLD Interface is added to brlan0 bridge.</small> | <small>Verify whether MLD Interface is added to brlan0 bridge. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Check if MLD Interface state is UP.</small> | <small>Verify whether MLD Interface state is UP. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 33: Verify MLD_Enable is true for all MLD-capable APs based on platform radio count</strong></summary>

## Test Case 33: TS_ONEWIFI_WIFI7_CheckMLDEnable

### Objectives
To verify that MLD_Enable is set to true for all MLD-capable AccessPoints based on the number of radios supported by the platform.

### Test Case ID
TS_ONEWIFI_WIFI7_008

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get number of radios from Device.WiFi.RadioNumberOfEntries.</small> | <small>Verify number of radios is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get MLD AP indices.</small> | <small>Verify MLD AP indices is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Step per AP index: Get MLD_Enable and check it is true.</small> | <small>Verify MLD_Enable is true for all MLD-capable APs. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 34: Verify the MLD interface reports UP and LOWER_UP operational flags</strong></summary>

## Test Case 34: TS_ONEWIFI_WIFI7_CheckMLDInterfaceUp

### Objectives
To check if MLD interface is UP and LOWER_UP indicating an operational Wi-Fi 7 connection.

### Test Case ID
TS_ONEWIFI_WIFI7_001

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get MLD interface status.</small> | <small>Verify MLD interface status is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Check if UP,LOWER_UP flags are present to confirm operational status.</small> | <small>Verify whether UP,LOWER_UP flags are present to confirm operational status. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 35: Verify each MLD link MAC matches its corresponding radio interface MAC</strong></summary>

## Test Case 35: TS_ONEWIFI_WIFI7_CheckMLDLinkMACs

### Objectives
To verify that each MLD link's MAC address from MLD interface info matches the Hardware address of its corresponding radio interface

### Test Case ID
TS_ONEWIFI_WIFI7_006

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get number of radios.</small> | <small>Verify number of radios is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get radio interface prefix.</small> | <small>Verify radio interface prefix is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get link addr from MLD Interface info for this link ID.</small> | <small>Verify link addr from MLD Interface info for this link ID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Get HWaddr of radio interface.</small> | <small>Verify HWaddr of radio interface is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Compare link addr with radio interface HWaddr.</small> | <small>Verify link addr matches radio interface HWaddr. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 36: Verify all expected MLD link IDs are present for the platform radio count</strong></summary>

## Test Case 36: TS_ONEWIFI_WIFI7_CheckMLDLinks

### Objectives
To verify that all expected MLD link IDs are present in MLD interface info based on the number of radios supported by the platform

### Test Case ID
TS_ONEWIFI_WIFI7_004

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get number of radios.</small> | <small>Verify number of radios is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Check each link ID is present in MLD Interface info.</small> | <small>Verify each link ID is present in MLD Interface info. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 37: Verify MLD interface hardware MAC matches the wireless MLD MAC report</strong></summary>

## Test Case 37: TS_ONEWIFI_WIFI7_CheckMLDMACAddress

### Objectives
To verify that the MLD interface hardware address matches the address reported by MLD interface info confirming MAC address consistency

### Test Case ID
TS_ONEWIFI_WIFI7_003

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get MLD Interface hardware address.</small> | <small>Verify MLD Interface hardware address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get MLD addr from wireless interface info.</small> | <small>Verify MLD addr from wireless interface info is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Validate both MACs match (case-insensitive).</small> | <small>Verify that both MACs match (case-insensitive). If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 38: Verify each MLD link channel matches its corresponding TR-181 radio channel</strong></summary>

## Test Case 38: TS_ONEWIFI_WIFI7_CheckMLDRadioChannelConfig

### Objectives
This test case is to verify that the channel shown for each MLD link in wireless info matches the channel configured for its corresponding radio in the TR-181 data model.

### Test Case ID
TS_ONEWIFI_WIFI7_007

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get number of radios.</small> | <small>Verify number of radios is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get channel for this radio.</small> | <small>Verify channel for this radio is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get channel for this link from MLD Interface info.</small> | <small>Verify channel for this link from MLD Interface info is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Compare TR-181 channel with MLD Interface info channel.</small> | <small>Verify TR-181 channel matches MLD Interface info channel. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 39: Verify MLD interface SSID matches Device.WiFi.SSID.1.SSID</strong></summary>

## Test Case 39: TS_ONEWIFI_WIFI7_CheckMLDSSID

### Objectives
To Verify SSID from MLD Interface matches Device.WiFi.SSID.1.SSID

### Test Case ID
TS_ONEWIFI_WIFI7_005

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Get SSID from MLD Interface wireless info.</small> | <small>Verify SSID from MLD Interface wireless info is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get configured SSID from Device.WiFi.SSID.1.SSID.</small> | <small>Verify configured SSID from Device.WiFi.SSID.1.SSID is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Validate SSID from MLD Interface matches Device.WiFi.SSID.1.SSID.</small> | <small>Verify that SSID from MLD Interface matches Device.WiFi.SSID.1.SSID. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 40: Verify a connected Wi-Fi client appears in the Host table with Active true</strong></summary>

## Test Case 40: TS_ONEWIFI_WIFI7_CheckWiFiClientHostTableUpdate

### Objectives
To verify that a connected MLD/non-MLD Wi-Fi client appears in the Host table with Active status true

### Test Case ID
TS_ONEWIFI_WIFI7_010

### Test Type
Positive

### Test Environment
| Component |
|-----------|
| DUT - Device under test |
| WLAN Client - Wireless client |

### Test Configuration
None

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>&nbsp;</small> | <small>Connect a WLAN client to the target SSID.</small> | <small>Verify the WLAN client is connected before continuing. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get the number of Host entries.</small> | <small>&nbsp;</small> | <small>Verify the number of Host entries is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Iterate through the Host Table and find any WiFi client entry.</small> | <small>&nbsp;</small> | <small>Verify a WiFi client entry is found in the Host Table. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Get the value of Device.Hosts.Host.{i}.Active and verify the value as true.</small> | <small>&nbsp;</small> | <small>Verify Device.Hosts.Host.{i}.Active is true. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 41: LAN client Telnet to WLAN client through gateway</strong></summary>

## Test Case 41: E2E_WIFI_Telnet_FromLanToWlan

## Objectives
Verify that a LAN client can successfully establish a Telnet connection to a WLAN client through the wireless gateway.

## Test Case ID
TC_TDKB_E2E_793

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify SSID and keypassphrase are retrieved and match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>&nbsp;</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>&nbsp;</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get IP address assigned to LAN client interface</small> | <small>Verify LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify LAN client IP address is within the gateway DHCP range</small> | <small>Verify LAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Establish Telnet connection from LAN client to WLAN client IP address</small> | <small>Verify Telnet connection from LAN client to WLAN client is successful. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 42: WLAN client ping to LAN client through gateway</strong></summary>

## Test Case 42: E2E_WIFI_Ping_FromWlanToLan

## Objectives
Verify that a WLAN client can successfully ping a LAN client through a gateway.

## Test Case ID
TC_TDKB_E2E_794

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify SSID and keypassphrase are retrieved and match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>&nbsp;</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>&nbsp;</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get IP address assigned to LAN client interface</small> | <small>Verify LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify LAN client IP address is within the gateway DHCP range</small> | <small>Verify LAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Ping from WLAN client to LAN client IP address</small> | <small>&nbsp;</small> | <small>Verify ping from WLAN client to LAN client is successful. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 43: LAN client ping to WLAN client through gateway</strong></summary>

## Test Case 43: E2E_WIFI_Ping_FromLanToWlan

## Objectives
Verify that a LAN client can successfully ping a WLAN client through a gateway.

## Test Case ID
TC_TDKB_E2E_795

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify SSID and keypassphrase are retrieved and match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>&nbsp;</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>&nbsp;</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get IP address assigned to LAN client interface</small> | <small>Verify LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify LAN client IP address is within the gateway DHCP range</small> | <small>Verify LAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Ping from LAN client to WLAN client IP address</small> | <small>Verify ping from LAN client to WLAN client is successful. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 44: WLAN client ping to gateway's public WAN IP</strong></summary>

## Test Case 44: E2E_WIFI_PingRouterPublicIP

## Objectives
Verify that a WLAN client connected to the wireless gateway can successfully ping the gateway's public WAN IP address.

## Test Case ID
TC_TDKB_E2E_796

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase</small> | <small>&nbsp;</small> | <small>Verify SSID and keypassphrase are retrieved and match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Ping from WLAN client to the gateway's public WAN IP address</small> | <small>Verify ping from WLAN client to the gateway's public WAN IP is successful. If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 45: WLAN client HTTP to LAN server through gateway</strong></summary>

## Test Case 45: E2E_WIFI_Http_FromWlanToLan

## Objectives
Verify that a WLAN client can successfully reach a LAN host via HTTP through the wireless gateway.

## Test Case ID
TC_TDKB_E2E_797

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify SSID and keypassphrase are retrieved and match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>&nbsp;</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>&nbsp;</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get IP address assigned to LAN client interface</small> | <small>Verify LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify LAN client IP address is within the gateway DHCP range</small> | <small>Verify LAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Perform HTTP request from WLAN client to LAN server IP address</small> | <small>&nbsp;</small> | <small>Verify HTTP request from WLAN client to LAN server is successful. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 46: WLAN client HTTPS to LAN server through gateway</strong></summary>

## Test Case 46: E2E_WIFI_Https_FromWlanToLan

## Objectives
Verify that a WLAN client can successfully reach a LAN host via HTTPS through the wireless gateway.

## Test Case ID
TC_TDKB_E2E_798

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify SSID and keypassphrase are retrieved and match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>&nbsp;</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>&nbsp;</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get IP address assigned to LAN client interface</small> | <small>Verify LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify LAN client IP address is within the gateway DHCP range</small> | <small>Verify LAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Perform HTTPS request from WLAN client to LAN server IP address</small> | <small>&nbsp;</small> | <small>Verify HTTPS request from WLAN client to LAN server is successful. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 47: WLAN client FTP download from LAN server through gateway</strong></summary>

## Test Case 47: E2E_WIFI_FTP_FromWlanToLan

## Objectives
Verify that a WLAN client can successfully download a file from a LAN FTP server through the wireless gateway.

## Test Case ID
TC_TDKB_E2E_799

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify SSID and keypassphrase are retrieved and match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>&nbsp;</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>&nbsp;</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get IP address assigned to LAN client interface</small> | <small>Verify LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify LAN client IP address is within the gateway DHCP range</small> | <small>Verify LAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Perform FTP file download from WLAN client to LAN FTP server IP address</small> | <small>&nbsp;</small> | <small>Verify FTP file download from WLAN client to LAN server is successful. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 48: LAN client FTP download from WLAN server through gateway</strong></summary>

## Test Case 48: E2E_WIFI_FTP_FromLanToWLan

## Objectives
Verify that a WLAN client acting as an FTP server can successfully serve a file download to a LAN client.

## Test Case ID
TC_TDKB_E2E_800

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify SSID and keypassphrase are retrieved and match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>&nbsp;</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>&nbsp;</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get IP address assigned to LAN client interface</small> | <small>Verify LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify LAN client IP address is within the gateway DHCP range</small> | <small>Verify LAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Perform FTP file download from LAN client to WLAN FTP server IP address</small> | <small>Verify FTP file download from LAN client to WLAN server is successful. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 49: UDP WLAN to LAN with firewall Medium</strong></summary>

## Test Case 49: E2E_WIFI_FirewallMedium_UDPFromWlanToLan

## Objectives
Verify that UDP traffic from a WLAN client to a LAN client is allowed when the gateway firewall is set to Medium level.

## Test Case ID
TC_TDKB_E2E_801

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, and Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_Security.Firewall.FirewallLevel to "Medium"</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify firewall level is set to Medium successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Wait 60 seconds for firewall configuration to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>&nbsp;</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>&nbsp;</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get IP address assigned to LAN client interface</small> | <small>Verify LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify LAN client IP address is within the gateway DHCP range</small> | <small>Verify LAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Send UDP traffic from WLAN client to LAN client IP address</small> | <small>&nbsp;</small> | <small>Verify UDP traffic is received at LAN client with 0% packet loss. If the condition is met PASS, else FAIL</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>12</small> | <small>Revert Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 50: UDP WLAN to LAN with firewall Low</strong></summary>

## Test Case 50: E2E_WIFI_FirewallLow_UDPFromWlanToLan

## Objectives
Verify that UDP traffic from a WLAN client to a LAN client is allowed when the gateway firewall is set to Low level.

## Test Case ID
TC_TDKB_E2E_802

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, and Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_Security.Firewall.FirewallLevel to "Low"</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify firewall level is set to Low successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Wait 60 seconds for firewall configuration to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>&nbsp;</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>&nbsp;</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get IP address assigned to LAN client interface</small> | <small>Verify LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify LAN client IP address is within the gateway DHCP range</small> | <small>Verify LAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Send UDP traffic from WLAN client to LAN client IP address</small> | <small>&nbsp;</small> | <small>Verify UDP traffic is received at LAN client with 0% packet loss. If the condition is met PASS, else FAIL</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>12</small> | <small>Revert Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 51: TCP WLAN to LAN with firewall Low</strong></summary>

## Test Case 51: E2E_WIFI_FirewallLow_TCPFromWlanToLan

## Objectives
Verify that TCP traffic from a WLAN client to a LAN client is allowed when the gateway firewall is set to Low level.

## Test Case ID
TC_TDKB_E2E_803

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, and Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_Security.Firewall.FirewallLevel to "Low"</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify firewall level is set to Low successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Wait 60 seconds for firewall configuration to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>&nbsp;</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>&nbsp;</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get IP address assigned to LAN client interface</small> | <small>Verify LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify LAN client IP address is within the gateway DHCP range</small> | <small>Verify LAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Send TCP traffic from WLAN client to LAN client IP address</small> | <small>&nbsp;</small> | <small>Verify TCP bandwidth is received at LAN client successfully. If the condition is met PASS, else FAIL</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>12</small> | <small>Revert Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 52: UDP WLAN to LAN with firewall High</strong></summary>

## Test Case 52: E2E_WIFI_FirewallHigh_UDPFromWlanToLan

## Objectives
Verify that UDP traffic from a WLAN client to a LAN client is allowed when the gateway firewall is set to High level.

## Test Case ID
TC_TDKB_E2E_804

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, and Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_Security.Firewall.FirewallLevel to "High"</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify firewall level is set to High successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Wait 60 seconds for firewall configuration to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>&nbsp;</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>&nbsp;</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get IP address assigned to LAN client interface</small> | <small>Verify LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify LAN client IP address is within the gateway DHCP range</small> | <small>Verify LAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Send UDP traffic from WLAN client to LAN client IP address</small> | <small>&nbsp;</small> | <small>Verify UDP traffic is received at LAN client with 0% packet loss. If the condition is met PASS, else FAIL</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>12</small> | <small>Revert Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 53: TCP WLAN to LAN with firewall High</strong></summary>

## Test Case 53: E2E_WIFI_FirewallHigh_TCPFromWlanToLan

## Objectives
Verify that TCP traffic from a WLAN client to a LAN client is allowed when the gateway firewall is set to High level.

## Test Case ID
TC_TDKB_E2E_805

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, and Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_Security.Firewall.FirewallLevel to "High"</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify firewall level is set to High successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Wait 60 seconds for firewall configuration to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>&nbsp;</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>&nbsp;</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get IP address assigned to LAN client interface</small> | <small>Verify LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify LAN client IP address is within the gateway DHCP range</small> | <small>Verify LAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Send TCP traffic from WLAN client to LAN client IP address</small> | <small>&nbsp;</small> | <small>Verify TCP bandwidth is received at LAN client successfully. If the condition is met PASS, else FAIL</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>12</small> | <small>Revert Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 54: UDP WLAN to LAN with firewall Custom</strong></summary>

## Test Case 54: E2E_WIFI_FirewallCustom_UDPFromWlanToLan

## Objectives
Verify that UDP traffic from a WLAN client to a LAN client is allowed when the gateway firewall is set to Custom level.

## Test Case ID
TC_TDKB_E2E_806

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Custom |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, and Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_Security.Firewall.FirewallLevel to "Custom"</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify firewall level is set to Custom successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Wait 60 seconds for firewall configuration to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>&nbsp;</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>&nbsp;</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get IP address assigned to LAN client interface</small> | <small>Verify LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify LAN client IP address is within the gateway DHCP range</small> | <small>Verify LAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Send UDP traffic from WLAN client to LAN client IP address</small> | <small>&nbsp;</small> | <small>Verify UDP traffic is received at LAN client with 0% packet loss. If the condition is met PASS, else FAIL</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>12</small> | <small>Revert Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 55: TCP WLAN to LAN with firewall Custom</strong></summary>

## Test Case 55: E2E_WIFI_FirewallCustom_TCPFromWlanToLan

## Objectives
Verify that TCP traffic from a WLAN client to a LAN client is allowed when the gateway firewall is set to Custom level.

## Test Case ID
TC_TDKB_E2E_807

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Custom |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, and Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_Security.Firewall.FirewallLevel to "Custom"</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify firewall level is set to Custom successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Wait 60 seconds for firewall configuration to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>&nbsp;</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get IP address assigned to WLAN client interface after connecting to WiFi</small> | <small>&nbsp;</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP address is within the gateway DHCP range</small> | <small>&nbsp;</small> | <small>Verify WLAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get IP address assigned to LAN client interface</small> | <small>Verify LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify LAN client IP address is within the gateway DHCP range</small> | <small>Verify LAN client IP is within DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Send TCP traffic from WLAN client to LAN client IP address</small> | <small>&nbsp;</small> | <small>Verify TCP bandwidth is received at LAN client successfully. If the condition is met PASS, else FAIL</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from WiFi SSID</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>12</small> | <small>Revert Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 56: WLAN client connection rejected with invalid passphrase</strong></summary>

## Test Case 56: E2E_WIFI_ConnectWithInvalidKey

## Objectives
Verify that a WLAN client cannot connect to the gateway's WiFi SSID using an invalid passphrase.

## Test Case ID
TC_TDKB_E2E_808

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase</small> | <small>&nbsp;</small> | <small>Verify SSID and keypassphrase are retrieved and match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Attempt to connect to WiFi SSID using an invalid passphrase</small> | <small>Verify WLAN client fails to connect to the WiFi SSID when an invalid passphrase is used. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 57: Verify MAC filter defaults after factory reset</strong></summary>

## Test Case 57: E2E_WIFI_ACL_VerifyMacFilterDefaultValues_FactoryReset

## Objectives
Verify that after a factory reset, the DUT has MAC filter enabled set to false, MAC filter blacklist set to false, and filtering mode set to Allow-All as the default values for all radios, and also verify that a WLAN client can connect successfully.

## Test Case ID
TC_TDKB_E2E_771

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.FactoryReset | Router,Wifi,VoIP,Dect,MoCA |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.X_CISCO_COM_DeviceControl.FactoryReset to "Router,Wifi,VoIP,Dect,MoCA" to trigger factory reset</small> | <small>&nbsp;</small> | <small>Verify factory reset is initiated on the DUT successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Wait for DUT to resume connectivity after factory reset (approximately 5 minutes)</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>3</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason</small> | <small>&nbsp;</small> | <small>Verify last reboot reason is "factory-reset". If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.WiFi.RadioNumberOfEntries</small> | <small>&nbsp;</small> | <small>Verify the number of radio entries is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.Enable for each radio index</small> | <small>&nbsp;</small> | <small>Verify Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.Enable is "false" as the default value for all radios. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.FilterAsBlackList for each radio index</small> | <small>&nbsp;</small> | <small>Verify Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.FilterAsBlackList is "false" as the default value for all radios. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_MAC_FilteringMode for each radio index</small> | <small>&nbsp;</small> | <small>Verify Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_MAC_FilteringMode is "Allow-ALL" as the default value for all radios. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase (2.4GHz index)</small> | <small>&nbsp;</small> | <small>Verify SSID and keypassphrase are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>SET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase (2.4GHz index) to configured values</small> | <small>&nbsp;</small> | <small>Verify SSID and keypassphrase are set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>Wait 60 seconds for WiFi configuration changes to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Connect to WiFi SSID using the configured credentials</small> | <small>Verify WLAN client connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>12</small> | <small>&nbsp;</small> | <small>Disconnect from WiFi SSID</small> | <small>Verify WLAN client disconnected successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 58: MAC filter allows 2.4GHz connection only</strong></summary>

## Test Case 58: E2E_WIFI_ACL_MacFilterAllowOnly2.4GHZ

## Objectives
Verify that the gateway allows access only for a Wi-Fi client whose MAC address is configured in the MAC filter table for the 2.4GHz SSID.

## Test Case ID
TC_TDKB_E2E_772

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.Enable (all radios) | true |
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.FilterAsBlackList (all radios) | false |
| Device.WiFi.AccessPoint.1.X_CISCO_COM_MacFilterTable.{i}.MACAddress | WLAN client MAC address |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.Enable to true and Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.FilterAsBlackList to false for all radio indices</small> | <small>&nbsp;</small> | <small>Verify MAC filter prerequisites are set for all radios. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Get MAC address of WLAN client interface</small> | <small>Verify WLAN client MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>ADD row to Device.WiFi.AccessPoint.1.X_CISCO_COM_MacFilterTable and SET MACAddress to WLAN client MAC</small> | <small>&nbsp;</small> | <small>Verify WLAN client MAC address is set in the 2.4GHz filter table. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.WiFi.SSID.1.BSSID and configure 2.4GHz SSID/passphrase</small> | <small>&nbsp;</small> | <small>Verify 2.4GHz BSSID, SSID and passphrase are set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Wait 60 seconds for configuration to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Connect to 2.4GHz WiFi SSID using the 2.4GHz BSSID</small> | <small>Verify WLAN client connected to the 2.4GHz SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.WiFi.Radio.1.PossibleChannels</small> | <small>&nbsp;</small> | <small>Verify 2.4GHz possible channel list is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Verify the connected channel belongs to the 2.4GHz possible channels</small> | <small>Verify WLAN client is confirmed connected on the 2.4GHz band. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Disconnect from 2.4GHz WiFi SSID</small> | <small>&nbsp;</small> |
| <small>10</small> | <small>Revert SSID/passphrase, delete MAC filter table entry, and revert MAC filter settings for all radios</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 59: MAC filter allows 5GHz connection only</strong></summary>

## Test Case 59: E2E_WIFI_ACL_MacFilterAllowOnly5GHZ

## Objectives
Verify that the gateway allows access only for a Wi-Fi client whose MAC address is configured in the MAC filter table for the 5GHz SSID.

## Test Case ID
TC_TDKB_E2E_773

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.Enable (all radios) | true |
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.FilterAsBlackList (all radios) | false |
| Device.WiFi.AccessPoint.2.X_CISCO_COM_MacFilterTable.{i}.MACAddress | WLAN client MAC address |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.Enable to true and Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.FilterAsBlackList to false for all radio indices</small> | <small>&nbsp;</small> | <small>Verify MAC filter prerequisites are set for all radios. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Get MAC address of WLAN client interface</small> | <small>Verify WLAN client MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>ADD row to Device.WiFi.AccessPoint.2.X_CISCO_COM_MacFilterTable and SET MACAddress to WLAN client MAC</small> | <small>&nbsp;</small> | <small>Verify WLAN client MAC address is set in the 5GHz filter table. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.WiFi.SSID.2.BSSID and configure 5GHz SSID/passphrase</small> | <small>&nbsp;</small> | <small>Verify 5GHz BSSID, SSID and passphrase are set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Wait 60 seconds for configuration to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Connect to 5GHz WiFi SSID using the 5GHz BSSID</small> | <small>Verify WLAN client connected to the 5GHz SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.WiFi.Radio.2.PossibleChannels</small> | <small>&nbsp;</small> | <small>Verify 5GHz possible channel list is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Verify the connected channel belongs to the 5GHz possible channels</small> | <small>Verify WLAN client is confirmed connected on the 5GHz band. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Disconnect from 5GHz WiFi SSID</small> | <small>&nbsp;</small> |
| <small>10</small> | <small>Revert SSID/passphrase, delete MAC filter table entry, and revert MAC filter settings for all radios</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 60: MAC filter blocks 2.4GHz client in deny mode</strong></summary>

## Test Case 60: E2E_WIFI_ACL_MacFilterBlock2.4GHZ

## Objectives
Verify that the gateway blocks access for a specific Wi-Fi client whose MAC address is in the Deny (blacklist) MAC filter table for the 2.4GHz SSID.

## Test Case ID
TC_TDKB_E2E_774

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.Enable (all radios) | true |
| Device.WiFi.AccessPoint.1.X_CISCO_COM_MACFilter.FilterAsBlackList | true |
| Device.WiFi.AccessPoint.1.X_CISCO_COM_MacFilterTable.{i}.MACAddress | WLAN client MAC address |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>SET MAC filter enable to true and FilterAsBlackList to false for all radios; then SET FilterAsBlackList to true for 2.4GHz</small> | <small>&nbsp;</small> | <small>Verify 2.4GHz filter mode is set to Deny successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Get MAC address of WLAN client interface</small> | <small>Verify WLAN client MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>ADD row to Device.WiFi.AccessPoint.1.X_CISCO_COM_MacFilterTable and SET MACAddress to WLAN client MAC</small> | <small>&nbsp;</small> | <small>Verify WLAN client MAC address is set in the 2.4GHz deny list. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.WiFi.SSID.1.BSSID and configure 2.4GHz SSID/passphrase; wait 60 seconds</small> | <small>&nbsp;</small> | <small>Verify configuration is applied. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Attempt to connect to 2.4GHz WiFi SSID using the 2.4GHz BSSID</small> | <small>Verify WLAN client fails to connect to the 2.4GHz SSID as the MAC is in the deny list. If the condition is met PASS, else FAIL</small> |
| <small>6</small> | <small>Revert SSID/passphrase, delete MAC filter table entry, and revert MAC filter settings</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 61: MAC filter blocks 5GHz client in deny mode</strong></summary>

## Test Case 61: E2E_WIFI_ACL_MacFilterBlock5GHZ

## Objectives
Verify that the gateway blocks access for a specific Wi-Fi client whose MAC address is in the Deny (blacklist) MAC filter table for the 5GHz SSID.

## Test Case ID
TC_TDKB_E2E_775

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.Enable (all radios) | true |
| Device.WiFi.AccessPoint.2.X_CISCO_COM_MACFilter.FilterAsBlackList | true |
| Device.WiFi.AccessPoint.2.X_CISCO_COM_MacFilterTable.{i}.MACAddress | WLAN client MAC address |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>SET MAC filter enable to true and FilterAsBlackList to false for all radios; then SET FilterAsBlackList to true for 5GHz</small> | <small>&nbsp;</small> | <small>Verify 5GHz filter mode is set to Deny successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Get MAC address of WLAN client interface</small> | <small>Verify WLAN client MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>ADD row to Device.WiFi.AccessPoint.2.X_CISCO_COM_MacFilterTable and SET MACAddress to WLAN client MAC</small> | <small>&nbsp;</small> | <small>Verify WLAN client MAC address is set in the 5GHz deny list. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.WiFi.SSID.2.BSSID and configure 5GHz SSID/passphrase; wait 60 seconds</small> | <small>&nbsp;</small> | <small>Verify configuration is applied. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Attempt to connect to 5GHz WiFi SSID using the 5GHz BSSID</small> | <small>Verify WLAN client fails to connect to the 5GHz SSID as the MAC is in the deny list. If the condition is met PASS, else FAIL</small> |
| <small>6</small> | <small>Revert SSID/passphrase, delete MAC filter table entry, and revert MAC filter settings</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 62: MAC filter allows 2.4GHz and blocks 5GHz</strong></summary>

## Test Case 62: E2E_WIFI_ACL_MacFilterAllow2.4GHZ_Block5GHZ

## Objectives
Verify that MAC address-based access control allows a Wi-Fi client to connect via 2.4GHz SSID while denying access via 5GHz SSID.

## Test Case ID
TC_TDKB_E2E_776

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.Enable (all radios) | true |
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.FilterAsBlackList (all radios) | false |
| Device.WiFi.AccessPoint.2.X_CISCO_COM_MACFilter.FilterAsBlackList | true |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>SET MAC filter enable to true and FilterAsBlackList to false for all radios; SET FilterAsBlackList to true for 5GHz</small> | <small>&nbsp;</small> | <small>Verify MAC filter and deny mode are configured. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Get MAC address of WLAN client interface</small> | <small>Verify WLAN client MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>ADD WLAN client MAC to 2.4GHz allow table and 5GHz deny table</small> | <small>&nbsp;</small> | <small>Verify MAC entries are configured for both bands. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Configure SSID/passphrase for both bands; wait 60 seconds</small> | <small>&nbsp;</small> | <small>Verify configuration is applied. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Connect to 2.4GHz WiFi SSID using the 2.4GHz BSSID and verify connected channel is 2.4GHz</small> | <small>Verify WLAN client connected on 2.4GHz band. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Disconnect from 2.4GHz; attempt to connect to 5GHz SSID using 5GHz BSSID</small> | <small>Verify WLAN client fails to connect to the 5GHz SSID. If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>Revert SSID/passphrase, delete MAC filter table entries, and revert MAC filter settings for all radios</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 63: MAC filter allows 5GHz and blocks 2.4GHz</strong></summary>

## Test Case 63: E2E_WIFI_ACL_MacFilterAllow5GHZ_Block2.4GHZ

## Objectives
Verify that MAC address-based access control allows a Wi-Fi client to connect via 5GHz SSID while denying access via 2.4GHz SSID.

## Test Case ID
TC_TDKB_E2E_777

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.Enable (all radios) | true |
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.FilterAsBlackList (all radios) | false |
| Device.WiFi.AccessPoint.1.X_CISCO_COM_MACFilter.FilterAsBlackList | true |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>SET MAC filter enable to true and FilterAsBlackList to false for all radios; SET FilterAsBlackList to true for 2.4GHz</small> | <small>&nbsp;</small> | <small>Verify MAC filter and deny mode are configured. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Get MAC address of WLAN client interface</small> | <small>Verify WLAN client MAC address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>ADD WLAN client MAC to 5GHz allow table and 2.4GHz deny table</small> | <small>&nbsp;</small> | <small>Verify MAC entries are configured for both bands. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Configure SSID/passphrase for both bands; wait 60 seconds</small> | <small>&nbsp;</small> | <small>Verify configuration is applied. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Connect to 5GHz WiFi SSID using the 5GHz BSSID and verify connected channel is 5GHz</small> | <small>Verify WLAN client connected on 5GHz band. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Disconnect from 5GHz; attempt to connect to 2.4GHz SSID using 2.4GHz BSSID</small> | <small>Verify WLAN client fails to connect to the 2.4GHz SSID. If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>Revert SSID/passphrase, delete MAC filter table entries, and revert MAC filter settings for all radios</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 64: Allow mode 2.4GHz blocks unlisted client</strong></summary>

## Test Case 64: E2E_WIFI_ACL_MacFilteringModeAllow2.4GHZ_WithInvalidMACFilterEntry

## Objectives
Verify that a WLAN client whose MAC address is not in the MAC filter allow list cannot access the 2.4GHz wireless gateway when filtering mode is set to Allow.

## Test Case ID
TC_TDKB_E2E_778

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.Enable (all radios) | true |
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.FilterAsBlackList (all radios) | false |
| Device.WiFi.AccessPoint.1.X_CISCO_COM_MacFilterTable.{i}.MACAddress | Invalid MAC address (not the WLAN client MAC) |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>SET MAC filter enable to true and FilterAsBlackList to false for all radios</small> | <small>&nbsp;</small> | <small>Verify MAC filter prerequisites are set. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>ADD row to Device.WiFi.AccessPoint.1.X_CISCO_COM_MacFilterTable and SET MACAddress to an invalid MAC (aa:bb:cc:dd:ee:ff)</small> | <small>&nbsp;</small> | <small>Verify invalid MAC is set in the 2.4GHz allow filter table. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.WiFi.SSID.1.BSSID and configure 2.4GHz SSID/passphrase; wait 60 seconds</small> | <small>&nbsp;</small> | <small>Verify configuration is applied. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Attempt to connect to 2.4GHz WiFi SSID using the 2.4GHz BSSID</small> | <small>Verify WLAN client fails to connect as its MAC is not in the allow list. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>Revert SSID/passphrase, delete MAC filter table entry, and revert MAC filter settings</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 65: Allow mode 5GHz blocks unlisted client</strong></summary>

## Test Case 65: E2E_WIFI_ACL_MacFilteringModeAllow5GHZ_WithInvalidMACFilterEntry

## Objectives
Verify that a WLAN client whose MAC address is not in the MAC filter allow list cannot access the 5GHz wireless gateway when filtering mode is set to Allow.

## Test Case ID
TC_TDKB_E2E_779

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.Enable (all radios) | true |
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.FilterAsBlackList (all radios) | false |
| Device.WiFi.AccessPoint.2.X_CISCO_COM_MacFilterTable.{i}.MACAddress | Invalid MAC address (not the WLAN client MAC) |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>SET MAC filter enable to true and FilterAsBlackList to false for all radios</small> | <small>&nbsp;</small> | <small>Verify MAC filter prerequisites are set. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>ADD row to Device.WiFi.AccessPoint.2.X_CISCO_COM_MacFilterTable and SET MACAddress to an invalid MAC (aa:bb:cc:dd:ee:ff)</small> | <small>&nbsp;</small> | <small>Verify invalid MAC is set in the 5GHz allow filter table. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.WiFi.SSID.2.BSSID and configure 5GHz SSID/passphrase; wait 60 seconds</small> | <small>&nbsp;</small> | <small>Verify configuration is applied. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Attempt to connect to 5GHz WiFi SSID using the 5GHz BSSID</small> | <small>Verify WLAN client fails to connect as its MAC is not in the allow list. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>Revert SSID/passphrase, delete MAC filter table entry, and revert MAC filter settings</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 66: Deny mode 2.4GHz allows unlisted client</strong></summary>

## Test Case 66: E2E_WIFI_ACL_MacFilteringModeDeny2.4GHZ_WithInvalidMACFilterEntry

## Objectives
Verify that a WLAN client whose MAC address is not in the MAC filter deny list can access the 2.4GHz wireless gateway when filtering mode is set to Deny.

## Test Case ID
TC_TDKB_E2E_780

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.Enable (all radios) | true |
| Device.WiFi.AccessPoint.1.X_CISCO_COM_MACFilter.FilterAsBlackList | true |
| Device.WiFi.AccessPoint.1.X_CISCO_COM_MacFilterTable.{i}.MACAddress | Invalid MAC address (not the WLAN client MAC) |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>SET MAC filter enable to true and FilterAsBlackList to false for all radios; SET FilterAsBlackList to true for 2.4GHz</small> | <small>&nbsp;</small> | <small>Verify 2.4GHz deny mode is configured. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>ADD row to Device.WiFi.AccessPoint.1.X_CISCO_COM_MacFilterTable and SET MACAddress to an invalid MAC (aa:bb:cc:dd:ee:ff)</small> | <small>&nbsp;</small> | <small>Verify invalid MAC is set in the 2.4GHz deny filter table. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.WiFi.SSID.1.BSSID and configure 2.4GHz SSID/passphrase; wait 60 seconds</small> | <small>&nbsp;</small> | <small>Verify configuration is applied. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Connect to 2.4GHz WiFi SSID using the 2.4GHz BSSID</small> | <small>Verify WLAN client connects successfully as its MAC is not in the deny list. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.WiFi.Radio.1.PossibleChannels</small> | <small>&nbsp;</small> | <small>Verify 2.4GHz possible channel list is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify the connected channel belongs to the 2.4GHz possible channels; disconnect</small> | <small>Verify WLAN client is confirmed connected on the 2.4GHz band. If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>Revert SSID/passphrase, delete MAC filter table entry, and revert MAC filter settings</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 67: Deny mode 5GHz allows unlisted client</strong></summary>

## Test Case 67: E2E_WIFI_ACL_MacFilteringModeDeny5GHZ_WithInvalidMACFilterEntry

## Objectives
Verify that a WLAN client whose MAC address is not in the MAC filter deny list can access the 5GHz wireless gateway when filtering mode is set to Deny.

## Test Case ID
TC_TDKB_E2E_781

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.AccessPoint.{i}.X_CISCO_COM_MACFilter.Enable (all radios) | true |
| Device.WiFi.AccessPoint.2.X_CISCO_COM_MACFilter.FilterAsBlackList | true |
| Device.WiFi.AccessPoint.2.X_CISCO_COM_MacFilterTable.{i}.MACAddress | Invalid MAC address (not the WLAN client MAC) |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>SET MAC filter enable to true and FilterAsBlackList to false for all radios; SET FilterAsBlackList to true for 5GHz</small> | <small>&nbsp;</small> | <small>Verify 5GHz deny mode is configured. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>ADD row to Device.WiFi.AccessPoint.2.X_CISCO_COM_MacFilterTable and SET MACAddress to an invalid MAC (aa:bb:cc:dd:ee:ff)</small> | <small>&nbsp;</small> | <small>Verify invalid MAC is set in the 5GHz deny filter table. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.WiFi.SSID.2.BSSID and configure 5GHz SSID/passphrase; wait 60 seconds</small> | <small>&nbsp;</small> | <small>Verify configuration is applied. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Connect to 5GHz WiFi SSID using the 5GHz BSSID</small> | <small>Verify WLAN client connects successfully as its MAC is not in the deny list. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.WiFi.Radio.2.PossibleChannels</small> | <small>&nbsp;</small> | <small>Verify 5GHz possible channel list is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify the connected channel belongs to the 5GHz possible channels; disconnect</small> | <small>Verify WLAN client is confirmed connected on the 5GHz band. If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>Revert SSID/passphrase, delete MAC filter table entry, and revert MAC filter settings</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

</details>

---

<details>
<summary><strong>Provisioning and Management</strong></summary>

# Provisioning and Management

<details>
<summary><strong>Test Case 1: Verify admin user remote access capability can be toggled</strong></summary>

## Test Case 1: TS_PAM_DeviceUsers_EnableAdminRemoteAccess

## Objectives
Verify that the remote access capability of the admin user (Device.Users.User.3.RemoteAccessCapable) can be toggled successfully.

## Test Case ID
TC_PAM_61

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Users.User.3.RemoteAccessCapable | true (or false, toggled from current value) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Users.User.3.RemoteAccessCapable and save the current value</small> | <small>Verify the current remote access capability value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.Users.User.3.RemoteAccessCapable to the opposite of the current value</small> | <small>Verify the SET operation is successful. If the condition is met PASS, else FAIL</small> |
| <small>3</small> | <small>SET Device.Users.User.3.RemoteAccessCapable back to the original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 2: Verify admin user account Enable status can be set to true</strong></summary>

## Test Case 2: TS_PAM_DeviceUsers_EnableAdminUser

## Objectives
Verify that the Enable status of the admin user account (Device.Users.User.{i}.Enable) can be set to true.

## Test Case ID
TC_PAM_62

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Users.User.{i}.Enable | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Users.User.{i}.Username for each user entry to identify the admin user index</small> | <small>Verify the admin user entry is found successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Users.User.{i}.Enable for the admin user and save the current value</small> | <small>Verify the current Enable value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.Users.User.{i}.Enable = true for the admin user</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Users.User.{i}.Enable for the admin user</small> | <small>Verify the retrieved value equals true. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET Device.Users.User.{i}.Enable back to the original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 3: Verify CusAdmin user remote access capability can be toggled</strong></summary>

## Test Case 3: TS_PAM_DeviceUsers_EnableCusAdminRemoteAccess

## Objectives
Verify that the remote access capability of the CusAdmin user (Device.Users.User.2.RemoteAccessCapable) can be toggled successfully.

## Test Case ID
TC_PAM_63

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Users.User.2.RemoteAccessCapable | true (or false, toggled from current value) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Users.User.2.RemoteAccessCapable and save the current value</small> | <small>Verify the current remote access capability value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.Users.User.2.RemoteAccessCapable to the opposite of the current value</small> | <small>Verify the SET operation is successful. If the condition is met PASS, else FAIL</small> |
| <small>3</small> | <small>SET Device.Users.User.2.RemoteAccessCapable back to the original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 4: Verify CusAdmin user account Enable status can be set to true</strong></summary>

## Test Case 4: TS_PAM_DeviceUsers_EnableCusAdminUser

## Objectives
Verify that the Enable status of the CusAdmin user account (Device.Users.User.{i}.Enable) can be set to true.

## Test Case ID
TC_PAM_64

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Users.User.{i}.Enable | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Users.User.{i}.Username for each user entry to identify the CusAdmin user index</small> | <small>Verify the CusAdmin user entry is found successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Users.User.{i}.Enable for the CusAdmin user and save the current value</small> | <small>Verify the current Enable value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.Users.User.{i}.Enable = true for the CusAdmin user</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Users.User.{i}.Enable for the CusAdmin user</small> | <small>Verify the retrieved value equals true. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET Device.Users.User.{i}.Enable back to the original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 5: Verify MSO user remote access capability can be set to true</strong></summary>

## Test Case 5: TS_PAM_DeviceUsers_EnableMSORemoteAccess

## Objectives
Verify that the remote access capability of the MSO user (Device.Users.User.{i}.X_CISCO_COM_UIRemoteAccess) can be set to true.

## Test Case ID
TC_PAM_65

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Users.User.{i}.X_CISCO_COM_UIRemoteAccess | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Users.User.{i}.Username for each user entry to identify the MSO user index</small> | <small>Verify the MSO user entry is found successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Users.User.{i}.X_CISCO_COM_UIRemoteAccess for the MSO user and save the current value</small> | <small>Verify the current remote access value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.Users.User.{i}.X_CISCO_COM_UIRemoteAccess = true for the MSO user</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Users.User.{i}.X_CISCO_COM_UIRemoteAccess for the MSO user</small> | <small>Verify the retrieved value equals true. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET Device.Users.User.{i}.X_CISCO_COM_UIRemoteAccess back to the original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 6: Verify MSO user account Enable status can be set to true</strong></summary>

## Test Case 6: TS_PAM_DeviceUsers_EnableMSOUser

## Objectives
Verify that the Enable status of the MSO user account (Device.Users.User.{i}.Enable) can be set to true.

## Test Case ID
TC_PAM_66

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Users.User.{i}.Enable | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Users.User.{i}.Username for each user entry to identify the MSO user index</small> | <small>Verify the MSO user entry is found successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Users.User.{i}.Enable for the MSO user and save the current value</small> | <small>Verify the current Enable value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.Users.User.{i}.Enable = true for the MSO user</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Users.User.{i}.Enable for the MSO user</small> | <small>Verify the retrieved value equals true. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET Device.Users.User.{i}.Enable back to the original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 7: Verify admin user password can be changed successfully</strong></summary>

## Test Case 7: TS_PAM_DeviceUsers_SetAdminPassword

## Objectives
Verify that the password of the admin user (Device.Users.User.3.Password) can be changed successfully.

## Test Case ID
TC_PAM_67

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Users.User.3.Password | random value |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Users.User.3.Password and save the current value</small> | <small>Verify the current password value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.Users.User.3.Password to a new random password string</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Users.User.3.Password</small> | <small>Verify the retrieved password value is non-empty and different from the original value. If the condition is met PASS, else FAIL</small> |
| <small>4</small> | <small>SET Device.Users.User.3.Password back to the original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 8: Verify CusAdmin user password can be changed successfully</strong></summary>

## Test Case 8: TS_PAM_DeviceUsers_SetCusAdminPassword

## Objectives
Verify that the password of the CusAdmin user (Device.Users.User.{i}.Password) can be changed successfully.

## Test Case ID
TC_PAM_68

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Users.User.{i}.Password | TestPassword |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Users.User.{i}.Username for each user entry to identify the CusAdmin user index</small> | <small>Verify the CusAdmin user entry is found successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Users.User.{i}.Password for the CusAdmin user and save the current value</small> | <small>Verify the current password is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.Users.User.{i}.Password to a new password string for the CusAdmin user</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Users.User.{i}.Password for the CusAdmin user</small> | <small>Verify the retrieved password value is non-empty and different from the original. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET Device.Users.User.{i}.Password back to the original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 9: Verify all valid values can be set for the WEBUI Enable feature parameter</strong></summary>

## Test Case 9: TS_PAM_SetValidValues_WEBUI

## Objectives
Verify that all valid values (Enable, Disable, MSOonly) can be successfully set for the WEBUI feature enable parameter (Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable).

## Test Case ID
TC_PAM_238

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable | Enable |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable and save the current value</small> | <small>Verify the current value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable = Enable</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable</small> | <small>Verify the retrieved value equals Enable. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable = Disable</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable</small> | <small>Verify the retrieved value equals Disable. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable = MSOonly</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable</small> | <small>Verify the retrieved value equals MSOonly. If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable back to the original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 10: Verify disabling WebUI.Enable causes HTTP remote access to be disabled</strong></summary>

## Test Case 10: TS_PAM_DisableWEBUI

## Objectives
Verify that setting Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable to false (Disable) causes Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable to be disabled.

## Test Case ID
TC_PAM_238

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable | false |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable and save the current value</small> | <small>Verify the current HttpEnable value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable is not true, SET Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable = true</small> | <small>Verify HTTP access is enabled. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable = false</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable</small> | <small>Verify Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable is now false. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable and Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable to their original values</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 11: Verify setting WebUI.Enable to MSOonly causes HTTP remote access to be disabled</strong></summary>

## Test Case 11: TS_PAM_MSOOnlyWEBUI

## Objectives
Verify that setting Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable to MSOonly causes Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable to be disabled.

## Test Case ID
TC_PAM_240

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable | MSOonly |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable and save the current value</small> | <small>Verify the current HttpEnable value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable is not true, SET Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable = true</small> | <small>Verify HTTP access is enabled. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable = MSOonly</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable</small> | <small>Verify Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable is now false. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable and Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable to their original values</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 12: Verify syndication partner ID set and get values match after activation</strong></summary>

## Test Case 12: TS_PAM_SetSyndicationPartnerId

## Objectives
Verify that setting a syndication partner ID via Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId and activating it results in the GET value matching the SET value.

## Test Case ID
TC_PAM_159

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId | new partner ID |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId and save the current value</small> | <small>Verify the current partner ID is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId to a new partner ID value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Activate the syndication partner ID</small> | <small>Verify the activation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId</small> | <small>Verify the GET value matches the SET value. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId back to the original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 13: Verify syndication partner ID persists after device reboot</strong></summary>

## Test Case 13: TS_PAM_CheckSyndicationPartnerIdAfterReboot

## Objectives
Verify that a syndication partner ID set via Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId and activated persists after a device reboot.

## Test Case ID
TC_PAM_157

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId | new partner ID value |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId and save the current value</small> | <small>Verify the current partner ID is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId to a new partner ID value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Activate the syndication partner ID</small> | <small>Verify the activation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Reboot the DUT and wait for it to come back online</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId</small> | <small>Verify the partner ID still matches the previously set value after reboot. If the condition is met PASS, else FAIL</small> |
| <small>6</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId back to the original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 14: Verify default admin IP equals the LAN IP address</strong></summary>

## Test Case 14: TS_PAM_CheckDefaultAdminIP_EqualToLANIP

## Objectives
Verify that Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_UIBranding.DefaultAdminIP equals Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress.

## Test Case ID
TC_PAM_206

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
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_UIBranding.DefaultAdminIP</small> | <small>Verify the DefaultAdminIP value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>Verify the LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Compare Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_UIBranding.DefaultAdminIP with Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>Verify both values are equal. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 15: Verify default local IPv4 subnet range equals the LAN subnet mask</strong></summary>

## Test Case 15: TS_PAM_CheckDefaultLocalIPv4SubnetRange_EqualToLanSubnetMask

## Objectives
Verify that Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_UIBranding.DefaultLocalIPv4SubnetRange equals Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask.

## Test Case ID
TC_PAM_207

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
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_UIBranding.DefaultLocalIPv4SubnetRange</small> | <small>Verify the DefaultLocalIPv4SubnetRange value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask</small> | <small>Verify the LAN subnet mask is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Compare both values</small> | <small>Verify both values are equal. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 16: Verify DNS server IP cannot be set when server type is not static</strong></summary>

## Test Case 16: TS_PAM_DNSClient_SetDNSServerIP

## Objectives
Verify that setting Device.DNS.Client.Server.1.DNSServer fails when the DNS server type (Device.DNS.Client.Server.1.Type) is not static.

## Test Case ID
TC_PAM_180

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
| <small>1</small> | <small>GET Device.IP.Interface.{i} to retrieve an available IP interface</small> | <small>Verify an IP interface is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.DNS.Client.Server.1.Type</small> | <small>Verify the DNS server type is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>If type is not static, SET Device.DNS.Client.Server.1.DNSServer to a new IP address value</small> | <small>Verify the SET operation fails when the server type is not static. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 17: Verify DNS server interface cannot be set when server type is not static</strong></summary>

## Test Case 17: TS_PAM_DNSClient_SetServerInterface

## Objectives
Verify that setting Device.DNS.Client.Server.1.Interface fails when the DNS server type (Device.DNS.Client.Server.1.Type) is not static.

## Test Case ID
TC_PAM_181

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
| <small>1</small> | <small>GET Device.IP.Interface.{i} to retrieve an available IP interface</small> | <small>Verify an IP interface is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.DNS.Client.Server.1.Type</small> | <small>Verify the DNS server type is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>If type is not static, SET Device.DNS.Client.Server.1.Interface to an interface value</small> | <small>Verify the SET operation fails when the server type is not static. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 18: Verify dnsmasq restart does not log DNS strict order message when DNSStrictOrder is enabled</strong></summary>

## Test Case 18: TS_PAM_CheckDnsmasqRestartLogs_DNSStrictOrderEnabled

## Objectives
Verify that when Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable is set to true, restarting the dnsmasq process does not cause the "RFC DNSTRICT ORDER is not defined or Enabled" log message to be written to /rdklogs/logs/Consolelog.txt.0.

## Test Case ID
TC_PAM_220

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable and save the initial value</small> | <small>Verify the current value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If the value is not true, SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable = true</small> | <small>Verify DNSStrictOrder is enabled. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Get the current count of "RFC DNSTRICT ORDER is not defined or Enabled" lines in /rdklogs/logs/Consolelog.txt.0</small> | <small>Verify the initial log count is obtained. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Kill the dnsmasq process to force a restart and wait for dnsmasq to restart</small> | <small>Verify the dnsmasq process is killed and restarted. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Get the new count of "RFC DNSTRICT ORDER is not defined or Enabled" lines in /rdklogs/logs/Consolelog.txt.0</small> | <small>Verify the log count has NOT incremented after dnsmasq restart with DNSStrictOrder enabled. If the condition is met PASS, else FAIL</small> |
| <small>6</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable back to the initial value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 19: Verify dnsmasq restart logs DNS strict order message when DNSStrictOrder is disabled</strong></summary>

## Test Case 19: TS_PAM_CheckDnsmasqRestartLogs_DNSStrictOrderDisabled

## Objectives
Verify that when Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable is set to false, restarting the dnsmasq process causes the "RFC DNSTRICT ORDER is not defined or Enabled" log message count to increment by 1.

## Test Case ID
TC_PAM_221

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable | false |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable and save the initial value</small> | <small>Verify the current value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If the value is not false, SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable = false</small> | <small>Verify DNSStrictOrder is disabled. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Get the current count of "RFC DNSTRICT ORDER is not defined or Enabled" lines in /rdklogs/logs/Consolelog.txt.0</small> | <small>Verify the initial log count is obtained. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Kill the dnsmasq process to force a restart and wait for dnsmasq to restart</small> | <small>Verify the dnsmasq process is killed and restarted. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Get the new count of "RFC DNSTRICT ORDER is not defined or Enabled" lines in /rdklogs/logs/Consolelog.txt.0</small> | <small>Verify the log count has incremented by 1 after dnsmasq restart with DNSStrictOrder disabled. If the condition is met PASS, else FAIL</small> |
| <small>6</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable back to the initial value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 20: Verify LAN client lease entries in dnsmasq.leases persist after device reboot</strong></summary>

## Test Case 20: TS_PAM_DNSMasq_Lease

## Objectives
Verify that the IP address and MAC address of a connected LAN client are reflected in the /nvram/dnsmasq.leases file and that these lease entries persist after a device reboot.

## Test Case ID
TC_PAM_248

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired Ethernet client connected to DUT LAN port |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Hosts.HostNumberOfEntries</small> | <small>&nbsp;</small> | <small>Verify at least one LAN client is connected. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Iterate through Device.Hosts.Host.{i}.Layer1Interface to identify an Ethernet-connected LAN client</small> | <small>&nbsp;</small> | <small>Verify an Ethernet-connected LAN client is found. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Hosts.Host.{i}.IPAddress and Device.Hosts.Host.{i}.PhysAddress for the identified LAN client</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address and MAC address are retrieved and non-empty. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Read the /nvram/dnsmasq.leases file on DUT</small> | <small>&nbsp;</small> | <small>Verify /nvram/dnsmasq.leases contains the LAN client IP address and MAC address. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Reboot the DUT and wait for it to come back online</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>6</small> | <small>Read the /nvram/dnsmasq.leases file on DUT after reboot</small> | <small>&nbsp;</small> | <small>Verify /nvram/dnsmasq.leases still contains the LAN client IP address and MAC address after reboot. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 21: Verify DHCP pool start address cannot be set to the LAN gateway IP</strong></summary>

## Test Case 21: TS_PAM_SetDHCPBeginIPasLANGatewayIP

## Objectives
Verify that setting the DHCP begin address (Device.DHCPv4.Server.Pool.1.MinAddress) to the same value as the LAN Gateway IP address fails.

## Test Case ID
TC_PAM_175

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
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to retrieve the LAN gateway IP address</small> | <small>Verify the LAN gateway IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Attempt to SET Device.DHCPv4.Server.Pool.1.MinAddress to the retrieved LAN gateway IP address value</small> | <small>Verify the SET operation fails. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 22: Verify DHCP pool end address cannot be set beyond the subnet mask range</strong></summary>

## Test Case 22: TS_PAM_SetDHCPEndIPBeyondSubnetRange

## Objectives
Verify that setting the DHCP end IP address (Device.DHCPv4.Server.Pool.1.MaxAddress) to a value beyond the subnet mask range fails.

## Test Case ID
TC_PAM_176

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>Verify the LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask = 255.255.255.0</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Attempt to SET Device.DHCPv4.Server.Pool.1.MaxAddress to an address with the last octet as 255</small> | <small>Verify the SET operation fails. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 23: Verify LAN gateway IP cannot be set beyond the allowed private address range</strong></summary>

## Test Case 23: TS_PAM_SetDHCPServerIPBeyondPrivateAddressRange

## Objectives
Verify that setting Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to an IP address beyond the allowed private address range fails.

## Test Case ID
TC_PAM_177

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
| <small>1</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to an IP address beyond the allowed private address range (e.g., a public IP address)</small> | <small>Verify the SET operation fails. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 24: Verify MaxAddress out of range is rejected for subnet 255.255.255.0 with LAN IP 10.0.0.1</strong></summary>

## Test Case 24: TS_PAM_SetMaxAddressOutOfRange_SubnetMask255.255.255.0_LanIP10.0.0.1

## Objectives
Verify that setting Device.DHCPv4.Server.Pool.1.MaxAddress to an out-of-range value (10.0.0.255) fails when the Subnet Mask is 255.255.255.0 and LAN IP Address is 10.0.0.1.

## Test Case ID
TC_PAM_231

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET and store initial values of LanSubnetMask, LanIPAddress, MinAddress, and MaxAddress</small> | <small>Verify all values are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET LanSubnetMask = 255.255.255.0, LanIPAddress = 10.0.0.1, MinAddress = 10.0.0.2 if not already configured</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Attempt to SET Device.DHCPv4.Server.Pool.1.MaxAddress = 10.0.0.255</small> | <small>Verify the SET operation fails. If the condition is met PASS, else FAIL</small> |
| <small>4</small> | <small>Revert all parameters to their initial values</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 25: Verify MinAddress out of range is rejected for subnet 255.255.255.0 with LAN IP 10.0.0.4</strong></summary>

## Test Case 25: TS_PAM_SetMinAddressOutOfRange_SubnetMask255.255.255.0_LanIP10.0.0.4

## Objectives
Verify that setting Device.DHCPv4.Server.Pool.1.MinAddress to an out-of-range value (10.0.0.3) fails when the Subnet Mask is 255.255.255.0 and LAN IP Address is 10.0.0.4.

## Test Case ID
TC_PAM_232

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.4 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET and store initial values of LanSubnetMask, LanIPAddress, MinAddress, and MaxAddress</small> | <small>Verify all values are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET LanSubnetMask = 255.255.255.0, LanIPAddress = 10.0.0.4, MaxAddress = 10.0.0.253 if not already configured</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Attempt to SET Device.DHCPv4.Server.Pool.1.MinAddress = 10.0.0.3</small> | <small>Verify the SET operation fails. If the condition is met PASS, else FAIL</small> |
| <small>4</small> | <small>Revert all parameters to their initial values</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 26: Verify invalid MaxAddress with last octet less than 2 is rejected for subnet 255.255.0.0</strong></summary>

## Test Case 26: TS_PAM_SetInvalidMaxAddress_SubnetMask255.255.0.0_LanIP10.1.10.1

## Objectives
Verify that setting Device.DHCPv4.Server.Pool.1.MaxAddress to an invalid value 10.1.255.1 fails when the Subnet Mask is 255.255.0.0 and LAN IP Address is 10.1.10.1.

## Test Case ID
TC_PAM_233

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.0.0 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.1.10.1 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.1.10.2 |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET and store initial values of LanSubnetMask, LanIPAddress, MinAddress, and MaxAddress</small> | <small>Verify all values are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET LanSubnetMask = 255.255.0.0, LanIPAddress = 10.1.10.1, MinAddress = 10.1.10.2 if not already configured</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Attempt to SET Device.DHCPv4.Server.Pool.1.MaxAddress = 10.1.255.1</small> | <small>Verify the SET operation fails. If the condition is met PASS, else FAIL</small> |
| <small>4</small> | <small>Revert all parameters to their initial values</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 27: Verify MaxAddress equal to MinAddress is rejected for subnet 255.255.0.0 with LAN IP 10.1.10.1</strong></summary>

## Test Case 27: TS_PAM_SetEqualMinAndMaxAddress_SubnetMask255.255.0.0_LanIP10.1.10.1

## Objectives
Verify that setting Device.DHCPv4.Server.Pool.1.MaxAddress to the same value as Device.DHCPv4.Server.Pool.1.MinAddress (10.1.10.2) fails when the Subnet Mask is 255.255.0.0 and LAN IP is 10.1.10.1.

## Test Case ID
TC_PAM_234

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.0.0 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.1.10.1 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.1.10.2 |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET and store initial values of LanSubnetMask, LanIPAddress, MinAddress, and MaxAddress</small> | <small>Verify all values are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET LanSubnetMask = 255.255.0.0, LanIPAddress = 10.1.10.1, MinAddress = 10.1.10.2 if not already configured</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Attempt to SET Device.DHCPv4.Server.Pool.1.MaxAddress = 10.1.10.2 (equal to MinAddress)</small> | <small>Verify the SET operation fails. If the condition is met PASS, else FAIL</small> |
| <small>4</small> | <small>Revert all parameters to their initial values</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 28: Verify MaxAddress lesser than MinAddress is rejected for subnet 255.255.255.0 with LAN IP 10.0.0.1</strong></summary>

## Test Case 28: TS_PAM_SetMaxAddrLesserThanMinAddr_SubnetMask255.255.255.0_LanIP10.0.0.1

## Objectives
Verify that setting Device.DHCPv4.Server.Pool.1.MaxAddress to a value lesser than Device.DHCPv4.Server.Pool.1.MinAddress fails.

## Test Case ID
TC_PAM_235

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.10 |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET and store initial values of LanSubnetMask, LanIPAddress, MinAddress, and MaxAddress</small> | <small>Verify all values are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET LanSubnetMask = 255.255.255.0, LanIPAddress = 10.0.0.1, MinAddress = 10.0.0.10, MaxAddress = 10.0.0.253 if not already configured</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Attempt to SET Device.DHCPv4.Server.Pool.1.MaxAddress = 10.0.0.8 (less than MinAddress 10.0.0.10)</small> | <small>Verify the SET operation fails. If the condition is met PASS, else FAIL</small> |
| <small>4</small> | <small>Revert all parameters to their initial values</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 29: Verify MinAddress and MaxAddress derive correct defaults after LAN subnet and IP change with reboot</strong></summary>

## Test Case 29: TS_PAM_ValidateMinAndMaxAddress

## Objectives
Verify that Device.DHCPv4.Server.Pool.1.MinAddress and MaxAddress have the expected default values (10.1.10.2 and 10.1.10.253) when LanSubnetMask is set to 255.255.255.0 and LanIPAddress is set to 10.1.10.1, after a device reboot.

## Test Case ID
TC_PAM_245

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.1.10.1 |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET and store LanSubnetMask and LanIPAddress initial values</small> | <small>Verify all values are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET LanSubnetMask = 255.255.255.0 and LanIPAddress = 10.1.10.1</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Reboot the DUT and wait for it to come back online</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>GET Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>Verify MinAddress equals 10.1.10.2 and MaxAddress equals 10.1.10.253. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>Revert LanSubnetMask and LanIPAddress to their initial values</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 30: Verify RIP send and receive protocol version is RIP2</strong></summary>

## Test Case 30: TS_PAM_GetRIPProtocolVersion

## Objectives
Verify that the Send and Receive RIP protocol version parameters both return the value "RIP2".

## Test Case ID
TC_PAM_173

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
| <small>1</small> | <small>GET Device.Routing.RIP.InterfaceSetting.1.X_CISCO_COM_SendVersion</small> | <small>Verify the retrieved Send RIP protocol version equals "RIP2". If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Routing.RIP.InterfaceSetting.1.X_CISCO_COM_ReceiveVersion</small> | <small>Verify the retrieved Receive RIP protocol version equals "RIP2". If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 31: Verify enabling Advanced Security OTM RFC logs the enable event</strong></summary>

## Test Case 31: TS_PAM_EnableRFC_AdvSecOTMEnable

## Objectives
Verify that enabling Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable causes the "ADVANCE_SECURITY_OTM_EANBLED" log message to appear in /rdklogs/logs/agent.txt.

## Test Case ID
TC_PAM_241

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable and save the initial value</small> | <small>Verify the current value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If the initial value is true, SET it to false to ensure it starts disabled</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Get the current count of "ADVANCE_SECURITY_OTM_EANBLED" log lines in /rdklogs/logs/agent.txt</small> | <small>Verify the initial log count is obtained. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable = true</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Get the updated count of "ADVANCE_SECURITY_OTM_EANBLED" log lines</small> | <small>Verify the log count has incremented. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Verify via syscfg that "Adv_AdvSecOTMRFCEnable" reflects the enabled state</small> | <small>Verify the syscfg value is consistent. If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable back to the initial value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 32: Verify disabling Advanced Security OTM RFC logs the disable event</strong></summary>

## Test Case 32: TS_PAM_DisableRFC_AdvSecOTMEnable

## Objectives
Verify that disabling Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable causes the "ADVANCE_SECURITY_OTM_DISABLED" log message to appear in /rdklogs/logs/agent.txt.

## Test Case ID
TC_PAM_242

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable | false |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable and save the initial value</small> | <small>Verify the current value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If the initial value is false, SET it to true to ensure it starts enabled</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Get the current count of "ADVANCE_SECURITY_OTM_DISABLED" log lines in /rdklogs/logs/agent.txt</small> | <small>Verify the initial log count is obtained. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable = false</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Get the updated count of "ADVANCE_SECURITY_OTM_DISABLED" log lines</small> | <small>Verify the log count has incremented. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Verify via syscfg that "Adv_AdvSecOTMRFCEnable" reflects the disabled state</small> | <small>Verify the syscfg value is consistent. If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable back to the initial value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 33: Verify enabling DLCaStore RFC is reflected in TR181 GET and syscfg</strong></summary>

## Test Case 33: TS_PAM_EnableRFC_DLCaStoreEnable

## Objectives
Verify that enabling Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable can be set successfully and is reflected via both TR181 GET and syscfg DLCaStoreEnabled key.

## Test Case ID
TC_PAM_208

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable and save the initial value</small> | <small>Verify the current value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable = true</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable and execute syscfg get DLCaStoreEnabled</small> | <small>Verify both the TR181 GET value and the syscfg value equal true. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Check /rdklogs/logs/PAMlog.txt.0 for the RFC set log entry for DLCaStore.Enable</small> | <small>Verify the log entry confirming the enable set operation is present. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable back to the initial value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 34: Verify disabling DLCaStore RFC is reflected in TR181 GET and syscfg</strong></summary>

## Test Case 34: TS_PAM_DisableRFC_DLCaStoreEnable

## Objectives
Verify that disabling Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable can be set successfully and is reflected via both TR181 GET and syscfg DLCaStoreEnabled key.

## Test Case ID
TC_PAM_209

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable | false |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable and save the initial value</small> | <small>Verify the current value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable = false</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable and execute syscfg get DLCaStoreEnabled</small> | <small>Verify both the TR181 GET value and the syscfg value equal false. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Check /rdklogs/logs/PAMlog.txt.0 for the RFC set log entry for DLCaStore.Enable = false</small> | <small>Verify the log entry confirming the disable set operation is present. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable back to the initial value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 35: Verify SNMP Onboard Reboot Enable cannot be disabled</strong></summary>

## Test Case 35: TS_PAM_SetSnmpOnboardRebootEnable

## Objectives
Verify that attempting to disable Device.X_RDKCENTRAL-COM_XPC.SnmpOnboardReboot.Enable (set to false) fails.

## Test Case ID
TC_PAM_189

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
| <small>1</small> | <small>GET Device.X_RDKCENTRAL-COM_XPC.SnmpOnboardReboot.Enable</small> | <small>Verify the parameter value is true (enabled). If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Attempt to SET Device.X_RDKCENTRAL-COM_XPC.SnmpOnboardReboot.Enable = false</small> | <small>Verify the SET operation fails (disable is not permitted). If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 36: Verify LAN status is stopped when device is set to bridge-static mode</strong></summary>

## Test Case 36: TS_PAM_BridgeModeCheckLANStatus

## Objectives
Verify that when the device is set to bridge-static mode, the LAN status (sysevent get lan-status) transitions to "stopped".

## Test Case ID
TC_PAM_223

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode | bridge-static |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode and save the current value</small> | <small>Verify the current LAN mode is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode = bridge-static and wait 60 seconds</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Execute sysevent get lan-status on the DUT</small> | <small>Verify the lan-status equals "stopped". If the condition is met PASS, else FAIL</small> |
| <small>4</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode back to the original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 37: Verify IPv4 BlockFragIPPkts iptables rules are added and removed on enable and disable</strong></summary>

## Test Case 37: TS_PAM_SetFirewallSecurityIPv4BlockFragIPPkts

## Objectives
Verify that IPv4 iptable rules associated with Device.Firewall.X_RDKCENTRAL-COM_Security.V4.BlockFragIPPkts are added to iptables when enabled and removed when disabled.

## Test Case ID
TC_PAM_192

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Firewall.X_RDKCENTRAL-COM_Security.V4.BlockFragIPPkts | true (or false, toggled from current value) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Firewall.X_RDKCENTRAL-COM_Security.V4.BlockFragIPPkts and save the current value</small> | <small>Verify the current value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If the current value is true, verify all iptable rules associated with BlockFragIPPkts are present in iptables</small> | <small>Verify the iptable rules are present when the parameter is enabled. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.Firewall.X_RDKCENTRAL-COM_Security.V4.BlockFragIPPkts = false; wait 60 seconds</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Verify iptable rules associated with BlockFragIPPkts are no longer present in iptables</small> | <small>Verify the iptable rules are removed when the parameter is disabled. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET Device.Firewall.X_RDKCENTRAL-COM_Security.V4.BlockFragIPPkts back to the initial value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 38: Verify IPv4 IPFloodDetect iptables rules are added and removed on enable and disable</strong></summary>

## Test Case 38: TS_PAM_SetFirewallSecurityIPv4IPFloodDetect

## Objectives
Verify that IPv4 iptable rules associated with Device.Firewall.X_RDKCENTRAL-COM_Security.V4.IPFloodDetect are added to iptables when enabled and removed when disabled.

## Test Case ID
TC_PAM_190

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Firewall.X_RDKCENTRAL-COM_Security.V4.IPFloodDetect | true (or false, toggled from current value) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Firewall.X_RDKCENTRAL-COM_Security.V4.IPFloodDetect and save the current value</small> | <small>Verify the current value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If the current value is true, verify all iptable rules associated with IPFloodDetect are present in iptables</small> | <small>Verify the iptable rules are present when the parameter is enabled. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.Firewall.X_RDKCENTRAL-COM_Security.V4.IPFloodDetect = false; wait 60 seconds</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Verify iptable rules associated with IPFloodDetect are no longer present in iptables</small> | <small>Verify the iptable rules are removed when the parameter is disabled. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET Device.Firewall.X_RDKCENTRAL-COM_Security.V4.IPFloodDetect back to the initial value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 39: Verify IPv4 PortScanProtect iptables rules are added and removed on enable and disable</strong></summary>

## Test Case 39: TS_PAM_SetFirewallSecurityIPv4PortScanProtect

## Objectives
Verify that IPv4 iptable rules associated with Device.Firewall.X_RDKCENTRAL-COM_Security.V4.PortScanProtect are added to iptables when enabled and removed when disabled.

## Test Case ID
TC_PAM_191

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Firewall.X_RDKCENTRAL-COM_Security.V4.PortScanProtect | true (or false, toggled from current value) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Firewall.X_RDKCENTRAL-COM_Security.V4.PortScanProtect and save the current value</small> | <small>Verify the current value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If the current value is true, verify all iptable rules associated with PortScanProtect are present in iptables</small> | <small>Verify the iptable rules are present when the parameter is enabled. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.Firewall.X_RDKCENTRAL-COM_Security.V4.PortScanProtect = false; wait 60 seconds</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Verify iptable rules associated with PortScanProtect are no longer present in iptables</small> | <small>Verify the iptable rules are removed when the parameter is disabled. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET Device.Firewall.X_RDKCENTRAL-COM_Security.V4.PortScanProtect back to the initial value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 40: Verify IPv6 BlockFragIPPkts ip6tables rules are added and removed on enable and disable</strong></summary>

## Test Case 40: TS_PAM_SetFirewallSecurityIPv6BlockFragIPPkts

## Objectives
Verify that IPv6 iptable rules associated with Device.Firewall.X_RDKCENTRAL-COM_Security.V6.BlockFragIPPkts are added to ip6tables when enabled and removed when disabled.

## Test Case ID
TC_PAM_195

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Firewall.X_RDKCENTRAL-COM_Security.V6.BlockFragIPPkts | true (or false, toggled from current value) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Firewall.X_RDKCENTRAL-COM_Security.V6.BlockFragIPPkts and save the current value</small> | <small>Verify the current value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If the current value is true, verify all ip6tables rules associated with BlockFragIPPkts are present</small> | <small>Verify the ip6tables rules are present when the parameter is enabled. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.Firewall.X_RDKCENTRAL-COM_Security.V6.BlockFragIPPkts = false; wait 60 seconds</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Verify ip6tables rules associated with BlockFragIPPkts are no longer present</small> | <small>Verify the ip6tables rules are removed when the parameter is disabled. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET Device.Firewall.X_RDKCENTRAL-COM_Security.V6.BlockFragIPPkts back to the initial value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 41: Verify IPv6 IPFloodDetect ip6tables rules are added and removed on enable and disable</strong></summary>

## Test Case 41: TS_PAM_SetFirewallSecurityIPv6IPFloodDetect

## Objectives
Verify that IPv6 iptable rules associated with Device.Firewall.X_RDKCENTRAL-COM_Security.V6.IPFloodDetect are added to ip6tables when enabled and removed when disabled.

## Test Case ID
TC_PAM_193

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Firewall.X_RDKCENTRAL-COM_Security.V6.IPFloodDetect | true (or false, toggled from current value) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Firewall.X_RDKCENTRAL-COM_Security.V6.IPFloodDetect and save the current value</small> | <small>Verify the current value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If the current value is true, verify all ip6tables rules associated with IPFloodDetect are present</small> | <small>Verify the ip6tables rules are present when the parameter is enabled. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.Firewall.X_RDKCENTRAL-COM_Security.V6.IPFloodDetect = false; wait 60 seconds</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Verify ip6tables rules associated with IPFloodDetect are no longer present</small> | <small>Verify the ip6tables rules are removed when the parameter is disabled. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET Device.Firewall.X_RDKCENTRAL-COM_Security.V6.IPFloodDetect back to the initial value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 42: Verify IPv6 PortScanProtect ip6tables rules are added and removed on enable and disable</strong></summary>

## Test Case 42: TS_PAM_SetFirewallSecurityIPv6PortScanProtect

## Objectives
Verify that IPv6 iptable rules associated with Device.Firewall.X_RDKCENTRAL-COM_Security.V6.PortScanProtect are added to ip6tables when enabled and removed when disabled.

## Test Case ID
TC_PAM_194

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Firewall.X_RDKCENTRAL-COM_Security.V6.PortScanProtect | true (or false, toggled from current value) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Firewall.X_RDKCENTRAL-COM_Security.V6.PortScanProtect and save the current value</small> | <small>Verify the current value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If the current value is true, verify all ip6tables rules associated with PortScanProtect are present</small> | <small>Verify the ip6tables rules are present when the parameter is enabled. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.Firewall.X_RDKCENTRAL-COM_Security.V6.PortScanProtect = false; wait 60 seconds</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Verify ip6tables rules associated with PortScanProtect are no longer present</small> | <small>Verify the ip6tables rules are removed when the parameter is disabled. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET Device.Firewall.X_RDKCENTRAL-COM_Security.V6.PortScanProtect back to the initial value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 43: Verify SelfHeal aggressive interval and compute window have correct default values after factory reset</strong></summary>

## Test Case 43: TS_PAM_CheckDefaultValues_SelfHealAggresInterval

## Objectives
Verify that after a factory reset, SelfHeal.AggressiveInterval and UsageComputeWindow have their expected default values (5 and 15 respectively), and that SelfHealAggressive.txt log file is present.

## Test Case ID
TC_PAM_189

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.FactoryReset | Router,Wifi,VoIP,Dect,MoCA |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.X_CISCO_COM_DeviceControl.FactoryReset = Router,Wifi,VoIP,Dect,MoCA and wait for device to come back online</small> | <small>Verify factory reset completes successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SoftwareProcessManager.SelfHeal.AggressiveInterval and Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_UsageComputeWindow</small> | <small>Verify AggressiveInterval equals 5 and UsageComputeWindow equals 15. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Check if /rdklogs/logs/SelfHealAggressive.txt file exists on the DUT</small> | <small>Verify the SelfHealAggressive.txt log file is present. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SoftwareProcessManager.SelfHeal.AggressiveInterval = 6</small> | <small>Verify the SET operation is successful. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>SET AggressiveInterval back to 5</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 44: Verify SelfHeal aggressive interval rejects values below the minimum</strong></summary>

## Test Case 44: TS_PAM_SetInvalid_SelfHealAggresInterval

## Objectives
Verify that setting SelfHeal.AggressiveInterval to an invalid value (1 minute, which is below the minimum of 2 minutes) fails.

## Test Case ID
TC_PAM_190

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
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SoftwareProcessManager.SelfHeal.AggressiveInterval and save the current value</small> | <small>Verify the current value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Attempt to SET AggressiveInterval = 1 (below minimum of 2 minutes)</small> | <small>Verify the SET operation fails. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 45: Verify SelfHeal aggressive interval is rejected when greater than compute window and accepted when lesser</strong></summary>

## Test Case 45: TS_PAM_SetAggresInterval_GreaterAndlessthanComputeWindow

## Objectives
Verify that SelfHeal.AggressiveInterval accepts values lesser than the compute window but rejects values greater than or equal to the compute window.

## Test Case ID
TC_PAM_186

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
| <small>1</small> | <small>GET UsageComputeWindow and AggressiveInterval and save both values</small> | <small>Verify both values are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Attempt to SET AggressiveInterval to a value greater than UsageComputeWindow</small> | <small>Verify the SET operation fails. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET AggressiveInterval to a value lesser than UsageComputeWindow</small> | <small>Verify the SET operation succeeds. If the condition is met PASS, else FAIL</small> |
| <small>4</small> | <small>SET AggressiveInterval back to the original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 46: Verify UsageComputeWindow cannot be set equal to AggressiveInterval</strong></summary>

## Test Case 46: TS_PAM_SetComputeWindow_EqualtoSetAggresInterval

## Objectives
Verify that setting Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_UsageComputeWindow to a value equal to AggressiveInterval fails.

## Test Case ID
TC_PAM_187

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
| <small>1</small> | <small>GET AggressiveInterval and UsageComputeWindow and save both values</small> | <small>Verify both values are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Attempt to SET UsageComputeWindow equal to AggressiveInterval</small> | <small>Verify the SET operation fails. If the condition is met PASS, else FAIL</small> |
| <small>3</small> | <small>Revert UsageComputeWindow to the original value if the SET succeeded unexpectedly</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 47: Verify UsageComputeWindow cannot be set below AggressiveInterval</strong></summary>

## Test Case 47: TS_PAM_SetComputeWindow_BelowAggresInterval

## Objectives
Verify that setting Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_UsageComputeWindow to a value less than AggressiveInterval fails.

## Test Case ID
TC_PAM_188

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
| <small>1</small> | <small>GET UsageComputeWindow and AggressiveInterval and save both values</small> | <small>Verify both values are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Attempt to SET UsageComputeWindow to a value less than AggressiveInterval</small> | <small>Verify the SET operation fails. If the condition is met PASS, else FAIL</small> |
| <small>3</small> | <small>Revert UsageComputeWindow to the original value if the SET succeeded unexpectedly</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 48: Verify AutoReboot UpTime rejects values outside the valid range after factory reset</strong></summary>

## Test Case 48: TS_PAM_SetInvalidAutoRebootuptime

## Objectives
Verify that Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AutoReboot.UpTime rejects invalid values (outside the valid range of 1 to 365 days).

## Test Case ID
TC_PAM_163

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.FactoryReset | Router,Wifi,Firewall |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.X_CISCO_COM_DeviceControl.FactoryReset = Router,Wifi,Firewall and wait for device to come back online</small> | <small>Verify factory reset completes successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AutoReboot.Enable</small> | <small>Verify AutoReboot.Enable equals true after factory reset. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AutoReboot.UpTime</small> | <small>Verify AutoReboot.UpTime equals 120 (default). If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Attempt to SET AutoReboot.UpTime to -1</small> | <small>Verify the SET operation fails for invalid value -1. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Attempt to SET AutoReboot.UpTime to 0</small> | <small>Verify the SET operation fails for invalid value 0. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Attempt to SET AutoReboot.UpTime to 366</small> | <small>Verify the SET operation fails for invalid value 366. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Attempt to SET AutoReboot.UpTime to 367</small> | <small>Verify the SET operation fails for invalid value 367. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 49: Verify factory reset count increments by one after factory reset</strong></summary>

## Test Case 49: TS_PAM_CheckFactoryResetCount

## Objectives
Verify that after a factory reset, the factory reset count (Device.DeviceInfo.X_RDKCENTRAL-COM_FactoryResetCount) increments by 1.

## Test Case ID
TC_PAM_161

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.FactoryReset | Router,Wifi,Firewall |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_FactoryResetCount and save the initial count</small> | <small>Verify the factory reset count is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.FactoryReset = Router,Wifi,Firewall and wait for device to come back online</small> | <small>Verify factory reset completes successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_FactoryResetCount</small> | <small>Verify the factory reset count equals the initial count plus 1. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 50: Verify last reboot reason is factory-reset after factory reset</strong></summary>

## Test Case 50: TS_PAM_GetLastRebootReasonAfterFactoryReset

## Objectives
Verify that after a factory reset, Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason equals "factory-reset".

## Test Case ID
TC_PAM_153

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.FactoryReset | Router,Wifi,VoIP,Dect,MoCA |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.X_CISCO_COM_DeviceControl.FactoryReset = Router,Wifi,VoIP,Dect,MoCA and wait for device to come back online</small> | <small>Verify factory reset completes successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason</small> | <small>Verify the last reboot reason equals "factory-reset". If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 51: Verify admin user password is empty by default after factory reset</strong></summary>

## Test Case 51: TS_PAM_FRCheckDefaultPasswordisEmpty

## Objectives
Verify that after a factory reset, the admin user password (Device.Users.User.{i}.Password) is empty as expected by default.

## Test Case ID
TC_PAM_237

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.FactoryReset | Router,Wifi,Firewall |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.X_CISCO_COM_DeviceControl.FactoryReset = Router,Wifi,Firewall and wait for device to come back online</small> | <small>Verify factory reset completes successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Users.User.{i}.Password via TR181 for the admin user</small> | <small>Verify the password value is empty after factory reset. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Execute syscfg get to retrieve the admin password from syscfg database</small> | <small>Verify the syscfg value is also empty. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 52: Verify device uptime resets to a lower value after reboot</strong></summary>

## Test Case 52: TS_PAM_GetUpTime_AfterReboot

## Objectives
Verify that Device.DeviceInfo.UpTime is greater than zero after the device reboots, confirming that the uptime is reset and updated correctly following a reboot.

## Test Case ID
TC_PAM_82

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
| <small>1</small> | <small>GET Device.DeviceInfo.UpTime before reboot and save the value</small> | <small>Verify the uptime is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Reboot the DUT and wait for it to come back online</small> | <small>&nbsp;</small> |
| <small>3</small> | <small>GET Device.DeviceInfo.UpTime after reboot</small> | <small>Verify the uptime after reboot is greater than 0 and less than the pre-reboot value. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 53: Verify device current local time parameter returns a non-empty value</strong></summary>

## Test Case 53: TS_PAM_GetCurrentLocalTime

## Objectives
Verify that the Device.Time.CurrentLocalTime parameter returns a non-empty value.

## Test Case ID
TC_PAM_91

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
| <small>1</small> | <small>GET Device.Time.CurrentLocalTime</small> | <small>Verify the current local time value is non-empty. If the condition is met PASS, else FAIL</small> |

</details>

---

</details>

---

<details>
<summary><strong>Firmware Upgrade</strong></summary>

# Firmware Upgrade

<details>
<summary><strong>Test Case 1: TS_FirmwareUpgrade_UsingFWUpgradeManager</strong></summary>

## Test Case 1: TS_FirmwareUpgrade_UsingFWUpgradeManager

## Objectives
This test validates firmware upgrade on the DUT using Firmware Upgrade Manager TR-181 parameters. It configures the target firmware details, triggers the download via Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadAndFactoryReset, and verifies the DUT boots with the target firmware.

## Test Case ID
TC_FirmwareUpgrade_1

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Broadband residential gateway (RDKB) |
| WAN System - HTTP server hosting firmware images |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadProtocol | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadURL | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareToDownload | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadAndFactoryReset | 1 |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Precondition: A Python HTTP server with target firmware image is running on a machine accessible from the DUT.</small> | <small>&nbsp;</small> |
| <small>2</small> | <small>Execute ifconfig on the eRouter interface to obtain the eRouter IP address of the DUT</small> | <small>Validate eRouter IP address is obtained successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Execute `cat /version.txt` on DUT to read the current firmware image name</small> | <small>Validate current firmware version and filename are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Execute curl command to query availability of the target firmware image on the HTTP server</small> | <small>Validate HTTP server returns 200 OK for the target firmware and the target firmware is different from the current firmware. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadProtocol; GET FirmwareDownloadURL; GET FirmwareToDownload; GET FirmwareDownloadAndFactoryReset</small> | <small>Validate all current firmware upgrade configuration values are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus</small> | <small>Validate initial FirmwareDownloadStatus is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>SET FirmwareDownloadProtocol; SET FirmwareDownloadURL to the configured firmware server URL; SET FirmwareToDownload to the target firmware filename; SET FirmwareDownloadAndFactoryReset to 1 to trigger firmware download</small> | <small>Validate all firmware upgrade parameters are set successfully and firmware download is triggered. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus; DUT downloads target firmware and reboots to apply the upgrade</small> | <small>Validate FirmwareDownloadStatus is "Completed". If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>Execute `cat /version.txt` on DUT after firmware upgrade reboot</small> | <small>Validate current firmware version matches the target firmware version. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>Execute `cat /version.txt` on DUT after firmware recovery reboot</small> | <small>Validate current firmware version matches the initial firmware version. If the condition is met CONTINUE, else FAIL</small> |
| <small>11</small> | <small>Revert FirmwareDownloadProtocol, FirmwareDownloadURL, and FirmwareToDownload to original values (without triggering download)</small> | <small>Validate firmware upgrade configuration values are restored to original values successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 2: TS_FirmwareUpgrade_SetInvalidFirmwareToDownload</strong></summary>

## Test Case 2: TS_FirmwareUpgrade_SetInvalidFirmwareToDownload

## Objectives
This test verifies that setting an invalid firmware image name via TR-181 parameters causes the firmware download to fail on the DUT. Successful validation is confirmed when FirmwareDownloadStatus reports "Failed".

## Test Case ID
TC_FirmwareUpgrade_2

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Broadband residential gateway (RDKB) |
| WAN System - HTTP server hosting firmware images |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadProtocol | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadURL | As per test configuration (valid server URL) |
| Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareToDownload | Invalid, non-existent firmware filename |
| Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadAndFactoryReset | 1 |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Precondition: A Python HTTP server with target firmware image is running on a machine accessible from the DUT.</small> | <small>&nbsp;</small> |
| <small>2</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadProtocol; GET FirmwareDownloadURL; GET FirmwareToDownload; GET FirmwareDownloadAndFactoryReset</small> | <small>Validate all current firmware upgrade configuration values are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus</small> | <small>Validate initial FirmwareDownloadStatus is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>SET FirmwareDownloadProtocol to a valid protocol; SET FirmwareDownloadURL to a valid server URL; SET FirmwareToDownload to an invalid, non-existent firmware filename; SET FirmwareDownloadAndFactoryReset to 1</small> | <small>Validate firmware upgrade parameters are set successfully and firmware download is triggered. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus</small> | <small>Validate FirmwareDownloadStatus is "Failed", confirming the DUT correctly reports download failure for an invalid firmware image name. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Revert FirmwareDownloadProtocol, FirmwareDownloadURL, and FirmwareToDownload to original values (without triggering download)</small> | <small>Validate firmware upgrade configuration values are restored to original values successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 3: TS_FirmwareUpgrade_SetInvalidFirmwareUpgradeURL</strong></summary>

## Test Case 3: TS_FirmwareUpgrade_SetInvalidFirmwareUpgradeURL

## Objectives
This test verifies that setting an invalid firmware download URL via TR-181 parameters keeps the FirmwareDownloadStatus as "Not Started". Successful validation is confirmed when FirmwareDownloadStatus remains "Not Started".

## Test Case ID
TC_FirmwareUpgrade_3

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Broadband residential gateway (RDKB) |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadProtocol | As per test configuration |
| Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadURL | dummy_url.com (invalid, non-accessible URL) |
| Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareToDownload | As per test configuration (valid firmware filename) |
| Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadAndFactoryReset | 1 |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadProtocol; GET FirmwareDownloadURL; GET FirmwareToDownload; GET FirmwareDownloadAndFactoryReset</small> | <small>Validate all current firmware upgrade configuration values are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus</small> | <small>Validate initial FirmwareDownloadStatus is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET FirmwareDownloadProtocol; SET FirmwareDownloadURL to an invalid, non-accessible URL; SET FirmwareToDownload to a valid firmware filename; SET FirmwareDownloadAndFactoryReset to 1</small> | <small>Validate firmware upgrade parameters are set successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus</small> | <small>Validate FirmwareDownloadStatus remains "Not Started", confirming the DUT does not initiate firmware download when the configured URL is invalid. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Revert FirmwareDownloadProtocol, FirmwareDownloadURL, and FirmwareToDownload to original values (without triggering download)</small> | <small>Validate firmware upgrade configuration values are restored to original values successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 4: TS_FirmwareUpgrade_FWUpgradeUsingXCONFServer</strong></summary>

## Test Case 4: TS_FirmwareUpgrade_FWUpgradeUsingXCONFServer

## Objectives
This test validates firmware upgrade on the DUT using XCONF server-based configuration. Successful validation is confirmed when the DUT upgrades to the target firmware image and subsequently reverts to the original firmware.

## Test Case ID
TC_FirmwareUpgrade_4

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Broadband residential gateway (RDKB) |
| WAN System - HTTP server hosting firmware images |
| XCONF Server |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| XCONF Firmware Filename | As per test configuration |
| XCONF Firmware Location | As per test configuration |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Precondition: A Python HTTP server with target firmware image is running. XCONF Server is active and reachable. Target image should not be present in either bank of the DUT.</small> | <small>&nbsp;</small> |
| <small>2</small> | <small>Execute crontab command on DUT to disable the firmware upgrade cron job</small> | <small>Validate firmware upgrade cron job is disabled successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Execute ifconfig on the eRouter interface to obtain the eRouter IP address of the DUT</small> | <small>Validate eRouter IP address is obtained successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Execute `cat /version.txt` on DUT to read the current firmware image name</small> | <small>Validate current firmware version and filename are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute curl command to query availability of the target firmware image on the HTTP server</small> | <small>Validate HTTP server returns 200 OK for the target firmware and it is different from the current firmware. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Execute shell command on DUT to retrieve the DUT MAC address</small> | <small>Validate DUT MAC address is obtained successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Execute curl POST commands to configure XCONF server: add Supported Model, MAC List, Firmware Config (with target firmware details), MAC Rule, and Define Properties</small> | <small>Validate XCONF server responds with valid configuration for all POST requests. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Execute /usr/bin/fwupgrade binary on DUT to initiate firmware download</small> | <small>Validate firmware upgrade binary executes without errors. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>Read device log file on DUT and search for firmware upgrade initiation message</small> | <small>Validate "Firmware upgrade is in progress" message is found in device logs. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>Execute find command on DUT to check for presence of target firmware file in /mnt/bootpart; DUT completes firmware download and reboots</small> | <small>Validate target firmware file is found in /mnt/bootpart. If the condition is met CONTINUE, else FAIL</small> |
| <small>11</small> | <small>Execute `cat /version.txt` on DUT after firmware upgrade reboot</small> | <small>Validate current firmware version matches the target firmware version. If the condition is met CONTINUE, else FAIL</small> |
| <small>12</small> | <small>Execute `cat /version.txt` on DUT after firmware recovery reboot</small> | <small>Validate current firmware version matches the initial firmware version. If the condition is met CONTINUE, else FAIL</small> |
| <small>13</small> | <small>Execute curl DELETE commands to remove all XCONF server configuration rules: Define Properties, MAC Rule, Firmware Config, MAC List, and Supported Model</small> | <small>Validate all XCONF server configuration rules are deleted successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>14</small> | <small>Execute crontab command on DUT to re-enable the firmware upgrade cron job</small> | <small>Validate firmware upgrade cron job is re-enabled successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 5: TS_FirmwareUpgrade_InvalidImage_FWUpgradeUsingXCONFServer</strong></summary>

## Test Case 5: TS_FirmwareUpgrade_InvalidImage_FWUpgradeUsingXCONFServer

## Objectives
This test verifies that the DUT does not trigger a firmware download when an invalid firmware image name is configured in the XCONF server. Successful validation is confirmed when no firmware download is initiated and no firmware file appears in /mnt/bootpart.

## Test Case ID
TC_FirmwareUpgrade_5

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Broadband residential gateway (RDKB) |
| XCONF Server |
| WAN System - HTTP server hosting firmware images |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| XCONF Firmware Filename | dummy_version.bin.wic.bz2 (invalid, non-existent firmware) |
| XCONF Firmware Location | As per test configuration |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Precondition: A Python HTTP server with target firmware image is running. XCONF Server is active and reachable.</small> | <small>&nbsp;</small> |
| <small>2</small> | <small>Execute `cat /version.txt` on DUT to read the current firmware image name</small> | <small>Validate current firmware version and filename are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Execute shell command on DUT to retrieve the DUT MAC address</small> | <small>Validate DUT MAC address is obtained successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Execute curl POST commands to configure XCONF server with invalid firmware details: add Supported Model, MAC List, Firmware Config (with invalid firmware filename), MAC Rule, and Define Properties</small> | <small>Validate XCONF server responds with valid configuration for all POST requests. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute /usr/bin/fwupgrade binary on DUT to attempt firmware download</small> | <small>Validate firmware upgrade binary executes without command errors. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Read device log file on DUT and search for firmware upgrade initiation message</small> | <small>Validate "Firmware upgrade is in progress" message is NOT found in device logs. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Execute find command on DUT to check for presence of the invalid firmware file in /mnt/bootpart</small> | <small>Validate the invalid firmware file is NOT present in /mnt/bootpart. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Execute curl DELETE commands to remove all XCONF server configuration rules: Define Properties, MAC Rule, Firmware Config, MAC List, and Supported Model</small> | <small>Validate all XCONF server configuration rules are deleted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 6: TS_FirmwareUpgrade_InvalidURL_FWUpgradeUsingXCONFServer</strong></summary>

## Test Case 6: TS_FirmwareUpgrade_InvalidURL_FWUpgradeUsingXCONFServer

## Objectives
This test verifies that the DUT does not trigger a firmware download when an invalid firmware location URL is configured in the XCONF server. Successful validation is confirmed when no firmware download is initiated and no firmware file appears in /mnt/bootpart.

## Test Case ID
TC_FirmwareUpgrade_6

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Broadband residential gateway (RDKB) |
| XCONF Server |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| XCONF Firmware Filename | As per test configuration |
| XCONF Firmware Location | http://invalid_url/ (invalid, non-accessible URL) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Precondition: A Python HTTP server with target firmware image is running. XCONF Server is active and reachable.</small> | <small>&nbsp;</small> |
| <small>2</small> | <small>Execute `cat /version.txt` on DUT to read the current firmware image name</small> | <small>Validate current firmware version and filename are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Execute shell command on DUT to retrieve the DUT MAC address</small> | <small>Validate DUT MAC address is obtained successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Execute curl POST commands to configure XCONF server with valid firmware name but invalid firmware location URL (http://invalid_url/): add Supported Model, MAC List, Firmware Config, MAC Rule, and Define Properties</small> | <small>Validate XCONF server responds with valid configuration for all POST requests. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute /usr/bin/fwupgrade binary on DUT to attempt firmware download</small> | <small>Validate firmware upgrade binary executes without command errors. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Read device log file on DUT and search for firmware upgrade initiation message</small> | <small>Validate "Firmware upgrade is in progress" message is NOT found in device logs. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Execute find command on DUT to check for presence of the target firmware file in /mnt/bootpart</small> | <small>Validate the target firmware file is NOT present in /mnt/bootpart. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Execute curl DELETE commands to remove all XCONF server configuration rules: Define Properties, MAC Rule, Firmware Config, MAC List, and Supported Model</small> | <small>Validate all XCONF server configuration rules are deleted successfully. If the condition is met PASS, else FAIL</small> |

</details>

---

</details>

---

<details>
<summary><strong>Lan Manager Lite</strong></summary>

# Lan Manager Lite

<details>
<summary><strong>Test Case 1: Bridge mode reports ConnectedDeviceNumber as zero</strong></summary>

## Test Case 1: TS_LMLite_CheckConnectedDeviceNumber_InBridgeMode

## Objectives
Verify that when the gateway is in bridge mode, Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber is zero.

## Test Case ID
TC_LMLite_10

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode | bridge-static |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode.</small> | <small>Verify the current LAN mode is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to bridge-static.</small> | <small>Verify the device can be placed in bridge mode when required. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Wait for the LAN mode change to take effect.</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Get Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber.</small> | <small>Verify the device returns the current connected device count. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify the connected device count is 0 while the device is in bridge mode. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to original value.</small> | <small>Verify the LAN mode is reverted to the original value. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 2: Bridge mode reports HostNumberOfEntries as zero</strong></summary>

## Test Case 2: TS_LMLite_CheckHostNumberOfEntries_InBridgeMode

## Objectives
Verify that when the gateway is in bridge mode, Device.Hosts.HostNumberOfEntries is zero.

## Test Case ID
TC_LMLite_11

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode | bridge-static |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode.</small> | <small>Verify the current LAN mode is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to bridge-static.</small> | <small>Verify the device can be placed in bridge mode when required. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Wait for the LAN mode change to take effect.</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Get Device.Hosts.HostNumberOfEntries.</small> | <small>Verify the device returns the current host table entry count. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify the host table entry count is 0 while the device is in bridge mode. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to original value.</small> | <small>Verify the LAN mode is reverted to the original value. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 3: Active LAN client IP matches Device.Hosts value</strong></summary>

## Test Case 3: TS_LMLite_CheckLANClientIPAddress

## Objectives
Verify that the IP address of the active LAN client matches the IP address reported by the device.

## Test Case ID
TC_LMLite_08

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| None | None |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber.</small> | <small>Verify the connected device count is greater than 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Run the ARP command on the DUT to retrieve active LAN client IP addresses.</small> | <small>Verify the DUT returns the IPv4 address for active LAN clients. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Get Device.Hosts.HostNumberOfEntries.</small> | <small>Verify the host table entry count is greater than 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Get Device.Hosts.Host.{i}.Active for each host entry.</small> | <small>Verify at least one host entry is active. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Get Device.Hosts.Host.{i}.Layer1Interface for each active host entry.</small> | <small>Verify the active host entry corresponds to a LAN client. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Get Device.Hosts.Host.{i}.IPv4Address.1.IPAddress for each active LAN host entry.</small> | <small>Verify the host table returns the IPv4 address. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Verify the value reported by Device.Hosts.Host.{i}.IPv4Address.1.IPAddress matches the value collected from the DUT runtime view. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Verify the active host count matches Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 4: Active LAN client MAC matches Device.Hosts value</strong></summary>

## Test Case 4: TS_LMLite_CheckLANClientPhysAddress

## Objectives
Verify that the physical address of the active LAN client matches the MAC address reported by the device.

## Test Case ID
TC_LMLite_12

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| None | None |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber.</small> | <small>Verify the connected device count is greater than 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Run the ARP command on the DUT to retrieve active LAN client physical addresses.</small> | <small>Verify the DUT returns the physical address for active LAN clients. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Get Device.Hosts.HostNumberOfEntries.</small> | <small>Verify the host table entry count is greater than 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Get Device.Hosts.Host.{i}.Active for each host entry.</small> | <small>Verify at least one host entry is active. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Get Device.Hosts.Host.{i}.Layer1Interface for each active host entry.</small> | <small>Verify the active host entry corresponds to a LAN client. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Get Device.Hosts.Host.{i}.PhysAddress for each active LAN host entry.</small> | <small>Verify the host table returns the physical address. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Verify the value reported by Device.Hosts.Host.{i}.PhysAddress matches the value collected from the DUT runtime view. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Verify the active host count matches Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 5: Connected LAN clients are marked active</strong></summary>

## Test Case 5: TS_LMLite_CheckLANClientsActiveOrNot

## Objectives
Verify that if Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber is greater than zero, the connected clients are active.

## Test Case ID
TC_LMLite_09

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| None | None |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber.</small> | <small>Verify the connected device count is greater than 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get Device.Hosts.HostNumberOfEntries.</small> | <small>Verify the host table entry count is greater than 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Get Device.Hosts.Host.{i}.Active for each host entry.</small> | <small>Verify the host activity state is returned for each host entry. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Get Device.Hosts.Host.{i}.Layer1Interface for each active host entry.</small> | <small>Verify each active LAN host entry reports an Ethernet layer-1 interface. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify the number of active LAN host entries matches Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 6: Layer1Interface matches ARP-detected interface</strong></summary>

## Test Case 6: TS_LMLite_CheckLayer1Interface

## Objectives
Verify that Device.Hosts.Host.2.Layer1Interface matches the interface identified on the device using the arp command.

## Test Case ID
TC_LMLite_17

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| None | None |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber.</small> | <small>Verify the connected device count is greater than 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Run the ARP command on the DUT to retrieve active LAN client interface details.</small> | <small>Verify the DUT returns interface details for active LAN clients. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Get Device.Hosts.HostNumberOfEntries.</small> | <small>Verify the host table entry count is greater than 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Get Device.Hosts.Host.{i}.Active for each host entry.</small> | <small>Verify at least one host entry is active. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Get Device.Hosts.Host.{i}.Layer1Interface for each active host entry.</small> | <small>Verify each active LAN host entry reports an Ethernet layer-1 interface. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify the active host layer-1 interface matches the interface details collected from the DUT runtime view. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Verify the active host count matches Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 7: WAN MAC matches Host Parent value</strong></summary>

## Test Case 7: TS_LMLite_CheckWANMacAddress

## Objectives
Verify that the WAN MAC address matches the value of Device.Hosts.Host.1.X_RDKCENTRAL-COM_Parent.

## Test Case ID
TC_LMLite_13

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |
| WAN - WAN system |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| None | None |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber.</small> | <small>Verify the connected device count is greater than 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Run the DUT utility command to retrieve the WAN MAC address.</small> | <small>Verify the DUT returns a valid WAN MAC address. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Get Device.Hosts.HostNumberOfEntries.</small> | <small>Verify the host table entry count is greater than 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Get Device.Hosts.Host.{i}.Active for each host entry.</small> | <small>Verify at least one host entry is active. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Get Device.Hosts.Host.{i}.Layer1Interface for each active host entry.</small> | <small>Verify each active LAN host entry reports an Ethernet layer-1 interface. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Get Device.Hosts.Host.{i}.X_RDKCENTRAL-COM_Parent for each active host entry.</small> | <small>Verify the WAN parent identifier is returned for each active host entry. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Verify the WAN parent value for the active host entry matches the WAN MAC address returned by the DUT utility command. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Verify the active host count matches Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 8: Each active host reports one IPv4 entry</strong></summary>

## Test Case 8: TS_LMLite_GetIPv4AddressNumberOfEntries

## Objectives
Verify that Device.Hosts.Host.1.IPv4AddressNumberOfEntries is always 1 and should not be 0.

## Test Case ID
TC_LMLite_14

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| None | None |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber.</small> | <small>Verify the connected device count is greater than 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get Device.Hosts.HostNumberOfEntries.</small> | <small>Verify the host table entry count is greater than 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Get Device.Hosts.Host.{i}.Active for each host entry.</small> | <small>Verify at least one host entry is active. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Get Device.Hosts.Host.{i}.Layer1Interface for each active host entry.</small> | <small>Verify each active LAN host entry reports an Ethernet layer-1 interface. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Get Device.Hosts.Host.{i}.IPv4AddressNumberOfEntries for each active host entry.</small> | <small>Verify each active host entry reports exactly one IPv4 address entry. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify the active host count matches Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 9: LeaseTimeRemaining is valid for active hosts</strong></summary>

## Test Case 9: TS_LMLite_GetLeaseTimeRemaining

## Objectives
Verify that Device.Hosts.Host.1.LeaseTimeRemaining is greater than zero when Device.Hosts.Host.1.AddressSource is DHCP; otherwise, it should be zero.

## Test Case ID
TC_LMLite_16

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| None | None |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber.</small> | <small>Verify the connected device count is greater than 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get Device.Hosts.HostNumberOfEntries.</small> | <small>Verify the host table entry count is greater than 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Get Device.Hosts.Host.{i}.Active for each host entry.</small> | <small>Verify at least one host entry is active. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Get Device.Hosts.Host.{i}.Layer1Interface for each active host entry.</small> | <small>Verify each active LAN host entry reports an Ethernet layer-1 interface. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Get Device.Hosts.Host.{i}.AddressSource for each active host entry.</small> | <small>Verify the address source is returned for each active host entry. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Get Device.Hosts.Host.{i}.LeaseTimeRemaining for each active host entry.</small> | <small>Verify DHCP host entries report a lease time greater than 0 and non-DHCP host entries report 0. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Verify the active host count matches Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 10: Reject higher polling period when status is enabled</strong></summary>

## Test Case 10: TS_LMLite_NWDeviceStatus_Enabled_SetHigherPollingPeriod

## Objectives
Verify that when Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled is true, the new polling period is not greater than the current polling period.

## Test Case ID
TC_LMLite_03

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled | true |
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod | Runtime-derived next higher valid value |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod.</small> | <small>Verify the current PollingPeriod is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled.</small> | <small>Verify the enabled state is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled to true.</small> | <small>Verify the reporting feature is enabled when required. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod to a higher value.</small> | <small>Verify the DUT rejects a higher PollingPeriod than the current allowed value. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Revert Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled to original value.</small> | <small>Verify the enabled state is reverted to the original value. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 11: Reject higher reporting period when status is enabled</strong></summary>

## Test Case 11: TS_LMLite_NWDeviceStatus_Enabled_SetHigherReportingPeriod

## Objectives
Verify that when Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled is true, the new reporting period is not greater than the current reporting period.

## Test Case ID
TC_LMLite_04

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled | true |
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod | Runtime-derived next higher valid value |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod.</small> | <small>Verify the current ReportingPeriod is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled.</small> | <small>Verify the enabled state is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled to true.</small> | <small>Verify the reporting feature is enabled when required. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod to a higher value.</small> | <small>Verify the DUT rejects a higher ReportingPeriod than the current allowed value. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Revert Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled to original value.</small> | <small>Verify the enabled state is reverted to the original value. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 12: PollingPeriod reverts to default after OverrideTTL</strong></summary>

## Test Case 12: TS_LMLite_NWDeviceStatus_GetPollingPeriodAfterOverrideTTL

## Objectives
Verify that Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod resets to its default value after the OverrideTTL duration.

## Test Case ID
TC_LMLite_01

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled | false, then true |
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod | Runtime-derived different valid value |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod.</small> | <small>Verify the current reporting period is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Default.PollingPeriod.</small> | <small>Verify the default polling period is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Default.OverrideTTL.</small> | <small>Verify the override TTL is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled.</small> | <small>Verify the enabled state is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod.</small> | <small>Verify the current polling period is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled to false.</small> | <small>Verify the reporting feature can be disabled before modifying the polling period. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod to a different valid value.</small> | <small>Verify a different valid polling period can be configured while the feature is disabled. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled to true.</small> | <small>Verify the reporting feature is enabled again. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>Wait for the greater of the override TTL interval or the configured reporting interval to expire.</small> | <small>&nbsp;</small> |
| <small>11</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod.</small> | <small>Verify the polling period returns to its default value after the override TTL expires. If the condition is met CONTINUE, else FAIL.</small> |
| <small>12</small> | <small>Revert Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod to original value.</small> | <small>Verify the original polling period is restored. If the condition is met CONTINUE, else FAIL.</small> |
| <small>13</small> | <small>Revert Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled to original value.</small> | <small>Verify the original enabled state is restored. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 13: ReportingPeriod reverts to default after OverrideTTL</strong></summary>

## Test Case 13: TS_LMLite_NWDeviceStatus_GetReportingPeriodAfterOverrideTTL

## Objectives
Verify that Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod resets to its default value after the OverrideTTL duration.

## Test Case ID
TC_LMLite_02

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod | Runtime-derived lower valid value when required |
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod | Runtime-derived valid non-default value |
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled | true |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Default.ReportingPeriod.</small> | <small>Verify the default reporting period is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Default.OverrideTTL.</small> | <small>Verify the override TTL is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled.</small> | <small>Verify the enabled state is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod.</small> | <small>Verify the current reporting period is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>6</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod.</small> | <small>Verify the current polling period is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>7</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod to a lower valid value when required.</small> | <small>Verify the polling period is adjusted to a lower valid value when required. If the condition is met CONTINUE, else FAIL.</small> |
| <small>8</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod to a valid non-default value.</small> | <small>Verify a valid non-default reporting period can be configured. If the condition is met CONTINUE, else FAIL.</small> |
| <small>9</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled to true.</small> | <small>Verify the reporting feature is enabled. If the condition is met CONTINUE, else FAIL.</small> |
| <small>10</small> | <small>Wait for the greater of the override TTL interval or the configured reporting interval to expire.</small> | <small>&nbsp;</small> |
| <small>11</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod.</small> | <small>Verify the reporting period returns to its default value after the override TTL expires. If the condition is met CONTINUE, else FAIL.</small> |
| <small>12</small> | <small>Revert Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod to original value.</small> | <small>Verify the original reporting period is restored. If the condition is met CONTINUE, else FAIL.</small> |
| <small>13</small> | <small>Revert Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod to original value.</small> | <small>Verify the original polling period is restored. If the condition is met CONTINUE, else FAIL.</small> |
| <small>14</small> | <small>Revert Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled to original value.</small> | <small>Verify the original enabled state is restored. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 14: Reject invalid NetworkDevicesStatus polling period</strong></summary>

## Test Case 14: TS_LMLite_NWDeviceStatus_SetInvalidDevicesStatusPollingPeriod

## Objectives
Verify that NetworkDevicesStatus.PollingPeriod accepts only valid values [5, 10, 15, 30, 60, 300, 900, 1800, 3600, 10800, 21600, 43200, 86400], and confirm that setting an invalid value is rejected.

## Test Case ID
TC_LMLite_06

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod | 100 |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod.</small> | <small>Verify the current PollingPeriod is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod to 100 (invalid).</small> | <small>Verify the DUT rejects the invalid PollingPeriod. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Revert Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod to original value.</small> | <small>Verify the original PollingPeriod is restored. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 15: Reject invalid NetworkDevicesStatus reporting period</strong></summary>

## Test Case 15: TS_LMLite_NWDeviceStatus_SetInvalidDevicesStatusReportingPeriod

## Objectives
Verify that NetworkDevicesStatus.ReportingPeriod accepts only valid values [5, 10, 15, 30, 60, 300, 900, 1800, 3600, 10800, 21600, 43200, 86400], and confirm that setting an invalid value is rejected.

## Test Case ID
TC_LMLite_07

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod | 100 |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod.</small> | <small>Verify the current ReportingPeriod is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod to 100 (invalid).</small> | <small>Verify the DUT rejects the invalid ReportingPeriod. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Revert Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod to original value.</small> | <small>Verify the original ReportingPeriod is restored. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 16: Reject reporting period lower than polling period</strong></summary>

## Test Case 16: TS_LMLite_NWDeviceStatus_SetReportingPeriodLessThanPollingPeriod

## Objectives
Verify that the new reporting period is not less than the current polling period.

## Test Case ID
TC_LMLite_05

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod | Runtime-derived lower-than-polling value |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod.</small> | <small>Verify the current reporting period is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.PollingPeriod.</small> | <small>Verify the current polling period is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod to a value lower than the polling period.</small> | <small>Verify the DUT rejects a reporting period that is lower than the polling period. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Revert Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod to original value.</small> | <small>Verify the original reporting period is restored. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 17: Reject invalid NetworkDevicesTraffic polling period</strong></summary>

## Test Case 17: TS_LMLite_NWDevicesTraffic_SetInvalidPollingPeriod

## Objectives
Verify that NetworkDevicesTraffic.PollingPeriod accepts only valid values [30, 60, 300, 900, 1800, 3600, 10800, 21600, 43200, 86400], and confirm that setting an invalid value is rejected.

## Test Case ID
TC_LMLite_18

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.PollingPeriod | 100 |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.PollingPeriod.</small> | <small>Verify the current PollingPeriod is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.PollingPeriod to 100 (invalid).</small> | <small>Verify the DUT rejects the invalid PollingPeriod. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Revert Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.PollingPeriod to original value.</small> | <small>Verify the original PollingPeriod is restored. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 18: Reject invalid NetworkDevicesTraffic reporting period</strong></summary>

## Test Case 18: TS_LMLite_NWDevicesTraffic_SetInvalidReportingPeriod

## Objectives
Verify that NetworkDevicesTraffic.ReportingPeriod accepts only valid values [30, 60, 300, 900, 1800, 3600, 10800, 21600, 43200, 86400], and confirm that setting an invalid value is rejected.

## Test Case ID
TC_LMLite_19

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.ReportingPeriod | 100 |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.ReportingPeriod.</small> | <small>Verify the current ReportingPeriod is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.ReportingPeriod to 100 (invalid).</small> | <small>Verify the DUT rejects the invalid ReportingPeriod. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Revert Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.ReportingPeriod to original value.</small> | <small>Verify the original ReportingPeriod is restored. If the condition is met PASS, else FAIL.</small> |

</details>

---

<details>
<summary><strong>Test Case 19: Reject traffic reporting period lower than polling period</strong></summary>

## Test Case 19: TS_LMLite_NWDevicesTraffic_SetReportingPeriodLessThanPollingPeriod

## Objectives
Verify that the new reporting period is not less than the current polling period.

## Test Case ID
TC_LMLite_20

## Test Type
Negative

## Test Environment
| Component |
|-----------|
| DUT - Device under test |
| LAN Client - Wired client |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.ReportingPeriod | Runtime-derived lower-than-polling value |

## Test Procedure and Expected Results
| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>Connect a LAN client to the DUT and ensure the client remains active throughout the test.</small> | <small>Verify the LAN client prerequisite is satisfied before executing the test. If the condition is met CONTINUE, else FAIL.</small> |
| <small>2</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.ReportingPeriod.</small> | <small>Verify the current reporting period is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>3</small> | <small>Get Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.PollingPeriod.</small> | <small>Verify the current polling period is returned. If the condition is met CONTINUE, else FAIL.</small> |
| <small>4</small> | <small>Set Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.ReportingPeriod to a value lower than the polling period.</small> | <small>Verify the DUT rejects a reporting period that is lower than the polling period. If the condition is met CONTINUE, else FAIL.</small> |
| <small>5</small> | <small>Revert Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.ReportingPeriod to original value.</small> | <small>Verify the original reporting period is restored. If the condition is met PASS, else FAIL.</small> |

</details>

---

</details>

---

<details>
<summary><strong>Test And Diagnostics</strong></summary>

# Test And Diagnostics

<details>
<summary><strong>Test Case 1: Verify DownloadDiagnostics DiagnosticsState is a valid TR-181 state</strong></summary>

## Test Case 1: TS_TAD_GetDownloadDiagnosticsState

## Objectives
To verify that Device.IP.Diagnostics.DownloadDiagnostics.DiagnosticsState can be retrieved and returns a valid TR-181 state value.

## Test Case ID
TC_TAD_01

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
| <small>1</small> | <small>GET Device.IP.Diagnostics.DownloadDiagnostics.DiagnosticsState</small> | <small>Verify the GET operation returns successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Verify the retrieved DiagnosticsState value is a valid TR-181 state (None, Requested, Completed, Error_CannotResolveHostName, Error_NoRouteToHost, Error_InitConnectionFailed, Error_NoResponse, Error_TransferFailed, Error_PasswordRequestFailed, Error_LoginFailed, Error_NoTransferMode, Error_NoPASV, Error_IncorrectSize, Error_Timeout, Error_Internal, or Error_Other). If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 2: Verify IPPing DiagnosticsState is a valid TR-181 state</strong></summary>

## Test Case 2: TS_TAD_GetIPPingDiagnosticsState

## Objectives
To verify that Device.IP.Diagnostics.IPPing.DiagnosticsState can be retrieved and returns a valid TR-181 state value.

## Test Case ID
TC_TAD_02

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
| <small>1</small> | <small>GET Device.IP.Diagnostics.IPPing.DiagnosticsState</small> | <small>Verify the GET operation returns successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Verify the retrieved DiagnosticsState value is a valid TR-181 state (None, Requested, Complete, Error_CannotResolveHostName, Error_NoRouteToHost, Error_MaxHopCountExceeded, or Error_Other). If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 3: Verify TraceRoute DiagnosticsState is a valid TR-181 state</strong></summary>

## Test Case 3: TS_TAD_GetTraceRouteDiagnosticsState

## Objectives
To verify that Device.IP.Diagnostics.TraceRoute.DiagnosticsState can be retrieved and returns a valid TR-181 state value.

## Test Case ID
TC_TAD_04

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
| <small>1</small> | <small>GET Device.IP.Diagnostics.TraceRoute.DiagnosticsState</small> | <small>Verify the GET operation returns successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Verify the retrieved DiagnosticsState value is a valid TR-181 state (None, Requested, Complete, Error_CannotResolveHostName, Error_NoRouteToHost, Error_MaxHopCountExceeded, or Error_Other). If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 4: Verify UploadDiagnostics DiagnosticsState is a valid TR-181 state</strong></summary>

## Test Case 4: TS_TAD_GetUploadDiagnosticsState

## Objectives
To verify that Device.IP.Diagnostics.UploadDiagnostics.DiagnosticsState can be retrieved and returns a valid TR-181 state value.

## Test Case ID
TC_TAD_05

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
| <small>1</small> | <small>GET Device.IP.Diagnostics.UploadDiagnostics.DiagnosticsState</small> | <small>Verify the GET operation returns successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Verify the retrieved DiagnosticsState value is a valid TR-181 state (None, Requested, Completed, Error_CannotResolveHostName, Error_NoRouteToHost, Error_NoTransferMode, Error_NoPASV, Error_IncorrectSize, Error_Timeout, Error_Internal, or Error_Other). If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 5: Verify IPPing average response time is greater than zero after a successful ping</strong></summary>

## Test Case 5: TS_TAD_IPPing_CheckAvgResponseTime

## Objectives
To check if the average response time is greater than zero after a successful ping test.

## Test Case ID
TC_TAD_21

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Interface | Interface_erouter0 |
| Device.IP.Diagnostics.IPPing.Host | As per test configuration |
| Device.IP.Diagnostics.IPPing.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.Interface to Interface_erouter0</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.IPPing.DiagnosticsState to Requested to trigger the IP ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the ping test to complete</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.IP.Diagnostics.IPPing.AverageResponseTime</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.IPPing.AverageResponseTime is greater than zero. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 6: Verify IPPing success count is greater than zero after a successful ping</strong></summary>

## Test Case 6: TS_TAD_IPPing_CheckSuccessCount

## Objectives
To check if the success count is greater than zero after a successful IPPing test.

## Test Case ID
TC_TAD_22

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Interface | Interface_erouter0 |
| Device.IP.Diagnostics.IPPing.Host | As per test configuration |
| Device.IP.Diagnostics.IPPing.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.Interface to Interface_erouter0</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.IPPing.DiagnosticsState to Requested to trigger the IP ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the ping test to complete</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.IP.Diagnostics.IPPing.SuccessCount</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.IPPing.SuccessCount is greater than zero. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 7: Verify IPPing DiagnosticsState cannot be set to an invalid value</strong></summary>

## Test Case 7: TS_TAD_IPPing_SetInvalidDiagnosticsState

## Objectives
To check if DiagnosticsState of IPPing can be set with an invalid value. Requested and Canceled are the only writable values.

## Test Case ID
TC_TAD_23

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
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.DiagnosticsState to Completed (an invalid writable value; only Requested and Canceled are valid writable values)</small> | <small>Verify the SET operation returns FAILURE, confirming Completed cannot be set directly. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 8: Verify CPE uses routing policy when IPPing interface is set to an invalid value</strong></summary>

## Test Case 8: TS_TAD_IPPing_SetInvalidInterface

## Objectives
To set the invalid interface name and check whether the CPE uses the interface as directed by its bridging or routing policy.

## Test Case ID
TC_TAD_24

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Interface | (empty string â€“ invalid interface) |
| Device.IP.Diagnostics.IPPing.Host | As per test configuration |
| Device.IP.Diagnostics.IPPing.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.Interface to an empty string (invalid interface)</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.IPPing.DiagnosticsState to Requested to trigger the IP ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the ping test to complete</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.IP.Diagnostics.IPPing.SuccessCount</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.IPPing.SuccessCount is greater than zero, confirming the CPE uses its routing policy when an invalid interface is provided. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 9: Verify IPPing DiagnosticsState error when no host name is set</strong></summary>

## Test Case 9: TS_TAD_IPPing_SetNoHostName

## Objectives
To set all IPPing parameters except host name and check whether the error thrown is either Error_Other or Error_CannotResolveHostName.

## Test Case ID
TC_TAD_25

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Interface | Interface_erouter0 |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.Interface to Interface_erouter0</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to an empty string (no host name)</small> | <small>Verify the SET operation returns FAILURE, confirming an empty host name is rejected. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.IPPing.DiagnosticsState to Requested to trigger the IP ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the ping test to complete</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.IP.Diagnostics.IPPing.DiagnosticsState</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.IPPing.DiagnosticsState is either Error_CannotResolveHostName or Error_Other. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 10: Verify IPPing DiagnosticsState changes to error value when invalid host is set</strong></summary>

## Test Case 10: TS_TAD_IPPing_CheckDiagnosticsState_ForInvalidHostName

## Objectives
To set an invalid host name for IPPing and verify that the diagnostic state changes to an error value.

## Test Case ID
TC_TAD_26

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Host | (invalid host name) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to an invalid host name</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.IP.Diagnostics.IPPing.DiagnosticsState</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.IPPing.DiagnosticsState is set to an error value (e.g., Error_CannotResolveHostName or Error_Other). If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 11: Verify IPPing average response time is zero when invalid host name is set</strong></summary>

## Test Case 11: TS_TAD_IPPing_CheckAvgResponseTime_ForInvalidHostName

## Objectives
To check if the average response time is equal to zero when the IP ping test is triggered with an invalid host name.

## Test Case ID
TC_TAD_27

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Host | (empty string) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to an empty string</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.IP.Diagnostics.IPPing.AverageResponseTime</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.IPPing.AverageResponseTime is equal to zero. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 12: Verify IPPing DiagnosticsState after a successful ping</strong></summary>

## Test Case 12: TS_TAD_IPPing_GetDiagnosticsState

## Objectives
To set all IPPing parameters and get the IPPing diagnostic state after a successful ping.

## Test Case ID
TC_TAD_28

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Interface | Interface_erouter0 |
| Device.IP.Diagnostics.IPPing.Host | As per test configuration |
| Device.IP.Diagnostics.IPPing.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.Interface to Interface_erouter0</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.IPPing.DiagnosticsState to Requested to trigger the IP ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the ping test to complete</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.IP.Diagnostics.IPPing.DiagnosticsState</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.IPPing.DiagnosticsState is Complete after a successful ping. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 13: Verify IPPing DiagnosticsState clears to None after modifying a writable parameter</strong></summary>

## Test Case 13: TS_TAD_IPPing_ClearDiagnosticsState

## Objectives
To set all IPPing parameters to do a ping test and check whether the IPPing diagnostic state changes to None after changing any of the writable parameters.

## Test Case ID
TC_TAD_29

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Interface | Interface_erouter0 |
| Device.IP.Diagnostics.IPPing.Host | As per test configuration |
| Device.IP.Diagnostics.IPPing.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.Interface to Interface_erouter0</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.IPPing.DiagnosticsState to Requested to trigger the IP ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the ping test to complete</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to a different value to modify a writable parameter</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.IP.Diagnostics.IPPing.DiagnosticsState</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.IPPing.DiagnosticsState has been cleared to None after changing a writable parameter. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 14: Verify IPPing SuccessCount clears to zero after modifying a writable parameter</strong></summary>

## Test Case 14: TS_TAD_IPPing_ClearSuccessCount

## Objectives
To set all IPPing parameters to do a ping test and check whether the IPPing success count gets cleared after changing any of the writable parameters.

## Test Case ID
TC_TAD_30

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Interface | Interface_erouter0 |
| Device.IP.Diagnostics.IPPing.Host | As per test configuration |
| Device.IP.Diagnostics.IPPing.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.Interface to Interface_erouter0</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.IPPing.DiagnosticsState to Requested to trigger the IP ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the ping test to complete</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to a different value to modify a writable parameter</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.IP.Diagnostics.IPPing.SuccessCount</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.IPPing.SuccessCount has been cleared to zero after changing a writable parameter. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 15: Verify IPPing DiagnosticsState resets to None after reboot</strong></summary>

## Test Case 15: TS_TAD_IPPing_CheckDiagnosticsStateAfterReboot

## Objectives
To check if after a reboot the result parameters from the most recent test are not retained and the DiagnosticsState is set to None.

## Test Case ID
TC_TAD_31

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Interface | Interface_erouter0 |
| Device.IP.Diagnostics.IPPing.Host | As per test configuration |
| Device.IP.Diagnostics.IPPing.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.Interface to Interface_erouter0</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.IPPing.DiagnosticsState to Requested to trigger the IP ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Reboot the DUT</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>After reboot, GET Device.IP.Diagnostics.IPPing.DiagnosticsState</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.IPPing.DiagnosticsState is None after reboot. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 16: Verify no DIAGNOSTICS COMPLETE log in TR069 when IPPing is triggered</strong></summary>

## Test Case 16: TS_TAD_IPPing_CheckTR069Logs

## Objectives
To ensure no DIAGNOSTICS COMPLETE logs are in TR069.log when the IP Ping is triggered using namespaces.

## Test Case ID
TC_TAD_77

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable | true |
| Device.IP.Diagnostics.IPPing.Interface | Interface_erouter0 |
| Device.IP.Diagnostics.IPPing.Host | As per test configuration |
| Device.IP.Diagnostics.IPPing.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If TR069support.Enable is false, SET it to true</small> | <small>Verify the SET operation is successful if performed. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Verify the TR069 log file /rdklogs/logs/TR69log.txt.0 is present on the DUT</small> | <small>Verify the file exists. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>SET Device.IP.Diagnostics.IPPing.Interface to Interface_erouter0</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>SET Device.IP.Diagnostics.IPPing.DiagnosticsState to Requested to trigger the IP ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait for the ping test to complete</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>Read /rdklogs/logs/TR69log.txt.0 and check for "CwmpEvent->EventCode = 8 DIAGNOSTICS COMPLETE"</small> | <small>Verify the string is NOT present in the TR069 log file. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Revert TR069support.Enable to original value if changed</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 17: Verify all TraceRoute parameters can be set and the test runs successfully</strong></summary>

## Test Case 17: TS_TAD_SetTraceRoute

## Objectives
To set all TraceRoute parameters and verify whether the operation succeeds.

## Test Case ID
TC_TAD_06

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.TraceRoute.Interface | Interface_erouter0 |
| Device.IP.Diagnostics.TraceRoute.Host | As per test configuration |
| Device.IP.Diagnostics.TraceRoute.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.TraceRoute.Interface to Interface_erouter0</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.TraceRoute.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.TraceRoute.DiagnosticsState to Requested to trigger the trace route test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the trace route test to complete</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.IP.Diagnostics.TraceRoute.RouteHopsNumberOfEntries</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.TraceRoute.RouteHopsNumberOfEntries is greater than zero. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 18: Verify TraceRoute average response time is greater than zero after a successful test</strong></summary>

## Test Case 18: TS_TAD_TraceRoute_CheckAvgResponseTime

## Objectives
To check if the average response time is greater than zero after a successful trace route test.

## Test Case ID
TC_TAD_07

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.TraceRoute.Interface | Interface_erouter0 |
| Device.IP.Diagnostics.TraceRoute.Host | As per test configuration |
| Device.IP.Diagnostics.TraceRoute.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.TraceRoute.Interface to Interface_erouter0</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.TraceRoute.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.TraceRoute.DiagnosticsState to Requested to trigger the trace route test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the trace route test to complete</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.IP.Diagnostics.TraceRoute.RouteHops.{i}.RTimes for the first hop</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify the average response time from RouteHops.{i}.RTimes is greater than zero. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 19: Verify TraceRoute average response time is zero when invalid host name is set</strong></summary>

## Test Case 19: TS_TAD_TraceRoute_CheckAvgResponseTime_ForInvalidHostName

## Objectives
To check if the average response time is equal to zero when the trace route test is triggered with an invalid host name.

## Test Case ID
TC_TAD_08

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.TraceRoute.Host | (empty string) |
| Device.IP.Diagnostics.TraceRoute.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.TraceRoute.Host to an empty string</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.TraceRoute.DiagnosticsState to Requested to trigger the trace route test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Wait for the trace route test to complete</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>GET Device.IP.Diagnostics.TraceRoute.RouteHops.{i}.RTimes for the first hop</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify the average response time is equal to zero when triggered with an invalid host name. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 20: Verify TraceRoute round-trip times list contains no more than three items</strong></summary>

## Test Case 20: TS_TAD_TraceRoute_CheckRoundTripTimes

## Objectives
To get the round-trip time in milliseconds for each hop and verify that the list contains no more than three items.

## Test Case ID
TC_TAD_09

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.TraceRoute.Interface | Interface_erouter0 |
| Device.IP.Diagnostics.TraceRoute.Host | As per test configuration |
| Device.IP.Diagnostics.TraceRoute.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.TraceRoute.Interface to Interface_erouter0</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.TraceRoute.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.TraceRoute.DiagnosticsState to Requested to trigger the trace route test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the trace route test to complete</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.IP.Diagnostics.TraceRoute.RouteHops.{i}.RTimes for a hop entry</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify the RTimes list for the hop contains no more than three items. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 21: Verify previous TraceRoute result is cleared when parameters are set again</strong></summary>

## Test Case 21: TS_TAD_TraceRoute_ClearResult

## Objectives
Set all parameters and check if the result is obtained successfully. Then set all the parameters again and check if the previous result is cleared.

## Test Case ID
TC_TAD_10

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.TraceRoute.Interface | Interface_erouter0 |
| Device.IP.Diagnostics.TraceRoute.Host | As per test configuration |
| Device.IP.Diagnostics.TraceRoute.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.TraceRoute.Interface, Host, and DiagnosticsState to trigger the trace route test</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Wait for the trace route test to complete</small> | <small>&nbsp;</small> |
| <small>3</small> | <small>GET Device.IP.Diagnostics.TraceRoute.RouteHopsNumberOfEntries</small> | <small>Verify RouteHopsNumberOfEntries is greater than zero. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>SET Interface, Host, and DiagnosticsState again to trigger a second trace route test</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Wait for the second trace route test to complete</small> | <small>&nbsp;</small> |
| <small>6</small> | <small>GET Device.IP.Diagnostics.TraceRoute.RouteHopsNumberOfEntries</small> | <small>Verify RouteHopsNumberOfEntries reflects only the result of the latest run and the previous result has been cleared. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 22: Verify TraceRoute reports error when max hop count is exceeded</strong></summary>

## Test Case 22: TS_TAD_TraceRoute_ExceedMaxHopCount

## Objectives
To set the maximum hop count to 1 and verify the TraceRoute behavior for a destination that requires more than one hop.

## Test Case ID
TC_TAD_11

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.TraceRoute.MaxHopCount | 1 |
| Device.IP.Diagnostics.TraceRoute.Host | As per test configuration |
| Device.IP.Diagnostics.TraceRoute.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.TraceRoute.MaxHopCount to 1</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.TraceRoute.Host to a destination that requires more than one hop</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.TraceRoute.DiagnosticsState to Requested to trigger the trace route test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the trace route test to complete</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.IP.Diagnostics.TraceRoute.DiagnosticsState</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.TraceRoute.DiagnosticsState is Error_MaxHopCountExceeded. If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>Revert Device.IP.Diagnostics.TraceRoute.MaxHopCount to original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 23: Verify TraceRoute DiagnosticsState cannot be set to an invalid value</strong></summary>

## Test Case 23: TS_TAD_TraceRoute_SetInvalidDiagnosticsState

## Objectives
To check whether the DiagnosticsState of TraceRoute can be set to an invalid value.

## Test Case ID
TC_TAD_12

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.TraceRoute.DiagnosticsState | Completed (invalid) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.TraceRoute.DiagnosticsState to Completed (an invalid writable value; only Requested and Canceled are valid writable values)</small> | <small>Verify the SET operation returns FAILURE, confirming Completed cannot be set directly. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 24: Verify CPE uses routing policy when TraceRoute interface is set to an invalid value</strong></summary>

## Test Case 24: TS_TAD_TraceRoute_SetInvalidInterface

## Objectives
To set invalid interface in TraceRoute and check whether the CPE uses its routing policy to determine the appropriate interface.

## Test Case ID
TC_TAD_13

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.TraceRoute.Interface | (invalid interface name) |
| Device.IP.Diagnostics.TraceRoute.Host | As per test configuration |
| Device.IP.Diagnostics.TraceRoute.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.TraceRoute.Interface to an invalid interface name</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.TraceRoute.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.TraceRoute.DiagnosticsState to Requested to trigger the trace route test</small> | <small>Verify the SET operation is successful, confirming the CPE uses its routing policy when an invalid interface is provided. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 25: Verify TraceRoute NumberOfTries cannot be set to an invalid value</strong></summary>

## Test Case 25: TS_TAD_TraceRoute_SetInvalidNumberOfTries

## Objectives
To set an invalid value for the trace route number of tries and verify that the parameter update fails.

## Test Case ID
TC_TAD_14

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.TraceRoute.NumberOfTries | 4 (an invalid value) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.TraceRoute.NumberOfTries to 4 (only 1, 2, and 3 are valid values)</small> | <small>Verify the SET operation returns FAILURE. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 26: Verify TraceRoute reports error when triggered with no host name</strong></summary>

## Test Case 26: TS_TAD_TraceRoute_SetNoHostName

## Objectives
To set all trace route parameters except host name and check whether TraceRoute returns Error_MaxHopCountExceeded or Error_CannotResolveHostName.

## Test Case ID
TC_TAD_15

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.TraceRoute.Host | (empty string) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.TraceRoute.Host to an empty string</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.TraceRoute.DiagnosticsState to Requested to trigger the trace route test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Wait for the trace route test to complete</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>GET Device.IP.Diagnostics.TraceRoute.DiagnosticsState</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.TraceRoute.DiagnosticsState is either Error_MaxHopCountExceeded or Error_CannotResolveHostName. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 27: Verify no DIAGNOSTICS COMPLETE log in TR069 when TraceRoute is triggered</strong></summary>

## Test Case 27: TS_TAD_TraceRoute_CheckTR069Logs

## Objectives
To ensure no DIAGNOSTICS COMPLETE logs are in TR069.log when the TraceRoute is triggered using namespaces.

## Test Case ID
TC_TAD_78

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable | true |
| Device.IP.Diagnostics.TraceRoute.Interface | Interface_erouter0 |
| Device.IP.Diagnostics.TraceRoute.Host | As per test configuration |
| Device.IP.Diagnostics.TraceRoute.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If TR069support.Enable is false, SET it to true</small> | <small>Verify the SET operation is successful if performed. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Verify the TR069 log file /rdklogs/logs/TR69log.txt.0 is present on the DUT</small> | <small>Verify the file exists. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>SET Device.IP.Diagnostics.TraceRoute.Interface to Interface_erouter0</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>SET Device.IP.Diagnostics.TraceRoute.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>SET Device.IP.Diagnostics.TraceRoute.DiagnosticsState to Requested to trigger the trace route test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait for the trace route test to complete</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>Read /rdklogs/logs/TR69log.txt.0 and check for "CwmpEvent->EventCode = 8 DIAGNOSTICS COMPLETE"</small> | <small>Verify the string is NOT present in the TR069 log file. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Revert TR069support.Enable to original value if changed</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 28: Verify NSLookup result parameters are cleared after modifying a writable parameter</strong></summary>

## Test Case 28: TS_TAD_NSLookup_ClearResult

## Objectives
To check whether after a successful NSLookup, setting any writable parameter clears the result parameter.

## Test Case ID
TC_TAD_36

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DNS.Diagnostics.NSLookupDiagnostics.Interface | As per test configuration |
| Device.DNS.Diagnostics.NSLookupDiagnostics.HostName | As per test configuration |
| Device.DNS.Diagnostics.NSLookupDiagnostics.DNSServer | As per test configuration |
| Device.DNS.Diagnostics.NSLookupDiagnostics.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.IP.Interface.{i}.IPv4Address.{i}.IPAddress to determine the interface namespace</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.DNS.Diagnostics.NSLookupDiagnostics.Interface to the obtained interface namespace</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET NSLookupDiagnostics.HostName to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.DNS.Diagnostics.NSLookupDiagnostics.DNSServer and save the original value; SET DNSServer to the configured value</small> | <small>Verify GET and SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>SET NSLookupDiagnostics.DiagnosticsState to Requested to trigger the test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET ResultNumberOfEntries and SuccessCount</small> | <small>Verify both are greater than zero. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>SET NSLookupDiagnostics.HostName to a different value to modify a writable parameter</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>GET Device.DNS.Diagnostics.NSLookupDiagnostics.ResultNumberOfEntries</small> | <small>Verify ResultNumberOfEntries is cleared to zero after changing a writable parameter. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Revert Device.DNS.Diagnostics.NSLookupDiagnostics.DNSServer to original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 29: Verify NSLookup ResultNumberOfEntries equals NumberOfRepetitions after a successful test</strong></summary>

## Test Case 29: TS_TAD_NSLookup_CompareNumberOfRepetitionsandEntries

## Objectives
To check if the ResultNumberOfEntries and NumberOfRepetitions of NSLookup are equal and success count is greater than zero after a successful test.

## Test Case ID
TC_TAD_37

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DNS.Diagnostics.NSLookupDiagnostics.Interface | As per test configuration |
| Device.DNS.Diagnostics.NSLookupDiagnostics.HostName | As per test configuration |
| Device.DNS.Diagnostics.NSLookupDiagnostics.DNSServer | As per test configuration |
| Device.DNS.Diagnostics.NSLookupDiagnostics.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.IP.Interface.{i}.IPv4Address.{i}.IPAddress to determine the interface namespace</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET NSLookupDiagnostics.Interface, HostName, and DNSServer; trigger the test by setting DiagnosticsState to Requested</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.DNS.Diagnostics.NSLookupDiagnostics.ResultNumberOfEntries and NumberOfRepetitions</small> | <small>Verify both values are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Verify ResultNumberOfEntries equals NumberOfRepetitions and SuccessCount is greater than zero. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>Revert Device.DNS.Diagnostics.NSLookupDiagnostics.DNSServer to original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 30: Verify NSLookup succeeds when Interface is not set (CPE uses routing policy)</strong></summary>

## Test Case 30: TS_TAD_NSLookup_SetNoInterface

## Objectives
To set interface in NSLookup as empty and check whether the CPE uses its routing policy to determine the appropriate interface.

## Test Case ID
TC_TAD_38

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.DNS.Diagnostics.NSLookupDiagnostics.HostName | As per test configuration |
| Device.DNS.Diagnostics.NSLookupDiagnostics.DNSServer | As per test configuration |
| Device.DNS.Diagnostics.NSLookupDiagnostics.DiagnosticsState | Requested |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET NSLookupDiagnostics.DNSServer and save the original value; SET DNSServer to the configured value</small> | <small>Verify GET and SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET NSLookupDiagnostics.HostName to the configured host value (without setting Interface)</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET NSLookupDiagnostics.DiagnosticsState to Requested to trigger the NSLookup test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the NSLookup test to complete</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.DNS.Diagnostics.NSLookupDiagnostics.SuccessCount</small> | <small>Verify SuccessCount is greater than zero, confirming the CPE uses its routing policy when Interface is not set. If the condition is met PASS, else FAIL</small> |
| <small>6</small> | <small>Revert Device.DNS.Diagnostics.NSLookupDiagnostics.DNSServer to original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 31: Verify all UDPEcho result details are updated after a successful test</strong></summary>

## Test Case 31: TS_TAD_UDPEchoConfig_CheckIfSuccess

## Objectives
To check whether all result details are updated after a successful UDPEcho test.

## Test Case ID
TC_TAD_41

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.UDPEchoConfig.Interface | (empty string) |
| Device.IP.Diagnostics.UDPEchoConfig.SourceIPAddress | DUT IP address |
| Device.IP.Diagnostics.UDPEchoConfig.UDPPort | 7 |
| Device.IP.Diagnostics.UDPEchoConfig.Enable | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.UDPEchoConfig.Interface to empty string</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.UDPEchoConfig.SourceIPAddress to the DUT IP address</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.UDPEchoConfig.UDPPort to 7</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>SET Device.IP.Diagnostics.UDPEchoConfig.Enable to true</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Send a valid UDP echo request from the source IP address to the DUT UDP port 7</small> | <small>Verify the UDP request was sent successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.IP.Diagnostics.UDPEchoConfig.BytesReceived</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.UDPEchoConfig.BytesReceived is greater than zero. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 32: Verify UDPEcho fails when an invalid port number is configured</strong></summary>

## Test Case 32: TS_TAD_UDPEchoConfig_InvalidPort

## Objectives
To check if UDPEcho is failing with an invalid port number.

## Test Case ID
TC_TAD_42

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.UDPEchoConfig.UDPPort | (invalid port number) |
| Device.IP.Diagnostics.UDPEchoConfig.Enable | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.UDPEchoConfig.SourceIPAddress to the DUT IP address</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.UDPEchoConfig.UDPPort to an invalid port number</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.UDPEchoConfig.Enable to true</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Send a UDP echo request to the DUT</small> | <small>Verify the UDP request was sent. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.IP.Diagnostics.UDPEchoConfig.BytesReceived</small> | <small>Verify BytesReceived is zero, confirming no packets are received when an invalid port number is configured. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 33: Verify UDPEchoConfig returns error when invalid interface is set</strong></summary>

## Test Case 33: TS_TAD_UDPEchoConfig_InvalidInterface

## Objectives
To check if setting an invalid interface in UDPEchoConfig throws an "invalid parameter" error.

## Test Case ID
TC_TAD_43

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.UDPEchoConfig.Interface | (invalid interface name) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.UDPEchoConfig.Interface to an invalid interface name</small> | <small>Verify the SET operation returns an error (invalid parameter). If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 34: Verify UDPEcho result details are cleared after disable and re-enable</strong></summary>

## Test Case 34: TS_TAD_UDPEchoConfig_ClearResult

## Objectives
To check if the result details are getting cleared when UDPEchoConfig is enabled after being disabled.

## Test Case ID
TC_TAD_44

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.UDPEchoConfig.Interface | (empty string) |
| Device.IP.Diagnostics.UDPEchoConfig.SourceIPAddress | DUT IP address |
| Device.IP.Diagnostics.UDPEchoConfig.UDPPort | 7 |
| Device.IP.Diagnostics.UDPEchoConfig.Enable | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Interface to empty string, SourceIPAddress to DUT IP, UDPPort to 7, and Enable to true</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Send a valid UDP echo request from the source IP address to the DUT UDP port 7</small> | <small>Verify the UDP request was sent successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.IP.Diagnostics.UDPEchoConfig.BytesReceived</small> | <small>Verify BytesReceived is greater than zero. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>SET Device.IP.Diagnostics.UDPEchoConfig.Enable to false, then SET Enable to true to re-enable</small> | <small>Verify both SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.IP.Diagnostics.UDPEchoConfig.BytesReceived</small> | <small>Verify BytesReceived is cleared to zero after disabling and re-enabling UDPEchoConfig. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 35: Verify UDPEcho fails when request comes from an IP other than the configured source</strong></summary>

## Test Case 35: TS_TAD_UDPEchoConfig_InvalidUDPRequest

## Objectives
To verify that UDPEcho fails with an invalid UDP Request from an IP address other than the source IP address.

## Test Case ID
TC_TAD_45

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.UDPEchoConfig.Interface | (empty string) |
| Device.IP.Diagnostics.UDPEchoConfig.SourceIPAddress | DUT IP address |
| Device.IP.Diagnostics.UDPEchoConfig.UDPPort | 7 |
| Device.IP.Diagnostics.UDPEchoConfig.Enable | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Interface to empty string, SourceIPAddress to DUT IP, UDPPort to 7, and Enable to true</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Send an invalid UDP echo request from a different IP address (not matching the configured SourceIPAddress)</small> | <small>Verify the UDP request was sent. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.IP.Diagnostics.UDPEchoConfig.BytesReceived</small> | <small>Verify BytesReceived is zero, confirming UDP echo requests from an IP other than the configured source are rejected. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 36: Verify UDPEcho does not work when UDPEchoConfig is disabled</strong></summary>

## Test Case 36: TS_TAD_UDPEchoConfig_TestAfterDisable

## Objectives
To verify that UDPEcho is not working when UDPEchoConfig is disabled.

## Test Case ID
TC_TAD_46

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.UDPEchoConfig.Interface | (empty string) |
| Device.IP.Diagnostics.UDPEchoConfig.SourceIPAddress | DUT IP address |
| Device.IP.Diagnostics.UDPEchoConfig.UDPPort | 7 |
| Device.IP.Diagnostics.UDPEchoConfig.Enable | false |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Interface to empty string, SourceIPAddress to DUT IP, and UDPPort to 7</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.UDPEchoConfig.Enable to false to disable UDPEchoConfig</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Send a UDP echo request from the source IP address to the DUT UDP port 7</small> | <small>Verify the UDP request was sent. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.IP.Diagnostics.UDPEchoConfig.BytesReceived</small> | <small>Verify BytesReceived is zero, confirming UDPEcho does not work when UDPEchoConfig is disabled. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 37: Verify SuccessCount and all response metrics are greater than zero after a successful PingTest</strong></summary>

## Test Case 37: TS_TAD_IPPingTest_CheckSuccessAndResponse

## Objectives
To verify that SuccessCount and all response time metrics are greater than zero after a successful ping test using Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run.

## Test Case ID
TC_TAD_53

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Host | As per test configuration |
| Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.IP.Diagnostics.IPPing.Host and save the original value</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run to true to trigger the ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the ping test to complete</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.IP.Diagnostics.IPPing.SuccessCount, AverageResponseTime, MinimumResponseTime, and MaximumResponseTime</small> | <small>Verify all GET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify SuccessCount, AverageResponseTime, MinimumResponseTime, and MaximumResponseTime are all greater than zero. If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>Revert Device.IP.Diagnostics.IPPing.Host to original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 38: Verify all ping metrics are zero when an invalid URI is set as host</strong></summary>

## Test Case 38: TS_TAD_IPPingTest_InvalidUri_CheckFailureAndResponse

## Objectives
To verify all ping metrics are zero when an invalid URI is set as the host and the ping test is triggered.

## Test Case ID
TC_TAD_54

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Host | (invalid URL) |
| Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to an invalid URL</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run to true to trigger the ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Wait for the ping test to complete</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>GET Device.IP.Diagnostics.IPPing.SuccessCount, AverageResponseTime, MinimumResponseTime, and MaximumResponseTime</small> | <small>Verify all GET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify SuccessCount, AverageResponseTime, MinimumResponseTime, and MaximumResponseTime are all equal to zero. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 39: Verify DiagnosticsState is Error_Other when PingTest is triggered with no host</strong></summary>

## Test Case 39: TS_TAD_IPPingTest_NoHost_CheckStatus

## Objectives
To verify DiagnosticsState is Error_Other when the ping test is triggered with no host name.

## Test Case ID
TC_TAD_55

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Host | (empty string) |
| Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to an empty string</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run to true to trigger the ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Wait for the ping test to complete</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>GET Device.IP.Diagnostics.IPPing.DiagnosticsState</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.IPPing.DiagnosticsState is Error_Other when no host is specified. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 40: Verify DiagnosticsState is Complete when PingTest is triggered with a valid host</strong></summary>

## Test Case 40: TS_TAD_IPPingTest_ValidHostName

## Objectives
To verify DiagnosticsState is Complete when the ping test is triggered with a valid host name.

## Test Case ID
TC_TAD_56

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Host | www.google.com |
| Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to www.google.com</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run to true to trigger the ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Wait for the ping test to complete</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>GET Device.IP.Diagnostics.IPPing.DiagnosticsState</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.IPPing.DiagnosticsState is Complete. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 41: Verify DiagnosticsState is Error_CannotResolveHostName when an invalid host name is set</strong></summary>

## Test Case 41: TS_TAD_IPPingTest_InvalidHostName

## Objectives
To verify DiagnosticsState is Error_CannotResolveHostName when the ping test is triggered with an invalid host name.

## Test Case ID
TC_TAD_57

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Host | www.invalidurl.c |
| Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to www.invalidurl.c</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run to true to trigger the ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Wait for the ping test to complete</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>GET Device.IP.Diagnostics.IPPing.DiagnosticsState</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.IPPing.DiagnosticsState is Error_CannotResolveHostName. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 42: Verify X_RDKCENTRAL-COM_PingTest.DeviceModel matches Device.DeviceInfo.ModelName</strong></summary>

## Test Case 42: TS_TAD_IPPingTest_GetDeviceModel

## Objectives
To get Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.DeviceModel and verify it matches Device.DeviceInfo.ModelName.

## Test Case ID
TC_TAD_58

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
| <small>1</small> | <small>GET Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.DeviceModel</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.DeviceInfo.ModelName</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.DeviceModel matches Device.DeviceInfo.ModelName. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 43: Verify X_RDKCENTRAL-COM_PingTest.DeviceID matches Device.DeviceInfo.SerialNumber</strong></summary>

## Test Case 43: TS_TAD_IPPingTest_GetDeviceID

## Objectives
To get Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.DeviceID and verify it matches Device.DeviceInfo.SerialNumber.

## Test Case ID
TC_TAD_59

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
| <small>1</small> | <small>GET Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.DeviceID</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.DeviceInfo.SerialNumber</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.DeviceID matches Device.DeviceInfo.SerialNumber. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 44: Verify PingTest succeeds even when an invalid interface is set</strong></summary>

## Test Case 44: TS_TAD_IPPingTest_InvalidInterface_CheckSuccessAndResponse

## Objectives
To set an invalid interface and verify SuccessCount and all response time metrics are still greater than zero.

## Test Case ID
TC_TAD_60

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Host | As per test configuration |
| Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.IP.Diagnostics.IPPing.Host and save the original value</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to the configured host value</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run to true with an invalid interface</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the ping test to complete</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.IP.Diagnostics.IPPing.SuccessCount, AverageResponseTime, MinimumResponseTime, and MaximumResponseTime</small> | <small>Verify all GET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify SuccessCount, AverageResponseTime, MinimumResponseTime, and MaximumResponseTime are all greater than zero (CPE uses routing policy). If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>Revert Device.IP.Diagnostics.IPPing.Host to original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 45: Verify X_RDKCENTRAL-COM_PingTest.ecmMAC matches Device.DeviceInfo.X_CISCO_COM_BaseMacAddress</strong></summary>

## Test Case 45: TS_TAD_IPPingTest_GetEcmMAC

## Objectives
To get Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC and verify it matches Device.DeviceInfo.X_CISCO_COM_BaseMacAddress.

## Test Case ID
TC_TAD_65

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
| <small>1</small> | <small>GET Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.DeviceInfo.X_CISCO_COM_BaseMacAddress</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC matches Device.DeviceInfo.X_CISCO_COM_BaseMacAddress. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 46: Verify DiagnosticsState is Error_CannotResolveHostName after timeout when invalid host is set</strong></summary>

## Test Case 46: TS_TAD_IPPingTest_GetDiagnosticState_AfterTimeout

## Objectives
To verify that DiagnosticsState is Error_CannotResolveHostName after the configured timeout when an invalid host is set.

## Test Case ID
TC_TAD_66

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Host | (invalid URL) |
| Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.IP.Diagnostics.IPPing.Timeout and save the original value</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to an invalid URL</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run to true to trigger the ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait for the timeout period to elapse</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.IP.Diagnostics.IPPing.DiagnosticsState</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.IPPing.DiagnosticsState is Error_CannotResolveHostName after the timeout period. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 47: Verify ARPTableNumberOfEntries matches the count from ip neigh command</strong></summary>

## Test Case 47: TS_TAD_IPPingTest_GetARPEntries

## Objectives
To get Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTableNumberOfEntries and verify it matches the number of entries from the ip neigh command.

## Test Case ID
TC_TAD_73

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
| <small>1</small> | <small>GET Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTableNumberOfEntries</small> | <small>Verify the GET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Execute the command "ip neigh show | wc -l" on the DUT to get the number of ARP table entries from the OS</small> | <small>Verify the command executes successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Verify Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTableNumberOfEntries matches the count returned by the "ip neigh show | wc -l" command. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 48: Verify DiagnosticsState reflects timeout error after configuring IPPing timeout</strong></summary>

## Test Case 48: TS_TAD_IPPingTest_ConfigureTimeout

## Objectives
To configure the IPPing timeout value and verify that DiagnosticsState reflects a timeout error when an unreachable host is set.

## Test Case ID
TC_TAD_75

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.IP.Diagnostics.IPPing.Timeout | 1000 |
| Device.IP.Diagnostics.IPPing.Host | www.invalidurl.c |
| Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.IP.Diagnostics.IPPing.Timeout and save the original value</small> | <small>Verify the GET operation returns a non-empty value. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.IP.Diagnostics.IPPing.Timeout to 1000</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.IP.Diagnostics.IPPing.Timeout to verify the new value</small> | <small>Verify the GET operation is successful and value is 1000. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>SET Device.IP.Diagnostics.IPPing.Host to www.invalidurl.c</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>SET Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run to true to trigger the ping test</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Wait for the configured timeout period to elapse</small> | <small>&nbsp;</small> |
| <small>7</small> | <small>GET Device.IP.Diagnostics.IPPing.DiagnosticsState</small> | <small>Verify DiagnosticsState reflects a timeout error. If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>Revert Device.IP.Diagnostics.IPPing.Timeout to original value</small> | <small>&nbsp;</small> |

</details>

---

</details>

---

<details>
<summary><strong>DHCPv4</strong></summary>

# DHCPv4

---

<details>
<summary><strong>E2E - DHCP LAN Configuration</strong></summary>

# E2E - DHCP LAN Configuration

<details>
<summary><strong>Test Case 1: LAN client obtains IP in Class A private DHCP range</strong></summary>

## Test Case 1: E2E_DHCP_ClassAPrivate_CheckLanIPAddress

## Objectives
Verify that the DHCPv4 server pool can be configured with a Class A private IP address range (10.x.x.x) and that a connected LAN client obtains an IP address within that range. The test sets the gateway LAN IP, subnet mask, and DHCP pool boundaries to Class A values and confirms the LAN client's assigned IP falls within the configured range.

## Test Case ID
TC_TDKB_E2E_192

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the configured Class A DHCP range (10.0.0.x)</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 2: LAN client obtains IP in Class B private DHCP range</strong></summary>

## Test Case 2: E2E_DHCP_ClassBPrivate_CheckLanIPAddress

## Objectives
Verify that the DHCPv4 server pool can be configured with a Class B private IP address range (172.16.x.x) and that a connected LAN client obtains an IP address within that range.

## Test Case ID
TC_TDKB_E2E_193

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 172.16.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 172.16.0.2 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 172.16.0.253 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 172.16.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 172.16.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 172.16.0.253</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the configured Class B DHCP range (172.16.0.x)</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 3: LAN client obtains IP in Class C private DHCP range</strong></summary>

## Test Case 3: E2E_DHCP_ClassCPrivate_CheckLanIPAddress

## Objectives
Verify that the DHCPv4 server pool can be configured with a Class C private IP address range (192.168.x.x) and that a connected LAN client obtains an IP address within that range.

## Test Case ID
TC_TDKB_E2E_194

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 192.168.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 192.168.0.2 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 192.168.0.253 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 192.168.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 192.168.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 192.168.0.253</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the configured Class C DHCP range (192.168.0.x)</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 4: DHCP config updates are reflected on LAN client without reboot</strong></summary>

## Test Case 4: E2E_DHCP_Check_ConfigUpdate_InLANClient

## Objectives
Verify that DHCPv4 server configuration updates (LAN IP, subnet mask, and DHCP pool range) are reflected on a connected LAN client without requiring a client reboot. The test sets the gateway to Class A values with a /16 subnet mask and confirms both the subnet mask and IP address are updated on the LAN client.

## Test Case ID
TC_TDKB_E2E_283

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.0.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.0.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the LAN client interface and verify it is 255.255.0.0</small> | <small>Verify the LAN client subnet mask has been updated to 255.255.0.0. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the DHCP range defined by the updated LanIPAddress (10.0.0.x)</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 5: Ensure DHCP address re-assignment with active lease time</strong></summary>


## Test Case 5: E2E_DHCP_GetLanIPAddress_OnReconnection_WithActiveLease

## Objectives
Verify that a LAN client retains the same IP address when disconnected and reconnected while the DHCP lease is still active. The test configures a 120-second lease time, retrieves the initial client IP, waits 60 seconds (half the lease period), and confirms the same IP is assigned after reconnection.

## Test Case ID
TC_TDKB_E2E_276

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Device.DHCPv4.Server.Pool.1.LeaseTime | 120 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress, Device.DHCPv4.Server.Pool.1.MaxAddress and Device.DHCPv4.Server.Pool.1.LeaseTime and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1 and Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0</small> | <small>&nbsp;</small> | <small>Verify SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2, Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 and Device.DHCPv4.Server.Pool.1.LeaseTime to 120</small> | <small>&nbsp;</small> | <small>Verify SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET all five parameters and verify the retrieved values match the SET values</small> | <small>&nbsp;</small> | <small>Verify all retrieved values match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface and save as initial IP</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify the initial LAN client IP address is within the configured DHCP range</small> | <small>Verify LAN client IP is in the DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Wait 60 seconds (lease is still active â€” only half the 120-second lease has elapsed)</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface again and save as renewed IP</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Verify the renewed LAN client IP address is within the configured DHCP range</small> | <small>Verify renewed LAN client IP is in the DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Verify the renewed IP address is the same as the initial IP address (client retains IP while lease is active)</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>12</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>13</small> | <small>Revert Device.DHCPv4.Server.Pool.1.MinAddress, Device.DHCPv4.Server.Pool.1.MaxAddress and Device.DHCPv4.Server.Pool.1.LeaseTime to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 6: LAN client retains same IP on reconnection after lease expiry</strong></summary>

## Test Case 6: E2E_DHCP_GetLanIPAddress_OnReconnection_AfterLeaseTime

## Objectives
Verify that a LAN client retains the same IP address when the DHCP lease expires and is renewed. The test configures a 120-second lease time, waits 150 seconds (beyond lease expiry), and confirms the client is assigned the same IP address upon renewal.

## Test Case ID
TC_TDKB_E2E_277

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Device.DHCPv4.Server.Pool.1.LeaseTime | 120 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress, Device.DHCPv4.Server.Pool.1.MaxAddress and Device.DHCPv4.Server.Pool.1.LeaseTime and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1 and Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0</small> | <small>&nbsp;</small> | <small>Verify SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2, Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 and Device.DHCPv4.Server.Pool.1.LeaseTime to 120</small> | <small>&nbsp;</small> | <small>Verify SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET all five parameters and verify the retrieved values match the SET values</small> | <small>&nbsp;</small> | <small>Verify all retrieved values match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface and save as initial IP</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify the initial LAN client IP address is within the configured DHCP range</small> | <small>Verify LAN client IP is in the DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Wait 150 seconds for the 120-second DHCP lease to expire and for the client to renew its lease</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface after lease expiry and save as renewed IP</small> | <small>Verify the LAN client obtained a valid IP address after lease renewal. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Verify the renewed LAN client IP address is within the configured DHCP range</small> | <small>Verify renewed LAN client IP is in the DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>11</small> | <small>&nbsp;</small> | <small>Verify the renewed IP address is the same as the initial IP address (client retains IP after lease expiry and renewal)</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>12</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>13</small> | <small>Revert Device.DHCPv4.Server.Pool.1.MinAddress, Device.DHCPv4.Server.Pool.1.MaxAddress and Device.DHCPv4.Server.Pool.1.LeaseTime to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 7: Updated DHCP subnet mask is reflected on LAN client</strong></summary>

## Test Case 7: E2E_DHCP_Validate_SetSubnetMask

## Objectives
Verify that the DHCPv4 server subnet mask can be updated on the wireless gateway and that the new subnet mask (255.255.0.0) is reflected on the connected LAN client.

## Test Case ID
TC_TDKB_E2E_264

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.0.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.0.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the LAN client interface and verify it contains 255.255.0.0</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>6</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 8: LAN client IP falls within narrow DHCP server pool range</strong></summary>

## Test Case 8: E2E_DHCP_VerifyLANClientIP_InServerPoolRange

## Objectives
Verify that when the DHCP server pool is configured with a narrow IP address range (10.0.0.10 to 10.0.0.15), the LAN client obtains an IP address that falls strictly within that configured pool range.

## Test Case ID
TC_TDKB_E2E_282

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.0.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.10 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.15 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.0.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.10 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.15</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address falls within the configured pool range (10.0.0.10 to 10.0.0.15)</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

</details>

---

<details>
<summary><strong>E2E - DHCP Invalid LAN IP Address</strong></summary>

# E2E - DHCP Invalid LAN IP Address

<details>
<summary><strong>Test Case 9: DUT rejects public IP address as LAN IP</strong></summary>

## Test Case 9: E2E_DHCP_SetLanIPAddress_PublicAddress

## Objectives
Verify that setting the DHCPv4 server LAN IP address to a public routable IP address (203.212.202.114) is rejected by the DUT. The LAN client IP address must remain unaffected.

## Test Case ID
TC_TDKB_E2E_254

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 203.212.202.114 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 203.212.202.114 (public/routable IP address) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects the public IP address). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify it still holds the baseline value 10.0.0.1 and did not change to 203.212.202.114</small> | <small>&nbsp;</small> | <small>Verify LanIPAddress was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the valid DHCP range (10.0.0.x) and is unaffected by the rejected SET</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>10</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 10: DUT rejects 0.0.0.0 as LAN IP address</strong></summary>

## Test Case 10: E2E_DHCP_SetLanIPAddress_AnyAddress

## Objectives
Verify that setting the DHCPv4 server LAN IP address to 0.0.0.0 (any/unspecified address) is rejected by the DUT and the LAN client IP address remains unaffected.

## Test Case ID
TC_TDKB_E2E_255

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 0.0.0.0 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 0.0.0.0 (any/unspecified address) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects 0.0.0.0). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify it still holds 10.0.0.1 and did not change to 0.0.0.0</small> | <small>&nbsp;</small> | <small>Verify LanIPAddress was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the valid DHCP range (10.0.0.x) and is unaffected by the rejected SET</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>10</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 11: DUT rejects network address as LAN IP</strong></summary>

## Test Case 11: E2E_DHCP_SetLanIPAddress_NetworkIP

## Objectives
Verify that setting the DHCPv4 server LAN IP address to a network address (10.0.0.0) is rejected by the DUT and the LAN client IP address remains unaffected.

## Test Case ID
TC_TDKB_E2E_256

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.0 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.0 (network address) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects the network address). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify it still holds 10.0.0.1 and did not change to 10.0.0.0</small> | <small>&nbsp;</small> | <small>Verify LanIPAddress was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the valid DHCP range (10.0.0.x) and is unaffected by the rejected SET</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>10</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 12: DUT rejects network broadcast address as LAN IP</strong></summary>

## Test Case 12: E2E_DHCP_SetLanIPAddress_NetworkBroadcastIP

## Objectives
Verify that setting the DHCPv4 server LAN IP address to a network broadcast address (10.0.0.255) is rejected by the DUT and the LAN client IP address remains unaffected.

## Test Case ID
TC_TDKB_E2E_257

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.255 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.255 (network broadcast address) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects the network broadcast address). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify it still holds 10.0.0.1 and did not change to 10.0.0.255</small> | <small>&nbsp;</small> | <small>Verify LanIPAddress was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the valid DHCP range (10.0.0.x) and is unaffected by the rejected SET</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>10</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 13: DUT rejects multicast address as LAN IP</strong></summary>

## Test Case 13: E2E_DHCP_SetLanIPAddress_MulticastIPRange

## Objectives
Verify that setting the DHCPv4 server LAN IP address to a multicast address (224.0.0.1) is rejected by the DUT and the LAN client IP address remains unaffected.

## Test Case ID
TC_TDKB_E2E_258

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 224.0.0.1 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 224.0.0.1 (multicast address) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects the multicast address). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify it still holds 10.0.0.1 and did not change to 224.0.0.1</small> | <small>&nbsp;</small> | <small>Verify LanIPAddress was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the valid DHCP range (10.0.0.x) and is unaffected by the rejected SET</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>10</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 14: DUT rejects limited broadcast address as LAN IP</strong></summary>

## Test Case 14: E2E_DHCP_SetLanIPAddress_BroadcastIP

## Objectives
Verify that setting the DHCPv4 server LAN IP address to the limited broadcast address (255.255.255.255) is rejected by the DUT and the LAN client IP address remains unaffected.

## Test Case ID
TC_TDKB_E2E_259

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 255.255.255.255 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 255.255.255.255 (limited broadcast address) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects the limited broadcast address). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify it still holds 10.0.0.1 and did not change to 255.255.255.255</small> | <small>&nbsp;</small> | <small>Verify LanIPAddress was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the valid DHCP range (10.0.0.x) and is unaffected by the rejected SET</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>10</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 15: DUT rejects subnet mask value as LAN IP address</strong></summary>

## Test Case 15: E2E_DHCP_SetLanIPAddress_SubnetMask

## Objectives
Verify that setting the DHCPv4 server LAN IP address to a subnet mask value (255.255.0.0) is rejected by the DUT and the LAN client IP address remains unaffected.

## Test Case ID
TC_TDKB_E2E_260

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 255.255.0.0 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 255.255.0.0 (subnet mask value used as IP address) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects subnet mask value as IP). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify it still holds 10.0.0.1 and did not change to 255.255.0.0</small> | <small>&nbsp;</small> | <small>Verify LanIPAddress was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the valid DHCP range (10.0.0.x) and is unaffected by the rejected SET</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>10</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 16: DUT rejects special characters as LAN IP address</strong></summary>

## Test Case 16: E2E_DHCP_SetLanIPAddress_SpecialCharacters

## Objectives
Verify that setting the DHCPv4 server LAN IP address to a string of special characters (!@*&!) is rejected by the DUT and the LAN client IP address remains unaffected.

## Test Case ID
TC_TDKB_E2E_261

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | !@*&! |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to !@*&! (special characters string) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects the special characters string). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify it still holds 10.0.0.1 and did not change to !@*&!</small> | <small>&nbsp;</small> | <small>Verify LanIPAddress was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the valid DHCP range (10.0.0.x) and is unaffected by the rejected SET</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>10</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 17: DUT rejects alphanumeric string as LAN IP address</strong></summary>

## Test Case 17: E2E_DHCP_SetLanIPAddress_Alphanumeric

## Objectives
Verify that setting the DHCPv4 server LAN IP address to an alphanumeric string (test123) is rejected by the DUT and the LAN client IP address remains unaffected.

## Test Case ID
TC_TDKB_E2E_262

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | test123 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to test123 (alphanumeric string) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects the alphanumeric string). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify it still holds 10.0.0.1 and did not change to test123</small> | <small>&nbsp;</small> | <small>Verify LanIPAddress was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the valid DHCP range (10.0.0.x) and is unaffected by the rejected SET</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>10</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 18: DUT rejects hexadecimal string as LAN IP address</strong></summary>

## Test Case 18: E2E_DHCP_SetLanIPAddress_Hexadecimal

## Objectives
Verify that setting the DHCPv4 server LAN IP address to a hexadecimal string (123ABC) is rejected by the DUT and the LAN client IP address remains unaffected.

## Test Case ID
TC_TDKB_E2E_263

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 123ABC |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 123ABC (hexadecimal string) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects the hexadecimal string). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify it still holds 10.0.0.1 and did not change to 123ABC</small> | <small>&nbsp;</small> | <small>Verify LanIPAddress was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the valid DHCP range (10.0.0.x) and is unaffected by the rejected SET</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>10</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 19: DUT rejects DHCP lease time less than 120 seconds</strong></summary>

## Test Case 19: E2E_DHCP_SetServerLeaseTime_LessThan120

## Objectives
Verify that the DHCPv4 server lease time cannot be set to a value less than 120 seconds (2 minutes). The DUT must reject a LeaseTime of 60 seconds, and the LAN client lease time must remain unchanged at the previously configured value.

## Test Case ID
TC_TDKB_E2E_275

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Baseline Device.DHCPv4.Server.Pool.1.LeaseTime | 120 |
| Invalid Device.DHCPv4.Server.Pool.1.LeaseTime | 60 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress, Device.DHCPv4.Server.Pool.1.MaxAddress and Device.DHCPv4.Server.Pool.1.LeaseTime and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1 and Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0</small> | <small>&nbsp;</small> | <small>Verify SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2, Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 and Device.DHCPv4.Server.Pool.1.LeaseTime to 120</small> | <small>&nbsp;</small> | <small>Verify SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET all five parameters and verify the retrieved values match the SET values</small> | <small>&nbsp;</small> | <small>Verify all retrieved values match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>6</small> | <small>Attempt to SET Device.DHCPv4.Server.Pool.1.LeaseTime to 60 (less than minimum 120 seconds) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects lease time less than 120 s). If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.DHCPv4.Server.Pool.1.LeaseTime and verify it still holds 120 and did not change to 60</small> | <small>&nbsp;</small> | <small>Verify LeaseTime was not changed to 60. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the valid DHCP range (10.0.0.x)</small> | <small>Verify LAN client IP is in the DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>&nbsp;</small> | <small>Retrieve the lease time from the LAN client's DHCP lease and verify it is not 60 seconds (confirming the rejected SET had no effect on the client)</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>11</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>12</small> | <small>Revert Device.DHCPv4.Server.Pool.1.MinAddress, Device.DHCPv4.Server.Pool.1.MaxAddress and Device.DHCPv4.Server.Pool.1.LeaseTime to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

</details>

---

<details>
<summary><strong>E2E - DHCP Invalid Subnet Mask</strong></summary>

# E2E - DHCP Invalid Subnet Mask

<details>
<summary><strong>Test Case 20: DUT rejects public IP address as subnet mask</strong></summary>

## Test Case 20: E2E_DHCP_SetSubnetMask_PublicAddress

## Objectives
Verify that setting the DHCPv4 server subnet mask to a public routable IP address (203.212.202.114) is rejected by the DUT and the LAN client subnet mask remains unaffected.

## Test Case ID
TC_TDKB_E2E_265

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 203.212.202.114 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 203.212.202.114 (public IP address used as subnet mask) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects the public IP as subnet mask). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask and verify it still holds 255.255.255.0 and did not change to 203.212.202.114</small> | <small>&nbsp;</small> | <small>Verify LanSubnetMask was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the LAN client interface and verify it does not contain 203.212.202.114</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 21: DUT rejects 0.0.0.0 as subnet mask</strong></summary>

## Test Case 21: E2E_DHCP_SetSubnetMask_AnyAddress

## Objectives
Verify that setting the DHCPv4 server subnet mask to 0.0.0.0 (any address) is rejected by the DUT and the LAN client subnet mask remains unaffected.

## Test Case ID
TC_TDKB_E2E_266

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 0.0.0.0 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 0.0.0.0 (any/unspecified address) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects 0.0.0.0 as subnet mask). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask and verify it still holds 255.255.255.0 and did not change to 0.0.0.0</small> | <small>&nbsp;</small> | <small>Verify LanSubnetMask was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the LAN client interface and verify it does not contain 0.0.0.0</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 22: DUT rejects network address as subnet mask</strong></summary>

## Test Case 22: E2E_DHCP_SetSubnetMask_NetworkIP

## Objectives
Verify that setting the DHCPv4 server subnet mask to a network address value (10.0.0.0) is rejected by the DUT and the LAN client subnet mask remains unaffected.

## Test Case ID
TC_TDKB_E2E_267

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 10.0.0.0 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 10.0.0.0 (network address) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects network address as subnet mask). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask and verify it still holds 255.255.255.0 and did not change to 10.0.0.0</small> | <small>&nbsp;</small> | <small>Verify LanSubnetMask was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the LAN client interface and verify it does not contain 10.0.0.0</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 23: DUT rejects network broadcast address as subnet mask</strong></summary>

## Test Case 23: E2E_DHCP_SetSubnetMask_NetworkBroadcastIP

## Objectives
Verify that setting the DHCPv4 server subnet mask to a network broadcast address value (10.0.0.255) is rejected by the DUT and the LAN client subnet mask remains unaffected.

## Test Case ID
TC_TDKB_E2E_268

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 10.0.0.255 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 10.0.0.255 (network broadcast address) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects network broadcast address as subnet mask). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask and verify it still holds 255.255.255.0 and did not change to 10.0.0.255</small> | <small>&nbsp;</small> | <small>Verify LanSubnetMask was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the LAN client interface and verify it does not contain 10.0.0.255</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 24: DUT rejects multicast address as subnet mask</strong></summary>

## Test Case 24: E2E_DHCP_SetSubnetMask_MulticastIPRange

## Objectives
Verify that setting the DHCPv4 server subnet mask to a multicast address (224.0.0.1) is rejected by the DUT and the LAN client subnet mask remains unaffected.

## Test Case ID
TC_TDKB_E2E_269

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 224.0.0.1 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 224.0.0.1 (multicast address) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects multicast address as subnet mask). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask and verify it still holds 255.255.255.0 and did not change to 224.0.0.1</small> | <small>&nbsp;</small> | <small>Verify LanSubnetMask was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the LAN client interface and verify it does not contain 224.0.0.1</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 25: DUT rejects limited broadcast address as subnet mask</strong></summary>

## Test Case 25: E2E_DHCP_SetSubnetMask_BroadcastIP

## Objectives
Verify that setting the DHCPv4 server subnet mask to the limited broadcast address (255.255.255.255) is rejected by the DUT and the LAN client subnet mask remains unaffected.

## Test Case ID
TC_TDKB_E2E_270

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.255 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.255 (limited broadcast address) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects limited broadcast as subnet mask). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask and verify it still holds 255.255.255.0 and did not change to 255.255.255.255</small> | <small>&nbsp;</small> | <small>Verify LanSubnetMask was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the LAN client interface and verify it does not contain 255.255.255.255</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 26: DUT rejects special characters as subnet mask</strong></summary>

## Test Case 26: E2E_DHCP_SetSubnetMask_SpecialCharacters

## Objectives
Verify that setting the DHCPv4 server subnet mask to a string of special characters (!@*&!) is rejected by the DUT and the LAN client subnet mask remains unaffected.

## Test Case ID
TC_TDKB_E2E_271

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | !@*&! |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to !@*&! (special characters string) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects special characters as subnet mask). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask and verify it still holds 255.255.255.0 and did not change to !@*&!</small> | <small>&nbsp;</small> | <small>Verify LanSubnetMask was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the LAN client interface and verify it does not contain !@*&!</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 27: DUT rejects alphanumeric string as subnet mask</strong></summary>

## Test Case 27: E2E_DHCP_SetSubnetMask_Alphanumeric

## Objectives
Verify that setting the DHCPv4 server subnet mask to an alphanumeric string (test123) is rejected by the DUT and the LAN client subnet mask remains unaffected.

## Test Case ID
TC_TDKB_E2E_272

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | test123 |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to test123 (alphanumeric string) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects alphanumeric string as subnet mask). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask and verify it still holds 255.255.255.0 and did not change to test123</small> | <small>&nbsp;</small> | <small>Verify LanSubnetMask was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the LAN client interface and verify it does not contain test123</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 28: DUT rejects hexadecimal string as subnet mask</strong></summary>

## Test Case 28: E2E_DHCP_SetSubnetMask_Hexadecimal

## Objectives
Verify that setting the DHCPv4 server subnet mask to a hexadecimal string (123ABC) is rejected by the DUT and the LAN client subnet mask remains unaffected.

## Test Case ID
TC_TDKB_E2E_273

## Test Type
Negative

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client â€“ Wired Ethernet client connected to DUT LAN port |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Baseline Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Baseline Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Baseline Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |
| Invalid Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 123ABC |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253 (Class A baseline)</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the SET baseline values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Attempt to SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 123ABC (hexadecimal string) â€” DUT should reject this invalid value</small> | <small>&nbsp;</small> | <small>Verify the SET operation fails (DUT rejects hexadecimal string as subnet mask). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask and verify it still holds 255.255.255.0 and did not change to 123ABC</small> | <small>&nbsp;</small> | <small>Verify LanSubnetMask was not changed to the invalid value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the LAN client interface and verify it does not contain 123ABC</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

</details>

---

<details>
<summary><strong>E2E - DHCP WLAN Configuration</strong></summary>

# E2E - DHCP WLAN Configuration


<details>
<summary><strong>Test Case 29: WLAN client obtains IP in Class A private DHCP range</strong></summary>

## Test Case 29: E2E_DHCP_WLAN_ClassAPrivate_CheckIPAddress

## Objectives
Verify that when the DHCP server pool is configured with a Class A private IP address range (10.x.x.x), a WLAN client connecting to the configured WLAN SSID obtains an IP address within that range.

## Test Case ID
TC_TDKB_E2E_786

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | Configured from test config |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | Configured from test config |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase to configured values; SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET all six parameters and verify the retrieved values match the SET values</small> | <small>&nbsp;</small> | <small>Verify all retrieved values match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Connect WLAN client to the configured SSID using the configured credentials</small> | <small>Verify the WLAN client connected successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the WLAN client interface</small> | <small>Verify the WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify the WLAN client IP address is within the configured Class A DHCP range (10.0.0.x)</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from the configured SSID</small> | <small>&nbsp;</small> |
| <small>9</small> | <small>Revert Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 30: WLAN client obtains IP in Class B private DHCP range</strong></summary>

## Test Case 30: E2E_DHCP_WLAN_ClassBPrivate_CheckIPAddress

## Objectives
Verify that when the DHCP server pool is configured with a Class B private IP address range (172.16.x.x), a WLAN client connecting to the configured WLAN SSID obtains an IP address within that range.

## Test Case ID
TC_TDKB_E2E_787

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | Configured from test config |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | Configured from test config |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 172.16.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.0.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 172.16.0.2 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 172.16.0.253 |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase to configured values; SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 172.16.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.0.0, Device.DHCPv4.Server.Pool.1.MinAddress to 172.16.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 172.16.0.253</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET all six parameters and verify the retrieved values match the SET values</small> | <small>&nbsp;</small> | <small>Verify all retrieved values match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Connect WLAN client to the configured SSID using the configured credentials</small> | <small>Verify the WLAN client connected successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the WLAN client interface</small> | <small>Verify the WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify the WLAN client IP address is within the configured Class B DHCP range (172.16.0.x)</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from the configured SSID</small> | <small>&nbsp;</small> |
| <small>9</small> | <small>Revert Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 31: WLAN client obtains IP in Class C private DHCP range</strong></summary>

## Test Case 31: E2E_DHCP_WLAN_ClassCPrivate_CheckIPAddress

## Objectives
Verify that when the DHCP server pool is configured with a Class C private IP address range (192.168.x.x), a WLAN client connecting to the configured WLAN SSID obtains an IP address within that range.

## Test Case ID
TC_TDKB_E2E_788

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | Configured from test config |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | Configured from test config |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 192.168.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 192.168.0.2 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 192.168.0.253 |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase to configured values; SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 192.168.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 192.168.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 192.168.0.253</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET all six parameters and verify the retrieved values match the SET values</small> | <small>&nbsp;</small> | <small>Verify all retrieved values match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Connect WLAN client to the configured SSID using the configured credentials</small> | <small>Verify the WLAN client connected successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the WLAN client interface</small> | <small>Verify the WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify the WLAN client IP address is within the configured Class C DHCP range (192.168.0.x)</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from the configured SSID</small> | <small>&nbsp;</small> |
| <small>9</small> | <small>Revert Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 32: WLAN client receives 255.0.0.0 subnet mask from DHCP</strong></summary>

## Test Case 32: E2E_DHCP_WLAN_SetSubnetMask_255.0.0.0

## Objectives
Verify that when the DHCP server subnet mask is configured to 255.0.0.0 (/8), a WLAN client connecting to the configured WLAN SSID receives this subnet mask in its DHCP lease.

## Test Case ID
TC_TDKB_E2E_789

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | Configured from test config |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | Configured from test config |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.0.0.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase to configured values; SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.0.0.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET all six parameters and verify the retrieved values match the SET values</small> | <small>&nbsp;</small> | <small>Verify all retrieved values match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Connect WLAN client to the configured SSID using the configured credentials</small> | <small>Verify the WLAN client connected successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the WLAN client interface</small> | <small>Verify the WLAN client subnet mask is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify the WLAN client subnet mask is 255.0.0.0</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from the configured SSID</small> | <small>&nbsp;</small> |
| <small>9</small> | <small>Revert Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 33: WLAN client receives 255.255.0.0 subnet mask from DHCP</strong></summary>

## Test Case 33: E2E_DHCP_WLAN_SetSubnetMask_255.255.0.0

## Objectives
Verify that when the DHCP server subnet mask is configured to 255.255.0.0 (/16), a WLAN client connecting to the configured WLAN SSID receives this subnet mask in its DHCP lease.

## Test Case ID
TC_TDKB_E2E_790

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | Configured from test config |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | Configured from test config |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.0.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase to configured values; SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.0.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET all six parameters and verify the retrieved values match the SET values</small> | <small>&nbsp;</small> | <small>Verify all retrieved values match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Connect WLAN client to the configured SSID using the configured credentials</small> | <small>Verify the WLAN client connected successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the WLAN client interface</small> | <small>Verify the WLAN client subnet mask is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify the WLAN client subnet mask is 255.255.0.0</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from the configured SSID</small> | <small>&nbsp;</small> |
| <small>9</small> | <small>Revert Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 34: WLAN client receives 255.255.255.0 subnet mask from DHCP</strong></summary>

## Test Case 34: E2E_DHCP_WLAN_SetSubnetMask_255.255.255.0

## Objectives
Verify that when the DHCP server subnet mask is configured to 255.255.255.0 (/24), a WLAN client connecting to the configured WLAN SSID receives this subnet mask in its DHCP lease.

## Test Case ID
TC_TDKB_E2E_791

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | Configured from test config |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | Configured from test config |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.0 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase to configured values; SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.0, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.253</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET all six parameters and verify the retrieved values match the SET values</small> | <small>&nbsp;</small> | <small>Verify all retrieved values match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Connect WLAN client to the configured SSID using the configured credentials</small> | <small>Verify the WLAN client connected successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the WLAN client interface</small> | <small>Verify the WLAN client subnet mask is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify the WLAN client subnet mask is 255.255.255.0</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from the configured SSID</small> | <small>&nbsp;</small> |
| <small>9</small> | <small>Revert Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 35: WLAN client receives 255.255.255.128 subnet mask from DHCP</strong></summary>

## Test Case 35: E2E_DHCP_WLAN_SetSubnetMask_255.255.255.128

## Objectives
Verify that when the DHCP server subnet mask is configured to 255.255.255.128 (/25), a WLAN client connecting to the configured WLAN SSID receives this subnet mask in its DHCP lease. The DHCP pool MaxAddress is set to 10.0.0.126 to fit within the /25 subnet range.

## Test Case ID
TC_TDKB_E2E_792

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client â€“ Wi-Fi client connected to DUT wireless network |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | Configured from test config |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | Configured from test config |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 |
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask | 255.255.255.128 |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.126 |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase to configured values; SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 10.0.0.1, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to 255.255.255.128, Device.DHCPv4.Server.Pool.1.MinAddress to 10.0.0.2 and Device.DHCPv4.Server.Pool.1.MaxAddress to 10.0.0.126</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET all six parameters and verify the retrieved values match the SET values</small> | <small>&nbsp;</small> | <small>Verify all retrieved values match the configured values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Connect WLAN client to the configured SSID using the configured credentials</small> | <small>Verify the WLAN client connected successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Get the subnet mask assigned to the WLAN client interface</small> | <small>Verify the WLAN client subnet mask is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify the WLAN client subnet mask is 255.255.255.128</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Disconnect WLAN client from the configured SSID</small> | <small>&nbsp;</small> |
| <small>9</small> | <small>Revert Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

</details>

---

</details>

---

<details>
<summary><strong>IPv6</strong></summary>

# IPv6

<details>
<summary><strong>E2E</strong></summary>

# E2E

<details>
<summary><strong>Test Case 1: E2E_IPV6_CheckDNSResolutionViaPrimaryDNSServerFromLANClient</strong></summary>

## Test Case 1: E2E_IPV6_CheckDNSResolutionViaPrimaryDNSServerFromLANClient

## Objectives

Verify that the Primary IPv6 DNS server configured on the gateway successfully resolves DNS queries issued from a wired LAN client. The test retrieves the DUT's WAN IPv6 address to confirm IPv6 connectivity, obtains the Primary IPv6 DNS server address from Device.DNS.Client.Server.1.DNSServer, and then connects to the LAN client to perform an nslookup, confirming the domain name is resolved successfully via the Primary DNS server.

## Test Case ID

TC_TDKB_E2E_782

## Test Type

Positive

## Test Environment

| Component                                                    |
| ------------------------------------------------------------ |
| DUT - Device under test                    |
| LAN Client - Wired Ethernet client connected to DUT LAN port |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | LAN Client                                                                                                              | TDK Validation and Expected Results                                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                   | <small>&nbsp;</small>                                                                                                                  |
| <small>2</small> | <small>&nbsp;</small>                                                                                                                                               | <small>Ensure the LAN client is connected to the gateway and has obtained a valid IPv6 address from the gateway</small> | <small>Verify LAN client is connected and has obtained a valid IPv6 address. If the condition is met CONTINUE, else FAIL</small>       |
| <small>3</small> | <small>GET Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 to retrieve the WAN IPv6 address</small>                                                                        | <small>&nbsp;</small>                                                                                                   | <small>Verify WAN IPv6 address is available. If the condition is met CONTINUE, else FAIL</small>                                       |
| <small>4</small> | <small>GET Device.DNS.Client.Server.1.DNSServer to retrieve the Primary IPv6 DNS server address</small>                                                             | <small>&nbsp;</small>                                                                                                   | <small>Verify Primary IPv6 DNS server address is obtained. If the condition is met CONTINUE, else FAIL</small>                         |
| <small>5</small> | <small>&nbsp;</small>                                                                                                                                               | <small>Perform nslookup for the configured domain name using the retrieved Primary IPv6 DNS server address</small>      | <small>Verify the domain name is resolved successfully by the Primary IPv6 DNS server. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 2: E2E_IPV6_CheckInternetConnectivityFromLANClient</strong></summary>

## Test Case 2: E2E_IPV6_CheckInternetConnectivityFromLANClient

## Objectives

Verify that a wired LAN client connected to the gateway has end-to-end IPv6 internet connectivity. The test retrieves the DUT's WAN IPv6 address, obtains and validates the LAN client's IPv6 address on its interface, and then performs an IPv6 ping to an external host via the LAN interface to confirm active IPv6 internet connectivity from the LAN client.

## Test Case ID

TC_TDKB_E2E_784

## Test Type

Positive

## Test Environment

| Component                                                    |
| ------------------------------------------------------------ |
| DUT - Device under test                    |
| LAN Client - Wired Ethernet client connected to DUT LAN port |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | LAN Client                                                                                                              | TDK Validation and Expected Results                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                   | <small>&nbsp;</small>                                                                                                                        |
| <small>2</small> | <small>&nbsp;</small>                                                                                                                                               | <small>Ensure the LAN client is connected to the gateway and has obtained a valid IPv6 address from the gateway</small> | <small>Verify LAN client is connected and has obtained a valid IPv6 address. If the condition is met CONTINUE, else FAIL</small>             |
| <small>3</small> | <small>GET Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 to retrieve the WAN IPv6 address</small>                                                                        | <small>&nbsp;</small>                                                                                                   | <small>Verify WAN IPv6 address is obtained successfully. If the condition is met CONTINUE, else FAIL</small>                                 |
| <small>4</small> | <small>&nbsp;</small>                                                                                                                                               | <small>Get the IPv6 address of the LAN client interface</small>                                                         | <small>Verify LAN client has an IPv6 address. If the condition is met CONTINUE, else FAIL</small>                                            |
| <small>5</small> | <small>&nbsp;</small>                                                                                                                                               | <small>Check that the IPv6 address obtained from the LAN client interface is in valid IPv6 format</small>               | <small>Verify the IPv6 address obtained from the LAN client is a valid IPv6 format. If the condition is met CONTINUE, else FAIL</small>      |
| <small>6</small> | <small>&nbsp;</small>                                                                                                                                               | <small>Check IPv6 internet connectivity by pinging an external IPv6 host via the LAN interface</small>                  | <small>Verify IPv6 ping to the external host via LAN interface succeeds with 0% packet loss. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 3: E2E_IPV6_CheckInternetConnectivityFromWLANClient</strong></summary>

## Test Case 3: E2E_IPV6_CheckInternetConnectivityFromWLANClient

## Objectives

Verify that a WLAN client connected to the gateway has end-to-end IPv6 internet connectivity. The test retrieves the DUT's WAN IPv6 address and saves the current SSID and key passphrase values. When the device does not have MLO capability, the SSID and key passphrase are configured with the test values before connecting the WLAN client to the WiFi network. The WLAN client's IPv6 address is then obtained and validated for correct IPv6 format, and an IPv6 ping to an external host is performed via the WLAN interface to confirm active IPv6 internet connectivity. Any modified WiFi parameters are reverted to their original values after the test.

## Test Case ID

TC_TDKB_E2E_785

## Test Type

Positive

## Test Environment

| Component                                                  |
| ---------------------------------------------------------- |
| DUT - Device under test                  |
| WLAN client - Wireless LAN client |

## Test Configuration

| Parameter                                                         | Value                     |
| ----------------------------------------------------------------- | ------------------------- |
| Device.WiFi.SSID.{i}.SSID                          | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |

## Test Procedure and Expected Results

| Step Number       | DUT                                                                                                                                                                 | WLAN Client                                                                                                | TDK Validation and Expected Results                                                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small>  | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                      | <small>&nbsp;</small>                                                                                                                             |
| <small>2</small>  | <small>GET Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 to retrieve the WAN IPv6 address</small>                                                                        | <small>&nbsp;</small>                                                                                      | <small>Verify WAN IPv6 address is obtained successfully. If the condition is met CONTINUE, else FAIL</small>                                      |
| <small>3</small>  | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase to save the current values</small>                                      | <small>&nbsp;</small>                                                                                      | <small>Verify current SSID and key passphrase values are retrieved. If the condition is met CONTINUE, else FAIL</small>                           |
| <small>4</small>  | <small>SET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase to the configured values if required</small>                                        | <small>&nbsp;</small>                                                                                      | <small>Verify SSID and key passphrase are SET successfully. If the condition is met CONTINUE, else FAIL</small>                                   |
| <small>5</small>  | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase to verify the SET values</small>                                        | <small>&nbsp;</small>                                                                                      | <small>Verify retrieved SSID and key passphrase values match the configured values. If the condition is met CONTINUE, else FAIL</small>           |
| <small>6</small>  | <small>&nbsp;</small>                                                                                                                                               | <small>Connect to the configured WiFi SSID</small>                                                         | <small>Verify WLAN client connects to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small>                             |
| <small>7</small>  | <small>&nbsp;</small>                                                                                                                                               | <small>Get the IPv6 address of the WLAN client interface</small>                                           | <small>Verify WLAN client has an IPv6 address. If the condition is met CONTINUE, else FAIL</small>                                                |
| <small>8</small>  | <small>&nbsp;</small>                                                                                                                                               | <small>Check that the IPv6 address obtained from the WLAN client interface is in valid IPv6 format</small> | <small>Verify the IPv6 address obtained from the WLAN client is a valid IPv6 format. If the condition is met CONTINUE, else FAIL</small>          |
| <small>9</small>  | <small>&nbsp;</small>                                                                                                                                               | <small>Check IPv6 internet connectivity by pinging an external IPv6 host via the WLAN interface</small>    | <small>Verify IPv6 ping to the external host via WLAN interface succeeds with 0% packet loss. If the condition is met CONTINUE, else FAIL</small> |
| <small>10</small> | <small>&nbsp;</small>                                                                                                                                               | <small>Disconnect from the configured WiFi SSID</small>                                                    | <small>Verify WLAN client is disconnected from the WiFi SSID. If the condition is met CONTINUE, else FAIL</small>                                 |
| <small>11</small> | <small>Revert Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase to their original values</small>                                     | <small>&nbsp;</small>                                                                                      | <small>Verify SSID and key passphrase are reverted to original values. If the condition is met PASS, else FAIL</small>                            |

</details>

---

<details>
<summary><strong>Test Case 4: E2E_IPV6_DNSResolutionViaPrimaryDNSServerFromWLANClient</strong></summary>

## Test Case 4: E2E_IPV6_DNSResolutionViaPrimaryDNSServerFromWLANClient

## Objectives

Verify that the Primary IPv6 DNS server configured on the gateway successfully resolves DNS queries issued from a WLAN client. The test retrieves the DUT's WAN IPv6 address, the current SSID, key passphrase, and Primary IPv6 DNS server address. When the device does not have MLO capability, the SSID and key passphrase are configured with the test values before connecting the WLAN client to the WiFi network. An nslookup is then performed from the WLAN client using the retrieved Primary IPv6 DNS server address to confirm that the domain name is resolved successfully. Any modified WiFi parameters are reverted to their original values after the test.

## Test Case ID

TC_TDKB_E2E_783

## Test Type

Positive

## Test Environment

| Component                                                  |
| ---------------------------------------------------------- |
| DUT - Device under test                  |
| WLAN client - Wireless LAN client |

## Test Configuration

| Parameter                                                         | Value                     |
| ----------------------------------------------------------------- | ------------------------- |
| Device.WiFi.SSID.{i}.SSID                         | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                  | WLAN Client                                                                                                                                                  | TDK Validation and Expected Results                                                                                                         |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small>  | <small>&nbsp;</small>                                                                                                                                        | <small>&nbsp;</small>                                                                                                                       |
| <small>2</small> | <small>GET Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 to retrieve the WAN IPv6 address</small>                                                                         | <small>&nbsp;</small>                                                                                                                                        | <small>Verify WAN IPv6 address is obtained successfully. If the condition is met CONTINUE, else FAIL</small>                                |
| <small>3</small> | <small>GET Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase and Device.DNS.Client.Server.1.DNSServer to save the current values</small> | <small>&nbsp;</small>                                                                                                                                        | <small>Verify current SSID, key passphrase and Primary DNS server values are retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>SET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase to the configured values if required</small>                                         | <small>&nbsp;</small>                                                                                                                                        | <small>Verify SSID and key passphrase are SET successfully. If the condition is met CONTINUE, else FAIL</small>                             |
| <small>5</small> | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase to verify the SET values</small>                                         | <small>&nbsp;</small>                                                                                                                                        | <small>Verify retrieved SSID and key passphrase values match the configured values. If the condition is met CONTINUE, else FAIL</small>     |
| <small>6</small> | <small>&nbsp;</small>                                                                                                                                                | <small>Connect to the configured WiFi SSID</small>                                                                                                           | <small>Verify WLAN client connects to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL</small>                       |
| <small>7</small> | <small>&nbsp;</small>                                                                                                                                                | <small>Perform nslookup for the configured domain name using the Primary IPv6 DNS server address retrieved from Device.DNS.Client.Server.1.DNSServer</small> | <small>Verify the domain name is resolved successfully by the Primary IPv6 DNS server. If the condition is met CONTINUE, else FAIL</small>  |
| <small>8</small> | <small>&nbsp;</small>                                                                                                                                                | <small>Disconnect from the configured WiFi SSID</small>                                                                                                      | <small>Verify WLAN client is disconnected from the WiFi SSID. If the condition is met CONTINUE, else FAIL</small>                           |
| <small>9</small> | <small>Revert Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase to their original values</small>                                      | <small>&nbsp;</small>                                                                                                                                        | <small>Verify SSID and key passphrase are reverted to original values. If the condition is met PASS, else FAIL</small>                      |

</details>

---

</details>

---

<details>
<summary><strong>IPV6 - Status Checks</strong></summary>

# IPV6 - Status Checks

<details>
<summary><strong>Test Case 5: TS_IPV6_Get_WANIPv6Address</strong></summary>

## Test Case 5: TS_IPV6_Get_WANIPv6Address

## Objectives

Verify that the WAN interface (erouter0) on the DUT receives a valid global IPv6 address via DHCPv6, with prefix length /128. The test retrieves the WAN interface name using Device.DHCPv6.Client.1.Interface, confirms the interface has a global scope IPv6 address, validates the prefix length is /128, and cross-verifies that the IPv6 address obtained from the TR-181 data model (Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6) matches the address observed directly on the WAN interface.

## Test Case ID

TC_IPV6_1

## Test Type

Positive

## Test Environment

| Component                                 |
| ----------------------------------------- |
| DUT - Device under test |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                                                                                  |
| <small>2</small> | <small>GET Device.DHCPv6.Client.1.Interface to retrieve the WAN interface name</small>                                                                              | <small>Verify WAN interface name is obtained successfully. If the condition is met CONTINUE, else FAIL</small>                                                                         |
| <small>3</small> | <small>Run the command to check for a global scope inet6 address on the WAN interface</small>                                                             | <small>Verify WAN interface has inet6 address with global scope. If the condition is met CONTINUE, else FAIL</small>                                                                   |
| <small>4</small> | <small>Run the command to extract the global IPv6 address and prefix length from the WAN interface</small>                                                             | <small>Verify IPv6 address and prefix length are obtained from the WAN interface. If the condition is met CONTINUE, else FAIL</small>                                                  |
| <small>5</small> | <small>Check that the global IPv6 address prefix length on the WAN interface is /128</small>                                                                        | <small>Verify the global IPv6 address prefix length on the WAN interface is /128. If the condition is met CONTINUE, else FAIL</small>                                                  |
| <small>6</small> | <small>GET Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 to retrieve WAN IPv6 address via TR-181</small>                                                                 | <small>Verify WAN IPv6 address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small>                                                                          |
| <small>7</small> | <small>Validate that the retrieved WAN IPv6 address is in valid IPv6 format</small>                                                                                 | <small>Verify the retrieved IPv6 address is a valid IPv6 format. If the condition is met CONTINUE, else FAIL</small>                                                                   |
| <small>8</small> | <small>Compare the IPv6 address from Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 with the IPv6 address obtained from the WAN interface</small>                         | <small>Verify the IPv6 address from Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 matches the IPv6 address obtained from the WAN interface. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 6: TS_IPV6_Get_Brlan0_IPv6Address</strong></summary>

## Test Case 6: TS_IPV6_Get_Brlan0_IPv6Address

## Objectives

Verify that the LAN bridge interface brlan0 on the DUT receives a valid global IPv6 address via DHCPv6 prefix delegation, with prefix length /64. The test checks the brlan0 interface for a global scope IPv6 address, extracts the address and prefix length, and confirms the prefix length is /64, validating that the DUT correctly receives and assigns a delegated IPv6 prefix to its LAN interface.

## Test Case ID

TC_IPV6_2

## Test Type

Positive

## Test Environment

| Component                                 |
| ----------------------------------------- |
| DUT - Device under test |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                      |
| <small>2</small> | <small>Run the command to check for a global scope inet6 address on brlan0</small>                                                                           | <small>Verify brlan0 interface has inet6 address with global scope. If the condition is met CONTINUE, else FAIL</small>    |
| <small>3</small> | <small>Run the command to extract the global IPv6 address and prefix length from brlan0</small>                                                                    | <small>Verify IPv6 address and prefix length are obtained from brlan0. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Check that the global IPv6 address prefix length on brlan0 is /64</small>                                                                                    | <small>Verify the global IPv6 address prefix length on brlan0 is /64. If the condition is met PASS, else FAIL</small>      |

</details>

---

<details>
<summary><strong>Test Case 7: TS_IPV6_CheckDibblerServerStatus</strong></summary>

## Test Case 7: TS_IPV6_CheckDibblerServerStatus

## Objectives

Verify that the Dibbler DHCPv6 server process is actively running on the DUT. The test checks the process list to confirm the dibbler-server process is present and then validates the dibbler-server status output to confirm the server is in RUNNING state and returns a valid process ID (PID), ensuring the DHCPv6 server is fully operational.

## Test Case ID

TC_IPV6_3

## Test Type

Positive

## Test Environment

| Component                                 |
| ----------------------------------------- |
| DUT - Device under test |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                       |
| <small>2</small> | <small>Run the command to check if the dibbler-server process is active</small>                                             | <small>Verify dibbler-server process is present and active. If the condition is met CONTINUE, else FAIL</small>             |
| <small>3</small> | <small>Run the command to retrieve the dibbler-server status and PID</small>                                               | <small>Verify dibbler-server status is RUNNING and a valid PID is obtained. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 8: TS_IPV6_Check_ActiveLANClient_IPv6Address</strong></summary>

## Test Case 8: TS_IPV6_Check_ActiveLANClient_IPv6Address

## Objectives

Verify that the DUT's host table correctly records the global IPv6 address of an active wired LAN client. The test confirms that there are active clients connected to the gateway, identifies an active LAN client with an Ethernet Layer1 interface from the Device.Hosts table, and validates that its global IPv6 address is populated in the Device.Hosts.Host.{i}.IPv6Address table entry.

## Test Case ID

TC_IPV6_4

## Test Type

Positive

## Test Environment

| Component                                                    |
| ------------------------------------------------------------ |
| DUT - Device under test                    |
| LAN Client - Wired Ethernet client connected to DUT LAN port |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                                   |
| <small>2</small> | <small>GET Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber to get the number of active connected clients</small>                                                     | <small>Verify the number of connected devices is greater than 0. If the condition is met CONTINUE, else FAIL</small>                    |
| <small>3</small> | <small>GET Device.Hosts.HostNumberOfEntries to retrieve the total number of hosts in the host table</small>                                                         | <small>Verify host count is retrieved and greater than 0. If the condition is met CONTINUE, else FAIL</small>                           |
| <small>4</small> | <small>Loop through Device.Hosts.Host.{i}.Layer1Interface and Device.Hosts.Host.{i}.Active to identify an active LAN client with Ethernet Layer1 interface</small>  | <small>Verify an active LAN client is identified in the host table. If the condition is met CONTINUE, else FAIL</small>                 |
| <small>5</small> | <small>GET Device.Hosts.Host.{i}.IPv6Address.3.IPAddress for the identified active LAN client</small>                                                               | <small>Verify the IPv6 address of the active LAN client is populated in the host table. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 9: TS_IPV6_Check_ActiveWLANClient_IPv6Address</strong></summary>

## Test Case 9: TS_IPV6_Check_ActiveWLANClient_IPv6Address

## Objectives

Verify that the DUT's host table correctly records the global IPv6 address of an active WLAN client. The test confirms that there are active clients connected to the gateway, identifies an active WLAN client with a Device.WiFi.SSID Layer1 interface from the Device.Hosts table, and validates that its global IPv6 address is populated in the Device.Hosts.Host.{i}.IPv6Address table entry.

## Test Case ID

TC_IPV6_5

## Test Type

Positive

## Test Environment

| Component                                                  |
| ---------------------------------------------------------- |
| DUT - Device under test                  |
| WLAN client - Wireless LAN client |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                         | TDK Validation and Expected Results                                                                                                      |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small>         | <small>&nbsp;</small>                                                                                                                    |
| <small>2</small> | <small>GET Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber to get the number of active connected clients</small>                                                             | <small>Verify the number of connected devices is greater than 0. If the condition is met CONTINUE, else FAIL</small>                     |
| <small>3</small> | <small>GET Device.Hosts.HostNumberOfEntries to retrieve the total number of hosts in the host table</small>                                                                 | <small>Verify host count is retrieved and greater than 0. If the condition is met CONTINUE, else FAIL</small>                            |
| <small>4</small> | <small>Loop through Device.Hosts.Host.{i}.Layer1Interface and Device.Hosts.Host.{i}.Active to identify an active WLAN client with Device.WiFi.SSID Layer1 interface</small> | <small>Verify an active WLAN client is identified in the host table. If the condition is met CONTINUE, else FAIL</small>                 |
| <small>5</small> | <small>GET Device.Hosts.Host.{i}.IPv6Address.3.IPAddress for the identified active WLAN client</small>                                                                      | <small>Verify the IPv6 address of the active WLAN client is populated in the host table. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 10: TS_IPV6_CheckInternetConnectivity</strong></summary>

## Test Case 10: TS_IPV6_CheckInternetConnectivity

## Objectives

Verify that the DUT has end-to-end IPv6 internet connectivity. The test first confirms the DUT has a valid WAN IPv6 address via Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6, validates the address format, and then performs an IPv6 ping from the DUT to an external IPv6 host (www.google.com) to confirm active internet reachability over IPv6.

## Test Case ID

TC_IPV6_8

## Test Type

Positive

## Test Environment

| Component                                 |
| ----------------------------------------- |
| DUT - Device under test |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                      |
| <small>2</small> | <small>GET Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 to retrieve the WAN IPv6 address</small>                                                                        | <small>Verify WAN IPv6 address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small>              |
| <small>3</small> | <small>Validate that the retrieved WAN IPv6 address is in valid IPv6 format</small>                                                                                 | <small>Verify the retrieved IPv6 address is a valid IPv6 format. If the condition is met CONTINUE, else FAIL</small>       |
| <small>4</small> | <small>Execute the command to ping www.google.com to verify IPv6 internet connectivity</small>                                                                                | <small>Verify IPv6 ping to the external host succeeds with 0% packet loss. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 11: TS_IPV6_Check_RouterAdvertisement_LANPrefixConfiguration</strong></summary>

## Test Case 11: TS_IPV6_Check_RouterAdvertisement_LANPrefixConfiguration

## Objectives

Verify that Router Advertisement is enabled on the DUT and that the IPv6 prefix configured for advertisement on the LAN interface is consistent with the prefix actually configured on that interface. The test checks Device.RouterAdvertisement.Enable, retrieves the configured advertisement prefix from Device.RouterAdvertisement.InterfaceSetting.1.Prefixes, identifies the RA interface, and validates that the advertised prefix length matches the IPv6 prefix length configured on the interface.

## Test Case ID

TC_IPV6_9

## Test Type

Positive

## Test Environment

| Component                                 |
| ----------------------------------------- |
| DUT - Device under test |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                                                                                                      |
| <small>2</small> | <small>GET Device.RouterAdvertisement.Enable to check whether Router Advertisement is enabled</small>                                                               | <small>Verify Router Advertisement is enabled. If the condition is met CONTINUE, else FAIL</small>                                                                                                         |
| <small>3</small> | <small>GET Device.RouterAdvertisement.InterfaceSetting.1.Prefixes to retrieve the IPv6 prefix configured for advertisement</small>                                  | <small>Verify the IPv6 prefix configured for advertisement is obtained. If the condition is met CONTINUE, else FAIL</small>                                                                                |
| <small>4</small> | <small>GET Device.RouterAdvertisement.InterfaceSetting.1.Interface to retrieve the interface used for Router Advertisement</small>                                  | <small>Verify the Router Advertisement interface is obtained. If the condition is met CONTINUE, else FAIL</small>                                                                                          |
| <small>5</small> | <small>Run the command to extract the global IPv6 address and prefix length from the RA interface</small>                                                       | <small>Verify IPv6 address and prefix length on the RA interface are obtained. If the condition is met CONTINUE, else FAIL</small>                                                                         |
| <small>6</small> | <small>Compare the prefix length from Device.RouterAdvertisement.InterfaceSetting.1.Prefixes with the IPv6 prefix length configured on the RA interface</small>     | <small>Verify the prefix length from Device.RouterAdvertisement.InterfaceSetting.1.Prefixes matches the IPv6 prefix length configured on the RA interface. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 12: TS_IPV6_Check_DNSResolution_PrimaryIPv6Server</strong></summary>

## Test Case 12: TS_IPV6_Check_DNSResolution_PrimaryIPv6Server

## Objectives

Verify that the DUT can resolve domain names to IPv6 addresses using the Primary IPv6 DNS server. The test confirms the DUT has a WAN IPv6 address, retrieves the Primary IPv6 DNS server address from Device.DNS.Client.Server.1.DNSServer, performs a DNS resolution for a configured domain name using that DNS server, and validates that the resolved address is a valid IPv6 address.

## Test Case ID

TC_IPV6_10

## Test Type

Positive

## Test Environment

| Component                                 |
| ----------------------------------------- |
| DUT - Device under test |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                                       |
| <small>2</small> | <small>GET Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 to verify the DUT has a WAN IPv6 address</small>                                                                | <small>Verify DUT has a valid WAN IPv6 address. If the condition is met CONTINUE, else FAIL</small>                                         |
| <small>3</small> | <small>GET Device.DNS.Client.Server.1.DNSServer to retrieve the Primary IPv6 DNS server address</small>                                                             | <small>Verify Primary IPv6 DNS server address is obtained. If the condition is met CONTINUE, else FAIL</small>                              |
| <small>4</small> | <small>Run DNS resolution command for the configured domain name using the retrieved Primary IPv6 DNS server</small>                                                | <small>Verify the domain name is resolved successfully via the Primary IPv6 DNS server. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Validate that the resolved IP address is in valid IPv6 format</small>                                                                                        | <small>Verify the resolved IP address is a valid IPv6 format. If the condition is met PASS, else FAIL</small>                               |

</details>

---

<details>
<summary><strong>Test Case 13: TS_IPV6_Get_Brlan0IPv6LinkLocalAddress</strong></summary>

## Test Case 13: TS_IPV6_Get_Brlan0IPv6LinkLocalAddress

## Objectives

Verify that the LAN bridge interface brlan0 on the DUT auto-configures a valid link-local IPv6 address after the interface comes up. The test checks that brlan0 has an inet6 address with link-local scope and validates that the prefix length of the auto-configured link-local address is /64, confirming correct stateless address auto-configuration (SLAAC) on the LAN interface.

## Test Case ID

TC_IPV6_12

## Test Type

Positive

## Test Environment

| Component                                 |
| ----------------------------------------- |
| DUT - Device under test |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                                 |
| <small>2</small> | <small>Run the command to check for a link-local scope inet6 address on brlan0</small>                                                                       | <small>Verify brlan0 interface has inet6 address with link-local scope. If the condition is met CONTINUE, else FAIL</small>           |
| <small>3</small> | <small>Run the command to extract the link-local IPv6 address and prefix length from brlan0</small>                                                                | <small>Verify link-local IPv6 address and prefix length are obtained from brlan0. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Check that the link-local IPv6 address prefix length on brlan0 is /64</small>                                                                                | <small>Verify the link-local IPv6 address prefix length on brlan0 is /64. If the condition is met PASS, else FAIL</small>             |

</details>

---

<details>
<summary><strong>Test Case 14: TS_IPV6_Get_WANIPv6LinkLocalAddress</strong></summary>

## Test Case 14: TS_IPV6_Get_WANIPv6LinkLocalAddress

## Objectives

Verify that the WAN interface (erouter0) on the DUT auto-configures a valid link-local IPv6 address after the interface comes up. The test retrieves the WAN interface name from Device.DHCPv6.Client.1.Interface, checks the interface for a link-local scope IPv6 address, extracts the address and prefix, and validates that the prefix length of the auto-configured link-local address is /64.

## Test Case ID

TC_IPV6_13

## Test Type

Positive

## Test Environment

| Component                                 |
| ----------------------------------------- |
| DUT - Device under test |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                                            |
| <small>2</small> | <small>GET Device.DHCPv6.Client.1.Interface to retrieve the WAN interface name</small>                                                                              | <small>Verify WAN interface name is obtained successfully. If the condition is met CONTINUE, else FAIL</small>                                   |
| <small>3</small> | <small>Run the command to check for a link-local scope inet6 address on the WAN interface</small>                                                         | <small>Verify WAN interface has inet6 address with link-local scope. If the condition is met CONTINUE, else FAIL</small>                         |
| <small>4</small> | <small>Run the command to extract the link-local IPv6 address and prefix length from the WAN interface</small>                                                  | <small>Verify link-local IPv6 address and prefix length are obtained from the WAN interface. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Check that the link-local IPv6 address prefix length on the WAN interface is /64</small>                                                                     | <small>Verify the link-local IPv6 address prefix length on the WAN interface is /64. If the condition is met PASS, else FAIL</small>             |

</details>

---

<details>
<summary><strong>Test Case 15: TS_IPV6_Check_DHCPv6ClientStatus</strong></summary>

## Test Case 15: TS_IPV6_Check_DHCPv6ClientStatus

## Objectives

Validate that the DHCPv6 client on the DUT is enabled and in active operational status by default. The test checks that Device.DHCPv6.Client.1.Enable is set to "true" confirming the DHCPv6 client is administratively enabled, and that Device.DHCPv6.Client.1.Status reports "Enabled" confirming the client is operationally active and capable of obtaining IPv6 addresses.

## Test Case ID

TC_IPV6_18

## Test Type

Positive

## Test Environment

| Component                                 |
| ----------------------------------------- |
| DUT - Device under test |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                            |
| <small>2</small> | <small>GET Device.DHCPv6.Client.1.Enable to check the DHCPv6 client enable status</small>                                                                           | <small>Verify Device.DHCPv6.Client.1.Enable value is "true". If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.DHCPv6.Client.1.Status to check the DHCPv6 client operational status</small>                                                                      | <small>Verify Device.DHCPv6.Client.1.Status value is "Enabled". If the condition is met PASS, else FAIL</small>  |

</details>

---

</details>

---

<details>
<summary><strong>IPV6 - Behavioral Checks</strong></summary>

# IPV6 - Behavioral Checks

<details>
<summary><strong>Test Case 16: TS_IPV6_CheckIPV6Address_AfterReboot</strong></summary>

## Test Case 16: TS_IPV6_CheckIPV6Address_AfterReboot

## Objectives

Verify that the DUT re-acquires valid IPv6 addresses after a system reboot. The test records the current WAN IPv6 address using Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6, reboots the DUT, and then confirms that after the device recovers, a valid WAN IPv6 address is re-obtained via DHCPv6, ensuring IPv6 address recovery is automatic and seamless after a reboot.

## Test Case ID

TC_IPV6_6

## Test Type

Positive

## Test Environment

| Component                                 |
| ----------------------------------------- |
| DUT - Device under test |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                |
| <small>2</small> | <small>GET Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 to retrieve the current WAN IPv6 address before reboot</small>                                                  | <small>Verify WAN IPv6 address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small>        |
| <small>3</small> | <small>Validate that the WAN IPv6 address retrieved before reboot is in valid IPv6 format</small>                                                                   | <small>Verify the retrieved IPv6 address is a valid IPv6 format. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Reboot the DUT</small>                                                                                                                                       | <small>&nbsp;</small>                                                                                                |
| <small>5</small> | <small>GET Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 to retrieve the WAN IPv6 address after reboot</small>                                                           | <small>Verify WAN IPv6 address is re-acquired after reboot. If the condition is met CONTINUE, else FAIL</small>      |
| <small>6</small> | <small>Validate that the WAN IPv6 address re-acquired after reboot is in valid IPv6 format</small>                                                                  | <small>Verify the re-acquired IPv6 address is a valid IPv6 format. If the condition is met PASS, else FAIL</small>   |

</details>

---

<details>
<summary><strong>Test Case 17: TS_IPV6_CheckIPV6Address_AfterFR</strong></summary>

## Test Case 17: TS_IPV6_CheckIPV6Address_AfterFR

## Objectives

Verify that the DUT re-acquires a valid WAN IPv6 address after a Factory Reset. The test records the current WAN IPv6 address, triggers a Factory Reset via Device.X_CISCO_COM_DeviceControl.FactoryReset, waits for the device to recover, and then confirms that a valid WAN IPv6 address is re-obtained after the factory reset, ensuring IPv6 connectivity is automatically restored following a complete device reset.

## Test Case ID

TC_IPV6_7

## Test Type

Positive

## Test Environment

| Component                                 |
| ----------------------------------------- |
| DUT - Device under test |

## Test Configuration

| Parameter                                     | Value                      |
| --------------------------------------------- | -------------------------- |
| Device.X_CISCO_COM_DeviceControl.FactoryReset | Router,Wifi,VoIP,Dect,MoCA |

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                  |
| <small>2</small> | <small>GET Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 to retrieve the current WAN IPv6 address before Factory Reset</small>                                           | <small>Verify WAN IPv6 address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small>          |
| <small>3</small> | <small>Validate that the WAN IPv6 address retrieved before Factory Reset is in valid IPv6 format</small>                                                            | <small>Verify the retrieved IPv6 address is a valid IPv6 format. If the condition is met CONTINUE, else FAIL</small>   |
| <small>4</small> | <small>SET Device.X_CISCO_COM_DeviceControl.FactoryReset to "Router,Wifi,VoIP,Dect,MoCA" to trigger Factory Reset</small>                                           | <small>Verify Factory Reset is triggered successfully. If the condition is met CONTINUE, else FAIL</small>             |
| <small>5</small> | <small>GET Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 to retrieve the WAN IPv6 address after Factory Reset</small>                                                    | <small>Verify WAN IPv6 address is re-acquired after Factory Reset. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Validate that the WAN IPv6 address re-acquired after Factory Reset is in valid IPv6 format</small>                                                           | <small>Verify the re-acquired IPv6 address is a valid IPv6 format. If the condition is met PASS, else FAIL</small>     |

</details>

---

<details>
<summary><strong>Test Case 18: TS_IPV6_Get_DeviceMode_AfterFR</strong></summary>

## Test Case 18: TS_IPV6_Get_DeviceMode_AfterFR

## Objectives

Verify that the DUT operates in Dualstack mode by default after a Factory Reset. The test triggers a Factory Reset, waits for the device to recover, and then validates that: the device reports IPv6 capability (Device.IP.IPv6Capable is "true"), IPv6 is enabled (Device.IP.IPv6Enable is "true"), IPv6 status is "Enabled" (Device.IP.IPv6Status), a valid WAN IPv6 address is present, and the device mode is "Dualstack" (Device.X_CISCO_COM_DeviceControl.DeviceMode).

## Test Case ID

TC_IPV6_11

## Test Type

Positive

## Test Environment

| Component                                 |
| ----------------------------------------- |
| DUT - Device under test |

## Test Configuration

| Parameter                                     | Value                      |
| --------------------------------------------- | -------------------------- |
| Device.X_CISCO_COM_DeviceControl.FactoryReset | Router,Wifi,VoIP,Dect,MoCA |

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                           |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.FactoryReset to "Router,Wifi,VoIP,Dect,MoCA" to trigger Factory Reset on the DUT</small>                                | <small>Verify Factory Reset is triggered successfully. If the condition is met CONTINUE, else FAIL</small>                      |
| <small>3</small> | <small>GET Device.IP.IPv6Capable to check whether the device is IPv6 capable after Factory Reset</small>                                                            | <small>Verify Device.IP.IPv6Capable value is "true". If the condition is met CONTINUE, else FAIL</small>                        |
| <small>4</small> | <small>GET Device.IP.IPv6Enable to check whether IPv6 is enabled on the device after Factory Reset</small>                                                          | <small>Verify Device.IP.IPv6Enable value is "true". If the condition is met CONTINUE, else FAIL</small>                         |
| <small>5</small> | <small>GET Device.IP.IPv6Status to validate the IPv6 operational status after Factory Reset</small>                                                                 | <small>Verify Device.IP.IPv6Status value is "Enabled". If the condition is met CONTINUE, else FAIL</small>                      |
| <small>6</small> | <small>GET Device.DeviceInfo.X_COMCAST-COM_WAN_IPv6 to verify the DUT has a WAN IPv6 address after Factory Reset</small>                                            | <small>Verify WAN IPv6 address is available after Factory Reset. If the condition is met CONTINUE, else FAIL</small>            |
| <small>7</small> | <small>GET Device.X_CISCO_COM_DeviceControl.DeviceMode to verify the default device mode after Factory Reset</small>                                                | <small>Verify Device.X_CISCO_COM_DeviceControl.DeviceMode value is "Dualstack". If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 19: TS_IPV6_Check_Brlan0LinkLocalNeighborConnectivity_LANInterface</strong></summary>

## Test Case 19: TS_IPV6_Check_Brlan0LinkLocalNeighborConnectivity_LANInterface

## Objectives

Verify that the brlan0 LAN interface on the DUT can ping the link-local IPv6 address of an active wired LAN client connected to it. The test confirms that brlan0 has a valid link-local IPv6 address, identifies an active LAN client from the host table and retrieves its link-local IPv6 address via Device.Hosts.Host.{i}.IPv6Address.2.IPAddress, and then verifies that an IPv6 ping from brlan0 to the LAN client's link-local address succeeds.

## Test Case ID

TC_IPV6_14

## Test Type

Positive

## Test Environment

| Component                                                    |
| ------------------------------------------------------------ |
| DUT - Device under test                    |
| LAN Client - Wired Ethernet client connected to DUT LAN port |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                                                  |
| <small>2</small> | <small>Run the command to check for a link-local scope inet6 address on brlan0</small>                                                                       | <small>Verify brlan0 interface has inet6 address with link-local scope. If the condition is met CONTINUE, else FAIL</small>                            |
| <small>3</small> | <small>GET Device.Hosts.HostNumberOfEntries to retrieve the total number of hosts</small>                                                                           | <small>Verify host count is retrieved and greater than 0. If the condition is met CONTINUE, else FAIL</small>                                          |
| <small>4</small> | <small>Loop through Device.Hosts.Host.{i}.Layer1Interface and Device.Hosts.Host.{i}.Active to identify an active LAN client with Ethernet Layer1 interface</small>  | <small>Verify an active LAN client is identified in the host table. If the condition is met CONTINUE, else FAIL</small>                                |
| <small>5</small> | <small>GET Device.Hosts.Host.{i}.IPv6Address.2.IPAddress to retrieve the link-local IPv6 address of the active LAN client</small>                                   | <small>Verify the link-local IPv6 address of the active LAN client is obtained. If the condition is met CONTINUE, else FAIL</small>                    |
| <small>6</small> | <small>Run the command to ping the LAN client link-local IPv6 address from brlan0</small>                                                                           | <small>Verify IPv6 ping to the LAN client link-local address from brlan0 succeeds with 0% packet loss. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 20: TS_IPV6_Check_Brlan0LinkLocalNeighborConnectivity_WLANInterface</strong></summary>

## Test Case 20: TS_IPV6_Check_Brlan0LinkLocalNeighborConnectivity_WLANInterface

## Objectives

Verify that the brlan0 LAN interface on the DUT can ping the link-local IPv6 address of an active WLAN client connected to it. The test confirms that brlan0 has a valid link-local IPv6 address, identifies an active WLAN client from the host table and retrieves its link-local IPv6 address via Device.Hosts.Host.{i}.IPv6Address.2.IPAddress, and then verifies that an IPv6 ping from brlan0 to the WLAN client's link-local address succeeds.

## Test Case ID

TC_IPV6_15

## Test Type

Positive

## Test Environment

| Component                                                  |
| ---------------------------------------------------------- |
| DUT - Device under test                  |
| WLAN client - Wireless LAN client |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                         | TDK Validation and Expected Results                                                                                                                     |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small>         | <small>&nbsp;</small>                                                                                                                                   |
| <small>2</small> | <small>Run the command to check for a link-local scope inet6 address on brlan0</small>                                                                               | <small>Verify brlan0 interface has inet6 address with link-local scope. If the condition is met CONTINUE, else FAIL</small>                             |
| <small>3</small> | <small>GET Device.Hosts.HostNumberOfEntries to retrieve the total number of hosts</small>                                                                                   | <small>Verify host count is retrieved and greater than 0. If the condition is met CONTINUE, else FAIL</small>                                           |
| <small>4</small> | <small>Loop through Device.Hosts.Host.{i}.Layer1Interface and Device.Hosts.Host.{i}.Active to identify an active WLAN client with Device.WiFi.SSID Layer1 interface</small> | <small>Verify an active WLAN client is identified in the host table. If the condition is met CONTINUE, else FAIL</small>                                |
| <small>5</small> | <small>GET Device.Hosts.Host.{i}.IPv6Address.2.IPAddress to retrieve the link-local IPv6 address of the active WLAN client</small>                                          | <small>Verify the link-local IPv6 address of the active WLAN client is obtained. If the condition is met CONTINUE, else FAIL</small>                    |
| <small>6</small> | <small>Run the command to ping the WLAN client link-local IPv6 address from brlan0</small>                                                                                  | <small>Verify IPv6 ping to the WLAN client link-local address from brlan0 succeeds with 0% packet loss. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 21: TS_IPV6_Check_PingToLANClientGlobalIPv6</strong></summary>

## Test Case 21: TS_IPV6_Check_PingToLANClientGlobalIPv6

## Objectives

Verify that the DUT can reach a wired LAN client using the client's global IPv6 address over the delegated LAN prefix. The test confirms both the WAN interface and brlan0 LAN interface have global IPv6 addresses, identifies an active LAN client from the host table, retrieves the LAN client's global IPv6 address via Device.Hosts.Host.{i}.IPv6Address.3.IPAddress, and verifies that an IPv6 ping from the DUT to the LAN client's global address succeeds.

## Test Case ID

TC_IPV6_16

## Test Type

Positive

## Test Environment

| Component                                                    |
| ------------------------------------------------------------ |
| DUT - Device under test                    |
| LAN Client - Wired Ethernet client connected to DUT LAN port |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                 | TDK Validation and Expected Results                                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small> | <small>&nbsp;</small>                                                                                                                  |
| <small>2</small> | <small>GET Device.DHCPv6.Client.1.Interface to retrieve the WAN interface name</small>                                                                              | <small>Verify WAN interface name is obtained successfully. If the condition is met CONTINUE, else FAIL</small>                         |
| <small>3</small> | <small>Run the command to check for a global scope inet6 address on the WAN interface</small>                                                             | <small>Verify WAN interface has inet6 address with global scope. If the condition is met CONTINUE, else FAIL</small>                   |
| <small>4</small> | <small>Run the command to check for a global scope inet6 address on brlan0</small>                                                                           | <small>Verify brlan0 interface has inet6 address with global scope. If the condition is met CONTINUE, else FAIL</small>                |
| <small>5</small> | <small>GET Device.Hosts.HostNumberOfEntries to retrieve the total number of hosts</small>                                                                           | <small>Verify host count is retrieved and greater than 0. If the condition is met CONTINUE, else FAIL</small>                          |
| <small>6</small> | <small>Loop through Device.Hosts.Host.{i}.Layer1Interface and Device.Hosts.Host.{i}.Active to identify an active LAN client with Ethernet Layer1 interface</small>  | <small>Verify an active LAN client is identified in the host table. If the condition is met CONTINUE, else FAIL</small>                |
| <small>7</small> | <small>GET Device.Hosts.Host.{i}.IPv6Address.3.IPAddress to retrieve the global IPv6 address of the active LAN client</small>                                       | <small>Verify the global IPv6 address of the active LAN client is obtained. If the condition is met CONTINUE, else FAIL</small>        |
| <small>8</small> | <small>Run the command to ping the LAN client global IPv6 address from the DUT</small>                                                                              | <small>Verify IPv6 ping to the LAN client global address succeeds with 0% packet loss. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 22: TS_IPV6_Check_PingToWLANClientGlobalIPv6</strong></summary>

## Test Case 22: TS_IPV6_Check_PingToWLANClientGlobalIPv6

## Objectives

Verify that the DUT can reach a WLAN client using the client's global IPv6 address over the delegated LAN prefix. The test confirms both the WAN interface and brlan0 LAN interface have global IPv6 addresses, identifies an active WLAN client from the host table, retrieves the WLAN client's global IPv6 address via Device.Hosts.Host.{i}.IPv6Address.3.IPAddress, and verifies that an IPv6 ping from the DUT to the WLAN client's global address succeeds.

## Test Case ID

TC_IPV6_17

## Test Type

Positive

## Test Environment

| Component                                                  |
| ---------------------------------------------------------- |
| DUT - Device under test                  |
| WLAN client - Wireless LAN client |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number      | DUT                                                                                                                                                                         | TDK Validation and Expected Results                                                                                                     |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| <small>1</small> | <small>Precondition: An IPv6 environment must be available. If native IPv6 connectivity is unavailable, the IPv6 Simulator Setup must be set up and running</small>         | <small>&nbsp;</small>                                                                                                                   |
| <small>2</small> | <small>GET Device.DHCPv6.Client.1.Interface to retrieve the WAN interface name</small>                                                                                      | <small>Verify WAN interface name is obtained successfully. If the condition is met CONTINUE, else FAIL</small>                          |
| <small>3</small> | <small>Run the command to check for a global scope inet6 address on the WAN interface</small>                                                                     | <small>Verify WAN interface has inet6 address with global scope. If the condition is met CONTINUE, else FAIL</small>                    |
| <small>4</small> | <small>Run the command to check for a global scope inet6 address on brlan0</small>                                                                                   | <small>Verify brlan0 interface has inet6 address with global scope. If the condition is met CONTINUE, else FAIL</small>                 |
| <small>5</small> | <small>GET Device.Hosts.HostNumberOfEntries to retrieve the total number of hosts</small>                                                                                   | <small>Verify host count is retrieved and greater than 0. If the condition is met CONTINUE, else FAIL</small>                           |
| <small>6</small> | <small>Loop through Device.Hosts.Host.{i}.Layer1Interface and Device.Hosts.Host.{i}.Active to identify an active WLAN client with Device.WiFi.SSID Layer1 interface</small> | <small>Verify an active WLAN client is identified in the host table. If the condition is met CONTINUE, else FAIL</small>                |
| <small>7</small> | <small>GET Device.Hosts.Host.{i}.IPv6Address.3.IPAddress to retrieve the global IPv6 address of the active WLAN client</small>                                              | <small>Verify the global IPv6 address of the active WLAN client is obtained. If the condition is met CONTINUE, else FAIL</small>        |
| <small>8</small> | <small>Run the command to ping the WLAN client global IPv6 address from the DUT</small>                                                                                     | <small>Verify IPv6 ping to the WLAN client global address succeeds with 0% packet loss. If the condition is met PASS, else FAIL</small> |

</details>

---

</details>

---

</details>

---

<details>
<summary><strong>Firewall</strong></summary>

# FIREWALL

<details>
<summary><strong>Test Case 1: FTP from LAN to WAN with Custom Firewall</strong></summary>

## Test Case 1: E2E_Firewall_Custom_FtpFromLanToWan

### Objectives
Verify that when Firewall Config is set to Custom FTP access from LAN to WAN should not be blocked
### Test Type
Positive
To check if the PT rule doesn't take effect and inbound traffic is not let through, if the trigger is sent using incorrect protocol.
### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Custom |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Custom and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Initiate FTP connection to the WAN client</small> | <small>Receive FTP connection from LAN client</small> | <small>FTP from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |


</details>

---

<details>
<summary><strong>Test Case 2: HTTP from LAN to WAN with Custom Firewall</strong></summary>

## Test Case 2: E2E_Firewall_Custom_HttpFromLanToWan

### Objectives
Verify that when Firewall Config is set to Custom HTTP access from LAN to WAN should not be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Custom |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Custom and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Send HTTP request to the WAN server</small> | <small>Receive HTTP request from LAN client</small> | <small>HTTP access from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 3: HTTPS from LAN to WAN with Custom Firewall</strong></summary>

## Test Case 3: E2E_Firewall_Custom_HttpsFromLanToWan

### Objectives
Verify that when Firewall Config is set to Custom HTTPS access from LAN to WAN should not be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Custom |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Custom and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Send HTTPS request to the WAN server</small> | <small>Receive HTTPS request from LAN client</small> | <small>HTTPS access from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 4: Ping from LAN to WAN with Custom Firewall</strong></summary>

## Test Case 4: E2E_Firewall_Custom_PingFromLanToWan

### Objectives
Verify that when Firewall Config is set to Custom Ping access from LAN to WAN should not be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Custom |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Custom and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Send Ping to the WAN host</small> |  | <small>Ping from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>6</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 5: SSH to WAN from LAN and WLAN with Custom Firewall</strong></summary>

## Test Case 5: E2E_Firewall_Custom_SSHToWAN_FromLANAndWLAN

### Objectives
Verify that when Firewall Config is set to Custom SSH access from LAN to WAN and WLAN to WAN should  be success
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Custom |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Custom; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  |  | <small>Both WLAN and LAN client IP addresses are in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  |  | <small>Static route added in WLAN client. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>8</small> |  | <small>Initiate SSH connection to the WAN client</small> |  | <small>Receive SSH connection from WLAN client</small> | <small>SSH from WLAN to WAN is successful. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>9</small> |  | <small>Delete the added static route</small> |  |  |  |
| <small>10</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |  |
| <small>11</small> |  |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added in LAN client. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>12</small> |  |  | <small>Initiate SSH connection to the WAN client</small> | <small>Receive SSH connection from LAN client</small> | <small>SSH from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>13</small> |  |  | <small>Delete the added static route</small> |  |  |
| <small>14</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 6: Telnet from LAN to WAN with Custom Firewall</strong></summary>

## Test Case 6: E2E_Firewall_Custom_TelnetFromLanToWan

### Objectives
Verify that when Firewall Config is set to Custom Telnet access from LAN to WAN should succeed
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Custom |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Custom and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Initiate Telnet connection to the WAN client</small> | <small>Receive Telnet connection from LAN client</small> | <small>Telnet from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 7: FTP from LAN to WAN with High Firewall</strong></summary>

## Test Case 7: E2E_Firewall_High_FtpFromLanToWan

### Objectives
Verify that when Firewall Config is set to High FTP access from LAN to WAN should  be blocked
### Test Type
Negative

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to High and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Initiate FTP connection to the WAN client</small> | <small>Receive FTP connection from LAN client</small> | <small>FTP from LAN to WAN is blocked. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 8: FTP from WLAN to LAN with High Firewall</strong></summary>

## Test Case 8: E2E_Firewall_High_FtpFromWlanToLan

### Objectives
Verify that when Firewall Config is set to High FTP access from WLAN to LAN should be allowed
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to High; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Initiate FTP connection to the LAN client</small> | <small>Receive FTP connection from WLAN client</small> | <small>FTP from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 9: FTP from WLAN to WAN with High Firewall</strong></summary>

## Test Case 9: E2E_Firewall_High_FtpFromWlanToWan

### Objectives
Verify that when Firewall Config is set to High FTP access from WLAN to WAN should be blocked
### Test Type
Negative

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to High; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>WLAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Initiate FTP connection to the WAN client</small> | <small>Receive FTP connection from WLAN client</small> | <small>FTP from WLAN to WAN is blocked. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Delete the added static route</small> |  |  |
| <small>9</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>10</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 10: HTTP from LAN to WAN with High Firewall</strong></summary>

## Test Case 10: E2E_Firewall_High_HttpFromLanToWan

### Objectives
Verify that when Firewall Config is set to High HTTP access from LAN to WAN should not be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to High and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Send HTTP request to the WAN server</small> | <small>Receive HTTP request from LAN client</small> | <small>HTTP access from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 11: HTTP from WLAN to LAN with High Firewall</strong></summary>

## Test Case 11: E2E_Firewall_High_HttpFromWlanToLan

### Objectives
Verify that when Firewall Config is set to High HTTP traffic from WLAN to LAN should pass through
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to High; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send HTTP request to the LAN client</small> | <small>Receive HTTP request from WLAN client</small> | <small>HTTP access from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 12: HTTP from WLAN to WAN with High Firewall</strong></summary>

## Test Case 12: E2E_Firewall_High_HttpFromWlanToWan

### Objectives
Verify that when Firewall Config is set to High HTTP traffic from WLAN to WAN should pass through
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to High; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>WLAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send HTTP request to the WAN server</small> | <small>Receive HTTP request from WLAN client</small> | <small>HTTP access from WLAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Delete the added static route</small> |  |  |
| <small>9</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>10</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 13: HTTPS from LAN to WAN with High Firewall</strong></summary>

## Test Case 13: E2E_Firewall_High_HttpsFromLanToWan

### Objectives
Verify that when Firewall Config is set to High HTTPS access from LAN to WAN should not be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to High and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Send HTTPS request to the WAN server</small> | <small>Receive HTTPS request from LAN client</small> | <small>HTTPS access from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 14: HTTPS from WLAN to LAN with High Firewall</strong></summary>

## Test Case 14: E2E_Firewall_High_HttpsFromWlanToLan

### Objectives
Verify that when Firewall Config is set to High HTTPS traffic from WLAN to LAN should pass through
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to High; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send HTTPS request to the LAN client</small> | <small>Receive HTTPS request from WLAN client</small> | <small>HTTPS access from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 15: HTTPS from WLAN to WAN with High Firewall</strong></summary>

## Test Case 15: E2E_Firewall_High_HttpsFromWlanToWan

### Objectives
Verify that when Firewall Config is set to High HTTPS traffic from WLAN to WAN should pass through
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to High; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>WLAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send HTTPS request to the WAN server</small> | <small>Receive HTTPS request from WLAN client</small> | <small>HTTPS access from WLAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Delete the added static route</small> |  |  |
| <small>9</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>10</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 16: Ping from LAN to WAN with High Firewall</strong></summary>

## Test Case 16: E2E_Firewall_High_PingFromLanToWan

### Objectives
Verify that when Firewall Config is set to High Ping access from LAN to WAN should be blocked
### Test Type
Negative

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to High and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Send Ping to the WAN host</small> |  | <small>Ping from LAN to WAN is blocked. If the condition is met, then PASS else FAIL.</small> |
| <small>6</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 17: Ping from WLAN to LAN with High Firewall</strong></summary>

## Test Case 17: E2E_Firewall_High_PingFromWlanToLan

### Objectives
Verify that when Firewall Config is set to High ICMP message from WLAN to LAN should be allowed
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to High; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send Ping to the LAN client</small> |  | <small>Ping from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 18: Ping from WLAN to WAN with High Firewall</strong></summary>

## Test Case 18: E2E_Firewall_High_PingFromWlanToWan

### Objectives
Verify that when Firewall Config is set to High ICMP message from WLAN to WAN should be blocked
### Test Type
Negative

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to High; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>WLAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Send Ping to the WAN host</small> |  | <small>Ping from WLAN to WAN is blocked. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>8</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 19: SSH to WAN from LAN and WLAN with High Firewall</strong></summary>

## Test Case 19: E2E_Firewall_High_SSHToWAN_FromLANAndWLAN

### Objectives
Verify that when Firewall Config is set to High SSH access from LAN to WAN and WLAN to WAN should  be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  |  | <small>WiFi parameters set as per test configuration and firewall level set to High; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  |  | <small>Both WLAN and LAN client IP addresses are in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  |  | <small>Static route added in WLAN client. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>8</small> |  | <small>Initiate SSH connection to the WAN client</small> |  | <small>Receive SSH connection from WLAN client</small> | <small>SSH from WLAN to WAN is blocked. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>9</small> |  | <small>Delete the added static route</small> |  |  |  |
| <small>10</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |  |
| <small>11</small> |  |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added in LAN client. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>12</small> |  |  | <small>Initiate SSH connection to the WAN client</small> | <small>Receive SSH connection from LAN client</small> | <small>SSH from LAN to WAN is blocked. If the condition is met, then PASS else FAIL.</small> |
| <small>13</small> |  |  | <small>Delete the added static route</small> |  |  |
| <small>14</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 20: Telnet from LAN to WAN with High Firewall</strong></summary>

## Test Case 20: E2E_Firewall_High_TelnetFromLanToWan

### Objectives
Verify that when Firewall Config is set to High Telnet access from LAN to WAN should be blocked
### Test Type
Negative

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to High and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Initiate Telnet connection to the WAN client</small> | <small>Receive Telnet connection from LAN client</small> | <small>Telnet from LAN to WAN is blocked. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 21: Telnet from WLAN to LAN with High Firewall</strong></summary>

## Test Case 21: E2E_Firewall_High_TelnetFromWlanToLan

### Objectives
Verify that when Firewall Config is set to High Telnet access from WLAN to LAN should be allowed
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to High; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Initiate Telnet connection to the LAN client</small> | <small>Receive Telnet connection from WLAN client</small> | <small>Telnet from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 22: Telnet from WLAN to WAN with High Firewall</strong></summary>

## Test Case 22: E2E_Firewall_High_TelnetFromWlanToWan

### Objectives
Verify that when Firewall Config is set to High Telnet from WLAN to WAN should be blocked
### Test Type
Negative

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | High |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to High; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>WLAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Initiate Telnet connection to the WAN client</small> | <small>Receive Telnet connection from WLAN client</small> | <small>Telnet from WLAN to WAN is blocked. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Delete the added static route</small> |  |  |
| <small>9</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>10</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 23: FTP from LAN to WAN with Low Firewall</strong></summary>

## Test Case 23: E2E_Firewall_Low_FtpFromLanToWan

### Objectives
Verify that when Firewall Config is set to Low FTP access from LAN to WAN should not be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Low and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Initiate FTP connection to the WAN client</small> | <small>Receive FTP connection from LAN client</small> | <small>FTP from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 24: FTP from WLAN to LAN with Low Firewall</strong></summary>

## Test Case 24: E2E_Firewall_Low_FtpFromWlanToLan

### Objectives
Verify that when Firewall Config is set to Low FTP access from WLAN to LAN should be allowed
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Low; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Initiate FTP connection to the LAN client</small> | <small>Receive FTP connection from WLAN client</small> | <small>FTP from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 25: FTP from WLAN to WAN with Low Firewall</strong></summary>

## Test Case 25: E2E_Firewall_Low_FtpFromWlanToWan

### Objectives
Verify that when Firewall Config is set to Low FTP access from WLAN to WAN should passthrough
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Low; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>WLAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Initiate FTP connection to the WAN client</small> | <small>Receive FTP connection from WLAN client</small> | <small>FTP from WLAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Delete the added static route</small> |  |  |
| <small>9</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>10</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 26: HTTP from LAN to WAN with Low Firewall</strong></summary>

## Test Case 26: E2E_Firewall_Low_HttpFromLanToWan

### Objectives
Verify that when Firewall Config is set to Low HTTP access from LAN to WAN should not be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Low and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Send HTTP request to the WAN server</small> | <small>Receive HTTP request from LAN client</small> | <small>HTTP access from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 27: HTTP from WLAN to LAN with Low Firewall</strong></summary>

## Test Case 27: E2E_Firewall_Low_HttpFromWlanToLan

### Objectives
Verify that when Firewall Config is set to Low HTTP traffic from WLAN to LAN should pass through
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Low; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send HTTP request to the LAN client</small> | <small>Receive HTTP request from WLAN client</small> | <small>HTTP access from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 28: HTTP from WLAN to WAN with Low Firewall</strong></summary>

## Test Case 28: E2E_Firewall_Low_HttpFromWlanToWan

### Objectives
Verify that when Firewall Config is set to Low HTTP traffic from WLAN to WAN should pass through
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Low; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>WLAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send HTTP request to the WAN server</small> | <small>Receive HTTP request from WLAN client</small> | <small>HTTP access from WLAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Delete the added static route</small> |  |  |
| <small>9</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>10</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 29: HTTPS from LAN to WAN with Low Firewall</strong></summary>

## Test Case 29: E2E_Firewall_Low_HttpsFromLanToWan

### Objectives
Verify that when Firewall Config is set to Low HTTPS access from LAN to WAN should not be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Low and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Send HTTPS request to the WAN server</small> | <small>Receive HTTPS request from LAN client</small> | <small>HTTPS access from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 30: HTTPS from WLAN to LAN with Low Firewall</strong></summary>

## Test Case 30: E2E_Firewall_Low_HttpsFromWlanToLan

### Objectives
Verify that when Firewall Config is set to Low HTTPS traffic from WLAN to LAN should pass through
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Low; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send HTTPS request to the LAN client</small> | <small>Receive HTTPS request from WLAN client</small> | <small>HTTPS access from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 31: HTTPS from WLAN to WAN with Low Firewall</strong></summary>

## Test Case 31: E2E_Firewall_Low_HttpsFromWlanToWan

### Objectives
Verify that when Firewall Config is set to Low HTTPS traffic from WLAN to WAN should pass through
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Low; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>WLAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send HTTPS request to the WAN server</small> | <small>Receive HTTPS request from WLAN client</small> | <small>HTTPS access from WLAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Delete the added static route</small> |  |  |
| <small>9</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>10</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 32: Ping from LAN to WAN with Low Firewall</strong></summary>

## Test Case 32: E2E_Firewall_Low_PingFromLanToWan

### Objectives
Verify that when Firewall Config is set to Low Ping access from LAN to WAN should not be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Low and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Send Ping to the WAN host</small> |  | <small>Ping from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>6</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 33: Ping from WLAN to LAN with Low Firewall</strong></summary>

## Test Case 33: E2E_Firewall_Low_PingFromWlanToLan

### Objectives
Verify that when Firewall Config is set to Low ICMP message from WLAN to LAN should be allowed
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Low; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send Ping to the LAN client</small> |  | <small>Ping from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 34: Ping from WLAN to WAN with Low Firewall</strong></summary>

## Test Case 34: E2E_Firewall_Low_PingFromWlanToWan

### Objectives
Verify that when Firewall Config is set to Low ICMP message from WLAN to WAN IP of gateway should pass through
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Low; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>WLAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Send Ping to the WAN host</small> |  | <small>Ping from WLAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>8</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 35: SSH to WAN from LAN and WLAN with Low Firewall</strong></summary>

## Test Case 35: E2E_Firewall_Low_SSHToWAN_FromLANAndWLAN

### Objectives
Verify that when Firewall Config is set to Low SSH access from LAN to WAN and WLAN to WAN should  be success
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Low; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  |  | <small>Both WLAN and LAN client IP addresses are in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  |  | <small>Static route added in WLAN client. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>8</small> |  | <small>Initiate SSH connection to the WAN client</small> |  | <small>Receive SSH connection from WLAN client</small> | <small>SSH from WLAN to WAN is successful. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>9</small> |  | <small>Delete the added static route</small> |  |  |  |
| <small>10</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |  |
| <small>11</small> |  |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added in LAN client. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>12</small> |  |  | <small>Initiate SSH connection to the WAN client</small> | <small>Receive SSH connection from LAN client</small> | <small>SSH from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>13</small> |  |  | <small>Delete the added static route</small> |  |  |
| <small>14</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 36: Telnet from LAN to WAN with Low Firewall</strong></summary>

## Test Case 36: E2E_Firewall_Low_TelnetFromLanToWan

### Objectives
Verify that when Firewall Config is set to Low Telnet access from LAN to WAN should be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Low and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Initiate Telnet connection to the WAN client</small> | <small>Receive Telnet connection from LAN client</small> | <small>Telnet from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 37: Telnet from WLAN to LAN with Low Firewall</strong></summary>

## Test Case 37: E2E_Firewall_Low_TelnetFromWlanToLan

### Objectives
Verify that when Firewall Config is set to Low Telnet access from WLAN to LAN should be allowed
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Low |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Low; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Initiate Telnet connection to the LAN client</small> | <small>Receive Telnet connection from WLAN client</small> | <small>Telnet from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 38: FTP from LAN to WAN with Medium Firewall</strong></summary>

## Test Case 38: E2E_Firewall_Medium_FtpFromLanToWan

### Objectives
Verify that when Firewall Config is set to Medium FTP access from LAN to WAN should not be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Medium and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Initiate FTP connection to the WAN client</small> | <small>Receive FTP connection from LAN client</small> | <small>FTP from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 39: FTP from WLAN to LAN with Medium Firewall</strong></summary>

## Test Case 39: E2E_Firewall_Medium_FtpFromWlanToLan

### Objectives
Verify that when Firewall Config is set to Medium FTP access from WLAN to LAN should be allowed
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Medium; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Initiate FTP connection to the LAN client</small> | <small>Receive FTP connection from WLAN client</small> | <small>FTP from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 40: HTTP from LAN to WAN with Medium Firewall</strong></summary>

## Test Case 40: E2E_Firewall_Medium_HttpFromLanToWan

### Objectives
Verify that when Firewall Config is set to Medium HTTP access from LAN to WAN should not be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Medium and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Send HTTP request to the WAN server</small> | <small>Receive HTTP request from LAN client</small> | <small>HTTP access from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 41: HTTP from WLAN to LAN with Medium Firewall</strong></summary>

## Test Case 41: E2E_Firewall_Medium_HttpFromWlanToLan

### Objectives
Verify that when Firewall Config is set to Medium HTTP access from WLAN to LAN should pass through
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Medium; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send HTTP request to the LAN client</small> | <small>Receive HTTP request from WLAN client</small> | <small>HTTP access from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 42: HTTP from WLAN to WAN with Medium Firewall</strong></summary>

## Test Case 42: E2E_Firewall_Medium_HttpFromWlanToWan

### Objectives
Verify that when Firewall Config is set to High HTTP traffic from WLAN to WAN should pass through
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Medium; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>WLAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send HTTP request to the WAN server</small> | <small>Receive HTTP request from WLAN client</small> | <small>HTTP access from WLAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Delete the added static route</small> |  |  |
| <small>9</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>10</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 43: HTTPS from LAN to WAN with Medium Firewall</strong></summary>

## Test Case 43: E2E_Firewall_Medium_HttpsFromLanToWan

### Objectives
Verify that when Firewall Config is set to Medium HTTPS access from LAN to WAN should not be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Medium and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Send HTTPS request to the WAN server</small> | <small>Receive HTTPS request from LAN client</small> | <small>HTTPS access from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 44: HTTPS from WLAN to LAN with Medium Firewall</strong></summary>

## Test Case 44: E2E_Firewall_Medium_HttpsFromWlanToLan

### Objectives
Verify that when Firewall Config is set to Medium HTTPS access from WLAN to LAN should pass through
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Medium; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send HTTPS request to the LAN client</small> | <small>Receive HTTPS request from WLAN client</small> | <small>HTTPS access from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 45: HTTPS from WLAN to WAN with Medium Firewall</strong></summary>

## Test Case 45: E2E_Firewall_Medium_HttpsFromWlanToWan

### Objectives
Verify that when Firewall Config is set to Medium HTTPS traffic from WLAN to WAN should pass through
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Medium; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>WLAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send HTTPS request to the WAN server</small> | <small>Receive HTTPS request from WLAN client</small> | <small>HTTPS access from WLAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Delete the added static route</small> |  |  |
| <small>9</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>10</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 46: Ping from LAN to WAN with Medium Firewall</strong></summary>

## Test Case 46: E2E_Firewall_Medium_PingFromLanToWan

### Objectives
Verify that when Firewall Config is set to Medium Ping access from LAN to WAN should not be blocked
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Medium and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Send Ping to the WAN host</small> |  | <small>Ping from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>6</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 47: Ping from WLAN to LAN with Medium Firewall</strong></summary>

## Test Case 47: E2E_Firewall_Medium_PingFromWlanToLan

### Objectives
Verify that when Firewall Config is set to Medium ICMP message from WLAN to LAN should be allowed
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Medium; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Send Ping to the LAN client</small> |  | <small>Ping from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 48: Ping from WLAN to WAN with Medium Firewall</strong></summary>

## Test Case 48: E2E_Firewall_Medium_PingFromWlanToWan

### Objectives
Verify that when Firewall Config is set to Medium ICMP message from WLAN to WAN should pass through
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Medium; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>WLAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Send Ping to the WAN host</small> |  | <small>Ping from WLAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>8</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 49: SSH to WAN from LAN and WLAN with Medium Firewall</strong></summary>

## Test Case 49: E2E_Firewall_Medium_SSHToWAN_FromLANAndWLAN

### Objectives
Verify that when Firewall Config is set to Medium SSH access from LAN to WAN and WLAN to WAN should  be success
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Medium; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Connect to the configured WiFi SSID</small> |  |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  | <small>Get the WLAN client IP address</small> |  |  | <small>WLAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  |  | <small>Both WLAN and LAN client IP addresses are in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  |  | <small>Static route added in WLAN client. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>8</small> |  | <small>Initiate SSH connection to the WAN client</small> |  | <small>Receive SSH connection from WLAN client</small> | <small>SSH from WLAN to WAN is successful. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>9</small> |  | <small>Delete the added static route</small> |  |  |  |
| <small>10</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |  |
| <small>11</small> |  |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added in LAN client. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>12</small> |  |  | <small>Initiate SSH connection to the WAN client</small> | <small>Receive SSH connection from LAN client</small> | <small>SSH from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>13</small> |  |  | <small>Delete the added static route</small> |  |  |
| <small>14</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 50: Telnet from LAN to WAN with Medium Firewall</strong></summary>

## Test Case 50: E2E_Firewall_Medium_TelnetFromLanToWan

### Objectives
Verify that when Firewall Config is set to Medium Telnet access from LAN to WAN is success
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| LAN Client - Wired client |
| WAN - WAN system |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

### Test Procedure and Expected Results
| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|-------------|-----|------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the firewall level using Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET the firewall level to the desired value using Device.X_CISCO_COM_Security_Firewall.FirewallLevel</small> |  |  | <small>Firewall level set to Medium and verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> |  | <small>Get the LAN client IP address</small> |  | <small>LAN client IP address obtained. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>LAN client IP address is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Add a static route to route traffic via the DUT to the WAN client</small> |  | <small>Static route added successfully. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Initiate Telnet connection to the WAN client</small> | <small>Receive Telnet connection from LAN client</small> | <small>Telnet from LAN to WAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>7</small> |  | <small>Delete the added static route</small> |  |  |
| <small>8</small> | <small>Revert firewall level, Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---
<details>
<summary><strong>Test Case 51: Telnet from WLAN to LAN with Medium Firewall</strong></summary>

## Test Case 51: E2E_Firewall_Medium_TelnetFromWlanToLan

### Objectives
Verify that when Firewall Config is set to Medium Telnet access from WLAN to LAN should be allowed
### Test Type
Positive

### Test Environment
| Component |
|-----------|
| Broadband residential gateway (RDKB) |
| WLAN Client - Wireless client |
| LAN Client - Wired client |

### Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.WiFi.SSID.{i}.SSID | As per test configuration |
| Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase | As per test configuration |
| Device.WiFi.Radio.{i}.Enable | true |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | Medium |

### Test Procedure and Expected Results
| Step Number | DUT | WLAN Client | LAN Client | TDK Validation and Expected Results |
|-------------|-----|-------------|------------|-------------------------------------|
| <small>1</small> | <small>GET the initial WiFi configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel</small> |  |  | <small>Current WiFi parameters and firewall level retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>2</small> | <small>SET to custom WiFi test configuration - Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Radio enable - Device.WiFi.Radio.{i}.Enable to true, and Firewall level - Device.X_CISCO_COM_Security.Firewall.FirewallLevel to {fw_level}</small> |  |  | <small>WiFi parameters set as per test configuration and firewall level set to Medium; verified via GET. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>3</small> | <small>GET gateway's LAN management IP Address - Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> |  |  | <small>Gateway LAN IP address retrieved. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>4</small> |  |  | <small>Get the LAN client IP address</small> | <small>LAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>5</small> |  | <small>Connect to the configured WiFi SSID</small> |  | <small>WLAN client connected to WiFi SSID. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>6</small> |  | <small>Get the WLAN client IP address</small> |  | <small>WLAN client IP address obtained and is in the expected DHCP range. If the condition is met, then CONTINUE else FAIL.</small> |
| <small>7</small> |  | <small>Initiate Telnet connection to the LAN client</small> | <small>Receive Telnet connection from WLAN client</small> | <small>Telnet from WLAN to LAN is successful. If the condition is met, then PASS else FAIL.</small> |
| <small>8</small> |  | <small>Disconnect from the WiFi SSID</small> |  |  |
| <small>9</small> | <small>Revert the WiFi configuration to initial state using Device.WiFi.SSID.{i}.SSID, Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase, Device.WiFi.Radio.{i}.Enable, and Firewall level should be reset using Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value</small> |  |  |  |

</details>

---

</details>

---

<details>
<summary><strong>Cellular Manager</strong></summary>

# Cellular Manager

<details>
<summary><strong>Status and Parameter Validation</strong></summary>

# Status and Parameter Validation

<details>
<summary><strong>Test Case 1: Verify X_RDK_Status transitions to DEREGISTERED/CONNECTED on interface disable/enable</strong></summary>

## Test Case 1: TS_CellularManager_CheckCellularX_RDK_Status

## Objectives
Verify that Device.Cellular.X_RDK_Status correctly reports DEREGISTERED when the cellular interface is disabled and CONNECTED when the interface is re-enabled. The test disables the cellular interface, confirms DEREGISTERED status, re-enables it, and confirms CONNECTED status.

## Test Case ID
TC_CellularManager_1

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Cellular.Interface.1.Enable | false (to trigger DEREGISTERED), true (to trigger CONNECTED) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If Device.Cellular.Interface.1.Enable is true, SET Device.Cellular.Interface.1.Enable to false</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to false. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Wait 20 seconds for the cellular interface to transition to DEREGISTERED state</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is DEREGISTERED. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>SET Device.Cellular.Interface.1.Enable to true</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to true. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Wait 20 seconds for the cellular interface to reconnect</small> | <small>&nbsp;</small> |
| <small>7</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is CONNECTED. If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>Cleanup: Revert Device.Cellular.Interface.1.Enable to original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 2: Verify key cellular parameters report expected values when CONNECTED</strong></summary>

## Test Case 2: TS_CellularManager_CheckParametersValue_CONNECTED

## Objectives
Verify that key cellular data model parameters report correct values when the cellular manager status is CONNECTED. The test confirms that Device.Cellular.X_RDK_Enable is true, Device.Cellular.Interface.1.Enable is true, Device.Cellular.Interface.1.X_RDK_RadioEnvConditions is one of FAIR/EXCELLENT/POOR/GOOD, Device.Cellular.Interface.1.X_RDK_Identification.Imei is non-empty, and Device.Cellular.Interface.1.Status is Up.

## Test Case ID
TC_CellularManager_6

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Cellular.Interface.1.Enable | true (if not already enabled) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If Device.Cellular.Interface.1.Enable is false, SET to true; wait 20 seconds</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to true. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is CONNECTED. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Cellular.X_RDK_Enable from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Enable is true. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify Device.Cellular.Interface.1.Enable is true. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.Cellular.Interface.1.X_RDK_RadioEnvConditions from the DUT</small> | <small>Verify value is one of EXCELLENT, GOOD, FAIR, or POOR. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.Cellular.Interface.1.X_RDK_Identification.Imei from the DUT</small> | <small>Verify IMEI is non-empty. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>GET Device.Cellular.Interface.1.Status from the DUT</small> | <small>Verify Device.Cellular.Interface.1.Status is Up. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Cleanup: Revert Device.Cellular.Interface.1.Enable to original value (if changed)</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 3: Verify RadioEnvConditions matches RSRP signal level when CONNECTED</strong></summary>

## Test Case 3: TS_CellularManager_CheckRadioEnvConditions_CONNECTED

## Objectives
Verify that the radio environment condition (EXCELLENT, GOOD, FAIR, or POOR) correctly reflects the actual RSRP signal level when the cellular manager is in CONNECTED or REGISTERED state. The test confirms that Device.Cellular.Interface.1.X_RDK_RadioEnvConditions is consistent with the Device.Cellular.Interface.1.RSRP value according to the defined thresholds.

## Test Case ID
TC_CellularManager_7

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Cellular.Interface.1.Enable | true (if not already enabled) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If Device.Cellular.Interface.1.Enable is false, SET to true; wait 20 seconds</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to true. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is CONNECTED or REGISTERED. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Cellular.Interface.1.X_RDK_RadioEnvConditions from the DUT</small> | <small>Verify value is one of EXCELLENT, GOOD, FAIR, or POOR. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.Cellular.Interface.1.RSRP from the DUT</small> | <small>Verify RSRP value matches the expected range for the reported RadioEnvConditions: EXCELLENT (RSRP > -85), GOOD (-85 >= RSRP > -95), FAIR (-95 >= RSRP > -105), POOR (-105 >= RSRP > -115). If the condition is met PASS, else FAIL</small> |
| <small>6</small> | <small>Cleanup: Revert Device.Cellular.Interface.1.Enable to original value (if changed)</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 4: Verify RadioEnvConditions reports UNAVAILABLE when interface is disabled</strong></summary>

## Test Case 4: TS_CellularManager_CheckRadioEnvConditions_DEREGISTERED

## Objectives
Verify that the radio environment conditions parameter reports UNAVAILABLE when the cellular interface is disabled and the cellular status is DEREGISTERED. The test disables the interface, confirms DEREGISTERED status, and validates that Device.Cellular.Interface.1.X_RDK_RadioEnvConditions returns UNAVAILABLE.

## Test Case ID
TC_CellularManager_8

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Cellular.Interface.1.Enable | false (to trigger DEREGISTERED state) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If Device.Cellular.Interface.1.Enable is true, SET to false; wait 20 seconds</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to false. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is DEREGISTERED. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Cellular.Interface.1.X_RDK_RadioEnvConditions from the DUT</small> | <small>Verify Device.Cellular.Interface.1.X_RDK_RadioEnvConditions is UNAVAILABLE. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>Cleanup: Revert Device.Cellular.Interface.1.Enable to original value (if changed)</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 5: Verify BytesSent and BytesReceived are non-zero when CONNECTED</strong></summary>

## Test Case 5: TS_CellularManager_GetStatistics_CONNECTED

## Objectives
Verify that cellular statistics BytesSent and BytesReceived are non-zero when the cellular manager status is CONNECTED, confirming live data is being pulled from the modem. The test generates network traffic, waits for statistics to update, and validates that both counters report non-zero values.

## Test Case ID
TC_CellularManager_11

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Cellular.Interface.1.Enable | true (if not already enabled) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If Device.Cellular.Interface.1.Enable is false, SET to true; wait 10 seconds</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to true. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is CONNECTED. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Generate network traffic from the DUT by running a ping operation</small> | <small>Verify traffic is generated successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Wait 10 seconds for statistics to update</small> | <small>&nbsp;</small> |
| <small>6</small> | <small>GET Device.Cellular.Interface.1.X_RDK_Statistics.BytesSent from the DUT</small> | <small>Verify BytesSent is a non-zero value. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.Cellular.Interface.1.X_RDK_Statistics.BytesReceived from the DUT</small> | <small>Verify BytesReceived is a non-zero value. If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>Cleanup: Revert Device.Cellular.Interface.1.Enable to original value (if changed)</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 6: Verify BytesSent and BytesReceived are zero when DEREGISTERED</strong></summary>

## Test Case 6: TS_CellularManager_GetStatistics_DEREGISTERED

## Objectives
Verify that BytesSent and BytesReceived statistics are zero when the cellular interface is disabled and the status is DEREGISTERED. The test ensures CONNECTED state, disables the interface, waits for DEREGISTERED status, and validates that both statistics counters report zero.

## Test Case ID
TC_CellularManager_12

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Cellular.Interface.1.Enable | false (to trigger DEREGISTERED state) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If Device.Cellular.Interface.1.Enable is false, SET to true; wait 10 seconds</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to true. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is CONNECTED. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>SET Device.Cellular.Interface.1.Enable to false</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to false. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify Device.Cellular.Interface.1.Enable value is false. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is DEREGISTERED. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.Cellular.Interface.1.X_RDK_Statistics.BytesSent from the DUT</small> | <small>Verify BytesSent is zero. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>GET Device.Cellular.Interface.1.X_RDK_Statistics.BytesReceived from the DUT</small> | <small>Verify BytesReceived is zero. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Cleanup: Revert Device.Cellular.Interface.1.Enable to original value</small> | <small>&nbsp;</small> |

</details>

---

</details>

---

<details>
<summary><strong>Interface and Connectivity</strong></summary>

# Interface and Connectivity

<details>
<summary><strong>Test Case 7: Verify wwan0 interface is UP and has a valid IP when cellular is enabled</strong></summary>

## Test Case 7: TS_CellularManager_CheckIPAddressandInterfaceStatus

## Objectives
Verify that the wwan0 cellular interface is up and has a valid IP address assigned when the cellular interface is enabled. The test ensures the interface is enabled, confirms CONNECTED or REGISTERED status, checks that wwan0 is in UP state, and retrieves its IP address.

## Test Case ID
TC_CellularManager_4

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Cellular.Interface.1.Enable | true (if not already enabled) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If Device.Cellular.Interface.1.Enable is false, SET to true; wait 20 seconds</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to true. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is CONNECTED or REGISTERED. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Check if wwan0 interface is UP on the DUT</small> | <small>Verify wwan0 interface is in UP state. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Get the wwan0 interface IP address from the DUT</small> | <small>Verify wwan0 has a valid IP address assigned. If the condition is met PASS, else FAIL</small> |
| <small>6</small> | <small>Cleanup: Revert Device.Cellular.Interface.1.Enable to original value (if changed)</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 8: Verify internet connectivity via wwan0 with zero packet loss when CONNECTED</strong></summary>

## Test Case 8: TS_CellularManager_CheckInternetConnectivity

## Objectives
Verify that the device has active internet connectivity over the cellular wwan0 interface with zero packet loss. The test ensures the interface is enabled and CONNECTED, retrieves the wwan0 IP address, and performs a ping to confirm internet connectivity with 0% packet loss.

## Test Case ID
TC_CellularManager_3

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Cellular.Interface.1.Enable | true (if not already enabled) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If Device.Cellular.Interface.1.Enable is false, SET to true; wait 10 seconds</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to true. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is CONNECTED. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Get the wwan0 interface IP address from the DUT</small> | <small>Verify wwan0 IP address is obtained. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Perform a ping from the DUT to check internet connectivity</small> | <small>Verify ping is successful with 0% packet loss. If the condition is met PASS, else FAIL</small> |
| <small>6</small> | <small>Cleanup: Revert Device.Cellular.Interface.1.Enable to original value (if changed)</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 9: Verify internet connectivity is present only when cellular interface is enabled</strong></summary>

## Test Case 9: TS_CellularManager_GetIPAddressandCheckInternetConnectivity

## Objectives
Verify that internet connectivity over wwan0 is available only when the cellular interface is enabled and connected, and is correctly absent when the interface is disabled. The test disables the interface, confirms no connectivity, then enables it, confirms CONNECTED status, retrieves the wwan0 IP, and verifies successful ping.

## Test Case ID
TC_CellularManager_10

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Cellular.Interface.1.Enable | false (to verify no connectivity), true (to verify connectivity) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.Cellular.Interface.1.Enable to false (ensure interface is disabled)</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to false. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is DEREGISTERED. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Perform a ping from the DUT to check internet connectivity</small> | <small>Verify ping fails with no internet connectivity when interface is disabled. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>SET Device.Cellular.Interface.1.Enable to true; wait 20 seconds</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to true. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is CONNECTED. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Get the wwan0 interface IP address from the DUT</small> | <small>Verify wwan0 has a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Perform a ping from the DUT to check internet connectivity</small> | <small>Verify ping is successful. If the condition is met PASS, else FAIL</small> |
| <small>9</small> | <small>Cleanup: Revert Device.Cellular.Interface.1.Enable to original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 10: Verify RSSI, SNR, RSRP, and RSRQ are within valid ranges when CONNECTED</strong></summary>

## Test Case 10: TS_CellularManager_CheckInterfaceParamsWithinRange

## Objectives
Verify that the cellular interface signal quality parameters are within their valid ranges when Device.Cellular.X_RDK_Status is CONNECTED. The test validates RSSI (-117 dBm to -25 dBm), X_RDK_SNR (0 dB to 20 dB), RSRP (-155 dBm to -44 dBm), and RSRQ (-43 dB to 20 dB).

## Test Case ID
TC_CellularManager_2

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Cellular.Interface.1.Enable | true (if not already enabled) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If Device.Cellular.Interface.1.Enable is false, SET to true; wait 20 seconds</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to true. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is CONNECTED. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Cellular.Interface.1.RSSI from the DUT</small> | <small>Verify RSSI value is within range -117 dBm to -25 dBm. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.Cellular.Interface.1.X_RDK_SNR from the DUT</small> | <small>Verify X_RDK_SNR value is within range 0 dB to 20 dB. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.Cellular.Interface.1.RSRP from the DUT</small> | <small>Verify RSRP value is within range -155 dBm to -44 dBm. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.Cellular.Interface.1.RSRQ from the DUT</small> | <small>Verify RSRQ value is within range -43 dB to 20 dB. If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>Cleanup: Revert Device.Cellular.Interface.1.Enable to original value (if changed)</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>SIM, Access Technology, and Profile</strong></summary>

# SIM, Access Technology, and Profile

<details>
<summary><strong>Test Case 11: Verify SIM card slot is active and operator name is retrievable</strong></summary>

## Test Case 11: TS_CellularManager_GetSimcard_Status

## Objectives
Verify that the SIM card is active and that the operator name is retrievable from the modem. The test ensures the cellular interface is enabled and CONNECTED, then retrieves the SIM card operator name and confirms the SIM card slot status is active.

## Test Case ID
TC_CellularManager_13

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Cellular.Interface.1.Enable | true (if not already enabled) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If Device.Cellular.Interface.1.Enable is false, SET to true; wait 20 seconds</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to true. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is CONNECTED. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Get the SIM card operator name from the DUT using qmicli</small> | <small>Verify operator name is retrieved and is non-empty. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Get the SIM card slot status from the DUT using qmicli</small> | <small>Verify SIM card slot status is active. If the condition is met PASS, else FAIL</small> |
| <small>6</small> | <small>Cleanup: Revert Device.Cellular.Interface.1.Enable to original value (if changed)</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 12: Verify X_RDK_Status transitions to DEREGISTERED on SIM power-off and REGISTERED on power-on</strong></summary>

## Test Case 12: TS_CellularManager_CheckStatusAfterSimPowerOffandOn

## Objectives
Verify that the cellular manager correctly transitions to DEREGISTERED on SIM power-off and returns to REGISTERED on SIM power-on. The test confirms the interface is enabled and CONNECTED as a pre-requisite, powers off the SIM, verifies DEREGISTERED status, powers on the SIM, and confirms REGISTERED status.

## Test Case ID
TC_CellularManager_11

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| None | &nbsp; |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify Device.Cellular.Interface.1.Enable is true (pre-requisite). If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is CONNECTED (pre-requisite). If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Power off the SIM on the DUT using qmicli command</small> | <small>Verify SIM power-off command executed successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 5 seconds for status to update</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is DEREGISTERED or DOWN. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Power on the SIM on the DUT using qmicli command</small> | <small>Verify SIM power-on command executed successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is REGISTERED or CONNECTED. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 13: Verify CurrentAccessTechnology is within the list of SupportedAccessTechnologies</strong></summary>

## Test Case 13: TS_CellularManager_GetCurrentAccessTechnology

## Objectives
Verify that the current cellular access technology reported by the data model is within the device's list of supported access technologies. The test retrieves Device.Cellular.Interface.1.SupportedAccessTechnologies and Device.Cellular.Interface.1.CurrentAccessTechnology, and confirms the current technology is a member of the supported list.

## Test Case ID
TC_CellularManager_17

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Cellular.Interface.1.Enable | true (if not already enabled) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify value is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>If Device.Cellular.Interface.1.Enable is false, SET to true; wait 20 seconds</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to true. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status is CONNECTED. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.Cellular.Interface.1.SupportedAccessTechnologies from the DUT</small> | <small>Verify list of supported technologies is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.Cellular.Interface.1.CurrentAccessTechnology from the DUT</small> | <small>Verify current access technology value is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify Device.Cellular.Interface.1.CurrentAccessTechnology is within Device.Cellular.Interface.1.SupportedAccessTechnologies. If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>Cleanup: Revert Device.Cellular.Interface.1.Enable to original value (if changed)</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 14: Verify RDK context profile status transitions with cellular interface enable state</strong></summary>

## Test Case 14: TS_CellularManager_CheckRDKContextProfileStatus

## Objectives
Verify that the RDK context profile status correctly transitions between INACTIVE and ACTIVE in alignment with the cellular interface enable state and the corresponding X_RDK_Status. The test reads the current state, verifies consistency, toggles the enable parameter, and confirms both X_RDK_Status and context profile status transition accordingly.

## Test Case ID
TC_CellularManager_14

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.Cellular.Interface.1.Enable | Toggled to opposite of current value |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.Cellular.Interface.1.Enable from the DUT</small> | <small>Verify value is true or false. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify status corresponds to current enable state (CONNECTED if enabled, DEREGISTERED if disabled). If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.Cellular.Interface.1.X_RDK_ContextProfile.1.Status from the DUT</small> | <small>Verify context profile status corresponds to current enable state (ACTIVE if enabled, INACTIVE if disabled). If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>SET Device.Cellular.Interface.1.Enable to the toggled value; wait 10 seconds</small> | <small>Verify Device.Cellular.Interface.1.Enable is SET to the toggled value. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.Cellular.X_RDK_Status from the DUT</small> | <small>Verify Device.Cellular.X_RDK_Status has transitioned to the expected value (CONNECTED if enabled, DEREGISTERED if disabled). If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.Cellular.Interface.1.X_RDK_ContextProfile.1.Status from the DUT</small> | <small>Verify context profile status has transitioned (ACTIVE if enabled, INACTIVE if disabled). If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>Cleanup: Revert Device.Cellular.Interface.1.Enable to original value</small> | <small>&nbsp;</small> |

</details>

---

</details>

---


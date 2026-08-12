# Performance and Stability Validation Suite

## Test Specification Document for Performance and Stability Validation Suite

<strong>Version: 1.0</strong><br>
<strong>Date: August 2026</strong><br>
<strong>Purpose: Low-Level Test Specification for Performance and Stability Validation Suite</strong><br>
<strong>Maintained by: TDKB Test Automation Team</strong><br>

---

## Table of Contents

| # | Category | Description | Number of Tests |
|---|---|---|---|
| 1 | Performance | End-to-End throughput performance tests via iperf over wired and wireless paths | 6 |
| 2 | Stability | Long-duration stability tests covering reboots, factory resets, connectivity, DNS and WebPA load | 5 |

---

<details>
<summary><strong>Performance</strong></summary>

# Performance

<details>
<summary><strong>Test Case 1: Measure TCP Throughput from LAN to WAN</strong></summary>

## Test Case 1: E2E_TCPFromLanToWan_GetThroughput

## Objectives
Verify that the TCP throughput from the LAN client to the WAN system via iperf is within the desired throughput range, confirming end-to-end wired network performance through the gateway.

## Test Case ID
TC_TDKB_E2E_815

## Test Type
Positive

## Test Environment

| Component |
|---|
| DUT - Gateway under test |
| LAN Client - Wired client |
| WAN - WAN system |

## Test Configuration

| Parameter | Value |
|---|---|
| LAN to WAN TCP throughput threshold (LAN_THROUGHPUT_TO_WAN) | As per test configuration |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | WAN system | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| 1 | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small> Get the Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify that the gateway IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 2 | <small>&nbsp;</small> | <small>Get the IP address of the LAN client.</small> | <small>&nbsp;</small> | <small>Verify that the LAN client IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 3 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that the LAN client IP address is within the same DHCP range as the gateway IP. If the condition is met CONTINUE, else FAIL.</small> |
| 4 | <small>&nbsp;</small> | <small>Add a static route to WAN IP via the gateway IP on the LAN interface.</small> | <small>&nbsp;</small> | <small>Verify that the static route is added successfully on the LAN client. If the condition is met CONTINUE, else FAIL.</small> |
| 5 | <small>&nbsp;</small> | <small>Run iperf TCP client towards the WAN system.</small> | <small>Run iperf TCP server.</small> | <small>Verify that TCP data transfer from LAN client to WAN system is successful and server-side bandwidth output is available. If the condition is met CONTINUE, else FAIL.</small> |
| 6 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that the measured throughput (in Mbps) is within the expected range (configured threshold ± 5 Mbps). If the condition is met PASS, else FAIL.</small> |
| 7 | <small>&nbsp;</small> | <small>Delete the static route to WAN IP via the gateway on the LAN interface.</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 2: Measure TCP Throughput from LAN to WLAN</strong></summary>

## Test Case 2: E2E_WIFI_TCPFromLanToWlan_GetThroughput

## Objectives
Verify that the TCP throughput from the LAN client to the WLAN client via iperf is within the desired throughput range, confirming end-to-end wireless network performance through the gateway.

## Test Case ID
TC_TDKB_E2E_814

## Test Type
Positive

## Test Environment

| Component |
|---|
| DUT - Gateway under test |
| LAN Client - Wired client |
| WLAN Client - Wireless client |

## Test Configuration

| Parameter | Value |
|---|---|
| WiFi SSID name (MLO_SSID) | As per test configuration |
| WiFi SSID passphrase (MLO_PASSWORD) | As per test configuration |
| LAN to WLAN TCP throughput threshold (LAN_THROUGHPUT_TO_WLAN) | As per test configuration |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| 1 | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get the Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase and verify that the current SSID and KeyPassphrase are retrieved and match the values as per test configuration. If the condition is met CONTINUE, else FAIL.</small> |
| 2 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Connect to the WiFi SSID using the SSID name and credentials as per test configuration.</small> | <small>Verify that the WLAN client is connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 3 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get the IP address of the WLAN client after connecting to WiFi.</small> | <small>Verify that the WLAN client IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 4 | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get the Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify that the gateway IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 5 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that the WLAN client IP address is within the same DHCP range as the gateway IP. If the condition is met CONTINUE, else FAIL.</small> |
| 6 | <small>&nbsp;</small> | <small>Get the IP address of the LAN client.</small> | <small>&nbsp;</small> | <small>Verify that the LAN client IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 7 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that the LAN client IP address is within the same DHCP range as the gateway IP. If the condition is met CONTINUE, else FAIL.</small> |
| 8 | <small>&nbsp;</small> | <small>Run iperf TCP client towards the WLAN client.</small> | <small>Run iperf TCP server.</small> | <small>Verify that TCP data transfer from LAN client to WLAN client is successful and server-side bandwidth output is available. If the condition is met CONTINUE, else FAIL.</small> |
| 9 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that the measured throughput (in Mbps) is within the expected range (configured threshold ± 5 Mbps). If the condition is met PASS, else FAIL.</small> |
| 10 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Disconnect from the WiFi SSID.</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 3: Measure TCP Throughput from WLAN to LAN</strong></summary>

## Test Case 3: E2E_WIFI_TCPFromWlanToLan_GetThroughput

## Objectives
Verify that the TCP throughput from the WLAN client to the LAN client via iperf is within the desired throughput range, confirming end-to-end wireless-to-wired network performance through the gateway.

## Test Case ID
TC_TDKB_E2E_812

## Test Type
Positive

## Test Environment

| Component |
|---|
| DUT - Gateway under test |
| LAN Client - Wired client |
| WLAN Client - Wireless client |

## Test Configuration

| Parameter | Value |
|---|---|
| WiFi SSID name (MLO_SSID) | As per test configuration |
| WiFi SSID passphrase (MLO_PASSWORD) | As per test configuration |
| WLAN to LAN TCP throughput threshold (WLAN_MLO_THROUGHPUT_TO_LAN) | As per test configuration |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| 1 | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get the Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase and verify that the current SSID and KeyPassphrase are retrieved and match the values as per test configuration. If the condition is met CONTINUE, else FAIL.</small> |
| 2 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Connect to the WiFi SSID using the SSID name and credentials as per test configuration.</small> | <small>Verify that the WLAN client is connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 3 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get the IP address of the WLAN client after connecting to WiFi.</small> | <small>Verify that the WLAN client IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 4 | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get the  Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify that the gateway IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 5 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that the WLAN client IP address is within the same DHCP range as the gateway IP. If the condition is met CONTINUE, else FAIL.</small> |
| 6 | <small>&nbsp;</small> | <small>Get the IP address of the LAN client.</small> | <small>&nbsp;</small> | <small>Verify that the LAN client IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 7 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that the LAN client IP address is within the same DHCP range as the gateway IP. If the condition is met CONTINUE, else FAIL.</small> |
| 8 | <small>&nbsp;</small> | <small>Run iperf TCP server.</small> | <small>Run iperf TCP client towards the LAN client.</small> | <small>Verify that TCP data transfer from WLAN client to LAN client is successful and server-side bandwidth output is available. If the condition is met CONTINUE, else FAIL.</small> |
| 9 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that the measured throughput (in Mbps) is within the expected range (configured threshold ± 5 Mbps). If the condition is met PASS, else FAIL.</small> |
| 10 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Disconnect from the WiFi SSID.</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 4: Measure Average TCP Throughput from WLAN to LAN over Configured Duration</strong></summary>

## Test Case 4: E2E_WIFI_TCPFromWlanToLan_Perf

## Objectives
Measure and verify the average TCP throughput from the WLAN client to the LAN client over a specified duration using iperf, confirming that the average throughput is within the expected performance range.

## Test Case ID
TC_TDKB_E2E_834

## Test Type
Positive

## Test Environment

| Component |
|---|
| DUT - Gateway under test |
| LAN Client - Wired client |
| WLAN Client - Wireless client |

## Test Configuration

| Parameter | Value |
|---|---|
| WiFi SSID name (MLO_SSID) | As per test configuration |
| WiFi SSID passphrase (MLO_PASSWORD) | As per test configuration |
| WLAN to LAN average TCP throughput threshold (WLAN_MLO_THROUGHPUT_TO_LAN) | As per test configuration |
| WLAN throughput Output file (WLAN_MLO_THROUGHPUT_OUTFILE) | As per test configuration |
| Performance test duration (PERF_TEST_DURATION) | As per test configuration |
| Performance test poll interval (PERF_TEST_POLL_INTERVAL) | As per test configuration |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| 1 | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get the Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase and verify that the current SSID and KeyPassphrase are retrieved and match the values as per test configuration. If the condition is met CONTINUE, else FAIL.</small> |
| 2 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Connect to the WiFi SSID using the SSID name and credentials as per test configuration.</small> | <small>Verify that the WLAN client is connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 3 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get the IP address of the WLAN client after connecting to WiFi.</small> | <small>Verify that the WLAN client IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 4 | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get the Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify that the gateway IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 5 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that the WLAN client IP address is within the same DHCP range as the gateway IP. If the condition is met CONTINUE, else FAIL.</small> |
| 6 | <small>&nbsp;</small> | <small>Get the IP address of the LAN client.</small> | <small>&nbsp;</small> | <small>Verify that the LAN client IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 7 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that the LAN client IP address is within the same DHCP range as the gateway IP. If the condition is met CONTINUE, else FAIL.</small> |
| 8 | <small>&nbsp;</small> | <small>Run iperf TCP server for the configured performance test duration.</small> | <small>Run iperf TCP client towards the LAN client at periodic intervals and save throughput values to an output file.</small> | <small>Verify that the average throughput (in Mbps) calculated from all interval measurements is within the expected range (configured threshold ± 5 Mbps). If the condition is met PASS, else FAIL.</small> |
| 9 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Disconnect from the WiFi SSID.</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 5: Measure TCP Throughput from WLAN to WAN</strong></summary>

## Test Case 5: E2E_WIFI_TCPFromWlanToWan_GetThroughput

## Objectives
Verify that the TCP throughput from the WLAN client to the WAN system via iperf is within the desired throughput range, confirming end-to-end wireless-to-WAN network performance through the gateway.

## Test Case ID
TC_TDKB_E2E_813

## Test Type
Positive

## Test Environment

| Component |
|---|
| DUT - Gateway under test |
| WLAN Client - Wireless client |
| WAN - WAN system |

## Test Configuration

| Parameter | Value |
|---|---|
| WiFi SSID name (MLO_SSID) | As per test configuration |
| WiFi SSID passphrase (MLO_PASSWORD) | As per test configuration |
| WLAN to WAN TCP throughput threshold (WLAN_MLO_THROUGHPUT_TO_WAN) | As per test configuration |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | WAN system | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| 1 | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get the Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase and verify that the current SSID and KeyPassphrase are retrieved and match the values as per test configuration. If the condition is met CONTINUE, else FAIL.</small> |
| 2 | <small>&nbsp;</small> | <small>Connect to the WiFi SSID using the SSID name and credentials as per test configuration.</small> | <small>&nbsp;</small> | <small>Verify that the WLAN client is connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 3 | <small>&nbsp;</small> | <small>Get the IP address of the WLAN client after connecting to WiFi.</small> | <small>&nbsp;</small> | <small>Verify that the WLAN client IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 4 | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get the Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify that the gateway IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 5 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that the WLAN client IP address is within the same DHCP range as the gateway IP. If the condition is met CONTINUE, else FAIL.</small> |
| 6 | <small>&nbsp;</small> | <small>Add a static route to WAN IP via the gateway IP on the WLAN interface.</small> | <small>&nbsp;</small> | <small>Verify that the static route is added successfully on the WLAN client. If the condition is met CONTINUE, else FAIL.</small> |
| 7 | <small>&nbsp;</small> | <small>Run iperf TCP client towards the WAN system.</small> | <small>Run iperf TCP server.</small> | <small>Verify that TCP data transfer from WLAN client to WAN system is successful and server-side bandwidth output is available. If the condition is met CONTINUE, else FAIL.</small> |
| 8 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that the measured throughput (in Mbps) is within the expected range (configured threshold ± 5 Mbps). If the condition is met PASS, else FAIL.</small> |
| 9 | <small>&nbsp;</small> | <small>Delete the static route to WAN IP via the gateway on the WLAN interface.</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| 10 | <small>&nbsp;</small> | <small>Disconnect from the WiFi SSID.</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 6: Measure Average TCP Throughput from WLAN to WAN over Configured Duration</strong></summary>

## Test Case 6: E2E_WIFI_TCPFromWlanToWan_Perf

## Objectives
Measure and verify the average TCP throughput from the WLAN client to the WAN system over a specified duration using iperf, confirming that the average throughput is within the expected performance range.

## Test Case ID
TC_TDKB_E2E_833

## Test Type
Positive

## Test Environment

| Component |
|---|
| DUT - Gateway under test |
| WLAN Client - Wireless client |
| WAN - WAN system |

## Test Configuration

| Parameter | Value |
|---|---|
| WiFi SSID name (MLO_SSID) | As per test configuration |
| WiFi SSID passphrase (MLO_PASSWORD) | As per test configuration |
| WLAN to WAN average TCP throughput threshold (WLAN_MLO_THROUGHPUT_TO_WAN) | As per test configuration |
| WLAN throughput Output file (WLAN_MLO_THROUGHPUT_OUTFILE) | As per test configuration |
| Performance test duration (PERF_TEST_DURATION) | As per test configuration |
| Performance test poll interval (PERF_TEST_POLL_INTERVAL) | As per test configuration |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | WAN system | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|------------------------------|
| 1 | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get the Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase and verify that the current SSID and KeyPassphrase are retrieved and match the values as per test configuration. If the condition is met CONTINUE, else FAIL.</small> |
| 2 | <small>&nbsp;</small> | <small>Connect to the WiFi SSID using the SSID name and credentials as per test configuration.</small> | <small>&nbsp;</small> | <small>Verify that the WLAN client is connected to the WiFi SSID successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 3 | <small>&nbsp;</small> | <small>Get the IP address of the WLAN client after connecting to WiFi.</small> | <small>&nbsp;</small> | <small>Verify that the WLAN client IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 4 | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Get the Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify that the gateway IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 5 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that the WLAN client IP address is within the same DHCP range as the gateway IP. If the condition is met CONTINUE, else FAIL.</small> |
| 6 | <small>&nbsp;</small> | <small>Add a static route to WAN IP via the gateway IP on the WLAN interface.</small> | <small>&nbsp;</small> | <small>Verify that the static route is added successfully on the WLAN client. If the condition is met CONTINUE, else FAIL.</small> |
| 7 | <small>&nbsp;</small> | <small>Run iperf TCP client towards the WAN system at periodic intervals and save throughput values to an output file.</small> | <small>Run iperf TCP server for the configured performance test duration.</small> | <small>Verify that the average throughput (in Mbps) calculated from all interval measurements is within the expected range (configured threshold ± 5 Mbps). If the condition is met PASS, else FAIL.</small> |
| 8 | <small>&nbsp;</small> | <small>Delete the static route to WAN IP via the gateway on the WLAN interface.</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| 9 | <small>&nbsp;</small> | <small>Disconnect from the WiFi SSID.</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

</details>

---

<details>
<summary><strong>Stability</strong></summary>

# Stability

<details>
<summary><strong>Test Case 7: Verify Gateway Stability across Multiple Reboots</strong></summary>

## Test Case 7: TS_STABILITY_MultipleReboots

## Objectives
Verify that the gateway remains operational and all critical interfaces and processes are up after repeated reboots, confirming device stability across multiple reboot cycles.

## Test Case ID
TC_STABILITY_1

## Test Type
Positive

## Test Environment

| Component |
|---|
| DUT - Gateway under test |

## Test Configuration

| Parameter | Value |
|---|---|
| Maximum process-up wait time (MAX_PROCESSUP_WAITTIME) | As per test configuration |
| Interface list (INTERFACE_LIST) | As per test configuration |
| Critical process list (CCSP_PROCESS, SNMP_PROCESS, WEBPA_PROCESS, LIGHTTPD_PROCESS, DROPBEAR_PROCESS, WEBCONFIG_PROCESS, PSM_PROCESS, TELEMETRY_PROCESS, WIFI_PROCESS) | As per test configuration |
| Total iterations (TOTAL_ITERATIONS) |  As per test configuration |
| Upload server url (UPLOAD_SERVER_URL) | As per test configuration |
| Device Failure Logs Location (FAILURE_ARTIFACT_ROOT) | As per test configuration |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Read maximum process-up wait time from device configuration.</small> | <small>Get the maximum process-up wait time from the configuration file. Verify that the wait time is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 2 | <small>Read interface list from device configuration.</small> | <small>Get the list of interfaces from the configuration file. Verify that the interface list is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 3 | <small>Read critical process list from device configuration.</small> | <small>Get the critical process list from the configuration file. Verify that the critical process list is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 4 | <small>Reboot the DUT.</small> | <small>Verify that the device reboots and resumes connectivity. If the condition is met CONTINUE, else FAIL.</small> |
| 5 | <small>GET Device.DeviceInfo.UpTime</small> | <small>Get the Device.DeviceInfo.UpTime and verify that the device uptime is retrieved. If uptime is less than the configured wait time, sleep for the remaining duration before proceeding. If the condition is met CONTINUE, else FAIL.</small> |
| 6 | <small>Check that all configured network interfaces are up and have valid IP addresses.</small> | <small>Verify that all interfaces are up after reboot. If the condition is met CONTINUE, else FAIL.</small> |
| 7 | <small>Check that all critical processes are running after reboot.</small> | <small>Verify that all critical processes are running. Repeat steps 4–7 for TOTAL_ITERATIONS times. If all iterations succeed PASS, else FAIL on first failure.</small> |
| 8 | <small>On first failure, collect device snapshots (process list, top output, memory info, CPU info, service status, network state, core dumps, and rdklogs) and upload to the upload server.</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 8: Verify Gateway Stability across Multiple Factory Resets</strong></summary>

## Test Case 8: TS_STABILITY_MultipleFactoryReset

## Objectives
Verify that the gateway remains operational and all critical interfaces and processes are up after repeated factory resets, confirming device stability across multiple reset cycles.

## Test Case ID
TC_STABILITY_2

## Test Type
Positive

## Test Environment

| Component |
|---|
| DUT - Gateway under test |

## Test Configuration

| Parameter | Value |
|---|---|
| Device.X_CISCO_COM_DeviceControl.FactoryReset | Router,Wifi,VoIP,Dect,MoCA |
| Maximum process-up wait time (MAX_PROCESSUP_WAITTIME) | As per test configuration |
| Interface list (INTERFACE_LIST) | As per test configuration |
| Critical process list (CCSP_PROCESS, SNMP_PROCESS, WEBPA_PROCESS, LIGHTTPD_PROCESS, DROPBEAR_PROCESS, WEBCONFIG_PROCESS, PSM_PROCESS, TELEMETRY_PROCESS, WIFI_PROCESS) | As per test configuration |
| Total iterations (TOTAL_ITERATIONS) | As per test configuration |
| Upload server url (UPLOAD_SERVER_URL) | As per test configuration |
| Device Failure Logs Location (FAILURE_ARTIFACT_ROOT) | As per test configuration |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Read maximum process-up wait time from device configuration.</small> | <small>Get the maximum process-up wait time from the configuration file. Verify that the wait time is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 2 | <small>Read interface list from device configuration.</small> | <small>Get the list of interfaces from the configuration file. Verify that the interface list is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 3 | <small>Read critical process list from device configuration.</small> | <small>Get the critical process list from the configuration file. Verify that the critical process list is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 4 | <small>&nbsp;</small> | <small>Set the Device.X_CISCO_COM_DeviceControl.FactoryReset with value "Router,Wifi,VoIP,Dect,MoCA" and verify that the factory reset is triggered successfully and the device resumes connectivity. If the condition is met CONTINUE, else FAIL.</small> |
| 5 | <small>GET Device.DeviceInfo.UpTime</small> | <small>Get the Device.DeviceInfo.UpTime and verify that the device uptime is retrieved. If uptime is less than the configured wait time, sleep for the remaining duration before proceeding. If the condition is met CONTINUE, else FAIL.</small> |
| 6 | <small>Check that all configured network interfaces are up and have valid IP addresses.</small> | <small>Verify that all interfaces are up after factory reset. If the condition is met CONTINUE, else FAIL.</small> |
| 7 | <small>Check that all critical processes are running after factory reset.</small> | <small>Verify that all critical processes are running. Repeat steps 4–7 for TOTAL_ITERATIONS times. If all iterations succeed PASS, else FAIL on first failure.</small> |
| 8 | <small>On first failure, collect device snapshots (process list, top output, memory info, CPU info, service status, network state, core dumps, and rdklogs) and upload to the upload server.</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 9: Verify Long-Run IPv4 Connectivity from LAN Client without Packet Loss</strong></summary>

## Test Case 9: TS_STABILITY_E2E_LongRunIPV4ConnectivityfromLanClient

## Objectives
Verify that a long-duration IPv4 ping from the LAN client to a public IPv4 address does not cause any packet loss or device crash, and that device health metrics (memory and CPU usage) remain within acceptable limits throughout the test.

## Test Case ID
TS_STABILITY_4

## Test Type
Positive

## Test Environment

| Component |
|---|
| DUT - Gateway under test |
| LAN Client - Wired client |

## Test Configuration

| Parameter | Value |
|---|---|
| Critical process list (CCSP_PROCESS, SNMP_PROCESS, WEBPA_PROCESS, LIGHTTPD_PROCESS, DROPBEAR_PROCESS, WEBCONFIG_PROCESS, PSM_PROCESS, TELEMETRY_PROCESS, WIFI_PROCESS) | As per test configuration |
| Upload server url (UPLOAD_SERVER_URL) | As per test configuration |
| Device Failure Logs Location (FAILURE_ARTIFACT_ROOT) | As per test configuration |
| Public IPv4 address (PUBLIC_IPV4) | As per test configuration  |
| Connectivity duration (CONNECTIVITY_DURATION) | As per test configuration |
| Ping Output file (PING_OUTPUT_FILE) | As per test configuration |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| 1 | <small>Read critical process list from device configuration.</small> | <small>&nbsp;</small> | <small>Get the critical process list from the configuration file on the DUT. Verify that the critical process list is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 2 | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>Get the Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and verify that the gateway IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 3 | <small>&nbsp;</small> | <small>Start a continuous IPv4 ping to a public IPv4 address for the configured CONNECTIVITY_DURATION seconds, running in the background.</small> | <small>Verify that the ping is started successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 4 | <small>Periodically (every 10 iterations): Check that all critical processes are running.</small> | <small>&nbsp;</small> | <small>Verify that all critical processes are running on the DUT. If the condition is met CONTINUE, else FAIL.</small> |
| 5 | <small>Periodically: Capture free memory (pre-checkpoint).</small> | <small>&nbsp;</small> | <small>Verify that free memory is captured successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 6 | <small>Periodically: Capture free memory (post-checkpoint) and compare with pre-checkpoint value.</small> | <small>&nbsp;</small> | <small>Verify that memory loss does not exceed 10% of the pre-checkpoint value (no memory leak). If the condition is met CONTINUE, else FAIL.</small> |
| 7 | <small>Periodically (every 50 iterations): Capture CPU usage (pre-checkpoint).</small> | <small>&nbsp;</small> | <small>Verify that CPU usage is captured and is at or below 90%. If the condition is met CONTINUE, else FAIL.</small> |
| 8 | <small>Periodically (every 50 iterations): Capture CPU usage (post-checkpoint) and compare with pre-checkpoint value.</small> | <small>&nbsp;</small> | <small>Verify that CPU usage did not exceed 90% and the delta between pre and post CPU usage did not exceed acceptable limits. If the condition is met CONTINUE, else FAIL.</small> |
| 9 | <small>&nbsp;</small> | <small>After the configured CONNECTIVITY_DURATION, read the ping output file.</small> | <small>Verify that there is 0% packet loss in the ping output. If the condition is met PASS, else FAIL.</small> |
| 10 | <small>On first failure, collect device snapshots (process list, top output, memory info, CPU info, service status, network state, core dumps, and rdklogs) and upload to the upload server.</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 10: Verify DNS Stability under Repeated Queries from LAN Client</strong></summary>

## Test Case 10: TS_STABILITY_E2E_MultipleDNSQueryfromLanClient

## Objectives
Verify that repeated DNS queries from the LAN client do not cause DNS failures or device instability, and that device health metrics (DNS process status, memory usage, and CPU usage) remain within acceptable limits across multiple iterations.

## Test Case ID
TS_STABILITY_3

## Test Type
Positive

## Test Environment

| Component |
|---|
| DUT - Gateway under test |
| LAN Client - Wired client |

## Test Configuration

| Parameter | Value |
|---|---|
| Critical process list (CCSP_PROCESS, SNMP_PROCESS, WEBPA_PROCESS, LIGHTTPD_PROCESS, DROPBEAR_PROCESS, WEBCONFIG_PROCESS, PSM_PROCESS, TELEMETRY_PROCESS, WIFI_PROCESS) | As per test configuration |
| DNS process name (DNS_PROCESS) | As per test configuration |
| Number of connectivity iterations (CONNECTIVITY_ITERATIONS) | As per test configuration |
| Upload server url (UPLOAD_SERVER_URL) | As per test configuration |
| Device Failure Logs Location (FAILURE_ARTIFACT_ROOT) | As per test configuration |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| 1 | <small>Read critical process list from device configuration.</small> | <small>&nbsp;</small> | <small>Get the critical process list from the configuration file on the DUT. Verify that the critical process list is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 2 | <small>GET Device.DNS.Client.Server.1.DNSServer</small> | <small>&nbsp;</small> | <small>Get the Device.DNS.Client.Server.1.DNSServer and verify that the primary DNS server IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 3 | <small>Periodically (every 10 iterations): Capture CPU usage (pre-checkpoint).</small> | <small>&nbsp;</small> | <small>Verify that CPU usage is captured and is at or below 90%. If the condition is met CONTINUE, else FAIL.</small> |
| 4 | <small>Capture the DNS process PID (pre-checkpoint).</small> | <small>&nbsp;</small> | <small>Verify that the DNS process is running and its PID is captured. If the condition is met CONTINUE, else FAIL.</small> |
| 5 | <small>Capture free memory (pre-checkpoint).</small> | <small>&nbsp;</small> | <small>Verify that free memory is captured successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 6 | <small>&nbsp;</small> | <small>Run nslookup for the configured domain name against the primary DNS server IP.</small> | <small>Verify that the DNS query resolves successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 7 | <small>Periodically (every 10 iterations): Capture CPU usage (post-checkpoint).</small> | <small>&nbsp;</small> | <small>Verify that CPU usage is captured successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 8 | <small>Capture the DNS process PID (post-checkpoint).</small> | <small>&nbsp;</small> | <small>Verify that the DNS process is still running and its PID is captured. If the condition is met CONTINUE, else FAIL.</small> |
| 9 | <small>Capture free memory (post-checkpoint).</small> | <small>&nbsp;</small> | <small>Verify that free memory is captured successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 10 | <small>Check that all critical processes are running.</small> | <small>&nbsp;</small> | <small>Verify that all critical processes are running on the DUT. If the condition is met CONTINUE, else FAIL.</small> |
| 11 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that the DNS process PID is unchanged between pre and post checkpoint (DNS process did not crash). If the condition is met CONTINUE, else FAIL.</small> |
| 12 | <small>&nbsp;</small> | <small>&nbsp;</small> | <small>Verify that memory loss does not exceed 10% of the pre-checkpoint value (no memory leak). Repeat steps 3–12 for CONNECTIVITY_ITERATIONS times. If all iterations succeed PASS, else FAIL on first failure.</small> |
| 13 | <small>On first failure, collect device snapshots (process list, top output, memory info, CPU info, service status, network state, core dumps, and rdklogs) and upload to the upload server.</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 11: Verify Device Stability under Continuous WebPA Configuration Updates</strong></summary>

## Test Case 11: TS_STABILITY_MultipleWebPAQuery

## Objectives
Verify that continuous configuration updates via WebPA do not cause failures in the WebPA service or device stability issues, and that device health metrics (process status, memory usage, and CPU usage) remain within acceptable limits across multiple iterations.

## Test Case ID
TS_STABILITY_5

## Test Type
Positive

## Test Environment

| Component |
|---|
| DUT - Gateway under test |

## Test Configuration

| Parameter | Value |
|---|---|
| Critical process list (CCSP_PROCESS, SNMP_PROCESS, WEBPA_PROCESS, LIGHTTPD_PROCESS, DROPBEAR_PROCESS, WEBCONFIG_PROCESS, PSM_PROCESS, TELEMETRY_PROCESS, WIFI_PROCESS) | As per test configuration |
| WebPA process name (WEBPA_PROCESS) | As per test configuration |
| Parodus process name (PARODUS_PROCESS) | As per test configuration |
| Number of connectivity iterations (CONNECTIVITY_ITERATIONS) | As per test configuration |
| Upload server url (UPLOAD_SERVER_URL) | As per test configuration |
| Device Failure Logs Location (FAILURE_ARTIFACT_ROOT) | As per test configuration |
| Device.X_CISCO_COM_Security.Firewall.FirewallLevel | As per test configuration (alternate value cycled between High, Medium, Low) |
| Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable | As per test configuration (alternate value cycled between true and false) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|
| 1 | <small>Read critical process list from device configuration.</small> | <small>Get the critical process list from the configuration file. Verify that the critical process list is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 2 | <small>Check that all critical processes are running (pre-requisite check).</small> | <small>Verify that all critical processes are running on the DUT before starting the test. If the condition is met CONTINUE, else FAIL.</small> |
| 3 | <small>&nbsp;</small> | <small>Send a WEBPA GET request for Device.X_CISCO_COM_Security.Firewall.FirewallLevel to the WEBPA Server. Verify that the original value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 4 | <small>&nbsp;</small> | <small>Send a WEBPA GET request for Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable to the WEBPA Server. Verify that the original value is retrieved successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 5 | <small>Periodically (every 10 iterations): Capture CPU usage (pre-checkpoint).</small> | <small>Verify that CPU usage is captured and is at or below 90%. If the condition is met CONTINUE, else FAIL.</small> |
| 6 | <small>Capture WebPA process PID (pre-checkpoint).</small> | <small>Verify that the WebPA process is running and its PID is captured. If the condition is met CONTINUE, else FAIL.</small> |
| 7 | <small>Capture Parodus process PID (pre-checkpoint).</small> | <small>Verify that the Parodus process is running and its PID is captured. If the condition is met CONTINUE, else FAIL.</small> |
| 8 | <small>Capture free memory (pre-checkpoint).</small> | <small>Verify that free memory is captured successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 9 | <small>&nbsp;</small> | <small>Send a WEBPA GET request for the current WebPA parameter (Device.X_CISCO_COM_Security.Firewall.FirewallLevel or Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable, selected by iteration index) to the WEBPA Server. Verify that the current value is retrieved. If the condition is met CONTINUE, else FAIL.</small> |
| 10 | <small>&nbsp;</small> | <small>Send a WEBPA SET request for the selected WebPA parameter with an alternate valid value to the WEBPA Server. Verify that the SET operation succeeds. If the condition is met CONTINUE, else FAIL.</small> |
| 11 | <small>&nbsp;</small> | <small>Send a WEBPA GET request for the selected WebPA parameter to the WEBPA Server. Verify that the parameter value reflects the newly set value. If the condition is met CONTINUE, else FAIL.</small> |
| 12 | <small>Periodically (every 10 iterations): Capture CPU usage (post-checkpoint).</small> | <small>Verify that CPU usage is captured successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 13 | <small>Capture WebPA process PID (post-checkpoint).</small> | <small>Verify that the WebPA process is still running and its PID is captured. If the condition is met CONTINUE, else FAIL.</small> |
| 14 | <small>Capture Parodus process PID (post-checkpoint).</small> | <small>Verify that the Parodus process is still running and its PID is captured. If the condition is met CONTINUE, else FAIL.</small> |
| 15 | <small>Capture free memory (post-checkpoint).</small> | <small>Verify that free memory is captured successfully. If the condition is met CONTINUE, else FAIL.</small> |
| 16 | <small>Check that all critical processes are running.</small> | <small>Verify that all critical processes are running on the DUT. If the condition is met CONTINUE, else FAIL.</small> |
| 17 | <small>&nbsp;</small> | <small>Verify that the WebPA process PID is unchanged between pre and post checkpoint (WebPA process did not crash). If the condition is met CONTINUE, else FAIL.</small> |
| 18 | <small>&nbsp;</small> | <small>Verify that the Parodus process PID is unchanged between pre and post checkpoint (Parodus process did not crash). If the condition is met CONTINUE, else FAIL.</small> |
| 19 | <small>&nbsp;</small> | <small>Periodically (every 10 iterations): Verify that CPU usage did not spike (post CPU ≤ 90% and CPU delta ≤ 20% if post CPU ≤ 70%). If the condition is met CONTINUE, else FAIL.</small> |
| 20 | <small>&nbsp;</small> | <small>Verify that memory loss does not exceed 10% of the pre-checkpoint free memory value (no memory leak). Repeat steps 5–20 for CONNECTIVITY_ITERATIONS times. If any iteration fails, stop on first failure.</small> |
| 21 | <small>&nbsp;</small> | <small>Revert Device.X_CISCO_COM_Security.Firewall.FirewallLevel to original value via WEBPA SET to the WEBPA Server. Verify revert is successful. If the condition is met CONTINUE, else FAIL.</small> |
| 22 | <small>&nbsp;</small> | <small>Revert Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable to original value via WEBPA SET to the WEBPA Server. If the condition is met PASS, else FAIL.</small> |
| 23 | <small>On first failure, collect device snapshots (process list, top output, memory info, CPU info, service status, network state, core dumps, and rdklogs) and upload to the upload server.</small> | <small>&nbsp;</small> |

</details>

---

</details>

---

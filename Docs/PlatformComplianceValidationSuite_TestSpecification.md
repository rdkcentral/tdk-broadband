# Platform Compliance Validation Suite

## Test Specification Document for Platform Compliance Validation Suite

<strong>Version</strong>: 1.0<br>
<strong>Date</strong>: August 2026<br>
<strong>Purpose</strong>: Low-level test specification for the Platform Compliance Validation Suite<br>
<strong>Maintained by</strong>: TDKB Test Automation Team

## Table of Contents

| # | Category | Description | Number of Tests |
|---|----------|-------------|:---:|
| 1 | E2E | End-to-end functional tests | 9 |
| 2 | SANITY - Status Checks | Interface and process up/running checks | 11 |
| 3 | SANITY - Behavioral Checks | Behavioral and state transition checks | 16 |
| 4 | CCSP Common - MBUS | CCSP message bus interface tests | 2 |
| 5 | RBUS | RBUS open/close session tests | 3 |

---

<details>
<summary><strong>E2E</strong></summary>

# E2E

<details>
<summary><strong>Test Case 1: Verify LAN IP address change is reflected on wired LAN client DHCP range</strong></summary>

## Test Case 1: E2E_ChangeLanManagementEntry_LanIPAddress

## Objectives
Verify that changes to the default LAN management LAN IP address and DHCP address range are reflected on the wired LAN client. The test validates that after modifying Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.DHCPv4.Server.Pool.1.MinAddress, and Device.DHCPv4.Server.Pool.1.MaxAddress, a connected LAN client obtains an IP address within the newly configured DHCP range.

## Test Case ID
TC_TDKB_E2E_460

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client – Wired Ethernet client |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress | 10.0.0.1 or 172.16.0.1 (hardcoded alternate of current value) |
| Device.DHCPv4.Server.Pool.1.MinAddress | 10.0.0.2 or 172.16.0.2 (hardcoded alternate of current value) |
| Device.DHCPv4.Server.Pool.1.MaxAddress | 10.0.0.253 or 172.16.0.253 (hardcoded alternate of current value) |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.DHCPv4.Server.Pool.1.MinAddress, and Device.DHCPv4.Server.Pool.1.MaxAddress and save the original values</small> | <small>&nbsp;</small> | <small>Verify all parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.DHCPv4.Server.Pool.1.MinAddress, and Device.DHCPv4.Server.Pool.1.MaxAddress to the new configured values</small> | <small>&nbsp;</small> | <small>Verify all SET operations are successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.DHCPv4.Server.Pool.1.MinAddress, and Device.DHCPv4.Server.Pool.1.MaxAddress</small> | <small>&nbsp;</small> | <small>Verify the retrieved values match the newly SET values. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Wait 60 seconds for DHCP configuration changes to propagate to the LAN client</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the new configured DHCP range</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.DHCPv4.Server.Pool.1.MinAddress, and Device.DHCPv4.Server.Pool.1.MaxAddress to original values</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 2: Verify primary DNS server resolves domain names from the LAN client</strong></summary>

## Test Case 2: E2E_DNS_ResolveDomainName_PrimaryDNS

## Objectives
Verify that the gateway's primary IPv4 DNS server, as configured in Device.DNS.Client.Server.1.DNSServer, successfully resolves DNS queries issued from the LAN client. The test retrieves the Primary DNS Server IP from the DUT and uses it to perform an nslookup on the LAN client to confirm successful domain name resolution.

## Test Case ID
TC_TDKB_E2E_195

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client – Wired Ethernet client |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DNS.Client.Server.1.DNSServer and save the Primary DNS Server IP address</small> | <small>&nbsp;</small> | <small>Verify the Primary DNS Server IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Run nslookup for the configured domain name using the retrieved Primary DNS Server IP address as the DNS server</small> | <small>Verify the domain name is resolved successfully by the Primary DNS Server. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 3: Verify secondary DNS server resolves domain names from the LAN client</strong></summary>

## Test Case 3: E2E_DNS_ResolveDomainName_SecondaryDNS

## Objectives
Verify that the gateway's secondary IPv4 DNS server, as configured in Device.DNS.Client.Server.2.DNSServer, successfully resolves DNS queries issued from the LAN client. The test retrieves the Secondary DNS Server IP from the DUT and uses it to perform an nslookup on the LAN client to confirm successful domain name resolution.

## Test Case ID
TC_TDKB_E2E_196

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client – Wired Ethernet client |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.DNS.Client.Server.2.DNSServer and save the Secondary DNS Server IP address</small> | <small>&nbsp;</small> | <small>Verify the Secondary DNS Server IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Run nslookup for the configured domain name using the retrieved Secondary DNS Server IP address as the DNS server</small> | <small>Verify the domain name is resolved successfully by the Secondary DNS Server. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 4: Verify wired LAN client has internet access through the gateway</strong></summary>

## Test Case 4: E2E_WIFI_LAN_AccessInternet

## Objectives
Verify that a wired LAN client connected to the gateway has internet access. The test validates end-to-end connectivity from the LAN client through the gateway to the internet, confirming that the LAN client is connected to the gateway with a valid IP address and can successfully reach external internet hosts.

## Test Case ID
TC_TDKB_E2E_819

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client – Wired Ethernet client |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>&nbsp;</small> | <small>Verify the LAN client is connected to the gateway and has obtained a valid IP address from the gateway DHCP server</small> | <small>Verify LAN client is connected to the gateway with a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Check internet connectivity from the LAN client by attempting to reach an external internet host</small> | <small>If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 5: Verify LAN client obtains IP from DUT DHCP server in router mode</strong></summary>

## Test Case 5: E2E_RouterMode_CheckLANIPAddress

## Objectives
Verify that when the gateway is configured in Router mode (bridge mode disabled), the wired Ethernet LAN client obtains its IP address exclusively from the DUT's DHCP server. Pings from the LAN client to both the Default Gateway WAN IP address and the DHCP server IP address must succeed, confirming proper layer-3 routing is operational.

## Test Case ID
TC_TDKB_E2E_203

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client – Wired Ethernet client |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode | router |

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode and Device.DHCPv4.Client.1.IPRouters and save the original values</small> | <small>&nbsp;</small> | <small>Verify both parameters are retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to "router"</small> | <small>&nbsp;</small> | <small>Verify the SET operation is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode</small> | <small>&nbsp;</small> | <small>Verify the retrieved value is "router". If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>Verify the LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Ping from the LAN client to the Default Gateway WAN IP address (value of Device.DHCPv4.Client.1.IPRouters)</small> | <small>Verify ping is successful. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Ping from the LAN client to the DHCP server IP address (value of Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress)</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to original value</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 6: Verify LAN client IP address falls within the configured DHCP range</strong></summary>

## Test Case 6: E2E_SANITY_CheckLANIPAddress

## Objectives
Verify that a wired LAN client connected to the gateway obtains an IP address and that the assigned IP address falls within the expected DHCP range configured on the DUT. The test retrieves the DUT's LAN IP address to derive the DHCP range and confirms the LAN client's IP falls within that range.

## Test Case ID
TC_TDKB_E2E_410

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| LAN Client – Wired Ethernet client |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | LAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and save the current LAN IP address</small> | <small>&nbsp;</small> | <small>Verify the LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the LAN client interface</small> | <small>Verify the LAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Verify the LAN client IP address is within the DHCP range defined by the DUT's Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 7: Verify configured SSID(s) are broadcasted and visible to WLAN client</strong></summary>

## Test Case 7: E2E_SANITY_WIFI_CheckSSIDBroadcast

## Objectives
Verify that the configured SSID(s) bands are broadcasted and visible to a WLAN client. The test sets the SSID names and key passphrases from the test configuration on the DUT, then confirms from the WLAN client that both SSIDs are discoverable on the network. 

## Test Case ID
TC_TDKB_E2E_401

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client – Wi-Fi client used to scan for available SSIDs |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| None | None |


## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.1.SSID and save the current SSID name</small> | <small>&nbsp;</small> | <small>Verify the SSID name is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Scan for available WiFi networks and check if the configured SSID name is listed</small> | <small>If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 8: Verify WLAN client connects to SSID(s) and obtains valid IP address</strong></summary>

## Test Case 8: E2E_SANITY_WIFI_ConnectTo_SSID

## Objectives
Verify that a WLAN client can successfully connect to SSID(s) configured on the DUT and that the WLAN client obtains a valid IP address within the expected DHCP range for each connection. 

## Test Case ID
TC_TDKB_E2E_402

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |
| WLAN Client – Wireless client |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| None | None |

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.1.SSID and save the current SSID name</small> | <small>&nbsp;</small> | <small>Verify the SSID name is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Wait 60 seconds</small> | <small>&nbsp;</small> | <small>&nbsp;</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Scan for available WiFi networks and check if the configured SSID name is listed</small> | <small>If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>&nbsp;</small> | <small>Connect to the configured WiFi SSID using the configured credentials</small> | <small>Verify WLAN client connected to the SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the WLAN client interface</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>Verify the Gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Verify the WLAN client IP address is within the DHCP range defined by Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>Verify WLAN IP is in the DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>&nbsp;</small> | <small>Disconnect from the 2.4GHz WiFi SSID</small> | <small>Verify WLAN client disconnected successfully. If the condition is met CONTINUE, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 9: Verify WLAN client connects to MLO SSID and accesses the internet</strong></summary>

## Test Case 9: E2E_WIFI_WLAN_AccessInternet

## Objectives
Verify that a WLAN (Wi-Fi) client can connect to the DUT's MLO SSID, obtain a valid IP address within the DHCP range, and successfully access the internet. The test confirms that the WLAN client's assigned IP falls within the expected range and that an external internet host is reachable via ping. This test is applicable to MLO-capable devices.

## Test Case ID
TC_TDKB_E2E_818

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT – Broadband residential gateway (RDKB, MLO-capable) |
| WLAN Client – Wireless client |

## Test Configuration

None

## Test Procedure and Expected Results

| Step Number | DUT | WLAN Client | TDK Validation and Expected Results |
|---|------------------------------|------------------------------|------------------------------|
| <small>1</small> | <small>GET Device.WiFi.SSID.{i}.SSID and Device.WiFi.AccessPoint.{i}.Security.KeyPassphrase for the configured SSID index</small> | <small>&nbsp;</small> | <small>Verify the retrieved SSID and key passphrase match the values in the device configuration file. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>&nbsp;</small> | <small>Connect to the MLO SSID using the configured credentials</small> | <small>Verify WLAN client connected to the SSID successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Get the IP address assigned to the WLAN client interface</small> | <small>Verify WLAN client obtained a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>&nbsp;</small> | <small>Verify the Gateway LAN IP address is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>&nbsp;</small> | <small>Verify the WLAN client IP address is within the DHCP range defined by Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</small> | <small>Verify WLAN IP is in the DHCP range. If the condition is met CONTINUE, else FAIL</small> |
| <small>6</small> | <small>&nbsp;</small> | <small>Ping the configured internet host from the WLAN client</small> | <small>If the condition is met PASS, else FAIL</small> |
| <small>7</small> | <small>&nbsp;</small> | <small>Disconnect from the WiFi SSID</small> | <small>&nbsp;</small> |

</details>

---

</details>

---

<details>
<summary><strong>SANITY - Status Checks</strong></summary>

# SANITY - Status Checks

<details>
<summary><strong>Test Case 10: Verify brlan0 LAN bridge interface is up and its IP matches the TR-181 parameter</strong></summary>

## Test Case 10: TS_SANITY_Is_brlan0_Up

## Objectives
This test verifies that the brlan0 LAN bridge interface is up and operational on the DUT. It checks that the IP address retrieved from the ifconfig command for brlan0 matches the IP address returned by the TR-181 parameter Device.X_CISCO_COM_DeviceControl.LanManagementEntry.{i}.LanIPAddress.

## Test Case ID
TC_SYSUTIL_1

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
|---|--------------------------------|--------------------------------|
| <small>1</small> | <small>Execute command to retrieve the IP address of brlan0 interface from ifconfig</small> | <small>Verify brlan0 interface is up and a valid IP address is obtained. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.{i}.LanIPAddress</small> | <small>Verify IP address is successfully retrieved from the TR-181 parameter. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Verify IP address retrieved from ifconfig matches the value of Device.X_CISCO_COM_DeviceControl.LanManagementEntry.{i}.LanIPAddress. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 11: Verify all CCSP processes are running on the DUT</strong></summary>

## Test Case 11: TS_SANITY_Is_CCSPProcesses_UP

## Objectives
This test verifies that all CCSP processes listed in the platform configuration are up and running on the DUT. For the CcspHotspot process, the test first checks whether xfinitywifi is enabled before verifying the process status. All other CCSP processes are verified to be running and returning valid PIDs.

## Test Case ID
TC_SYSUTIL_6

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
|---|--------------------------------|--------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable</small> | <small>Verify the xfinitywifi enable status is successfully retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Execute command to get the PID of the CcspHotspot process</small> | <small>Verify CcspHotspot is running if xfinitywifi is enabled, or verify it is not expected to run if xfinitywifi is disabled. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Execute command to get the PID of each remaining CCSP process</small> | <small>Verify each CCSP process is running and returns a valid PID. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 12: Verify core CCSP components CR, PandM, and PSM are running</strong></summary>

## Test Case 12: TS_SANITY_Is_CoreCCSP_UP

## Objectives
This test verifies that the three core CCSP components — Component Registrar (CR), CcspPandMSsp (PandM), and PsmSsp (PSM) — are up and running on the DUT. CR status is verified via dmcli, and PandM and PSM processes are verified to be running using their PIDs.

## Test Case ID
TC_SYSUTIL_5

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
|---|--------------------------------|--------------------------------|
| <small>1</small> | <small>Execute dmcli command to query the Component Registrar (CR) name value</small> | <small>Verify the CR component is up and the response does not indicate a missing destination component. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Execute command to get the PID of CcspPandMSsp</small> | <small>Verify CcspPandMSsp is running and returns a valid PID. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Execute command to get the PID of PsmSsp</small> | <small>Verify PsmSsp is running and returns a valid PID. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 13: Verify DUT WAN interface obtains an IP address after reboot</strong></summary>

## Test Case 13: TS_SANITY_Is_DeviceUp_AfterReboot

## Objectives
This test verifies that the DUT comes back up and its WAN interface obtains an IP address after a reboot. It first confirms the WAN interface is up before the reboot, then initiates a device reboot and verifies that the WAN interface successfully obtains an IP address after the device comes back online.

## Test Case ID
TC_SYSUTIL_7

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
|---|--------------------------------|--------------------------------|
| <small>1</small> | <small>Execute command to retrieve the WAN interface name from platform configuration</small> | <small>Verify the WAN interface name is successfully retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Execute command to retrieve the IP address of the WAN interface from ifconfig</small> | <small>Verify the WAN interface is up and has a valid IP address prior to reboot. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Reboot the DUT</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>Execute command to retrieve the IP address of the WAN interface from ifconfig after reboot</small> | <small>Verify the WAN interface is up and has a valid IP address after the device comes back online. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 14: Verify dnsmasq configuration file is present and the process is running</strong></summary>

## Test Case 14: TS_SANITY_Is_DNSMASQ_UP

## Objectives
This test verifies that the dnsmasq DNS service is properly configured and operational on the DUT. It checks that the dnsmasq configuration file is present at the expected path retrieved from the platform configuration, and that the dnsmasq process is actively running.

## Test Case ID
TC_SYSUTIL_29

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
|---|--------------------------------|--------------------------------|
| <small>1</small> | <small>Execute command to retrieve the dnsmasq configuration file path from platform configuration</small> | <small>Verify the dnsmasq configuration file path is successfully retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Execute command to check if the dnsmasq configuration file is present at the retrieved path</small> | <small>Verify the dnsmasq configuration file is present on the DUT. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Execute command to check if the dnsmasq process is running</small> | <small>Verify the dnsmasq process is running and returns a valid PID. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 15: Verify Dropbear SSH process is running on the DUT</strong></summary>

## Test Case 15: TS_SANITY_Is_WEBPA_UP

## Objectives
This test verifies that the Dropbear SSH process is running on the DUT. It retrieves the list of Dropbear processes to be verified from the platform configuration and checks that each process is active and returns a valid PID.

## Test Case ID
TC_SYSUTIL_17

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
|---|--------------------------------|--------------------------------|
| <small>1</small> | <small>Execute command to retrieve the list of DROPBEAR processes from platform configuration</small> | <small>Verify the DROPBEAR process list is successfully retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Execute command to get the PID of each DROPBEAR process</small> | <small>Verify each DROPBEAR process is running and returns a valid PID. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 16: Verify erouter0 WAN interface is up and its IP matches the TR-181 parameter</strong></summary>

## Test Case 16: TS_SANITY_Is_erouter0_Up

## Objectives
This test verifies that the erouter0 WAN interface is up and operational on the DUT. It checks that the IP address retrieved from the ifconfig command for erouter0 matches the IP address returned by the TR-181 parameter Device.IP.Interface.{i}.IPv4Address.{i}.IPAddress.

## Test Case ID
TC_SYSUTIL_2

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
|---|--------------------------------|--------------------------------|
| <small>1</small> | <small>Execute command to retrieve the IP address of erouter0 interface from ifconfig</small> | <small>Verify erouter0 interface is up and a valid IP address is obtained. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.IP.Interface.{i}.IPv4Address.{i}.IPAddress</small> | <small>Verify IP address is successfully retrieved from the TR-181 parameter. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>&nbsp;</small> | <small>Verify IP address retrieved from ifconfig matches the value of Device.IP.Interface.{i}.IPv4Address.{i}.IPAddress. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 17: Verify Lighttpd web server process is running on the DUT</strong></summary>

## Test Case 17: TS_SANITY_Is_LIGHTTPD_UP

## Objectives
This test verifies that the Lighttpd web server process is running on the DUT. It retrieves the list of Lighttpd processes to be verified from the platform configuration and checks that each process is active and returns a valid PID.

## Test Case ID
TC_SYSUTIL_16

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
|---|--------------------------------|--------------------------------|
| <small>1</small> | <small>Execute command to retrieve the list of LIGHTTPD processes from platform configuration</small> | <small>Verify the LIGHTTPD process list is successfully retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Execute command to get the PID of each LIGHTTPD process</small> | <small>Verify each LIGHTTPD process is running and returns a valid PID. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 18: Verify SNMP process is running on the DUT</strong></summary>

## Test Case 18: TS_SANITY_Is_SNMP_UP

## Objectives
This test verifies that the SNMP process is running on the DUT. It retrieves the list of SNMP processes to be verified from the platform configuration and checks that each process is active and returns a valid PID.

## Test Case ID
TC_SYSUTIL_14

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
|---|--------------------------------|--------------------------------|
| <small>1</small> | <small>Execute command to retrieve the list of SNMP processes from platform configuration</small> | <small>Verify the SNMP process list is successfully retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Execute command to get the PID of each SNMP process</small> | <small>Verify each SNMP process is running and returns a valid PID. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 19: Verify WEBPA process is running on the DUT</strong></summary>

## Test Case 19: TS_SANITY_Is_WEBPA_UP

## Objectives
This test verifies that the WEBPA process is running on the DUT. It retrieves the list of WEBPA processes to be verified from the platform configuration and checks that each process is active and returns a valid PID.

## Test Case ID
TC_SYSUTIL_15

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
|---|--------------------------------|--------------------------------|
| <small>1</small> | <small>Execute command to retrieve the list of WEBPA processes from platform configuration</small> | <small>Verify the WEBPA process list is successfully retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Execute command to get the PID of each WEBPA process</small> | <small>Verify each WEBPA process is running and returns a valid PID. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 20: Verify /minidumps directory is present on the DUT</strong></summary>

## Test Case 20: TS_SANITY_IsMinidumpsPresent

## Objectives
This test verifies that the /minidumps directory is present on the DUT under the ARM console. The presence of this directory is a prerequisite for storing process crash minidump files.

## Test Case ID
TC_SYSUTIL_27

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
|---|--------------------------------|--------------------------------|
| <small>1</small> | <small>Execute command to check if the /minidumps directory is present on the DUT</small> | <small>Verify the /minidumps directory is present under the ARM console. If the condition is met PASS, else FAIL</small> |

</details>

---

</details>

---

<details>
<summary><strong>SANITY - Behavioral Checks</strong></summary>

# SANITY - Behavioral Checks

<details>
<summary><strong>Test Case 21: Verify brlan0 obtains an IPv6 global address when DUT is in router mode</strong></summary>

## Test Case 21: TS_SANITY_CheckBrlan0IPV6_InRouterMode

## Objectives
Verify that the brlan0 interface obtains an IPv6 global address when the DUT is operating in router mode. If the device is not already in router mode, the test transitions it to router mode and confirms the brlan0 interface receives a valid IPv6 global-scope address.

## Test Case ID
TC_SYSUTIL_69

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.{i}.LanMode | router |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------------------|------------------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode</small> | <small>Verify that the GET operation succeeds and the initial LanMode value is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to router (only if initial value is bridge-static)</small> | <small>&nbsp;</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to verify the SET (only if SET was performed in Step 2)</small> | <small>Verify that the LanMode is now "router" and the SET reflects in GET. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Execute command to check if brlan0 interface has an IPv6 global address (ifconfig brlan0)</small> | <small>Verify that brlan0 has a valid IPv6 global-scope address when DUT is in router mode. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to original value (only if SET was performed in Step 2)</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 22: Verify brlan0 IPv6 address assignment behaviour across LAN mode transitions</strong></summary>

## Test Case 22: TS_SANITY_CheckBrlan0IPV6_WithLanModeTransition

## Objectives
Verify that the brlan0 interface does not obtain an IPv6 address when the DUT is in bridge-static mode, and that it correctly obtains an IPv6 address after transitioning the LAN mode to router mode. This test validates the IPv6 address assignment behaviour across LAN mode transitions.

## Test Case ID
TC_SYSUTIL_70

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.{i}.LanMode | bridge-static |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------------------|------------------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode</small> | <small>Verify that the GET operation succeeds and the initial LanMode value is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to bridge-static (only if initial value is router)</small> | <small>&nbsp;</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to verify the SET (only if SET was performed in Step 2)</small> | <small>Verify that the LanMode is now "bridge-static" and the SET reflects in GET. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Execute command to check if brlan0 interface has an IPv6 global address (ifconfig brlan0) while in bridge-static mode</small> | <small>Verify that brlan0 does NOT have an IPv6 global-scope address when DUT is in bridge-static mode. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to router</small> | <small>&nbsp;</small> |
| <small>6</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to verify the SET</small> | <small>Verify that the LanMode is now "router" and the SET reflects in GET. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Execute command to check if brlan0 interface has an IPv6 global address (ifconfig brlan0) while in router mode</small> | <small>Verify that brlan0 has a valid IPv6 global-scope address when DUT is in router mode. If the condition is met PASS, else FAIL</small> |
| <small>8</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to original value (only if SET was performed in Step 2)</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 23: Verify SelfHeal restores brlan0 interface within 15 minutes after it goes down</strong></summary>

## Test Case 23: TS_SANITY_CheckBrlan0SelfHeal

## Objectives
Verify that the SelfHeal mechanism brings up the brlan0 interface within 15 minutes after the interface has been brought down, given that the DUT is in router mode and SelfHeal is enabled. The test ensures that the device's self-recovery feature correctly restores the LAN bridge interface.

## Test Case ID
TC_SANITY_77

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.{i}.LanMode | router |
| Device.SelfHeal.X_RDKCENTRAL-COM_Enable | true |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------------------|------------------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode</small> | <small>Verify that the GET operation succeeds and the initial LanMode value is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to router (only if initial value is not router)</small> | <small>&nbsp;</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to verify the SET (only if SET was performed in Step 2)</small> | <small>Verify that the LanMode is now "router" and the SET reflects in GET. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>GET Device.SelfHeal.X_RDKCENTRAL-COM_Enable</small> | <small>Verify that the GET operation succeeds and the initial SelfHeal enable state is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>SET Device.SelfHeal.X_RDKCENTRAL-COM_Enable to true (only if initial value is false)</small> | <small>&nbsp;</small> |
| <small>6</small> | <small>GET Device.SelfHeal.X_RDKCENTRAL-COM_Enable to verify the SET (only if SET was performed in Step 5)</small> | <small>Verify that Device.SelfHeal.X_RDKCENTRAL-COM_Enable is now "true" and the SET reflects in GET. If the condition is met CONTINUE, else FAIL</small> |
| <small>7</small> | <small>Execute command to get the current IP address of brlan0 interface</small> | <small>Verify that brlan0 has a valid IP address. If the condition is met CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Execute command to get the current status (UP or DOWN) of brlan0 interface</small> | <small>Verify that brlan0 interface status is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>9</small> | <small>Execute command to bring the brlan0 interface DOWN (only if interface is currently UP)</small> | <small>&nbsp;</small> |
| <small>10</small> | <small>Execute command to verify brlan0 interface status is DOWN</small> | <small>Verify that brlan0 interface status is DOWN. If the condition is met CONTINUE, else FAIL</small> |
| <small>11</small> | <small>Poll brlan0 interface status in 60-second iterations for up to 15 minutes until status changes to UP</small> | <small>Verify that brlan0 interface comes back UP within 15 minutes due to SelfHeal recovery. If the condition is met PASS, else FAIL</small> |
| <small>12</small> | <small>Revert Device.SelfHeal.X_RDKCENTRAL-COM_Enable to original value (only if SET was performed in Step 5)</small> | <small>&nbsp;</small> |
| <small>13</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to original value (only if SET was performed in Step 2)</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 24: Verify dnsmasq process is not running in bridge-static mode</strong></summary>

## Test Case 24: TS_SANITY_CheckDNSMasqInBridgeMode

## Objectives
Verify that the dnsmasq process is not running when the DUT is operating in bridge-static mode. The test transitions the device to bridge-static mode if necessary, then confirms that dnsmasq is not active, as it is not expected to run in bridge mode.

## Test Case ID
TC_SYSUTIL_64

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.{i}.LanMode | bridge-static |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------------------|------------------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode</small> | <small>Verify that the GET operation succeeds and the current LanMode value is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to bridge-static (only if current value is not bridge-static)</small> | <small>&nbsp;</small> |
| <small>3</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to verify the SET</small> | <small>Verify that the LanMode is now "bridge-static" and the SET reflects in GET. If the condition is met CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Execute command to check if dnsmasq process is running (pidof dnsmasq)</small> | <small>Verify that dnsmasq is NOT running in bridge-static mode (no PID returned). If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 25: Verify no services are stuck in activating state after device boot</strong></summary>

## Test Case 25: TS_SANITY_CheckForAnyActivatingServices

## Objectives
Verify that no services are found in an activating state after the device boots up. The test retrieves the current device uptime and checks for activating services. If the device uptime exceeds 10 minutes and no activating services are found in the current session, it initiates a device reboot and confirms that no services remain stuck in the activating state after the device comes back up.

## Test Case ID
TC_SANITY_63

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
|---|------------------------------------------|------------------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.UpTime</small> | <small>Verify that the GET operation succeeds and the device uptime value is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Execute command to check for services in activating state (systemctl -a --state=activating \| grep activating)</small> | <small>Verify that no services are found in activating state in the current session. If activating services are found, mark as FAILURE. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Initiate device reboot and wait for device to come back up (only if uptime >= 600 seconds and no activating services found in Step 2)</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>Execute command to check for services in activating state after reboot (systemctl -a --state=activating \| grep activating)</small> | <small>Verify that no services are found in activating state after device boot-up. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 26: Verify no failed services are present after device reboot</strong></summary>

## Test Case 26: TS_SANITY_CheckForAnyFailedServices

## Objectives
Verify that no failed services are present on the DUT after a device reboot. The test initiates a reboot, waits for the device to come back up, then queries systemctl for any failed services and validates that none exist.

## Test Case ID
TC_SYSUTIL_38

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
|---|------------------------------------------|------------------------------------------|
| <small>1</small> | <small>Initiate device reboot and wait for device to come back up</small> | <small>&nbsp;</small> |
| <small>2</small> | <small>Execute command to check for failed services after reboot (systemctl -a --state=failed \| grep failed)</small> | <small>Verify that no failed services are present after device boot-up. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 27: Verify no duplicate instances of critical system processes are running</strong></summary>

## Test Case 27: TS_SANITY_CheckForDuplicateProcess

## Objectives
Verify that no duplicate instances of critical system processes are running on the DUT. The test retrieves the list of processes expected to have only a single instance from the test configuration, and for each process checks that exactly one instance is running. For conditional processes such as CcspTr069PaSsp, the TR-069 RFC feature is enabled if not already active before checking.

## Test Case ID
TC_SYSUTIL_40

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

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------------------|------------------------------------------|
| <small>1</small> | <small>Execute command to retrieve the list of processes expected to have a single instance from the test configuration file (LIST_OF_PROCESSES)</small> | <small>Verify that the process list is retrieved successfully. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable (only if CcspTr069PaSsp is in the process list)</small> | <small>Verify that the GET operation succeeds and the TR069 RFC enable status is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable to true (only if CcspTr069PaSsp is in the process list and value is not already true)</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable to verify the SET (only if SET was performed in Step 3)</small> | <small>Verify that Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable is now "true" and the SET reflects in GET. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute command to count the number of running instances of each process in the list (ps \| grep &lt;process&gt; \| grep -v grep \| wc -l)</small> | <small>Verify that each process in the list has exactly one running instance. If the condition is met PASS, else FAIL</small> |
| <small>6</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable to original value (only if SET was performed in Step 3)</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 28: Verify no zombie (defunct) processes are present on the DUT</strong></summary>

## Test Case 28: TS_SANITY_CheckForZombieProcess

## Objectives
Verify that no zombie (defunct) processes are present on the DUT. The test executes a process listing command and checks that none of the running processes have a defunct status, ensuring the DUT is free of zombie processes.

## Test Case ID
TC_SYSUTIL_44

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
|---|------------------------------------------|------------------------------------------|
| <small>1</small> | <small>Execute command to check for zombie (defunct) processes (ps \| grep -rn " Z" \| grep -v grep)</small> | <small>Verify that no zombie (defunct) processes are found on the DUT. If the condition is met PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 29: Verify bridge-static LAN mode setting persists after device reboot</strong></summary>

## Test Case 29: TS_SANITY_CheckLanMode_AfterReboot

## Objectives
Verify that the bridge-static LAN mode setting persists after a device reboot. The test records the current LAN mode, sets it to bridge-static, reboots the device, and confirms that the bridge-static mode is retained after the device comes back up, before reverting to the original value.

## Test Case ID
TC_SYSUTIL_10

## Test Type
Positive

## Test Environment

| Component |
|-----------|
| DUT - Device under test |

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.{i}.LanMode | bridge-static |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|---|------------------------------------------|------------------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode</small> | <small>Verify that the GET operation succeeds and the current LanMode value is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to bridge-static</small> | <small>&nbsp;</small> |
| <small>3</small> | <small>Initiate device reboot and wait for device to come back up</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode after reboot</small> | <small>Verify that the LanMode is "bridge-static" after reboot, confirming the setting persisted. If the condition is met PASS, else FAIL</small> |
| <small>5</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 30: Verify Lighttpd process remains running across LAN mode transitions</strong></summary>

## Test Case 30: TS_SANITY_CheckLighttpdProcess_OnLanModeTransition

## Objectives
Verify that the lighttpd process continues to run on the DUT when the LAN mode is transitioned between router and bridge-static modes. The test checks lighttpd is running before and after a LAN mode transition (from router to bridge-static or vice-versa), confirming that the web server process is unaffected by LAN mode changes.

## Test Case ID
TC_SANITY_65

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
|---|------------------------------------------|------------------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode</small> | <small>Verify that the GET operation succeeds and the initial LanMode value is retrieved. If the condition is met CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Execute command to check if the lighttpd process is running (pidof lighttpd)</small> | <small>Verify that the lighttpd process is running and a valid PID is returned. If the condition is met CONTINUE, else FAIL</small> |
| <small>3</small> | <small>SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to the opposite mode (bridge-static if initial is router; router if initial is bridge-static)</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to verify the SET</small> | <small>Verify that the LanMode has transitioned to the expected mode and the SET reflects in GET. If the condition is met CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute command to check if the lighttpd process is still running after LAN mode transition (pidof lighttpd)</small> | <small>Verify that the lighttpd process is still running after the LAN mode transition. If the condition is met PASS, else FAIL</small> |
| <small>6</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to original value</small> | <small>&nbsp;</small> |

</details>

---

<details>
<summary><strong>Test Case 31: Verify minidump file is created and process recovers after a crash</strong></summary>

## Test Case 31: TS_SANITY_CheckMinidumpsAfterProcessCrash

## Objectives
To verify that a minidump file is created under the /minidumps directory after a process crash. The test crashes the CcspPandMSsp process using a segmentation fault signal and confirms that the dump file count in /minidumps increases. It also verifies that CcspPandMSsp recovers and resumes running after the crash.

## Test Case ID
TC_SYSUTIL_28

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
|-------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <small>1</small> | <small>Check if the CcspPandMSsp process is running and retrieve its PID</small> | <small>If the process is running and a valid PID is returned, CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Get the count of .dmp files present in /minidumps before the process crash</small> | <small>If the count is retrieved successfully, CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Send signal SIGSEGV (-11) to the CcspPandMSsp process to induce a crash</small> | <small>If the crash command executes successfully, CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Get the count of .dmp files present in /minidumps after the process crash and list the dump files</small> | <small>If the dump file count after crash is greater than the count before crash, CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Poll for CcspPandMSsp process to restart (retry every 10 seconds up to 6 times; if not up, retry every 5 minutes up to 6 times)</small> | <small>If the CcspPandMSsp process is running again with a valid PID, PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 32: Verify all critical processes are running within expected uptime after factory reset</strong></summary>

## Test Case 32: TS_SANITY_CheckProcessUptimeAfterFactoryReset

## Objectives
To verify that all critical processes are up and running on the DUT within the expected uptime after a factory reset. The test initiates a factory reset, waits for the device to restore, and then checks that each process in the configured critical process list is running using its PID.

## Test Case ID
TC_SYSUTIL_80

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
|-------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <small>1</small> | <small>Get the maximum process uptime wait time (MAX_PROCESSUP_WAITTIME) from the test configuration</small> | <small>If the wait time value is retrieved successfully, CONTINUE, else FAIL</small> |
| <small>2</small> | <small>SET Device.X_CISCO_COM_DeviceControl.FactoryReset to initiate a factory reset on the DUT</small> | <small>If the factory reset is initiated successfully, CONTINUE, else FAIL</small> |
| <small>3</small> | <small>After the DUT comes back up post factory reset, retrieve the current system uptime</small> | <small>If the uptime is retrieved successfully, CONTINUE, else FAIL</small> |
| <small>4</small> | <small>If the current uptime is less than MAX_PROCESSUP_WAITTIME, wait for the remaining duration before proceeding</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Get the list of critical processes (CCSP_PROCESS, SNMP_PROCESS, WEBPA_PROCESS, LIGHTTPD_PROCESS, DROPBEAR_PROCESS, NOTIFYCOMP_PROCESS, WEBCONFIG_PROCESS, PSM_PROCESS, TELEMETRY_PROCESS, WIFI_PROCESS) from the test configuration</small> | <small>If the process list is retrieved and is non-empty, CONTINUE, else FAIL</small> |
| <small>6</small> | <small>For each process in the list, check if the process is running using its PID. For CcspHotspot, first GET Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable; skip the process check if xfinitywifi is disabled</small> | <small>If all applicable processes are running with valid PIDs, PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 33: Verify all critical processes are running within expected uptime after reboot</strong></summary>

## Test Case 33: TS_SANITY_CheckProcessUptimeAfterReboot

## Objectives
To verify that all critical processes are up and running on the DUT within the expected uptime after a device reboot. The test initiates a reboot, waits for the device to come back up, and then checks that each process in the configured critical process list is running using its PID.

## Test Case ID
TC_SYSUTIL_39

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
|-------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <small>1</small> | <small>Get the maximum process uptime wait time (MAX_PROCESS_UPTIME) from the test configuration</small> | <small>If the wait time value is retrieved successfully, CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Initiate a reboot on the DUT</small> | <small>&nbsp;</small> |
| <small>3</small> | <small>After the DUT comes back up, GET Device.DeviceInfo.UpTime</small> | <small>If the uptime is retrieved successfully, CONTINUE, else FAIL</small> |
| <small>4</small> | <small>If Device.DeviceInfo.UpTime is less than MAX_PROCESS_UPTIME, wait for the remaining duration before proceeding</small> | <small>&nbsp;</small> |
| <small>5</small> | <small>Get the list of critical processes (CCSP_PROCESS, SNMP_PROCESS, WEBPA_PROCESS, LIGHTTPD_PROCESS, DROPBEAR_PROCESS, NOTIFYCOMP_PROCESS, WEBCONFIG_PROCESS, PSM_PROCESS, TELEMETRY_PROCESS, WIFI_PROCESS) from the test configuration</small> | <small>If the process list is retrieved and is non-empty, CONTINUE, else FAIL</small> |
| <small>6</small> | <small>For each process in the list, check if the process is running using its PID. For CcspHotspot, first GET Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable; skip the process check if xfinitywifi is disabled</small> | <small>If all applicable processes are running with valid PIDs, PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 34: Verify TR-069 RFC parameter is consistent with syscfg and controls CcspTr069PaSsp process</strong></summary>

## Test Case 34: TS_SANITY_CheckTR069RFC_AndTR069Process

## Objectives
To verify that the TR-181 parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable is consistent with the EnableTR69Binary value stored in syscfg.db. The test also validates that toggling the RFC parameter causes the CcspTr069PaSsp process to start or stop accordingly, and reverts the parameter to its initial state after the test.

## Test Case ID
TC_SYSUTIL_43

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable | Toggled from initial value (true/false) |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|-------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable</small> | <small>If the value is retrieved successfully, CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Get the value of EnableTR69Binary from syscfg.db using syscfg get</small> | <small>If the value is retrieved successfully, CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Compare the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable with EnableTR69Binary from syscfg.db</small> | <small>If both values are equal, CONTINUE, else FAIL</small> |
| <small>4</small> | <small>If RFC is enabled (true): check that the CcspTr069PaSsp process is running. If RFC is disabled (false): SET Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable to true and wait 15 seconds</small> | <small>If the condition is met (process running when enabled / SET succeeds when disabled), CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Get the updated value of EnableTR69Binary from syscfg.db after the SET</small> | <small>If the value is retrieved successfully, CONTINUE, else FAIL</small> |
| <small>6</small> | <small>Compare the SET value with the updated EnableTR69Binary from syscfg.db</small> | <small>If both values are equal, CONTINUE, else FAIL</small> |
| <small>7</small> | <small>If RFC was enabled: verify CcspTr069PaSsp is NOT running after SET to false. If RFC was disabled: verify CcspTr069PaSsp IS running after SET to true</small> | <small>If the process state matches the toggled RFC value, CONTINUE, else FAIL</small> |
| <small>8</small> | <small>Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable to its original value</small> | <small>If the revert operation is successful, PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 35: Verify UDHCPC zombie process is not present before and after reboot</strong></summary>

## Test Case 35: TS_SANITY_CheckUDHCPCZombie

## Objectives
To verify that the UDHCPC zombie process is not running on the DUT. The test checks the device uptime and the presence of UDHCPC zombie processes before and after a reboot (if uptime is greater than 5 minutes), ensuring the device remains free of UDHCPC zombie processes.

## Test Case ID
TC_SYSUTIL_79

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
|-------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <small>1</small> | <small>GET Device.DeviceInfo.UpTime</small> | <small>If the uptime is retrieved successfully as a valid integer, CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Check if a UDHCPC zombie process is present on the DUT by running: ps \| grep "[udhcpc]"</small> | <small>If no UDHCPC zombie process is found, CONTINUE, else FAIL</small> |
| <small>3</small> | <small>If Device.DeviceInfo.UpTime is greater than or equal to 300 seconds and no zombie was found, initiate a device reboot and wait 360 seconds for the DUT to come back up</small> | <small>&nbsp;</small> |
| <small>4</small> | <small>After reboot, check if a UDHCPC zombie process is present on the DUT by running: ps \| grep "[udhcpc]"</small> | <small>If no UDHCPC zombie process is found after reboot, PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 36: Verify LAN IP address set via TR-181 is reflected in brlan0 ifconfig output</strong></summary>

## Test Case 36: TS_SANITY_SetLanManagementEntryLanIPAddress

## Objectives
To verify that the LAN IP address set via the TR-181 parameter Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress is correctly reflected in the ifconfig output of the brlan0 interface. The test iterates through a list of configured private IP addresses, sets each one, and verifies the change takes effect on the brlan0 interface within 20 seconds.

## Test Case ID
TC_SYSUTIL_31

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test |

## Test Configuration
| Parameter | Value |
|-----------|-------|
| Device.X_CISCO_COM_DeviceControl.LanManagementEntry.{i}.LanIPAddress | As per test configuration |

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|-------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <small>1</small> | <small>GET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress; also retrieve the IP address from ifconfig brlan0</small> | <small>If both values are retrieved and are equal, CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Get the list of LAN IP addresses to test (LAN_IPADDRESS) from the test configuration</small> | <small>If the IP address list is retrieved and is non-empty, CONTINUE, else FAIL</small> |
| <small>3</small> | <small>For each IP address in the list (excluding the current default IP): SET Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress; wait 20 seconds; verify the new IP is reflected in ifconfig brlan0</small> | <small>If all SET IP addresses are reflected correctly in ifconfig brlan0, CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to the original value retrieved in Step 1</small> | <small>If the revert operation is successful, PASS, else FAIL</small> |

</details>

---

</details>

---

<details>
<summary><strong>CCSP Common - MBUS</strong></summary>

# CCSP Common - MBUS

<details>
<summary><strong>Test Case 37: Verify CcspBaseIf_busCheck returns CCSP_Message_Bus_OK via the message bus</strong></summary>

## Test Case 37: TS_CCSPCOMMON_MBUS_BusCheck

## Objectives
To validate the CCSP Base Interface CcspBaseIf_busCheck function. The test initialises the CCSP message bus, registers the message bus path and capabilities, and then invokes the bus check function. The expected outcome is that CcspBaseIf_busCheck returns CCSP_Message_Bus_OK [100] via the Component Registry (CR) over the message bus.

## Test Case ID
TC_CCSPMBUS_17

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
|-------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <small>1</small> | <small>Load the CCSP message bus configuration using CCSPMBUS_LoadCfg with TDKB.cfg</small> | <small>If message bus configuration loads successfully, CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Initialise the CCSP message bus using CCSPMBUS_Init with /tmp/ccsp_msg.cfg</small> | <small>If message bus initialisation is successful, CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Register the message bus path using CCSPMBUS_RegisterPath</small> | <small>If the path registration is successful, CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Register CCSP capabilities using CCSPMBUS_RegisterCapabilities</small> | <small>If the capability registration is successful, CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute the CCSP Base Interface bus check function (CcspBaseIf_busCheck) via CCSPMBUS_BusCheck; verify the return status is CCSP_Message_Bus_OK [100]</small> | <small>If the return status is CCSP_Message_Bus_OK [100], PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 38: Verify CcspBaseIf_isSystemReady returns OK and confirms all components are ready via message bus</strong></summary>

## Test Case 38: TS_CCSPCOMMON_MBUS_IsSystemReady

## Objectives
To validate the CCSP Base Interface CcspBaseIf_isSystemReady function. The test initialises the CCSP message bus, registers the message bus path and capabilities, and then invokes the IsSystemReady function. The expected outcome is that CcspBaseIf_isSystemReady returns CCSP_Message_Bus_OK [100] and provides a non-null readyStatus output argument, confirming that the system and all registered components are ready via the Component Registry (CR) over the message bus.

## Test Case ID
TC_CCSPMBUS_20

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
|-------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <small>1</small> | <small>Load the CCSP message bus configuration using CCSPMBUS_LoadCfg with TDKB.cfg</small> | <small>If message bus configuration loads successfully, CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Initialise the CCSP message bus using CCSPMBUS_Init with /tmp/ccsp_msg.cfg</small> | <small>If message bus initialisation is successful, CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Register the message bus path using CCSPMBUS_RegisterPath</small> | <small>If the path registration is successful, CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Register CCSP capabilities using CCSPMBUS_RegisterCapabilities</small> | <small>If the capability registration is successful, CONTINUE, else FAIL</small> |
| <small>5</small> | <small>Execute the CCSP Base Interface IsSystemReady function (CcspBaseIf_isSystemReady) via CCSPMBUS_IsSystemReady; verify the return status is CCSP_Message_Bus_OK [100] and the readyStatus output argument is non-null</small> | <small>If the return status is CCSP_Message_Bus_OK [100] and readyStatus is non-null, PASS, else FAIL</small> |

</details>

---

</details>

---

<details>
<summary><strong>RBUS</strong></summary>

# RBUS

<details>
<summary><strong>Test Case 39: Verify RBUS session creation and closure complete successfully</strong></summary>

## Test Case 39: TS_RBUS_CreateAndCloseSession

## Objectives
To verify the session lifecycle handling provided by the RBUS APIs rbus_createSession and rbus_closeSession. The test opens an RBUS connection, creates a session and stores the returned session ID, closes the session using that session ID, and then closes the RBUS connection, confirming that both session creation and closure complete successfully.

## Test Case ID
TC_RBUS_18

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test (must be in RBUS mode) |

## Test Configuration
None

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|-------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <small>1</small> | <small>Open the RBUS connection using the rbus_open API</small> | <small>If rbus_open returns success, CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Create an RBUS session using the rbus_createSession API and store the returned session ID</small> | <small>If rbus_createSession returns success and a valid session ID is obtained, CONTINUE, else FAIL</small> |
| <small>3</small> | <small>Close the RBUS session using the rbus_closeSession API with the session ID obtained in Step 2</small> | <small>If rbus_closeSession returns success, CONTINUE, else FAIL</small> |
| <small>4</small> | <small>Close the RBUS connection using the rbus_close API</small> | <small>If rbus_close returns success, PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 40: Verify rbus_open and rbus_close APIs complete successfully</strong></summary>

## Test Case 40: TS_RBUS_OpenAndClose

## Objectives
To validate the RBUS 2.0 APIs rbus_open and rbus_close. The test opens an RBUS connection using rbus_open with the component name "tdk_b" and then closes the connection using rbus_close, verifying that both operations complete successfully.

## Test Case ID
TC_RBUS_16

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
|-------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <small>1</small> | <small>Open the RBUS connection using the rbus_open API with component name "tdk_b"</small> | <small>If rbus_open returns success, CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Close the RBUS connection using the rbus_close API</small> | <small>If rbus_close returns success, PASS, else FAIL</small> |

</details>

---

<details>
<summary><strong>Test Case 41: Verify rbus_openBrokerConnection and rbus_closeBrokerConnection APIs complete successfully</strong></summary>

## Test Case 41: TS_RBUS_OpenAndCloseBrokerConnection

## Objectives
To validate the RBUS APIs rbus_openBrokerConnection and rbus_closeBrokerConnection. The test opens an RBUS broker connection using rbus_openBrokerConnection with the component name "tdk-b" and then closes it using rbus_closeBrokerConnection, verifying that both operations complete successfully on a DUT in RBUS mode.

## Test Case ID
TC_RBUS_32

## Test Type
Positive

## Test Environment
| Component |
|-----------|
| DUT - Device under test (must be in RBUS mode) |

## Test Configuration
None

## Test Procedure and Expected Results

| Step Number | DUT | TDK Validation and Expected Results |
|-------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <small>1</small> | <small>Open the RBUS broker connection using the rbus_openBrokerConnection API with component name "tdk-b"</small> | <small>If rbus_openBrokerConnection returns success, CONTINUE, else FAIL</small> |
| <small>2</small> | <small>Close the RBUS broker connection using the rbus_closeBrokerConnection API</small> | <small>If rbus_closeBrokerConnection returns success, PASS, else FAIL</small> |

</details>

---

</details>

---

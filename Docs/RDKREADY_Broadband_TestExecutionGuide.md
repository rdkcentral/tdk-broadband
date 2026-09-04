# RDK Ready Broadband — Test Execution Guide

<strong>Version</strong>: 1.0<br>
<strong>Date</strong>: September 2026<br>
<strong>Purpose</strong>: Test Execution Guide for RDK Ready Broadband Certification Program<br>
<strong>Maintained by</strong>: TDKB Test Automation Team

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Scope](#2-scope)
3. [Test Environment Setup](#3-test-environment-setup)
    - 3.1 [Hardware Configuration](#31-hardware-configuration)
    - 3.2 [Hardware Requirements](#32-hardware-requirements)
    - 3.3 [Software Requirements](#33-software-requirements)
    - 3.4 [Wi-Fi Client Setup](#34-wifi-client-setup)
    - 3.5 [Device Configuration File](#35-device-configuration-file)
4. [Prerequisites](#4-prerequisites)
5. [Test Suite Categories](#5-test-suite-categories)
   - 5.1 [Platform Compliance Validation Suite](#51-platform-compliance-validation-suite)
   - 5.2 [Device Management Validation Suite](#52-device-management-validation-suite)
   - 5.3 [Data Model Validation Suite](#53-data-model-validation-suite)
   - 5.4 [Connectivity & Platform Services Validation Suite](#54-connectivity--platform-services-validation-suite)
   - 5.5 [Vendor Test Suite](#55-vendor-test-suite)
   - 5.6 [Performance and Stability Validation Suite](#56-performance-and-stability-validation-suite)
6. [Execution Rules](#6-execution-rules)
7. [Pass/Fail Criteria](#7-passfail-criteria)
    - 7.1 [Test Case Level](#71-test-case-level)
    - 7.2 [Suite Level](#72-suite-level)
8. [Glossary](#8-glossary)
9. [Appendix for test configurations](#9-appendix-for-test-configurations)

---

## 1. Introduction

This document provides a comprehensive Test Execution Guide for the **RDK Ready Broadband Certification** program. It defines the structured approach for validating that broadband devices meet the functional, compliance, and performance requirements established by the RDK-B specification.

---

## 2. Scope

This guide covers the end-to-end test execution process for RDK Ready Broadband certification and Execution prerequisites and environment configuration.

---

## 3. Test Environment Setup

### 3.1 Hardware Configuration

The following hardware components are used in the TDK-B E2E setup:

**Broadband Router**

![Broadband Router Setup](TestSetupConfiguration/images/broadband_router_setup.png)

> **Note:**
> - **WiFi Chamber:** Good to have in case a lot of WiFi interference is observed. Mainly the device under test and WiFi client need to be placed inside the WiFi chamber.
> - Client devices support is provided for Ubuntu 16.04, 18.04, 20.04, 22.04 (tested so far).

---

### 3.2 Hardware Requirements

- Test Manager machine (Ubuntu)
- LAN Client — RPI/Laptop (Ubuntu 18.04 / 20.04 / 22.04 / 24.04)
- WAN Client — RPI/Laptop (Ubuntu 18.04 / 20.04 / 22.04 / 24.04)
- WLAN Client — RPI/Laptop (Ubuntu 18.04 / 20.04 / 22.04 / 24.04)
- Device under test — Broadband Router

> **Note:**
> - Currently E2E test scripts are validated only with client devices as separate Linux systems. Virtual Machines can also be used as LAN/WAN client devices if each VM has a different IP (not validated). For WiFi client, it should have an external WiFi adapter (not validated).
> - In case of WLAN client as a laptop, a WiFi driver with dual band support will be available by default. In case of WLAN client as any other system which supports only 2.4 GHz WiFi by default, an external 5 GHz WiFi adapter may be required.
> - In case of WLAN client which does not support 6 GHz WiFi by default, an external 6 GHz WiFi adapter may be required.

---

### 3.3 Software Requirements

### RPI Ubuntu Image

> This section applies when an RPI is used as a client system (LAN/WAN/WLAN client).

Download the RPI Ubuntu image: `ubuntu-mate-<version>-desktop-armhf-raspberry-pi` from the link below and bring the client device up.

- https://ubuntu-mate.org/raspberry-pi/

---

### Steps to Follow While Building the Docker Image

The Docker image is used to set up the client systems (LAN, WAN, and WLAN). Each client runs a Docker container that provides the required services and acts as the test client during E2E script execution. Use the following folder structure while building the Docker image:

![Docker Folder Structure](TestSetupConfiguration/images/docker_folder_structure.png)

**Setup files:** [Dockerfile](TestSetupConfiguration/setup_files/Dockerfile), [start-services.sh](TestSetupConfiguration/setup_files/start-services.sh), [telnet](TestSetupConfiguration/setup_files/telnet), [tftp](TestSetupConfiguration/setup_files/tftp), [xinetd.conf](TestSetupConfiguration/setup_files/xinetd.conf)

1. Place the `Dockerfile`, `start-services.sh`, `telnet`, `tftp`, `xinetd.conf`, and [`tdkbE2EClientScripts`](https://github.com/rdkcentral/tdk-core/tree/main/framework/fileStore/tdkbE2EClientScripts) in the same folder as shown in the picture above.

2. Before building the image, specify the username and password for clients in the `start-services.sh` file.

   > **Note:** The username configured in `start-services.sh` should **not** be the same as the host username. You can choose any username as it is the username for clients.

   ```bash
   # Set username and password
   USERNAME="client_tdkb"
   PASSWORD="********"
   ```

3. Build the Docker image with the following command:

   ```bash
   sudo docker build -t <name-of-the-docker-image> .
   ```

   > **Note:** You can use any name for the Docker image.

4. After completing the build process, verify that the Docker image has been created:

   ```bash
   sudo docker images
   ```

   > **Note:** On a new system, Docker commands may require `sudo` permissions. Use `sudo` with Docker commands or run them as the root user. You can also add the current user to the `docker` group to run Docker without `sudo` by referring to: https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo

5. Once the Docker image build is complete, place the Docker image on all the client systems.
   Use the `docker save` and `docker load` commands to transfer the Docker image to the client systems, or build the Docker image directly on the client system by following the steps above.

---

### Steps to Create Docker Container in WLAN Client System

After placing the Docker image on the WLAN client system:

1. Before proceeding, ensure that services like SSH, Apache2, vsftpd, and xinetd are **stopped** on the host system.
2. Disable FTP, HTTP, HTTPS, and TELNET ports on the host machine (use `systemctl` commands) before creating the Docker container.

3. Create the container using the following command:

   ```bash
   sudo docker run --network host --privileged \
     -v /var/run/dbus:/var/run/dbus \
     -v /var/run/NetworkManager:/var/run/NetworkManager \
     -v /etc/NetworkManager:/etc/NetworkManager \
     <image-name>
   ```

4. Verify the container has been created:

   ```bash
   sudo docker ps
   ```

5. Log in to the container:

   ```bash
   sudo docker exec -it <Container-ID> bash
   ```

6. Switch to the user created in the container:

   ```bash
   su <Username-specified-in-start-services.sh>
   ```

---

### Steps to Create Docker Container in LAN and WAN Systems

After placing the Docker image on the LAN and WAN client systems:

1. Before proceeding, ensure that services like SSH, Apache2, vsftpd, and xinetd are **stopped** on the host system.
2. Disable FTP, HTTP, HTTPS, and TELNET ports on the host machine (use `systemctl` commands) before creating the Docker container.

3. Create the container using the following command:

   ```bash
   sudo docker run -d --privileged --network host <image-name>
   ```

4. Verify the container has been created:

   ```bash
   sudo docker ps
   ```

5. Log in to the container:

   ```bash
   sudo docker exec -it <Container-ID> bash
   ```

6. Switch to the user created in the container:

   ```bash
   su <Username-specified-in-start-services.sh>
   ```

After the containers are created on the client systems, the containers will act as clients. Test script execution can begin after updating the device config file.

---

### 3.4 WiFi Client Setup

Ensure the following commands are working after the basic installations are done in the WLAN client.

**1. Check whether the WiFi SSIDs are listed in the WiFi networks:**

```bash
nmcli device wifi list | grep <SSIDNAME>
# Example:
nmcli device wifi list | grep "BPI-RDKB-MLO-AP"
```

**2. Connect to one of the SSIDs listed in the WiFi network:**

```bash
nmcli device wifi connect <SSIDNAME> password <PASSWORD>
# Example:
nmcli device wifi connect BPI-RDKB-MLO-AP password <PASSWORD>
```

**3. Disconnect from the connected SSID:**

```bash
nmcli device disconnect <WLAN_INTERFACE>
# Example:
nmcli device disconnect wlan0
```

---

### 3.5 Device Configuration File

Configuration details are to be populated as per sampleDevice.config and made available under tdkbDeviceConfig/ in the Test Manager Filestore. 

<details id="e2e-configuration">
<summary><strong>E2E Configuration</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">
#This section should have your device name. eg: If device name is RDKB-GW then the below section name and file name needs to be RDKB-GW.config
[sampleDevice.config]

#Setup type can be TDK/WEBPA.
SETUP_TYPE = TDK

################################# 2.4GHZ WIFI DETAILS ######################################

#Unique WIFI 2.4GHZ SSID Name
SSID_2GHZ_NAME = WIFI-2.4

#WIFI 2.4GHZ SSID password
SSID_2GHZ_PWD = wifitest123

#WIFI 2.4GHZ SSID Invalid password
SSID_2GHZ_INVALID_PWD = mywifipassword

#WEBPA WIFI 2.4GHZ SSID index. Index will be 1 for TDK and 10001 for WEBPA
WEBPA_SSID_2GHZ_INDEX = 10001

#WEBPA WIFI 2.4GHZ Radio index. Index will be 1 for TDK and 10000 for WEBPA
WEBPA_RADIO_2GHZ_INDEX = 10000

#TDK WIFI 2.4GHZ SSID index. Index will be 1 for TDK and 10001 for WEBPA
TDK_SSID_2GHZ_INDEX = 1

#TDK WIFI 2.4GHZ Radio index. Index will be 1 for TDK and 10000 for WEBPA
TDK_RADIO_2GHZ_INDEX = 1

#WIFI connection status log. wlan0 should be replaced by your wifi interface name
WLAN_2GHZ_SSID_CONNECT_STATUS = Device 'wlan0' successfully activated

#WIFI disconnection status log. wlan0 should be replaced by your wifi interface name
WLAN_2GHZ_SSID_DISCONNECT_STATUS = Device 'wlan0' successfully disconnected

#WLAN 2.4GHz client's throughput in Mbps while transferring data to WAN
WLAN_2GHZ_THROUGHPUT_TO_WAN =

#WLAN 2.4GHz client's throughput in Mbps while transferring data to another LAN
WLAN_2GHZ_THROUGHPUT_TO_LAN =

#Temporary file in wlan client, to write the throughput data of 2.4GHz frequency
WLAN_2GHZ_THROUGHPUT_OUTFILE =

################################# 5GHZ WIFI DETAILS ######################################

#Unique WIFI 5GHZ SSID Name
SSID_5GHZ_NAME = WIFI-5

#WIFI 5GHZ SSID password
SSID_5GHZ_PWD = wifitest123

#WIFI 5GHZ SSID Invalid password
SSID_5GHZ_INVALID_PWD = mywifipassword

#WEBPA WIFI 5GHZ SSID index. Index will be 2 for TDK and 10101 for WEBPA
WEBPA_SSID_5GHZ_INDEX = 10101

#WEBPA WIFI 5GHZ Radio index. Index will be 2 for TDK and 10100 for WEBPA
WEBPA_RADIO_5GHZ_INDEX = 10100

#TDK WIFI 5GHZ SSID index. Index will be 2 for TDK and 10101 for WEBPA
TDK_SSID_5GHZ_INDEX = 2

#TDK WIFI 5GHZ Radio index. Index will be 2 for TDK and 10100 for WEBPA
TDK_RADIO_5GHZ_INDEX = 2

#WIFI connection status log. wlan1 should be replaced by your wifi interface name
WLAN_5GHZ_SSID_CONNECT_STATUS = Device 'wlan1' successfully activated

#WIFI disconnection status log. wlan1 should be replaced by your wifi interface name
WLAN_5GHZ_SSID_DISCONNECT_STATUS = Device 'wlan1' successfully disconnected

#WLAN 5GHz client's throughput in Mbps while transferring data to WAN
WLAN_5GHZ_THROUGHPUT_TO_WAN =

#WLAN 5GHz client's throughput in Mbps while transferring data to another LAN
WLAN_5GHZ_THROUGHPUT_TO_LAN =

#Temporary file in wlan client, to write the throughput data of 2.4GHz frequency
WLAN_5GHZ_THROUGHPUT_OUTFILE =

################################# 6GHZ WIFI DETAILS ######################################

#Unique WIFI 6GHZ SSID Name
SSID_6GHZ_NAME = WIFI-6

#WIFI 6GHZ SSID password
SSID_6GHZ_PWD = wifitest123

#WIFI 6GHZ SSID Invalid password
SSID_6GHZ_INVALID_PWD = mywifipassword

#WEBPA WIFI 6GHZ SSID index. Index will be 17 for TDK and 10201 for WEBPA
WEBPA_SSID_6GHZ_INDEX = 10201

#WEBPA WIFI 6GHZ Radio index. Index will be 3 for TDK and 10200 for WEBPA
WEBPA_RADIO_6GHZ_INDEX = 10200

#TDK WIFI 6GHZ SSID index. Index will be 17 for TDK and 10201 for WEBPA
TDK_SSID_6GHZ_INDEX = 17

#TDK WIFI 6GHZ Radio index. Index will be 3 for TDK and 10200 for WEBPA
TDK_RADIO_6GHZ_INDEX = 3

#WIFI connection status log. wlan1 should be replaced by your wifi interface name
WLAN_6GHZ_SSID_CONNECT_STATUS = Device 'wlan1' successfully activated

#WIFI disconnection status log. wlan1 should be replaced by your wifi interface name
WLAN_6GHZ_SSID_DISCONNECT_STATUS = Device 'wlan1' successfully disconnected

#WLAN 6GHz client's throughput in Mbps while transferring data to WAN
WLAN_6GHZ_THROUGHPUT_TO_WAN =

#WLAN 6GHz client's throughput in Mbps while transferring data to another LAN
WLAN_6GHZ_THROUGHPUT_TO_LAN =

#Temporary file in wlan client, to write the throughput data of 6GHz frequency
WLAN_6GHZ_THROUGHPUT_OUTFILE =

################################# Public WIFI DETAILS ######################################

#WIFI connection status log. wlan0 should be replaced by your wifi interface name
WLAN_2GHZ_PUBLIC_SSID_CONNECT_STATUS = Device 'wlan0' successfully activated

#WIFI disconnection status log. wlan0 should be replaced by your wifi interface name
WLAN_2GHZ_PUBLIC_SSID_DISCONNECT_STATUS = Device 'wlan0' successfully disconnected

#WIFI connection status log. wlan1 should be replaced by your wifi interface name
WLAN_5GHZ_PUBLIC_SSID_CONNECT_STATUS = Device 'wlan1' successfully activated

#WIFI disconnection status log. wlan1 should be replaced by your wifi interface name
WLAN_5GHZ_PUBLIC_SSID_DISCONNECT_STATUS = Device 'wlan1' successfully disconnected

#WIFI connection status log. wlan1 should be replaced by your wifi interface name
WLAN_6GHZ_PUBLIC_SSID_CONNECT_STATUS = Device 'wlan1' successfully activated

#WIFI disconnection status log. wlan1 should be replaced by your wifi interface name
WLAN_6GHZ_PUBLIC_SSID_DISCONNECT_STATUS = Device 'wlan1' successfully disconnected

#Unique WIFI 2.4GHZ Public SSID Name
SSID_2GHZ_PUBLIC_NAME = xwifi-2.4

#Unique WIFI 5GHZ Public SSID Name
SSID_5GHZ_PUBLIC_NAME = xwifi-5

#Unique WIFI 6GHZ Public SSID Name
SSID_6GHZ_PUBLIC_NAME = xwifi-6

#Set Device.X_COMCAST-COM_GRE.Tunnel.1.DSCPMarkPolicy
DSCPMARKPOLICY = 44

#Set Device.X_COMCAST-COM_GRE.Tunnel.1.PrimaryRemoteEndpoint
PRIMARY_REMOTE_END_POINT = 68.86.15.199

#Set Device.X_COMCAST-COM_GRE.Tunnel.1.SecondaryRemoteEndpoint
SECONDARY_REMOTE_END_POINT = 68.86.15.171

#WEBPA WIFI 2.4GHZ Public SSID index. Index will be 5 for TDK and 10003 for WEBPA
WEBPA_SSID_2GHZ_PUBLIC_INDEX = 10003

#TDK WIFI 2.4GHZ public SSID index. Index will be 5 for TDK and 10003 for WEBPA
TDK_SSID_2GHZ_PUBLIC_INDEX = 5

#WEBPA WIFI 5GHZ SSID index. Index will be 6 for TDK and 10103 for WEBPA
WEBPA_SSID_5GHZ_PUBLIC_INDEX = 10103

#TDK WIFI 5GHZ SSID index. Index will be 6 for TDK and 10103 for WEBPA
TDK_SSID_5GHZ_PUBLIC_INDEX = 6

#WEBPA WIFI 6GHZ SSID index. Index will be 19 for TDK and 10203 for WEBPA
WEBPA_SSID_6GHZ_PUBLIC_INDEX = 10203

#TDK WIFI 6GHZ SSID index. Index will be 19 for TDK and 10203 for WEBPA
TDK_SSID_6GHZ_PUBLIC_INDEX = 19

############################### Invalid test SSID ##########################################

SSID_INVALID_NAME = TEST_SSID

SSID_INVALID_PWD = mywifipassword

################################# WLAN CLIENT DETAILS ######################################

#Specify the WIFI client machine OS. Currently only UBUNTU is supported
WLAN_OS_TYPE = UBUNTU

#Client IP
WLAN_IP = XX.XX.XX.XX

#Client username
WLAN_USERNAME = username

#Client password
WLAN_PASSWORD = password

#Client ftp username
WLAN_FTP_USERNAME = username

#Client ftp password
WLAN_FTP_PASSWORD = password

#WIFI interface name for 2.4GHZ incase any external wifi adapter is used. Configure interface name based on setup
WLAN_2GHZ_INTERFACE = wlan0

#WIFI interface name for PUBLICWiFi 2.4GHZ incase any external wifi adapter is used. Configure interface name based on setup
WLAN_2GHZ_PUBLIC_SSID_INTERFACE = wlan0

#WLAN client's WIFI interface name for 5GHZ incase any external wifi adapter is used. Configure interface name based on setup
WLAN_5GHZ_INTERFACE = wlan1

#WLAN client's WIFI interface name for PUBLICWiFi 5GHZ incase any external wifi adapter is used. Configure interface name based on setup
WLAN_5GHZ_PUBLIC_SSID_INTERFACE = wlan1

#WLAN client's WIFI interface name for 6GHZ incase any external wifi adapter is used. Configure interface name based on setup
WLAN_6GHZ_INTERFACE = wlan2

#WLAN client's WIFI interface name for PUBLICWiFi 6GHZ incase any external wifi adapter is used. Configure interface name based on setup
WLAN_6GHZ_PUBLIC_SSID_INTERFACE = wlan2

#Invalid interface name
WLAN_INVALID_INTERFACE = NoInt

#Keyword to fetch the WIFI Client's IPv4 address
WLAN_INET_ADDRESS = "inet addr"

#Keyword to fetch the WIFI Client's subnet mask address
WLAN_SUBNET_MASK = "Mask"

#Utility script to be placed in the WIFI Client machine. Configure the script location
WLAN_SCRIPT = /home/user/tdkbE2E_wlan.sh

#Node details for WEBUI scripts.
#The file in which node logs are updating if the node is wlan client
WEBUI_NODE_WLAN_LOGFILE =

#The path in node machine where selenium standalone is downloaded if the node is wlan client
WEBUI_NODE_WLAN_SELENIUM_PATH =

################################# LAN CLIENT DETAILS ######################################

#Specify the LAN client machine OS. Currently only UBUNTU is supported
LAN_OS_TYPE = UBUNTU

#Client IP
LAN_IP = XX.XX.XX.XX

#Client's public IP
LAN_PUBLIC_IP = XX.XX.XX.XX

#Client username
LAN_USERNAME = username

#Client password
LAN_PASSWORD = password

#Client ftp username
LAN_FTP_USERNAME = username

#Client ftp password
LAN_FTP_PASSWORD = password

#Client's ethernet interface name
LAN_INTERFACE = eth0

#Keyword to fetch the LAN Client's IPv4 address
LAN_INET_ADDRESS = "inet addr"

#Keyword to fetch the LAN Client's IPv6 address
LAN_INET6_ADDRESS = "inet6 addr"

#Keyword to fetch the LAN Client's subnet mask address
LAN_SUBNET_MASK = "Mask"

#Utility script to be placed in the LAN Client machine. Configure the script location
LAN_SCRIPT = /home/user/tdkbE2E_lan.sh

#location of the DHCP configuration file
LAN_DHCP_LOCATION = /var/run/

#Keyword to fetch the LAN Client's dhcp lease time
LAN_LEASE_TIME = "dhcp-lease-time"

#Keyword to fetch the LAN Client's DNS server
LAN_DNS_SERVER = "domain-name-servers"

#Keyword to fetch the LAN Client's domain name
LAN_DOMAIN_NAME = "domain-name"

#LAN client's throughput in Mbps while transferring data to WAN
LAN_THROUGHPUT_TO_WAN =

#LAN client's throughput in Mbps while transferring data to another LAN
LAN_THROUGHPUT_TO_WLAN =

#Temporary file in lan client, to write the its throughput data
LAN_THROUGHPUT_OUTFILE =

#Node details for WEBUI scripts.
#The file in which node logs are updating if the node is lan client
WEBUI_NODE_LAN_LOGFILE =

#The path in node machine where selenium standalone is downloaded if the node is lan client
WEBUI_NODE_LAN_SELENIUM_PATH =

################################# WAN CLIENT DETAILS ######################################

#Specify the WAN client machine OS. Currently only UBUNTU is supported
WAN_OS_TYPE = UBUNTU

#Client IP
WAN_IP = XX.XX.XX.XX
WAN_HTTP_IP = XX.XX.XX.XX
WAN_PING_IP = XX.XX.XX.XX
WAN_HTTPS_IP = XX.XX.XX.XX
WAN_FTP_IP = XX.XX.XX.XX

#Client username
WAN_USERNAME = username
WAN_FTP_USERNAME = username

#Client password
WAN_PASSWORD = password
WAN_FTP_PASSWORD = password

#Client's Ethernet interface name
WAN_INTERFACE = eth0

#Keyword to fetch the WAN IPv4 address
WAN_INET_ADDRESS = "inet addr"

#Utility script to be placed in the WIFI Client machine. Configure the script location
WAN_SCRIPT = /home/user/tdkbE2E_wan.sh

#Connection timeout
CONNECTION_TIMEOUT = 30

#Node details for WEBUI scripts.
#The file in which node logs are updating if the node is wan client
WEBUI_NODE_WAN_LOGFILE =

#The path in node machine where selenium standalone is downloaded if the node is wan client
WEBUI_NODE_WAN_SELENIUM_PATH =

#################################NETWORK DETAILS#########################################

#IP to check if internet is accessible or not.
NETWORK_IP = XX.XX.XX.XX

#Port for http service validation. Port to be configured based on your web server installed
HTTP_PORT = 80

#Port for http service validation on WAN client. Port to be configured based on your web server installed
WAN_HTTP_PORT = 80

#Port for http service validation on WLAN client. Port to be configured based on your web server installed
WLAN_HTTP_PORT = 80

#Port for https service validation. Port to be configured based on your web server installed
HTTPS_PORT = 443

#Port for https service validation on WAN client. Port to be configured based on your web server installed
WAN_HTTPS_PORT = 443

#Port for https service validation on WLAN client. Port to be configured based on your web server installed
WLAN_HTTPS_PORT = 443

#https port for remote management
REMOTE_ACCESS_HTTPS_PORT = 8181

#http port for remote management
REMOTE_ACCESS_HTTP_PORT = 8080

#Port for parental control http service validation on WLAN client.
PARENTALCTL_PORT = 80

#Domain name which should be resolved using nslookup
NSLOOKUP_DOMAIN_NAME = www.google.com

#Invalid domain name for nslookup
INVALID_DNS_SERVER = XX.XX.XX.XX

#The URL to test the parental control features
WEBSITE_URL = www.google.com

#This should be the keyword of WEBSITE_URL
WEBSITE_KEYWORD = google

#The URL which is not blocked thorugh parental control
ALLOWED_URL = www.wikipedia.org

#IPV6 address of any public url. eg: google.com
PUBLIC_IPV6_ADDRESS = 2001:4860:4860:0:0:0:0:8888

#IPV4 address of any public url. eg: google.com
PUBLIC_IPV4_ADDRESS = 8.8.8.8

#BridgeMode status of the device in ethwan mode.Values are Enabled/Disabled
BRIDGEMODE_STATUS =

#################################CABLE MODEM DETAILS#########################################

#CM Configuration variables are applicable only for Broaband box type and not for BPI/RPI/Emulator

#Cable Modem IP type - IPV4/IPV6
CM_IP_TYPE = IPV6

#Cable Modem IP Address - IPV4/IPV6 address
CM_IP = XX.XX.XX.XX

#WAN ip of the gateway device
GW_WAN_IP = XX.XX.XX.XX

####################################TEMPORARY FILE DETAILS################################
#Temporary file in lan client, to write the TCP output
TMP_FILE_LAN = /home/user/tmpLAN.txt

#Temporary file in wlan client, to write the UDP output
TMP_FILE_WLAN = /home/user/tmpWLAN.txt

#File to be transferred  during FTP
FTP_TEST_FILE = Transfer_Test.txt

################### XDNS ####################################
#default DNS server for XDNS testing
XDNS_DNS_SERVER = XX.XX.XX.XX

#Level1 DNS server for XDNS
XDNS_LEVEL1_DNS_SERVER = XX.XX.XX.XX

#Level3 DNS server for XDNS
XDNS_LEVEL2_DNS_SERVER = XX.XX.XX.XX

#Level3 DNS server for XDNS
XDNS_LEVEL3_DNS_SERVER = XX.XX.XX.XX

#default DNS server for XDNS testing
XDNS_IPV6_DNS_SERVER = XX.XX.XX.XX

#Level1 DNS server for XDNS
XDNS_LEVEL1_IPV6_DNS_SERVER = XX.XX.XX.XX

#Level3 DNS server for XDNS
XDNS_LEVEL2_IPV6_DNS_SERVER = XX.XX.XX.XX

#Level3 DNS server for XDNS
XDNS_LEVEL3_IPV6_DNS_SERVER = XX.XX.XX.XX

#Level1 DNS server for XDNS
XDNS_LEVEL1_SECONDARY_DNS_SERVER = XX.XX.XX.XX

#Level3 DNS server for XDNS
XDNS_LEVEL2_SECONDARY_DNS_SERVER = XX.XX.XX.XX

#Level3 DNS server for XDNS
XDNS_LEVEL3_SECONDARY_DNS_SERVER = XX.XX.XX.XX

#Level1 DNS server for XDNS
XDNS_LEVEL1_IPV6_SECONDARY_DNS_SERVER = XX.XX.XX.XX

#Level3 DNS server for XDNS
XDNS_LEVEL2_IPV6_SECONDARY_DNS_SERVER = XX.XX.XX.XX

#Level3 DNS server for XDNS
XDNS_LEVEL3_IPV6_SECONDARY_DNS_SERVER = XX.XX.XX.XX

#Level1 site uri
XDNS_LEVEL1_SITE = ""

#Level2 site uri
XDNS_LEVEL2_SITE = ""

#Level3 site uri
XDNS_LEVEL3_SITE = ""

############################WEBUI############################################################

#Path to tdkbE2E_startHUB.sh in machine where hub should start, eg: /home/TDKB/WEBUI/start_hub_script.sh
START_HUB_SCRIPT =

#True if the browser should open with proxy enabled, eg: True
PROXY_ENABLED =

#If proxy enabled, Fill the below proxy credential info
#Host name eg: "xx.xx.xx.xx"
PROXY_HOST =

#Port name eg: 8080
PROXY_PORT =

#Proxy credential username eg: ""
PROXY_USERNAME =

#Proxy credential password eg: ""
PROXY_PASSWORD =

#No proxy field, eg : "10.0.0.1,localhost,127.0.0.1"
NO_PROXY =

#Path to proxy.zip which includes background.js,geckodriver.log
PROXY_PATH =

#Url whcih should open in the browser
GRID_URL = http://10.0.0.1/index.php

#MSO Url whcih should open in the browser
MSO_GRID_URL =

#The file in which the logs should update in hub machine
WEBUI_LOGFILE =

#Path in hub machine where selenium-server-standalone-3.141.59.jar is downloaded
WEBUI_HUB_SELENIUM_PATH =

#IP of the hub machine
HUB_MACHINE_IP =

#username of getway UI page
UI_USERNAME =

#MSO Username of UI page
MSO_UI_USERNAME =

#Password of gateway UI page
UI_PASSWORD =

#MSO Password of gateway UI page
MSO_UI_PASSWORD =

#Incorrect Password of gateway UI page
INCORRECT_UI_PASSWORD =

#Default Password of gateway UI page
DEFAULT_UI_PASSWORD =

#Destination address to perform connectivity test
CONNECTIVITY_TEST_DESTINATION_ADDRESS = www.google.com

#Connected lan host name eg: ""
CONNECTED_LAN_HOSTNAME =

#Blocked site name eg: ""
BLOCKED_SITE =

#Set of invalid SSID names for the platform
INVALID_SSIDNAMES =

########################PERFORMANCE########################################################
#time duration in seconds, for performance test cases
PERF_TEST_DURATION =

#polling interval in seconds for performance test cases
PERF_TEST_POLL_INTERVAL =

#throughput offset in Mbits/sec for performance test cases
PERF_TEST_OFFSET =

#the path to rdk-test-tool/logs/logs/ in TDK test manager deployment
TM_LOGS_LOCATION =

########################################Port Triggering########################################

#File to redirect connectivity logs in server
PT_SERVER_LOGFILE =

#File to redirect connectivity logs in client
PT_CLIENT_LOGFILE =

#File under /tftpboot in server to be transferred via TFTP to client
PT_TFTPFILE =

##################################LAN client connected Port###############################

#User have to configure in which port LAN client is connected
LAN_PORT_Number =

#################################IPv6 Configurations######################################
#IPv6 host used for connectivity and DNS resolution checks.
IPV6_HOST_NAME = "www.google.com"

#Interface token used to identify IPv6 addresses on the WLAN client.
WLAN_INET6_ADDRESS = "inet6"

##################################################
#Wi-Fi 7 Section
##################################################

#MLO enable flag
MLO_ENABLE = True

#MLO SSID for connecting Wi-Fi clients
MLO_SSID = mlossid

#MLO Password for authenticating Wi-Fi clients
MLO_PASSWORD = rdk@1234

#MLO Invalid password
MLO_INVALID_PWD = mywifipassword

#Wireless interface name based on setup to be replaced in place of wlan0
WLAN_INTERFACE = wlan0

#WIFI connection status log. wlan0 should be replaced by your wifi interface name
WLAN_SSID_CONNECT_STATUS = Device 'wlan0' successfully activated

#WIFI disconnect status log. wlan0 should be replaced by your wifi interface name
WLAN_SSID_DISCONNECT_STATUS = Device 'wlan0' successfully disconnected

#Wireless client's throughput in Mbps while transferring data to WAN
WLAN_MLO_THROUGHPUT_TO_WAN =

#Wireless client's throughput in Mbps while transferring data to another LAN
WLAN_MLO_THROUGHPUT_TO_LAN =

#Temporary file in wlan client, to write the throughput data
WLAN_MLO_THROUGHPUT_OUTFILE =

</div>

</details>


---

## Note

- Ensure that the **auto-reconnect feature is disabled** on the WiFi client machine. If auto-reconnect is enabled, the client may unintentionally re-establish a connection to the gateway, causing certain tests to fail.

---

## 4. Prerequisites

The prerequisites should be satisfied before executing all test suites as mentioned under [Suite Catgories](#5-test-suite-categories) except for [Vendor Test Suite](#55-vendor-test-suite).

- DUT flashed with firmware under test
- TDK Standalone package installed in the DUT and TDK service status is active
- Test Manager establishes communication with the TDK agent in the DUT

---

## 5. Test Suite Categories

---

### 5.1 Platform Compliance Validation Suite

#### Overview

The Platform Compliance Validation Suite verifies that the DUT meets the core RDK-B platform requirements, including component initialization, process management and critical networking functionalities.

#### Objectives

- Verify mandatory platform processes are running and stable
- Validate system initialization, reboot, and factory reset behaviors
- Validate critical networking functionalities

#### Test Suite Configuration Requirements 

- No additional configuration requirements

---

### 5.2 Device Management Validation Suite

#### Overview

The Device Management Validation Suite validates the DUT's support for remote device management protocols, including TR-069 (CWMP), TR-369 (USP), WebPA (Websocket Protocol Agent), RFC (Remote Feature Control), WEBCONFIG. 

#### Objectives

- Verify Device Management server connectivity and session management
- Validate Device Management supported operations

#### Test Suite Configuration Requirements 

- [TR-069 ACS configuration](#tr69-configuration) [OPTIONAL]
- [TR-398 USP controller configuration](#tr398-configuration) [OPTIONAL]
- [WebPA configuration](#webpa-configuration) [OPTIONAL]
- [RFC configuration](#rfc-configuration) [OPTIONAL]
- [WEBCONFIG configuration](#webconfig-configuration) [OPTIONAL]

---

### 5.3 Data Model Validation Suite

#### Overview

The Data Model Validation Suite verifies that the DUT correctly implements the required TR-181 data model objects, parameters, and access controls as mandated by the RDK-B and Broadband Forum specification.

#### Objectives

- Validate presence and correct typing of mandatory TR-181 objects and parameters
- Verify read/write access levels match the specification
- Confirm parameter value ranges and enumeration compliance
- Validate table object creation/deletion
- Validate standalone and composite set operations 

#### Test Suite Configuration Requirements 

- [WebPA configuration](#webpa-configuration) [OPTIONAL]

---

### 5.4 Connectivity & Platform Services Validation Suite

#### Overview

The Connectivity & Platform Services Validation Suite validates end-to-end broadband connectivity, WAN/LAN functionality, and key platform services such as DHCP, DNS, firewall, Wi-Fi, and routing.

#### Objectives

- Validate primary and backup WAN 
- Verify LAN-side IPv4/IPv6 address assignment and routing
- Validate platform services: DHCP server, DNS, firewall, Advanced Features
- Confirm Wi-Fi functionality 

#### Test Suite Configuration Requirements 

- [Crash upload configuration](#crashupload-configuration) [OPTIONAL]
- [Downloadable App Containers configuration](#dac-configuration) [OPTIONAL]
- [Firmware upgrade configuration](#fwupgrade-configuration) 
- [RDK Remote Debugger configuartion](#rrd-configuration) 
- [Telco Voice Manager configuration](#telco-configuration) [OPTIONAL]
- [Telemetry configuration](#telemetry-configuration)
- [WEBUI configuration](#webui-configuration) [OPTIONAL]
- [OneWiFi configuration](#onewifi-configuration)
- [Cellular WAN configuration (secondary WAN)](#cellular-configuration) [OPTIONAL]
- [RNDIS WAN configuration (secondary WAN)](#rndis-configuration) [OPTIONAL]
- [IPv6 configuration](#ipv6-configuration) [OPTIONAL]

---

### 5.5 Vendor Test Suite

#### Overview

The Vendor Test Suite contains HAL test cases to validate specifications mandated by RDK-B HAL interface.

#### Objectives

- Validate vendor-specific implementation for RDK-B HAL interface

#### Pre-requisites 

- DUT flashed with firmware under test
- VTS test binary should be installed in the DUT

#### Test Suite Configuration Requirements 

- [Platform HAL](https://github.com/rdkcentral/rdkb-halif-test-platform)
- [DHCP HAL](https://github.com/rdkcentral/rdkb-halif-test-dhcp)
- [Firmwre Upgrade HAL](https://github.com/rdkcentral/rdkb-halif-test-fwupgrade)
- [Ethsw HAL](https://github.com/rdkcentral/rdkb-halif-test-ethsw)

---

### 5.6 Performance and Stability Validation Suite

#### Overview

The Performance and Stability Validation Suite validates that the DUT meets the minimum throughput and long-term stability requirements under realistic and stress conditions, ensuring a quality broadband experience over sustained operation.

#### Objectives

- Measure WAN-to-LAN and LAN-to-WAN throughput under load
- Verify system stability over extended stress periods
- Validate memory and CPU utilization within defined thresholds

#### Test Suite Configuration Requirements

- [WebPA configuration](#webpa-configuration)

---

## 6. Execution Rules

- Each suite must meet its **Pre-requisites** before execution begins.
- Test suite configuration must be completed before test suite is triggered

---

## 7. Pass/Fail Criteria

### 7.1 Test Case Level

| Result | Definition |
|--------|-----------|
| **SUCCESS** | All steps executed successfully; actual result matches expected result |
| **FAILURE** | Any step produces a result deviating from the expected result |

### 7.2 Suite Level

A test suite is considered **SUCCESS** when:
- All test cases have a result of SUCCESS

---

## 8. Glossary

| Term | Definition |
|------|-----------|
| ACS | Auto-Configuration Server (TR-069) |
| CPE | Customer Premises Equipment |
| CWMP | CPE WAN Management Protocol (TR-069) |
| DUT | Device Under Test |
| HAL | Hardware Abstraction Layer |
| RDK-B | Reference Design Kit for Broadband |
| TR-069 | Broadband Forum technical report for CPE remote management |
| TR-181 | Broadband Forum Device:2 data model |
| TR-369 | Broadband Forum User Services Platform (USP) |
| USP | User Services Platform |
| WAN | Wide Area Network |

---

## 9. Appendix for test configurations

<details id="tr69-configuration">
<summary><strong>TR-069 ACS configuration</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

TR-069 ACS bring-up - [TR-069 Test Setup Configuration](TestSetupConfiguration/TR-069-Test-Setup-Configuration.md) 

### Pre-requisites for executing TR-069 Scripts
Populate the values for the following variables in tr69Config.py under fileStore 

    #Location/path of the TR-069 (CWMP) client certificate on the DUT
    TR069_CERTIFICATE_LOCATION=""

    #URI of ACS server to be used for accessing API Interface
    ACS_NBI_URL=""

</div>

</details>

---

<details id="tr398-configuration">
<summary><strong>TR-398 USP Controller Configuration</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

Oktopus Controller bring-up - [TR-398 USPPA Test Setup Configuration](TestSetupConfiguration/USPPA-Test-Setup-Configuration.md) 

#### Pre-requisites for executing USPPA Scripts
USPPA process should be enabled in the EUT. 
USP Controller should be up and running 
EUT should be configured such that Controller and Agent should be able to communicate with each other. Under Devices in Controller UI , the specific EUT should listed as online.

Install PyJWT if not already available in Test Manager - 

    pip3 install PyJWT   

Populate the values for the following variables in usppaVariables.py under fileStore 

    #Expects the name of file holding JWT token. Token file will be in a location in the VM hosting the controller. 
    TOKEN_FILE = ""  

    #Give the USP Controller uri eg: http://<Controller-IP>:8000 
    CONTROLLER_URI = "" 

    #Give the Controller login username and password of Admin or a User . Username is usually a email address 
    USERNAME = "" 
    PASSWORD = "" 

</div>

</details>

---

<details id="webpa-configuration">
<summary><strong>WebPA Configuration</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

Before executing WebPA tests, verify that webpa server is operational and running.

Populate the values for the following variables in webpaVariables.py under fileStore 

    #give SAT_REQUIRED = 'true' if SAT token is required otherwise 'false'
    SAT_REQUIRED= ""

    #expects the name of file holding SAT token, including its path
    SAT_TOKEN_FILE = ""

    #WEBPA server uri
    SERVER_URI = ""

    #Give the authentication type, eg: AUTHTYPE="Basic d2VicGFAMTIzNDU2Nzg5MA==" for community webpa server
    AUTHTYPE = ""

</div>

</details>

---

<details id="rfc-configuration">
<summary><strong>RFC Configuration</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

Before executing RFC tests, verify that the XConf Server https://xconf.rdkcentral.com/ is operational and running.

The user is required to configure the XCONF API key in RFCVariables.py under Filestore

    #The user is required to configure the XCONF API key here
    XCONF_API_KEY=""

</div>

</details>

---

<details id="webconfig-configuration">
<summary><strong>WEBCONFIG Configuration</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

For WEBCONFIG based tests, verify that the WebConfig server https://webconfig.rdkcentral.com/app1/ is operational and running.

</div>

</details>

---

<details id="crashupload-configuration">
<summary><strong>Crash Upload Configuration</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

#### Pre-requisites for executing Crash Upload Scripts
A Python file transfer server must be running on a Local host machine (for local upload scenarios) and listening on a unique port.

Before running Local upload scenario Tests ensure that to populate the CrashUploadVariables.py under Filestore with correct upload server port and IP.

    LOCAL_SERVER_PORT = ""
    LOCAL_SERVER_IP = ""

</div>

</details>

---

<details id="dac-configuration">
<summary><strong>Downloadable App Containers Configuration</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

#### Pre-requisites for DAC scripts test execution
A local HTTP file server must be running and accessible from the DUT, hosting the required OCI bundles.

Before executing the DAC scripts, ensure that the file DACVariables.py under Filestore is updated with the correct IP address and port of the HTTP file server. An IPERF server to be started (iperf -s) in a new terminal in the same device HTTP file server is hosted.

    BUNDLE_DOWNLOAD_URL = f"http://{LOCAL_FILE_SERVER_IP}:{LOCAL_FILE_SERVER_PORT}/{OCI_BUNDLE_NAME}"
    BUNDLE_DOWNLOAD_URL_2 = f"http://{LOCAL_FILE_SERVER_IP}:{LOCAL_FILE_SERVER_PORT}/{OCI_BUNDLE_NAME_2}"
    IPERF3_SERVER_IP = ""  # IP of the iperf3 server to be set in bundle config.json


The user must generate the OCI bundles and place them in the HTTP file server directory. Steps to build the OCI image and create the bundle:
Building an OCI image (example: iperf3): https://github.com/rdkcentral/meta-dac-sdk-broadband/blob/main/README.md

Set up the BundleGen tool on a local Linux PC by following the instructions on the RDK wiki: https://wiki.rdkcentral.com/pages/viewpage.action?pageId=306425968

Create a file named "platform"_reference.json by using rpi4_reference_dunfell.json as a reference, and place it in the BundleGen/templates/generic/ directory.

Copy the generated "platform"_reference_libs.json (obtained from the platform build) to the BundleGen/templates/generic/ directory.

Generate the bundle for the iperf3 OCI image by executing the following command inside the BundleGen folder:
Bash
 
    ~/BundleGen$ bundlegen generate --platform bpir4_reference oci:dac-image-iperf3-raspberrypi4-64-20241004063830.rootfs-oci /home/heam/dac/Heam_bpir4_iperf
 
Note: The primary OCI bundle must be named iperf3filogic.tar.gz. An additional copy of the exact same bundle must also be placed in the HTTP file server directory and named iperf3bundlecopy.tar.gz.

</div>

</details>

---

<details id="fwupgrade-configuration">
<summary><strong>Firmware Upgrade Configuration</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

#### Pre-requisites for executing Firmware Upgrade Scripts using XCONF AdminService REST APIs.
The XConf Server https://xconf.rdkcentral.com/ should be operational and running.
A Python HTTP server is running in a WAN machine accessible from the DUT, hosting target firmware images for upgrade. The server details should be configured in firmwareUpgradeVariables.py file.
The firmware hosting server should listed to the the default HTTP port 80 for the firmware upgrade to occur.

Populate the following variables in the firmwareUpgradeVariables.py

    FIRMWARE_UPGRADE_BPI - Target Firmware Name
    FIRMWARE_LOCATION - Server IP hosting target images
    XCONF_API_KEY - User API key for accessing XCONF Server

The target firmware should not be present in any active/passive banks of the DUT

#### Pre-requisites for executing Firmware Upgrade Scripts using TR-181 Firmware Upgrade Commands.
A Python HTTP server is running in a WAN machine accessible from the DUT, hosting target firmware images for upgrade. The server details should be configured in firmwareUpgradeVariables.py file.
The firmware hosting server should listed to the the default HTTP port for the firmware upgrade to occur.

Populate the following variables in the firmwareUpgradeVariables.py

    FIRMWARE_UPGRADE_BPI - Target Firmware Name
    FIRMWARE_LOCATION - Server IP hosting target images

</div>

</details>

---

<details id="rrd-configuration">
<summary><strong>RDK Remote Debugger Configuartion</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

#### Pre-Requisites for executing RDK Remote Debugger Test Cases 
In case of static profile & dynamic profile, set up the upload server(Ex:Apache server) on the local Machine for BPIR4 to upload the debug reports

Instructions of upload server - 

    sudo apt install apache2 
    sudo a2enmod dav dav_fs
    sudo a2ensite upload.conf
    sudo mkdir /srv/upload && sudo chown www-data:www-data /srv/upload

Have the below content in /etc/apache2/sites-available/upload.conf - 
    <VirtualHost *:8080>
        ServerAdmin admin@example.com
        DocumentRoot /srv/upload

        <Directory /srv/upload>
            Options Indexes FollowSymLinks
            AllowOverride None
            Require all granted
            DAV On
        </Directory>

    </VirtualHost>


Add the ports to listen  in /etc/apache2/ports.conf - 

    Listen 0.0.0.0:80
    Listen 0.0.0.0:8080
    <IfModule ssl_module>
        Listen 443
    </IfModule>
    <IfModule mod_gnutls.c>
        Listen 443
    </IfModule>

Start Apache2 server 

    sudo systemctl enable apache2 
    sudo systemctl start apache2
    
    sudo netstat -lputnu |     grep apa
    tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      1038/apache2        
    tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN              1038/apache2 

In case of dynamic profile, install the Download Server ( Ex: Apache) and host the Dynamic profile in Download server path(in the below format) in addition to upload server.

    $cd /var/www/html
    $:/var/www/html$ sudo tar -tf RDK-RRD-Device_1.0-signed.tar RDK-RRD-Device.tar
    $:/var/www/html$ sudo tar -tf RDK-RRD-Device.tar etc/ etc/rrd/ etc/rrd/remote_debugger.json
    $:/var/www/html$ cat etc/rrd/remote_debugger.json { "Device" : { "wifi" : { "Commands": "iw dev;uname -r", "Timeout" : 10 } } }

Note that Download and Upload server can also be hosted in the same sytstem with 8080 port specified for upload server and another port for download server

Populate the following fields in tdkbRRDVariables.py

    #Upload Server URL
    #Format - http://<server_ip>:<port>
    upload_server_url = ""

    #Download Server URL - No need to specify port
    #Format - http://<server_ip>
    download_server_url = ""

</div>

</details>

---

<details id="telco-configuration">
<summary><strong>Telco Voice Manager Configuration</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

#### Pre-requisites required for executing Telco Voice Manager scripts are as follows
Two Inbound SIP clients run on Ubuntu machines in the same WAN network as the DUT (Asterisk server).
Outbound SIP endpoint is created via Linphone.
All credentials must match the configurations defined in the DUT hosting asterisk server - /etc/asterisk/pjsip.conf.

### Inbound Client Setup using Baresip SIP tool
Installation of Baresip tool - 
    sudo apt install baresip

Client Configuration - 

    mkdir -p ~/.baresip
    nano ~/.baresip/accounts


Add the following line in ~/.baresip/accounts

    <sip:USERNAME@ASTERISK_IP>;auth_user=USERNAME;auth_pass=USERNAME;regint=60;answermode=auto

Please Note :
ASTERISK_IP is the IP Address of the DUT.
The USERNAME and PASSWORD is configured as per the DUT configuration /etc/asterisk/pjsip.conf .
The default (username,password) configurations are  (601,601) and (602,602) 
          
Start Client using the following command - 
    baresip -vvv

#### Outbound Client Setup - 
Create account at:
https://subscribe.linphone.org/login

Signup username/password = outbound SIP credentials

Configure these credentials in tdkbTelcoVoiceManagerVariables.py [outbound_client_username , outbound_client_password ] for outbound configuration.

</div>

</details>

---

<details id="telemetry-configuration">
<summary><strong>Telemetry configuration</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

#### Pre-requisite for telemetry2_0 script executions are 
A python library msg pack should be installed in the Test Manager VM instance if not already available.

    pip3 install msgpack

Configure the tdkbTelemetry2.0_Variables.py as per user requirement.

Telemetry Upload Server configured should be up and running.

</div>

</details>

---

<details id="webui-configuration">
<summary><strong>WEBUI Configuration</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

WEBUI Docker setup bring-up : [WebUI Test Setup](TestSetupConfiguration/TDKB_WebUI_Test_Framework.md)

> Note: For WEBUI executions it is recommended to use Laptop as WLAN/WAN/LAN clients. If RPI is used, ensure that the firefox driver version is compatible. 

</div>

</details>

---

<details id="onewifi-configuration">
<summary><strong>OneWiFi Configuration</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

Ensure that for the following test scripts in the suite, a wireless LAN
client connection is manually established - 

TS_ONEWIFI_CheckHostActiveStatus_WithConnectedClient
TS_ONEWIFI_CheckTelemetryMarker_BytesSentAndReceived
TS_ONEWIFI_CheckTelemetryMarker_ConnectedClientMacaddress
TS_ONEWIFI_CheckTelemetryMarker_ErrorSent
TS_ONEWIFI_CheckTelemetryMarker_FailedAndReTransCount
TS_ONEWIFI_CheckTelemetryMarker_PacketsSent_PacketsReceived
TS_ONEWIFI_CheckTelemetryMarker_RETRANSCOUNT_FAILEDRETRANSCOUNT
TS_ONEWIFI_CheckTelemetryMarker_RetryAndMultipleRetryCount
TS_ONEWIFI_CheckTelemetryMarker_WIFI_ACS
TS_ONEWIFI_CheckTelemetryMarker_WIFI_MAC
TS_ONEWIFI_CheckTelemetryMarker_WiFiClientRxTxValue

</div>

</details>

---

<details id="cellular-configuration">
<summary><strong>Cellular LTE WAN configuration (secondary WAN)</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

## Prerequisites for Cellular LTE Testing
Before testing the module, insert a SIM to the device and do the necessary configurations to bring the device up in cellular mode.

Connect ethwan cable - erouter0 is coming up with v4/v6
Remove ethwan and connect LTE
Set Selection interface - psmcli set dmsb.wanmanager.if.2.Selection.Enable TRUE
Reboot device to start dhcp on new selected interface
LTE interface is up, DNS is updated

### Test Manager Configuration for Script Executions:
Connect the Test Manager (TM) as a LAN client to the DUT.
Configure the DUT IP address to 10.0.0.1 for script execution.

</div>

</details>

---

<details id="rndis-configuration">
<summary><strong>Cellular RNDIS configuration (secondary WAN)</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

## Prerequisites for Cellular RNDIS Testing
RNDIS-Enabled Build Required: An RNDIS-enabled build is required for testing. Build instructions are provided in the reference wiki page.

### Setup:
### Android USB
Disconnect the Ethernet WAN cable from the DUT.
Connect an Android phone to the USB port of the DUT using a USB-C cable.
Enable USB Tethering on the Android phone.
### iPhone USB
Disconnect the Ethernet WAN cable from the DUT.
Connect an iPhone to the USB port of the DUT using a USB-C cable.
Enable the Personal Hotspot and Accept the Trust Certificate on the iPhone. Toggle the “Allow other users to join” button (switch off and switch it on after 6-7 seconds). After these steps iPhone offers the IP.

### Test Manager Configuration for Script Executions:
Connect the Test Manager (TM) as a LAN client to the DUT.
Configure the DUT IP address to 10.0.0.1 for script execution.
Note: USB Tethering must be re-enabled on the Android /iPhone after each DUT reboot.

### For the below scripts ensure that a WiFi client is connected before running the test
TS_RNDIS_VerifyHostTableUpdateWithWiFiClient_AndroidUSB
TS_RNDIS_VerifyHostTableUpdateWithWiFiClient_iPhoneUSB

</div>

</details>

---

<details id="ipv6-configuration">
<summary><strong>IPv6 Configuration</strong></summary>

<br>

<div style="background-color:#1e1e1e; border:1px solid #f0f0f0; border-radius:6px; padding:20px 24px; font-family:monospace; font-size:0.88em; line-height:1.6; white-space:pre-wrap;">

For networks that do not natively support IPv6, the setup bring-up is detailed in : [IPv6 Simulator Setup](TestSetupConfiguration/TDKB_IPv6_Simulator_Setup.md)

### The following scripts need to be executed with a connected Wi-Fi client
TS_IPV6_Check_ActiveWLANClient_IPv6Address
TS_IPV6_Check_Brlan0LinkLocalNeighborConnectivity_WLANInterface
TS_IPV6_Check_PingToWLANClientGlobalIPv6

</div>

</details>

---

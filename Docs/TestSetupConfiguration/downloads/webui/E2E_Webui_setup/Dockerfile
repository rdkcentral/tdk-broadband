##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2026 RDK Management
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

# Use Ubuntu as base image
FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages, including ftp, telnet, xinetd, and other network utilities
RUN apt-get update && apt-get install -y \
    openssh-server \
    curl \
    vim \
    apache2 \
    vsftpd \
    ssl-cert \
    iperf \
    netcat \
    inetutils-ftp \
    inetutils-telnet \
    wget \
    xinetd \
    sshpass \
    tftpd \
    tftp \
    net-tools \
    iputils-ping \
    sudo \
    openssl \
    iproute2 \
    network-manager \
    netcat \
    nano \
    inetutils-telnetd \
    dnsutils \
    wireless-tools \
    python3 \
    python3-pip \
    openjdk-8-jdk \
    firefox \
    xvfb \
    dbus-x11 \
    bzip2 \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libx11-xcb1 \
    libxt6 \
    libpulse0 \
    libasound2 \
    libgl1-mesa-glx \
    libpci3 \
    libegl1 \
    libgl1-mesa-dri \
    libx11-xcb1 \
    && rm -rf /var/lib/apt/lists/*

# Copy the local Firefox tarball into the container
COPY firefox-133.0.tar.bz2 /tmp/

# Extract and install Firefox
RUN tar -xjf /tmp/firefox-133.0.tar.bz2 -C /opt \
    && ln -sf /opt/firefox/firefox /usr/bin/firefox \
    && rm /tmp/firefox-133.0.tar.bz2
# Create the secure chroot directory and set permissions for vsftpd
RUN mkdir -p /var/run/vsftpd/empty && \
    chmod 755 /var/run/vsftpd/empty

# Configure SSH
RUN mkdir -p /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config

# Configure Apache
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Configure Apache SSL
RUN a2enmod ssl
RUN a2ensite default-ssl
RUN mkdir -p /etc/apache2/ssl
RUN openssl genrsa -out /etc/apache2/ssl/ca.key 2048
RUN openssl req -nodes -new -key /etc/apache2/ssl/ca.key -out /etc/apache2/ssl/ca.csr -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"
RUN openssl x509 -req -days 365 -in /etc/apache2/ssl/ca.csr -signkey /etc/apache2/ssl/ca.key -out /etc/apache2/ssl/ca.crt

RUN sed -i 's|SSLCertificateFile.*|SSLCertificateFile /etc/apache2/ssl/ca.crt|g' /etc/apache2/sites-available/default-ssl.conf
RUN sed -i 's|SSLCertificateKeyFile.*|SSLCertificateKeyFile /etc/apache2/ssl/ca.key|g' /etc/apache2/sites-available/default-ssl.conf

# Configure VSFTPD with minimal config
RUN echo "listen=YES" > /etc/vsftpd.conf
RUN echo "listen_ipv6=NO" >> /etc/vsftpd.conf
RUN echo "anonymous_enable=NO" >> /etc/vsftpd.conf
RUN echo "local_enable=YES" >> /etc/vsftpd.conf
RUN echo "write_enable=YES" >> /etc/vsftpd.conf
RUN echo "local_umask=022" >> /etc/vsftpd.conf
RUN echo "dirmessage_enable=YES" >> /etc/vsftpd.conf
RUN echo "use_localtime=YES" >> /etc/vsftpd.conf
RUN echo "xferlog_enable=YES" >> /etc/vsftpd.conf
RUN echo "connect_from_port_20=YES" >> /etc/vsftpd.conf
RUN echo "seccomp_sandbox=NO" >> /etc/vsftpd.conf
RUN echo "pasv_enable=YES" >> /etc/vsftpd.conf
RUN echo "pasv_min_port=40000" >> /etc/vsftpd.conf
RUN echo "pasv_max_port=40100" >> /etc/vsftpd.conf

# Configure Telnet
RUN mkdir -p /etc/xinetd.d
COPY telnet /etc/xinetd.d/telnet
RUN chmod 644 /etc/xinetd.d/telnet

# Configure TFTP
RUN mkdir -p /tftpboot
RUN chmod -R 777 /tftpboot
RUN chown -R nobody:nogroup /tftpboot
COPY tftp /etc/xinetd.d/tftp
RUN chmod 644 /etc/xinetd.d/tftp

# Copy custom xinetd configuration file to container
COPY xinetd.conf /etc/xinetd.conf

# Create required directories for Apache, VSFTPD, and SSH
RUN mkdir -p /var/run/apache2 \
    && mkdir -p /var/run/vsftpd/empty \
    && mkdir -p /var/log/apache2 \
    && mkdir -p /var/lock/apache2 \
    && mkdir -p /run/sshd \
    && chown -R www-data:www-data /var/run/apache2 \
    && chown -R www-data:www-data /var/log/apache2 \
    && chown -R www-data:www-data /var/lock/apache2

# Copy startup script
COPY start-services.sh /start-services.sh
RUN chmod +x /start-services.sh

# Copy client scripts
COPY tdkbE2EClientScripts /tdkbE2EClientScripts/

# Copy the webui folder to the container
COPY webui /webui

# Change permissions for the webui folder and its contents
RUN chmod -R 777 /webui

# Install Selenium and WebDriver Manager
RUN pip3 install \
    selenium==4.18.1 \
    webdriver-manager \
    pyvirtualdisplay

# Add geckodriver executable to /usr/local/bin (geckodriver file will be copied later)
COPY geckodriver /usr/local/bin/geckodriver
RUN chmod +x /usr/local/bin/geckodriver

# Start services
CMD ["/start-services.sh"]


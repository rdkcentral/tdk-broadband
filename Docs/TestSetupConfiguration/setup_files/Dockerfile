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
    iperf3 \
    netcat \
    inetutils-ftp \wikidocs/tdk-broadband/Docs/TestSetupConfiguration/setup_files
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
&& rm -rf /var/lib/apt/lists/*
 
# Copy the vsftpd configuration file from the host to the container
#COPY vsftpd.conf /etc/vsftpd.conf
 
# Create the secure chroot directory and set permissions for vsftpd
RUN mkdir -p /var/run/vsftpd/empty && \
    chmod 755 /var/run/vsftpd/empty
 
# Configure SSH
RUN mkdir -p /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
 
# Configure Apache
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
#RUN sed -i 's/Listen 80/Listen 8080/' /etc/apache2/ports.conf
#RUN sed -i 's/Listen 443/Listen 8443/' /etc/apache2/ports.conf
 
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
 
# Start services
CMD ["/start-services.sh"]
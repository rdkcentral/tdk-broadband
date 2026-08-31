#!/bin/bash

echo "Initial service start..."

# Start services
service ssh start
service apache2 start
service vsftpd start
service xinetd start

apache2ctl -D FOREGROUND
echo "Start User creation..."

# Set username and password
USERNAME="client_tdkb"
PASSWORD="asdfqwer"

# User creation
useradd -m -s /bin/bash $USERNAME

# Set password for the user
echo "$USERNAME:$PASSWORD" | chpasswd

usermod -aG sudo $USERNAME
chmod 440 /etc/sudoers
cp /etc/sudoers /etc/sudoers.bak

# Add the user to the sudoers file
echo "$USERNAME   ALL=NOPASSWD: ALL" >> /etc/sudoers

echo "User $USERNAME created and added to the sudoers file successfully."

tail -f /dev/null



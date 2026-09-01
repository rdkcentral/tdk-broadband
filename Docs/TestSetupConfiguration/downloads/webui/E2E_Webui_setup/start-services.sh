#!/bin/bash

echo 'export PATH=$PATH:/usr/local/bin' >> /root/.bashrc
echo 'export PATH=$PATH:/usr/local/bin' >> /home/<username>/.bashrc

echo "Initial service start..."

# Start services
service ssh start

echo "Start User creation..."
# Set username and password
USERNAME=""
PASSWORD=""

# Create the user with the specified username
useradd -m -s /bin/bash $USERNAME

# Set the password for the user
echo "$USERNAME:$PASSWORD" | chpasswd

# Add the user to the sudo group
usermod -aG sudo $USERNAME

# Ensure proper permissions are set for sudoers file
chmod 440 /etc/sudoers

# Backup the original sudoers file (just in case)
cp /etc/sudoers /etc/sudoers.bak

# Add the user to the sudoers file with the desired permissions
echo "$USERNAME  ALL=NOPASSWD: ALL" >> /etc/sudoers

# Print success message
echo "User $USERNAME created and added to the sudoers file successfully."

# Set up Xvfb for headless browser testing
Xvfb :99 -ac &
export DISPLAY=:99


# Keep the container running
tail -f /dev/null

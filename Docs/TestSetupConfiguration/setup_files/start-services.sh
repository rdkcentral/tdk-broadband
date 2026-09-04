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
USERNAME="client_name"
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



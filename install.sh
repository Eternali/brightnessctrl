#!/bin/bash

echo "sudo `pwd`/brightness.py -i 15 -" > /usr/bin/brightness-
echo "sudo `pwd`/brightness.py -i 15 +" > /usr/bin/brightness+
sudo chmod +x /usr/bin/brightness-
sudo chmod +x /usr/bin/brightness+

if [ "$1" == "-s" ]; then
    sudo echo "`who am i | awk '{print $1}'` ALL=(ALL) NOPASSWD: `pwd`/brightness.py" >> /etc/sudoers
fi

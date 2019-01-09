#!/bin/bash

echo "sudo `pwd`/brightness.py -i 15 -" > /usr/bin/brightness-
echo "sudo `pwd`/brightness.py -i 15 +" > /usr/bin/brightness+
sudo chown $USER:$USER /usr/bin/brightness- /usr/bin/brightness+
sudo chmod +x /usr/bin/brightness-
sudo chmod +x /usr/bin/brightness+

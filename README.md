# brightnessctrl
Control brightness on linux

To install simply run the install script as sudo.

    $ sudo ./install.sh

Then use `brightness+` and `brightness-` to increase and decrease the brightness of the screen

Configuration:

Depending on the model display driver, you may have to change some configuration.
To do this, simply edit the install script according to your needs.

You can specify the brightness file with the "-f" flag in the invocation of the brightness script:
    
    > echo "sudo `pwd`/brightness.py -f /path/to/brightness/file -i 15 -" > /usr/bin/brightness-

This is usually something along the lines of `/sys/class/backlight/intel/brightness`.

You can also specify the interval that the brightness changes with the "-i" flag:

    > echo "sudo `pwd`/brightness.py -i 30 -" > /usr/bin/brightness-

You can also get the current brightness with:

    > sudo ./brightness.py get

If you want to be able to run this without requiring a password you can run `install.sh` with the "-s" flag or add the following line to your `/etc/sudoers` file (filling in the user specific fields).

    USERNAME ALL=(ALL) NOPASSWD: /full/install/path/brightnessctrl/brightness.py

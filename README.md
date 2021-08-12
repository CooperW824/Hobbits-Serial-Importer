# Hobbits-Serial-Importer

A tool to import binary data coming off of Serial ports (not including usb ports) into the hobbits tool.

## Importing the Plugin into Hobbits

This plugin is designed to work with [Hobbits](https://github.com/Mahlet-Inc/hobbits) a bitwise analyzation and manipulation tool.

In order for the plugin to work you must have Python 3.9+ with the PySerial package intalled and a hobbits v0.5.0+ binary. 

PySerial can be installed via

    pip install pyserial

To install, either download the source files or clone the Hobbits-Serial-Importer repository, go to your hobbits binary and enter the plugins folder, then create a new "python_importers" folder, **it must** be named "python_importers".  Copy the "SerialRead" folder into the new python_importers folder. Then copy the ```serialLib.py``` file (just the file) into hobbits/hobbits-cpython/lib/python3.9.

You have now installed the serial reader plugin and it can be used.

## Using the plugin

Now that the plugin is installed you are ready to use it the steps for use are below:

1. Enter your Baudrate, or rate of transimission of the device, this differs device to device, look in the owner's manual/online for this info.
2. Determine if you would like to include the Newline and Carriage Return symbols in your BitContainer, some devices (like arduinos) do this on each transfer. 
3. Enter the port of your device, a list of active ports can be found by entering this command into a terminal/command prompt: ```python3 -m serial.tools.list_ports```
4. Enter the timeout duration, how long to read for before stopping and entering the data into the BitContainer. 

## Contributing 

Contributions are always welcome, bug reports, feature requests, and commits, if you are trying to pull your code into the main branch please link an issue with your pull request, if there is no issue then please create one.

Docs for hobbits python plugin development is linked [here:](https://mahlet-inc.github.io/)
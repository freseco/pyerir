# pyerir
## About
Simple fullscreen player for m3u files. It works in Raspberry pi 4 with Python3.9. It can get the IR code from IR remote control.

This project is a small example of wxpython for the GUI, threading for getting the IR codes, using wraper vlc library, gpio pins and the m3u_parser library for parsing the m3u files.

It has two types of notifications: wx.adv and popup windows(not work yet)

*Not testing with other python versions.

## First step: Installation of dependencies
    $ pip install requirements.txt 

## Setting IR received in Raspberry pi.

![The IR receiver](https://github.com/freseco/pyerir/blob/main/pics/IRreceiver_remoteControl.jpg)

## Using
    $ pip pyerir [-v | --version]  [<m3u_file_name>] 
*by default, it will try to open tdt.m3u

## VLC in python
[VLC module in Python](https://www.geeksforgeeks.org/vlc-module-in-python-an-introduction/)

## m3u parser
[m3u_parser](https://pypi.org/project/m3u-parser/)

## TODO:
- Fill readme file.
- Help to install code.
- Help to install IR remote code: shema picture.
- Help to run the code.
- Help to modifie.
- Improve description.
- Get m3u form url. Right now it gets a file in local system file.
- Memorize favorite channels.
- Testing in other platforms.
- Read configuration file.

## Error list:
- Not show the windows for channel name and volumen value.

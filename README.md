# PYERIR
## About
Simple fullscreen player for m3u files. It works in Raspberry pi 4 with Python3.9. It can get the IR code from IR remote control.

This project is a small example of wxpython for the GUI, threading for getting the IR codes, using wraper vlc library, gpio pins and the m3u_parser library for parsing the m3u files.

It has two types of notifications: wx.adv(OS notification) and popup windows.

*Not testing with other python versions.

## First step: Installation of dependencies
    $ pip install requirements.txt 

## Setting IR received(HX1838) in Raspberry pi.

![The IR receiver](https://github.com/freseco/pyerir/blob/main/pics/IRreceiver_remoteControl.jpg)

## Start the pigpio daemon
$ sudo pigpiod

[pigpiod libraries](https://abyz.me.uk/rpi/pigpio/download.html)


## Using
    $ python[3.9] pyerir.py [-v | --version]  [<m3u_file_name>] [--debug]

Parameters:
- [-v | --version] shows script version.
- [m3u_file_name] file to get the channels.
- [--debug] shows debug information in console.

*by default, it will try to open tdt.m3u

## VLC in python
[VLC module in Python](https://www.geeksforgeeks.org/vlc-module-in-python-an-introduction/)

## m3u_parser library.
[m3u_parser](https://pypi.org/project/m3u-parser/)

## TODO:
- Menu/windows to show and scrolling all channels.
- Memorize favorite channels.
- Testing in other platforms.
- Read configuration file: json format, favorite channels, url or path of m3u file.
- Get channels information from Xtream-Codes IPTV servers.

## Error list:
- No exit well when push #
- key only when windows channel o volumen are shown.

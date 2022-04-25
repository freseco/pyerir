# PYERIR
## About
Simple fullscreen player for m3u files(IPTV). It works in Raspberry pi 4 with Python3.9. It can get the IR code from (any?) IR remote control.


This project is a small example of wxpython for the GUI, threading for getting the IR codes, using wraper vlc library, gpio pins and the m3u_parser library for parsing the m3u files and pyttsx3, a text-to-speech conversion library in Python.

It has two types of notifications: wx.adv(OS notification) and popup windows.

*Not testing with other python versions.

## Features
- Playe channels in fullscreen, doing streaming from url in a m3u file.
- Changes volumen.
- Shows list of the channels.
- Speech some information.
- Works in raspberry 4.

## First step: Installation of dependencies
    $ pip install requirements.txt 

## Setting IR received(HX1838) in Raspberry pi.

![The IR receiver](https://github.com/freseco/pyerir/blob/main/pics/IRreceiver_remoteControl.jpg)

## Start the pigpio daemon

[Install the pigpiod libraries](https://abyz.me.uk/rpi/pigpio/download.html)

$ sudo pigpiod


## Using
    $ python[3.9] pyerir.py [-v | --version]  [<m3u_file_name>] [--debug]

Parameters:
- [-v | --version] shows script version.
- [m3u_file_name] file to get the channels.
- [--debug] shows debug information in console.

*by default, it will try to open tdt.m3u

## Remote control

### Normal mode
![Normal mode](https://github.com/freseco/pyerir/blob/List-of-channels/pics/remote_control_1.png)

### List channels mode
![List menu channels](https://github.com/freseco/pyerir/blob/List-of-channels/pics/remote_control_2.png)

## Development status
Pyerir is beta software, but it can be used

## VLC in python
[VLC module in Python](https://www.geeksforgeeks.org/vlc-module-in-python-an-introduction/)

## m3u_parser library.
[m3u_parser](https://pypi.org/project/m3u-parser/)

## TODO:
- [ ] Memorize favorite channels.
- [ ] **Up** and **down** buttons to change the volume(Normal mode).
- [ ] **Right** and **left** buttons to change the channel(Normal mode).
- [ ] Testing in other platforms.
- [ ] Read configuration file(**config.py**): favorite channels, ~~url or path of m3u file~~.(Done)
- [ ] Get channels information from Xtream-Codes IPTV servers.
- [ ] Shows channel's logo if it exists.
- [ ] Option to create IR codes from a new remote cotrol with a parameters in the script..
- [ ] Splass screen.
- [ ] Source code refactoring
- [ ] Facilitate the installation of the script. Create an installer?
- [ ] Improve of readme file.
- [ ] Transparencies in windows menu.
- [ ] Create logo of the app.
- [ ] Add opcions of mute and poweroff in remote control when it is in list channel mode.

## Error list:
- No exit well when push #
- Key only when windows channel o volumen are shown.

## Debugging

$ python[3.9] pyerir.py [--debug]


## Discussion
Our main forum for discussion is the project's [GitHub issue tracker](https://github.com/freseco/pyerir/issues). This is the right place to start a discussion of any of the above or most any other topic concerning the project.

## Contributing
Help in testing, development, documentation and other tasks is highly appreciated and useful to the project.

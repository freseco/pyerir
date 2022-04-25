# PYERIR
## About
Simple fullscreen player for m3u files(IPTV:tv:). It works in Raspberry pi 4 with Python3.9. It can get the IR code from (any?) IR remote control.

![RaspberryPI](https://www.raspberrypi.org/pagekit-assets/media/images/4913a547895720ff30c1.svg)**+**![Python](https://www.python.org/static/img/python-logo.png)**+**![wxpython](https://www.wxpython.org/images/header-logo.png)**+**![VLC](https://images.videolan.org/images/VLC-IconSmall.png)**+**![IR_Receiver](https://github.com/freseco/pyerir/blob/List-of-channels/pics/IR_receiver.png)


This project is a small example of wxpython for the GUI, threading for getting the IR codes, using wraper vlc library, gpio pins and the m3u_parser library for parsing the m3u files and pyttsx3, a text-to-speech conversion library in Python.

It has two types of notifications: wx.adv(OS notification) and popup windows.

Enjoy it and I would like to know if you have used it, thanks.


*Not testing with other python versions.

## Features
- Play channels in fullscreen, doing streaming from url in a m3u file.
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

## Development status:rescue_worker_helmet:
Pyerir is beta software, but it can be used if no error prevents you:roll_eyes:.

## VLC in python
Install vlc if your raspberry does not have:construction_worker_woman:.

>sudo apt update && sudo apt install vlc -y

[VLC module in Python](https://www.geeksforgeeks.org/vlc-module-in-python-an-introduction/)

## TODO:pencil2::
- [ ] Memorize favorite channels.
- [ ] **Up**:arrow_up: and **down**:arrow_down: buttons to change the volume(Normal mode).
- [ ] **Right**:arrow_right: and **left**:arrow_left: buttons to change the channel(Normal mode).
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
- [ ] Show menu for list of channels group.
- [ ] Testing script in raspberry pi 3.

## :warning:Error list:
- No exit well when push #
- Key only when windows channel o volumen are shown.

## Debugging:construction_worker:

$ python[3.9] pyerir.py [--debug]


## Discussion:speak_no_evil:
Our main forum for discussion is the project's [GitHub issue tracker](https://github.com/freseco/pyerir/issues). This is the right place to start a discussion of any of the above or most any other topic concerning the project.

## Contributing:sos:
Help in testing, development, documentation and other tasks is highly appreciated and useful to the project.

## Support:hearts:
Want to help me out? While donations aren't required, they are greatly appreciated and and speed up the development!

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](buymeacoffee.com/fresecoO)

# THANK YOU!

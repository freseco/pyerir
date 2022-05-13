# PYERIR
## About
Simple fullscreen player for m3u files(IPTV:tv:). It works in Raspberry pi 4 with **Python3.9** from Linux command line. It can get the IR code from (any?) IR remote control.

![RaspberryPI](https://www.raspberrypi.org/pagekit-assets/media/images/4913a547895720ff30c1.svg)         **+**        ![Python](https://www.python.org/static/img/python-logo.png)       **+**   ![wxpython](https://www.wxpython.org/images/header-logo.png)**+**![VLC](https://images.videolan.org/images/VLC-IconSmall.png)**+**![IR_Receiver](/pics/IR_receiver.png)


This project is a small example of how to use wxpython for the GUI, threading(Thread-based parallelism) for getting the IR codes, using a wraper for vlc media player library, gpio pins and the m3u_parser library for parsing the m3u files and pyttsx3, a text-to-speech conversion library in Python.

It has two types of notifications: wx.adv(OS notification) and popup windows.

Enjoy it and I would like to know if you have used it, thanks.


*Not tested with other python versions.

## Features
- Play channels in fullscreen, streaming from url in a m3u file.
- Changes volumen.
- Shows list of the channels.
- Text-to-speech output for some help information.
- Works in raspberry 4.

## The first step is to get the code of the repository, downloading or cloning it.

- [**Repository**](https://github.com/freseco/pyerir/archive/refs/heads/main.zip). Once the file is downloaded, unzip it.

Or

- **Clone using the git command:**

    $ **git** clone git@github.com:freseco/pyerir.git



## Second step: Since it's a python proyect, we need to install the dependencies. The file that indicates the dependencies is in the directory named sourcecode. Using the following command, we will install them.

- $ pip3 install -r requirements.txt 
    
    or with specific python version:
    
- $ python3.9 -m pip install -r requirements.txt
    


## Setting the Infrared Remote Control Module IR Receiver(HX1838) in Raspberry pi.

![The IR receiver](/pics/IRreceiver_remoteControl.jpg)

## Start the pigpio daemon at Startup: Pigpio is a Python module for the Raspberry which talks to the pigpio daemon to allow control of the general purpose input outputs (GPIO). It has to be running before to run pyerir. Run the following command on the terminal:

    $ sudo pigpiod

If you want it to run at startup. Open the terminal and type the following command to open the rc.local file: 

    $ sudo nano /etc/rc.local 

Enter the command that starts pigpiod before the "exit 0" line:


[help for pigpiod libraries](https://abyz.me.uk/rpi/pigpio/download.html)


## Using
    $ python[3.9] pyerir.py [-v | --version]  [<m3u_file_name>] [--debug] [--ircodes]

Parameters:
- [-v | --version] shows script version.
- [m3u_file_name] file to get the channels.
- [--debug] shows debug information in console.
- [--ircodes] Shows windows to ger new IR codes. They'll be saved in 'remoteIR.json' file.

*by default, it will try to open one of the these three options in **config.py** file:
- m3u file name. I has to be in the same path of the pyerir.py script.
- m3u url.
- Xtream code(not implemented yet).

In this file, you can setting those options.

## Remote control

### Normal mode
![Normal mode](/pics/remote_control_1.png)

### Channels list mode.
![List menu channels](/pics/remote_control_2.png)


## Configuration windows

![The IR receiver](/pics/conf_win1.png)
![The IR receiver](/pics/conf_win2.png)
![The IR receiver](/pics/conf_win3.png)

### Getting new IR codes.

Running:
python[3.9] pyerir.py --ircodes

Shows this windows, where you can change the IR code for every default button.

![Windows to get new IR codes.](/pics/winIRcodes.PNG)

When you finish to change the default ir codes, press the button 'Save IRcodes' to save de new ir codes in remoteIR.json.

This file will be read by pyerir.py the next time to run.


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
- [ ] Splass screen.
- [ ] Source code refactoring.
- [ ] Improve of readme file.
- [ ] Transparencies in windows menu.
- [ ] Create logo of the app.
- [ ] Add opcions of mute and poweroff in remote control when it is in list channel mode.
- [ ] Show menu for list of channels group.
- [ ] Testing script in raspberry pi 3(poor performance).
- [ ] Facilitate the installation of the script. Create an installer with PyInstaller(required install lastest python3.9-dev).


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

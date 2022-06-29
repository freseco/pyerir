# PYERIR
## :speech_balloon: About
A simple fullscreen player for m3u files (IPTV:tv:). Tested and working on a **Raspberry Pi 4 running Rasbian OS (32bits) with Python 3.9**(*). It can also get the IR code from any IR remote control (as far as I've tested).

![RaspberryPI](https://www.raspberrypi.org/pagekit-assets/media/images/4913a547895720ff30c1.svg)         **+**        ![Python](https://www.python.org/static/img/python-logo.png)       **+**   ![wxpython](https://www.wxpython.org/images/header-logo.png)**+**![VLC](https://images.videolan.org/images/VLC-IconSmall.png)**+**![IR_Receiver](/pics/IR_receiver.png)


This project is a small example of how to use:

 - [Wxpython](https://www.wxpython.org/) for the GUI,
 - Threading (thread-based parallelism) for getting the IR codes,
 - A wraper for VLC media player library and the m3u_parser library for parsing the m3u files,
 - [pyttsx3](https://pypi.org/project/pyttsx3/), a text-to-speech conversion library in Python,
 - And control of the General Purpose Input-Outputs (GPIO) in Raspberry PI.

It has two types of notifications: wx.adv (O.S. notification) and popup windows.

You might be asking yourselves why this project exists. As well as for the fun of it, I wanted to give my elder parents an easier way to watch IPTV channels. Some people still find very usefull an IR remote control, because it’s much easier to remember numbers that are assigned to specific channels.

I hope you find it as useful as I did. Please let me know if you have used it, or if you have had any problems. Thanks.

(*)Not tested with other python versions.

## :point_up: Features
- Play channels in fullscreen, streaming from url in a m3u file.
- Changes volumen.
- Shows list of the channels.
- Text-to-speech output for some information messages.
- Works in Raspberry 4. Though tested in a Raspberry 3B, it works kind of jerky, not recommended.

## :1234: Installation & configuration steps
 1. Get the code from the [repository](https://github.com/freseco/pyerir/archive/refs/heads/main.zip), and unzip. Or clone using the git command:

	 `$ git clone git@github.com:freseco/pyerir.git`

 2. Install dependencies. 
Since it's a python proyect, we need to install the dependencies. The file that indicates the dependencies is in the "sourcecode" directory. Install them with the following command.

	`$ pip3 install -r requirements.txt` 
    
    or with specific python version:
	`$ python3.9 -m pip install -r requirements.txt`
	
 3. Install software speech synthesizer for English and other languages:
 
 	`$ sudo apt espeak`
 
 4. Setting up the infrared remote control module IR Receiver (HX1838) in the Raspberry Pi

	![The IR receiver](/pics/GPIO.jpg)

 5. Start the pigpio daemon at Startup.
 [Pigpio](https://abyz.me.uk/rpi/pigpio/python.html) is a Python module for the Raspberry, which talks to the [pigpio daemon](https://abyz.me.uk/rpi/pigpio/pigpiod.html) to allow control of the General Purpose Input-Outputs (GPIO). Installation:

 
 	`$ sudo apt install pigpio python-pigpio python3-pigpio`

 	`$ sudo systemctl start pigpiod` 
 
 
 It has to be lauched before Pyerir. Run the following command on the terminal, will enable it to auto-start on boot:
 
	$ sudo systemctl enable pigpiod

[Help for pigpiod libraries.](https://abyz.me.uk/rpi/pigpio/download.html)

6. (Optional) You may need to increase the GPU memory split setting to 256MB for smoother performance.

	To adjust the memory split setting from the Raspbian desktop, click Menu >Preferences > Raspberry Pi Configuration, select the Performance tab, enter the required memory amount (256) into "GPU Memory:", click OK, and reboot.

	To adjust the memory split setting from the Raspbian command line, enter "sudo raspi-config", go to "Advanced Options" > "Memory Split", enter 256, select OK, select Finish, and reboot.

## :bookmark_tabs: How to use
    $ python[3.9] pyerir.py [-v | --version]  [<file_name.m3u>] [--debug] [--ircodes]

Optional parameters:
- [-v | --version] shows script version.
- [file_name.m3u] file to get the channels.
- [-\-debug] shows debug information in console.
- [-\-ircodes] Shows windows to capture new IR codes. They'll be saved in 'remoteIR.json' file.

*by default, it will try to open one of the these three options in **config.py** file:
- m3u file name. I has to be in the same path of the pyerir.py script.
- m3u url.
- Xtream code (not implemented yet).

In this file, you can setting those options.

## :tv: Remote control

### Normal mode
![Normal mode](/pics/remote_control_1.png)

### Channels list mode.
![List menu channels](/pics/remote_control_2.png)


## :pencil: Configuration windows

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


## :rescue_worker_helmet: Development status
Pyerir is beta software, but it can be used. If no error shows up :roll_eyes:.

## :clapper: VLC in python
Install vlc if your raspberry does not have:construction_worker_woman:.

    $ sudo apt update && sudo apt install vlc -y

[VLC module in Python](https://www.geeksforgeeks.org/vlc-module-in-python-an-introduction/)


## :pencil2: TODO:
- [ ] Memorize favorite channels.
- [ ] **Up**:arrow_up: and **down**:arrow_down: buttons to change the volume(Normal mode).
- [ ] **Right**:arrow_right: and **left**:arrow_left: buttons to change the channel(Normal mode).
- [ ] Testing in other platforms and hardwares: Orange pi, Banana pi, Rock 64, Raspberry Pi OS (64-bit), etc.
- [ ] Read configuration file (**config.py**): favorite channels, ~~url or path of m3u file~~.(Done)
- [ ] Get channels information from Xtream-Codes IPTV servers.
- [ ] Shows channel's logo, if it exists.
- [ ] Splash screen.
- [ ] Source code refactoring.
- [ ] Improve of readme file.
- [ ] Transparencies in windows menu.
- [ ] Create a requirements.txt with only needed dependencies.
- [ ] Create logo of the app.
- [ ] Add opcions of mute and poweroff in remote control when it is in "list channel" mode.
- [ ] Show menu for list of channels group.
- [x] Testing script in raspberry pi 3 (poor performance).
- [ ] Make it easier to install the script. Create an installer with PyInstaller (requires installing lastest python3.9-dev).
- [x] Change the font of the menu.
- [ ] Create a background script to start pyerir with the remote control. It will be started at boot.
- [x] Check long press. Impossible for volume windows with this architecture.
- [x] Add more buttos to configure: power ON/OFF rasp or screen, go back to the previous channel, Mute, show tech info on the screen.


## :warning: Error list:
- Does not exit well when pressing #
- ~~Key only when windows channel o volumen are shown.~~

## :construction_worker: Debugging

    $ python[3.9] pyerir.py [--debug]


## :speak_no_evil: Discussion
Our main forum for discussion is the project's [GitHub issue tracker](https://github.com/freseco/pyerir/issues). This is the right place to start a discussion of any of the above, or any other topic concerning the project.

## :sos: Contributing
Help in testing, development, documentation and other tasks is highly appreciated and useful to the project.

## :heart_decoration: Support
Want to help me out? Donations aren't required, but they are greatly appreciated and speeds up the development!

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](buymeacoffee.com/fresecoO)

# :man: THANK YOU!

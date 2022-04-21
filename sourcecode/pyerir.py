#! /usr/bin/python
# -*- coding: utf-8 -*-

# <https://github.com/freseco>
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston MA 02110-1301, USA.
#
"""
A simple example for VLC python bindings using wxPython and PIOG IR codes reading.

https://github.com/oaubert/python-vlc/blob/master/examples/wxvlc.py

pigpiod libraries:
https://abyz.me.uk/rpi/pigpio/download.html

Author: FReseco
Date: 10-04-2022

First run:
sudo pigpiod

Second to execute this script:
python3.9 wxpython_test.py

Show a windows in a fullscreen mode.

Keys:
	ESC to exit.
	F1 play.
	F2 stop.

"""
import logging
from cmath import log
import sys
import wx
import wx.adv #notification popup
import vlc
from os.path import basename,expanduser, isfile
from my_m3u_parser import M3uParser
import my_helper
import vlc
import os
from pathlib import Path
import mythreadIR
import pyttsx3



__version__ = '1.00.0'

class VentanaCanal(wx.Frame):
    
    def cerrarventana(self):
        self.timer.Start(500)
  
    def __init__(self, parent=None):
        style = ( wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.FRAME_SHAPED )
    
        height=150
        width=1450
        
        self.frame=wx.Frame.__init__(self, style = style,parent=parent,size=(width,height),pos = (10,500))

        panel = wx.Panel(self,size=(width,height),style=wx.TRANSPARENT_WINDOW) 
        panel.SetBackgroundColour((0,0,0))
                
        self.lbl = wx.StaticText(panel,-1,style = wx.ALIGN_LEFT,size=(width,height),pos=(50,10))
        font = wx.Font(55, wx.ROMAN, wx.ITALIC, wx.NORMAL) 
        self.lbl.SetFont(font) 
    
        self.lbl.SetForegroundColour((255,255,255)) 
        self.lbl.SetBackgroundColour((0,0,0)) 
        self.lbl.SetLabel("PYERIR") 
        

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        
        self.SetTransparent(240)
        self.segundos=12
        self.Hide()
        
    #actualización con el timer	
    def update(self, event):
        logging.debug("seconds %s to close windowschannel",self.segundos)
        
        self.segundos-=1
        
        self.SetFocus()
        if self.segundos==0:            
            self.timer.Stop()
            #self.Close()
            self.Hide()
            logging.debug("Closed/Hide windowschannel!")
            
    def mostrar(self, texto):
        self.segundos=12
        self.lbl.SetLabel(texto) 
        if not self.timer.IsRunning():
            self.Show()
            self.SetFocus()
            self.cerrarventana()

class VentanaVolumen(wx.Frame):
    """
    Class used for creating frames other than the main one
    """
    segundos=4

    def cerrarventana(self):
        self.timer.Start(1000)
  
    def __init__(self,  parent=None):
        super(VentanaVolumen, self).__init__()
        style = ( wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.FRAME_SHAPED )
        
        
        self.SetWindowStyle(wx.STAY_ON_TOP)
        
        screen_width, screen_height = wx.GetDisplaySize()
        
        height=150
        width=1450
        
        frame=wx.Frame.__init__(self, style = style,parent=parent,size=(width,height),pos = (0,200))

        panel = wx.Panel(self,size=(width,height),style=wx.TRANSPARENT_WINDOW) 
        
        
        self.lbl = wx.StaticText(panel,-1,style = wx.ALIGN_LEFT,size=(screen_width,height))
        font = wx.Font(60, wx.ROMAN, wx.ITALIC, wx.NORMAL) 
        self.lbl.SetFont(font) 
        self.lbl.SetForegroundColour((255,0,0)) 
        self.lbl.SetBackgroundColour((0,0,0))
        

         

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        
        self.SetTransparent(240)
        self.Hide()
        
        
    #actualización con el timer	
    def update(self, event):
        logging.debug("seconds %s to close ventanavolumnen",self.segundos)
        self.segundos-=1
        self.SetFocus()
        if self.segundos==0:            
            self.timer.Stop()
            self.Hide()
            logging.debug("ventana cerrada")
            
    def mostrar(self, valor):
        self.segundos=4
        valor_backup=valor
        caracter=" \x7C "
        texto="Volumen: "
        valor=valor/10
        while valor>0:
            texto=texto+caracter
            valor=valor-1
            
        self.lbl.SetLabel( texto+str(valor_backup)+" %")
         
        if not self.timer.IsRunning():
            self.Show()
            self.SetFocus()
            self.cerrarventana()




class MyPanel(wx.Panel):
			
	def __init__(self, parent,video=''):
		#m3u file
		self.video = video

		width, height = wx.GetDisplaySize()
		logging.debug("Resolution: "+str(width)+"x"+str(height))
		wx.Panel.__init__(self, parent,id= -1, size=(width-200,height-100))

		
		#handler for KEY PRESS
		self.Bind(wx.EVT_KEY_DOWN, self.onKey)
		

		self.Layout()
		self.Show()
		logger=logging.getLogger(__name__)
		if logger.getEffectiveLevel()==logging.DEBUG:  
			vlc_options = '--no-xlib --no-quiet --no-video-on-top'#--video-title-show --no-quiet --video-title-timeout=5'
		else:
			vlc_options = '--no-xlib --quiet --no-video-on-top'#--video-title-show --no-quiet --video-title-timeout=5'
		
		self.vlc_instance = vlc.Instance(vlc_options)
		self.player =self.vlc_instance.media_player_new()		
		
		self.Bind(wx.EVT_CHAR_HOOK, self.onKey)
  
		
		useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
		self.parser = M3uParser(timeout=5, useragent=useragent)
		
		
		self.parser.parse_m3u(self.video)
		self.parser.sort_by("name",asc=True)
		#type dict
		self.channels = self.parser.get_list()

		if len(self.channels)==0:
			logging.debug('No channel in m3u file!')
			exit()

		self.numcanales=len(self.channels)
		logging.debug("Number of channels: "+str(self.numcanales))
		self.actualcanal=0
  
		self.engine = pyttsx3.init()		
		rate = self.engine.getProperty('rate')   # getting details of current speaking rate
		self.engine.setProperty('voice', 'spanish')
		self.engine.setProperty('rate', 120)     # setting up new voice rateate
		self.speech("Hay, "+str(self.numcanales)+" canales.")
  
	# Set up event handler for any worker thread results
		mythreadIR.evt_result(self,self.OnResultIRcode)
	# Initial receving IR codes
		self.worker = mythreadIR.WorkerThread(self)
  
		
		self.winchannel= VentanaCanal(self)
		self.winvolume = VentanaVolumen(self)
  
  #Pressing numbers in the remote control
		self.timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.update, self.timer)
		self.seconds=4
		self.canaltecleado=""
  
  
	def speech(self,text):
		self.engine.say(text)
		self.engine.runAndWait()
  
    #actualización con el timer	
	def update(self, event):
		logging.debug("seconds %s to end pressing numbers",self.seconds)		
		self.seconds-=1
		self.SetFocus()
		if self.seconds==0:
			if len(self.canaltecleado)>0:
				self.ShowsThiscanal(int(self.canaltecleado))
			self.canaltecleado=""
			self.timer.Stop()
			self.seconds=4  
            
	def OnResultIRcode(self,codigo):			
			if codigo.data==mythreadIR.remote.ok:
				self.stop()       
				logging.debug("Pulsado OK")
			elif codigo.data==mythreadIR.remote.zero:
				#self.ShowsThiscanal(0)	
				self.canaltecleado+="0"
				self.winchannel.mostrar(self.canaltecleado)
				logging.debug("Pulsado 0")           
			elif codigo.data==mythreadIR.remote.one:
				#self.ShowsThiscanal(1)
				self.canaltecleado+="1"
				self.winchannel.mostrar(self.canaltecleado)
				logging.debug("Pulsado 1")
			elif codigo.data==mythreadIR.remote.two:
				#self.ShowsThiscanal(2)
				self.canaltecleado+="2"
				self.winchannel.mostrar(self.canaltecleado)
				logging.debug("Pulsado 2")
			elif codigo.data==mythreadIR.remote.three:
				#self.ShowsThiscanal(3)
				self.canaltecleado+="3"
				self.winchannel.mostrar(self.canaltecleado)
				logging.debug("Pulsado 3")
			elif codigo.data==mythreadIR.remote.four:
				#self.ShowsThiscanal(4)
				self.canaltecleado+="4"
				self.winchannel.mostrar(self.canaltecleado)
				logging.debug("Pulsado 4")
			elif codigo.data==mythreadIR.remote.five:
				#self.ShowsThiscanal(5)
				self.canaltecleado+="5"
				self.winchannel.mostrar(self.canaltecleado)
				logging.debug("Pulsado 5")
			elif codigo.data==mythreadIR.remote.six:
				#self.ShowsThiscanal(6)
				self.canaltecleado+="6"
				self.winchannel.mostrar(self.canaltecleado)
				logging.debug("Pulsado 6")
			elif codigo.data==mythreadIR.remote.seven:
				#self.ShowsThiscanal(7)
				self.canaltecleado+="7"
				self.winchannel.mostrar(self.canaltecleado)
				logging.debug("Pulsado 7")
			elif codigo.data==mythreadIR.remote.eight:
				#self.ShowsThiscanal(8)
				self.canaltecleado+="8"
				self.winchannel.mostrar(self.canaltecleado)
				logging.debug("Pulsado 8")
			elif codigo.data==mythreadIR.remote.nine:
				#self.ShowsThiscanal(9)
				self.canaltecleado+="9"
				self.winchannel.mostrar(self.canaltecleado)
				logging.debug("Pulsado 9")
			elif codigo.data==mythreadIR.remote.hash:
				logging.debug("Pulsado #")
				self.speech("¡Hasta luego!")
				self.exit()
			elif codigo.data==mythreadIR.remote.up:
				self.siguientecanal()
				logging.debug("Pulsado up")
			elif codigo.data==mythreadIR.remote.down:
				self.anteriorcanal()
				logging.debug("Pulsado down")
			elif codigo.data==mythreadIR.remote.left:
				self.BajarVolumen()
				logging.debug("Pulsado left")
			elif codigo.data==mythreadIR.remote.right:
				self.SubirVolumen()
				logging.debug("Pulsado right")
			elif codigo.data==mythreadIR.remote.asterisk:
				self.OnMute()
				logging.debug("Pulsado *")			
			else:
				logging.debug("Botón no reconocido! " +str(codigo))		
    	
			if self.canaltecleado.isnumeric():
				if self.numcanales>int(self.canaltecleado):
					if self.timer.IsRunning():
						self.seconds+=3
					else:
						self.timer.Start(1000)
				else:
					self.canaltecleado=""
					self.timer.Stop()
					self.seconds=4
					self.winchannel.mostrar("Out of range!")
					logging.debug("number out of the channels range")

	#pushing key	
	def onKey(self, event):	
		#https://wxpython.org/Phoenix/docs/html/wx.KeyCode.enumeration.html
		key_code = event.GetKeyCode()
		
		logging.debug("Tecla: "+str(key_code))
		if key_code == wx.WXK_ESCAPE:
			logging.debug("Tecla: ESC => Exit()")
			self.exit()	
		elif key_code == 84:# letter T
			self.OnMute()
			logging.debug("Tecla: T= mute")
		elif key_code == wx.WXK_F1:
			self.play()
		elif key_code == wx.WXK_F2:
			self.stop()
		elif key_code== wx.WXK_UP:
			self.SubirVolumen()
		elif key_code==wx.WXK_DOWN:
			self.BajarVolumen()
		elif key_code==wx.WXK_LEFT:
			self.anteriorcanal()
		elif key_code==wx.WXK_RIGHT:
			self.siguientecanal()			
		else:			
			event.Skip()

			
	def SubirVolumen(self):
     	# since vlc volume range is in [0, 200],
        # and our volume slider has range [0, 100], just divide by 2.
        # self.volslider.SetValue(self.player.audio_get_volume() / 2)		
		valor=vlc.libvlc_audio_get_volume(self.player)
		if valor!=100:
			valor+=1
			while valor%10!=0:
				valor+=1
		self.winvolume.mostrar(valor)
		self.ShowMsgClicked('Volumen:',str(valor))
		vlc.libvlc_audio_set_volume(self.player, valor)

	def BajarVolumen(self):		
		valor=vlc.libvlc_audio_get_volume(self.player)
		if valor!=0:
			valor-=1
			while valor%10!=0:
				valor-=1
		self.winvolume.mostrar(valor)
		self.ShowMsgClicked('Volumen:',str(valor))
		vlc.libvlc_audio_set_volume(self.player, valor)

	def ShowsThiscanal(self,nextcanal):
    		
		self.actualcanal=nextcanal
			
		infochannel=self.channels[self.actualcanal]
		logging.debug("Channel name: "+infochannel["name"])
		logging.debug("Status channel: "+infochannel["status"])
  
		self.winchannel.mostrar(str(nextcanal)+": "+infochannel["name"])
  
		self.ShowMsgClicked('CANAL:',infochannel["name"])
		logging.debug("Url: "+infochannel["url"])		
		media = self.vlc_instance.media_new(infochannel["url"])
		# setting media to the player
		self.player.set_media(media)		
  
		# set the window id where to render VLC's video output
		handle = self.GetHandle()
		if sys.platform.startswith('linux'):  # for Linux using the X Server
			self.player.set_xwindow(handle)
		elif sys.platform == "win32":  # for Windows
			self.player.set_hwnd(handle)
		elif sys.platform == "darwin":  # for MacOS
			self.player.set_nsobject(handle)
    
      
		# play the video
		self.player.play()



	def siguientecanal(self):
		nextcanal= self.actualcanal+1
		if nextcanal>=self.numcanales:
			nextcanal=0

		self.actualcanal=nextcanal

		infochannel=self.channels[self.actualcanal]
		logging.debug("Channel name: "+infochannel["name"])
		logging.debug("Status channel: "+infochannel["status"])
  
		self.winchannel.mostrar(str(nextcanal)+": "+infochannel["name"])
  
		self.ShowMsgClicked('CANAL:',infochannel["name"])
		logging.debug("Url: "+infochannel["url"])		
		media = self.vlc_instance.media_new(infochannel["url"])
		# setting media to the player
		self.player.set_media(media)		
  
		# set the window id where to render VLC's video output
		handle = self.GetHandle()
		if sys.platform.startswith('linux'):  # for Linux using the X Server
			self.player.set_xwindow(handle)
		elif sys.platform == "win32":  # for Windows
			self.player.set_hwnd(handle)
		elif sys.platform == "darwin":  # for MacOS
			self.player.set_nsobject(handle)
    
      
		# play the video
		self.player.play()

	def anteriorcanal(self):    
		nextcanal= self.actualcanal-1
		if nextcanal<0:
			nextcanal=len(self.channels)-1
		
		self.actualcanal=nextcanal
  
		logging.debug("Position channel: "+str(nextcanal))

		infochannel=self.channels[self.actualcanal]

		logging.debug(infochannel["url"])
		self.winchannel.mostrar(str(nextcanal)+": "+infochannel["name"])
		self.ShowMsgClicked('Channel:',infochannel["name"])
		media = self.vlc_instance.media_new(infochannel["url"])
		# setting media to the player
		self.player.set_media(media)
		
  # set the window id where to render VLC's video output
		handle = self.GetHandle()
		if sys.platform.startswith('linux'):  # for Linux using the X Server
			self.player.set_xwindow(handle)
		elif sys.platform == "win32":  # for Windows
			self.player.set_hwnd(handle)
		elif sys.platform == "darwin":  # for MacOS
			self.player.set_nsobject(handle)
   
  		# play the video
		self.player.play()
   
	def stop(self):
		 #Pause the player.
		if self.player.is_playing():
			self.player.stop()
   		
	def OnMute(self):
        #Mute/Unmute according to the audio button.
		muted = self.player.audio_get_mute()
		self.player.audio_set_mute(not muted)
		logging.debug("Mute if muted else Unmute")    
        
	def exit(self):
		
		self.worker._want_abort=True
		self.stop()
		self.GetParent().Close()
		sys.exit(0)

	def ShowMsgClicked(self,sTitle,texto):		
		sMsg =texto	# 'This is a notification message.\n\nWelcome on wxWidgets ;-)'

		nmsg = wx.adv.NotificationMessage(title=sTitle, message=sMsg)
		nmsg.SetFlags(wx.ICON_INFORMATION)

		nmsg.Show(timeout=wx.adv.NotificationMessage.Timeout_Auto)



class MyFrame(wx.Frame):

	def __init__(self,title='',video=''):		

		wx.Frame.__init__(self, None,-1,title=title)
		
		self.panel1 = MyPanel(self,video=video)		

		self.panel1.SetBackgroundColour(wx.BLACK)		
			
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)# | wx.STAY_ON_TOP) 
  
		

if __name__ == "__main__":
	_video = "tdt.m3u"

	debugging=False
	
	#print("Logging level: "+str(logging.getLevelName(logging.level))	)
 
	while len(sys.argv) > 1:
		arg = sys.argv.pop(1)
		if arg.lower() in ('-v', '--version'):
			# show all versions:
			# % python3 ./pyerir.py -v
			# wxpython_test.py: 1.00.0 (wx 4.1.1 gtk3 (phoenix) wxWidgets 3.1.5 _core.cpython-39-arm-linux-gnueabihf.so)


		# Print version of this vlc.py and of the libvlc
			c = basename(str(wx._core).split()[-1].rstrip('>').strip("'").strip('"'))
			logging.warning('%s: %s (%s %s %s)' % (basename(__file__), __version__,wx.__name__, wx.version(), c))

			try:
				vlc.print_version()
				vlc.print_python()
			except AttributeError:
				pass		
			sys.exit(0)
		elif arg.lower() in ('--debug'):
			logging.basicConfig(stream=sys.stdout,level=logging.DEBUG, format="%(levelname)s: %(message)s")
			logging.debug('Debugging mode enable!')			
			debugging=True
   
		elif arg.startswith('-'):
			logging.info('usage: %s  [-v | --version]  [<m3u_file_name>]  [--debug]' % (sys.argv[0],))
			sys.exit(1)

		elif arg:  # m3u file
			_video = expanduser(arg)
			if not my_helper.is_valid_url(_video):
				m3ufile=os.path.join(Path( __file__ ).parent.absolute(),_video)
				if not isfile(m3ufile):
					logging.warning('%s error: no such file or url: %r' % (sys.argv[0], arg))
					sys.exit(1)


	if not debugging:
		logging.basicConfig(stream=sys.stdout,level=logging.INFO, format="%(levelname)s: %(message)s")
  
	# Create a wx.App(), which handles the windowing system event loop
	app = wx.App(False)

	# Create the window containing our media player
	frame = MyFrame(title='pyerir',video=_video)

	# run the application
	app.MainLoop()
	
	sys.exit(0)
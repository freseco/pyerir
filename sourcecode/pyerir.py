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

import sys
import wx
import wx.adv #notification popup
import vlc
from os.path import basename,expanduser, isfile
from m3u_parser import M3uParser
import vlc
import os
from pathlib import Path

import mythreadIR


__version__ = '1.00.0'


class VentanaCanal(wx.Frame):
    """
    Class used for creating frames other than the main one
    """
    segundos=6

    def cerrarventana(self):
        self.timer.Start(1000)
  
    def __init__(self, parent=None):
        style = ( wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.FRAME_SHAPED )
        
        height=150
        width=1450
        
        frame=wx.Frame.__init__(self, style = style,parent=parent,size=(width,height),pos = (10,50))

        panel = wx.Panel(self,size=(width,height),style=wx.TRANSPARENT_WINDOW) 
        panel.SetBackgroundColour((0,0,0))
                
        self.lbl = wx.StaticText(panel,-1,style = wx.ALIGN_CENTER,size=(width,height),pos=(0,10))
        font = wx.Font(55, wx.ROMAN, wx.ITALIC, wx.NORMAL) 
        self.lbl.SetFont(font) 
    
        self.lbl.SetForegroundColour((255,0,0)) 
        self.lbl.SetBackgroundColour((0,0,0)) 
        self.lbl.SetLabel("PYERIR") 
        

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        
        self.SetTransparent(240)
        #self.Show()
        #self.SetFocus()        
        #self.cerrarventana()
        self.Hide()
        
    #actualización con el timer	
    def update(self, event):
        print("seconds %s to close windowschannel",self.segundos)
        self.segundos-=1
        self.SetFocus()
        if self.segundos==0:            
            self.timer.Stop()
            #self.Close()
            self.Hide()
            print("Closed/Hide windowschannel!")
            
    def mostrar(self, texto):
        self.segundos=4
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
        
        frame=wx.Frame.__init__(self, style = style,parent=parent,size=(width,height),pos = (100,590))

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
        #self.Show()
        #self.SetFocus()	
        #self.cerrarventana()
        
    #actualización con el timer	
    def update(self, event):
        print("seconds %s to close ventanavolumnen",self.segundos)
        self.segundos-=1
        self.SetFocus()
        if self.segundos==0:            
            self.timer.Stop()
            self.Hide()
            print("ventana cerrada")
            
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
	segundos=2
 

	def mostrarcanal(self):
		self.timer.Start(1000)
		
	def __init__(self, parent,video=''):
		#m3u file
		self.video = video

		width, height = wx.GetDisplaySize()
		print("Resolución: "+str(width)+"x"+str(height))
		wx.Panel.__init__(self, parent,id= -1, size=(width-200,height-100))

		self.funcionar=True
		#self.timer = wx.Timer(self)
		#self.Bind(wx.EVT_TIMER, self.update, self.timer)	

		
		#handler for KEY PRESS
		self.Bind(wx.EVT_KEY_DOWN, self.onKey)
		

		self.Layout()
		self.Show()
  	
		vlc_options = '--no-xlib --no-quiet --no-video-on-top'#--video-title-show --no-quiet --video-title-timeout=5'
		self.vlc_instance = vlc.Instance(vlc_options)
		self.player =self.vlc_instance.media_player_new()		
		
  
		
		useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
		self.parser = M3uParser(timeout=5, useragent=useragent)
		m3ufile=os.path.join(Path( __file__ ).parent.absolute(),self.video)
		
		   
		self.parser.parse_m3u(m3ufile)


		#type dict
		self.canal = self.parser.get_list()

		if len(self.canal)==0:
			print('No channel in m3u file!')
			exit()

		self.numcanales=len(self.canal)
		print("Número de canales: "+str(self.numcanales))
		self.actualcanal=10	
  
	# Set up event handler for any worker thread results
		mythreadIR.evt_result(self,self.OnResultIRcode)
	# Initial receving IR codes
		self.worker = mythreadIR.WorkerThread(self)
  
		#self.mostrarcanal()
		self.winchannel=VentanaCanal(self)
		self.winvolume=VentanaVolumen(self)

  
	def OnResultIRcode(self,codigo):			
			if codigo.data==mythreadIR.remote.ok:
				self.stop()       
				print("Pulsado OK")
			elif codigo.data==mythreadIR.remote.zero:
				print("Pulsado 0")           
			elif codigo.data==mythreadIR.remote.one:				
				print("Pulsado 1")
			elif codigo.data==mythreadIR.remote.two:
				print("Pulsado 2")
			elif codigo.data==mythreadIR.remote.three:
				print("Pulsado 3")
			elif codigo.data==mythreadIR.remote.four:
				print("Pulsado 4")
			elif codigo.data==mythreadIR.remote.five:
				print("Pulsado 5")
			elif codigo.data==mythreadIR.remote.six:
				print("Pulsado 6")
			elif codigo.data==mythreadIR.remote.seven:
				print("Pulsado 7")
			elif codigo.data==mythreadIR.remote.eight:
				print("Pulsado 8")
			elif codigo.data==mythreadIR.remote.nine:
				print("Pulsado 9")
			elif codigo.data==mythreadIR.remote.hash:
				print("Pulsado #")
				self.exit()
			elif codigo.data==mythreadIR.remote.up:
				self.siguientecanal()
				print("Pulsado up")
			elif codigo.data==mythreadIR.remote.down:
				self.anteriorcanal()
				print("Pulsado down")
			elif codigo.data==mythreadIR.remote.left:
				self.BajarVolumen()
				print("Pulsado left")
			elif codigo.data==mythreadIR.remote.right:
				self.SubirVolumen()
				print("Pulsado right")
			elif codigo.data==mythreadIR.remote.asterisk:
				self.exit()
				print("Pulsado *")			
			else:
				print("Botón no reconocido! " +str(codigo))			
			
  
	#pushing key	
	def onKey(self, event):	
		#https://wxpython.org/Phoenix/docs/html/wx.KeyCode.enumeration.html
		key_code = event.GetKeyCode()
		
		print("Tecla: "+str(key_code))
		if key_code == wx.WXK_ESCAPE:
			print("Tecla: ESC => Exit()")
			self.exit()	
		elif key_code == 84:# letter T
			self.segundos=4
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

	#actualización con el timer	
	def update(self, event):
		print("segunods %s",self.segundos)
		self.segundos-=1
		if self.segundos==0:
			self.siguientecanal()
			self.timer.Stop()
			print("parado")
			
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

	def siguientecanal(self):
		nextcanal= self.actualcanal+1
		if nextcanal<self.numcanales:
			self.actualcanal=nextcanal
		else:
			self.actualcanal=0
			
		# creating a media
		print("Channel:")
		print(self.canal[self.actualcanal]["name"])
		#framecanal=VentanaCanal(self.canal[self.actualcanal]["name"])
  
		self.winchannel.mostrar(self.canal[self.actualcanal]["name"])
  
		self.ShowMsgClicked('CANAL:',self.canal[self.actualcanal]["name"])
		print(self.canal[self.actualcanal]["url"])		
		media = self.vlc_instance.media_new(self.canal[self.actualcanal]["url"])
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
		print(self.player.video_get_title_description())

	def anteriorcanal(self):    
		nextcanal= self.actualcanal-1
		if nextcanal>=0:
			self.actualcanal=nextcanal
		else:
			self.actualcanal=0
			
		# creating a media
		print(self.canal[self.actualcanal]["url"])
		self.winchannel.mostrar(self.canal[self.actualcanal]["name"])
		self.ShowMsgClicked('CANAL:',self.canal[self.actualcanal]["name"])
		media = self.vlc_instance.media_new(self.canal[self.actualcanal]["url"])
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
   		
	def OnMute(self, evt):
        #Mute/Unmute according to the audio button.
		muted = self.player.audio_get_mute()
		self.player.audio_set_mute(not muted)
		self.mute.SetLabel("Mute" if muted else "Unmute")    
        
	def exit(self):
		self.funcionar=False
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
	while len(sys.argv) > 1:
		arg = sys.argv.pop(1)
		if arg.lower() in ('-v', '--version'):
			# show all versions, sample output on macOS:
			# % python3 ./wxpython_text.py -v
			# wxpython_test.py: 1.00.0 (wx 4.1.1 gtk3 (phoenix) wxWidgets 3.1.5 _core.cpython-39-arm-linux-gnueabihf.so)


		# Print version of this vlc.py and of the libvlc
			c = basename(str(wx._core).split()[-1].rstrip('>').strip("'").strip('"'))
			print('%s: %s (%s %s %s)' % (basename(__file__), __version__,wx.__name__, wx.version(), c))

			try:
				vlc.print_version()
				vlc.print_python()
			except AttributeError:
				pass		
			sys.exit(0)

		elif arg.startswith('-'):
			print('usage: %s  [-v | --version]  [<m3u_file_name>]' % (sys.argv[0],))
			sys.exit(1)

		elif arg:  # m3u file
			_video = expanduser(arg)
			if not isfile(_video):
				print('%s error: no such file: %r' % (sys.argv[0], arg))
				sys.exit(1)


	# Create a wx.App(), which handles the windowing system event loop
	app = wx.App(False)

	# Create the window containing our media player
	frame = MyFrame(video=_video)

	# run the application
	app.MainLoop()

	print("after main")
	sys.exit(0)
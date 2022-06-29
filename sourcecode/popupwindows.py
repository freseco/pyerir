import wx
import wx.adv #notification popup
import logging
import my_helper
import requests
import io
from config import config

class VentanaCanal(wx.Frame):
    
    def cerrarventana(self):
        self.timer.Start(500)
  
    def __init__(self, parent=None):
        style = ( wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.FRAME_SHAPED )
    
        height=130
        width=1650
        super(VentanaCanal, self).__init__(parent,style=style, size=(width,height),pos=(10,10))
        
        panel = wx.Panel(self,size=(width,height),style=wx.TRANSPARENT_WINDOW) 
        panel.SetBackgroundColour((0,0,0))
                
        self.lbl = wx.StaticText(panel,-1,style = wx.ALIGN_LEFT,size=(width,height),pos=(50,10))
        font = wx.Font(55, wx.FONTFAMILY_SWISS, wx.ITALIC, wx.NORMAL) 
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
            
    def mostrar(self, texto,logo=""):
        self.segundos=12
        self.lbl.SetLabel(texto) 
        if not self.timer.IsRunning():
            self.Show()
            self.SetFocus()
            self.cerrarventana()


class VentanaLogo(wx.Frame):
    
    def cerrarventana(self):
        self.timer.Start(500)
  
    def __init__(self, parent=None):
        style = ( wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.FRAME_SHAPED )
    
        self.height=100
        self.width=70
        super(VentanaLogo, self).__init__(parent,style=style, size=(self.width,self.height),pos=(0,0))
        
        self.panel = wx.Panel(self,size=(self.width,self.height),pos=(0,0),style=wx.TRANSPARENT_WINDOW) 
        
        img = wx.Bitmap(self.width,self.height)
        self.staticImage = wx.StaticBitmap(self.panel, wx.ID_ANY,(img),pos=(0,0),size=(self.width,self.height))
        

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        
        
        self.segundos=12
        self.Hide()
        
    #actualización con el timer	
    def update(self, event):
        logging.debug("seconds %s to close VentanaLogo",self.segundos)
        
        self.segundos-=1
        
        self.SetFocus()
        if self.segundos==0:            
            self.timer.Stop()
            #self.Close()
            self.Hide()
            logging.debug("Closed/Hide VentanaLogo!")
            
    def mostrar(self, logo=""):
        self.segundos=12
        content = requests.get(logo).content
        io_bytes = io.BytesIO(content)
        image = wx.Image(io_bytes).Scale(self.width,self.height).ConvertToBitmap()
        
        self.staticImage.SetBitmap((image))
        self.panel.Refresh()
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
        
        screen_width, screen_height = wx.GetDisplaySize()
        
        height=150
        width=1450
        self.leftpos=0
        self.uppos=screen_height-height
        
        style = ( wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.FRAME_SHAPED )
        
        super(VentanaVolumen, self).__init__(parent,style=style, size=(screen_width,height),pos=(self.leftpos,self.uppos))
        

                
        self.SetWindowStyle(wx.STAY_ON_TOP)
          
        panel = wx.Panel(self,size=(screen_width,height),style=wx.TRANSPARENT_WINDOW)         
        
        self.lbl = wx.StaticText(panel,-1,style = wx.ALIGN_LEFT,size=(screen_width,height))
        font = wx.Font(60, wx.FONTFAMILY_SWISS, wx.ITALIC, wx.NORMAL) 
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
        self.SetPosition(wx.Point(self.leftpos,self.uppos))
        self.SetFocus()
        if self.segundos==0:            
            self.timer.Stop()
            self.Hide()
            logging.debug("ventana cerrada")
    
                
    def mostrar(self, valor):
        self.SetPosition(wx.Point(self.leftpos,self.uppos))
        self.segundos=4
        valor_backup=valor
        
        caracter='\u2588' 
        texto="Volumen: "
        valor=valor/10
        while valor>0:
            texto=texto+caracter+caracter
            valor=valor-1
            
        self.lbl.SetLabel( texto+str(valor_backup)+" %")
         
        if not self.timer.IsRunning():
            self.Show()
            self.SetFocus()
            self.cerrarventana()

class VentanaListChannels(wx.Frame):
	def __init__(self,  parent=None, Listchannels=None):
		
  
		self.listchanels=Listchannels
		screen_width, screen_height = wx.GetDisplaySize()
		
		height=910
		width=1100
		self.leftpos=0
		self.uppos=0
		
		style = ( wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.FRAME_SHAPED )
		super(VentanaListChannels, self).__init__(parent,style=style, size=(width,height),pos=(self.leftpos,self.uppos))
		

				
		self.SetWindowStyle(wx.STAY_ON_TOP)
			
		panel = wx.Panel(self,size=(width,height),style=wx.TRANSPARENT_WINDOW,pos=(0,0))
		panel.SetBackgroundColour((0,0,0))
  		
		self.longlistlbl=10
		self.listlbls=[]
		for x in range(0,self.longlistlbl+1):
			lbl = wx.StaticText(panel,-1,style = wx.ALIGN_LEFT,size=(width,height),pos=(0,x*80))
			
			
			lbl.SetForegroundColour((255,0,0)) 
			if x==5:
				lbl.SetBackgroundColour((255,255,255))
				lbl.SetForegroundColour((0,0,255))
				font = wx.Font(55, wx.FONTFAMILY_SWISS, wx.ITALIC, wx.BOLD) 
			else:
				lbl.SetBackgroundColour((0,0,0))
				font = wx.Font(50, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.NORMAL) 
			lbl.SetFont(font) 
			lbl.SetLabel("Canal "+str(x+1))
			self.listlbls.append(lbl)
  
		self.actualchannel=self.longlistlbl/2
  


		self.SetTransparent(240)
		self.Hide()
  

  
  #Shows windows and lista channels
	def Mostrar(self,actualchannel,listchannels):
		self.actualchannel=actualchannel  
		self.MostrarListCanales()		
		self.Show()
#shows list the channels and underline the actual channel.
	def MostrarListCanales(self):		
		numchannels=len(self.listchanels)
		infochannel=self.listchanels[self.actualchannel]
		self.listlbls[5].SetLabel(str(self.actualchannel)+": "+infochannel["name"])
  
		nextyes=self.actualchannel
		for x in range(6, self.longlistlbl+1):
			nextyes=self.get_nextchannel(nextyes,numchannels)
			self.listlbls[x].SetLabel(str(nextyes)+": "+self.listchanels[nextyes]["name"])	
			
   
		alteryes=self.actualchannel
		for x in range(5,0,-1):
			alteryes=self.get_alterchannel(alteryes,numchannels)
			self.listlbls[x-1].SetLabel(str(alteryes)+": "+self.listchanels[alteryes]["name"])
     
	def SetListchannels(self,List):
		self.listchanels=List
	def get_nextchannel(self,next_to,longlist):
		next=next_to+1
		if (next)>=longlist:
			return longlist-next
		else:
			return next

	def get_alterchannel(self,alter_to,longlist):
		alter=alter_to-1
		if alter<0:
			return longlist+alter
		else:
			return alter

	def Hideme(self):
		self.Hide()
  
	def NextChannel(self):		
		self.actualchannel = my_helper.next_number(self.actualchannel,len(self.listchanels)-1)
		self.MostrarListCanales()
		logging.debug("nextchannel")

	def AfterChannel(self):
		self.actualchannel = my_helper.previous_number(self.actualchannel,len(self.listchanels)-1)
		self.MostrarListCanales()
		logging.debug("afterchannel")
  

class WinConfig(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("Pyerir config video source..")
        self.SetFocus()
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.file = wx.Notebook(self, wx.ID_ANY)
        self.isShow=False
        self.m3ufile = wx.Panel(self.file, wx.ID_ANY)
        self.file.AddPage(self.m3ufile, u"1º m3u file.")
        self.textmodified=False
        self.saved=False
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.txtm3ufilename = wx.TextCtrl(self.m3ufile, wx.ID_ANY, "")
        sizer_1.Add(self.txtm3ufilename, 0, wx.EXPAND | wx.TOP, 70)

        self.notebook_1_pane_2 = wx.Panel(self.file, wx.ID_ANY)
        self.file.AddPage(self.notebook_1_pane_2, u"2º URL")

        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        self.textm3uURL = wx.TextCtrl(self.notebook_1_pane_2, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        sizer_2.Add(self.textm3uURL, 0, wx.ALL | wx.EXPAND, 0)

        self.notebook_1_pane_3 = wx.Panel(self.file, wx.ID_ANY)
        self.file.AddPage(self.notebook_1_pane_3, u"3º Xtream account")

        sizer_3 = wx.BoxSizer(wx.VERTICAL)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_6, 1, wx.EXPAND | wx.LEFT | wx.TOP, 17)

        label_2 = wx.StaticText(self.notebook_1_pane_3, wx.ID_ANY, "User:")
        label_2.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_6.Add(label_2, 1, wx.EXPAND | wx.LEFT | wx.TOP, 5)

        self.txtuser = wx.TextCtrl(self.notebook_1_pane_3, wx.ID_ANY, "")
        sizer_6.Add(self.txtuser, 1, 0, 0)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_5, 1, wx.EXPAND | wx.LEFT, 17)

        label_3 = wx.StaticText(self.notebook_1_pane_3, wx.ID_ANY, "Password:")
        label_3.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_5.Add(label_3, 1, wx.LEFT, 3)

        self.txtpassword = wx.TextCtrl(self.notebook_1_pane_3, wx.ID_ANY, "")
        sizer_5.Add(self.txtpassword, 1, 0, 0)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_4, 1, wx.EXPAND | wx.LEFT, 17)

        label_1 = wx.StaticText(self.notebook_1_pane_3, wx.ID_ANY, "Server:")
        label_1.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_4.Add(label_1, 1, wx.LEFT, 0)

        self.txtserver = wx.TextCtrl(self.notebook_1_pane_3, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        sizer_4.Add(self.txtserver, 3, 0, 0)

        

        self.file_pane_1 = wx.Panel(self.file, wx.ID_ANY)
        self.file.AddPage(self.file_pane_1, "Help")

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)

        label_4 = wx.StaticText(self.file_pane_1, wx.ID_ANY, "PYERIR will follow the order to load the source video.", style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_NO_AUTORESIZE)
        label_4.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_7.Add(label_4, 0, wx.EXPAND | wx.TOP, 50)

        self.file_pane_1.SetSizer(sizer_7)

        self.notebook_1_pane_3.SetSizer(sizer_3)

        self.notebook_1_pane_2.SetSizer(sizer_2)

        self.m3ufile.SetSizer(sizer_1)

        self.Layout()
    
    #Event about text changed
    def serverchanged (self, event):
        self.textmodified=True
        print("Server changed!")
    def userchanged (self, event):
        self.textmodified=True
        print("user changed!")
    def passwordchanged (self, event):
        self.textmodified=True
        print("password changed!")
    def m3ufilechanged (self, event):
        self.textmodified=True
         
    def m3uurlchanged (self, event):
        self.textmodified=True
        print("url changed!")
        
    def ShowWindows(self):
        self.readconfig()
        self.Show(True)
        
  
            
    def OnClose(self, event):
        self.saveconfig()
            
        
        
    def saveconfig(self):
        if self.saved==False and self.textmodified==True:
            conf=config()
            conf.data['IPTV_url'] =self.textm3uURL.GetValue()
            
            conf.data['m3u_file'] = self.txtm3ufilename.GetValue()
            
            conf.data['provider']['username']= self.txtuser.GetValue()
            conf.data['provider']['txtpassword']=self.txtpassword.GetValue()
            conf.data['provider']['server']=self.txtserver.GetValue()
            conf.savejson()
            self.saved=True
            return True
        
    def readconfig(self):
        conf=config()
        self.textm3uURL.SetValue(conf.data['IPTV_url']) 
                 
        self.txtm3ufilename.SetValue(conf.data['m3u_file'])
        
        self.txtuser.SetValue(conf.data['provider']['username'])
        self.txtpassword.SetValue(conf.data['provider']['password'])
        self.txtserver.SetValue(conf.data['provider']['server'])
        self.saved=False
        #Checks if any text is changed
        self.Bind(wx.EVT_TEXT,self.m3ufilechanged,self.txtm3ufilename)
        self.Bind(wx.EVT_TEXT,self.m3uurlchanged,self.textm3uURL)
        self.Bind(wx.EVT_TEXT,self.userchanged,self.txtuser)
        self.Bind(wx.EVT_TEXT,self.passwordchanged,self.txtpassword)
        self.Bind(wx.EVT_TEXT,self.serverchanged,self.txtserver)

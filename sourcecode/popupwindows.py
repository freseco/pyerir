import wx
import wx.adv #notification popup
import logging
import my_helper


class VentanaCanal(wx.Frame):
    
    def cerrarventana(self):
        self.timer.Start(500)
  
    def __init__(self, parent=None):
        style = ( wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.FRAME_SHAPED )
    
        height=130
        width=1650
        super(VentanaCanal, self).__init__(parent,style=style, size=(width,height),pos=(10,90))
        
        panel = wx.Panel(self,size=(width,height),style=wx.TRANSPARENT_WINDOW) 
        panel.SetBackgroundColour((0,0,0))
                
        self.lbl = wx.StaticText(panel,-1,style = wx.ALIGN_LEFT,size=(width,height),pos=(50,20))
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
            
    def mostrar(self, texto,logo=""):
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
				font = wx.Font(55, wx.ROMAN, wx.ITALIC, wx.BOLD) 
			else:
				lbl.SetBackgroundColour((0,0,0))
				font = wx.Font(50, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.NORMAL) 
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
  


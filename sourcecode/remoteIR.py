#Gets the IR code from the IR receiver

"""Can't connect to pigpio at localhost(8888)

Did you start the pigpio daemon? E.g. sudo pigpiod

Did you specify the correct Pi host/port in the environment
variables PIGPIO_ADDR/PIGPIO_PORT?
E.g. export PIGPIO_ADDR=soft, export PIGPIO_PORT=8888

Did you specify the correct Pi host/port in the
pigpio.pi() function? E.g. pigpio.pi('soft', 8888)"""


from piir.io import receive
from piir.decode import decode
import ast
import logging
import json
import os
from pathlib import Path


class remote:
    # GPIO of IR receiver
    pinr = 23

    #IR codes for default remote control buttons
    IRcodes={
    "ok"   : '00ff1ce3',
    "left" :'00ff08f7',
    "right":'00ffZa5',
    "up"   :'00ff18e7',
    "down" :'00ffRad',
    "one"  :'00ffEba',
    "two"  :'00ffFb9',
    "three":'00ffGb8',
    "four" :'00ffDbb',
    "five" :'00ff@bf',
    "six"  :'00ffCbc',
    "seven":'00ff07f8',
    "eight":'00ff15ea',
    "nine" :'00fftf6',
    "zero" :'00ff19e6',
    "asterisk":'00ff16e9',
    "hash" :'00ffrf2',
    "pwr":'',
    "info":'',
    "back":'',
    "mute":''}
    
    Salir=False
    
    def __init__(self):
        Salir=False
        logging.debug("debug remoteIR")
        # GPIO of IR receiver
        self.pinr = 23
        
        #Exist json with new IR codes?
        remoteIRfile=os.path.join(Path( __file__ ).parent.absolute(),"remoteIR.json")
        if os.path.isfile(remoteIRfile):
            with open(remoteIRfile) as json_file:
                data = json.load(json_file)
                #string to bytes? check this!
                self.IRcodes["ok"]      =data["ok"   ] 
                self.IRcodes["left"]    =data["left" ]
                self.IRcodes["right"]   =data["right"]
                self.IRcodes["up"]      =data["up"   ]
                self.IRcodes["down"]    =data["down" ]
                self.IRcodes["one"]     =data["one"  ]
                self.IRcodes["two"]     =data["two"  ]
                self.IRcodes["three"]   =data["three"]
                self.IRcodes["four"]    =data["four" ]
                self.IRcodes["five"]    =data["five" ]
                self.IRcodes["six"]     =data["six"  ]
                self.IRcodes["seven"]   =data["seven"]
                self.IRcodes["eight"]   =data["eight"]
                self.IRcodes["nine"]    =data["nine" ]
                self.IRcodes["zero"]    =data["zero" ]
                self.IRcodes["asterisk"]=data["asterisk"]
                self.IRcodes["hash"]     =data["hash"]
                self.IRcodes["pwr"]     =data["pwr"]
                self.IRcodes["info"]     =data["info"]
                self.IRcodes["back"]     =data["back"]
                self.IRcodes["mute"]     =data["mute"]

        
    
    def Getcode(self):                
        
        self.Salir=False
            
        while not self.Salir:
            logging.debug("Waiting for IR code!")            
            #Example of received data:
            # {'preamble': [16, 8], 'coding': 'ppm', 'zero': [1, 1], 'one': [1, 3], 'byte_separator': None, 'msb_first': False, 'bits': 32, 'data': b'\x00\xff\x1c\xe3', 'postamble': [1], 'timebase': 590, 'gap': 39000}
            data = str(decode(receive(self.pinr)))
            if data !='None':  
                self.Salir=True
                lista=ast.literal_eval(data)
                #returns string with ir code.      
                codigo=str(lista[0]['data']).replace("b'","").replace("\\","").replace("x","").replace("'","")
                return codigo
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

    #IR remote control buttons
    ok   = b'\x00\xff\x1c\xe3'
    left =b'\x00\xff\x08\xf7'
    right=b'\x00\xffZ\xa5'
    up   =b'\x00\xff\x18\xe7'
    down =b'\x00\xffR\xad'
    one  =b'\x00\xffE\xba'
    two  =b'\x00\xffF\xb9'
    three=b'\x00\xffG\xb8'
    four =b'\x00\xffD\xbb'
    five =b'\x00\xff@\xbf'
    six  =b'\x00\xffC\xbc'
    seven=b'\x00\xff\x07\xf8'
    eight=b'\x00\xff\x15\xea'
    nine =b'\x00\xff\t\xf6'
    zero =b'\x00\xff\x19\xe6'
    asterisk=b'\x00\xff\x16\xe9'
    #
    hash =b'\x00\xff\r\xf2'
    
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
                remote.ok      =data["ok"   ].replace("b'", "").replace("'","").encode() 
                remote.left    =data["left" ].replace("b'", "").replace("'","").encode()
                remote.right   =data["right"].replace("b'", "").replace("'","").encode()
                remote.up      =data["up"   ].replace("b'", "").replace("'","").encode()
                remote.down    =data["down" ].replace("b'", "").replace("'","").encode()
                remote.one     =data["one"  ].replace("b'", "").replace("'","").encode()
                remote.two     =data["two"  ].replace("b'", "").replace("'","").encode()
                remote.three   =data["three"].replace("b'", "").replace("'","").encode()
                remote.four    =data["four" ].replace("b'", "").replace("'","").encode()
                remote.five    =data["five" ].replace("b'", "").replace("'","").encode()
                remote.six     =data["six"  ].replace("b'", "").replace("'","").encode()
                remote.seven   =data["seven"].replace("b'", "").replace("'","").encode()
                remote.eight   =data["eight"].replace("b'", "").replace("'","").encode()
                remote.nine    =data["nine" ].replace("b'", "").replace("'","").encode()
                remote.zero    =data["zero" ].replace("b'", "").replace("'","").encode()
                remote.asterisk=data["asterisk"].replace("b'", "").replace("'","").encode()

        
    
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
                codigo=lista[0]['data']
                return codigo
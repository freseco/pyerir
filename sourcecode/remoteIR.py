#Obtiene el código captado por el sensor IR

from piir.io import receive
from piir.decode import decode
import ast

class remote:
    # GPIO of IR receiver
    pinr = 23

    #botones del mando
    ok= b'\x00\xff\x1c\xe3'
    left=b'\x00\xff\x08\xf7'
    right=b'\x00\xffZ\xa5'
    up=b'\x00\xff\x18\xe7'
    down=b'\x00\xffR\xad'
    one=b'\x00\xffE\xba'
    two=b'\x00\xffF\xb9'
    three=b'\x00\xffG\xb8'
    four=b'\x00\xffD\xbb'
    five=b'\x00\xff@\xbf'
    six=b'\x00\xffC\xbc'
    seven=b'\x00\xff\x07\xf8'
    eight=b'\x00\xff\x15\xea'
    nine=b'\x00\xff\t\xf6'
    zero=b'\x00\xff\x19\xe6'
    asterisk=b'\x00\xff\x16\xe9'
    #
    hash=b'\x00\xff\r\xf2'
    
    Salir=False
    
    def __init__(self, name):
        Salir=False
        
    
    def Getcode(self):   
        pinr=23
        self.Salir=False
            
        while not self.Salir:
            print("waiting for code")            
            #Ejemplo de dato recibido.
            # {'preamble': [16, 8], 'coding': 'ppm', 'zero': [1, 1], 'one': [1, 3], 'byte_separator': None, 'msb_first': False, 'bits': 32, 'data': b'\x00\xff\x1c\xe3', 'postamble': [1], 'timebase': 590, 'gap': 39000}
            data = str(decode(receive(pinr)))
            if data !='None':  
                self.Salir=True
                lista=ast.literal_eval(data)      
                codigo=lista[0]['data']
                return codigo
        print("fuera pidiendo code")
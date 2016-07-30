import sys
import time
import os
import datetime
from moduloinicio import *
from moduloeventos import *
from modulopromociones import *
from modulotours import *
from modhabit import *
menuprincipal()
while True:
    try:
        t=int(input("Ingrese la opcion que desee: "))
        break
    except ValueError:
        print("Ingrese un número porfavor.")
        
if t==1:
    menuinicio()
elif t==3:
    eventos()
elif t==4:
    tours()
elif t==5:
    promociones()
elif t==6:
    tipo()

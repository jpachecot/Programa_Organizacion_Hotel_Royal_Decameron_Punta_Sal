import sys
import time
import os
import datetime

def menu():
    line = "="*80
    print(line)
    print("\tPrograma de Organizacion de Hotel Royal Decameron Punta Sal")
    print(line)
    print("\t1 --> Inicio.")
    print("\t2 --> Reservaciones.")
    print("\t3 --> Eventos.")
    print("\t4 --> Tours.")
    print("\t5 --> Promociones.")
    print("\t6 --> Descripcion de Habitaciones.")
    print("\t7 --> Restaurantes.")
    
class cliente:
    def __init__(self,nombre,apellido_paterno,apellido_materno,dni):
        self.nombre = nombre
        self.apellido_materno = apellido_materno
        self.apellido_paterno = apellido_paterno
        self.dni = dni
menu()

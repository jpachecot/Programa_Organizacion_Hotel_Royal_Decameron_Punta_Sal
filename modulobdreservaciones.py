#MODULO RESERVACIONES - BASE DE DATOS

import os
import sys
import sqlite3
import moduloinicio

def menubdreservacion():
    os.system("cls")
    os.system("color e")
    print("\n\t\tMENU RESERVACIONES")
    print("\t\t******************")
    print("\t(1) Ver reservaciones")
    print("\t(2) Agregar reservaciones")
    print("\t(3) Modificar reservaciones")
    print("\t(4) Eliminar reservaciones")
    print("\t(5) Volver al menu principal")

    opbd = input("\tDigite una opcion del menu: ")

    if opbd == "1":
        consulta()
    elif opbd == "5":
        os.system ("cls")
        moduloinicio.menuprincipal()
    else:
        os.system("cls")
        input("\tDigite una opcion valida del menu")
        menubdreservacion()

def consulta():
    os.system("cls")

    con = sqlite3.connect("HOTEL.s3db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM reg_hotel")

    print("Reservaciones Registradas")
    print("=========================\n")
    
    for v in cursor:
        print("Reservacion: ", v[0])
        print("DNI: ", v[5])
        print("Nombres: ", v[1])
        print("Apellido Paterno: ", v[2])
        print("Apellido Materno: ", v[3])
        print("Ciudad de Origen: ", v[4])
        print("Tipo de Reservacion: ", v[11])
        print("Fecha: ", v[6], " al ", v[7])
        print("Tipo de Habitacion: ", v[8], " - " , v[9], " - ", v[10])
        print("\n------------------------------------------------------------\n")
        input("Presione 'Enter' para volver al menu...")
    con.close()

    

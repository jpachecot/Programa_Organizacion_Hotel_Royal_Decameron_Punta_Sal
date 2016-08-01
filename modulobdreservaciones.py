#MODULO RESERVACIONES - BASE DE DATOS

import os
import sys
import sqlite3
import moduloinicio
import moduloreservaciones

def nombre():
    letras = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while True:
        x = str(input("\tNOMBRE:"))
        verificacion = True
        for letra in x:
            if letra not in letras:
                print ("\tIngresa solo letras")
                verificación = False
                nombre()
                break
        if verificacion == True:
            return x

def appaterno():
    letras = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while True:
        x = str(input("\tAPELLIDO PATERNO:"))
        verificacion = True
        for letra in x:
            if letra not in letras:
                print ("\tIngresa solo letras")
                verificación = False
                appaterno()
                break
        if verificacion == True:
            return x

def apmaterno():
    letras = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while True:
        x = str(input("\tAPELLIDO MATERNO:"))
        verificacion = True
        for letra in x:
            if letra not in letras:
                print ("\tIngresa solo letras")
                verificación = False
                apmaterno()
                break
        if verificacion == True:
            return x

def corigen():
    letras = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while True:
        x = str(input("\tCIUDAD ORIGEN:"))
        verificacion = True
        for letra in x:
            if letra not in letras:
                print ("\tIngresa solo letras")
                verificación = False
                corigen()
                break
        if verificacion == True:
            return x


def vtexto(a):
    for t in a:
        if ((ord(t)<65 or ord(t)>90) and (ord(t)<97 or ord(t)>122) and ord(t)!=32):
            return False
        return True

def menubd():
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
    elif opbd == "2":
        agregar()
    elif opbd == "5":
        os.system ("cls")
        moduloinicio.menuprincipal()
    else:
        os.system("cls")
        input("\tDigite una opcion valida del menu")
        menubd()

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

    menubd()

def agregar():
    os.system("cls")

    print("\n\tAgregar Reservacion")
    print("\t===================\n")

    print("\tIngrese los datos que a continuacion se le piden POR FAVOR\n")

    #INGRESO DEL DNI
    while True:
        try:
            c=1
            while c!=8:
                ndni=int(input("\tDNI: "))
                c=len(str(ndni))
                if c!=8:
                    print("\tSolo se permite el ingreso de un DNI valido (8 numeros). Pruebe de nuevo POR FAVOR.")
            break
        except ValueError:
            print("\tSolo se permite el ingreso de valores numeros para su DNI. Pruebe de nuevo POR FAVOR.")
    ndni=str(ndni)

    #INGRESO DEL NOMBRE
    nom=nombre()

    #INGRESO DEL APELLIDO PATERNO
    appa=appaterno()

    #INGRESO DEL APELLIDO MATERNO
    apma=apmaterno()

    #INGRESO DE CIUDAD DE ORIGEN
    co=corigen()

    #INGRESO DEL TIPO DE RESERVACION
    print("\n\tTIPO DE RESERVACION")
    print("\t-------------------")
    print("\n\t(1) HOTEL")
    print("\t(2) HOTEL - AEREO")

    while True:
        try:
            tr=0
            while (tr!=1 and tr!=2):
                tr=int(input("¿Que tipo de reservacion desea hacer(1,2): "))
                if tr==1:
                    tres='HOTEL'
                elif tr==2:
                    tres='HOTEL - AEREO'
                else:
                    print("Ingrese un tipo reservacion valido")
            break
        except ValueError:
            print("Solo EXISTEN LOS TIPOS DE RESERVACION 1,2. Pruebe de nuevo POR FAVOR.")

    #INGRESO DE FECHA ENTRADA
    fen=input("\n\tFecha de entrada: ")

    #INGRESO DE FECHA SALIDA
    fsa=input("\n\tFecha de salida: ")

    #INGRESO DE TIPO DE HABITACION
    print("\tSELECCIONE EL TIPO DE HABITACIONES QUE DESEA PARA SU RESERVACION")
    moduloreservaciones.thab1()

    while True:
        try:
            th1a=0
            while (th1a!=1 and th1a!=2 and th1a!=3):
                th1a=int(input("\tCLASE DE HABITACION: "))
                if th1a==1:
                    th1='KIND A'
                    print("\tSELECCIONE EL TIPO DE HABITACION")
                    print("\t--------------------------------")
                    moduloreservaciones.thab211()
                    while True:
                        try:
                            th2a=0
                            while (th2a!=1 and th2a!=2):
                                th2a=int(input("\tTIPO DE HABITACION: "))
                                if th2a==1:
                                    th2='SENCILLA'
                                    th3=''
                                elif th2a==2:
                                    th2='DOBLE'
                                    th3=''
                                else:
                                    print("\tIngrese un tipo valido")
                            break
                        except ValueError:
                            print("\tSolo EXISTEN LOS TIPOS 1,2. Pruebe de nuevo POR FAVOR.")
                elif th1a==2:
                    th1='KIND B'
                    print("\tSELECCIONE EL TIPO DE HABITACION")
                    print("\t--------------------------------")
                    moduloreservaciones.thab212()
                    while True:
                        try:
                            th2a=0
                            while (th2a!=1 and th2a!=2 and th2a!=3 and th2a!=4):
                                th2a=int(input("\tTIPO DE HABITACION: "))
                                if th2a==1:
                                    th2='SENCILLA'
                                    th3=''
                                elif th2a==2:
                                    th2='DOBLE'
                                    th3=''
                                elif th2a==3:
                                    th2='TRIPLE'
                                    th3=''
                                elif th2a==4:
                                    th2='CUADRUPLE'
                                    th3=''
                                else:
                                    print("\tIngrese un tipo valido")
                            break
                        except ValueError:
                            print("\tSolo EXISTEN LOS TIPOS 1,2,3,4. Pruebe de nuevo POR FAVOR.")
                elif th1a==3:
                    th1='BUNGALOWS'
                    print("\tSELECCIONE LAS CLASES DE BUNGALOWS")
                    print("\t----------------------------------")
                    moduloreservaciones.thab213()
                    while True:
                        try:
                            th2a=0
                            while (th2a!=1 and th2a!=2):
                                th2a=int(input("\tCLASE DE BUNGALOWS: "))
                                if th2a==1:
                                    th2='KIND A'
                                    print("\tSELECCIONE EL TIPO DE HABITACION")
                                    print("\t--------------------------------")
                                    moduloreservaciones.thab2131()
                                    while True:
                                        try:
                                            th3a=0
                                            while (th3a!=1 and th3a!=2):
                                                th3a=int(input("\tTIPO DE HABITACION: "))
                                                if th3a==1:
                                                    th3='SENCILLA'
                                                elif th3a==2:
                                                    th3='DOBLE'
                                                else:
                                                    print("\tIngrese un tipo valido")
                                            break
                                        except ValueError:
                                            print("\tSolo EXISTEN LOS TIPOS 1,2. Pruebe de nuevo POR FAVOR.")
                                elif th2a==2:
                                    th2='KIND B'
                                    print("\tSELECCIONE EL TIPO DE HABITACION")
                                    print("\t--------------------------------")
                                    moduloreservaciones.thab2132()
                                    while True:
                                        try:
                                            th3a=0
                                            while (th3a!=1 and th3a!=2 and th3a!=3 and th3a!=4):
                                                th3a=int(input("\tTIPO DE HABITACION: "))
                                                if th3a==1:
                                                    th3='SENCILLA'
                                                elif th3a==2:
                                                    th3='DOBLE'
                                                elif th3a==3:
                                                    th3='TRIPLE'
                                                elif th3a==4:
                                                    th3='CUADRUPLE'
                                                else:
                                                    print("\tIngrese un tipo valido")
                                            break
                                        except ValueError:
                                            print("\tSolo EXISTEN LOS TIPOS 1,2,3,4. Pruebe de nuevo POR FAVOR.")
                                else:
                                    print("\tIngrese una clase valida")
                            break
                        except ValueError:
                            print("\tSolo EXISTEN LAS CLASES 1,2. Pruebe de nuevo POR FAVOR.")
                else:
                    print("\tIngrese una clase valida")
            break
        except ValueError:
            print("\tSolo EXISTEN LAS CLASES 1,2,3. Pruebe de nuevo POR FAVOR.")

    con = sqlite3.connect("HOTEL.s3db")
    cursor = con.cursor()

    cursor.execute("Insert into reg_hotel (nombre,appaterno,apmaterno,ciudadorigen,dni,fentrada,fsalida,thab1,thab2,thab3,treservacion) values ('"+nom+"','"+appa+"','"+apma+"','"+co+"','"+ndni+"','"+fen+"','"+fsa+"','"+th1+"','"+th2+"','"+th3+"','"+tres+"')")
    con.commit()
    con.close()
    os.system("cls")
    input("Reservacion registrada exitosamente!")
    menubd()
    

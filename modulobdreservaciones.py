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

def thabitacion():
    global th1, th2, th3
    
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
        os.system("clear")
        consulta()
    elif opbd == "2":
        os.system("clear")
        agregar()
    elif opbd == "3":
        modificar()
    elif opbd == "4":
        eliminar()
    elif opbd == "5":
        os.system ("cls")
        moduloinicio.menuprincipal()
    else:
        os.system("cls")
        input("\tDigite una opcion valida del menu")
        menubd()

#-----------------------------------CONSULTAR--------------------------------

def consulta():
    os.system("cls")

    con = sqlite3.connect("HOTEL.s3db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM reg_hotel")

    print("\tReservaciones Registradas")
    print("\t=========================\n")
    
    for v in cursor:
        print("\tReservacion: ", v[0])
        print("\tDNI: ", v[5])
        print("\tNombres: ", v[1])
        print("\tApellido Paterno: ", v[2])
        print("\tApellido Materno: ", v[3])
        print("\tCiudad de Origen: ", v[4])
        print("\tTipo de Reservacion: ", v[11])
        print("\tFecha: ", v[6], " al ", v[7])
        print("\tTipo de Habitacion: ", v[8], " - " , v[9], " - ", v[10])
        print("\n\t------------------------------------------------------------\n")
        input("\tPresione 'Enter' para volver al menu...")
    con.close()

    menubd()

#-----------------------------------AGREGAR--------------------------------

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
    thabitacion()

    con = sqlite3.connect("HOTEL.s3db")
    cursor = con.cursor()

    cursor.execute("Insert into reg_hotel (nombre,appaterno,apmaterno,ciudadorigen,dni,fentrada,fsalida,thab1,thab2,thab3,treservacion) values ('"+nom+"','"+appa+"','"+apma+"','"+co+"','"+ndni+"','"+fen+"','"+fsa+"','"+th1+"','"+th2+"','"+th3+"','"+tres+"')")
    con.commit()
    con.close()
    os.system("cls")
    input("Reservacion registrada exitosamente!")
    menubd()

#-----------------------------------MODIFICAR--------------------------------
    
def modificar():
    os.system("cls")

    con = sqlite3.connect("HOTEL.s3db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM reg_hotel")

    print("\tReservaciones Registradas")
    print("\t=========================\n")
    
    for v in cursor:
        print("\tReservacion: ", v[0])
        print("\tDNI: ", v[5])
        print("\tNombres: ", v[1])
        print("\tApellido Paterno: ", v[2])
        print("\tApellido Materno: ", v[3])
        print("\tCiudad de Origen: ", v[4])
        print("\tTipo de Reservacion: ", v[11])
        print("\tFecha: ", v[6], " al ", v[7])
        print("\tTipo de Habitacion: ", v[8], " - " , v[9], " - ", v[10])
        print("\n\t------------------------------------------------------------\n")

    codigo = input("\tDigite el codigo del campo que desea modificar: ")

    print("\n\tIngrese los datos en los siguientes campos para modificar: ")

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
    nom=nombre()
    appa=appaterno()
    apma=apmaterno()
    co=corigen()

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

    fen=input("\n\tFecha de entrada: ")
    fsa=input("\n\tFecha de salida: ")
    thabitacion()

    cursor.execute("update reg_hotel set nombre = '"+nom+"', appaterno = '"+appa+"', apmaterno = '"+apma+"', ciudadorigen = '"+co+"', dni = '"+ndni+"', fentrada = '"+fen+"', fsalida = '"+fsa+"', thab1 = '"+th1+"', thab2 = '"+th2+"', thab3 = '"+th3+"', treservacion = '"+tres+"' where ID = '"+codigo+"' ")
    con.commit()
    con.close()
    os.system("cls")
    input("Reservacion modificada")
    menubd()
    
#-----------------------------------ELIMINAR--------------------------------

def eliminar():
    os.system("cls")

    con = sqlite3.connect("HOTEL.s3db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM reg_hotel")

    print("\tReservaciones Registradas")
    print("\t=========================\n")
    
    for v in cursor:
        print("\tReservacion: ", v[0])
        print("\tDNI: ", v[5])
        print("\tNombres: ", v[1])
        print("\tApellido Paterno: ", v[2])
        print("\tApellido Materno: ", v[3])
        print("\tCiudad de Origen: ", v[4])
        print("\tTipo de Reservacion: ", v[11])
        print("\tFecha: ", v[6], " al ", v[7])
        print("\tTipo de Habitacion: ", v[8], " - " , v[9], " - ", v[10])
        print("\n\t------------------------------------------------------------\n")

    codigo = input("\tDigite el codigo del campo que desea eliminar: ")

    cursor.execute("delete from reg_hotel where ID = '"+codigo+"' ")

    con.commit()
    con.close()
    input("\tReservacion eliminada")

    menubd()
    

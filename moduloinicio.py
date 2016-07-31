
import sys
import os

from moduloeventos import *
from modulopromociones import *
from modulotours import *
from modhabit import *
from modulorestaurante import *
from modulobdreservaciones import *

def menuprincipal():
    print("\tPrograma de Organizacion de Hotel Royal Decameron Punta Sal")
    print("\t1 --> Inicio.")
    print("\t2 --> Reservaciones.")
    print("\t3 --> Eventos.")
    print("\t4 --> Tours.")
    print("\t5 --> Promociones.")
    print("\t6 --> Descripcion de Habitaciones.")
    print("\t7 --> Restaurantes.")

    t=input("\n\tIngrese la opcion que desee: ")

    if t=="1":
        menuinicio()
    if t=="2":
        menubdreservacion()
    elif t=="3":
        eventos()
    elif t=="4":
        tours()
    elif t=="5":
        promociones()
    elif t=="6":
        tipo()
    elif t=="7":
        restaurantes()
    else:
        print("Ingrese un valor correcto")
        menuprincipal()

def op():
    s1=input("Realmente deseas regresar al menú principal SI/NO: ")
    if s1=="Si" or s1=="SI" or s1=="si":
        menuprincipal()
    elif s1=="NO" or s1=="no" or s1=="No":
        tipo()
    else:
        print("Ingrese  SI/NO porfavor")
        op()

def ope():
    se=input("Realmente deseas regresar al menú principal SI/NO: ")
    if se=="Si" or se=="SI" or se=="si":
        menuprincipal()
    elif se=="NO" or se=="no" or se=="No":
        menuinicio()
    else:
        print("Ingrese  SI/NO porfavor")
        ope()

def ope2():
    se2=input("Realmente deseas salir SI/NO: ")
    if se2=="Si" or se2=="SI" or se2=="si":
        sys.exit(5)
    elif se2=="NO" or se2=="no" or se2=="No":
        menuinicio()
    else:
        print("Ingrese  SI/NO porfavor")
        ope2()

def ope3():
    s=input("Realmente deseas regresar al menú principal SI/NO: ")
    if s=="Si" or s=="SI" or s=="si":
        menuprincipal()
    elif s=="NO" or s=="no" or s=="No":
        restaurantes()
    else:
        print("Ingrese  SI/NO porfavor")
        ope3()

def ope4():
    ss=input("Realmente deseas salir SI/NO: ")
    if ss=="Si" or ss=="SI" or ss=="si":
        sys.exit(5)
    elif ss=="NO" or ss=="no" or ss=="No":
        restaurantes()
    else:
        print("Ingrese  SI/NO porfavor")
        ope4()

def op1():
    sss=input("Realmente deseas salir SI/NO: ")
    if sss=="Si" or sss=="SI" or sss=="si":
        sys.exit(5)
    elif sss=="NO" or sss=="no" or sss=="No":
        tipo()
    else:
        print("Ingrese  SI/NO porfavor")
        op1()
def operacion1():
    p=input("Deseas realizar otra  consulta SI/NO: ")
    if p=="Si" or p=="SI" or p=="si":
        menuprincipal()
    elif p=="NO" or p=="no" or p=="No":
        sys.exit(5)
    else:
        print("Ingrese  SI/NO porfavor")
        operacion1()

def operacion2():
    p1=input("Deseas realizar otra  consulta SI/NO: ")
    if p1=="Si" or p1=="SI" or p1=="si":
        menuinicio()
    elif p1=="NO" or p1=="no" or p1=="No":
        sys.exit(5)
    else:
        print("Ingrese  SI/NO porfavor")
        operacion2()

def operacion3():
    p3=input("Deseas realizar otra  consulta SI/NO: ")
    if p3=="Si" or p3=="SI" or p3=="si":
        eventos()
    elif p3=="NO" or p3=="no" or p3=="No":
        sys.exit(5)
    else:
        print("Ingrese  SI/NO porfavor")
        operacion3()

def operacion4():
    p4=input("Deseas realizar otra  consulta SI/NO: ")
    if p4=="Si" or p4=="SI" or p4=="si":
        restaurantes()
    elif p4=="NO" or p4=="no" or p4=="No":
        sys.exit(5)
    else:
        print("Ingrese  SI/NO porfavor")
        operacion4()

def menuinicio():
    print("1--->Ubicacion.")
    print("2--->Programa Todo Incluido.")
    print("3--->Descripcion de Habitaciones.")
    print("4--->Servicios.")
    print("5--->Salir al menu principal")
    print("6--->Salir del programa")
    print()

    x=input("Ingrese la opcion que desea observar: ")

    if x=="1":
        print()
        print("El Hotel Royal Decameron Punta Sal está ubicado en el kilómetro 1190 de la Carretera Panamericana Norte, cerca de la frontera sur de Ecuador, distrito de Zorritos, región de Tumbes, Perú. La ciudad de Tumbes se encuentra a 1 hora 30 minutos en avión de la ciudad de Lima y el hotel a su vez está ubicado a 1 hora 15 minutos del aeropuerto de Tumbes por tierra. El Hotel Royal Decameron Punta Sal Beach Resort, Spa & Convention Center cuenta con 1 kilómetro y medio de playa. La zona goza de sol durante todo el año. Sus aguas son cálidas, sobrepasando generalmente los 20ºC. También cuenta con una gran diversidad biológica por su ubicación en esta zona al extremo norte del Perú, en donde el agua de la corriente de Humboldt por lo general no tiene influencia directa, las condiciones microclimáticas que presenta durante todas las estaciones del año, de tipo tropical, con cielo despejado, sol radiante, temperaturas cálidas del aire y del mar")
        print()
        operacion2()

    elif x=="2":
        print()
        print("El Hotel cuenta con todas los servicios y las instalaciones que usted necesita: ")
        print()
        print("* Desayunos, almuerzos y cenas tipo buffet.")
        print("* Cenas a la carta.")
        print("* Snack y piqueos.")
        print("* Estacion de cevicheria durante el almuerzo.")
        print("* Bebidas alcoholicas nacionales e internacionales.")
        print("* Refrescos ilimitados.")
        print("* Deportes nauticos no motorizados.")
        print("* Piscina para adultos.")
        print("* Sillas y toallas para la palya y piscina.")
        print("* Gimnasio.")
        print("* Sala de Videojuegos.")
        print("* Dos canchas de tenis.")
        print("* Torneo de voley y futbol playa.")
        print("* Programacion de actividades diarias.")
        print("* Entretenimiento nocturno.")
        print("* Discoteca.")
        print("* Topico o Enfermeria.")
        print()
        operacion2()

    elif x=="3":
        print()
        print("Contamos con 313 habitaciones (42 habitaciones superior twin, 12 bungalows y 259 habitaciones estándar) que cuentan con: ")
        print()
        print("* Con una cama King Size o dos camas Twin Size.")
        print("* Sofa camam adicional.")
        print("* Aire acondicionado.")
        print("* Television por cable.")
        print("* Secador de cabello.")
        print("* Agua caliente.")
        print("* Telefono.")
        print("* Terraza o balcon.")
        print()
        operacion2()

    elif x=="4":
        print()
        print("---> Nuestro Hotel cuenta con 3 Restaurantes: ")
        print()
        print("* Buffet principal:            - RESTAURANTE BLUE MARLIN.")
        print("                                 Desayuno, almuerzo y cenas tematicas.")
        print()
        print("* Dos restaurantes a la carta: - RESTAURANTE LA CEVICHERIA.")
        print("                                 Especialidad: Comida peruana.")
        print("                               - RESTAURANTE OLIVA LIMON.")
        print("                                 Especialidad: Comida mediterranea.")
        print()
        print("* Snack:                       - RESTAURANTE BLUE MARLIN / RESTAURANTE OLIVA LIMON.")
            
        print()
        print("---> Nuestro hotel cuenta con 5 bares fijos: ")
        print()
        print("* Lobby Bar.")
        print("* Bar del Sol (piscina).")
        print("* Discoteca.")
        print("* Restaurante Oliva Limon.")
        print("* Restaurante La Cevicheria.")
        print("* Centro de convenciones.")
        print("* Restaurante Blue Marlin.")
        print()

        print("---> Otros servicion con cargo adicional.")
        print()
        print("* Salon de convenciones con capacidad para 500 personas.")
        print("* Decameron Explorer Tour Desk ofreciendo mas de 17 excursiones y circuitos a diferentes puntos de interes en Perú.")
        print("* Llamadas locales e internacionales.")
        print("* Boutique.")
        print("* Lavanderia.")
        print("* Wi-fi.")
        print("* SPA.")
        print("* Asistencia medica.")
        print("* Cajilla de seguridad.")
        operacion2()

    elif x=="5":
        ope()

    elif x=="6":
        ope2()

    else:
        print("Ingrese un valor correcto porfavor")
        menuinicio()



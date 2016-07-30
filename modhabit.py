#Tipos de habitacion

def tipo():
    print("1. Habitacion Estandar (Tipo A).")
    print("2. Habitacion Estandar Superior (Tipo B).")
    print("3. Bungalows.")
    x=int(input("Seleccione el tipo de habitacion: "))
    if x==1:
        print()
        print("-Estandar Sencilla (1 persona): 1 cama tamaño king size.")
        print("-Estandar Doble (2 personas): 1 cama tamaño king size \n1 cama de una plaza.")
        print("-Estandar Tripe (3 personas): 1 cama tamaño king size \n1 cama de una plaza.")
        print("-Estandar Cuadruple (4 personas): NO APLICA.")

    if x==2:
        print()
        print("-Estandar Superior Sencilla (1 persona): 1 cama twin size.")
        print("-Estandar Superior Doble (2 personas): 2 camas twin size.")
        print("-Estandar Superior Triple (3 personas): 2 camas twin size. \n1 cama de una plaza.")
        print("-Estandar Superior Cuadruple (3 dultos 1 niño): 2 camas twin size. \n1 cama de 1 plaza.")

    if x==3:
        print()
        print("-Bungalow Tipo A Sencillo (1 persona): 1 cama king size.")
        print("-Bungalow Tipo A Doble (2 personas): 1 cama king size.")
        print("-Bungalow Tipo A Triple (3 personas): NO APLICA.")
        print("-Bungalow Tipo A cuadruple (4 personas): NO APLICA.")

        
        print()
        print("-Bungalow Tipo B Sencillo (1 persona): 1 cama twin size.")
        print("-Bungalow Tipo B Doble (2 adultos y 2 niños): 2 camas twin size.")
        print("-Bungalow Tipo B Triple: NO APLICA.")
        print("-Bungalow Tipo B Cuadruple: NO APLICA.")



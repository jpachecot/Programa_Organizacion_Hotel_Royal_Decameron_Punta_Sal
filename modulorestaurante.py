
import sys
import moduloinicio

def operacion():
    pe=input("Deseas realizar otra  consulta SI/NO: ")
    if pe=="Si" or pe=="SI" or pe=="si":
        restaurantes()
    elif pe=="NO" or pe=="no" or pe=="No":
        sys.exit(5)
    else:
        print("Ingrese  SI/NO porfavor")
        operacion()

def restaurantes():
    print("\t\t RESTAURANTES.")
    print("\t1.----> Restaurante Blue Marlin.")
    print("\t2.---->Restaurante La Cevicheria.")
    print("\t3.---->Restaurante Oliva Limon.")
    print("\t4.---->Salir al Menu Principal.")
    print("\t5.---->Salir")
    r=input("Escoja el restaurante del que desea ver la carta: ")
    if r=="1":
        print("\t Restaurante Blue Marlin.")
        print("1--->Desayuno.")
        print("2--->Almuerzo.")
        print("3--->Cena.")
        print("4--->Salir al menu Restaurantes")
        print("5--->Salir")
        b=input("Escoga la opcion que desea ver: ")
        if (b=="1"):
            print("\t Desayuno.")
            print("*Cafe con eche - tostada integral con aceite de oliva y tomate - zumo de naranja")
            print("*Cereales con leche - zumo de naranja - platano")
            print("*Cafe con leche - Tostada de queso fresco con miel uvas")
            operacion()
        elif (b=="2"):
            print("\t Almuerzo.")
            print("Macarrones con tomate y carne picada. Ensalada de lechuga y tomate. Pan. Fruta.")
            print("Gazpacho. Tortilla de patata. Pan. Lácteo.")
            print("Crema de calabacín (con patatas y quesitos). Pechuga de pollo al horno con salsa de zumo de limón. Pan. Fruta.")
            operacion()
        elif b=="3":
            print("\t Cena.")
            print("Crema de zanahoria + lenguado con patata cocida + mandarina")
            print("Lasaña de calabacín con pavo + puré de patata + pera")
            print("Crema de verduras + pechuga de pollo + manzana")
            print("Crema de lechuga + croquetas de pescado con puré de patata + plátano")
            operacion()
        elif b=="4":
            restaurantes()
        elif b=="5":
            moduloinicio.ope4()
            
    elif r=="2":
        print("\t\t Restaurante La Cevicheria.")
        print("\tEspecialidad comida peruana")
        print("Chupe de camarones.")
        print("Seco de cabrito con frejoles")
        print("Tallarines rojos con carnen/pollo")
        moduloinicio.operacion4()

    elif r=="3":
        print("\t Restaurante Oliva Limon.")
        print("Paella de bogavante")
        print("Tagliatelle Genovesa al pesto")
        print("Pollo en escabeche")
        moduloinicio.operacion4()

    elif r=="4":
        moduloinicio.ope3()

    elif r=="5":
        moduloinicio.ope4()

    else:
        print("Ingrese una opcion correcta.")
        restaurantes()
        
        
        


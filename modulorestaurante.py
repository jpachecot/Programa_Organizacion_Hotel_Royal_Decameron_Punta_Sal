def restaurantes():
    print("\t\t RESTAURANTES.")
    print("\t1. Restaurante Blue Marlin.")
    print("\t2. Restaurante La Cevicheria.")
    print("\t3. Restaurante Oliva Limon.")
    r=int(input("Escoja el restaurante del que desea ver la carta: "))
    if r==1:
        print("\t Restaurante Blue Marlin.")
        print("1. Desayuno.")
        print("2. Almuerzo.")
        print("3. Cena.")
        b=int(input("Escoga la opcion que desea ver: "))
        if (b==1):
            print("\t Desayuno.")
            print("*Cafe con eche - tostada integral con aceite de oliva y tomate - zumo de naranja")
            print("*Cereales con leche - zumo de naranja - platano")
            print("*Cafe con leche - Tostada de queso fresco con miel uvas")
        if (b==2):
            print("\t Almuerzo.")
            print("Macarrones con tomate y carne picada. Ensalada de lechuga y tomate. Pan. Fruta.")
            print("Gazpacho. Tortilla de patata. Pan. Lácteo.")
            print("Crema de calabacín (con patatas y quesitos). Pechuga de pollo al horno con salsa de zumo de limón. Pan. Fruta.")
        if b==3:
            print("\t Cena.")
            print("Crema de zanahoria + lenguado con patata cocida + mandarina")
            print("Lasaña de calabacín con pavo + puré de patata + pera")
            print("Crema de verduras + pechuga de pollo + manzana")
            print("Crema de lechuga + croquetas de pescado con puré de patata + plátano")
        
    if r==2:
        print("\t\t Restaurante La Cevicheria.")
        print("\tEspecialidad comida peruana")
        print("Chupe de camarones.")
        print("Seco de cabrito con frejoles")
        print("Tallarines rojos con carnen/pollo")
        
    if r==3:
        print("\t Restaurante Oliva Limon.")
        print("Paella de bogavante")
        print("Tagliatelle Genovesa al pesto")
        print("Pollo en escabeche")
restaurantes()

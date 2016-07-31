import sys
import moduloinicio 

def eventos():
    print("1--->Convenciones y Eventos.")
    print("2--->Bodas.")
    print("3--->Grupos.")
    print("4--->Regresar al Menu Principal")
    print("5--->Salir del programa")
    print()

    e=input("Ingrese la opcion que desea observar.")

    if e=="1":
        print()
        print("CONVENCIONES Y EVENTOS.")
        print()
        print("Hoteles Decameron ofrece sus planes bajo diferentes modalidades para eventos y convenciones corporativas.")
        print("Nuestros Hoteles cuentan con habitaciones cómodamente dotadas y ofrecemos servicios adicionales de spa, restaurantes, bar abierto, piscina y actividades turísticas.")
        print("Disponemos de modernos Centros de Convenciones, dotados con todas las comodidades y tecnología de la hotelería moderna, constituyéndose por sus características e infraestructura en la mejor alternativa para la realización de los eventos que tu empresa requiere como: ")
        print()
        print("* Convenciones.")
        print("* Reuniones de ventas.")
        print("* Capacitaciones.")
        print("* Conferencias.")
        print("* Lanzamiento de productos.")
        print("* Seminarios y viajes de incentivos entre otros.")
        print()
        print("Contamos con un equipo humano altamente comprometido, garantizandole: ")
        print()
        print("* Coordinador permanente del evento.")
        print("* Coctel de bienvenida.")
        print("* Salones dotados con aire acondicionado central y equipos audiovisuales basicos.")
        print("* Montaje de acuerdo a las necesidades del grupo.")
        print("* Dos coffee breacks diarios por noche de alojamiento.")
        print("* Seminarios y viajes de incentivos entre otros.")
        print("* Adicionalmente fiestas tema y talleres vivenciales.")
        print("Por estas y muchas más razones esperamos tener la oportunidad de demostrarle porque somos la PRIMERA Y MEJOR opción.")
        print()
        moduloinicio.operacion3()

    elif e=="2":
        print()
        print("BODAS")
        print()
        print("Hoteles Decameron te ofrece la oportunidad de celebrar el matrimonio de tus sueños. Te invitamos a visitarnos y conocer el completo despliegue de servicios para bodas, que incluye un servicio de banquetería de la más alta calidad, decoración del lugar, coordinador de bodas y muchas cosas más. Celebra el día más importante de tu vida sin ninguna preocupación.")
        print("Nuestros planes de bendición de argollas, y diferentes ceremonias, están diseñados para que los novios vivan la importancia y la emoción del matrimonio.")
        print("Disfruta el TODO INCLUIDO de Hoteles Decameron y haz que tu matrimonio sea inolvidable para ti y tus invitados.")
        print()
        moduloinicio.operacion3()

    elif e=="3":
        print()
        print("GRUPOS")
        print()
        print("Hoteles Decameron tiene la mejor infraestructura para que pases unas vacaciones inolvidables, acompañado de tus amigos o familiares. Con más de 35 hoteles y según el destino que escojas, tendrás la oportunidad de disfrutar de una gran variedad de restaurantes, piscinas, bares, shows y muchas cosas más.")
        print("Además, realiza diferentes excursiones y recorridos que solo te ofrece Decameron Explorer, quien coordina todo para que no tengas que preocuparte por nada. Tenemos a tu disposición todos nuestros recursos para hacer que tu evento sea algo único e inolvidable, al mejor estilo Decameron con TODO INCLUIDO.")
        print()
        moduloinicio.operacion3()

    elif e=="4":
        moduloinicio.ope()

    elif e=="5":
        moduloinicio.ope2()

    else:
        print("Ingrese un valor valido")
        eventos()
    




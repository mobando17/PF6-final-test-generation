import os
import requests


def obtener_platos():

    respuesta = requests.get(
        "https://api-colombia.com/api/v1/TypicalDish"
    )

    return respuesta.json()


# Función obligatoria
def dish_fetch(num):

    platos = obtener_platos()

    for plato in platos:

        if plato["id"] == num:

            return {

                "id": plato["id"],

                "name": plato["name"],

                "description": plato["description"]
            }

    return {

        "id": -1,

        "name": "Plato no encontrado"
    }


def limpiar_pantalla():

    os.system("cls")


def mostrar_titulo():

    print("=" * 60)
    print("      MENÚ INTERACTIVO DE COMIDA COLOMBIANA")
    print("=" * 60)


def mostrar_menu():

    platos = obtener_platos()

    mostrar_titulo()

    for plato in platos[:15]:

        print(f"[{plato['id']}] {plato['name']}")

    print("[0] Salir")


def mostrar_ascii(nombre_plato):

    if "Bandeja" in nombre_plato:

        print(r"""
        _______________________
       /                       \
      |   FRIJOLES  ARROZ      |
      |   CHORIZO  HUEVO       |
      |   AGUACATE  CARNE      |
       \_______________________/
        """)

    elif "Ajiaco" in nombre_plato:

        print(r"""
             (  )
              )(
           .------.
          /        \
         | AJIACO  |
          \        /
           '------'
        """)

    elif "Lechona" in nombre_plato:

        print(r"""
          __________________
         /                  \
        |     LECHONA       |
        |   arroz y carne   |
         \__________________/
        """)

    elif "Arepa" in nombre_plato:

        print(r"""
            _____________
          /               \
         |     AREPA       |
          \_______________/
        """)

    elif "Empanada" in nombre_plato:

        print(r"""
             __________
            /          \
           / EMPANADA   \
           \            /
            \__________/
        """)

    else:

        print(r"""
            __________________
           |                  |
           |   PLATO TIPICO   |
           |__________________|
        """)


def mostrar_detalles(plato):

    limpiar_pantalla()

    print("=" * 50)
    print("         INFORMACIÓN DEL PLATO")
    print("=" * 50)

    print(f"\nID: {plato['id']}")
    print(f"Nombre: {plato['name']}")

    mostrar_ascii(plato["name"])

    if "description" in plato:

        print("\nDescripción:")
        print(plato["description"])

    print("\n" + "=" * 50)

    input("\nPresione ENTER para volver al menú...")


def main():

    while True:

        limpiar_pantalla()

        mostrar_menu()

        opcion = input(
            "\nSeleccione el número de un plato: "
        )

        if not opcion.isdigit():

            print("\nPor favor ingrese solo números.")
            input("\nPresione ENTER para continuar...")
            continue

        opcion = int(opcion)

        if opcion == 0:

            print("\nPrograma finalizado.")
            break

        plato = dish_fetch(opcion)

        if plato["id"] == -1:

            print("\nPlato no encontrado.")
            input("\nPresione ENTER para continuar...")

        else:

            mostrar_detalles(plato)


if __name__ == "__main__":

    main()
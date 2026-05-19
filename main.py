import requests


def obtener_platos():

    respuesta = requests.get(
        "https://api-colombia.com/api/v1/TypicalDish"
    )

    return respuesta.json()

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


def mostrar_menu():

    platos = obtener_platos()

    print("\n" + "=" * 55)
    print("        MENÚ DE PLATOS TÍPICOS COLOMBIANOS")
    print("=" * 55)

    for plato in platos[:15]:

        print(f"[{plato['id']}] {plato['name']}")

    print("[0] Salir")


def mostrar_informacion_plato(plato):

    print("\n" + "-" * 45)
    print("         INFORMACIÓN DEL PLATO")
    print("-" * 45)

    print(f"ID          : {plato['id']}")
    print(f"Nombre      : {plato['name']}")

    if "description" in plato:

        print("\nDescripción:")
        print(plato["description"])


def main():

    while True:

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

            print("\nCerrando programa...")
            break

        plato_seleccionado = dish_fetch(opcion)

        if plato_seleccionado["id"] == -1:

            print("\nPlato no encontrado.")

        else:

            mostrar_informacion_plato(plato_seleccionado)

        input("\nPresione ENTER para volver al menú...")


if __name__ == "__main__":

    main()
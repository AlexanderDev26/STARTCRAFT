from Jugador import Jugador
from Partida import Partida  # Asegúrate de importar la clase Partida

def mostrar_menu():
    jugador = Jugador()
    partida = Partida()  # Crear una instancia de la clase Partida
    
    while True:
        print("\n=== STARCRAFT MANAGEMENT SYSTEM ===")
        print("1. Crear Perfil de Jugador")
        print("2. Listar Perfiles de Jugadores")
        print("3. Actualizar Perfil de Jugador")
        print("4. Eliminar Perfil de Jugador")
        print("5. Crear Partida")
        print("6. Listar Partidas")
        print("7. Actualizar Partida")
        print("8. Eliminar Partida")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugador.crear()  # Llama al método `crear` de la clase `Jugador`
        elif opcion == "2":
            jugador.listar()  # Llama al método `listar` de la clase `Jugador`
        elif opcion == "3":
            jugador.actualizar()  # Llama al método `actualizar` de la clase `Jugador`
        elif opcion == "4":
            jugador.eliminar()  # Llama al método `eliminar` de la clase `Jugador`
        elif opcion == "5":
            partida.crear()  # Llama al método `crear` de la clase `Partida`
        elif opcion == "6":
            partida.listar()  # Llama al método `listar` de la clase `Partida`
        elif opcion == "7":
            partida.actualizar()  # Llama al método `actualizar` de la clase `Partida`
        elif opcion == "8":
            partida.eliminar()  # Llama al método `eliminar` de la clase `Partida`
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

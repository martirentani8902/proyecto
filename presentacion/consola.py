from servidores.modelos import Servidor
from servidores import excepciones

def agregar_servidores(admin):
    print("CARGA DE DATOS DE SERVIDORES:\n\n")
    while True:
        nombre = input("Ingrese el nombre del servidor: ")
        cpu = input("Ingrese la cantidad de CPUs del servidor: ")
        estado = input("Ingrese el estado del servidor (activo o inactivo): ")
        try:
            servidor = Servidor(nombre, cpu, estado)
        except ValueError as error:
            print("Error de creacion del servidor:", error)
            break
        except TypeError as error:
            print("Error de creacion del servidor:", error)
            break
        else:
            try:
                admin.agregar_servidor(servidor)
            except excepciones.ServidorYaEstaEnLista as error:
                print("Error al agregar:", error)
                break
            else:
                print("Servidor", nombre, "agregado al inventario.")
                while True:
                    opcion = input("\nDesea cargar otro servidor?\n1) Si\n2) No\n")
                    try:
                        opcion = int(opcion)
                    except ValueError:
                        print("Opcion invalida.")
                    else:
                        if opcion == 1 or opcion == 2:
                            break
                        else:
                            print("Opcion invalida.")
                if opcion == 1:
                    continue
                else:
                    break


def imprimir_inventario(admin):
    while True:
        print("MOSTRANDO INVENTARIO DE SERVIDORES\n\n")
        admin.mostrar_inventario()
        print("\n\nFIN DE INVENTARIO")
        while True:
            opcion = input("Desea ver el inventario de nuevo?\n1) Si\n2) No\n")
            try:
                opcion = int(opcion)
            except ValueError:
                print("Opcion invalida.")
                continue
            else:
                if opcion == 1 or opcion == 2:
                    break
                else:
                    print("Opcion invalida.")
                    continue
        if opcion == 1:
            continue
        else:
            break


def eliminar_servidor(admin):
    print("ELIMINACION DE SERVIDORES\n")
    while True:
        nombre = input("Ingrese el nombre del servidor que quiere eliminar: ")
        try:
            admin.eliminar_servidor(nombre)
        except ValueError as error:
            print("Error:",error)
            break
        except TypeError as error:
            print("Error:",error)
            break
        except excepciones.NombreVacio as error:
            print("Error:",error)
            break
        except excepciones.ServidorNoEncontrado as error:
            print("Error:",error)
            break
        else:
            print("Servidor eliminado correctamente\n")
            while True:
                opcion = input("Desea eliminar otro?\n1) Si\n2) No\n")
                try:
                    opcion = int(opcion)
                except ValueError:
                    print("Ingrese una opcion valida.")
                    continue
                else:
                    if opcion == 1 or opcion == 2:
                        break
                    else:
                        print("Ingrese una opcion valida.")
                        continue
        if opcion == 1:
            continue
        else:
            break

                
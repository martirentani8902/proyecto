from servidores.modelos import Servidor
from servidores.administrador import administrador
from servidores import metricas, excepciones, operaciones
from main.casos import imprimir_inventario, agregar_servidores, eliminar_servidor

print("Comienzo del programa")
print()

admin = administrador([])

while True:
    try:
        opcion = int(input("Seleccione una opcion:\n1) Ver inventario \n2) Agregar servidor\n3) Eliminar servidor\n4) Salir del programa\n"))
    except ValueError:
        print()
        print("Ingrese una opcion valida")
        print()
    else:
        if opcion in range (1,5): 
            match opcion:
                case 1:
                    imprimir_inventario(admin)
                case 2:
                    agregar_servidores(admin)
                case 3:
                    eliminar_servidor(admin)
                case 4:
                    break
        else:
            print("\nOpcion invalida\n")
print("\nFin del programa.")








        



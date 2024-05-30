import scripts.gastos_por_cliente as gastos_por_cliente
import scripts.productos_por_cliente as productos_por_cliente
import scripts.segmentar_clientes as segmentar_clientes

def main():
    while True:
        print("\n--- Menú ---\n")
        print("1. Ver clientes nuevos y antiguos")
        print("2. Ver productos más comprados por cliente")
        print("3. Ver gastos totales por cliente")
        print("4. Salir")
        option = input("Ingrese una opción: ")

        if option == "1":
            segmentar_clientes.main()
        elif option == "2":
            productos_por_cliente.main()
        elif option == "3":
            gastos_por_cliente.main()
        elif option == "4":
            print("\n--- Fin del programa ---\n")
            break
        else:
            print("\nOpción no válida")

if __name__ == "__main__":
    main()

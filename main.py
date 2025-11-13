# Este main.py funciona como menú para ejecutar de manera más sencilla cada uno de los metodos

#Vamos a importar la carpeta methods/ para realizar el trabajo de los distintos metodos

from methods import slicing, loop, recursion, stack

def mostrar_menu():
    print("\n===  Inversor de Palabras en Python ===")
    print("\n\n===  Bienvenido a este repositorio dónde exploraremos cada metodo para este ejercicio en concreto, su eficiencia y las recomendaciones para ocuparlo  ===")
    print("\n\nA continuación, selecciona un método para invertir la palabra:")
    print("1. Usando slicing [::-1]")
    print("2. Usando bucle for")
    print("3. Usando recursión")
    print("4. Usando pila (stack)")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nIngrese el número del método: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if opcion == 5:
            print("Saliendo...")
            break

        if opcion not in [1, 2, 3, 4]:
            print("Opción no válida. Por favor, intenta de nuevo.")
            continue

        palabra = input("Ingresa la palabra a invertir: ")

        if opcion == 1:
            _ = slicing.invertir_slicing(palabra)
        elif opcion == 2:
            _ = loop.invertir_loop(palabra)
        elif opcion == 3:
            _ = recursion.invertir_recursion(palabra)
        elif opcion == 4:
            _ = stack.invertir_stack(palabra)

if __name__ == "__main__":
    main()

import os

def invertir_stack(palabra: str) -> str:
    print("\n[Método] Pila (Stack)")
    input("\nEntendiendo el código:\n"
          "Se transforma la palabra en una lista (pila), y se extraen los elementos con pop(), "
          "de modo que el último en entrar es el primero en salir (LIFO).\n\nPresiona Enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")

    pila = list(palabra)
    resultado = ""
    while pila:
        resultado += pila.pop()

    print("Ejecución realizada:\n")
    print(f"Palabra original: {palabra}")
    print(f"Resultado invertido: {resultado}")
    print(f"Complejidad temporal: O(n)")
    print(f"Complejidad espacial: O(n)")
    input("\n\nPresiona Enter para ver la recomendación...")
    os.system("cls" if os.name == "nt" else "clear")

    print("Recomendación final:")
    print("El método de pila es ideal para ilustrar estructuras de datos LIFO o simular un comportamiento tipo stack.\n"
          "Tiene buena eficiencia, aunque no es tan corto como slicing.")
    input("\n\nPresiona Enter para volver al menú...")
    os.system("cls" if os.name == 'nt' else 'clear')

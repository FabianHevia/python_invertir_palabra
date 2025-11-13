import os

def invertir_loop(palabra: str) -> str:
    print("\n[Método] Bucle (for)")
    input("\nEntendiendo el código:\n"
          "El bucle recorre cada carácter y lo antepone a una nueva cadena para construir la palabra invertida.\n"
          "Esto implica múltiples concatenaciones sucesivas en memoria.\n\nPresiona Enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")

    resultado = ""
    for letra in palabra:
        resultado = letra + resultado

    print("Ejecución realizada:\n")
    print(f"Palabra original: {palabra}")
    print(f"Resultado invertido: {resultado}")
    print(f"Complejidad temporal: O(n²) (por concatenaciones sucesivas)")
    print(f"Complejidad espacial: O(n)")
    input("\n\nPresiona Enter para ver la recomendación...")
    os.system("cls" if os.name == "nt" else "clear")

    print("Recomendación final:")
    print("Usa el bucle for cuando quieras entender o enseñar el proceso paso a paso.\n"
          "Aunque es más claro, puede ser menos eficiente que slicing en cadenas grandes.")
    input("\n\nPresiona Enter para volver al menú...")
    os.system("cls" if os.name == 'nt' else 'clear')

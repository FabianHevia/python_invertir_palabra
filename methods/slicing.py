import os

def invertir_slicing(palabra: str) -> str:
    print("\n[Método] Slicing")
    input("\nEntendiendo el código:\n"
          "Slicing usa la sintaxis palabra[::-1] para crear una vista invertida de la cadena.\n"
          "Python realiza esto internamente copiando los caracteres desde el final hasta el inicio.\n\nPresiona Enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")

    resultado = palabra[::-1]
    print("Ejecución realizada:\n")
    print(f"Palabra original: {palabra}")
    print(f"Resultado invertido: {resultado}")
    print(f"Complejidad temporal: O(n)")
    print(f"Complejidad espacial: O(n)")
    input("\n\nPresiona Enter para ver la recomendación...")
    os.system("cls" if os.name == "nt" else "clear")

    print("Recomendación final:")
    print("Usa slicing cuando quieras una solución compacta, legible y rápida para la mayoría de casos. "
          "Es ideal para scripts y cuando no necesitas mostrar pasos intermedios.")
    input("\n\nPresiona Enter para volver al menú...")
    os.system("cls" if os.name == "nt" else "clear")

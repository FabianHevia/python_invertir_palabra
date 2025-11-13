import os

def invertir_recursion(palabra: str) -> str:
    print("\n[Método] Recursión")
    input("\nEntendiendo el código:\n"
          "La recursión divide el problema: toma el último carácter y concatena el resultado de invertir el resto.\n"
          "Tiene un caso base cuando la palabra está vacía o tiene un solo carácter.\n\nPresiona Enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")

    def _rec(p):
        if len(p) <= 1:
            return p
        return p[-1] + _rec(p[:-1])

    resultado = _rec(palabra)
    print("Ejecución realizada:\n")
    print(f"Palabra original: {palabra}")
    print(f"Resultado invertido: {resultado}")
    print(f"Complejidad temporal: O(n)")
    print(f"Complejidad espacial: O(n) (por el stack de llamadas)")
    input("\n\nPresiona Enter para ver la recomendación...")
    os.system("cls" if os.name == "nt" else "clear")

    print("Recomendación final:")
    print("La recursión es ideal para demostrar conceptos de descomposición de problemas.\n"
          "Evita usarla en cadenas muy largas por límites del stack de Python.")
    input("\n\nPresiona Enter para volver al menú...")
    os.system("cls" if os.name == 'nt' else 'clear')

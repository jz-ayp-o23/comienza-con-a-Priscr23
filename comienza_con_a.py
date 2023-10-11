"""
Diseña un programa para determinar si una palabra dada comienza con la letra "A". Toma en cuenta que puede estar en mayúscula o minúscula, con o sin acento, etc.
750722
"""
#Entradas
palabra = input("Escribe una palabra: ")

#Procesos
if palabra.startswith("A") or palabra.startswith("Á") or palabra.startswith("a") or palabra.startswith("á"):
    print(f"'{palabra}' comienza con 'A'")
else:
    print(f"'{palabra}' no comienza con 'A'")

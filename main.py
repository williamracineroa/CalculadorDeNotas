"""nt("aqui veras el promedio de tus notas")
nota1=float(input("ingrese su primera nota:"))
nota2=float(input("ingrse su segunda nota:"))
nota3=float(input("ingrese su tercera nota:"))



promedio=float(nota1+nota2+nota3)/3
print("tu promedio de notas es:",promedio)"""

# Programa para calcular el promedio de varias notas

cantidad = int(input("¿Cuántas notas deseas ingresar? "))
suma = 0

for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    suma += nota

promedio = suma / cantidad

print("El promedio es:", promedio)
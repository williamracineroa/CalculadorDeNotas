# 📊 Calculadora de Promedio en Python

Programa en Python que calcula el promedio de varias notas ingresadas por el usuario desde la terminal.

---

## 🚀 Descripción

Este programa permite:

- Ingresar la cantidad de notas
- Capturar cada nota individualmente
- Calcular el promedio automáticamente
- Mostrar el resultado en pantalla

Es ideal para practicar conceptos básicos de Python como:

- Variables
- Bucles `for`
- Entrada de datos con `input()`
- Conversión de tipos (`int`, `float`)
- Operaciones matemáticas

---

## 🧠 Código Fuente

```python
# Programa para calcular el promedio de varias notas

cantidad = int(input("¿Cuántas notas deseas ingresar? "))
suma = 0

for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    suma += nota

promedio = suma / cantidad

print("El promedio es:", promedio)
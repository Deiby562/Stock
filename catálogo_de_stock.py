# -*- coding: utf-8 -*-
"""Catálogo de Stock.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZydAtWG-CEWQ1sGOgK76yWYAw5q-UR_X
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk


#Definimos la clase Producto y sus atributos
class Producto:
    def __init__(self, codigo, categoria,  nombre,  cantidad, precio):
        self.codigo = str(codigo)
        self.categoria = categoria
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return (f"Código: {self.codigo}\n"
                f"Nombre: {self.nombre}\n"
                f"Categoría: {self.categoria}\n"
                f"Cantidad: {self.cantidad} unidades\n"
                f"Precio: ${self.precio}")

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para búsqueda rápida por código

    def agregar_producto(self, producto):
        self.productos[producto.codigo] = producto

    def buscar_producto(self, codigo):
        return self.productos.get(codigo, "Producto no encontrado")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            return "Producto eliminado"
        return "Producto no encontrado"

    def listar_productos(self):
        for p in self.productos.values():
            print(f"{p.codigo}: {p.nombre} ({p.categoria}) - {p.cantidad} unidades, ${p.precio}")

# Ejemplo de uso
inventario = Inventario()
inventario.agregar_producto(Producto("1001", "Hombre", "Camiseta",  50, 49.900))
inventario.agregar_producto(Producto("1002", "Niños", "Pantalón",  30, 29.900))
inventario.agregar_producto(Producto("1003", "Mujer", "Jean", 15, 29.900))
inventario.agregar_producto(Producto("1004", "Niñas", "Camisa", 20, 19.900))
#inventario.listar_productos()

# Solicitar entrada
codigo_ingresado = input("Ingrese el código del producto que desea buscar: ")

# Buscar producto en el inventario
producto = inventario.buscar_producto(str(codigo_ingresado))

# Mostrar resultados
if isinstance(producto, Producto):
    print("\nProducto encontrado:")
    print(producto)
else:
    print("Producto no encontrado")
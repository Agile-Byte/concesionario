#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""MAIN"""

import sys
import traceback

from src.proyecto.coche import Coche
from src.proyecto.cliente import Cliente
from src.proyecto.comun import generar_oferta
from src.proyecto.mozo import Mozo
from src.proyecto.robot import Robot

if __name__ == '__main__':
    try:
        # Se agrega un nuevo cliente
        cliente1 = Cliente('Juan', 'Costa', '14888652L', 55000)
        cliente1.añadir_cliente()
        # Se agrega un nuevo coche
        coche1 = Coche('Toyota', 'Rav4', 5, 45000)
        coche1.añadir_coche()
        # Se modifica un cliente
        cliente2 = Cliente('Héctor', 'Sanz', '39669854C', 28500)
        cliente2.modificar_cliente()
        # Se borra un cliente
        cliente1.borrar_cliente()
        # Se borra un coche
        coche1.borrar_coche()
        # Se genera una oferta
        generar_oferta(cliente1, '2023-11-26', 1)

        # Generacion proceso almacen
        m1 = Mozo()
        r1 = Robot()
        # Actualizacion de inventario
        df_stock_actualizado = m1.actualizar_inventario()
        # Almacenamiento de material
        res_ingesta = m1.almacenar_material(df_stock_actualizado)
        # Robot realiza el inventario
        res_ingesta, res_aviso = r1.inventario_material()
        if res_aviso:
            m1.pedir_material()
        # Se solicita la extracción de un producto
        res_ingesta = r1.sacar_producto('Llave inglesa', 1)
        res_ingesta = r1.sacar_producto('Tijeras', 2)
        res_ingesta = r1.sacar_producto('Casco', 2)
        res_ingesta = r1.sacar_producto('Martillo', 1)

    except Exception as e:
        print('Ha habido un error inesperado: %s', e)
        print("\n%s", traceback.format_exc())
        print("\nError: " + str(e))
        sys.exit(1)

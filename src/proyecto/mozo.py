# -*- coding: utf-8 -*-
"""Fichero Mozo"""
import sys
import traceback

import pandas as pd

from proyecto.comun import leer_de_bd, escribir_en_almacen, GenericError


class Mozo(object):

    @staticmethod
    def actualizar_inventario():
        try:
            df_albaran = leer_de_bd('albaran')
            if (df_albaran['Cantidad'] < 0).any():
                raise GenericError("Error, Se ha introducido un producto con cantidad negativa en el albarán")

            df_stock_productos = leer_de_bd('stock_productos')
            df_stock_actualizado = pd.concat([df_albaran, df_stock_productos]).groupby(
                ['Producto', 'Precio'], as_index=False
            ).sum()
            df_stock_actualizado['Porcentaje'] = df_stock_actualizado['Cantidad'] / df_stock_actualizado['Total']
            if (df_stock_actualizado['Porcentaje'] > 1).any():
                raise GenericError(
                    "Error, uno o varios productos tienen una capacidad superior al total:",
                    df_stock_actualizado[df_stock_actualizado['Porcentaje'] > 1]['Producto'].to_list()
                )
            return df_stock_actualizado
        except Exception as ge:
            print('Ha habido un error durante la actualizacion del inventario', ge)
            raise GenericError(ge)

    @staticmethod
    def almacenar_material(df_stock_actualizado):
        try:
            res_ingesta = escribir_en_almacen('stock_productos', df_stock_actualizado)
            if not res_ingesta:
                raise GenericError("Error, No se ha almacenado bien el material")
            return res_ingesta
        except Exception as ge:
            print('Ha habido un error durante el almacenamiento del inventario', ge)
            raise GenericError(ge)

    @staticmethod
    def pedir_material():
        try:
            df_stock_productos = leer_de_bd('stock_productos')
            df_productos_pedir = df_stock_productos[df_stock_productos['Porcentaje'] < 0.7]

            res_ingesta = escribir_en_almacen('stock_necesario', df_productos_pedir)
            if not res_ingesta:
                raise GenericError("Error, No se ha generado bien la peticion de material")
            return res_ingesta
        except Exception as ge:
            print('Ha habido un error durante el pedido del material', ge)
            raise GenericError(ge)

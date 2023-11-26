# -*- coding: utf-8 -*-
"""Fichero Robot"""
import sys
import traceback

import pandas as pd

from proyecto.comun import leer_de_bd, escribir_en_almacen, GenericError


class Robot(object):

    @staticmethod
    def inventario_material():
        try:
            df_stock_productos = leer_de_bd('stock_productos')
            df_falta_stock = df_stock_productos[df_stock_productos['Porcentaje'] < 0.7]
            if df_falta_stock.shape[0] > 0:
                res_ingesta = escribir_en_almacen('stock_necesario', df_falta_stock)
                res_aviso = True
            else:
                res_ingesta = False
                res_aviso = False
            return res_ingesta, res_aviso
        except Exception as ge:
            print('Ha habido un error durante el inventario', ge)
            raise GenericError(ge)

    @staticmethod
    def sacar_producto(tipo, cantidad):
        try:
            df_producto_sacar = pd.DataFrame({'Producto': [tipo], 'Cantidad': [cantidad]})
            df_stock_disponible = leer_de_bd('stock_productos')

            df_stock_actualizado = pd.merge(df_stock_disponible, df_producto_sacar, how='outer', on="Producto").fillna(0)
            df_stock_actualizado['Cantidad'] = df_stock_actualizado['Cantidad_x'] - df_stock_actualizado['Cantidad_y']
            df_stock_actualizado['Porcentaje'] = df_stock_actualizado['Cantidad'] / df_stock_actualizado['Total']
            df_stock_actualizado = df_stock_actualizado[['Producto', 'Precio', 'Cantidad', 'Total', 'Porcentaje']]
            res_ingesta = escribir_en_almacen('stock_productos', df_stock_actualizado)
            return res_ingesta
        except Exception as ge:
            print('Ha habido un error durante la extracción de un producto', ge)
            raise GenericError(ge)

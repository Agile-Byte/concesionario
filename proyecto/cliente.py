# -*- coding: utf-8 -*-
"""Fichero Cliente"""
import pandas as pd

from proyecto.comun import GenericError, leer_de_bd, escribir_en_bd, borrar_de_bd, modificar_en_bd, comprobar_existencia


class Cliente(object):
    def __init__(self, nombre, apellido, dni, presupuesto):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.presupuesto = presupuesto

    def añadir_cliente(self):
        try:
            df_lista_cliente = leer_de_bd('listado_cliente')
            dict_cliente_nuevo = {
                'Nombre': [self.nombre], 'Apellido': [self.apellido], 'DNI': [self.dni],
                'Presupuesto': [self.presupuesto]
            }
            cliente_nuevo = pd.DataFrame(dict_cliente_nuevo)
            res_existencia = comprobar_existencia(df_lista_cliente, cliente_nuevo)
            if res_existencia:
                raise GenericError("Error, ya existe el cliente que se quiere añadir")
            else:
                res_ingesta = escribir_en_bd('listado_cliente', df_lista_cliente, cliente_nuevo)
                print('Se ha ingestado correctamente el cliente')
            return res_ingesta
        except GenericError as ge:
            print('Ha habido un error durante la ingesta de un nuevo cliente', ge)
            raise GenericError(ge)

    def modificar_cliente(self):
        try:
            df_lista_clientes = leer_de_bd('listado_cliente')
            dict_cliente_modif = {
                'Nombre': [self.nombre], 'Apellido': [self.apellido], 'DNI': [self.dni],
                'Presupuesto': [self.presupuesto]
            }
            cliente_modif = pd.DataFrame(dict_cliente_modif)
            res_existencia = comprobar_existencia(df_lista_clientes, cliente_modif)
            if not res_existencia:
                raise GenericError("Error, no existe el cliente que se quiere modificar")
            else:
                modificar_en_bd('listado_cliente', df_lista_clientes, cliente_modif)
                res_modif = True
                print('Se ha modificado correctamente el cliente')
            return res_modif
        except GenericError as ge:
            print('Ha habido un error durante la modificacion de un cliente', ge)
            raise GenericError(ge)

    def borrar_cliente(self):
        try:
            df_lista_clientes = leer_de_bd('listado_cliente')
            dict_cliente_borrar = {
                'Nombre': [self.nombre], 'Apellido': [self.apellido], 'DNI': [self.dni],
                'Presupuesto': [self.presupuesto]
            }
            cliente_borrar = pd.DataFrame(dict_cliente_borrar)
            res_existencia = comprobar_existencia(df_lista_clientes, cliente_borrar)
            if not res_existencia:
                raise GenericError("Error, no existe el cliente que se quiere borrar")
            else:
                borrar_de_bd('listado_cliente', cliente_borrar)
                res_borrado = True
                print('Se ha borrado correctamente el cliente')
            return res_borrado
        except GenericError as ge:
            print('Ha habido un error durante la ingesta de un nuevo coche', ge)
            raise GenericError(ge)

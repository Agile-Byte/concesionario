# -*- coding: utf-8 -*-
"""Fichero Coche"""
import pandas as pd

from proyecto.comun import GenericError, leer_de_bd, escribir_en_bd, borrar_de_bd, comprobar_existencia


class Coche(object):
    def __init__(self, marca, modelo, num_puertas, precio):
        self.marca = marca
        self.modelo = modelo
        self.num_puertas = num_puertas
        self.precio = precio

    def añadir_coche(self):
        try:
            df_lista_coche = leer_de_bd('listado_coche')
            dict_coche_nuevo = {
                'Marca': [self.marca], 'Modelo': [self.modelo], 'Número puertas': [self.num_puertas],
                'Precio': [self.precio]
            }
            coche_nuevo = pd.DataFrame(dict_coche_nuevo)
            res_existencia = comprobar_existencia(df_lista_coche, coche_nuevo)
            if res_existencia:
                raise GenericError("Error, ya existe el coche que se quiere añadir")
            else:
                res_ingesta = escribir_en_bd('listado_coche', df_lista_coche, coche_nuevo)
                print('Se ha ingestado correctamente el coche')
            return res_ingesta
        except GenericError as ge:
            print('Ha habido un error durante la ingesta de un nuevo coche', ge)
            raise GenericError(ge)

    def borrar_coche(self):
        try:
            df_lista_coches = leer_de_bd('listado_coche')
            dict_coche_borrar = {
                'Marca': [self.marca], 'Modelo': [self.modelo], 'Número puertas': [self.num_puertas],
                'Precio': [self.precio]
            }
            coche_borrar = pd.DataFrame(dict_coche_borrar)
            res_existencia = comprobar_existencia(df_lista_coches, coche_borrar)
            if not res_existencia:
                raise GenericError("Error, el coche que queremos borrar no existe")
            else:
                borrar_de_bd('listado_coche', coche_borrar)
                res_borrado = True
                print('Se ha borrado correctamente el coche')
            return res_borrado
        except GenericError as ge:
            print('Ha habido un error durante el borrado de un coche', ge)
            raise GenericError(ge)

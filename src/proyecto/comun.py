# -*- coding: utf-8 -*-
"""Funciones comunes a todas las clases"""
import os
import pandas as pd


class GenericError(Exception):
    """ GenericError """
    pass


def leer_de_bd(tipo):
    try:
        path_fichero = os.path.join('../extras', "%s.%s" % (tipo, 'xlsx'))
        existe_fichero = os.path.isfile(path_fichero)
        if existe_fichero:
            df_listado = pd.read_excel(path_fichero)
        else:
            raise GenericError("Error, no existe el fichero con el listado", path_fichero)
        return df_listado
    except GenericError as ge:
        print('Ha habido un error durante la lectura del listado', ge)
        raise GenericError(ge)


def escribir_en_bd(tipo, df_lista_cliente, df_escribir):
    try:
        path_fichero = os.path.join('../extras', "%s.%s" % (tipo, 'xlsx'))
        existe_fichero = os.path.isfile(path_fichero)
        if existe_fichero:
            pd.concat([df_lista_cliente, df_escribir]).to_excel(path_fichero, index=False)
            res_ingesta = True
        else:
            raise GenericError("Error, no existe el fichero con el listado", path_fichero)
        return res_ingesta
    except GenericError as ge:
        print('Ha habido un error durante la escritura de nuevo objeto', ge)
        raise GenericError(ge)


def escribir_en_almacen(tipo, df_stock_producto):
    try:
        path_fichero = os.path.join('../extras', "%s.%s" % (tipo, 'xlsx'))
        existe_fichero = os.path.isfile(path_fichero)
        if existe_fichero:
            df_stock_producto.to_excel(path_fichero, index=False)
            res_ingesta = True
        else:
            raise GenericError("Error, no existe el fichero a escribir")
        return res_ingesta
    except GenericError as ge:
        print('Ha habido un error durante la escritura del nuevo stock disponible', ge)
        raise GenericError(ge)


def borrar_de_bd(tipo, df_borrar):
    try:
        path_fichero = os.path.join('../extras', "%s.%s" % (tipo, 'xlsx'))
        existe_fichero = os.path.isfile(path_fichero)
        if existe_fichero:
            df_listado = leer_de_bd(tipo)
            df_listado_new = pd.merge(df_listado, df_borrar, how='outer', indicator=True)
            df_listado_new = (df_listado_new.loc[df_listado_new._merge == 'left_only', df_listado_new.columns]).drop(
                ['_merge'], axis=1
            )
            df_listado_new.to_excel(path_fichero, index=False)
        else:
            raise GenericError("Error, no existe el fichero con el listado", path_fichero)
    except GenericError as ge:
        print('Ha habido un error durante el borrado de nuevo objeto', ge)
        raise GenericError(ge)


def modificar_en_bd(tipo, df_lista, df_modif):
    try:
        df_lista = pd.merge(
            df_lista, df_modif.iloc[:, :-1], on=df_lista.iloc[:, :-1].columns.tolist(), how="outer", indicator=True
        )
        df_lista = df_lista.loc[df_lista["_merge"] == "left_only"].drop("_merge", axis=1)
        df_lista = pd.concat([df_lista, df_modif])
        path_fichero = os.path.join('../extras', "%s.%s" % (tipo, 'xlsx'))
        df_lista.to_excel(path_fichero, index=False)
    except GenericError as ge:
        print('Ha habido un error durante el borrado de nuevo objeto', ge)
        raise GenericError(ge)


def comprobar_existencia(df_listado, df_valor_comprobar):
    try:
        df_existente = pd.merge(
            df_listado.iloc[:, :-1], df_valor_comprobar.iloc[:, :-1], on=df_listado.iloc[:, :-1].columns.tolist(),
            how="outer", indicator=True
        )
        df_existente = df_existente.loc[df_existente["_merge"] == "both"].drop("_merge", axis=1)

        res_existencia = False if df_existente.empty else True
        return res_existencia
    except GenericError as ge:
        print('Ha habido un error durante la comprobacion de existencia', ge)
        raise GenericError(ge)


def generar_oferta(cliente1):
    # Leer lista de coches
    df_lista_coche = leer_de_bd('listado_coche')

    # Filtar por precio
    df_lista_coche_filtrada = df_lista_coche[df_lista_coche['Precio'] <= cliente1.presupuesto]

    path_fichero = os.path.join('../extras', "%s_%s_oferta.%s" % (cliente1.nombre, cliente1.apellido, 'xlsx'))
    df_lista_coche_filtrada.to_excel(path_fichero, index=False)
    print("Se ha generado un fichero con los coches dentro del presupuesto del cliente")

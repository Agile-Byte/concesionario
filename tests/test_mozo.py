# -*- coding: utf-8 -*-
"""Test Mozo"""
import unittest
from unittest import mock
import pandas as pd
from pandas.testing import assert_frame_equal

from src.proyecto.mozo import Mozo
from tests.utils import df_albaran, df_albaran_neg, df_albaran_max, df_stock_productos


class TestMozo(unittest.TestCase):
    """Test Mozo"""

    @mock.patch("src.proyecto.mozo.leer_de_bd",
                side_effect=[pd.DataFrame(df_albaran), pd.DataFrame(df_stock_productos),
                             pd.DataFrame(df_albaran_neg), pd.DataFrame(df_stock_productos),
                             pd.DataFrame(df_albaran_max), pd.DataFrame(df_stock_productos)])
    def test_actualizar_inventario(self, _):
        from utils import df_stock_expected
        # Caso 1: Se ha actualizado el albarán correctamente
        m1 = Mozo()
        df_stock_real = m1.actualizar_inventario()
        assert_frame_equal(df_stock_real, pd.DataFrame(df_stock_expected))

        # Caso 2: Algún producto tiene una cantidad negativa
        m2 = Mozo()
        self.assertRaises(Exception, m2.actualizar_inventario)

        # Caso 3: Se va a guardar más stock del máximo permitido
        m2 = Mozo()
        self.assertRaises(Exception, m2.actualizar_inventario)

    @mock.patch("src.proyecto.mozo.escribir_en_almacen")
    def test_almacenar_material(self, mock_escritura):
        from utils import df_stock_expected
        # Caso 1: Se escribe correctamente el nuevo stock disponible
        mock_escritura.return_value = True
        m1 = Mozo()
        res_real = m1.almacenar_material(pd.DataFrame(df_stock_expected))
        self.assertEqual(res_real, True)

        # Caso 2: No se escribe correctamente el nuevo stock disponible
        mock_escritura.return_value = False
        m2 = Mozo()
        self.assertRaises(Exception, m2.almacenar_material, pd.DataFrame(df_stock_expected))

    @mock.patch("src.proyecto.mozo.escribir_en_almacen")
    @mock.patch("src.proyecto.mozo.leer_de_bd")
    def test_pedir_material(self, mock_lectura, mock_escritura):
        from utils import df_stock_productos
        # Caso 1: Se genera una peticion con los materiales que se encuentran por debajo del umbral
        mock_lectura.return_value = pd.DataFrame(df_stock_productos)
        mock_escritura.return_value = True
        m1 = Mozo()
        res_real = m1.pedir_material()
        self.assertEqual(res_real, True)

        # Caso 2: No se ha podido generar la peticion
        mock_lectura.return_value = pd.DataFrame(df_stock_productos)
        mock_escritura.return_value = False
        m2 = Mozo()
        self.assertRaises(Exception, m2.pedir_material)


if __name__ == '__main__':
    unittest.main()

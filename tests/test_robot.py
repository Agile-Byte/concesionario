# -*- coding: utf-8 -*-
"""Test Robot"""
import unittest
from unittest import mock
import pandas as pd

from src.proyecto.robot import Robot
from tests.utils import df_stock_productos, df_stock_productos_completo


class TestRobot(unittest.TestCase):
    """Test Robot"""

    @mock.patch("src.proyecto.robot.escribir_en_almacen")
    @mock.patch("src.proyecto.robot.leer_de_bd")
    def test_inventario_material(self, mock_lectura, mock_escritura):
        from utils import df_albaran
        # Caso 1º: Se ha comprobado el inventario correctamente y ha emitido aviso
        mock_lectura.return_value = pd.DataFrame(df_stock_productos)
        mock_escritura.return_value = True
        r1 = Robot()
        res_real, res_aviso = r1.inventario_material()
        self.assertEqual(res_real, True)
        self.assertEqual(res_aviso, True)

        # Caso 2º: No hay cambios en el inventario y no se ha emitido aviso
        mock_lectura.return_value = pd.DataFrame(df_stock_productos_completo)
        mock_escritura.return_value = False
        r2 = Robot()
        res_real, res_aviso = r2.inventario_material()
        self.assertEqual(res_real, False)
        self.assertEqual(res_aviso, False)

    @mock.patch("src.proyecto.robot.escribir_en_almacen")
    @mock.patch("src.proyecto.robot.leer_de_bd")
    def test_sacar_producto(self, mock_lectura, mock_escritura):
        # Caso 1º: Se ha realizado la extraccion
        mock_lectura.return_value = pd.DataFrame(df_stock_productos)
        mock_escritura.return_value = True
        r1 = Robot()
        res_real = r1.sacar_producto('Tijeras', 2)
        self.assertEqual(res_real, True)

        # Caso 2º: No se ha encontrado el producto a extraer
        mock_lectura.return_value = pd.DataFrame(df_stock_productos)
        r2 = Robot()
        self.assertRaises(Exception, r2.inventario_material, 'Destornillador', 1)

        # Caso 3º: Se ha intentado extraer más cantidad de la existente
        mock_lectura.return_value = pd.DataFrame(df_stock_productos)
        r3 = Robot()
        self.assertRaises(Exception, r3.inventario_material, 'Destornillador', 10)


if __name__ == '__main__':
    unittest.main()

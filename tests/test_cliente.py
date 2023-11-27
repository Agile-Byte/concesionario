# -*- coding: utf-8 -*-
"""Test Cliente"""

import unittest
from unittest import mock
import pandas as pd

from src.proyecto.cliente import Cliente
from tests.utils import df_clientes_existente, df_clientes_no_existente


class TestCliente(unittest.TestCase):
    """Test Cliente"""

    @mock.patch("src.proyecto.cliente.escribir_en_bd")
    @mock.patch("src.proyecto.cliente.comprobar_existencia", side_effect=[False, True])
    @mock.patch("src.proyecto.cliente.leer_de_bd",
                side_effect=[pd.DataFrame(df_clientes_no_existente), pd.DataFrame(df_clientes_existente)])
    def test_añadir_cliente(self, _, __, mock_escritura):
        # Caso 1º: Se ha añadido correctamente el cliente
        c1 = Cliente('Pablo', 'Garcia', '12345678A', 15000)

        mock_escritura.return_value = True
        res_1 = c1.añadir_cliente()
        self.assertEqual(res_1, True)

        # Caso 2: Error cliente ya existente
        c2 = Cliente('Pablo', 'Garcia', '12345678A', 15000)
        self.assertRaises(Exception, c2.añadir_cliente)

    @mock.patch("src.proyecto.cliente.modificar_en_bd")
    @mock.patch("src.proyecto.cliente.comprobar_existencia", side_effect=[True, False])
    @mock.patch("src.proyecto.cliente.leer_de_bd",
                side_effect=[pd.DataFrame(df_clientes_existente), pd.DataFrame(df_clientes_no_existente)])
    def test_modificar_cliente(self, _, __, mock_modificar):
        # Caso 1º: Se ha modificado correctamente el cliente
        c1 = Cliente('Pablo', 'Garcia', '12345678A', 15000)

        mock_modificar.return_value = True
        res_1 = c1.modificar_cliente()
        self.assertEqual(res_1, True)

        # Caso 2: Error cliente no existente
        c2 = Cliente('Pablo', 'Garcia', '12345678A', 15000)
        self.assertRaises(Exception, c2.modificar_cliente)

    @mock.patch("src.proyecto.cliente.borrar_de_bd")
    @mock.patch("src.proyecto.cliente.comprobar_existencia", side_effect=[True, False])
    @mock.patch("src.proyecto.cliente.leer_de_bd",
                side_effect=[pd.DataFrame(df_clientes_existente), pd.DataFrame(df_clientes_no_existente)])
    def test_borrar_cliente(self, _, __, mock_borrar):
        # Caso 1º: Se ha borrado correctamente el cliente
        c1 = Cliente('Pablo', 'Garcia', '12345678A', 15000)

        mock_borrar.return_value = True
        res_1 = c1.borrar_cliente()
        self.assertEqual(res_1, True)

        # Caso 2: Error cliente no existente
        c2 = Cliente('Pablo', 'Garcia', '12345678A', 15000)
        self.assertRaises(Exception, c2.borrar_cliente)


if __name__ == '__main__':
    unittest.main()

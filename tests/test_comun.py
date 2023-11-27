# -*- coding: utf-8 -*-
"""Test Comun"""

import unittest
from unittest import mock
import pandas as pd

from src.proyecto.comun import comprobar_existencia, generar_oferta
from src.proyecto.cliente import Cliente

from tests.utils import df_lista_coche, df_promo


class TestComun(unittest.TestCase):
    """Test Comun"""

    def test_comprobar_existencia_existente(self):
        from tests.utils import df_clientes_existente, df_cliente, df_no_cliente

        # Caso 1º: Cliente existente
        res_existencia = comprobar_existencia(
            pd.DataFrame(df_clientes_existente), pd.DataFrame(df_cliente)
        )
        self.assertTrue(res_existencia)

        # Caso 2º: Cliente no existente
        res_existencia = comprobar_existencia(
            pd.DataFrame(df_clientes_existente), pd.DataFrame(df_no_cliente)
        )
        self.assertFalse(res_existencia)

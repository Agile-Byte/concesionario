# -*- coding: utf-8 -*-
"""Test Coche"""

import unittest
from unittest import mock
import pandas as pd

from src.proyecto.coche import Coche


class TestCoche(unittest.TestCase):
    """Test Cliente"""

    @mock.patch("src.proyecto.coche.escribir_en_bd")
    @mock.patch("src.proyecto.coche.comprobar_existencia", side_effect=[False, True])
    @mock.patch("src.proyecto.coche.leer_de_bd")
    def test_añadir_coche(self, mock_lectura, __, mock_escritura):
        from tests.utils import df_lista_coche
        # Caso 1º: Se ha añadido correctamente el coche
        c1 = Coche('BMW', 'M3', 5, 85000)

        mock_escritura.return_value = True
        mock_lectura.return_value = pd.DataFrame(df_lista_coche)
        res_1 = c1.añadir_coche()
        self.assertEqual(res_1, True)

        # Caso 2: Error coche ya existente
        c2 = Coche('Toyota', 'Yaris', 3, 10000)
        mock_lectura.return_value = pd.DataFrame(df_lista_coche)
        self.assertRaises(Exception, c2.añadir_coche)

    @mock.patch("src.proyecto.coche.borrar_de_bd")
    @mock.patch("src.proyecto.coche.comprobar_existencia", side_effect=[True, False])
    @mock.patch("src.proyecto.coche.leer_de_bd")
    def test_borrar_coche(self, mock_lectura, __, mock_borrar):
        from tests.utils import df_lista_coche
        # Caso 1º: Se ha borrado correctamente el coche
        c1 = Coche('Audi', 'A4', 5, 77000)

        mock_borrar.return_value = True
        mock_lectura.return_value = pd.DataFrame(df_lista_coche)
        res_1 = c1.borrar_coche()
        self.assertEqual(res_1, True)

        # Caso 2: Error coche no existente
        c2 = Coche('Mercedes', 'Clase A', 5, 45000)
        mock_lectura.return_value = pd.DataFrame(df_lista_coche)
        self.assertRaises(Exception, c2.borrar_coche)


if __name__ == '__main__':
    unittest.main()

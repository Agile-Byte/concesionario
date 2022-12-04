#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

from tests.test_cliente import TestCliente
from tests.test_coche import TestCoche
from tests.test_mozo import TestMozo
from tests.test_robot import TestRobot

if __name__ == '__main__':
    try:
        # Test Suite 
        test = unittest.TestSuite()
        test.addTest(TestCliente('test_añadir_cliente'))
        test.addTest(TestCliente('test_modificar_cliente'))
        test.addTest(TestCliente('test_borrar_cliente'))
        test.addTest(TestCoche('test_añadir_coche'))
        test.addTest(TestCoche('test_borrar_coche'))
        test.addTest(TestMozo('test_actualizar_inventario'))
        test.addTest(TestMozo('test_almacenar_material'))
        test.addTest(TestMozo('test_pedir_material'))
        test.addTest(TestRobot('test_inventario_material'))
        test.addTest(TestRobot('test_sacar_producto'))
        # Run
        unittest.TextTestRunner().run(test)
    except KeyboardInterrupt:
        print("\nInterrumpido")
        sys.exit(0)
    except Exception as e:
        print("\nError: " + str(e))
        sys.exit(1)

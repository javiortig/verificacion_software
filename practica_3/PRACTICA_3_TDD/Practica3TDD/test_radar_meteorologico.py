from unittest import TestCase
from radar_meteorologico import alcance_del_radar

class TestRadarMeteorologico(TestCase):

    def test_valores_validos(self):
        """ Test de valores validos """
        self.assertAlmostEqual(alcance_del_radar(0.5, 2), 74999.700)
        self.assertAlmostEqual(alcance_del_radar(0.6, 1), 89999.85)
        self.assertAlmostEqual(alcance_del_radar(0.3, 0.5), 44999.925)


    def test_valores_fuera_rango(self):
        """ Test ValueError cuando hay valores positivos fuera de rango """
        self.assertRaises(ValueError, alcance_del_radar, 0.2, 5.0)
        self.assertRaises(ValueError, alcance_del_radar, 0.8, 2.0)
        self.assertRaises(ValueError, alcance_del_radar, 0.2, 5.0)


    def test_valores_negativos(self):
        """ Test ValueError cuando hay de valores negativos """
        self.assertRaises(ValueError, alcance_del_radar, -0.1, 2.0)
        self.assertRaises(ValueError, alcance_del_radar, 0.5, -1.0)
        self.assertRaises(ValueError, alcance_del_radar, -0.1, -1.0)


    def test_T_menor_tau(self):
        """ Test ValueError cuando T es menor que tau """
        self.assertRaises(ValueError, alcance_del_radar, 0.000002, 3.0)
        self.assertRaises(ValueError, alcance_del_radar, 0.000005, 6.0)


    def test_strings(self):
        """ Test TypeError cuando hay entrada de strings """
        self.assertRaises(TypeError, alcance_del_radar, 0.5, "2.0")
        self.assertRaises(TypeError, alcance_del_radar, "0.5", 2.0)
        self.assertRaises(TypeError, alcance_del_radar, "0.5", "2.0")
        self.assertRaises(TypeError, alcance_del_radar, "letra", "palabra")
        self.assertRaises(TypeError, alcance_del_radar, "123", "no es un número")


    def test_booleanos(self):
        """ Test TypeError cuando hay entrada de booleanos """
        self.assertRaises(TypeError, alcance_del_radar, True, 2.0)
        self.assertRaises(TypeError, alcance_del_radar, 0.5, True)


import unittest
from sources.weapon import WeaponDispenser

class TestWeaponDispenser(unittest.TestCase):
    def test_creation(self):
        """
        Weapon creation is possible

        Returns
        -------

        """

        w = WeaponDispenser()

import unittest
from sources.weapon import WeaponDispenser

class TestWeaponDispenser(unittest.TestCase):
    def test_creation(self):
        """
        Weapon creation is possible

        Returns
        -------

        """
        wd = WeaponDispenser()

    def test_num_weapons(self):
        """
        WeaponDispenser should start with the correct number of weapons

        Returns
        -------

        """
        wd = WeaponDispenser()
        self.assertTrue(len(wd.weapons) == 3,
                    "There are not 3 weapons in dispenser")

    def test_dispense_weapon(self):
        """
        WeaponDispenser dispenses next weapon

        Returns
        -------

        """

        wd = WeaponDispenser()
        top_of_stack = wd.weapons[-1]
        if wd.dispense() != top_of_stack:
            self.fail("We got a wrong weapon!")

    def test_empty_dispenser(self):
        """
        empty dispenser dispenses none

        Returns
        -------

        """
        wd = WeaponDispenser()
        for i in range(len(wd.weapons)):
            wd.dispense()
        self.assertFalse(wd.dispense(),
                         "Empty dispenser!")

    # @unittest.skip("TODO: Need designer input about future stuff")
    def test_future_stuff(self):
        """
        Future stuff

        Returns
        -------

        """
        self.fail("Failed for the purpose")

    @unittest.expectedFailure
    def test_easter_egg(self):
        """
        Easter egg...

        Returns
        -------

        """

        wd = WeaponDispenser()
        wd.easter_egg()

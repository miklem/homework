import unittest

from mpkg.lecture04 import my_function


class TestMyFunction(unittest.TestCase):
    def test_does_not_crashed(self):
        """
        my function() does not crashed when called

        Returns
        -------

        """
        my_function(5)

    def test_true_and_false(self):
        """
        using assertTrue and assetFalse to test things

        Returns
        -------

        """
        self.assertTrue(my_function(5) == 10)
        self.assertFalse(my_function(5) == 9)

    def test_special_zero(self):
        """
        my_function(0) returns 100
        Returns
        -------

        """
        x = my_function(0)
        if x != 100:
            self.fail("zero is special, my function(0) didn`t return 100")



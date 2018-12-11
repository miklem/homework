import unittest

from mpkg.lecture04 import my_function
from mpkg.lecture04 import MyClass


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


class TestMyClass(unittest.TestCase):
    @unittest.skip("not implemented yet")
    def test_counter_start(self):
        """
        counter starts zero
        Returns
        -------

        """
        self.skipTest("Not implemented, but skipping from inside")

    @unittest.skip("not implemented yet")
    def test_id_assigned(self):
        """

        Returns
        -------

        """
        pass

    @unittest.skip("not implemented yet")
    def test_counter_incremented(self):
        """
        Counter gets incremented
        Returns
        -------

        """
        pass

    @unittest.skip("not implemented yet")
    def test_get_id(self):
        """
        get id() works
        Returns
        -------

        """
        pass

    @unittest.expectedFailure
    def test_unstable_method(self):
        """
        unstable_method() does whatever it wants

        Returns
        -------

        """
        m = MyClass()
        m.unstable_method()
        
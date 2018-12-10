import unittest

from mpkg.lecture04 import show_the_text


class TestMyFunction(unittest.TestCase):
    def test_does_not_crashed(self):
        """
        my function() does not crashed when called
        Returns
        -------

        """
        show_the_text(5)

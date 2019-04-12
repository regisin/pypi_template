import unittest

from MY_PKG_NAME import *

class TestClasses(unittest.TestCase):
    """
    Tests class X.
    """
    def setUp(self):
        """
        Initialize test objects.
        """
        self.object = MY_CLASS()

    def TEST_NAME(self):
        """
        Tests `NAME` function.
        """
        a=0
        self.assertEqual(0, a)


if __name__ == '__main__':
    unittest.main()
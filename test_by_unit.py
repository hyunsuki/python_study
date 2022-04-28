import unittest

class MyTestClass(unittest.TestCase):

    def test_function1(self):
        self.assertEqual(1,1)
        self.assertNotEqual(1,1)
        self.assertFalse(4<5)
        self.assertTrue(4<5)

    def test_function2(self):
        self.assertTrue("BRAVO".isupper())
        self.assertEqual("ALPHA".lower(), "alpha")

def main():
    """
    This file make fortesting git
    """

if __name__ == '__main__':
    print(main.__doc__)
    unittest.main()

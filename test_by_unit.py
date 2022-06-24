import unittest

class MyTestClass(unittest.TestCase):

    def test_function_equal(self):
        self.assertEqual(1,1)

    def test_function_not_equal(self):
        self.assertNotEqual(1,2)

    def test_function_true(self):
        self.assertTrue(1<2)

    def test_function_false(self):
        self.assertFalse(1>2)

    def test_function_is(self):
        self.assertIs(1,1)

    def test_function_in_not(self):
        self.assertIsNot(1,2)

    def test_function_none(self):
        self.assertIsNone(None)

    def test_function_not_none(self):
        self.assertIsNotNone(1)

    def test_function_in(self):
        self.assertIn(1, [1, 2, 3])

    def test_function_not_in(self):
        self.assertNotIn(4, [1, 2, 3])

    def test_function_instance(self):
        self.assertIsInstance(1, int)

    def test_function_not_instance(self):
        self.assertNotIsInstance(1, str)

if __name__ == '__main__':
    unittest.main()

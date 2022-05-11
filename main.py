import unittest


class MyTestCase(unittest.TestCase):

    def test_func_equal(self):
        self.assertEqual(1, 1)

    def test_func_not_equal(self):
        self.assertNotEqual(1, 2)

    @unittest.skip('reason')
    def test_func_true(self):
        word = "world"
        self.assertTrue(word.islower())

    def test_func_false(self):
        word = "World"
        self.assertFalse(word.islower())

    def test_func_is(self):
        self.assertIs(1, 1)

    def test_func_is_not(self):
        self.assertIsNot(1, 2)

    def test_func_none(self):
        self.assertIsNone(None)

    def test_func_not_none(self):
        self.assertIsNotNone(1)

    def test_func_in(self):
        int_list = [1, 2, 3, 4, 5]
        self.assertIn(1, int_list)

    def test_func_not_in(self):
        int_list = [1, 2, 3, 4, 5]
        self.assertNotIn(6, int_list)

    def test_func(self):
        data = 10
        self.assertIsInstance(data, int)

    def test_func(self):
        data = 10
        self.assertNotIsInstance(data, str)


if __name__ == '__main__':
    unittest.main()

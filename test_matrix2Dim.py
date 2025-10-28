import unittest
from matrix2Dim import Matrix2Dim, IncorrectDimensionsException, IncoherentException

class TestMatrix2Dim(unittest.TestCase):

    def test_constructor_with_elements(self):
        m = Matrix2Dim((2, 2), [[1, 2], [3, 4]])
        self.assertEqual(m.get_element(0, 0), 1)
        self.assertEqual(m.get_element(1, 1), 4)

    def test_constructor_without_elements(self):
        m = Matrix2Dim((2, 2))
        self.assertEqual(m.get_element(0, 0), 0)
        self.assertEqual(m.get_element(1, 1), 0)

    def test_incorrect_dimensions_exception(self):
        with self.assertRaises(IncorrectDimensionsException):
            Matrix2Dim((0, 3))

    def test_incoherent_exception(self):
        with self.assertRaises(IncoherentException):
            Matrix2Dim((2, 2), [[1, 2], [3]])  # second row too short

    def test_get_element_valid(self):
        m = Matrix2Dim((2, 3), [[0, 1, 2], [3, 4, 5]])
        self.assertEqual(m.get_element(1, 1), 4)

    def test_get_element_out_of_bounds(self):
        m = Matrix2Dim((2, 2))
        with self.assertRaises(IndexError):
            m.get_element(2, 0)

    def test_set_element(self):
        m = Matrix2Dim((2, 2))
        m.set_element(0, 1, 9)
        self.assertEqual(m.get_element(0, 1), 9)

    def test_set_element_out_of_bounds(self):
        m = Matrix2Dim((2, 2))
        with self.assertRaises(IndexError):
            m.set_element(3, 3, 5)

    def test_str_representation(self):
        m = Matrix2Dim((2, 2), [[1, 2], [3, 4]])
        output = str(m)
        self.assertIn("(2, 2)", output)
        self.assertIn("|1||2|", output)
        self.assertIn("|3||4|", output)

    def test_eq_operator(self):
        a = Matrix2Dim((2, 2), [[1, 2], [3, 4]])
        b = Matrix2Dim((2, 2), [[1, 2], [3, 4]])
        c = Matrix2Dim((2, 2), [[4, 3], [2, 1]])
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)

    def test_transpose(self):
        m = Matrix2Dim((2, 3), [[1, 2, 3], [4, 5, 6]])
        t = m.transpose()
        expected = Matrix2Dim((3, 2), [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(t, expected)

    def test_is_symmetric_true(self):
        m = Matrix2Dim((2, 2), [[1, 2], [2, 1]])
        self.assertTrue(m.is_symmetric())

    def test_is_symmetric_false(self):
        m = Matrix2Dim((2, 2), [[1, 2], [3, 4]])
        self.assertFalse(m.is_symmetric())

    def test_total(self):
        m = Matrix2Dim((2, 2), [[1, 2], [3, 4]])
        self.assertEqual(m.total(), 10)

    def test_average(self):
        m = Matrix2Dim((2, 2), [[1, 2], [3, 4]])
        self.assertAlmostEqual(m.average(), 2.5)

    def test_is_coherent_true(self):
        m = Matrix2Dim((2, 3), [[1, 2, 3], [4, 5, 6]])
        self.assertTrue(m.is_coherent())

if __name__ == '__main__':
    unittest.main()

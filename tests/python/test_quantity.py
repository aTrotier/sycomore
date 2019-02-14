import unittest

import sycomore

class TestQuantity(unittest.TestCase):
    def test_comparison(self):
        q1 = sycomore.Quantity(2, sycomore.Dimensions(1,0,0,0,0,0,0))
        q2 = sycomore.Quantity(3, sycomore.Dimensions(1,0,0,0,0,0,0))
        q3 = sycomore.Quantity(2, sycomore.Dimensions(0,1,0,0,0,0,0))

        self.assertTrue(q1 == q1)
        self.assertFalse(q1 == q2)
        self.assertFalse(q1 == q3)

        self.assertFalse(q1 != q1)
        self.assertTrue(q1 != q2)
        self.assertTrue(q1 != q3)

        self.assertTrue(q1 < q2)
        self.assertFalse(q2 <= q1)
        self.assertFalse(q1 > q2)
        self.assertFalse(q1 >= q2)
        with self.assertRaises(Exception):
            q1 < q3
        with self.assertRaises(Exception):
            q1 <= q3
        with self.assertRaises(Exception):
            q1 > q3
        with self.assertRaises(Exception):
            q1 >= q3

    def test_addition_in_place(self):
        q1 = sycomore.Quantity(2, sycomore.Dimensions(1,0,0,0,0,0,0))
        q2 = sycomore.Quantity(3, sycomore.Dimensions(1,0,0,0,0,0,0))
        r = sycomore.Quantity(5, sycomore.Dimensions(1,0,0,0,0,0,0))
        q1 += q2
        self.assertEqual(q1, r)

        q3 = sycomore.Quantity(2, sycomore.Dimensions(0,1,0,0,0,0,0))
        with self.assertRaises(Exception):
            q1 += q3

    def test_subtraction_in_place(self):
        q1 = sycomore.Quantity(2, sycomore.Dimensions(1,0,0,0,0,0,0))
        q2 = sycomore.Quantity(3, sycomore.Dimensions(1,0,0,0,0,0,0))
        r = sycomore.Quantity(-1, sycomore.Dimensions(1,0,0,0,0,0,0))
        q1 -= q2
        self.assertEqual(q1, r)

        q3 = sycomore.Quantity(2, sycomore.Dimensions(0,1,0,0,0,0,0))
        with self.assertRaises(Exception):
            q1 -= q3

    def test_multiplication_in_place(self):
        q1 = sycomore.Quantity(2, sycomore.Dimensions(1,0,0,0,0,0,0))
        q2 = sycomore.Quantity(3, sycomore.Dimensions(0,1,0,0,0,0,0))
        r = sycomore.Quantity(6, sycomore.Dimensions(1,1,0,0,0,0,0))
        q1 *= q2
        self.assertEqual(q1, r)

    def test_scalar_multiplication_in_place(self):
        q = sycomore.Quantity(2, sycomore.Dimensions(1,0,0,0,0,0,0))
        r = sycomore.Quantity(6, sycomore.Dimensions(1,0,0,0,0,0,0))
        q *= 3
        self.assertEqual(q, r)

    def test_division_in_place(self):
        q1 = sycomore.Quantity(1, sycomore.Dimensions(1,0,0,0,0,0,0))
        q2 = sycomore.Quantity(4, sycomore.Dimensions(0,1,0,0,0,0,0))
        r = sycomore.Quantity(0.25, sycomore.Dimensions(1,-1,0,0,0,0,0))
        q1 /= q2
        self.assertEqual(q1, r)

    def test_scalar_division_in_place(self):
        q = sycomore.Quantity(2, sycomore.Dimensions(1,0,0,0,0,0,0))
        r = sycomore.Quantity(0.5, sycomore.Dimensions(1,0,0,0,0,0,0))
        q /= 4
        self.assertEqual(q, r)

    def test_unary_plus(self):
        q = sycomore.Quantity(2, sycomore.Dimensions(1,0,0,0,0,0,0))
        self.assertEqual(+q, q)

    def test_unary_minus(self):
        q = sycomore.Quantity(2, sycomore.Dimensions(1,0,0,0,0,0,0))
        r = sycomore.Quantity(-2, sycomore.Dimensions(1,0,0,0,0,0,0))
        self.assertEqual(-q, r)

    def test_addition(self):
        q1 = sycomore.Quantity(2, sycomore.Dimensions(1,0,0,0,0,0,0))
        q2 = sycomore.Quantity(3, sycomore.Dimensions(1,0,0,0,0,0,0))
        r = sycomore.Quantity(5, sycomore.Dimensions(1,0,0,0,0,0,0))
        self.assertEqual(q1+q2, r)

        q3 = sycomore.Quantity(2, sycomore.Dimensions(0,1,0,0,0,0,0))
        with self.assertRaises(Exception):
            q1 + q3

    def test_subtraction(self):
        q1 = sycomore.Quantity(2, sycomore.Dimensions(1,0,0,0,0,0,0))
        q2 = sycomore.Quantity(3, sycomore.Dimensions(1,0,0,0,0,0,0))
        r = sycomore.Quantity(-1, sycomore.Dimensions(1,0,0,0,0,0,0))
        self.assertEqual(q1-q2, r)

        q3 = sycomore.Quantity(2, sycomore.Dimensions(0,1,0,0,0,0,0))
        with self.assertRaises(Exception):
            q1 - q3

    def test_multiplication(self):
        q1 = sycomore.Quantity(2, sycomore.Dimensions(1,0,0,0,0,0,0))
        q2 = sycomore.Quantity(3, sycomore.Dimensions(0,1,0,0,0,0,0))
        r = sycomore.Quantity(6, sycomore.Dimensions(1,1,0,0,0,0,0))
        self.assertEqual(q1*q2, r)

    def test_scalar_multiplication(self):
        q = sycomore.Quantity(2, sycomore.Dimensions(1,0,0,0,0,0,0))
        r = sycomore.Quantity(6, sycomore.Dimensions(1,0,0,0,0,0,0))
        self.assertEqual(q*3, r)
        self.assertEqual(3*q, r)

    def test_division(self):
        q1 = sycomore.Quantity(1, sycomore.Dimensions(1,0,0,0,0,0,0))
        q2 = sycomore.Quantity(4, sycomore.Dimensions(0,1,0,0,0,0,0))
        r = sycomore.Quantity(0.25, sycomore.Dimensions(1,-1,0,0,0,0,0))
        self.assertEqual(q1/q2, r)

    def test_scalar_division(self):
        q = sycomore.Quantity(2, sycomore.Dimensions(1,0,0,0,0,0,0))
        r1 = sycomore.Quantity(0.5, sycomore.Dimensions(1,0,0,0,0,0,0))
        r2 = sycomore.Quantity(1.5, sycomore.Dimensions(-1,0,0,0,0,0,0))
        self.assertEqual(q/4, r1)
        self.assertEqual(3/q, r2)

if __name__ == "__main__":
    unittest.main()
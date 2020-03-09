import unittest
from homeWork.hw3_t6 import is_year_leap, isTriangle, getTypeTriangle


class task5_3_1(unittest.TestCase):
    def test_leap_year01(self):
        year = 2000
        rezult = is_year_leap(year)
        self.assertEqual(rezult, True, 'Is Leap')

    def test_leap_year02(self):
        year = 2001
        rezult = is_year_leap(year)
        self.assertEqual(rezult, False, 'is not Leap')

    def test_triangle01(self):
        a = 3
        b = 4
        c = 5
        rezult = isTriangle(a, b, c)
        self.assertEqual(rezult, True, 'is not triangle')
        # print(a)

    def test_triangle02(self):
        a = 3
        b = 4
        c = 15
        rezult = isTriangle(a, b, c)
        self.assertEqual(rezult, False, 'is realy triangle')
        # print(a)

    def test_get_type_triangle01(self):
        a = b = c = 4
        rezult = getTypeTriangle(a, b, c)
        self.assertEqual(rezult, 'Equilateral triangle (равносторонний)', 'its uncnown triangle')

    def test_get_type_triangle02(self):
        a = b = 4
        c = 5
        rezult = getTypeTriangle(a, b, c)
        self.assertEqual(rezult, 'Isosceles triangle (равнобедренный)', 'we have a problem')

    def test_get_type_triangle03(self):
        a = 4
        b = 3
        c = 5
        rezult = getTypeTriangle(a, b, c)
        self.assertEqual(rezult, 'Versatile triangle (разносторонний)', 'we have a problem')

    def test_get_type_triangle04(self):
        a = 4
        b = 3
        c = 15
        rezult = getTypeTriangle(a, b, c)
        self.assertEqual(rezult, 'Not a triangle', 'we have a problem')


if __name__ == '__main__':
    unittest.main()

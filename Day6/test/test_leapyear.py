import unittest
import leapyear_test

class TestLeapYear(unittest.TestCase):
    def test_leapyear_true(self):
        self.assertTrue(leapyear_test.leapyear_test(2000))

    def test_leapyear_false(self):
        self.assertTrue(leapyear_test.leapyear_test(2111))
        self.assertTrue(leapyear_test.leapyear_test(1900))
        self.assertTrue(leapyear_test.leapyear_test(1800))
        self.assertTrue(leapyear_test.leapyear_test(1500))


if __name__=='_main_':
    unittest.main()

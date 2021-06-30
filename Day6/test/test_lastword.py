import lastword_test
import unittest

class Testlength_of_lastword(unittest.TestCase):
    def test_blank_input(self):
      self.assertEqual(lastword_test.length_of_lastword(""),0)

    def test_multiplewords(self):
        self.assertEqual(lastword_test.length_of_lastword("wants and benefits"),8)

    if __name__=='_main_':
     unittest.main()
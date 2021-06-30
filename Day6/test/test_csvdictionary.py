import csvdictionary_test
import unittest

class Testcsvdictionary(unittest.TestCase):

   
    # read csv test 
    def test_read_csv(self):
        self.assertIsNotNone(csvdictionary_test.read("peeps.csv"))

    # file not found test
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            csvdictionary_test.read("")

    # test if correct type
    def test_if_correct_type(self):
        with self.assertRaises(OSError):
            csvdictionary_test.read(6)
    

    
if __name__ == '__main__':
    unittest.main()

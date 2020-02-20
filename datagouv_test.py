from datagouv import *
import unittest

class TestCSV(unittest.TestCase):
    ''' Classe pour tester la bibliothèque datagouv classe \n '''
    # https://docs.python.org/fr/3/library/unittest.html

    def test_test1(self):
        # Loading files
        datafile = DataFile('./test.csv',";")
        study = Study(datafile)
        # Loaded ?
        self.assertIs(type(datafile), DataFile, "Not a DataFile")
        self.assertIs(type(study), Study, "Not a Study")
        # Reading headers
        self.assertTrue(len(datafile.headers)>1, "Should be >1")
        self.assertEqual(datafile.headers[4], "date_creat", "Not a DataFile")

    def test_test2(self):
        datafile = DataFile('./test.csv')
        study = Study(datafile)
        datafile.read_first_lines()
        self.assertTrue(len(datafile.firstlines) == 10, "Should be 10")



        



    def test_test3(self):
        1

    def test_test4(self):
        1

    def test_test5(self):
        1        




if __name__ == '__main__':
    unittest.main()

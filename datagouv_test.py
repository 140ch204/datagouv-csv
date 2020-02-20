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
        # Testing headers
        self.assertTrue(len(datafile.headers)>1, "Should be >1")
        self.assertEqual(datafile.headers[4], "date_creat", "Not a DataFile")

    def test_test2(self):
        # Loading files
        datafile = DataFile('./test.csv')
        study = Study(datafile)

        # Test read_first_lines() and firstlines
        datafile.read_first_lines()
        self.assertTrue(len(datafile.firstlines) == 10, "Should be 10")

        # Test _updateresultfilename
        study._updateresultfilename()
        self.assertTrue("results_" in study.resultfilename , "Should include 'results_' ")


    def test_test3(self):
        # Loading files
        datafile = DataFile('./test.csv')
        study = Study(datafile)

        # Find Header
        self.assertEqual(study._findheader('date_creat'), 4 , "Should be 4 ")

        # Find all column
        self.assertEqual(len(study.search_in_all_column('76760')), 67, "Should be 67 ")

        # Find 
        study.search_in_one_column('76760','adrs_codeinsee')
        self.assertEqual(len(study.result), 3, "Should be 3 ")


    def test_test4(self):
        1

    def test_test5(self):
        1        




if __name__ == '__main__':
    unittest.main()

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

        # read_first_lines() 
        # firstlines
        datafile.read_first_lines()
        self.assertTrue(len(datafile.firstlines) == 10, "Should be 10")

        # _updateresultfilename
        study._updateresultfilename()
        self.assertTrue("results_" in study.resultfilename , "Should include 'results_' ")

    def test_test3(self):
        # Loading files
        datafile = DataFile('./test.csv')
        study = Study(datafile)

        # _findheader
        self.assertEqual(study._findheader('date_creat'), 4 , "Should be 4 ")

        # _find_in_all_column
        # search_in_all_column
        self.assertEqual(len(study._find_in_all_column('76760')), 5, "Should be 5 ")
        study.search_in_all_column('76760')
        self.assertEqual(len(study.result), 5, "Should be 5 ")

        # _find_in_one_column
        # search_in_one_column
        self.assertEqual(len(study._find_in_one_column('76760','adrs_codeinsee')), 3, "Should be 3 ")
        study.search_in_one_column('76760','adrs_codeinsee')
        self.assertEqual(len(study.result), 3, "Should be 3 ")

    def test_test4(self):

        # Loading files
        datafile = DataFile('./test.csv')
        study = Study(datafile)
        
        # extract_first_lines
        study.extract_first_lines(8)
        self.assertEqual(len(study.result), 8, "Should be 8 ")

        # _write_result
        study._write_result(study.result)
        with open( "results/" + study.resultfilename, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = study.datafile.delimiter)
            row_nb = 0
            for row in csv_reader:
                row_nb += 1
        self.assertEqual(row_nb, 9, "Should be 9 ")


 
if __name__ == '__main__':
    unittest.main()

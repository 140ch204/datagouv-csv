import csv
from datetime import datetime
from datagouv import *


#mystudy.extract_first_lines()

## StockEtablissement_utf8

#myfile = DataFile('./data/StockEtablissement_utf8.csv', delimiter = ',', lineterminator='\r\n', encoding = 'utf-8')
#mystudy = Study(myfile)
#mystudy.extract_first_lines()
#mystudy.search_in_one_column('91790', 'codePostalEtablissement')

## rna_import_20200101.csv

#myfile = DataFile('./data/rna_import_20200101.csv', delimiter = ';', lineterminator='\r\n',  encoding = 'latin_1')
#mystudy = Study(myfile)
#mystudy.search_in_one_column('91790', 'adrs_codepostal')


## rna_waldec_20200101

#myfile = DataFile('./data/rna_waldec_20200101.csv', delimiter = ';', lineterminator='\r\n',  encoding = 'latin_1')
#mystudy = Study(myfile)
#mystudy.search_in_one_column('91790', 'adrs_codepostal')


## chiffres_cle_2018.csv
#myfile = DataFile('./data/chiffres_cle_2018.csv', delimiter = ';', lineterminator='\r\n', encoding = 'utf-8')
#mystudy = Study(myfile)
#mystudy.search_in_one_column('91790', 'Code postal')
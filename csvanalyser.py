import csv
from datetime import datetime
from datagouv import *

#
#rnafile = DataFile('./results/results_2020_1_30_17_45_36.csv', ';')

#print(mystudy.search_in_one_colmun('00000','adrs_codepostal'))

# print(mystudy.datafile.titles)

#print(mystudy.datafile.firstlines)

#print(mystudy.search_in_all_colmun("00000"))

#mystudy.extract_first_lines(1000)

#print(mystudy.search_in_one_colmun('91790','codePostalEtablissement'))

rnafile = DataFile('./data/StockEtablissement_utf8.csv', ';')
mystudy = Study(rnafile)
mystudy.extract_first_lines(1000)
print(mystudy.search_in_one_column('91790','codePostalEtablissement'))

#Département

#rnafile = DataFile('./data/chiffres_cle_2018.csv', ';')
#mystudy = Study(rnafile)
#print(mystudy.search_in_one_column('91790','Code postal'))






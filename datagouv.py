import os
import csv
from datetime import datetime
clear = lambda: os.system('clear') #on Windows System
 
class DataFile:
  ### This is the opendata.gouv file with the data ### 
    def __init__(self, name, delimiter ):
        ### Initialization method ###
        self.created = datetime.now()
        self.updated = datetime.now()
        self.name = name
        self.delimiter = delimiter
        self.titles = []
        self.readtitles()
        self.firstlines = []
        self.read_first_lines(10)

    def __repr__(self):
         return self.name + " mis à jour le " + str(self.updated)

    def readtitles(self):
        self.titles = []
        with open(self.name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter, lineterminator='\r\n')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    self.titles += row
                    line_count += 1
                else:
                  break
        self.updated = datetime.now()

    def read_first_lines(self,linenumber = 2):
        self.firstlines = []
        with open(self.name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter, lineterminator='\r\n')
            line_count = 0
            for row in csv_reader:
                if line_count < linenumber:
                    self.firstlines += row
                    line_count += 1
                else:
                  break
        self.updated = datetime.now()

class Study:
    ###  Association     ###
    # CRUD Create Read Update Delete #

    def __init__(self, datafile ):
        ### Initialization method ###
        self.datafile = datafile
        self.created = datetime.now()
        self.updated = datetime.now()
        self.resultfilename = "not initialized"
        self.datafile.readtitles()

    def _updateresultfilename(self):
      ### update the name for the result file ###
        d = datetime.now()
        self.resultfilename = "results_" + str(d.year) + "_" + str(d.month) + "_" + str(d.day) + "_" + str(d.hour) + "_" + str(d.minute) + "_" + str(d.second)+".csv"

    def _findtitle(self,searched_title):
        columnnb = 0
        for title in self.datafile.titles:
            if searched_title == title:
                break
            columnnb += 1
        return columnnb

    def _write_result(self,result):
        self._updateresultfilename()
        with open( "results/" + self.resultfilename, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';')
            spamwriter.writerow(self.datafile.titles)
            for line in result:
                spamwriter.writerow(line)
        
    def search_in_one_column(self, value, searched_title): 
        # Search the value in the colmun named searched_title
        start_time = datetime.now()

        #Find
        result = self._find_in_one_column(value, searched_title) 
        #Save           
        self._write_result(result)

        end_time = datetime.now()

        return "Result saved in " + self.resultfilename + " within " + str(end_time - start_time)

    def _find_in_one_column(self,value, searched_title):
        columnnb = self._findtitle(searched_title)
        result = []
        with open( self.datafile.name, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = self.datafile.delimiter)
            row_nb = 0
            for row in csv_reader:
                if len(row)-1 >= columnnb: 
                    if (value in row[columnnb]) and row_nb !=0  :
                        result += [row]
                    row_nb += 1 
        return result

    def search_all(self,value): 
        with open(self.datafile.name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = self.datafile.delimiter)
            for row in csv_reader:
                for field in row:
                    if value in field :
                        print(row)
        return "test ok"


    def search_in_all_column(self, value): 
        # Search the value in the colmun named searched_title
        start_time = datetime.now()

        #Find
        result = self._find_in_all_column(value) 
        #Save           
        self._write_result(result)

        end_time = datetime.now()

        return "Result saved in " + self.resultfilename + " within " + str(end_time - start_time)


    def _find_in_all_column(self,value):

        result = []
        with open( self.datafile.name, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = self.datafile.delimiter)
            row_nb = 0
            for row in csv_reader:
                for field in row:
                    if value in field :
                        result += [row]
                    row_nb += 1 
        return result

    def extract_first_lines(self,linenumber=10):

        result = []
        with open( self.datafile.name, 'r', newline='',encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = self.datafile.delimiter, lineterminator='\r\n')
            line_count = 0
            for row in csv_reader:
                #print(result)
                if line_count < linenumber:
                    result += [row]
                    line_count += 1
                else:
                  break
            #print(result)
            
        self._write_result(result)

        return result

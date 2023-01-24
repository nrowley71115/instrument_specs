"""This function takes an inputted csv data sheet and returns the dicitonary.
Inputs: CSV data sheet directory
Outputs: dictionary of spec (key) and options (values). Options is a dictionary of code (key) and descriptions (value)."""

# Imports
import csv


class CsvToDict:
    def __init__(self, csv_file_dir):
        self.csv_file_dir = csv_file_dir

    def run(self):
        #opens csv file
        with open(self.csv_file_dir) as file_object:
            
            # Create variables
            # this variable counts what row we are on in the csv file
            i = 0
            spec_option_dict = {}
            code_descr_dict = {}
            spec = ''

            # reads text from csv
            # data type csv_reader. seems similar to a list
            reader_object = csv.reader(file_object)
            
            
            # loops through each row of text. Row is in a list format
            for row in reader_object:

                # if the row only has one column then it is a spec. This is the outer dictionary
                if len(row) == 1:
                    
                    # if we are on the first spec a code_description dictionary hasn't been made yet
                    if i > 0:
                        spec_option_dict[spec] = code_descr_dict

                    # empties/creates code: description dictionary    
                    code_descr_dict = {}
                    
                    # set's the first column equal to spec
                    spec = row[0]

                elif len(row) == 2:
                    key, value = row[0], row[1]
                    code_descr_dict[key] = value

                else:
                    print(f'\nThe amount of cells in row {i} is too long.\n It should have the code in the first column and a description in the second.\n')

                # itterates row count of csv file    
                i += 1

            return spec_option_dict
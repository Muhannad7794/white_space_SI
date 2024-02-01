# parse the data from the csv file in the dta_files folder

import csv
import os
import pandas as pd


# read the csv file and return a list of lists
def read_csv_file(file_name):
    data = []
    with open(file_name, "r") as csv_file:
        reader = csv.reader(csv_file)
        # skip the header
        next(reader)
        for row in reader:
            data.append(row)
    return data


output = read_csv_file("data_files/anna.csv")
print(output)

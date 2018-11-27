# Script to read data from CSV file

import csv

with open("D:\Learning\Python\PycharmProjects\CSV_Reader\example.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[1])
        print(row[2])

import csv
with open("Day1/data/billionaires_list.csv") as file:
     data = csv.reader(file)
     for row in data:
         print(row)        
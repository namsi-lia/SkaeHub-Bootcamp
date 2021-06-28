import csv
with open("/home/namsi/Desktop/skaehub-dev-program/skaehub/Day1/data/billionaires_list.csv") as file:
     data = csv.reader(file)
     for row in data:
         print(row)        
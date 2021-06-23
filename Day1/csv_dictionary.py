import csv
with open('Day1/Data_Output/Billionaires_list.csv') as file:
     data = csv.reader(file)
     for row in data:
         print(row)
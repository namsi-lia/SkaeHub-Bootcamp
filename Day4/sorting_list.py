#code implementation to sort list of dictionaries using lambda


#sorting() lambda

#initialize dictionary:

Dicts = [{ "name" : "Al -Hussieni", "country" : "Saudia Arabia"},
{ "name" : "Leornado Da Vince", "country" : "Italy" },
{ "name" : "Anne-Hathaway" , "country" : "United Kingdom" }]
 
#print he list of dictinaries,sorted according to country:
print(sorted(Dicts, key = lambda item: item['country']))

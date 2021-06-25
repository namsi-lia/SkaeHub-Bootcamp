def max_min_tuples(cars):
    return_max = max(cars,key=lambda item:item[1])[1]
    return_min = min(cars,key=lambda item:item[1])[1]
    return return_max, return_min
cars = [('Toyota', 90862), ('BMW', 111168), ('Mercedes_Benz',877672), ('Volkswagen',211370), ('Audi',453674), ('Mazda',789321)]

print("\nMaximum and minimum values of the said list of tuples:")
print(max_min_tuples(cars))
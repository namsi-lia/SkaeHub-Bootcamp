#import module:numpy
import numpy as np


#declare the year and month
year = int(input("Enter year of choice:"))
month = int(input("Enter month of choice:"))


# is month within january to december
if int(month) < 12:
    next_month = int(month)+1

# if month is December
elif int(month) == 12:
    next_year = str(int(year)+1)
    
    next_month = 1
    next_month = str(f"{next_month:02}")

    number_weekdays = np.busday_count("{}-{}".format(year, month), "{}-{}".format(next_year, next_month)) 
    print("The number of weekdays in the month of {}-{} are: {}".format(year, month, number_weekdays))

    exit()

else:
    print("Enter months 1-12!")
    exit()

if int(month) <= 2:
    month = str(f"{int(month):02}")
    next_month = str(f"{next_month:02}")

number_weekdays = np.busday_count("{}-{}".format(year, month), "{}-{}".format(year, next_month)) 
print("The number of weekdays in the month of {}-{} are: {}".format(year, month, number_weekdays))
    

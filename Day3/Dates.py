# code to implement dates of Yesterday,Today,Tomorrow

# import module :numpy
import numpy as np

# Declare the dates
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow =np.datetime64('today', 'D') + np.timedelta64(1, 'D')

#Generate/print the output of the dates
print("Yesterday's date is:",yesterday)
print("Today's date is:",today)
print("Tomorrow's date is:",tomorrow)
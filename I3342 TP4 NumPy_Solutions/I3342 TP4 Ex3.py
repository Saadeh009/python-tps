# Write a NumPy program to display all the dates for the month of March, 2017.
# Use np.arrange with datetime type.

import numpy as np

start_date = np.datetime64('2017-03-01')
end_date = np.datetime64('2017-04-01')
dates = np.arange(start_date, end_date, dtype='datetime64[D]')

print(dates)
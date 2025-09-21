'''Class Topic 
1) create a list of data 
2) create a series from the list 
3) create a dataframe from the series 
4) dataframe convert series 
5) create a series for 2 integer columns 
6) create a dataframe from the list and rename the columns. 
7) create a series from the dataframe 
8) create a dictionary 
9) create a series from the dictionary 
10) 
set to series and dataframe 
Tuple to series and dataframe 
Data Types 
check a dataframe and check the data types 
Neumeric data types 
object 
datetime 
create a list of dates 
create a dataframe with a dataframe column 
check the data type of the date column 
pd.to_datetime(dates) 
series convert 
read Excel with xlsx 
read csv'''

h="Hello, \nFucking World"
print(h)

import pandas as pd
import numpy as np
#generate a list of 1-100
data = list(range(1,101))
print(data)

#maing series
Srs=pd.Series(data)
print(Srs)

df=pd.DataFrame(Srs)
print(df)
print(type(df))

#dataframe to series
srs2=df[0]
print(srs2)
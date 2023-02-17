import pandas as pd

#Extract Airport Data from website
list = pd.read_html("https://parksandtrips.com/closest-airport-to-every-us-national-park/")

#Convert List of Airport Data to pandas dataframe
df=pd.DataFrame(list[0])

#Save pandas dataframe as .csv
df.to_csv("DATA/Airports.csv")
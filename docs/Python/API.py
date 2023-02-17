import requests
import pandas as pd

api_key = "key goes here"

# take the identified request and convert the corresponding data to a Pandas DataFrame

def request_df(r: None):
  
  data = r.json()['data']
  df = pd.DataFrame(data)
  
  return(df)

# NPS API url for passing the API key via the GET query paramater

url = 'https://developer.nps.gov/api/v1/'

# Retrieve Park data in paginated requests of 200 rows, convert to pandas DataFrame, concatenate the paginated DataFrames together, and save as .csv

r1 = requests.get(url + "parks?limit=200&fields=entranceFees&fields=entrancePasses&fields=images&fields=operatingHours&api_key=" + api_key)
df1 = request_df(r1)

r2 = requests.get(url + "parks?start=201&limit=200&fields=entranceFees&fields=entrancePasses&fields=images&fields=operatingHours&api_key=" + api_key)
df2 = request_df(r2)

r3 = requests.get(url + "parks?start=401&limit=200&fields=entranceFees&fields=entrancePasses&fields=images&fields=operatingHours&api_key=" + api_key)
df3 = request_df(r3)

pd.concat([df1, df2, df3], axis=0).to_csv("DATA/Parks.csv")

#  Retrieve the most recent 400 Alerts in paginated requests of 200 rows, convert to pandas DataFrame, concatenate the paginated DataFrames together, and save as .csv

r1 = requests.get(url + "alerts?limit=200&api_key=" + api_key)
df1 = request_df(r1)

r2 = requests.get(url + "alerts?start=201&limit=200&api_key=" + api_key)
df2 = request_df(r2)

pd.concat([df1, df2], axis=0).to_csv("DATA/Alerts.csv")

# Retrieve all campgrounds in paginated requests of 200 rows, convert to pandas DataFrame, concatenate the paginated DataFrames together, and save as .csv

r1 = requests.get(url + "campgrounds?limit=200&api_key=" + api_key)
df1 = request_df(r1)

r2 = requests.get(url + "campgrounds?start=201limit=200&api_key=" + api_key)
df2 = request_df(r2)

r3 = requests.get(url + "campgrounds?start=401limit=200&api_key=" + api_key)
df3 = request_df(r3)

pd.concat([df1, df2, df3], axis=0).to_csv("DATA/Campgrounds.csv")

# Retrieve the most recent 100 News Releases, convert to pandas DataFrame, and save as .csv

r1 = requests.get(url+"newsreleases?limit=100&api_key=" + api_key)
df1 = request_df(r1)

df1.to_csv("DATA/News.csv")
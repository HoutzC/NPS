import pandas as pd
import requests
from bs4 import BeautifulSoup

# take the identified request and convert the corresponding data to a Pandas DataFrame

def request_df(r: None):
  
  data = r.json()['data']
  df = pd.DataFrame(data)
  
  return(df)

def Extract_From_Wiki(Park, wikiurl, table_class):
    response=requests.get(wikiurl)

    soup = BeautifulSoup(response.text, 'html.parser')
    ParkTable =soup.find('table',{'class':(table_class)})

    df=pd.read_html(str(ParkTable))
    df=pd.DataFrame(df[0])

    df['Count'] = range(1, len(df) + 1)
    df = df.set_index('Count')

    df.columns = ['Month', 'Jan', 'Feb', 'Mar', 'Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Year']

    value_list = ['Record high °F (°C)', 'Average high °F (°C)', 'Daily mean °F (°C)','Average low °F (°C)','Record low °F (°C)','Average precipitation inches (mm)','Average snowfall inches (cm)','Average precipitation days (≥ 0.01 in)']
    df = df[df['Month'].isin(value_list)]

    df = df.reindex(columns=['Month', 'Jan', 'Feb', 'Mar', 'Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Year'])
    df = df.set_index('Month')
    df_t=df.T
    df_t['Park'] = (Park)
    df_t.index.names = ['Month']
    df_t = df_t.reset_index().set_index('Park', inplace=False)

    if 'Average snowfall inches (cm)' not in df_t:
      df_t['Average snowfall inches (cm)'] = ''
    if 'Daily mean °F (°C)' not in df_t:
      df_t['Daily mean °F (°C)'] = ''
    if 'Average precipitation days (≥ 0.01 in)' not in df_t:
      df_t['Average precipitation days (≥ 0.01 in)'] = ''
  
    df_t = df_t.reindex(columns=['Month','Record high °F (°C)','Average high °F (°C)', 'Daily mean °F (°C)','Average low °F (°C)','Record low °F (°C)','Average precipitation inches (mm)','Average snowfall inches (cm)','Average precipitation days (≥ 0.01 in)'])

    df_t.columns = ['Month', 'Record high temp F', 'Average high temp F', 'Daily mean temp F', 'Average low temp F', ' Record Low Temp F', 'Average precipation IN', 'Average snowfall IN', 'Average precipation DAYS']
    
    return(df_t)

import os, glob
import pandas as pd

#Set path for folder containing annual Public Use Statistics Reports
path = "REPORTS\Visitor Statistics"

#Target all files that begin with "Public Use Statistics"
all_files = glob.glob(os.path.join(path, "Public Use Statistics*.csv"))

#loop through all target files and create individual dataframes for each
all_df = []
for f in all_files:
    df = pd.read_csv(f, sep=',')
    df['file'] = f.split('/')[-1]
    all_df.append(df)

#Concat all dataframes together into a Master Dataframe
MDF = pd.concat(all_df, ignore_index=True, sort=False)
#Clean Master Dataframe of uneeded columns to reduce size
MDF = MDF.drop(columns=['ParkNameTotal', 'UnitCodeTotal', 'RegionTotal', 'StateTotal', 'YearTotal', 'ParkTypeTotal' ,'file'])
#Save MAster Dataframe as csv to directory
MDF.to_csv("DATA/Visitation.csv")

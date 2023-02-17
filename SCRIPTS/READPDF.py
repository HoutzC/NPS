import tabula
import pandas as pd
import numpy as np

#For 2010 Extract tables from PDF to dataframe, concat all table dataframes into a single table, add a column to identify year, and clean the data
#Identify the year and file location
year= 2010
file = f'Reports/NPS_{year}_Visitor_Spending_Effects.pdf'

#Target tables in pdf and extract list + convert to df
pdf1 = tabula.read_pdf(file, lattice=True, pages=26, area=(98.303,71.0,724.838,552.185))
for df1 in pdf1:
    ()
pdf2 = tabula.read_pdf(file, lattice=True, pages=27, area=(105.953,71.0,724.838,552.185))
for df2 in pdf2:
    ()
pdf3 = tabula.read_pdf(file, lattice=True, pages=28, area=(105.953,71.0,724.838,552.185))
for df3 in pdf3:
    ()
pdf4 = tabula.read_pdf(file, lattice=True, pages=29, area=(105.953,71.0,724.838,552.185))
for df4 in pdf4:
    ()
pdf5 = tabula.read_pdf(file, lattice=True, pages=30, area=(105.953,71.0,724.838,552.185))
for df5 in pdf5:
    ()
pdf6 = tabula.read_pdf(file, lattice=True, pages=31, area=(105.953,71.0,724.838,552.185))
for df6 in pdf6:
    ()
pdf7 = tabula.read_pdf(file, lattice=True, pages=32, area=(105.953,71.0,724.838,552.185))
for df7 in pdf7:
    ()
pdf8 = tabula.read_pdf(file, lattice=True, pages=33, area=(105.953,71.0,733.253,552.185))
for df8 in pdf8:
    ()
pdf9 = tabula.read_pdf(file, lattice=True, pages=34, area=(105.953,71.0,616.208,552.185))
for df9 in pdf9:
    ()

#Combine Dataframes into a single dataframe
DF2010 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=0)

#Add a Year column identifying this year
DF2010['Year'] = (year)

#Clean Data
DF2010.drop(['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6'], inplace=True, axis=1)

#Overwrite all column names
DF2010.columns = ['Park Unit', 'Recreation Visits','Overnight Stays', 'All Visitors (K)', 'Non-Local Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Year']

DF2010.index = np.arange(1, len(DF2010) + 1)
DF2010 = DF2010.drop([280])

#Repeat for 2011
year= 2011
file = f'Reports/NPS_{year}_Visitor_Spending_Effects.pdf'

pdf1 = tabula.read_pdf(file, stream=True, pages=23, area=(99.833,75.353,733.253,540.473))
for df1 in pdf1:
    ()
pdf2 = tabula.read_pdf(file, stream=True, pages=24, area=(98.303,75.353,721.778,540.473))
for df2 in pdf2:
    ()
pdf3 = tabula.read_pdf(file, stream=True, pages=25, area=(99.833,75.353,724.073,540.473))
for df3 in pdf3:
    ()
pdf4 = tabula.read_pdf(file, stream=True, pages=26, area=(96.773,75.353,724.838,540.473))
for df4 in pdf4:
    ()
pdf5 = tabula.read_pdf(file, stream=True, pages=27, area=(99.068,75.353,724.073,540.473))
for df5 in pdf5:
    ()
pdf6 = tabula.read_pdf(file, stream=True, pages=28, area=(99.833,75.353,733.253,540.473))
for df6 in pdf6:
    ()
pdf7 = tabula.read_pdf(file, stream=True, pages=29, area=(99.833,75.353,724.073,540.473))
for df7 in pdf7:
    ()
pdf8 = tabula.read_pdf(file, stream=True, pages=30, area=(97.538,75.353,724.838,540.473))
for df8 in pdf8:
    ()
pdf9 = tabula.read_pdf(file, stream=True, pages=31, area=(99.068,76.118,218.408,538.943))
for df9 in pdf9:
    ()

DF2011 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=0)

DF2011['Year'] = (year)

DF2011.columns = ['Park Unit', 'Recreation Visits','Overnight Stays', 'All Visitors (K)', 'Non-Local Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Year']

N = 2
DF2011.drop(index=DF2011.index[:N], 
        axis=0, 
        inplace=True)

DF2011['Park Unit'] = DF2011['Park Unit'].replace(['NHS'],['Mary Mcleod Bethune Council House NHS'])
DF2011.index = np.arange(1, len(DF2011) + 1)
DF2011 = DF2011.drop([227])

#Repeat for 2012
year= 2012
file = f'Reports/NPS_{year}_Visitor_Spending_Effects.pdf'

pdf1 = tabula.read_pdf(file, lattice=True, pages=25, area=(135.788,66.173,711.068,549.653))
for df1 in pdf1:
    ()
pdf2 = tabula.read_pdf(file, lattice=True, pages=26, area=(88.358,66.173,719.483,549.653))
for df2 in pdf2:
    ()
pdf3 = tabula.read_pdf(file, lattice=True, pages=27, area=(88.358,66.173,719.483,549.653))
for df3 in pdf3:
    ()
pdf4 = tabula.read_pdf(file, lattice=True, pages=28, area=(88.358,66.173,719.483,549.653))
for df4 in pdf4:
    ()
pdf5 = tabula.read_pdf(file, lattice=True, pages=29, area=(88.358,66.173,719.483,549.653))
for df5 in pdf5:
    ()
pdf6 = tabula.read_pdf(file, lattice=True, pages=30, area=(88.358,66.173,717.188,549.653))
for df6 in pdf6:
    ()
pdf7 = tabula.read_pdf(file, lattice=True, pages=31, area=(88.358,66.173,717.188,549.653))
for df7 in pdf7:
    ()
pdf8 = tabula.read_pdf(file, lattice=True, pages=32, area=(88.358,66.173,715.658,549.653))
for df8 in pdf8:
    ()
pdf9 = tabula.read_pdf(file, lattice=True, pages=33, area=(88.358,66.173,719.483,549.653))
for df9 in pdf9:
    ()
pdf10 = tabula.read_pdf(file, lattice=True, pages=34, area=(88.358,66.173,225.293,549.653))
for df10 in pdf10:
    ()

DF2012 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], axis=0)

DF2012['Year'] = (year)

DF2012.columns = ['Park Unit', 'Recreation Visits','All Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)', 'Year']
DF2012['Overnight Stays'] = ''
DF2012['Non-Local Visitors (K)'] = ''
DF2012 = DF2012.reindex(columns=['Park Unit', 'Recreation Visits','Overnight Stays', 'All Visitors (K)', 'Non-Local Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)','Year'])

DF2012.index = np.arange(1, len(DF2012) + 1)

#Repeat for 2013
year= 2013
file = f'Reports/NPS_{year}_Visitor_Spending_Effects.pdf'

pdf1 = tabula.read_pdf(file, lattice=True, pages=25, area=(133.493,72.293,717.188,540.473))
for df1 in pdf1:
    ()
pdf2 = tabula.read_pdf(file, lattice=True, pages=26, area=(86.063,72.293,710.303,540.473))
for df2 in pdf2:
    ()
pdf3 = tabula.read_pdf(file, lattice=True, pages=27, area=(86.063,72.293,710.303,540.473))
for df3 in pdf3:
    ()
pdf4 = tabula.read_pdf(file, lattice=True, pages=28, area=(86.063,72.293,710.303,540.473))
for df4 in pdf4:
    ()
pdf5 = tabula.read_pdf(file, lattice=True, pages=29, area=(86.063,72.293,710.303,540.473))
for df5 in pdf5:
    ()
pdf6 = tabula.read_pdf(file, lattice=True, pages=30, area=(86.063,72.293,715.658,540.473))
for df6 in pdf6:
    ()
pdf7 = tabula.read_pdf(file, lattice=True, pages=31, area=(86.063,72.293,720.248,540.473))
for df7 in pdf7:
    ()
pdf8 = tabula.read_pdf(file, lattice=True, pages=32, area=(86.063,72.293,707.243,540.473))
for df8 in pdf8:
    ()
pdf9 = tabula.read_pdf(file, lattice=True, pages=33, area=(86.063,72.293,711.068,540.473))
for df9 in pdf9:
    ()
pdf10 = tabula.read_pdf(file, lattice=True, pages=34, area=(86.063,72.293,639.923,540.473))
for df10 in pdf10:
    ()

DF2013 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], axis=0)

DF2013['Year'] = (year)

DF2013.columns = ['Park Unit', 'Recreation Visits','All Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)', 'Year']
DF2013['Overnight Stays'] = ''
DF2013['Non-Local Visitors (K)'] = ''
DF2013 = DF2013.reindex(columns=['Park Unit', 'Recreation Visits','Overnight Stays', 'All Visitors (K)', 'Non-Local Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)','Year'])

DF2013.index = np.arange(1, len(DF2013) + 1)

#Repeat for 2014
year= 2014
file = f'Reports/NPS_{year}_Visitor_Spending_Effects.pdf'

pdf1 = tabula.read_pdf(file, lattice=True, pages=23, area=(135.788,68.468,728.663,542.003))
for df1 in pdf1:
    ()
pdf2 = tabula.read_pdf(file, lattice=True, pages=24, area=(88.358,68.468,728.663,542.003))
for df2 in pdf2:
    ()
pdf3 = tabula.read_pdf(file, lattice=True, pages=25, area=(88.358,68.468,728.663,542.003))
for df3 in pdf3:
    ()
pdf4 = tabula.read_pdf(file, lattice=True, pages=26, area=(88.358,68.468,728.663,542.003))
for df4 in pdf4:
    ()
pdf5 = tabula.read_pdf(file, lattice=True, pages=27, area=(88.358,68.468,728.663,542.003))
for df5 in pdf5:
    ()
pdf6 = tabula.read_pdf(file, lattice=True, pages=28, area=(88.358,68.468,728.663,542.003))
for df6 in pdf6:
    ()
pdf7 = tabula.read_pdf(file, lattice=True, pages=29, area=(88.358,68.468,728.663,542.003))
for df7 in pdf7:
    ()
pdf8 = tabula.read_pdf(file, lattice=True, pages=30, area=(88.358,68.468,728.663,542.003))
for df8 in pdf8:
    ()
pdf9 = tabula.read_pdf(file, lattice=True, pages=31, area=(88.358,68.468,728.663,542.003))
for df9 in pdf9:
    ()
pdf10 = tabula.read_pdf(file, lattice=True, pages=32, area=(88.358,68.468,536.648,542.003))
for df10 in pdf10:
    ()

DF2014 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], axis=0)

DF2014['Year'] = (year)

DF2014.columns = ['Park Unit', 'Recreation Visits','All Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)', 'Year']
DF2014['Overnight Stays'] = ''
DF2014['Non-Local Visitors (K)'] = ''
DF2014 = DF2014.reindex(columns=['Park Unit', 'Recreation Visits','Overnight Stays', 'All Visitors (K)', 'Non-Local Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)','Year'])

DF2014.index = np.arange(1, len(DF2014) + 1)

#Repeat for 2015
year= 2015
file = f'Reports/NPS_{year}_Visitor_Spending_Effects.pdf'

pdf1 = tabula.read_pdf(file, lattice=True, pages=22, area=(157.973,65.408,643.748,538.943))
for df1 in pdf1:
    ()
pdf2 = tabula.read_pdf(file, lattice=True, pages=23, area=(119.723,65.408,635.333,538.943))
for df2 in pdf2:
    ()
pdf3 = tabula.read_pdf(file, lattice=True, pages=24, area=(119.723,65.408,635.333,538.943))
for df3 in pdf3:
    ()
pdf4 = tabula.read_pdf(file, lattice=True, pages=25, area=(119.723,65.408,635.333,538.943))
for df4 in pdf4:
    ()
pdf5 = tabula.read_pdf(file, lattice=True, pages=26, area=(119.723,65.408,635.333,538.943))
for df5 in pdf5:
    ()
pdf6 = tabula.read_pdf(file, lattice=True, pages=27, area=(119.723,65.408,635.333,538.943))
for df6 in pdf6:
    ()
pdf7 = tabula.read_pdf(file, lattice=True, pages=28, area=(119.723,65.408,635.333,538.943))
for df7 in pdf7:
    ()
pdf8 = tabula.read_pdf(file, lattice=True, pages=29, area=(119.723,65.408,635.333,538.943))
for df8 in pdf8:
    ()
pdf9 = tabula.read_pdf(file, lattice=True, pages=30, area=(119.723,65.408,626.918,538.943))
for df9 in pdf9:
    ()
pdf10 = tabula.read_pdf(file, lattice=True, pages=31, area=(119.723,65.408,626.918,538.943))
for df10 in pdf10:
    ()
pdf11 = tabula.read_pdf(file, lattice=True, pages=32, area=(119.723,65.408,626.918,538.943))
for df11 in pdf10:
    ()
pdf12 = tabula.read_pdf(file, lattice=True, pages=33, area=(119.723,65.408,626.918,538.943))
for df12 in pdf10:
    ()
pdf13 = tabula.read_pdf(file, lattice=True, pages=34, area=(119.723,65.408,626.918,538.943))
for df13 in pdf10:
    ()
pdf14 = tabula.read_pdf(file, lattice=True, pages=35, area=(119.723,65.408,626.918,538.943))
for df14 in pdf10:
    ()
pdf15 = tabula.read_pdf(file, lattice=True, pages=36, area=(119.723,65.408,626.918,538.943))
for df15 in pdf10:
    ()
pdf16 = tabula.read_pdf(file, lattice=True, pages=37, area=(119.723,65.408,249.773,538.943))
for df16 in pdf10:
    ()

DF2015 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16], axis=0)

DF2015['Year'] = (year)

DF2015.columns = ['Park Unit', 'Recreation Visits','All Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)', 'Year']
DF2015['Overnight Stays'] = ''
DF2015['Non-Local Visitors (K)'] = ''
DF2015 = DF2015.reindex(columns=['Park Unit', 'Recreation Visits','Overnight Stays', 'All Visitors (K)', 'Non-Local Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)','Year'])

DF2015.index = np.arange(1, len(DF2015) + 1)

#REpeat for 2016
year= 2016
file = f'Reports/NPS_{year}_Visitor_Spending_Effects.pdf'

pdf1 = tabula.read_pdf(file, lattice=True, pages=26, area=(143.438,62.348,619.268,547.358))
for df1 in pdf1:
    ()
pdf2 = tabula.read_pdf(file, lattice=True, pages=27, area=(118.193,62.348,610.088,547.358))
for df2 in pdf2:
    ()
pdf3 = tabula.read_pdf(file, lattice=True, pages=28, area=(118.193,62.348,636.098,547.358))
for df3 in pdf3:
    ()
pdf4 = tabula.read_pdf(file, lattice=True, pages=29, area=(118.193,62.348,636.098,547.358))
for df4 in pdf4:
    ()
pdf5 = tabula.read_pdf(file, lattice=True, pages=30, area=(118.193,62.348,636.098,547.358))
for df5 in pdf5:
    ()
pdf6 = tabula.read_pdf(file, lattice=True, pages=31, area=(118.193,62.348,642.218,547.358))
for df6 in pdf6:
    ()
pdf7 = tabula.read_pdf(file, lattice=True, pages=32, area=(118.193,62.348,636.863,547.358))
for df7 in pdf7:
    ()
pdf8 = tabula.read_pdf(file, lattice=True, pages=33, area=(118.193,62.348,642.218,547.358))
for df8 in pdf8:
    ()
pdf9 = tabula.read_pdf(file, lattice=True, pages=34, area=(118.193,62.348,642.218,547.358))
for df9 in pdf9:
    ()
pdf10 = tabula.read_pdf(file, lattice=True, pages=35, area=(118.193,62.348,642.218,547.358))
for df10 in pdf10:
    ()
pdf11 = tabula.read_pdf(file, lattice=True, pages=36, area=(118.193,62.348,648.338,547.358))
for df11 in pdf10:
    ()
pdf12 = tabula.read_pdf(file, lattice=True, pages=37, area=(118.193,62.348,636.863,547.358))
for df12 in pdf10:
    ()
pdf13 = tabula.read_pdf(file, lattice=True, pages=38, area=(118.193,62.348,640.688,547.358))
for df13 in pdf10:
    ()
pdf14 = tabula.read_pdf(file, lattice=True, pages=39, area=(118.193,62.348,274.253,547.358))
for df14 in pdf10:
    ()

DF2016 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14], axis=0)

DF2016['Year'] = (year)

DF2016.columns = ['Park Unit', 'Recreation Visits','All Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)', 'Year']
DF2016['Overnight Stays'] = ''
DF2016['Non-Local Visitors (K)'] = ''
DF2016 = DF2016.reindex(columns=['Park Unit', 'Recreation Visits','Overnight Stays', 'All Visitors (K)', 'Non-Local Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)','Year'])

DF2016.index = np.arange(1, len(DF2016) + 1)

#Repeat for 2017
year= 2017
file = f'Reports/NPS_{year}_Visitor_Spending_Effects.pdf'

pdf1 = tabula.read_pdf(file, lattice=True, pages=25, area=(127.373,68.468,639.158,536.648))
for df1 in pdf1:
    ()
pdf2 = tabula.read_pdf(file, lattice=True, pages=26, area=(87.593,68.468,639.158,536.648))
for df2 in pdf2:
    ()
pdf3 = tabula.read_pdf(file, lattice=True, pages=27, area=(87.593,68.468,653.693,536.648))
for df3 in pdf3:
    ()
pdf4 = tabula.read_pdf(file, lattice=True, pages=28, area=(87.593,68.468,621.563,536.648))
for df4 in pdf4:
    ()
pdf5 = tabula.read_pdf(file, lattice=True, pages=29, area=(87.593,68.468,636.863,536.648))
for df5 in pdf5:
    ()
pdf6 = tabula.read_pdf(file, lattice=True, pages=30, area=(87.593,68.468,623.093,536.648))
for df6 in pdf6:
    ()
pdf7 = tabula.read_pdf(file, lattice=True, pages=31, area=(87.593,68.468,636.863,536.648))
for df7 in pdf7:
    ()
pdf8 = tabula.read_pdf(file, lattice=True, pages=32, area=(87.593,68.468,645.278,536.648))
for df8 in pdf8:
    ()
pdf9 = tabula.read_pdf(file, lattice=True, pages=33, area=(87.593,68.468,636.098,536.648))
for df9 in pdf9:
    ()
pdf10 = tabula.read_pdf(file, lattice=True, pages=34, area=(87.593,68.468,646.043,536.648))
for df10 in pdf10:
    ()
pdf11 = tabula.read_pdf(file, lattice=True, pages=35, area=(87.593,68.468,638.393,536.648))
for df11 in pdf10:
    ()
pdf12 = tabula.read_pdf(file, lattice=True, pages=36, area=(87.593,68.468,638.393,536.648))
for df12 in pdf10:
    ()
pdf13 = tabula.read_pdf(file, lattice=True, pages=37, area=(87.593,68.468,414.248,536.648))
for df13 in pdf10:
    ()

DF2017 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13,], axis=0)

DF2017['Year'] = (year)

DF2017.columns = ['Park Unit', 'Recreation Visits','All Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)', 'Year']
DF2017['Overnight Stays'] = ''
DF2017['Non-Local Visitors (K)'] = ''
DF2017 = DF2017.reindex(columns=['Park Unit', 'Recreation Visits','Overnight Stays', 'All Visitors (K)', 'Non-Local Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)','Year'])

DF2017.index = np.arange(1, len(DF2017) + 1)

#Repeat for 2018
year= 2018
file = f'Reports/NPS_{year}_Visitor_Spending_Effects.pdf'

pdf1 = tabula.read_pdf(file, lattice=True, pages=26, area=(129.195,69.795,482.625,725.175))
for df1 in pdf1:
    ()
pdf2 = tabula.read_pdf(file, lattice=True, pages=27, area=(87.615,69.795,481.635,725.175))
for df2 in pdf2:
    ()
pdf3 = tabula.read_pdf(file, lattice=True, pages=28, area=(87.615,69.795,481.635,725.175))
for df3 in pdf3:
    ()
pdf4 = tabula.read_pdf(file, lattice=True, pages=29, area=(87.615,69.795,481.635,725.175))
for df4 in pdf4:
    ()
pdf5 = tabula.read_pdf(file, lattice=True, pages=30, area=(87.615,69.795,481.635,725.175))
for df5 in pdf5:
    ()
pdf6 = tabula.read_pdf(file, lattice=True, pages=31, area=(87.615,69.795,481.635,725.175))
for df6 in pdf6:
    ()
pdf7 = tabula.read_pdf(file, lattice=True, pages=32, area=(87.615,69.795,481.635,725.175))
for df7 in pdf7:
    ()
pdf8 = tabula.read_pdf(file, lattice=True, pages=33, area=(87.615,69.795,481.635,725.175))
for df8 in pdf8:
    ()
pdf9 = tabula.read_pdf(file, lattice=True, pages=34, area=(87.615,69.795,481.635,725.175))
for df9 in pdf9:
    ()
pdf10 = tabula.read_pdf(file, lattice=True, pages=35, area=(87.615,69.795,481.635,725.175))
for df10 in pdf10:
    ()
pdf11 = tabula.read_pdf(file, lattice=True, pages=36, area=(87.615,69.795,481.635,725.175))
for df11 in pdf11:
    ()
pdf12 = tabula.read_pdf(file, lattice=True, pages=37, area=(87.615,69.795,481.635,725.175))
for df12 in pdf12:
    ()
pdf13 = tabula.read_pdf(file, lattice=True, pages=38, area=(87.615,69.795,481.635,725.175))
for df13 in pdf13:
    ()
pdf14 = tabula.read_pdf(file, lattice=True, pages=39, area=(87.615,69.795,481.635,725.175))
for df14 in pdf14:
    ()
pdf15 = tabula.read_pdf(file, lattice=True, pages=40, area=(87.615,69.795,481.635,725.175))
for df15 in pdf15:
    ()
pdf16 = tabula.read_pdf(file, lattice=True, pages=41, area=(87.615,69.795,481.635,725.175))
for df16 in pdf16:
    ()
pdf17 = tabula.read_pdf(file, lattice=True, pages=42, area=(87.615,69.795,481.635,725.175))
for df17 in pdf17:
    ()
pdf18 = tabula.read_pdf(file, lattice=True, pages=43, area=(87.615,69.795,481.635,725.175))
for df18 in pdf18:
    ()
pdf19 = tabula.read_pdf(file, lattice=True, pages=44, area=(87.615,69.795,481.635,725.175))
for df19 in pdf19:
    ()

DF2018 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19], axis=0)

DF2018['Year'] = (year)

DF2018.columns = ['Park Unit', 'Recreation Visits','All Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)', 'Year']
DF2018['Overnight Stays'] = ''
DF2018['Non-Local Visitors (K)'] = ''
DF2018 = DF2018.reindex(columns=['Park Unit', 'Recreation Visits','Overnight Stays', 'All Visitors (K)', 'Non-Local Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)','Year'])

DF2018.index = np.arange(1, len(DF2018) + 1)

#Repeat for 2019
year= 2019
file = f'Reports/NPS_{year}_Visitor_Spending_Effects.pdf'

pdf1 = tabula.read_pdf(file, lattice=True, pages=24, area=(80.685,68.805,545.985,746.955))
for df1 in pdf1:
    ()
pdf2 = tabula.read_pdf(file, lattice=True, pages=25, area=(80.685,68.805,545.985,746.955))
for df2 in pdf2:
    ()
pdf3 = tabula.read_pdf(file, lattice=True, pages=26, area=(80.685,68.805,545.985,746.955))
for df3 in pdf3:
    ()
pdf4 = tabula.read_pdf(file, lattice=True, pages=27, area=(80.685,68.805,545.985,746.955))
for df4 in pdf4:
    ()
pdf5 = tabula.read_pdf(file, lattice=True, pages=28, area=(80.685,68.805,545.985,746.955))
for df5 in pdf5:
    ()
pdf6 = tabula.read_pdf(file, lattice=True, pages=29, area=(80.685,68.805,545.985,746.955))
for df6 in pdf6:
    ()
pdf7 = tabula.read_pdf(file, lattice=True, pages=30, area=(80.685,68.805,545.985,746.955))
for df7 in pdf7:
    ()
pdf8 = tabula.read_pdf(file, lattice=True, pages=31, area=(80.685,68.805,545.985,746.955))
for df8 in pdf8:
    ()
pdf9 = tabula.read_pdf(file, lattice=True, pages=32, area=(80.685,68.805,545.985,746.955))
for df9 in pdf9:
    ()
pdf10 = tabula.read_pdf(file, lattice=True, pages=33, area=(80.685,68.805,545.985,746.955))
for df10 in pdf10:
    ()
pdf11 = tabula.read_pdf(file, lattice=True, pages=34, area=(80.685,68.805,545.985,746.955))
for df11 in pdf11:
    ()
pdf12 = tabula.read_pdf(file, lattice=True, pages=35, area=(80.685,68.805,545.985,746.955))
for df12 in pdf12:
    ()
pdf13 = tabula.read_pdf(file, lattice=True, pages=36, area=(80.685,68.805,545.985,746.955))
for df13 in pdf13:
    ()
pdf14 = tabula.read_pdf(file, lattice=True, pages=37, area=(80.685,68.805,545.985,746.955))
for df14 in pdf14:
    ()
pdf15 = tabula.read_pdf(file, lattice=True, pages=38, area=(80.685,68.805,545.985,746.955))
for df15 in pdf15:
    ()
pdf16 = tabula.read_pdf(file, lattice=True, pages=39, area=(80.685,68.805,545.985,746.955))
for df16 in pdf16:
    ()
pdf17 = tabula.read_pdf(file, lattice=True, pages=40, area=(80.685,68.805,545.985,746.955))
for df17 in pdf17:
    ()
pdf18 = tabula.read_pdf(file, lattice=True, pages=41, area=(80.685,68.805,545.985,746.955))
for df18 in pdf18:
    ()

DF2019 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18], axis=0)

DF2019['Year'] = (year)

DF2019.columns = ['Park Unit', 'Recreation Visits','All Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)', 'Year']
DF2019['Overnight Stays'] = ''
DF2019['Non-Local Visitors (K)'] = ''
DF2019 = DF2019.reindex(columns=['Park Unit', 'Recreation Visits','Overnight Stays', 'All Visitors (K)', 'Non-Local Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)','Year'])

DF2019.index = np.arange(1, len(DF2019) + 1)

#Repeat for 2020
year= 2020
file = f'Reports/NPS_{year}_Visitor_Spending_Effects.pdf'

pdf1 = tabula.read_pdf(file, stream=True, pages=26, area=(128.205,73.755,453.915,708.345))
for df1 in pdf1:
    ()
pdf2 = tabula.read_pdf(file, stream=True, pages=27, area=(87.615,73.755,479.655,708.345))
for df2 in pdf2:
    ()
pdf3 = tabula.read_pdf(file, stream=True, pages=28, area=(87.615,73.755,467.775,708.345))
for df3 in pdf3:
    ()
pdf4 = tabula.read_pdf(file, stream=True, pages=29, area=(87.615,73.755,467.775,708.345))
for df4 in pdf4:
    ()
pdf5 = tabula.read_pdf(file, stream=True, pages=30, area=(87.615,73.755,467.775,708.345))
for df5 in pdf5:
    ()
pdf6 = tabula.read_pdf(file, stream=True, pages=31, area=(87.615,73.755,467.775,708.345))
for df6 in pdf6:
    ()
pdf7 = tabula.read_pdf(file, stream=True, pages=32, area=(87.615,73.755,467.775,708.345))
for df7 in pdf7:
    ()
pdf8 = tabula.read_pdf(file, stream=True, pages=33, area=(87.615,73.755,467.775,708.345))
for df8 in pdf8:
    ()
pdf9 = tabula.read_pdf(file, stream=True, pages=34, area=(87.615,73.755,467.775,708.345))
for df9 in pdf9:
    ()
pdf10 = tabula.read_pdf(file, stream=True, pages=35, area=(87.615,73.755,467.775,708.345))
for df10 in pdf10:
    ()
pdf11 = tabula.read_pdf(file, stream=True, pages=36, area=(87.615,73.755,467.775,708.345))
for df11 in pdf11:
    ()
pdf12 = tabula.read_pdf(file, stream=True, pages=37, area=(87.615,73.755,467.775,708.345))
for df12 in pdf12:
    ()
pdf13 = tabula.read_pdf(file, stream=True, pages=38, area=(87.615,73.755,467.775,708.345))
for df13 in pdf13:
    ()
pdf14 = tabula.read_pdf(file, stream=True, pages=39, area=(87.615,73.755,467.775,708.345))
for df14 in pdf14:
    ()
pdf15 = tabula.read_pdf(file, stream=True, pages=40, area=(87.615,73.755,467.775,708.345))
for df15 in pdf15:
    ()
pdf16 = tabula.read_pdf(file, stream=True, pages=41, area=(87.615,73.755,455.895,708.345))
for df16 in pdf16:
    ()
pdf17 = tabula.read_pdf(file, stream=True, pages=42, area=(87.615,73.755,459.855,708.345))
for df17 in pdf17:
    ()
pdf18 = tabula.read_pdf(file, stream=True, pages=43, area=(87.615,73.755,466.785,708.345))
for df18 in pdf18:
    ()
pdf19 = tabula.read_pdf(file, stream=True, pages=44, area=(87.615,73.755,466.785,708.345))
for df19 in pdf19:
    ()
pdf20 = tabula.read_pdf(file, stream=True, pages=45, area=(87.615,73.755,449.955,708.345))
for df20 in pdf20:
    ()
pdf21 = tabula.read_pdf(file, stream=True, pages=46, area=(87.615,73.755,408.375,708.345))
for df21 in pdf21:
    ()

DF2020 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21], axis=0)

DF2020['Year'] = (year)

DF2020.columns = ['Park Unit', 'Recreation Visits','All Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)', 'Year']
DF2020['Overnight Stays'] = ''
DF2020['Non-Local Visitors (K)'] = ''
DF2020 = DF2020.reindex(columns=['Park Unit', 'Recreation Visits','Overnight Stays', 'All Visitors (K)', 'Non-Local Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)','Year'])

DF2020.index = np.arange(1, len(DF2020) + 1)

DF2020 = DF2020.drop([1, 2, 19, 20, 22, 41, 42, 62, 63, 83, 84, 104, 105, 125, 126, 146, 147, 167, 168, 188, 189, 209, 210, 230, 231, 251, 252, 254, 259, 268, 273, 274, 294, 295, 315, 316, 319, 332, 336, 337, 347, 357, 358, 378, 379, 399, 400, 419, 420, 426])
DF2020['Park Unit'] = DF2020['Park Unit'].replace(['Arlington House, The Robert E.Lee','Lyndon Baines Johnson Memorial','Manhattan Project (New Mexico)','Mary McLeod Bethune Council',"Perry's Victory & International Peace", 'President William Jefferson Clinton','Rosie the Riveter WWII Home Front','Wolf Trap National Park for the'],['Arlington House, The Robert E.Lee Memorial NMEMc','Lyndon Baines Johnson Memorial Grove on the Potomac NMEM','Manhattan Project (New Mexico) NHP','Mary McLeod Bethune Council House NHS',"Perry's Victory & International Peace MEMa",'President William Jefferson Clinton Birthplace Home NHS','Rosie the Riveter WWII Home Front NHP','Wolf Trap National Park for the Performing Arts'])
DF2020.index = np.arange(1, len(DF2020) + 1)

#Repeat for 2021
year= 2021
file = f'Reports/NPS_{year}_Visitor_Spending_Effects.pdf'

pdf1 = tabula.read_pdf(file, stream=True, pages=26, area=(129.195,72.765,470.745,714.285))
for df1 in pdf1:
    ()
pdf2 = tabula.read_pdf(file, stream=True, pages=27, area=(88.605,72.765,482.625,714.285))
for df2 in pdf2:
    ()
pdf3 = tabula.read_pdf(file, stream=True, pages=28, area=(88.605,72.765,469.755,714.285))
for df3 in pdf3:
    ()
pdf4 = tabula.read_pdf(file, stream=True, pages=29, area=(88.605,72.765,469.755,714.285))
for df4 in pdf4:
    ()
pdf5 = tabula.read_pdf(file, stream=True, pages=30, area=(88.605,72.765,469.755,714.285))
for df5 in pdf5:
    ()
pdf6 = tabula.read_pdf(file, stream=True, pages=31, area=(88.605,72.765,469.755,714.285))
for df6 in pdf6:
    ()
pdf7 = tabula.read_pdf(file, stream=True, pages=32, area=(88.605,72.765,469.755,714.285))
for df7 in pdf7:
    ()
pdf8 = tabula.read_pdf(file, stream=True, pages=33, area=(88.605,72.765,469.755,714.285))
for df8 in pdf8:
    ()
pdf9 = tabula.read_pdf(file, stream=True, pages=34, area=(88.605,72.765,469.755,714.285))
for df9 in pdf9:
    ()
pdf10 = tabula.read_pdf(file, stream=True, pages=35, area=(88.605,72.765,469.755,714.285))
for df10 in pdf10:
    ()
pdf11 = tabula.read_pdf(file, stream=True, pages=36, area=(88.605,72.765,469.755,714.285))
for df11 in pdf11:
    ()
pdf12 = tabula.read_pdf(file, stream=True, pages=37, area=(88.605,72.765,469.755,714.285))
for df12 in pdf12:
    ()
pdf13 = tabula.read_pdf(file, stream=True, pages=38, area=(88.605,72.765,469.755,714.285))
for df13 in pdf13:
    ()
pdf14 = tabula.read_pdf(file, stream=True, pages=39, area=(88.605,72.765,462.825,714.285))
for df14 in pdf14:
    ()
pdf15 = tabula.read_pdf(file, stream=True, pages=40, area=(88.605,72.765,470.745,714.285))
for df15 in pdf15:
    ()
pdf16 = tabula.read_pdf(file, stream=True, pages=41, area=(88.605,72.765,470.745,714.285))
for df16 in pdf16:
    ()
pdf17 = tabula.read_pdf(file, stream=True, pages=42, area=(88.605,72.765,470.745,714.285))
for df17 in pdf17:
    ()
pdf18 = tabula.read_pdf(file, stream=True, pages=43, area=(88.605,72.765,462.825,714.285))
for df18 in pdf18:
    ()
pdf19 = tabula.read_pdf(file, stream=True, pages=44, area=(88.605,72.765,470.745,714.285))
for df19 in pdf19:
    ()
pdf20 = tabula.read_pdf(file, stream=True, pages=45, area=(88.605,72.765,470.745,714.285))
for df20 in pdf20:
    ()
pdf21 = tabula.read_pdf(file, stream=True, pages=46, area=(88.605,72.765,470.745,714.285))
for df21 in pdf21:
    ()
pdf22 = tabula.read_pdf(file, stream=True, pages=47, area=(88.605,72.765,470.745,714.285))
for df22 in pdf22:
    ()
pdf23 = tabula.read_pdf(file, stream=True, pages=48, area=(88.605,72.765,470.745,714.285))
for df23 in pdf23:
    ()
pdf24 = tabula.read_pdf(file, stream=True, pages=49, area=(88.605,72.765,215.325,714.285))
for df24 in pdf24:
    ()

DF2021 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21, df22, df23, df24], axis=0)

DF2021['Year'] = (year)

DF2021.columns = ['Park Unit', 'Recreation Visits','All Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)', 'Year']
DF2021['Overnight Stays'] = ''
DF2021['Non-Local Visitors (K)'] = ''
DF2021 = DF2021.reindex(columns=['Park Unit', 'Recreation Visits','Overnight Stays', 'All Visitors (K)', 'Non-Local Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)','Year'])

DF2021.index = np.arange(1, len(DF2021) + 1)

DF2021 = DF2021.drop([1, 2, 18, 19, 23, 38, 39, 57, 58, 76, 77, 95, 96, 114, 115, 133, 134, 152, 153, 171, 172, 190, 191, 209, 210, 228, 229, 247, 248, 258, 266, 267, 285, 286, 304, 305, 323, 324, 336, 342, 343, 361, 362, 380, 381, 399, 400, 418, 419, 430, 437, 438])
DF2021['Park Unit'] = DF2021['Park Unit'].replace(['Arlington House, The Robert E.Lee','Lyndon Baines Johnson Memorial Grove', 'President William Jefferson Clinton Birthplace','Wolf Trap National Park for the Performing'],['Arlington House, The Robert E.Lee Memorial NMEMc','Lyndon Baines Johnson Memorial Grove on the Potomac NMEM','President William Jefferson Clinton Birthplace Home NHS','Wolf Trap National Park for the Performing Arts'])
DF2021.index = np.arange(1, len(DF2021) + 1)

DF2021.index = np.arange(1, len(DF2021) + 1)

#Create a master dataframe (MDF) by combining each files final data frame
MDF = pd.concat([DF2010, DF2011, DF2012, DF2013, DF2014, DF2015, DF2016, DF2017, DF2018, DF2019, DF2020, DF2021], axis=0)

#Clean Data in MDF
MDF['Park Unit'] = MDF['Park Unit'].str.replace('*', '', regex=True)
MDF.index = np.arange(1, len(MDF) + 1)
MDF = MDF.reindex(columns=['Year','Park Unit', 'Recreation Visits','Overnight Stays', 'All Visitors (K)', 'Non-Local Visitors (K)', 'Jobs', 'Labor Income (K)', 'Value Added (K)', 'Output (K)'])

MDF.to_csv("DATA/Economic_Impact_Data.csv")

print("Report Completed")

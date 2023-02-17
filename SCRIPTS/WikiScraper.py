import pandas as pd
import requests
from bs4 import BeautifulSoup
from Utils import Extract_From_Wiki

Park= "Acadia National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Acadia_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = df_t

#
Park= "Arches National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Arches_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Badlands National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Badlands_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Big Bend National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Big_Bend_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Biscayne National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Biscayne_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Black Canyon of the Gunnison National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Black_Canyon_of_the_Gunnison_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Bryce Canyon National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Bryce_Canyon_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Canyonlands National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Canyonlands_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Capitol Reef National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Capitol_Reef_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Carlsbad Caverns National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Carlsbad_Caverns_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Channel Islands National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Channel_Islands_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Congaree National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Congaree_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Crater Lake National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Crater_Lake_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Cuyahoga National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Cuyahoga_Valley_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Denali National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Denali_National_Park_and_Preserve")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Death Valley National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Death_Valley_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Denali National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Denali_National_Park_and_Preserve")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Dry Tortugas National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Dry_Tortugas_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Everglades National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Everglades_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Glacier National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Glacier_National_Park_(U.S.)")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Glacier Bay National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Glacier_Bay_National_Park_and_Preserve")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Grand Canyon National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Grand_Canyon_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Grand Teton National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Grand_Teton_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Great Basin National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Great_Basin_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Great Sand Dunes National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Great_Sand_Dunes_National_Park_and_Preserve")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Great Smokey Mountains National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Great_Smoky_Mountains_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Guadalupe Mountains National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Guadalupe_Mountains_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Haleakalā National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Haleakal%C4%81_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Hawaiʻi Volcanoes National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Hawai%CA%BBi_Volcanoes_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Hot Springs National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Hot_Springs_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Indiana Dunes National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Indiana_Dunes_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Isle Royale National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Isle_Royale_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Joshua Tree National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Joshua_Tree_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Kenai Fjords National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Kenai_Fjords_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Kings Canyon National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Kings_Canyon_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Mammoth Cave National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Mammoth_Cave_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Mesa Verde National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Mesa_Verde_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Mount Rainier National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Mount_Rainier_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "North Cascades National Park"
wikiurl = ("https://en.wikipedia.org/wiki/North_Cascades_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Olympic National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Olympic_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Petrified Forest National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Petrified_Forest_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Pinnacles National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Pinnacles_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Redwood National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Redwood_National_and_State_Parks")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Saguaro National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Saguaro_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Shenandoah National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Shenandoah_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Voyageurs National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Voyageurs_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "White Sands National Park"
wikiurl = ("https://en.wikipedia.org/wiki/White_Sands_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Wind Cave National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Wind_Cave_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Wrangell–St. Elias National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Wrangell%E2%80%93St._Elias_National_Park_and_Preserve")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)

#
Park= "Zion National Park"
wikiurl = ("https://en.wikipedia.org/wiki/Zion_National_Park")
table_class="wikitable mw-collapsible"

df_t = Extract_From_Wiki(Park, wikiurl, table_class)
DFM = pd.concat([DFM, df_t], axis =0)


DFM = DFM.replace(r"\(.*\)","",regex=True)
DFM = DFM.replace("−","-",regex=True)
DFM = DFM.replace("trace",'',regex=True)

DFM.to_csv("DATA/WeatherData.csv")

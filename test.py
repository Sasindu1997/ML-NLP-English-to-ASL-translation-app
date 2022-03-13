import codecs

import xarray as xr
import pandas as pd
import os
from pprint import pprint
import json

# inputFile = os.path.abspath("C:/Users/Acer/PycharmProjects/tfModel/Dataset/maize/yield_1981.nc4")
# outputFile = os.path.abspath("C:/Users/Acer/PycharmProjects/tfModel/test.csv")
#
# data = xr.open_dataset(inputFile)
# data_df = data.to_dataframe().reset_index()
# data_df.to_csv(outputFile)

#
sentences = []
data = []
with codecs.open('IMDB.json', 'r', 'utf-8') as f:
    for item in f:
        pprint(item)

# df = pd.read_json('IMDB.json', lines=True)
# pprint(df['plot_synopsis'])
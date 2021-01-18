import pandas as pd
import plotly.express as px
import hashlib
import hmac
import json
import requests
from bitkub import Bitkub
# ### please INSTALL LIB. # ###
#   pip install bitkub
# ### please INSTALL LIB. # ###

#import csv
df = pd.read_csv("sell10.csv")
#get value from csv 
print(df.head(10))   #show 10 row   --row 0-9  is  row 1- 10s
print('-----END PRINT File---sell10--' )   


# API info
API_HOST = 'https://api.bitkub.com'
API_KEY = 'xxxxx'
API_SECRET = b'xxxxx'


bitkub = Bitkub()
bitkub.set_api_key(API_KEY)
bitkub.set_api_secret(API_SECRET)


print('SELL')
print(bitkub.place_ask(sym=df['unit'][0], amt=df['y'][0], rat=df['x'][0], typ='limit'))   #SELL
print(bitkub.place_ask(sym=df['unit'][1], amt=df['y'][1], rat=df['x'][1], typ='limit'))   #SELL
print(bitkub.place_ask(sym=df['unit'][2], amt=df['y'][2], rat=df['x'][2], typ='limit'))   #SELL
print(bitkub.place_ask(sym=df['unit'][3], amt=df['y'][3], rat=df['x'][3], typ='limit'))   #SELL
print(bitkub.place_ask(sym=df['unit'][4], amt=df['y'][4], rat=df['x'][4], typ='limit'))   #SELL
print(bitkub.place_ask(sym=df['unit'][5], amt=df['y'][5], rat=df['x'][5], typ='limit'))   #SELL
print(bitkub.place_ask(sym=df['unit'][6], amt=df['y'][6], rat=df['x'][7], typ='limit'))   #SELL
print(bitkub.place_ask(sym=df['unit'][7], amt=df['y'][7], rat=df['x'][8], typ='limit'))   #SELL
print(bitkub.place_ask(sym=df['unit'][8], amt=df['y'][8], rat=df['x'][8], typ='limit'))   #SELL
print(bitkub.place_ask(sym=df['unit'][9], amt=df['y'][9], rat=df['x'][9], typ='limit'))   #SELLs

print('Place SELL Order complete')
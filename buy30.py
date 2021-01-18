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
df = pd.read_csv("buy30.csv")
#get value from csv 
print(df.head(30))   #show 30 row   --row 0-29  is  row 1- 30
print('-----END PRINT File---buy30--' )   


# API info
API_HOST = 'https://api.bitkub.com'
API_KEY = 'xxxxx'
API_SECRET = b'xxxxx'


bitkub = Bitkub()
bitkub.set_api_key(API_KEY)
bitkub.set_api_secret(API_SECRET)


print('Buy')
print(bitkub.place_bid(sym=df['unit'][0], amt=df['y'][0], rat=df['x'][0], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][1], amt=df['y'][1], rat=df['x'][1], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][2], amt=df['y'][2], rat=df['x'][2], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][3], amt=df['y'][3], rat=df['x'][3], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][4], amt=df['y'][4], rat=df['x'][4], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][5], amt=df['y'][5], rat=df['x'][5], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][6], amt=df['y'][6], rat=df['x'][7], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][7], amt=df['y'][7], rat=df['x'][8], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][8], amt=df['y'][8], rat=df['x'][8], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][9], amt=df['y'][9], rat=df['x'][9], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][10], amt=df['y'][10], rat=df['x'][10], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][11], amt=df['y'][11], rat=df['x'][11], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][12], amt=df['y'][12], rat=df['x'][12], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][13], amt=df['y'][13], rat=df['x'][13], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][14], amt=df['y'][14], rat=df['x'][14], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][15], amt=df['y'][15], rat=df['x'][15], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][16], amt=df['y'][16], rat=df['x'][16], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][17], amt=df['y'][17], rat=df['x'][17], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][18], amt=df['y'][18], rat=df['x'][18], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][19], amt=df['y'][19], rat=df['x'][19], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][20], amt=df['y'][20], rat=df['x'][20], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][21], amt=df['y'][21], rat=df['x'][21], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][22], amt=df['y'][22], rat=df['x'][22], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][23], amt=df['y'][23], rat=df['x'][23], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][24], amt=df['y'][24], rat=df['x'][24], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][25], amt=df['y'][25], rat=df['x'][25], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][27], amt=df['y'][26], rat=df['x'][26], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][28], amt=df['y'][27], rat=df['x'][27], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][29], amt=df['y'][28], rat=df['x'][28], typ='limit'))   #buy
print(bitkub.place_bid(sym=df['unit'][29], amt=df['y'][29], rat=df['x'][29], typ='limit'))   #buy

print('Place Buy Order complete')
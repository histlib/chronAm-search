import pandas as pd
import requests

text = input("Enter your search term or terms:")
state = input("Enter the individual state you would like to search; leave blank if more than one:")
startDate = input("Enter the start date for your search:")
endDate = input("Enter the end date for your search:")
rows = input("Enter the number of results; entering 1000 or more really stalls this program:")

data = requests.get(f'https://chroniclingamerica.loc.gov/search/pages/results/?state={state}&date1={startDate}&date2={endDate}&proxtext={text}&x=0&y=0&dateFilterType=yearRange&rows={rows}&searchType=basic&format=json').json()['items']

df = pd.DataFrame.from_dict(data)

df_new = df.filter(['title','city','state','date','ocr_eng','id'])

page_url = []
for item in df_new['id']:
    page_url.append(f"https://chroniclingamerica.loc.gov{item}#date1={startDate}&index=0&rows={rows}&words={text}&searchType=basic&sequence=0&state={state}&date2={endDate}&proxtext={text}&y=0&x=0&dateFilterType=yearRange&page=1")

df_new['page_url'] = page_url
df_new.to_csv(f"chronAm-{text}.csv")

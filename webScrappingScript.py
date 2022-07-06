from fileinput import close
import requests
import pandas as pd

url = 'https://www.govcagecodes.com/?code=&company=TESLA#results'
try:
    # Checking URL/website status for Error 
    r = requests.get(url,timeout=9)                                 
    r.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
    
    # Aquiring URL data using python liberaries  
html = requests.get(url).content
df_list = pd.read_html(html)

df = df_list[-1]
print(df)

    # Saving the Table data in JSON format
df.to_json('output.json')

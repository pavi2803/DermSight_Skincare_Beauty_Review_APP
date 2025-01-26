# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:24:14 2024

@author: Pavithra
"""

import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
plt.style.use('ggplot')



def fetchcomments(prodid):
    dataset=""
    url = "https://display.powerreviews.com/m/6406/l/en_US/product/"+prodid+"/reviews"
    
    for x in range(1,100,5): 
        querystring = {"paging.from":f"{x}","paging.size":"7","filters":"","search":"","sort":"Newest","image_only":"false","page_locale":"en_US","native_only":"true","_noconfig":"true","apikey":"daa0f241-c242-4483-afb7-4449942d1a2b"}
    
        headers = {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "origin": "https://www.ulta.com",
            "priority": "u=1, i",
            "referer": "https://www.ulta.com/",
            "^sec-ch-ua": "^\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\^Windows^^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        }
        
        try:
            r = requests.request("GET", url, headers=headers, params=querystring)
            data=r.json()
            
            comments = [review['details']['comments'] for review in data['results'][0]['reviews']]
            
        
        # Print out each comment
            for comment in comments:
                dataset=dataset+" * "+comment
            return dataset
            break

        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching reviews: {e}")
            return None
            break


data = pd.read_csv("sunscreen.csv")
data['comments'] = 'None'

# Iterate over each ID and update the comments column
for i in range(len(data)):
    c = fetchcomments(data.loc[i, 'ID'])
    data.loc[i, 'comments'] = c


data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
data.to_csv("sunscreen.csv")

import pandas as pd
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import streamlit as st
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
from textblob import TextBlob
from sumy.summarizers.lsa import LsaSummarizer        
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm
import nltk
from nltk.corpus import stopwords
from collections import Counter
from rake_nltk import Rake
from sentence_transformers import SentenceTransformer, util
from sklearn.feature_extraction.text import TfidfVectorizer
import torch
from transformers import pipeline
import google.generativeai as genai

def jsontodata(jsonfile,product_database):
    # Step 1: Open the JSON file
    with open(jsonfile, 'r') as f:
        # Step 2: Load JSON data
        data = json.load(f)
        items = data['data']['Page']['content']['items']
        #image_url = items[0]["image"]["imageUrl"]
        scraped_data=[]
        for item in items:
            # Accessing product_id and product_name under Tealium
            tealium_data = item['dataCapture']["dataLayer"]["Tealium"]
            product_brand  = tealium_data['product_brand'][0]
            product_id = tealium_data['product_id'][0]  # assuming there's only one product_id
            product_name = tealium_data['product_name'][0]  # assuming there's only one product_name
            product_sku = tealium_data['product_sku'][0]
            scraped_data.append({'Brand' : product_brand,'Name' : product_name, 'ID' : product_id,'sku':product_sku})
            
            
        if(len(product_database)==0):
            product_database = pd.DataFrame(scraped_data)
            return product_database
        else:
            product_database_new_add =  pd.DataFrame(scraped_data)
            result = pd.concat([product_database, product_database_new_add], ignore_index=True)
            
            return result
        
        
product_database=[]
data1 = jsontodata('sunscreens1.json',product_database)
data2 = jsontodata('sunscreens2.json',data1)
data3 = jsontodata('sunscreens3.json',data2)
data4 = jsontodata('sunscreens4.json',data3)

data4.to_csv("sunscreen.csv")

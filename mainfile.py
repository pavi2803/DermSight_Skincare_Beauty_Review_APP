import requests

import pandas as pd

import streamlit as st

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import google.generativeai as genai

import os


# Fetch the API key from Streamlit's secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
generation_config = {"temperature" : 0.9, "top_p": 1, "top_k":1, "max_output_tokens": 2048}

model = genai.GenerativeModel("gemini-pro", generation_config = generation_config)



#Application

st.header("DermSight : Skincare and Makeup Insights")

dropdown_skinbeauty = ['None','Moisturizers','Sunscreens','Foundations','Blushes']
selected_category = st.selectbox("Choose the category you want to explore: ", dropdown_skinbeauty)


if(selected_category=="Moisturizers"):
    data=pd.read_csv("moisturizers.csv")

    brand_options = data['Brand'].unique()
    
    dropdownbrand = []
    dropdownbrand.append(None)
    
    for i in brand_options:
        dropdownbrand.append(i)
    
    selected_brand = st.selectbox("Select a brand", dropdownbrand)
    
    if selected_brand:
        
        filtered_brand = data[(data['Brand'] == selected_brand)]
        
        name_options = filtered_brand['Name']
        
        dropdownnames = []
        dropdownnames.append(None)
        
        for i in name_options:
            dropdownnames.append(i)
        
        selected_name = st.selectbox("Select a product", dropdownnames)
        
        
        if selected_name!=None:
            
            
            desired_prod_id =  data[(data['Brand'] == selected_brand) & (data['Name'] == selected_name)]
            
            st.image("https://media.ulta.com/i/ulta/"+str(desired_prod_id.iloc[0]['sku']), caption='image')    
            
            comments = desired_prod_id['comments']
            
            
            input_prompt = """For the following reviews, 
                        Do a pros cons list, and tell me what weighs more? If you dont get any reviews, just say you didnt find any.  """

            try:
                if(comments is not None):
                    for i in comments[0:10]:
                        print(i)
                        text=str(i)
                        input_prompt+=text
    
                    submit=st.button("Get Reviews for this product")
                    
                    if submit:
                        response=model.generate_content([input_prompt])
                        st.subheader("Based on the users review :")
                        st.write(response.text)
                else:
                    st.text("Sorry! No reviews found for this product")
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")
                
            
elif(selected_category=="Foundations"):
    
    
    data=pd.read_csv("foundations.csv")
    

    brand_options = data['Brand'].unique()
    
    dropdownbrand = []
    dropdownbrand.append(None)
    
    for i in brand_options:
        dropdownbrand.append(i)
    
    selected_brand = st.selectbox("Select a brand", dropdownbrand)
    
    if selected_brand:
        
        filtered_brand = data[(data['Brand'] == selected_brand)]
        name_options = filtered_brand['Name']
        
        dropdownnames = []
        dropdownnames.append(None)
        
        for i in name_options:
            dropdownnames.append(i)
        
        selected_name = st.selectbox("Select a product", dropdownnames)
        
        
        if selected_name!=None:
            
            
            desired_prod_id =  data[(data['Brand'] == selected_brand) & (data['Name'] == selected_name)]
            
            st.image("https://media.ulta.com/i/ulta/"+str(desired_prod_id.iloc[0]['sku']), caption='image')    
            
            comments = desired_prod_id['comments']
            
            
            input_prompt = """For the following reviews, 
                        Do a pros cons list, and tell me what weighs more? If you dont get any reviews, just say you didnt find any.  """
            
            try:
                if(comments is not None):
                    for i in comments[0:10]:
                        print("comment---")
                        text=str(i)
                        input_prompt+=text
    
                    submit=st.button("Get Reviews for this product")
                    
                    if submit:
                        response=model.generate_content([input_prompt])
                        st.subheader("Based on the users review :")
                        st.write(response.text)
                else:
                    st.text("Sorry! No reviews found for this product")
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")
    
            
                        
elif(selected_category=="Blushes"):
    data = pd.read_csv("blush.csv")


    brand_options = data['Brand'].unique()
    
    dropdownbrand = []
    dropdownbrand.append(None)
    
    for i in brand_options:
        dropdownbrand.append(i)
    
    selected_brand = st.selectbox("Select a brand", dropdownbrand)
    
    if selected_brand:
        
        filtered_brand = data[(data['Brand'] == selected_brand)]
        
        name_options = filtered_brand['Name']
        
        dropdownnames = []
        dropdownnames.append(None)
        
        for i in name_options:
            dropdownnames.append(i)
        
        selected_name = st.selectbox("Select a product", dropdownnames)
        
        
        if selected_name!=None:
            
            
            desired_prod_id =  data[(data['Brand'] == selected_brand) & (data['Name'] == selected_name)]
            
            st.image("https://media.ulta.com/i/ulta/"+str(desired_prod_id.iloc[0]['sku']), caption='image')    
            
            comments = desired_prod_id.iloc[0]['comments']
            
            
            input_prompt = """For the following reviews, 
                        Do a pros cons list, and tell me what weighs more? If you dont get any reviews, just say you didnt find any. """
            
            try:
                if(comments is not None):
                    for i in comments[0:10]:
                        text=str(i)
                        input_prompt+=text
    
                    submit=st.button("Get Reviews for this product")
                    
                    if submit:
                        response=model.generate_content([input_prompt])
                        st.subheader("Based on the users review :")
                        st.write(response.text)
                else:
                    st.text("Sorry! No reviews found for this product")
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")
    
elif(selected_category=="Sunscreens"):
    
      data = pd.read_csv("sunscreen.csv")


      brand_options = data['Brand'].unique()
      
      dropdownbrand = []
      dropdownbrand.append(None)
      
      for i in brand_options:
          dropdownbrand.append(i)
      
      selected_brand = st.selectbox("Select a brand", dropdownbrand)
      
      if selected_brand:
          
          filtered_brand = data[(data['Brand'] == selected_brand)]
          
          name_options = filtered_brand['Name']
          
          dropdownnames = []
          dropdownnames.append(None)
          
          for i in name_options:
              dropdownnames.append(i)
          
          selected_name = st.selectbox("Select a product", dropdownnames)
          
          
          if selected_name!=None:
              
              
              desired_prod_id =  data[(data['Brand'] == selected_brand) & (data['Name'] == selected_name)]
              
              st.image("https://media.ulta.com/i/ulta/"+str(desired_prod_id.iloc[0]['sku']), caption='image')    
              
              comments = desired_prod_id.iloc[0]['comments']
              
              
              input_prompt = """For the following reviews, 
                        Do a pros cons list, and tell me what weighs more?  """
              
              try:
                if(comments is not None):
                    for i in comments:
                        text=str(i)
                        input_prompt+=text
    
                    submit=st.button("Get Reviews for this product")
                    
                    if submit:
                        response=model.generate_content([input_prompt])
                        st.subheader("Based on the users review :")
                        st.write(response.text)
                else:
                    st.text("Sorry! No reviews found for this product")
                    
              except Exception as e:
                  st.error(f"An error occurred: {e}")



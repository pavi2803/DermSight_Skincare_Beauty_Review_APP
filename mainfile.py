import requests

import pandas as pd

import streamlit as st

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import google.generativeai as genai



genai.configure(api_key="AIzaSyB4btXoYPwPUSAz37MJbyt7xUQwabRcIVg")


def get_gemini_repsonse(input_prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([input_prompt])
    return response.text
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
                        Display the following in this format below::
                        without displaying each review, carefully summarize them all and give an overall sentiment score on a scale of 1 to 10 with 1 being most negative and 10 being most positive; in the format :: Overall Sentiment Score:  ___/10 \n
                        By Keep it concise, Highlight the top three essential information in the reviews, (consisting both negative and positive reviews) by representing the whole review set, in the format :: Highlights in the reviews : \n
                            Pros: \n
                             _____\n
                             ....
                            Cons: \n
                             ___ \n
                             .....
                        after analyzing all reviews, tell me what weighs more, the pros or cons?
                        If you did not get any reviews from me, just say : No reviews found for this product"""

            try:
                if(comments!=None):
                    for i in comments:
                        text=str(i)
                        input_prompt+=text
    
                    submit=st.button("Get Reviews for this product")
                    
                    if submit:
                        response=get_gemini_repsonse(input_prompt)
                        st.subheader("Based on the users review :")
                        st.write(response)
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
                        Display the following in this format below::
                        without displaying each review, carefully summarize them all and give an overall sentiment score on a scale of 1 to 10 with 1 being most negative and 10 being most positive; in the format :: Overall Sentiment Score:  ___/10 \n
                        By Keep it concise, Highlight the top three essential information in the reviews, (consisting both negative and positive reviews) by representing the whole review set, in the format :: Highlights in the reviews : \n
                            Pros: \n
                             _____\n
                             ....
                            Cons: \n
                             ___ \n
                             .....
                        and after analyzing all reviews, tell me what weighs more, the pros or cons?
                        If you did not get any reviews from me, just say : No reviews found for this product"""
            
            if(comments!=None):
                for i in comments:
                    text=str(i)
                    input_prompt+=text
                    submit=st.button("Get Reviews for this product")
                    
                    if submit:
                        response=get_gemini_repsonse(input_prompt)
                        st.subheader("Based on the users review :")
                        st.write(response)
            else:
                st.text("Sorry! No reviews found for this product")
    
            
                        
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
                        Display the following in this format below::
                        without displaying each review, carefully summarize them all and give an overall sentiment score on a scale of 1 to 10 with 1 being most negative and 10 being most positive; in the format :: Overall Sentiment Score:  ___/10 \n
                        By Keep it concise, Highlight the top three essential information in the reviews, (consisting both negative and positive reviews) by representing the whole review set, in the format :: Highlights in the reviews : \n
                            Pros: \n
                             _____\n
                             ....
                            Cons: \n
                             ___ \n
                             .....
                        After analyzing all reviews, tell me what weighs more, the pros or cons?
                        If you did not get any reviews from me, just say : No reviews found for this product"""
            
            if(comments!=None):
                for i in comments:
                    text=str(i)
                    input_prompt+=text
                    submit=st.button("Get Reviews for this product")
                    if submit:
                        response=get_gemini_repsonse(input_prompt)
                        st.subheader("Based on the users review :")
                        st.write(response)
            else:
                st.text("Sorry! No reviews found for this product")
    
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
                          Display the following in this format below::
                          without displaying each review, carefully summarize them all and give an overall sentiment score on a scale of 1 to 10 with 1 being most negative and 10 being most positive; in the format :: Overall Sentiment Score:  ___/10 \n
                          By Keep it concise, Highlight the top three essential information in the reviews, (consisting both negative and positive reviews) by representing the whole review set, in the format :: Highlights in the reviews : \n
                              Pros: \n
                               _____\n
                               ....
                              Cons: \n
                               ___ \n
                               .....
                          and after analyzing all reviews, tell me what weighs more, the pros or cons?
                          If you did not get any reviews from me, just say : No reviews found for this product"""
              
              if(comments!=None):
                  for i in comments:
                      text=str(i)
                      input_prompt+=text
                      submit=st.button("Get Reviews for this product")
                      if submit:
                          response=get_gemini_repsonse(input_prompt)
                          st.subheader("Based on the users review :")
                          st.write(response)
              else:
                  st.text("Sorry! No reviews found for this product")
              
  

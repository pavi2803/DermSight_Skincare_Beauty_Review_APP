import time
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import streamlit as st
from selenium.webdriver.chrome.options import Options
# Initialize the WebDriver

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Define a function to scrape the current page
@st.cache_data
def price_product(url):
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome()
    data=[]
    def scrape_page():
        
        old_len = 0
        # Get the page source
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        #time.sleep(5)
        
        # Extract data from the page
        items = soup.find_all('div', class_='ProductCard__content')
        for item in items:
            name_element = item.find('span', class_='Text-ds Text-ds--body-2 Text-ds--left')
            brand = item.find('span', class_='Text-ds Text-ds--body-2 Text-ds--left Text-ds--neutral-600')
            price_element = item.find('span', class_='Text-ds Text-ds--body-2 Text-ds--left Text-ds--black')
            
            # Check if both name and price elements are found
            if name_element and price_element:
                name = name_element.text.strip()
                brand = brand.text.strip()
                price = price_element.text.strip()
                data.append({'Brand':brand,'Name': name, 'Price': price})
                
               
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #time.sleep(4)
        page_length = driver.execute_script("return document.body.scrollHeight;")
        print("Length of the webpage:", page_length)
      
    messages = [
    "Loading... Please wait.",
    "Just a moment...",
    "Fetching the data...",
    "Hang tight, we are almost there...",
    "Good things take time...",
    "Cooking in progress..",
    "Thanks for your patience...",
    "Extracting info..",
    "Almost done..."
]
    loading_message = st.empty()

# Display loading messages with delay
    for message in messages:
        loading_message.text(message)
        time.sleep(3)
   
    url = url  # Replace with the actual URL
    # Open the website
    driver.get(url)
    # Allow some time for the page to load
    #time.sleep(3)
    
    # Scrape data from the first page
    scrape_page()
    
    # Loop through multiple pages
    while True:
        print("REFRESHING..")
     
        try:
            # Click the 'Next' button
            #parent_element = driver.find_element(By.CLASS_NAME, 'LoadContent')
            #time.sleep(5)
            
            parent = WebDriverWait(driver, 3).until(
           EC.visibility_of_element_located((By.CSS_SELECTOR, '.LoadContent[data-test="load-content"]'))
       )
            
            #parent=driver.find_element(By.CSS_SELECTOR, '.LoadContent[data-test="load-content"]')
            print(parent.text)
         #   next_button = parent_element.find_element(By.TAG_NAME, 'button')
            
          #  WebDriverWait(driver, 10).until(
    #      EC.element_to_be_clickable((By.TAG_NAME, 'button'))
    #  )
            next_button = WebDriverWait(driver, 5).until(
           EC.visibility_of_element_located((By.CSS_SELECTOR, '.Button-ds.LoadContent__button.Button-ds--compact.Button-ds--withHover.Button-ds--secondary'))
       )
            driver.execute_script("arguments[0].scrollIntoView();", next_button)
            #next_button = driver.find_element(By.TAG_NAME,'button')
            #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
            
            scrape_page()
            try:
                
                # Click the 'Load More' button
                next_button.click()
            except ElementClickInterceptedException:
                # If element click intercepted, click using JavaScript
                driver.execute_script("arguments[0].click();", next_button)
            
            #next_button.click()
            # Scrape data from the new page
            
        except NoSuchElementException:
            print("No 'Next' button found. Exiting loop.")
            driver.quit()
            st.text("The Products are:")
            df = pd.DataFrame(data)
            df_no_duplicates = df.drop_duplicates(subset=['Name'])
            brands = df_no_duplicates['Brand']
            products = df_no_duplicates['Name']
            prices=df_no_duplicates['Price']
            #for i in products:
            #    st.text(i)
            
            #df_no_duplicates.to_csv('scraped_data.csv', index=False)
            break  # If no 'Next' button is found, break the loop
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            driver.quit()
            st.text("The Products are:")
            df = pd.DataFrame(data)
            df_no_duplicates = df.drop_duplicates(subset=['Name'])
            brands = df_no_duplicates['Brand']
            products = df_no_duplicates['Name']
            prices=df_no_duplicates['Price']
            #for i in products:
            #    st.text(i)
            #df_no_duplicates.to_csv('scraped_data.csv', index=False)
            break  # Break the loop if any other exception occurs# If no 'Next' button is found, break the loop
    return df_no_duplicates


@st.cache_data
def fetch_ingr_url(url):
    url_fetch = url
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome()  # Ensure you have the correct path to your webdriver
    driver.get(url_fetch)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'paddingbl'))
        )
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        # Find the div with class 'paddingbl'
        items = soup.find('div', class_='paddingbl')
        
        # Check if items is not None
        if items is not None:
            # Find the first a element within the items
            first_link = items.find('a', class_='klavika simpletextlistitem')
            
            # Get the href attribute of the first a element
            first_href = first_link['href'] if first_link else 'No href found'
        else:
            first_href = 'No href found'
    except Exception as e:
        first_href = 'No href found'
        print(f"An error occurred: {e}")
    finally:
        # Close the driver
        driver.quit()
    
    return first_href
    

    
    

@st.cache_data
def fetch_ingr(url):
    ingrurl=url
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--no-sandbox")

   
    driver = webdriver.Chrome()
    driver.get(ingrurl)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    picture = soup.find('picture')
    img_tag = picture.find('img')
    
    img_src = img_tag['src'] if img_tag else 'no image found'
    
    if img_src!= 'no image found':
        st.image(img_src)
        
        

        # Extract the table rows
        table_rows = soup.find_all('tr')
        
        # Prepare a list to hold the table data
        table_data = []
        
        # Extract data from each row
        for row in table_rows:
            columns = row.find_all('td')
            row_data = [col.get_text(strip=True) for col in columns]
            if row_data:  # Avoid adding empty rows
                table_data.append(row_data)
        
        # Define the column names
        column_names = ['Ingredient', 'Function', 'Irritancy/Comedogenicity', 'Our Take']
        
        # Convert the data into a DataFrame
        df = pd.DataFrame(table_data, columns=column_names)
        
        st.title("Ingredient Table")
        st.dataframe(df)
        driver.quit()
    else:
        st.write('No image found!')
    
    

def people_thoughts():
    print("not done yet")
    st.write("Ooops, wait for this ")
    
    
    # Save data to a CSV file
   
    
    #print('Data has been saved to scraped_data.csv')
    
       
    

    

    
    
    
    
    
    
# WEB PAGE MAIN AREA START:

st.set_page_config(page_title="skincare")

st.header("Skincare and Beauty Decoded")


# Dropdown menu for selecting an option
dropdown_option_category = st.selectbox(
    'Choose an option to Know more:',
    ('None','Cleansers','Sunscreens', 'Face Moisturizers', 'Toners and Actives','Foundations','Blushes','Lipsticks')
)



# Display the selected option from the dropdown menu
if(dropdown_option_category=="Sunscreens" or dropdown_option_category=="Face Moisturizers" or dropdown_option_category=="Toners and Actives" or dropdown_option_category=="Foundations" or dropdown_option_category=="Blushes" or dropdown_option_category=="Cleansers" or dropdown_option_category=="Lipsticks"):
    st.write(f'You selected: {dropdown_option_category}')
    
    dropdown_option_choice = st.selectbox(
        "What would you like to know about this category?",
        ('None','Products, Price and Ingredients', 'What people think about?')
    )
    
    if(dropdown_option_category =="Sunscreens" and dropdown_option_choice=="Products, Price and Ingredients"):
        
        output_data = price_product("https://www.ulta.com/shop/body-care/suncare/sunscreen")
        
        dropdown_option_brand = st.selectbox(
            'Choose an option to Know more:',
            (i for i in output_data['Brand'].unique())
        )
        
        filtered_brand=output_data[output_data['Brand']==dropdown_option_brand]
        #st.table(filtered_brand)
        
        st.text("Select on the products to know more about the ingredients..")
        
        for index, row in filtered_brand.iterrows():
            col1, col2, col3= st.columns(3)
            with col1:
                st.write(row['Name'])
            with col2:
                st.write(row['Price'])
            with col3:
                if st.button('Ingredients', key=index):
                    st.text(f'Looking up..')
                    ingr_page_url = fetch_ingr_url("https://incidecoder.com/search?query="+row['Brand']+" "+row['Name'])
                    if(ingr_page_url=="No href found"):
                        st.text("Sorry! It looks like the ingredients for this product is not available.")
                    else:
                        fetch_ingr("https://incidecoder.com/"+ingr_page_url)
    
    elif(dropdown_option_category =="Face Moisturizers" and dropdown_option_choice=="Products, Price and Ingredients"):
       
       output_data = price_product("https://www.ulta.com/shop/skin-care/moisturizers/face-moisturizer")
       
       dropdown_option_brand = st.selectbox(
           'Choose an option to Know more:',
           (i for i in output_data['Brand'].unique())
       )
       
      
       filtered_brand=output_data[output_data['Brand']==dropdown_option_brand]
       #st.table(filtered_brand)
       
       st.text("Select on the products to know more about the ingredients..")
       
       for index, row in filtered_brand.iterrows():
           col1, col2, col3= st.columns(3)
           with col1:
               st.write(row['Name'])
           with col2:
               st.write(row['Price'])
           with col3:
               if st.button('Ingredients', key=index):
                   st.write(f'Looking up..')
                   ingr_page_url = fetch_ingr_url("https://incidecoder.com/search?query="+row['Brand']+" "+row['Name'])
                   if(ingr_page_url=="No href found"):
                       st.text("Sorry! It looks like the ingredients for this product is not available.")
                   else:
                       fetch_ingr("https://incidecoder.com/"+ingr_page_url)
           
           
    elif(dropdown_option_category =="Toners and Actives" and dropdown_option_choice=="Products, Price and Ingredients"):
        
        output_data = price_product("https://www.ulta.com/shop/skin-care/cleansers/toner")
       
       
        brands=['None']
        dupdf = output_data.copy()
       
        for i in dupdf['Brand'].unique():
           brands.append(i)
           
        dropdown_option_brand = st.selectbox(
           'Choose an option to Know more:',
           (i for i in brands)
       )
        
        filtered_brand=dupdf[dupdf['Brand']==dropdown_option_brand]
        #st.table(filtered_brand)
        
        st.text("Select on the products to know more about the ingredients..")
        
        for index, row in filtered_brand.iterrows():
            col1, col2, col3= st.columns(3)
            with col1:
                st.write(row['Name'])
            with col2:
                st.write(row['Price'])
            with col3:
                if st.button('Ingredients', key=index):
                    st.write(f'Looking up..')
                    ingr_page_url = fetch_ingr_url("https://incidecoder.com/search?query="+row['Brand']+" "+row['Name'])
                    if(ingr_page_url=="No href found"):
                        st.text("Sorry! It looks like the ingredients for this product is not available.")
                    else:
                        fetch_ingr("https://incidecoder.com/"+ingr_page_url)
                    
                    
    elif(dropdown_option_category =="Cleansers" and dropdown_option_choice=="Products, Price and Ingredients"):
        
        output_data = price_product("https://www.ulta.com/shop/skin-care/cleansers/face-wash")
       
       
        brands=['None']
        dupdf = output_data.copy()
       
        for i in dupdf['Brand'].unique():
           brands.append(i)
           
        dropdown_option_brand = st.selectbox(
           'Choose an option to Know more:',
           (i for i in brands)
       )
        
        filtered_brand=dupdf[dupdf['Brand']==dropdown_option_brand]
        #st.table(filtered_brand)
        
        st.text("Select on the products to know more about the ingredients..")
        
        for index, row in filtered_brand.iterrows():
            col1, col2, col3= st.columns(3)
            with col1:
                st.write(row['Name'])
            with col2:
                st.write(row['Price'])
            with col3:
                if st.button('Ingredients', key=index):
                    st.write(f'Looking up..')
                    ingr_page_url = fetch_ingr_url("https://incidecoder.com/search?query="+row['Brand']+" "+row['Name'])
                    if(ingr_page_url=="No href found"):
                        st.text("Sorry! It looks like the ingredients for this product is not available.")
                    else:
                        fetch_ingr("https://incidecoder.com/"+ingr_page_url)
                    
                    
    elif(dropdown_option_category =="Foundations" and dropdown_option_choice=="Products, Price and Ingredients"):
        
        output_data = price_product("https://www.ulta.com/shop/makeup/face/foundation")
       
       
        brands=['None']
        dupdf = output_data.copy()
       
        for i in dupdf['Brand'].unique():
           brands.append(i)
           
        dropdown_option_brand = st.selectbox(
           'Choose an option to Know more:',
           (i for i in brands)
       )
        
        filtered_brand=dupdf[dupdf['Brand']==dropdown_option_brand]
        #st.table(filtered_brand)
        
        st.text("Select on the products to know more about the ingredients..")
        
        for index, row in filtered_brand.iterrows():
            col1, col2, col3= st.columns(3)
            with col1:
                st.write(row['Name'])
            with col2:
                st.write(row['Price'])
            with col3:
                if st.button('Ingredients', key=index):
                    st.write(f'Looking up..')
                    ingr_page_url = fetch_ingr_url("https://incidecoder.com/search?query="+row['Brand']+" "+row['Name'])
                    if(ingr_page_url=="No href found"):
                        st.text("Sorry! It looks like the ingredients for this product is not available.")
                    else:
                        fetch_ingr("https://incidecoder.com/"+ingr_page_url)
                    
    elif(dropdown_option_category =="Blushes" and dropdown_option_choice=="Products, Price and Ingredients"):
        
        output_data = price_product("https://www.ulta.com/shop/makeup/face/blush")
       
       
        brands=['None']
        dupdf = output_data.copy()
       
        for i in dupdf['Brand'].unique():
           brands.append(i)
           
        dropdown_option_brand = st.selectbox(
           'Choose an option to Know more:',
           (i for i in brands)
       )
        
        filtered_brand=dupdf[dupdf['Brand']==dropdown_option_brand]
        #st.table(filtered_brand)
        
        st.text("Select on the products to know more about the ingredients..")
        
        for index, row in filtered_brand.iterrows():
            col1, col2, col3= st.columns(3)
            with col1:
                st.write(row['Name'])
            with col2:
                st.write(row['Price'])
            with col3:
                if st.button('Ingredients', key=index):
                    st.write(f'Looking up..')
                    ingr_page_url = fetch_ingr_url("https://incidecoder.com/search?query="+row['Brand']+" "+row['Name'])
                    if(ingr_page_url=="No href found"):
                        st.text("Sorry! It looks like the ingredients for this product is not available.")
                    else:
                        fetch_ingr("https://incidecoder.com/"+ingr_page_url)
                    
                    
    elif(dropdown_option_category =="Lipstick" and dropdown_option_choice=="Products, Price and Ingredients"):
        
        output_data = price_product("https://www.ulta.com/shop/makeup/lips/lipstick")
       
       
        brands=['None']
        dupdf = output_data.copy()
       
        for i in dupdf['Brand'].unique():
           brands.append(i)
           
        dropdown_option_brand = st.selectbox(
           'Choose an option to Know more:',
           (i for i in brands)
       )
        
        filtered_brand=dupdf[dupdf['Brand']==dropdown_option_brand]
        #st.table(filtered_brand)
        
        st.text("Select on the products to know more about the ingredients..")
        
        for index, row in filtered_brand.iterrows():
            col1, col2, col3= st.columns(3)
            with col1:
                st.write(row['Name'])
            with col2:
                st.write(row['Price'])
            with col3:
                if st.button('Ingredients', key=index):
                    st.write(f'Looking up..')
                    ingr_page_url = fetch_ingr_url("https://incidecoder.com/search?query="+row['Brand']+" "+row['Name'])
                    if(ingr_page_url=="No href found"):
                        st.text("Sorry! It looks like the ingredients for this product is not available.")
                    else:
                        fetch_ingr("https://incidecoder.com/"+ingr_page_url)
                    
    
    else:
        print("Concious Beauty is real Beauty!")
    
   
       
      
        
    

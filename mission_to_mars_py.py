#!/usr/bin/env python
# coding: utf-8

# # Mission to Mars

# ## Part 1: Web-scraping

# ### Nasa Mars News

# In[1]:


# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd


# In[2]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Mars URL to scrape
url = 'https://redplanetscience.com/'
browser.visit(url)


# In[4]:


# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = bs(html, 'html.parser')


# In[5]:


# use 'print' to make sure some info/data was collected
# can comment this out after inspecting & verifying 
# print(soup.prettify())


# In[6]:


results = soup.find_all('div', class_='list_text')
# print(results)


# In[7]:


for result in results:
    
    try:
    
        # Retrieve the query title
        news_title = result.find('div', class_='content_title').text
        # Identify and return paragraph
        news_p = result.find('div', class_='article_teaser_body').text

        # Print results only if title and paragraph are available
        if (news_title and news_p):
            print('-------------')
            print(news_title)
            print(news_p)
            
    except AttributeError as e:
        print(e)


# In[8]:


browser.quit()


# ### JPL Mars Space Images--Featured Image

# In[9]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[10]:


# Mars Image URL to scrape
url = 'https://spaceimages-mars.com/'
browser.visit(url)


# In[11]:


# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = bs(html, 'html.parser')


# In[12]:


# print(soup.prettify())


# In[13]:


results = soup.find('div', class_='header')


# In[14]:


print(results)


# In[15]:


find_image = results.find('div', class_='floating_text_area')
print(find_image)


# In[16]:


featured_image = find_image.find('a')['href']
print(featured_image)


# In[17]:


featured_image_url = url+featured_image
print(featured_image_url)


# In[18]:


browser.quit()


# ### Mars Facts

# In[19]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[20]:


# URL to scrape mars facts table
url = 'https://galaxyfacts-mars.com/'
browser.visit(url)


# In[21]:


# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = bs(html, 'html.parser')


# In[22]:


table = pd.read_html(url)
table


# In[23]:


type(table)


# In[24]:


# Convert list to pandas dataframe *look for the comma! it indicates where the first table stops and this table starts
facts_df = table[1]
facts_df.columns = ['Parameters', 'Values']
facts_df


# In[25]:


mars_facts_table = facts_df.to_html()
print(mars_facts_table)


# In[26]:


browser.quit()


# ### Mars Hemispheres

# In[27]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[28]:


# URL to scrape for Mars hemispheres images
url = 'https://marshemispheres.com/'
browser.visit(url)


# In[29]:


# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = bs(html, 'html.parser')


# In[30]:


hem_images = soup.find_all('div', class_="item")
print(hem_images)


# In[31]:


hem_list=[]

for image in hem_images:
    
    hemis_dict = {}
    title = image.h3.text
    hemis_dict['title'] = title
    
    hemis_link = browser.links.find_by_partial_text(title).click()
    
    hemis_html = browser.html
    hemis_soup = bs(hemis_html, 'html.parser')
    
    hemis_image = hemis_soup.find_all('li')
    image_link = hemis_image[0].find('a')['href']
    
    hemis_image_link = url + image_link
    hemis_dict['img_url'] = hemis_image_link
    
    print(hemis_dict)
    
    browser.back()


# In[34]:


browser.quit()


# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time

def mars_news():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    # Mars URL to scrape
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(1)
    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find_all('div', class_='list_text')
    for result in results:
        #create a dictionary 
        mars_news_dict = {}
        # retrieve the query title
        news_title = result.find('div', class_='content_title').text
        # add title to dictionary
        mars_news_dict['news_article_title'] = news_title
        # identify and return paragraph
        news_p = result.find('div', class_='article_teaser_body').text
        # add paragraph to dictionary
        mars_news_dict['news_article_p'] = news_p
    browser.quit()

    return mars_news_dict

def mars_featured_image():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    # Mars Image URL to scrape
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    time.sleep(1)
    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find('div', class_='header')
    find_image = results.find('div', class_='floating_text_area')
    featured_image = find_image.find('a')['href']
    featured_image_url = url + featured_image
    mars_image_dict = {}
    mars_image_dict['featured_image_url'] = featured_image_url
    browser.quit()

    return mars_image_dict

def mars_facts():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    # URL to scrape mars facts table
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)
    time.sleep(1)
    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html, 'html.parser')
    table = pd.read_html(url)
    facts_df = table[1]
    facts_df.columns = ['Parameters', 'Values']
    mars_facts_table = facts_df.to_html()
    mars_facts_dict = {}
    mars_facts_dict['facts_table_html'] = mars_facts_table
    browser.quit()

    return mars_facts_dict

def mars_hemispheres():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    # URL to scrape for Mars hemispheres images
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    time.sleep(1)
    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html, 'html.parser')
    hem_images = soup.find_all('div', class_="item")
    hem_list=[]
    for image in hem_images:
        hemis_dict = {}
        title = image.h3.text
        hemis_dict['hemisphere_title'] = title
        hemis_link = browser.links.find_by_partial_text(title).click()
        hemis_html = browser.html
        hemis_soup = bs(hemis_html, 'html.parser')
        hemis_image = hemis_soup.find_all('li')
        image_link = hemis_image[0].find('a')['href']
        hemis_image_link = url + image_link
        hemis_dict['img_url'] = hemis_image_link
        hem_list.append(hemis_dict)
        browser.back()
    browser.quit()
    return hem_list

# create a dictionary of the above dictionaries

def scrape():
    mars_news_dict = mars_news()
    mars_image_dict = mars_featured_image()
    mars_facts_dict = mars_facts()
    hem_list = mars_hemispheres()
    mars_dict = {}
    mars_dict['news'] = mars_news_dict
    mars_dict['image'] = mars_image_dict
    mars_dict['facts'] = mars_facts_dict
    mars_dict['hemispheres'] = hem_list
    
    return mars_dict
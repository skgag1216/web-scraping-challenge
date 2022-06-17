# Mission to Mars
### A Web Scraping Challenge
### <hr>
#### 
Welcome to a new way to display your research! Have you ever wondered what other planets in our solar system are like compared to Earth? Let's learn all about Mars and how to parse webpages in this new, exciting web scraping challenge!

<h3 align ="center"> :star: :alien: :telescope: :new_moon_with_face: </h3>

To create this application you'll use the following tools:
1. Jupyter notebook
    - Splinter
    - Beautiful Soup
    - ChromeDriverManager
    - Pandas
2. VS Code (or similar code editor)
    - copy over work from Jupyter Notebook and import above dependency tools
    - also import ``` time ``` for your scraping app
    - Flask
    - Pymongo
3. MongoDB (MongoDB Compass) 
4. Google Chrome web browser

```
# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time
```

First we start with Jupyter Notebook and create a new interactive python notebook file. Run Splinter application on each website to scrape the information we want to gather. Plenty of    ``` # comments ``` in the ```.ipynb``` Jupyter Notebook file to follow along with how to execute Splinter and Beautiful Soup to parse each web page.

Note: Before you begin, know that you need to save the specified information into a python dictionary ``` <name-of-dict-here> = { } ```

<i>News</i>

For Mars News you will gather the title of each of the latest articles and the corresponding paragraph snippet from this webpage: ``` https://redplanetscience.com/ ``` 

<i>Featured Image </i>

Next grab the featured image by parsing: ``` https://spaceimages-mars.com/ ```

<i> Facts </i>

Then we want to get a table of facts about Mars from this webpage: ``` https://galaxyfacts-mars.com/ ``` 
The information will appear in a table on the webpage, we want to grab that information and store it in a dataframe using pandas; then we need to save it in html format by calling our handy-dandy ```.to_html``` method.

<i> Hemispheres </i>

Lastly we gather the titles and images of Mars' hemispheres. We need to pull the title of each one and then the corresponding full size image using: ``` https://marshemispheres.com/ ``` We will be using a ``` for ``` loop and grabbing a title then Splinter to click to the webpage that holds the full size image of the specific hemisphere and saving it to a new variable as well. This will occur 4 times, once for each hemisphere. This data will be saved to a dictionary, appended to a list, and finally after the loop has completed, the list will be appended to a dictionary outside of the loop.

<hr>

After performing the tasks inside Jupyter Notebook we move to VS Code where we create a scraping application
```
scrape_mars.py
```
 and then a displaying application
 ``` 
 app.py
 ```

 Start with creating the scraping application. Basically, you'll copy over the work you did for each section (News, Featured Image, Facts, Hemispheres) into a definition fuction that returns the dictionary to complete the function.
 ```
 def mars_news():

    <code-here-for-scraping>
    <from-Jupyter-Notebook>

    return mars_news_dict
```

Make sure the final data set is saved into a dictionary. If you do each section individually you'll need to append each dictionary to one final dictionary to return. If you do all the sections together fluidly then you're final output will be the final dictionary you return and use for the next application.

The next step is to create the application that will pull everything together. This will be a new file in the same folder that we will name ``` app.py ```

A different set of dependencies will imported to start ```app.py```
```
# Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
```
Then go through the steps of code (all in ``` # comments of app.py``` ) to create an instance of Flask. Use PyMongo to establish Mongo connection. Name your database in MongoDB by simply calling it what you would like after the forward-slash in the connection line, for example I have mine as ```mars_app```
```
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
```

Drop the collection if available to remove duplicates. This line will also prevent duplicate sets of datat from saving inside your database.

```mongo.db.<name-of-final-dict-returned-here>.drop()```

Create a route to render index.html template using data from Mongo. When creating routes use the definition function inside the route, have it grab one record of data from MongoDB and return the template for ```index.html``` and the data.

Create a route that will trigger the scrape function.
Run the scrape function and update the Mongo database using update and ```upsert=True``` and redirect back to the home page for the return.

Lastly use the standard code to call the Flask app to run at the end.

Inside the main folder you are working in you will need a folder specifically called ```templates``` and inside this folder is where you will create and store ```index.html```

Use HTML and inline CSS to set up how you would like to display all your newly found Mars information.

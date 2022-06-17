# Mission to Mars
### A Web Scraping Challenge
### <hr>
#### 
Welcome to a new way to display your research! Have you ever wondered what other planets in our solar system are like compared to Earth? Let's learn all about Mars and how to parse webpages in this new, exciting web scraping challenge!

<h2> :star: :alien: :telescope: :new_moon_with_face: </h2> 

First we start with Jupyter Notebook and create a new interactive python notebook file. Run Splinter application on each website to scrape the information we want to gather. 
'''python
# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
'''
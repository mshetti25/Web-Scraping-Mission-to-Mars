# Web-Scraping-Mission-to-Mars
In this assignment, I will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

## Step 1 - Scraping
Completed the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
Created a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines are scraped.

### NASA Mars News
Scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
#### Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."

### JPL Mars Space Images - Featured Image
Visited the url for JPL Featured Space Image.
Used splinter to navigate the site and find the image url for the current Featured Mars Image and assigned the url string to a variable called featured_image_url.
#### Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'

### Mars Facts
Visited the Mars Facts webpage and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
Used Pandas to convert the data to a HTML table string.



### Mars Hemispheres
Visited the USGS Astrogeology site here to obtain high resolution images for each of Mars hemispheres.
Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys img_url and title.
Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
#### Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},

## Step 2 - MongoDB and Flask Application
Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
Started by converting the Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
Next, created a route called /scrape that will import your scrape_mars.py script and call the scrape function.
Stored the return value in Mongo as a Python dictionary.
Created a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
Created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 

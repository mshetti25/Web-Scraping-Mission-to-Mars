import pandas as pd
from splinter import Browser as b
from bs4 import BeautifulSoup as bs
import time

executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = b("chrome", **executable_path, headless=False)



def scrape():
    data = {}
    news = mars_news()
    data["mars_news"] = news[0]
    data["mars_paragraph"] = news[1]
    data["mars_image"] = mars_image()
    data["mars_facts"] = mars_facts()
    data["mars_hemisphere"] = mars_hem_data()
    browser.quit()
    return data

# NASA Mars News
def mars_news():
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = bs(html, 'html.parser')
    title = soup.find("div",class_="content_title").text
    para = soup.find("div", class_="article_teaser_body").text
    news_data = [title, para]
    return news_data

# JPL Mars Space Images - Featured Image
def  mars_image():
    space_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(space_image_url)
    time.sleep(5)
    space_image_html = browser.html
    soup = bs(space_image_html,"html.parser")
    i_path = soup.find('img', class_ = 'thumb')['src']
    featured_image_url = "https://www.jpl.nasa.gov" + i_path
    return featured_image_url

# Mars Facts
def  mars_facts():
    facts_df = pd.read_html('https://space-facts.com/mars/')[0]
    facts_df.columns=['Labels', 'Value']
    facts_html = facts_df.to_html(header = False, index = False)
    return facts_html

    # Mars Hemispheres
def mars_hem_data():
    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    time.sleep(5)
    html = browser.html
    soup = bs(html,'html.parser')
    img = soup.find('div', class_='collapsible results')
    hem_img = []

    for x in range(len(img.find_all("div", class_="item"))):
        time.sleep(5)
        h_img = browser.find_by_tag('h3')
        h_img[x].click()
        html = browser.html
        soup = bs(html, 'html.parser')
        t = soup.find("h2", class_="title").text
        d = soup.find("div", class_="downloads")
        url = d.find('a')
        link = url.attrs['href']
        hem_dict = {
                'title' : t,
                'img_url' : link
            }
        hem_img.append(hem_dict)
        browser.back()
    return hem_img  

if __name__ == "__main__":
    print('Starting the app...')
    scrape()

import pandas as pd
from splinter import Browser as b
from bs4 import BeautifulSoup as bs
import time

    


def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser =  b('chrome', **executable_path)

    data= {}

    # NASA Mars News
    browser.visit('https://mars.nasa.gov/news/')
    html = browser.html
    soup = bs(html, 'html.parser')
    title = soup.find('div', class_="bottom_gradient").text
    para = soup.find('div', class_='article_teaser_body').text
    data["News_title"] = title
    data["New_para"] = para

    # JPL Mars Space Images - Featured Image
    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)
    html = browser.html
    soup = bs(html,'html.parser')
    i_path= soup.find('figure',class_='lede').a['href']
    featured_image_url = 'https://www.jpl.nasa.gov/'+ i_path
    data["Featured_image_url"] = featured_image_url

    # Mars Facts
    facts_df = pd.read_html('https://space-facts.com/mars/')[0]
    facts_df.columns=['Labels', 'Value']
    facts_html = facts_df.to_html(header = False, index = False)
    data["Mars_table"] = facts_html

    # Mars Hemispheres
    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    html = browser.html
    soup = bs(html,'html.parser')
    img = soup.find('div', class_='collapsible results')
    hem_img = []

    # print(len(images.find_all("div", class_="item")))
    for x in range(len(img.find_all("div", class_="item"))):
        # print(i)
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
        data["hemispheres_image_urls"] = hem_img

    return data

if __name__ == "__main__":
    scrape()
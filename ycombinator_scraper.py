# IMPORT LIBRARIES
from socket import socket
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from IPython.display import Image
from datetime import datetime as dt
import time
import socket
import concurrent.futures as cf

# FUNCTION TO CHECK THE INTERNET CONNECTIVITY
import urllib.request
def internet_on():
    
    try:
        urllib.request.urlopen('https://www.google.com', timeout=2)
        return True
    except:
        return False


# FUNCTION TO SETUP CHROME BROWSER
def browser_setup():
    
    # Path to the Chromedriver.
    PATH = "C:/Users/famou/.wdm/drivers/chromedriver/win32/99.0.4844.51/chromedriver.exe"

    # Change options.headless to False to show chrome browser.
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(PATH, chrome_options=options)

    # Load url in browser.
    URL = 'https://www.ycombinator.com/companies/'
    driver.get(URL)
    return driver


# FUNCTION TO CONFIGURE SELENIUM FOR INFINITE SCROLLING
def infinite_scroll(driver):
    
    try:
        # Wait for some elements to load.
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, 
                        "/html/body/div/div[2]/div/div/div[2]/div[4]/a[1]/div[1]/div/img")))
        
        
        SCROLL_PAUSE_TIME = 0.5
        
        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    except TimeoutException:
        print("Loading took too much time!!. Please refresh.")


# FUNCTION TO GET THE URL AND LOCATION OF ALL COMPANIES
def get_company_url_and_country():

    homepage = browser_setup()
    infinite_scroll(homepage)
    
    page = homepage.page_source
    ycombinator = BeautifulSoup(page, 'html.parser')

    # Find all the anchor tags with class = "styles-module__company___1UVnl no-hovercard"
    # and return their "href".
    sites = []
    count = 0
    for link in ycombinator.find_all('a',
                            class_ = "styles-module__company___1UVnl no-hovercard"):
        # display the actual urls
        site = link.get('href') 
        site_mod = f"https://www.ycombinator.com{site}"
        sites.append(site_mod)
        count += 1

         # Extract location.
        hold = link.find('span', class_='styles-module__coLocation___yhKam')
        Location.append(hold.text)

        # Extract the country of each company.
        country = str(hold.text).split(",")[-1].strip()
        Country.append(country)

    # Count number of links.
    print(f"\nCompanies total:", count)
    print('\n')
    return sites


# INITIATE PLACEHOLDER LISTS
Company_name = []
Company_tag = []
Short_description = []
Founded = []
Team_size = []
Location = []
Country = []
Website = [] 
Active_founders = []
Social_media_company = []
Founders_info = []
Description = []


# FUNCTION TO SCRAPE COMPANIES DATA
def get_companies_info(soup):
    
    # Company name.
    select = soup.find('div', class_="font-bold text-lg")
    Company_name.append(select.text)

    # Company tag.
    hold = []
    select = soup.find_all('span',  class_='ycdc-badge')
    for j in select:
        j = j.text.replace('Y Combinator Logo', '')
        hold.append(j)

    Company_tag.append(hold)    

    # Short description.
    select = soup.find('h3', class_="sm:block md:hidden")
    Short_description.append(select.text)

    # Founded.
    select = soup.find('div', class_ = "space-y-0.5")
    select = select.next_element
    for j in select:
        if j.text != 'Founded:':
            Founded.append(j.text)

    # Team Size.
    select = select.next_sibling
    for j in select:
        if j.text != 'Team Size:':
            Team_size.append(j.text)

    # Location.
    # Check the function get_company_url_and_country.
    
    # Website.
    for j in soup.find('div', class_ = "flex flex-row items-center leading-none px-3"):
        if j.get('href') != None:
            Website.append(j.get('href'))

    # Company's social media links.
    hold = []
    for j in soup.find(class_ = "space-x-2"):
        link = j.get('href')
        hold.append(link)

    Social_media_company.append(hold)

    # Full description.
    select = soup.find('p', class_="whitespace-pre-line")
    Description.append(select.text)


# FUNCTION TO SCRAPE FOUNDERS DATA
def get_founders_info(soup):

    try:
        # Active founders.
        hold = []
        founders = soup.find('div', class_='space-y-5')
        for name in founders.find_all('div', class_='leading-snug'):
            hold.append(name.div.text)
        Active_founders.append(hold)

        # Founders details.
        all_info = []
        for what in founders.find_all('div', class_='flex flex-row gap-3 items-start flex-col md:flex-row'):
            info = {}
            name = what.h3.text
            split = name.split(', ')

            info['name'] = split[0]

            if split[0] != split[-1]:
                info['role'] = split[-1]
            else:
                info['role'] = ''

            
            info['social_media'] = [link['href'] for link in what.find('div', class_='mt-1 space-x-2').find_all('a')]
            
            info['description'] = [d.text for d in what.find('p', class_='prose max-w-full whitespace-pre-line')]

            all_info.append(info)


        Founders_info.append(all_info)
        
    # Handle difference in page layouts for Founders.
    except:
        hold = []
        all_info = []

        founders = soup.find('div', class_='space-y-4')

        for founder in founders.find_all('div', class_='leading-snug'):
            
            info = {}
            name = founder.find('div', class_='font-bold').text
            info['name'] = name

            divs = [what for what in founder.find_all('div')]

            info['role'] = divs[1].text
            info['social_media'] = [link['href'] for link in founder.find('div', class_='mt-1 space-x-2').find_all('a')]

            all_info.append(info)
            hold.append(founder.find('div', class_='font-bold').text)
            
        Active_founders.append(hold)
        Founders_info.append(all_info)


# FUNCTION TO SCRAPE ALL DATA
def scrape_info(url): 

    # Hold the unscraped sites.
    unscraped_sites = []

    # Pass to BeautifulSoup.
    Each_page = requests.get(url)
    soup = BeautifulSoup(Each_page.content)

    try:
        get_companies_info(soup)
        get_founders_info(soup)
    
    except (socket.gaierror, ConnectionError):
        unscraped_sites.append(url)

    return unscraped_sites


# SCRAPE DATA WITH MULTI-THREADING
run = True
unscraped_sites = []
i = 0

# Check internet connection.
conn = internet_on()

# Start timer.
start_thread = dt.now()

if conn is True:

    # Get company links.
    links = get_company_url_and_country()

    while run:
        
        with cf.ThreadPoolExecutor() as executor:
            executor.map(scrape_info, links)

        # Print unscraped sites.
        print(f"Sites left to scrape are:", unscraped_sites)

        # Check for unscraped sites and reinitiate scraping.
        if unscraped_sites != []:
            links = unscraped_sites
            
        else:
            print('DONE!')
            run = False

else:
    print("Check internet connection!")


# STORE EXTRACTED DATA IN A DATAFRAME.
d = zip(Company_name, Company_tag, Short_description, Founded, Location, Country, Team_size, Website, Active_founders, Social_media_company, Founders_info, Description)
mapped = list(d)
df = pd.DataFrame(mapped, columns=['Company_name','Company_tag', 'Short_description', 'Founded', 'Location', 'Country', 'Team_size', 'Website', 'Active_founders', 'Company_social_media', 'Founders_info', 'Description'])

# EXPORT DATAFRAME TO CSV.
df.to_csv('ycombinator.csv')

runtime_thread = (dt.now() - start_thread)
print(f'Total runtime: {runtime_thread}')
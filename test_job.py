from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time

# Set up the Chrome web driver
options=webdriver.ChromeOptions()
# options.add_argument("--headless=new")
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

# Navigate to the LinkedIn login page
driver.get('https://www.linkedin.com/login')
driver.maximize_window()
driver.implicitly_wait(15)
# Wait for the page to load

def test_login():
    # Fill in the login form
    username = driver.find_element(By.ID, 'username')
    username.send_keys('danial.ds2015@gmail.com')
    password = driver.find_element(By.ID, 'password')
    password.send_keys('test_DS_23')
    password.send_keys(Keys.RETURN)
    # Wait for the home page to load
    time.sleep(15)
    


def test_jobList():


        # Navigate to the LinkedIn job search page
    job_search_url = "https://www.linkedin.com/jobs/"
    driver.get(job_search_url)
    time.sleep(2)
    # Locate and interact with the search results
    search_bar = wait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#jobs-search-box-keyword-id-ember23"))
    )
    search_bar[0].send_keys('visual market')
    time.sleep(2)
    search_bar[0].send_keys(Keys.RETURN)
    time.sleep(5)

def test_scrapData():
    # Scrape data from job listings
    job_listings = driver.find_elements(By.CSS_SELECTOR, "#main > div > div.scaffold-layout__list > div > ul")
    time.sleep(2)


    counter=0
    job_data = []
    for listing in job_listings:
        job_tags=listing.find_elements(By.TAG_NAME, "li")

        divs=job_tags[0].find_elements(By.TAG_NAME, "div")
        # print("first\n", divs)

        sub_div1=divs[0].find_elements(By.TAG_NAME, "div")


        for index in [sub_div1[1]]:
            job_data.append(index.text)

    print(job_data)

        # sub_div2 = sub_div1[1].find_elements(By.CLASS_NAME, "full-width artdeco-entity-lockup__title ember-view")

        # sub_div3 = sub_div1[1].find_elements(By.CLASS_NAME, "disabled ember-view job-card-container__link job-card-list__title")
       # print("Third\n", sub_div2)
        #sub_div3=sub_div2[1].find_element(By.TAG_NAME,"div")
        #mytext=sub_div3.find_element(By.CSS_SELECTOR, "#flex-grow-1 artdeco-entity-lockup__content ember-view")


        # print(sub_div3[0].get_attribute("class"))
        # print(sub_div3.text)

        # title=sub_div1[1][0].text
        # company=sub_div1[1][1].text
        # location=sub_div1[1][2].text

        # print(title,"|", company, "|", location)
            # for titles in enumerate(title):
            # job_location=cell.find_elements(By.CLASS_NAME, "").text
            # print("hello")
            # print(title[0])
    # for index in job_tags:
    #     job_title = index.find_element(By.CLASS_NAME, "job-card-list__entity-lockup artdeco-entity-lockup artdeco-entity-lockup--size-4 ember-view")
        
    #     # company_name = listing.find_element(By.CLASS_NAME,'job-card-container__primary-description').text
    #     # job_location = listing.find_element(By.CLASS_NAME,'job-card-container__metadata-item').text
    #     # job_data.append({'Job Title': job_title, 'Company Name': company_name, 'Job Location': job_location})

    # # # Print the scraped data

    # # df = pd.DataFrame(job_data)
    # print(job_title)

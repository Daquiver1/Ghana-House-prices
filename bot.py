from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from crawler import get_details
import requests
import time

# Used when polling.

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# PATH = "path to folder"
s = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# options.headless = false
driver = webdriver.Chrome(service=s, options=options)

URL = "https://meqasa.com/houses-for-sale-in-Accra.html?y=965793785&w=1"

# Log in
driver.get(URL)
driver.find_element(By.ID, "redi-modal-close").click()
get_details(driver.current_url)

next_button = driver.find_element(By.ID, "pagenumnext")
# It's a js button, so need to use execute script
driver.execute_script("arguments[0].click();", next_button)



def download_pasco(links, choice):
    """
    A function to download past questions.
    It takes in the links of the past questions and the users choice.
    Returns the path of the downloaded past question.
    """

    for i, v in links.items():
        if int(choice) == i:
            driver.get(v)  # Move to the url of users choice.

    file = driver.find_element(By.CLASS_NAME, "openPopUp")
    driver.execute_script(
        "arguments[0].click();", file
    )  # screen displayed is a frame, so adapts to a frame.
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.CLASS_NAME, "cboxIframe")
        )
    )
    wait.until(EC.element_to_be_clickable((By.ID, "download"))).click()
    driver.back()
    time.sleep(2)  # wait for file to be downloaded before moving on.
    file = newest(PATH)
    return file



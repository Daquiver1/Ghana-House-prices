from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
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
parent = driver.current_window_handle
driver.implicitly_wait(10)
driver.find_element(By.ID, "redi-modal-close").click()


next_button = driver.find_element(By.ID, "pagenumnext")
driver.execute_script("arguments[0].click();", next_button)



def link_of_pasco():
    """
    A function to retrieve the links of all the past questions displayed.
    output: A dictionary containing the index and the past question link.
    """

    page = requests.get(driver.current_url)

    soup = BeautifulSoup(page.content, "lxml")
    pasco1 = soup.find_all("a", class_="titleField")
    links = {}
    for i in range(1, len(pasco1) + 1):  # Starts from 1 not 0,
        links[i] = "https://balme.ug.edu.gh" + pasco1[i - 1]["href"]

    return links


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


if __name__ == "__main__":
    pass

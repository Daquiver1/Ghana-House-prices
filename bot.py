from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from crawler import get_details
import time


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.headless = true
driver = webdriver.Chrome(service=s, options=options)

URL = "https://meqasa.com/houses-for-sale-in-Accra.html?y=965793785&w=1"


driver.get(URL)
next_button = driver.find_element(By.ID, "pagenumnext")

for i in range(2):
    driver.execute_script("arguments[0].click();", next_button)
    value = f"pg{2+i}"
    print(value)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, value)))


source1 = driver.execute_script("return document.body.innerHTML;")
get_details(source1)


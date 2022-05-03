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
# options.headless = true
driver = webdriver.Chrome(service=s, options=options)

URL = "https://meqasa.com/houses-for-sale-in-Accra.html?y=965793785&w=1"

# Log in
driver.get(URL)
driver.find_element(By.ID, "redi-modal-close").click()
print(driver.current_url)
get_details(driver.current_url)

# next_button = driver.find_element(By.ID, "pagenumnext")
# # It's a js button, so need to use execute script
# driver.execute_script("arguments[0].click();", next_button)



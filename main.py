import requests
from bs4 import BeautifulSoup

# Get url
url = "https://meqasa.com/houses-for-sale-in-Accra.html?y=965793785&w=1"
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")

# Locate where it's stored
results = soup.find(id="pg1")
mqs_class = results.find_all(
    "div", class_="row mqs-featured-prop-inner-wrap clickable "
)

data_file = open("data/temp.txt", "w")

for i in mqs_class:
    description = i.find(["h2"]).get_text().strip()  # get description
    price = i.find(["p"], ["h3"]).get_text().strip()  # get the prices
    room_num = (
        i.find(["li"], ["bed"]).get_text().strip()
    )  # get the number of rooms
    # print(f"{description} {price} {room_num}")
    data_file.write(
        f"{description}, {price}, {room_num}"
    )  # store it in the text file
    data_file.write("\n")

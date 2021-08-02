import requests
from bs4 import BeautifulSoup

# Storing the webpage
url = "https://meqasa.com/houses-for-sale-in-East%20Legon"
page = requests.get(url)

# Locating where the prices,bedroom,baths and garages are stored
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="pg1")
mqs_class = results.find_all("div", class_= "mqs-prop-dt-wrapper")
# In results, find all p and ul tags with attribues h3 and prop-features
test = results.find_all(['p', 'ul'], ['h3', 'prop-features'])

# Storing the data into a text file named house_details
houses_file = open("houses_details.txt", "w")

for data in mqs_class: # Open the mqs-prop-dt-wrapper tag class
    for instances in test:
        trial = instances.get_text()
        #count += 1, there are 534 instances, that's more than enough to train our model
        houses_file.writelines(trial)

# Removing the whitespaces
lines = []

with open("/content/houses_details.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            lines.append(line)
# Storing the data in a txt file but this time each
# entry is stored on a single line

houses_file2 = open("houses_details1.txt", "w")

for element in lines[:]:
    if element.startswith("P"):
        houses_file2.write("\n") #adds a newline
    houses_file2.write(element)
    houses_file2.write(", ")


"""
 Last notes

1. Ignore the data from line 483, so you can delete it.
2. The numbers represent price,bedrooms,showers, garages and area in m2.
3. After going through the docs throughly I've realized I could have done this more efficiently and with less lines, but am tired. Next time.

"""

import re
from bs4 import BeautifulSoup


def get_details(source, val):
    """
    A function to get the description, prices and room number of houses"

    arguments: The page source. Type = String
    output: A text file storing the description, prices and room num separated
    by a comma.

    """

    soup = BeautifulSoup(source, "lxml")
    results = soup.find(id=val)
    mqs_class = results.find_all(
        "div", class_=re.compile("row mqs-featured-prop-inner-wrap clickable ")
    )

    data_file = open("data/temp.txt", "w")
    for i in mqs_class:
        # iterate through the values and store in text file
        description = i.find(["h2"]).get_text().strip()
        price = i.find(["p"], ["h3"]).get_text().strip()
        room_num = i.find(["li"], ["bed"]).get_text().strip()
        data_file.write(f"{description}, {price}, {room_num}")
        data_file.write("\n")

    data_file.close()


if __name__ == "__main__":
    pass

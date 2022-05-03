import requests
from bs4 import BeautifulSoup


def get_details(source):
 
    soup = BeautifulSoup(source, "lxml")
    results = soup.find(id="listview")
    mqs_class = results.find_all("div", class_=re.compile("row mqs-featured-prop-inner-wrap clickable "))


    data_file = open("/content/temp.txt", "w")
    for i in mqs_class:
        description = i.find(["h2"]).get_text().strip()
        price = i.find(["p"], ["h3"]).get_text().strip()
        room_num = i.find( ["li"], ["bed"]).get_text().strip()
        print(f"{description} {price} {room_num}")    
        data_file.write(f"{description}, {price}, {room_num}")
        data_file.write("\n")

    data_file.close()
 

if __name__ == "__main__":
    pass

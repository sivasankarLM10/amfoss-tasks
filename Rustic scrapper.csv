## This is the main file which is used for scraping COVID-19 updates
import requests
from bs4 import BeautifulSoup

# You can also get data for specific countries by changing the URL
# For example
# for US: https://www.worldometers.info/coronavirus/country/us/
# for India: https://www.worldometers.info/coronavirus/country/india/

url = "https://www.worldometers.info/coronavirus/"
req = requests.get(url)
bsObj = BeautifulSoup(req.text, "html.parser")
data = bsObj.find_all("div",class_ = "maincounter-number")

print("Total Cases: ", data[0].text.strip())
print("Total Deaths: ", data[1].text.strip())
print("Total Recovered: ", data[2].text.strip())

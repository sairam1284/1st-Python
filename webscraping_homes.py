#Get the first page to extract page numbers
import requests, re
from bs4 import BeautifulSoup
import pandas as pd
import pdb
raw = requests.get("http://www.century21.com/real-estate/cambridge-ma-02139/LZ02139/?k=1")
c = raw.content
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div", {"class":"property-card-primary-info"})

l=[]
for item in all:
    d={}
    # pdb.set_trace()
    d["Address"] = item.find("div", {"class":"property-address"}).text.replace("\n", "").strip()
    d["Price"] = item.find("a", {"class":"listing-price"}).text.replace("\n", "").strip()
    d["City"] = item.find("div", {"class":"property-city"}).text.replace("\n", "").strip()
    if item.find("div", {"class":"property-sqft"}) == None:
        d["Property Size"] = "None Listed"
    else:
        d["Property Size"] = item.find("div", {"class":"property-sqft"}).text.replace("\n", "").strip()
    if item.find("div", {"class":"property-beds"}) == None:
        d["# of Beds"] ="None Listed"
    else:
        d["# of Beds"] = item.find("div", {"class":"property-beds"}).text.replace("\n", "").strip()
    if item.find("div", {"class":"property-baths"}) == None:
        d["# of Baths"] = "None Listed"
    else:
        d["# of Baths"] = item.find("div", {"class":"property-baths"}).text.replace("\n", "").strip()
    l.append(d)

df2 = pd.DataFrame(l)
print(df2)
df2.to_csv("Output.csv")



# address = []
# price = []
# city = []
# area=[]
# beds= []
# sqft = []
# baths = []
# realtor = []
# for item in all:
#     address.append(item.find("div", {"class":"property-address"}).text.replace("\n", "").strip())
#     price.append(item.find("a", {"class":"listing-price"}).text.replace("\n", "").strip())
#     city.append(item.find("div", {"class":"property-city"}).text.replace("\n", "").strip())
#     if item.find("div", {"class":"property-sqft"}) == None:
#         area.append("None Listed")
#     else:
#         area.append(item.find("div", {"class":"property-sqft"}).text.replace("\n", "").strip())
#     if item.find("div", {"class":"property-beds"}) == None:
#         beds.append("None Listed")
#     else:
#         beds.append(item.find("div", {"class":"property-beds"}).text.replace("\n", "").strip())
#     if item.find("div", {"class":"property-baths"}) == None:
#         baths.append("None Listed")
#     else:
#         baths.append(item.find("div", {"class":"property-baths"}).text.replace("\n", "").strip())
#     if item.find("div", {"class":"property-card-attribution"}) == None:
#         realtor.append("None Listed")
#     else:
#         realtor.append(item.find("div", {"class":"property-card-attribution"}).text.replace("\n", "").strip())
#
# df1 = pd.DataFrame({'price':price, 'address': address, 'city':city, 'area':area, 'beds':beds, 'baths':baths})
#
# print(df1)

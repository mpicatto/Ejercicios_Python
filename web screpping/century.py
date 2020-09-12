import requests
from bs4 import BeautifulSoup
import pandas
l=[]
base_url="http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
r=requests.get(base_url+str(0)+".html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content
soup=BeautifulSoup(c,"html.parser")
page_nr=soup.find_all("a",{"class":"Page"})[-1].text
for page in range(0,int(page_nr)*10,10):
    print(base_url+str(page)+".html")
    r=requests.get(base_url+str(page)+".html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    for item in all:
     d={}   
     d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
     d["Address"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
     d["Locality"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
     try:
        d["Beds"]=item.find("span",{"class":"infoBed"}).find("b").text
     except:
        d["Beds"]="none"
     try:
        d["Area"]=item.find("span",{"class":"infoSqFt"}).find("b").text
     except:
        d["Area"]="none"
     try:
        d["Full Baths"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
     except:
        d["Full Baths"]="none"
     try:
        d["Half Baths"]=item.find("span",{"class":"infoValueHalfBath"}).find("b").text
     except:
        d["Hals Baths"]="none"
     for column_group in item.find_all("div",{"class":"columnGroup"}):
        for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
            if "Lot Size" in feature_group.text:
                d["Lot Size"]=feature_name.text
     l.append(d)
df=pandas.DataFrame(l)
df.to_csv("realstate.csv")

import requests
from bs4 import BeautifulSoup
import csv
import unidecode


new_names=[]
links=[]
names=[]
dob_list=[]
website_url = requests.get("https://en.wikipedia.org/wiki/All-time_Chivas_USA_roster").text
soup = BeautifulSoup(website_url,'lxml')
ul = soup.findAll("ul")
for li in ul:
  li = soup.findAll("li")
  for a in soup.findAll("a",href=True):
    if a.find(class_="thumbborder"):
      continue
    if a.find(class_="flagicon"):
      continue
    if a.find(class_="tocnumber"):
      continue
    if a.find(class_="mw-jump-link"):
      continue
    if a.find(class_="mw-redirect"):
      continue
    if a.find(class_="external text"):
      continue
    if a["href"] not in links:
      if a["href"][:5]=="/wiki":
        links.append(a["href"])


bad_names=[]
i=0
c = 3
for link in links[4:227]:
  try:
    i+=1
    website_url = requests.get("https://en.wikipedia.org"+link).text
    soup = BeautifulSoup(website_url,'lxml')
    dob = soup.find("span", {"class": "bday"})
    dob_list.append(dob.text)
    name = soup.find("h1",{"id","firstHeading"})
    names.append(name.text)
  except Exception as e:
    print("CANT FIND DOB"+link)
    bad_names.append(link)
    print(links[i+c])
    del links[i+c]
    c -= 1

for name in names:
  new_names.append(unidecode.unidecode(name))
d = dict(zip(new_names,dob_list))

print(d.keys())


with open("CHIVAS.csv","w+",newline="") as file:
  writer = csv.writer(file)
  for key,value in d.items():
    writer.writerow([key,value])
  


  


    



    




                             


            

    





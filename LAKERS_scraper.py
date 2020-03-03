import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


website_url = requests.get("https://www.basketball-reference.com/teams/LAL/").text #Edit this URL
soup = BeautifulSoup(website_url,'lxml')
div = soup.find("div", {"id": "div_LAL"})
bad_char=['*']
name_list=[]
tr=[]
th=[]
links=[]
name_list=[]
dob_list=[]
year_list=[]
for table in div:
    for tbody in table:
        tbody = table.find("tbody")
    try:
        for tr in tbody:
            tr = tbody.find_all("tr")
            tr.append(tr)
 
    except:
        pass
for th in tr:
    try:
        th = th.find(("th", {"class": "left"}))
        th.append(th)
    except:
        pass
for a in th:
    try:
        a = a.find("a")
        link = a.attrs['href']
        if int(link[-9:-5]) > 1964:
            url = "https://www.basketball-reference.com"+link
            links.append(url)
    except:
        pass


for link in links:
    website_url = requests.get(link).text
    soup = BeautifulSoup(website_url,'lxml')
    table = soup.find("table", {"id": "roster"})
    tbody = table.find("tbody")
    for tr in tbody:
        td = tr.find("td")
        try:
            dob = tr.find("td", {"data-stat": "birth_date"})
            dob = dob.text
            a = td.find("a")
            name = a.text
            name_list.append(name)
            dob_list.append(dob)
            year_list.append(link[-9:-5])
        except:
            pass

    pre_final_list=zip(name_list,dob_list,year_list)
    final_list=[]
    for item in pre_final_list:
        if item not in final_list:
            final_list.append(item)
    with open('LAKERS_players.csv', 'w',encoding='utf-8', newline='') as file: #Change the name of this csv file to whatever you like
        writer = csv.writer(file)
        for item in final_list:
            writer.writerow(item)
            

    





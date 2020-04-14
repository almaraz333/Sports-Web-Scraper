import time
import unidecode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import requests
import csv



file = 'FILE.csv' #CSV File
dob_list=[]
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

browser = webdriver.Firefox()
browser.get('https://basketball.realgm.com/')

search_box = browser.find_element_by_xpath('//*[@id="searchfield"]')
delay = 3

with open(file,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    writer = csv.writer(csvfile)
    for row in reader:
        if row[1] == "Name":
            pass
        else:
            try:
                browser.find_element_by_xpath('//*[@id="searchfield"]').send_keys(row[1])
                browser.find_element_by_xpath('//*[@id="searchfield"]').send_keys(Keys.ENTER)
                time.sleep(6)
                dob_link = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/p[2]/a") 
                split_dob = dob_link.text.split()
                if split_dob[0] in months:
                    dob_list.append(dob_link.text)
                    print(dob_link.text)
                else:
                    dob_link = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/p[3]/a")
                    dob_list.append(dob_link.text)
                    split_dob = dob_link.text.split()
                    if split_dob[0] in months:
                        dob_list.append(dob_link.text)
                        print(dob_link.text)
                    else:
                        dob_link = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/p[1]/a")
                        dob_list.append(dob_link.text)
                        print(dob_link.text)
           
            except:
                try:
                    url = requests.get(browser.current_url).text
                    soup = BeautifulSoup(url, 'lxml')
                    tables = soup.findAll("tbody")
                    table = tables[0]
                    tr = table.findAll("tr")
                    has_college = []
                    for item in tr:
                        td = item.findAll("td")
                        college = td[-2].text
                        name = td[0]
                        a = name.find("a")
                        href = a['href']
                        
                        for item in td:
                            if college == row[8]:
                                browser.get("https://basketball.realgm.com" + href)
                                time.sleep(6)
                                dob_link = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/p[2]/a")
                                split_dob = dob_link.text.split()
                                if split_dob[0] in months:
                                    dob_list.append(dob_link.text)
                                    print(dob_link.text)
                                    has_college.append(dob_link.text)
                                    break
                                else:
                                    dob_link = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/p[5]/a")
                                    dob_list.append(dob_link.text)
                                    print(dob_link.text)
                                    has_college.append(dob_link.text)
                                    break
                            else:
                                pass
                    if len(has_college) == 0:
                            print("College Doesn't Match " + row[1] )


                        
                except:
                    print("ERROR")




browser.quit()
    






    



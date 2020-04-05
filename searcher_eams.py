import time
import unidecode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import csv



file = 'FILE.csv'
hascase=[]


browser = webdriver.Firefox()
browser.get('https://eams.dwc.ca.gov/WebEnhancement/InjuredWorkerFinder')

firstname = browser.find_element_by_id('firstname')
lastname = browser.find_element_by_id('lastname')
email = browser.find_element_by_id('email')
reason = browser.find_element_by_xpath("/html/body/div[1]/div/div/form/table/tbody/tr[10]/td/select/option[3]")
nextbutton = browser.find_element_by_xpath("/html/body/div[1]/div/div/form/table/tbody/tr[11]/th/input[3]")

firstname.send_keys("Joe")
lastname.send_keys("Mama")
email.send_keys("sdgadsgadg@adgagasd.net")
reason.click()
nextbutton.click()

dob = browser.find_element_by_id('dob')
firstname = browser.find_element_by_id('firstname')
lastname = browser.find_element_by_id('lastname')
search = browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/form/p/input[3]")


i=0
with open(file,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    writer = csv.writer(csvfile)
    try:
        for row in reader:
            try:
                name = row[2].split()#Split Row of Full Name
                first = name[0][0]
                last = name[1:]
                browser.find_element_by_id("firstname").send_keys(Keys.CONTROL + "a")
                browser.find_element_by_id("firstname").send_keys(Keys.DELETE)
                browser.find_element_by_id("lastname").send_keys(Keys.CONTROL + "a")
                browser.find_element_by_id("lastname").send_keys(Keys.DELETE)
                browser.find_element_by_id("dob").send_keys(Keys.CONTROL + "a")
                browser.find_element_by_id("dob").send_keys(Keys.DELETE)
                browser.find_element_by_id('firstname').send_keys(first)
                browser.find_element_by_id('lastname').send_keys(last)
                browser.find_element_by_id('dob').send_keys(row[4][:6]+"19"+row[4][6:]) #Row of DOB
                browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/form/p/input[3]").click()
                try:
                    browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/table")
                    print("YES")
                except:
                    print("NO")
            except:
                print(row[3]+" 2")
    except:
        print(row[3]+" 3")
            


            
browser.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup, Comment
import requests
import csv
import re
from datetime import datetime


def getInfo(player_link, name):    #Find the "Game Logs" section of the page and check if last game played was 2018 or earlier
    website_url = requests.get(player_link).text
    soup = BeautifulSoup(website_url,'lxml')
    first_name_appearence = soup.find("h1", string=name)
    info_div = first_name_appearence.parent
    info = info_div.find_all('p')
    for item in info:
        if item.find('strong', text='Born:'):
            birth_place = (item.find('strong', text='Born:').next_sibling.next_sibling.next_sibling.next_sibling.text)
            birth_place = "".join(birth_place.split())
            birth_place = birth_place[2:]
            birth_place = birth_place.split(',')
            birth_city = birth_place[0]
            birth_state = birth_place[1]
        if item.find('strong', text='College'):
            college = item.find('strong', text='College').next_sibling.next_sibling.text

    gamelog = soup.find(text='Gamelogs').findNext('ul')
    games = gamelog.find_all('li')
    return [first_name_appearence.text,games[-1].text, birth_city,birth_state, college]

    
def writePlayer(list_of_players): #Write players to file called "fooball_players_years_over_3.csv"
    with open('fooball_players_years_over_3.csv', 'w',encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for item in list_of_players:
            writer.writerow(item)
        file.close()


def getPlayers():
    players_names=[]
    players_list=[]
    website_url = requests.get("https://www.pro-football-reference.com/teams/").text  #Initial site
    soup = BeautifulSoup(website_url,'lxml')
    teams_table = soup.find_all('tbody')
    team_names = teams_table[0].find_all("a", href=re.compile(r"^/teams"))  #Find all links that link to a team page 
    for team_name in team_names:
        website_url = requests.get("https://www.pro-football-reference.com" + team_name['href']).text #Get team page of each active team
        soup = BeautifulSoup(website_url,'lxml')
        team = team_name.text
        print(team) #Prints team name to keep track of how far the program is through the list 
        team_years = soup.find_all("th", {"data-stat": "year_id"}) #Find all years team played 
        for year_link in team_years:
            if year_link.text != 'Year' and int(year_link.text) <= 2019: #Loop though all years 2005-2019
                print(year_link.text) #Prints year to keep track of how far the program is through the team
                website_url = requests.get("https://www.pro-football-reference.com"+team_name['href']+year_link.text+"_roster.htm").text
                soup = BeautifulSoup(website_url,'lxml')
                comments = soup.findAll(text=lambda text:isinstance(text, Comment))
                for comment in comments:
                    if 'table' in comment:
                        comment_soup = BeautifulSoup(comment, 'html.parser')
                        for tr in comment_soup.find_all('tr'):
                            td = tr.find_all('td')
                            if len(td) > 0:
                                try:
                                    name = td[0].text
                                    for letter in name:
                                        if letter == '+' or letter == '*':
                                            name = name.replace(letter, '')
                                    if name not in players_names: #Find players who have not been added
                                        players_names.append(name)
                                        print("https://www.pro-football-reference.com"+td[0].find('a')['href'])
                                        player_info = getInfo("https://www.pro-football-reference.com"+td[0].find('a')['href'], name)
                                        player = []
                                        age = round((datetime.today() - (datetime.strptime(td[8].text, '%m/%d/%Y'))).days/365)
                                        player_info.append(age)
                                        player_info.append(td[8].text)
                                        player.extend((player_info))
                                        players_list.append(player)
                                except:   
                                    pass
    return players_list
                                    

                    
                    
                
            
writePlayer(getPlayers())


        

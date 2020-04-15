# Sports-Web-Scraper
A web-scraper in Python that parses through a specified site using Beautiful Soup to extract data about players in an automated fashion so it is not necessary to look up the info by hand. 

NFL-search.py gathers data from https://www.pro-football-reference.com on only players who have played >3 years and have played there last game between 2006 and 2018 and creates a CSV file with the data for easy readability. 

Lakers-scraper.py is a web scraper that can be changed to scrape any team on the basketball, football, or hockey reference site by changing the website URL. 

searcher_eams.py searches the EAMS database for names in a CSV file in a specified row for the first name, last name, and DOB 
and prints a "YES" or "NO" for each person. 

soccer_dob.py pulls the DOB for each person from a specified Wikipedia link that are stored in a list format. Some names link to a page that the program cannot pull the DOB from. In this case it returns an error message, adds the name to a list of "bad names", and it must be done manually.
This happens very rarely. 

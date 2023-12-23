import requests
import pandas as pd
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
my_url = "https://www.premierleague.com/"

my_headers = {'User-Agent':user_agent}
response=requests.get(my_url,headers=my_headers)
data = response.content # The data u need

from bs4 import BeautifulSoup
soup = BeautifulSoup(data,"html.parser")

Updates = []

list1=soup.findAll('span',{"class":"media-thumbnail__title"})
for elem in list1:
    if elem.string != None and len(elem.string)>20 :
        Updates.append(elem.string.strip())

my_dict = {'Updates':Updates}
df = pd.DataFrame(my_dict)
df.to_csv('PremierLeague.csv')

Tabs = []

list2 = soup.findChildren('a')
for i in list2:
    if i.text == "Home" or i.text =="Fixtures" or i.text== "Results" or i.text == "Tables" or i.text == "Transfers" or i.text == "Stats" or i.text == "News":
        Tabs.append(i.text)
new_dict = {'Tabs':Tabs}
df1 = pd.DataFrame(new_dict)
df1.to_csv('Tabs.csv')

Buttons = []

list3 = soup.findAll('span',{"class":"navText"})
for button in list3:
    Buttons.append(button.text)

dict2 = {'Buttons':Buttons}
df2 = pd.DataFrame(dict2)
df2.to_csv('PremierLeague_Buttons.csv')

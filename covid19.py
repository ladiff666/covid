import requests 
from bs4 import BeautifulSoup 
from fake_useragent import UserAgent
import json 

user_agent = UserAgent() 
url = "https://www.worldometers.info/coronavirus/" 
page = requests.get(url, headers={"user-agent": user_agent.chrome})
soup = BeautifulSoup(page.text,'html.parser')
def get_data():
        numbr =soup.findAll('span',limit=7)
        total_cases = numbr[4].text
        death = numbr[5].text 
        Recovered = numbr[6].text
        nmbr2 =soup.find_all('div',class_="number-table-main")
        Active_Cases  = nmbr2[0].text 
        Closed_Cases = nmbr2[1].text
        tr =soup.findAll('tr')
        nmbrs = []
        for t in tr[9:224] :
                for td in t:
                        if td != '\n':
                                nmbrs.append(td.text)
                nmbrs.append("_")
        n_ = []
        list_n = []
        for n in nmbrs :
                if n != '_':
                        n_.append(n)
                elif n == '_' :
                        
                        list_n.append(n_)
                        n_ = []
        for i in range(0,len(list_n)):
                        list_n[i] = list_n[i][1:]
                        
        list_n = sorted(list_n, key=lambda colonnes: int(colonnes[1].replace(",", "")),reverse = True)

        return list_n,total_cases,death,Active_Cases,Recovered,Closed_Cases
def get_columns():
        columns = []
        a = soup.find('tr')
        for t in a :
                if t != '\n' :
                        columns.append(t.text)
        columns = columns[:-4]
        columns[-2] = columns[-2].splitlines()[0] + columns[-2].splitlines()[1]

        return columns

if __name__ == '__main__':
        data = get_columns()
        columns_name = get_columns()
        print(data)
        print(columns_name)
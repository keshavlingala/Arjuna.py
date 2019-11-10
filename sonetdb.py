import requests
from html.parser import HTMLParser
h=HTMLParser()
import bs4 as b
r=requests.post('http://teleuniv.net/sonetDB.php',{'roll':input()})
soup=b.BeautifulSoup(r.text,'html.parser')
for i in soup.find_all('input'):
    print(i.get('id'),i.get('class'),i.get('value'))
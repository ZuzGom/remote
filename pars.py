import requests
from bs4 import BeautifulSoup
# funnkcja która zwraca name, line1, line2 tak aktualne jak się tylko da
def track():
    try:
        page = requests.get('https://github.com/ZuzGom/remote/blob/main/url.txt')
    except requests.exceptions.ConnectionError:
        linia = None
    else:       
        soup = BeautifulSoup(page.content, 'html.parser')
        linia = str(soup.find("td", {"id": "LC1"})).split()[-1][9:-5]                        
    return linia
print(track())
import requests
from bs4 import BeautifulSoup 



def main():
    url = "https://www.autovit.ro/"
    f = requests.get(url)
    soup = BeautifulSoup(f.content, 'lxml')
    print(soup)

if __name__=="__main__":
    main()
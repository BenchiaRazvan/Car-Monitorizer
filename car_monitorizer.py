import requests
from bs4 import BeautifulSoup 


url = "https://www.autovit.ro/"
f = requests.get(url)
soup = BeautifulSoup(f.content, 'lxml')


def best_offer():

    cars = soup.find('section', {
        'class' : 'e1a4cfxe1'
    }).find_all('a')

    informations_list = []

    car_title = soup.find('h3', { 'class' : 'e1lmj3dz0'}).text
    car_price = soup.find('div', { 'class': 'evznqyf1'}).text

    car_informations = soup.find('ul', { 'class': 'optimus-app-13n8fh9 e16henwp0'}).find_all('span')
    for car in car_informations:
        informations_list.append(car.text)

    car_year = informations_list[0]

    for inf in informations_list:
        if(inf.endswith('km')):
            car_km = inf

    json_output = {
        'name': car_title,
        'price': car_price,
        'year': car_year,
        'km' : car_km,
    }
    print(json_output)      

def daily_offer():
    print("test")

def main():
    best_offer()

if __name__=="__main__":
    main()
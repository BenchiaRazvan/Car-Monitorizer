import requests
from bs4 import BeautifulSoup
import re
import json


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
    informations_list.append(json_output)
    return informations_list


def daily_offer():

    offer = soup.find_all('section', { 'class' : 'optimus-app-fdjy12 ek2z86x0'})
    
    output_json = []
    for j in offer:
        
        offer2 = j.find_all('span', 'optimus-app-3tn7f8')
        

        car_name = j.find('h3', {'class' : 'e1lmj3dz0'}).text
        car_price = j.find('div', { 'class' : 'evznqyf1'}).text

        for i in j.find_all('span', 'optimus-app-3tn7f8'):
            properties = i.text

            match = re.match(r'.*([1-2][0-9]{3})', i.text)
            if match is not None:
                car_year = match.group(1)
            if(properties.endswith('km')):
                car_km = properties
            elif(properties.endswith('cm3')):
                car_engine = properties

        json = {
            'name' : car_name,
            'price' : car_price,
            'km' : car_km,
            'year' : car_year,
            'engine' : car_engine
        }
        output_json.append(json)
    return output_json


def json_file():

    daily_json = []
    best_json = []
    final_json = []
    with open('data.json', 'w') as outfile:
        daily_json = daily_offer()
        best_json = best_offer()
        final_json = daily_json + best_json
        print(final_json)
        json.dump(final_json, outfile)

def main():

    json_file()
    
if __name__=="__main__":
    main()
from typing import final
import requests
from bs4 import BeautifulSoup
import time
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

    return json_output


def daily_offer():

    offer = soup.find_all('section', { 'class' : 'optimus-app-fdjy12 ek2z86x0'})


    output_json = []

    for j in offer:
        
        span_elements = j.find_all('section', { 'class' : 'optimus-app-7kiohr e2nxjc60'})

        for i in span_elements:
            
            car_name = i.find('h3', {'class' : 'e1lmj3dz0 optimus-app-g6vljw'}).text
            car_price = i.find('div', { 'class' : 'evznqyf1 optimus-app-5t16gy'}).text

            
            properties = i.find('ul', {'class' : 'optimus-app-13n8fh9 e16henwp0'}).find_all('li')

            json = {
                'name' : car_name,
                'price' : car_price,
                'km' : properties[0].text,
                'year' : properties[1].text,
                'engine' : properties[2].text
            }
            output_json.append(json)
    return output_json


def json_file():

    with open('data.json', 'r+') as outfile:
        if(outfile.read() == ''):
            outfile.write(json.dumps([]))
        outfile.close()


    current_day_json = daily_offer()
    current_day_json.append(best_offer())

    with open('data.json', 'r') as outfile:
        prev_json = json.load(outfile)
        outfile.close()

    json_object = json.dumps(current_day_json + prev_json, indent = 4)

    with open('data.json', 'w') as outfile:
        outfile.write(json_object)
        outfile.close()
       

def main():

    while True:
        json_file()
        time.sleep(3600 * 24)
    
if __name__=="__main__":
    main()
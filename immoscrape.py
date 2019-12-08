#module import#
from bs4 import BeautifulSoup
import requests
import csv
import time

#prepare csv#
exportcsv = open('Immoscrape.csv', 'w', newline='')
csvwriter = csv.writer(exportcsv)
csvwriter.writerow(['Ad ID', 'Address', 'Amount', 'Area', 'Rooms', 'Distance', 'Link'])

#define target site#
for i in range(5):
    source = requests.get('https://www.immobilienscout24.de/Suche/S-2/P-{}/Wohnung-Kauf/Fahrzeitsuche/Berlin/-/229458/2511136/-/1276003001/60/-/-/EURO--150000,00'.format(i+1)).text
    soup = BeautifulSoup(source, 'lxml')

    #scrape data#
    for results in soup.find_all('div', class_ ='grid-item result-list-entry__data-container'):
        ID = results.find('button', {"title": 'Auf der Karte anzeigen'})
        print(ID['data-result-id'])
        address = results.find('div', class_='font-ellipsis').text
        address = address.replace(',', '')
        print(address)

        grid = results.find('div', class_='grid grid-flex gutter-horizontal-l gutter-vertical-s').text
        amount = grid.split(' €')[0]
        amount = amount.replace('.', '')
        area = grid.split('€')[1]
        area = area.split('m²')[0]
        area = area.replace('Kaufpreis', '')
        area = area.replace('Preis', '')
        area = area.replace(',', '.')

        try:
            rooms = grid.split('Wohnfläche')[1]
            rooms = rooms.split('.')[1]
        except Exception as e:
            rooms = 'N/A'

        print(amount)
        print(area)
        print(rooms)

        distance = results.find('div', class_='float-left').text
        distance = distance.split(' m')[0]
        print(distance)

        link = f"https://www.immobilienscout24.de/expose/{ID['data-result-id']}"
        print(link)

        print()

        #export to csv#
        csvwriter.writerow([ID['data-result-id'], address, amount, area, rooms, distance, link])

        time.sleep(1)

exportcsv.close()

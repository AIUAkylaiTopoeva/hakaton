# хакатон среднее(задание 2)
import requests
from bs4 import BeautifulSoup
import csv
import lxml
def write_to_csv(data):
    with open('car.csv', 'a') as file:
        write= csv.writer(file)
        write.writerow([data['title'], data['price'], data['description']])


def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    products = soup.find('div', class_='search-results-table').find_all('div', class_='list-item list-label')
    for product in products:
        title= product.find('h2', class_='name').text.strip()
        price= product.find('div', class_='block price').find('p', class_='price').text.strip()
        description= product.find('p', class_='year-miles').text.strip()+''+ product.find('p', class_='body-type').text.strip()+product.find('p', class_='volume').text.strip()
        dict_={'title':title, 'price': price, 'description': description}
        write_to_csv(dict_)
# get_data(get_html('https://www.mashina.kg/commercialsearch/all/'))

with open('car.csv', 'w') as file:
    write= csv.writer(file)
    write.writerow(['title', 'description', 'price'])

def main():
    url='https://www.mashina.kg/commercialsearch/all/'
    pages= '?page='
    html= get_html(url)
    number = 166
    # get_data(html)
    i=1
    while i <= number:
        url_with_page = url + pages+ str(i)
        i+=1
        html=get_html(url_with_page)
        get_data(html)
main()
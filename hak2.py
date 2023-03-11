# хакатон легкое(задание 1)

import requests
from bs4 import BeautifulSoup
import lxml
import csv 

def write_to_csv(data):
    with open('data.csv', 'a') as file:
        write= csv.writer(file)
        write.writerow([data['title'], data['image'], data['price']])



def get_html(url):
    response= requests.get(url)
    # print(response)
    return response.text

def get_total_pages(html):
    soup= BeautifulSoup(html , 'lxml')
    # page_list= soup.find('div', class_='pager-wrap').find('ul', class_='pagination pagination-sm').find_all('li')
    # print(page_list)
    # last_page = page_list[-1].text
    # print(last_page)
    # return int(last_page)

# print(get_total_pages(get_html('https://www.kivano.kg/product/index?search=телефон')))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    products= soup.find('div', class_='list-view').find_all('div', class_='item')
    # print(products)
    for product in products:
        title= product.find('div', class_= 'listbox_title oh').find('strong').text
    # print(title)
        image='https://www.kivano.kg/' +product.find('img').get('src')
        price= product.find('div', class_='listbox_price').find('strong').text
        # description=product.find('div', class_='product_text pull-left').text.replace(title , '').strip()
        dict_= {'title': title, 'image':image, 'price': price}
        write_to_csv(dict_)


with open('data.csv', 'w') as file:
    write= csv.writer(file)
    write.writerow(['title    ', 'image     ', 'price   '])


def main(): 
    url='https://www.kivano.kg/mobilnye-telefony'
    pages= '?page='
    html= get_html(url)
    number = 25
    # get_data(html)
    i=1
    while i <= number:
        url_with_page = url + pages+ str(i)
        i+=1
        html=get_html(url_with_page)
        get_data(html)
        print(i)

main()
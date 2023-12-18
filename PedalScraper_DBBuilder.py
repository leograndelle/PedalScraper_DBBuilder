#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
from bs4 import BeautifulSoup
import sqlite3
import time
import math

def connect_db():
    '''Connects to the 'pedals' SQLite database.'''
    conn = sqlite3.connect('pedals.db')
    c = conn.cursor()
    return conn, c


def create_table(conn, c):
    '''Creates a 'pedals' table in the connected database if it doesn't exist.'''
    c.execute('''CREATE TABLE IF NOT EXISTS pedals (
             name TEXT,
             price REAL,
             stars REAL,
             n_reviews INT
             )''')
    conn.commit()


def get_soup(url):
    '''Retrieves and returns a BeautifulSoup object from the provided URL.'''
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def pagination(url):
    '''Determines the number of pages based on the total number of pedals and pedals per page.'''
    soup = get_soup(url)
    product_count = soup.find('p', {'class':'o-number-results'}).text.split()
    total_pedals = int(product_count[-1])
    pedals_per_page = int(product_count[-3])
    pages = math.ceil(total_pedals / pedals_per_page)
    return pages


def scrape_to_db(url):
    '''Scrapes pedal data from multiple pages and stores it in the 'pedals' database.'''
    for page in range(pagination(url)):
        soup = get_soup(f'{url}?pageNumber={page + 1}')
        content = soup.find_all('div', {'class':'o-tile'})

        for data in content:
            name = data.find('div', {'class':'o-tile__row o-tile__title undefined no-border'}).text
            price = data.find('span').text.replace('£','')

            reviews = data.find('div', {'class':'o-tile__row o-tile__reviews'})
            n_reviews = reviews.text.strip('[]') if reviews else '0'

            star_element = data.find('div', {'class':'o-review-stars'})
            stars = star_element.get('title') if star_element else 'N/A'

            c.execute('INSERT INTO pedals VALUES (?, ?, ?, ?)', (name, price, n_reviews, stars))
            conn.commit() # Commits the changes to the database
        time.sleep(3)
    return 


if __name__ == '__main__':
    conn, c = connect_db()
    create_table(conn, c)
    url = 'https://www.andertons.co.uk/guitar-pedals'
    scrape_to_db(url)
    conn.close()


#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from pushover import Client


class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR


def get_page_html(url):
    driver = webdriver.Firefox()
    driver.get(url)
    html = driver.execute_script("return document.documentElement.outerHTML")
    driver.close()
    return html


def check_item_in_stock(html):
    sel_soup = BeautifulSoup(html, 'html.parser')
    out_of_stock_divs = sel_soup.findAll("div", {"class": "btn btn-grey"})
    out_of_stock_span = out_of_stock_divs[0].findAll("span", {"class": "text"})

    return out_of_stock_span[0].text


def check_inventory():
    url = "https://www.public-cyprus.com.cy/product/sony-playstation-5-konsola-leyko/prod10238545pp/"    # standard edition
    url2 = "https://www.public-cyprus.com.cy/product/sony-playstation-5-digital-edition/prod10810253pp/" # digital edition
    html = get_page_html(url)
    html2 = get_page_html(url2)
    stock = check_item_in_stock(html)
    stock2 = check_item_in_stock(html2)

    # Standard
    if stock == "εξαντλήθηκε!":
        print("Standard editon: " + bcolors.FAIL + "Out of stock" + bcolors.RESET)
    elif stock == "διαθέσιμο":
        print(bcolors.OK + "In stock" + bcolors.RESET)

        notify("PS5 standard in stock")

    # Digital
    if stock2 == "εξαντλήθηκε!":
        print("Digital  editon: " + bcolors.FAIL + "Out of stock" + bcolors.RESET)
    elif stock2 == "διαθέσιμο":
        print(bcolors.OK + "In stock" + bcolors.RESET)

        notify("PS5 digital in stock")


def notify(message):

    client = Client("ugp3zjw5if8qmwqefpra5r3cc28ny1", api_token="a8dux9o4r8xyxfiai7j2dep29htzn7")
    client.send_message(message, title="!--PS5 STOCK--!")


while True:
    check_inventory()
    time.sleep(60)

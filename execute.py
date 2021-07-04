#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import time
from selenium import webdriver
from bs4 import BeautifulSoup


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
    url = "https://www.public-cyprus.com.cy/product/sony-playstation-5-konsola-leyko/prod10238545pp/"
    html = get_page_html(url)
    stock = check_item_in_stock(html)

    if stock == "εξαντλήθηκε!":
        print(bcolors.FAIL + "Out of stock" + bcolors.RESET)
    elif stock == "διαθέσιμο":
        print(bcolors.OK + "In stock" + bcolors.RESET)


while True:
    check_inventory()
    time.sleep(60)

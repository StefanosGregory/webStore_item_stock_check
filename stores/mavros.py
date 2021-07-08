#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from tools.consoleBcolors import bcolors
from tools.notify import notify
import requests
import re


def check_inventory():
    # Stock Checker standard, digital
    print("~Mavros:")

    ps5 = ["https://www.mavroslarnaca.com/product-page/ps5-console",
           "https://www.mavroslarnaca.com/product-page/ps5-console-digital-edition"]
    flag = "Standard edition: "

    for item in ps5:
        try:
            response = requests.get(item).text
            soup = BeautifulSoup(response, "html.parser")
            status = soup.body.findAll(text=re.compile("Buy Now"))

            if not status:
                print(flag + bcolors.FAIL + "Out of stock" + bcolors.RESET)
            else:
                print(flag + bcolors.OK + "In stock at Mavros" + bcolors.RESET)

                notify("PS5 " + flag + " in stock at Mavros")

            flag = "Digital  edition: "
        except:
            print(flag + bcolors.WARNING + "Error searching for item" + bcolors.RESET)

            # notify("Error PS5 " + flag + " Mavros")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

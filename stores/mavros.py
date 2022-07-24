#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from pythonConsoleConfigs.Font import Color

from tools.log import cPrint
from tools.notify import notify
import requests
import re


def check_inventory():
    # Stock Checker standard, digital
    cPrint(["", "~Mavros:"], Color.MAGENTA)

    ps5 = ["https://www.mavroslarnaca.com/product-page/ps5-console",
           "https://www.mavroslarnaca.com/product-page/ps5-console-digital-edition"]
    flag = "Standard edition: "

    for item in ps5:
        try:
            response = requests.get(item).text
            soup = BeautifulSoup(response, "html.parser")
            status = soup.body.findAll(text=re.compile("Buy Now"))

            if not status:
                cPrint([flag, "Out of stock"], Color.RED)
            else:
                cPrint([flag, "In stock at Mavros"], Color.GREEN)
                notify("PS5 " + flag + " in stock at Mavros")

            flag = "Digital  edition: "
        except:
            cPrint([flag, "Error searching for item"], Color.YELLOW)
            # notify("Error PS5 " + flag + " Mavros")

    cPrint(["", "~" * 30], Color.MAGENTA)


check_inventory()

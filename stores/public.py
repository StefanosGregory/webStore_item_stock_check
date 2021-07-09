#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from tools.consoleBcolors import bcolors
from tools.notify import notify
import requests


def check_inventory():
    # Stock Checker standard, digital
    print("~Public:")

    ps5_link = "https://www.public-cyprus.com.cy/cy/common/updateProductInfo.jsp?product="
    ps5 = ["prod10238545pp", "prod10810253pp", "prod13802366pp", "prod13923508pp"]
    ps5_names = ["Standard edition: ", "Digital  edition: ", "Ratchet  edition: ", "2 Games  edition: "]
    
    for item in range(len(ps5)):
        try:
            response = requests.get(ps5_link + ps5[item]).json()
            stock = response['productInfo'][0]['stockRule']

            if stock == "εξαντλήθηκε!":
                print(ps5_names[item] + bcolors.FAIL + "Out of stock" + bcolors.RESET)
            else:
                print(ps5_names[item] + bcolors.OK + "In stock at Public" + bcolors.RESET)

                notify("PS5 " + ps5_names[item] + " in stock at Public")

        except:
            print(ps5_names[item] + bcolors.WARNING + "Error searching for item" + bcolors.RESET)
            
            notify("Error PS5 " + ps5_names[item] + " public")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")





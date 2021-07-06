#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from tools.consoleBcolors import bcolors
from tools.notify import notify
import requests


def check_inventory():
    # Stock Checker standard, digital
    print("~Public:")

    ps5_link = "https://www.public-cyprus.com.cy/cy/common/updateProductInfo.jsp?product="
    ps5 = ["prod10238545pp", "prod10810253pp"]
    flag = "Standard edition: "
    
    for item in ps5:
        try:
            response = requests.get(ps5_link + item).json()
            stock = response['productInfo'][0]['stockRule']

            if stock == "εξαντλήθηκε!":
                print(flag + bcolors.FAIL + "Out of stock" + bcolors.RESET)
            else:
                print(flag + bcolors.OK + "In stock at Public" + bcolors.RESET)

                notify("PS5 " + flag + " in stock at Public")

            flag = "Digital  edition: "
        except:
            print(flag + bcolors.WARNING + "Error searching for item" + bcolors.RESET)
            
            notify("Error PS5 " + flag + " public")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




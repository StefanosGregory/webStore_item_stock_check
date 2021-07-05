#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import time
from pushover import Client
import requests


class bcolors:
    # Command line font Color
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR


def check_inventory():
    # Stock Checker standard, digital
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
                print(flag + bcolors.OK + "In stock" + bcolors.RESET)

                notify("PS5 " + flag + " in stock")

            flag = "Digital  edition: "
        except:
            print(flag + bcolors.WARNING + "Error searching for item" + bcolors.RESET)
            
            notify("Error PS5 " + flag)


def notify(message):
    # Notification to my device
    client = Client("ugp3zjw5if8qmwqefpra5r3cc28ny1", api_token="a8dux9o4r8xyxfiai7j2dep29htzn7")
    client.send_message(message, "PS5")


while True:
    check_inventory()
    time.sleep(60)

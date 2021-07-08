from bs4 import BeautifulSoup
import requests
import re
from tools.consoleBcolors import bcolors
from tools.notify import notify


def check_inventory():
    # Stock Checker standard, digital
    print("~Sony:")

    ps5 = ["https://sonycentercy.com/playstation-5/2186-sony-playstation-5-0711719395003.html",    "https://sonycentercy.com/playstation-5/2187-sony-playstation-5-digital-edition-0711719395102.html"]
    flag = "Standard edition: "

    for item in ps5:
        try:
            response = requests.get(item).text
            soup = BeautifulSoup(response, "html.parser")
            status = soup.body.findAll(text=re.compile("Out-of-Stock"))
            if status:
                print(flag + bcolors.FAIL + "Out of stock" + bcolors.RESET)
            else:
                print(flag + bcolors.OK + "In stock at Sony" + bcolors.RESET)

                notify("PS5 " + flag + " in stock at Sony")

            flag = "Digital  edition: "
        except:
            print(flag + bcolors.WARNING + "Error searching for item" + bcolors.RESET)

            notify("Error PS5 " + flag + "sony")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
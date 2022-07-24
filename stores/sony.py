from bs4 import BeautifulSoup
import requests
import re

from tools.log import cPrint
from tools.notify import notify
from pythonConsoleConfigs.Font import Color


def check_inventory():
    # Stock Checker standard, digital
    cPrint(["", "~Sony:"], Color.MAGENTA)

    ps5 = ["https://sonycentercy.com/playstation-5/2186-sony-playstation-5-0711719395003.html",
           "https://sonycentercy.com/playstation-5/2187-sony-playstation-5-digital-edition-0711719395102.html"]
    flag = "Standard edition: "

    for item in ps5:
        try:
            response = requests.get(item).text
            soup = BeautifulSoup(response, "html.parser")
            status = soup.body.findAll(text=re.compile("Out-of-Stock"))
            if status:
                cPrint([flag, "Out of stock"], Color.RED)
            else:
                cPrint([flag, "In stock at Sony"], Color.GREEN)
                notify("PS5 " + flag + " in stock at Sony")

            flag = "Digital  edition: "
        except:
            cPrint([flag, "Error searching for item"], Color.YELLOW)
            notify("Error PS5 " + flag + "sony")

    cPrint(["", "~" * 30], Color.MAGENTA)


check_inventory()

from bs4 import BeautifulSoup
import requests
import re
from tools.consoleBcolors import bcolors
from tools.notify import notify


def check_inventory():
    # Stock Checker standard, digital
    print("~Kotsovolos:")

    ps5 = ["https://www.kotsovolos.gr/gaming-gadgets/playstation-5/konsola-ps5/214305-sony-ps5", "https://www.kotsovolos.gr/gaming-gadgets/playstation-5/konsola-ps5/216991-sony-ps5-digital"]
    ps5_names = ["Standard edition: ", "Digital  edition: "]

    for item in ps5:
        try:
            response = requests.get(item).text
            soup = BeautifulSoup(response, "html.parser")
            status = soup.body.findAll(text=re.compile(" 0 Προϊόντα"))
            print(status)
            # stock = response['productInfo'][0]['stockRule']
            #
            # if stock == "εξαντλήθηκε!" or stock == "προσωρινά εξαντλημένο":
            #     print(ps5_names[item] + bcolors.FAIL + "Out of stock" + bcolors.RESET)
            # else:
            #     print(ps5_names[item] + bcolors.OK + "In stock at Public" + bcolors.RESET)
            #
            #     notify("PS5 " + ps5_names[item] + " in stock at Public")

        except:
            print(ps5_names[item] + bcolors.WARNING + "Error searching for item" + bcolors.RESET)

            # notify("Error PS5 " + ps5_names[item] + " public")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

check_inventory()
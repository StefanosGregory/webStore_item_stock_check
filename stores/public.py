#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from pythonConsoleConfigs.Font import Color

from tools.log import cPrint
from tools.notify import notify


def check_inventory():
    # Stock Checker standard, digital
    cPrint(["", "~Public:"], Color.MAGENTA)

    ps5_link = "https://www.public.cy/public/v1/mm/stockRules?skuId="
    ps5 = ["1428499", "1530295", "1633212", "1629042"]
    ps5_names = ["Standard edition: ", "Digital  edition: ", "Ratchet  edition: ", "2 Games  edition: "]

    for item in range(len(ps5)):
        try:
            response = requests.get(ps5_link + ps5[item])

            result_json = response.json()
            stock_text = result_json['rules'][0]['deliveryRule']['displayText']

            if stock_text == "εξαντλήθηκε" or stock_text == "προσωρινά εξαντλημένο":
                cPrint([ps5_names[item], "Out of stock"], Color.RED)
            else:
                cPrint([ps5_names[item], "In stock at Public"], Color.GREEN)
                notify("PS5 " + ps5_names[item] + " in stock at Public")

        except:
            cPrint([ps5_names[item], "Error searching for item"], Color.YELLOW)
            # notify("Error PS5 " + ps5_names[item] + " public")
    cPrint(["", "~"*30], Color.MAGENTA)


check_inventory()

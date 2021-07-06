from pushover import Client


def notify(message):
    # Notification to my device
    client = Client("ua8hh7y8923wxhax5ofws8113ejafb", api_token="a4w5z5mt382yzrjrq2nrbnt57fcjao")
    client.send_message(message, "PS5")
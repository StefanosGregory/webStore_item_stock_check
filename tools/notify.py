from pushover import Client


def notify(message):
    # Notification to my device
    client = Client("Your setup", api_token="and here")
    client.send_message(message, "PS5")

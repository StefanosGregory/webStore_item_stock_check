from stores import bionic, public, sony, mavros
from tools.countdown import count

print("~Playstation 5 stock checker CY~\nExit -> ctrl+C on re-run section\n")

while True:
    public.check_inventory()  # check for stock in bionic store
    bionic.check_inventory()  # check for stock in public store
    sony.check_inventory()    # check for stock in sony store
    mavros.check_inventory()  # check for stock in mavros store
    count()  # re Run every 50sec
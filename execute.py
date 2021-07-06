from stores import bionic, public, sony
from tools.countdown import count

while True:
    public.check_inventory()  # check for stock in bionic store
    bionic.check_inventory()  # check for stock in bionic store
    sony.check_inventory()  # check for stock in sony store

    count()  # re Run every 60sec
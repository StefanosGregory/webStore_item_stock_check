from pythonConsoleConfigs.Font import Color

from stores import bionic, public, sony, mavros
from tools.countdown import count

while True:
    public.check_inventory()  # check for stock in bionic store
    bionic.check_inventory()  # check for stock in public store
    sony.check_inventory()  # check for stock in sony store
    mavros.check_inventory()  # check for stock in mavros store
    count()  # re Run every 50sec



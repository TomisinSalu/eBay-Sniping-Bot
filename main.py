from credentials import *
from products import *
from ebay_sniper import *
import datetime

#Enter max bid amount here
max_bid = "20"

Sniper_Instance = EbaySniper(
 name = Product_Instance.Get_Name(),
 username = flipndrip.username, 
 password = flipndrip.password, 
 product_url = Product_Instance.url, 
 max_bid = max_bid, 
 bid_datetime = "Enter bid endtime here" )

try:
    print(Sniper_Instance.name)
    Sniper_Instance.login()
    Sniper_Instance.bid()
except:
    print(datetime.now())

#Make it so that all user has to do is input product name and max bid create sniper instance
#Program computer to check if I won the bid
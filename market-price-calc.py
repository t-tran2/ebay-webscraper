from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

"""
Create ebay url to search for items based on name, condition, purchase method, and sold & completed items.
"""
""" 
https://www.ebay.com/sch/i.html?_from=R40&_nkw=macbook+pro&_sacat=0&LH_Auction=1&
LH_ItemCondition=3000&rt=nc&LH_Sold=1&LH_Complete=1
"""
product_name = input("What is the name of the item you are searching for? ")
name_url = f"_nkw={product_name.replace(" ", "+")}"

condition = input("What condition are you looking for(new, used, open box)? ")
# Condition used code
condition_code = 3000



purchase_method = input("Are you looking to \"Buy It Now\", \"Auction\" or either? ")



ebay_url = 
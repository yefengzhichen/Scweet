from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers
from Scweet.utils import init_driver, log_in
import pandas as pd
driver = init_driver(headless=True, show_images=False, proxy="http://172.26.64.1:7890")
log_in(driver, env=".env")


products = ['refrigerator', 'Split wall mounted type air conditioner', 'Rice Cooker (Pot)', 
            'Microwave Oven', 'Window type air conditioner', 'Pulsator Washing Machine', 
            'Front Loading Washing Machine', 'Induction Cooker', 'Electric', 
            'Dehumidifier', 'Air Purifier', 'Steam Furnace', 
            'Filter element', 'Multi split air conditioner-RAC', 'Vacuum Cleaner', 
            'Hot Water Bottle', 'Bulk package (product)', 'Electric Kettle', 
            'Iron', 'Electric Fan', 'Dishwasher', 
            'Toaster Oven', 'Filtered water dispenser', 'Air filter', 
            'Pressure Cooker', 'Feed Electric Appliance', 'Hanging Ironing Machine', 
            'Electric water heater', 'Split window type air conditioner', 'Grilled machine']


# 一个循环，遍历products 所有商品，调用scrape
for product in products[0:1]:
    data = scrape(hashtag="toshiba,"+product, since="2020-03-02", until="2024-03-02", from_account=None, interval=120,
                  headless=True, display_type="Top", save_images=False,
                  resume=False, filter_replies=False, proximity=False, driver=driver)
    out = data[['Tweet URL', 'Embedded_text', 'Comments', 'Timestamp', 'Likes', 'Retweets']]
    out.to_csv('out/'+product+'.csv', index=False)


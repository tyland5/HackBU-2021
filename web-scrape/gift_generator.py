import requests
from bs4 import BeautifulSoup
import random
import json 

picker = random.randint(1,201)
gifts = requests.get('https://www.gifts.com/valentines-day/nC0?prid=GFTNONE&navContent=T%3aValentine%27s+Day%3a&productgroup=glpvday&tile=catpg_hero1').text
gifts_html = BeautifulSoup(gifts, 'lxml')

items = gifts_html.find("div", class_= "UCStandardProductTemplate_r Product_{}".format(picker))

product_name = items.find("div", class_ = "productInformation applyDiscount")
product_price = items.find("span", class_= "discountedPosition")

image_section = items.find("div" ,class_="productImage") 
image = items.find("div", class_="productImage")
image_array= str(image.img).split("src=\"")
image_crop = image_array[1]
image_cutoff = image_crop.find("\"")


name_ = product_name.a.text
price_ = product_price.span.text
image_url = image_crop[0:image_cutoff]


product_dict =  {
        "name": name_,
        "price": price_,
        "image": image_url
    }

#json boolean start with lower rather than captial

with open('products.json','w') as f:
    json.dump(product_dict, f, indent = 1)

    
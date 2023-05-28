import requests
from bs4 import BeautifulSoup
import mysql.connector
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

all_products = []
for page in range(1,101):
    #Lấy nội dung HTML của trang web
    url = f'https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48/Page-{page}'
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    products = soup.find_all("div", class_="item-cell")
    for product in products:
         # get ItemID
        ItemID = product.find("a", class_="item-title")["href"].split('/')[-1].split('?')[0]
         # get Title
        title = product.find("a", class_="item-title").get_text().strip()
        # get Branding
        brand_element = product.find("a", class_="item-brand")
        if brand_element is not None:
            brand = brand_element["href"].split('/')[-3]
        else:
            brand = "N/A"
        # get rating
        rating_element = product.find("a", class_="item-rating")
        if rating_element is not None:
            rating = rating_element.get("title").split()[2]
        else:
            rating = "N/A"
        # get number of rating
        rating_count_element = product.find("span", class_="item-rating-num")
        if rating_count_element is not None:
            rating_count = rating_count_element.get_text().strip()[1:-1]
        else:
            rating_count = "N/A"
        # get Price
        price_element = product.find("li", class_="price-current").text.strip('$').strip(' ')
        if price_element is not None:
            price_parts = price_element.replace(",", "").replace("$", "").split()
            if len(price_parts) > 0:
                price = price_parts[0].strip()
            else:
                price = 0.0
        else:
            price = 0.0
        # get shipping
        def shipping_to_number(shipping):
            if "Free" in shipping:
                return 0
            elif "N/A" in shipping:
                return None
            else:
                 if shipping == "Special":
                    return 0.0
                 else:
                    return shipping.replace("$", "")
        shipping_element = product.find("li", class_="price-ship")
        if shipping_element is not None:
            shipping = shipping_element.get_text().strip().replace("$", "").replace(" Shipping", "")
            shipping_number = shipping_to_number(shipping)
        else:
            shipping = "N/A"
            shipping_number = 0
        # get image_url
        image_url = product.find("a", class_="item-img")["href"]
        #get total Price
        total_price = float(price) + float(shipping_number)
        #get detail product
        item_features = soup.find('ul', class_='item-features')
        features = soup.find_all('li')

        values = {
            'Max Resolution': '',
            'DisplayPort': '',
            'HDMI': '',
            'DirectX': '',
            'Model': ''
        }
        for feature in features:
            strong_tag = feature.find('strong')
            if strong_tag:
                if strong_tag.text == 'Max Resolution:':
                    values['Max Resolution'] = feature.text.replace('Max Resolution:', '').strip()
                elif strong_tag.text == 'DisplayPort:':
                    values['DisplayPort'] = feature.text.replace('DisplayPort:', '').strip()
                elif strong_tag.text == 'HDMI:':
                    values['HDMI'] = feature.text.replace('HDMI:', '').strip()
                elif strong_tag.text == 'DirectX:':
                    values['DirectX'] = feature.text.replace('DirectX:', '').strip()
                elif strong_tag.text == 'Model #: ':
                    values['Model'] = feature.text.replace('Model #: ', '').strip()
            #print(title)
            # Create a dictionary to store the product information
        product_dict = {
                "ItemID": ItemID,
                "Title": title,
                "Brand": brand,
                "Rating": rating,
                "Rating_Count": rating_count,
                "Price": price,
                "Shipping": shipping,
                "shipping_number": shipping_number,
                "total_price": total_price,
                "image_url": image_url,
                "Max_Resolution": values['Max Resolution'],
                "DisplayPort": values['DisplayPort'],
                "HDMI": values['HDMI'],
                "DirectX": values['DirectX'],
                "Model": values['Model']
            }

        # Append the product dictionary to the list of all products
        all_products.append(product_dict)

    # Print a message after each page is processed to track the progress
df = pd.DataFrame(all_products, columns=['ItemID','Title','Brand', 'Rating', 'Rating_Count','Price','Shipping','shipping_number','total_price',
                                      'image_url','Max_Resolution','DisplayPort','HDMI','Model','DirectX'
                                     ])
df.to_csv('data_products1.csv', index=False)
# After all pages have been processed, print the final list of products
# Print confirmation message
print('Data exported to final_data1.csv')

# Establish a connection to the MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Suong@200994",
  database="graphics_cards"
)
# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Create a table to store the product information
mycursor.execute("CREATE TABLE IF NOT EXISTS products (ItemID VARCHAR(255), Title VARCHAR(255), Brand VARCHAR(255), Rating VARCHAR(255), Rating_Count VARCHAR(255), Price FLOAT, Shipping VARCHAR(255), shipping_number FLOAT, total_price FLOAT, image_url VARCHAR(255), Max_Resolution VARCHAR(255), DisplayPort VARCHAR(255), HDMI VARCHAR(255), Model VARCHAR(255), DirectX VARCHAR(255))")

# Loop through all the products and insert them into the database
for product in all_products:
    # Convert the details dictionary to a JSON string
    details_json = json.dumps({
        "Max_Resolution": product["Max_Resolution"],
        "DisplayPort": product["DisplayPort"],
        "HDMI": product["HDMI"],
        "DirectX": product["DirectX"],
        "Model": product["Model"]
    })
    # Insert the product information into the database
    sql = "INSERT INTO products (ItemID, Title, Brand, Rating, Rating_Count, Price, Shipping, shipping_number, total_price, image_url, Max_Resolution, DisplayPort, HDMI, Model, DirectX) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (product["ItemID"], product["Title"], product["Brand"], product["Rating"], product["Rating_Count"], product["Price"], product["Shipping"], product["shipping_number"], product["total_price"], product["image_url"], product["Max_Resolution"], product["DisplayPort"], product["HDMI"], product["Model"], product["DirectX"])
    mycursor.execute(sql, val)
    mydb.commit()

# Close the database connection
mydb.close()

import matplotlib.pyplot as plt

# Product counts by brand
data = pd.read_csv('data_products1.csv')
plt.figure(figsize=(16, 8))
brand_counts = df["Brand"].value_counts()
plt.bar(brand_counts.index, brand_counts.values)
plt.xticks(rotation=90)
plt.xlabel('Brand', fontsize=16)
plt.ylabel('brand_counts', fontsize=16)
plt.title("Product counts by brand")
plt.show()

# Phân bố giá của các sảnphẩm
price_bins = pd.cut(df["total_price"], bins=[0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000])
price_counts = price_bins.value_counts().sort_index()
plt.bar(price_counts.index.astype(str), price_counts.values)
plt.xticks(rotation=90)
plt.title("Price distribution of products")
plt.show()

# Phân bố giá sản phẩm theo hãng
brand_price = df.groupby("Brand")["total_price"].mean().sort_values()
plt.bar(brand_price.index, brand_price.values)
plt.xticks(rotation=90)
plt.title("Price distribution by brand")
plt.show()

# Biểu diễn mối liên hệ giữa giá sản phẩm và rating của người dùng
plt.scatter(df["Rating"], df["total_price"])
plt.xlabel("Rating")
plt.ylabel("Price")
plt.title("Relationship between rating and price")
plt.show()
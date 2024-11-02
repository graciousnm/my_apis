from flask import jsonify, Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route("/ebay")

def scrape():
    items = []
    url = "https://www.ebay.ca/deals/trending/all" # the url of ebay trending products
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    start = soup.find_all("div", class_ = "col")
    for img in start: # getting required data
        title = img.find("h3")
        title = title.attrs["title"]
        amount = img.find("span", class_= "first").text
        price = amount[3:]
        price = price.strip('"').replace(",", "")

        results = {
                        "Product_name" : title,
                        "price" : float(price)

                }
        items.append(results)
    return jsonify(items)
# note that some of the names of the products names contains emojis which are in unicodes 
if __name__ == '__main__':
    app.run(debug=True)

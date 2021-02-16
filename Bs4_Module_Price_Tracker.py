from bs4 import BeautifulSoup
from urllib.request import urlopen as ureq
import urllib.request
import time
import requests
ASIN=input("Please Enter Asin of product : ")
link='https://www.amazon.in/dp/'+ASIN
user_input_price=int(input("Enter Your Desired Price : "))
req=urllib.request.Request(link,headers = {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" })
client=ureq(req)
soup=BeautifulSoup(client.read(),'html.parser')
def product_price():
    try:
        
        name = soup.find(id="productTitle").get_text().strip()
        print(name)
        price = soup.find(id="priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
        converted_price = float(price[0:6])
        print(converted_price)
        if converted_price<=user_input_price:
            send_message("\n" "\n"+"Good News!! Price Fell Down"+"\n" "\n"+name+"\n" "\n"+str(converted_price)+ "\n" "\n"+ link)
            print("Message Sent")
    except:
        print("*Price Unavaivable ")
        
def send_message(bot_message):

    bot_token = 'Your Bot Token'
    bot_chatID = 'Your Bot Chat Id'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

while True:
    product_price()
    time.sleep(5)

while True:
    product_price()
    time.sleep(3)
    



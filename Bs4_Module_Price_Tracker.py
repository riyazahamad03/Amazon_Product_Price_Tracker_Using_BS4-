from bs4 import BeautifulSoup
from urllib.request import urlopen as ureq
import urllib.request
import time
from datetime import datetime
import requests
ASIN=input("Please Enter Asin of product : ")
link='https://www.amazon.in/dp/'+ASIN
user_input_price=int(input("Enter Your Desired Price : "))
user_agent={"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" }

def product_price():
    try:
       
        req=urllib.request.Request(link,headers =user_agent)
        client=ureq(req)
        soup=BeautifulSoup(client.read(),'html.parser')
        
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        name = soup.find(id="productTitle").get_text().strip()
        print(name)
        price = soup.find(id="priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
        converted_price = float(price[0:6])
        print(converted_price)
        if converted_price<=user_input_price:
            send_message("\n" "\n"+"Good News!! Price Fell Down"+"\n" "\n"+name+"\n" "\n"+str(converted_price)+ "\n" "\n"+ str(link))
            print("Message Sent",current_time)
    except:
        print("*Price Unavaivable ")
        
def send_message(bot_message):

    bot_token = '1145135629:AAEOUYNdMrO7eujmgjlHdhvjK1E-2XYnIYY'
    bot_chatID = '620621191'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text='+bot_message
    response = requests.get(send_text)
    return response.json()

while True:
    product_price()
    time.sleep(3)
    



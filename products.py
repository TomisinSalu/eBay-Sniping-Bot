from cgitb import html
import datetime
import requests
from bs4 import BeautifulSoup

class Product:
    def __init__(self, url):
        self.url = url
        # self.time = datetime()
        

    def Get_Name(self):
        response =  requests.get(self.url)
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        name = soup.find("h1").text
        self.name = name

    def Get_Time(self):
        response =  requests.get(self.url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        time = soup.find(id_ = "vi-time-wrapperSection")
        self.time = time


url = "https://www.ebay.com/itm/144682667149?hash=item21afc24c8d%3Ag%3AQYAAAOSwG8ti-utI&amdata=enc%3AAQAHAAAAkGxtXGiDlVODUB25OizMKa8n4bOkyKrZ0WwGWmWYfOS2x5PktTkq%2BpcBa1MIG5fcZzvE6hndENnZvQe9Dj6DIT2ylBF%2Bxokph8%2BiuRCPP9YBE8VU6Wmdrk6Wp%2FlpL6kyeAXTqBlYxJDNF5QD5538Ra2gmZULpem%2F3Hbd4ij1eg9c%2BfaR2YQuual3%2FwAdfzV8Xg%3D%3D%7Ctkp%3ABk9SR5Trof3YYA&LH_Auction=1"
Product_Instance = Product(url)
Product_Instance.Get_Name()
Product_Instance.Get_Time()

print(Product_Instance.time, Product_Instance.name)
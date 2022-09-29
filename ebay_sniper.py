from lib2to3.pgen2 import driver
from ssl import Options
from selenium import webdriver
from time import sleep
import datetime
from credentials import *
from products import *
import chromedriver_autoinstaller as chromedriver
# ua = UserAgent()
# userAgent = ua.random
# option = options.add_argument(f'user-agent={userAgent}')
chromedriver.install()
driver = webdriver.Chrome()


class EbaySniper:
    ebay_url = "https://www.ebay.com"

    def __init__(self, name, username, password, product_url, max_bid, bid_datetime):
        self.name = name
        self.username = username
        self.password = password
        self.product_url = product_url
        self.max_bid = max_bid
        self.bid_datetime = bid_datetime
    
    def login(self):
        driver.get(self.ebay_url)
        sleep(2)
        io = driver.find_element_by_link_text("Sign in")
        io.click()
        loop = False
        sleep(2)

        loop = True
        while loop:
            try:
                userField = driver.find_element_by_id("userid")
                userField.clear()
                userField.send_keys(self.username)
                button = driver.find_element_by_id("signin-continue-btn")
                button.click()
                loop = False
            except:
                pass
        sleep(2)
        loop = True
        while loop:
            try:
                passField = driver.find_element_by_id("pass")
                passField.clear()
                passField.send_keys(self.password)
                button = driver.find_element_by_id("sgnBt")
                button.click()
                loop = False
            except:
                pass
        sleep(3)   

    def solve_captcha(self):
        button = driver.find_element_by_id("checkbox")
        button.click()
        #Change to text Captcha
        option = driver.find_element_by_tag_name("svg")
        option.click()
        option = driver.find_element_by_id("text_challenge")
        option.click()
        #Copy Catcha question
        #<div class="text-text" tabindex="0" style="opacity: 1; height: 100px; vertical-align: middle; display: table-cell; padding: 0px 10px 5px; word-break: break-word;">is a bull a president?</div>
        question1 = ""
        answer1 = input(question1 + ": ")
        #Input answer into text field
        answerField = driver.find_element_by_class_name("input-field")
        answerField.send_keys(answer1)
        next = driver.find_element_by_class_name("button-submit button")
        next.click()



    def wait(self):
        while datetime.datetime.now() < datetime.datetime(2022, 7, 14, 8, 17):
            sleep(1)
        
    def bid(self):
        loop = True
        while loop:
            try:
                driver.get(self.product_url)
                loop = False
            except:
                pass
        sleep(3)

        loop = True
        while loop:
            try:
                bidField = driver.find_element_by_id("MaxBidId")
                bidField.clear()
                bidField.send_keys(self.max_bid)
                button = driver.find_element_by_link_text("Place bid")
                button.click()
                loop = False
            except:
                pass
        self.wait()
        loop = True
        while loop:
            try:
                io = driver.find_element_by_id("confirm_button")
                io.click()
                loop = False
            except:
                pass
        input("Press any key to end")
        


#time = ""
# true_blue_time = datetime.datetime(2022, 7, 5, 1, 14,)
# true_blue_url = "https://www.ebay.com/itm/185485930686"

#trueBlue = EbaySniper( true_blue.name, ryan.username, ryan.password, true_blue.url, max_bid , time )

#trueBlue.login()
#trueBlue.wait()
#trueBlue.bid()
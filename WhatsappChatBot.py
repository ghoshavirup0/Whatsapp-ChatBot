from warnings import catch_warnings
from selenium import webdriver
chrome_browser=webdriver.Chrome(executable_path='/Users/ghosh/Desktop/chromedriver.exe')
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random

chrome_browser.get("https://web.whatsapp.com/")
chrome_browser.set_window_size(1400,1000)
chrome_browser.maximize_window()
print("Scan QR Code, And then Enter")
input()
time.sleep(5)
print("Logged In")
counter=1
#while True:
 
#Machine learning code is not made public right now. Improvements going on. Will upload shortly :)
botReply=[
"Hi!! I am a chat bot. Avirup is offline now.",
"Hello, I am just a robot, my maker is offline now",
"Hii I am a little computer program want to tell you that Avirup is offline now.",
"Hi! I am a robot , Avirup is offline now",
"Hola! I am a robot, My master is offline now. I will let him know that you texted him :)",
"Hello I am Avirup's chatbot. Have a nice day",
"I am a robot. I am still under development mode :) Avirup is offline now",
"Hi there, Hope you are having a nice day. I am a chatbot. Avirup is offline now. He will reply you later on :)"
]


#In this function get the last unread messages from whatsapp and PROCESS it to get suitable responses and send to the respective chats.
def send_message(text):
    
    message_box=chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
    #Just sending a random reply from the list 
    message_box.send_keys(random.choice(botReply))
    btn=chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
    btn.click()

def lastMessage(name):
    print(name)
    WebDriverWait(chrome_browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//span[@title="{}"]'.format(name)))).click()
    time.sleep(1.5)
    #Get the last messages here and add it in place of the STRING parameter below
    send_message("")
    

    

        
    
group = chrome_browser.find_elements_by_xpath('//*[@id="pane-side"]//div[@class="-GlrD _2xoTX"]//div[@class="_210SC"]')
time.sleep(2)

while True:
    
    List = [] 
    
    for item in group:

        att = item.find_element_by_xpath('.//span[@class="_3ko75 _5h6Y_ _3Whw5"]')
        name=att.get_attribute('title')
        try:
            state=item.find_element_by_xpath('.//span[@class="_31gEB"]').text
            flag=True
        except:
            flag=False
        time.sleep(0.3)
        if(flag):
            List.append(name)
        
        

    for i in List:
        lastMessage(i)

    time.sleep(1)


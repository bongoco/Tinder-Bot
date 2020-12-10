from selenium import webdriver
from time import sleep
import random
from getpass import getpass

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(5) 
        #login button
        btn_login = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
        btn_login.click()

        sleep(1)
        #facebook button
        btn_fb = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
        btn_fb.click()
        
        sleep(3)
        #store base/Tinder window[0]
        window_base = self.driver.window_handles[0] 
        #focus switched to Facebook popup window
        window_popup = self.driver.switch_to.window(bot.driver.window_handles[1])
        sleep(1)

        #input credentials
        print('FB Email:')
        username = input()
        password = getpass()

        #fill in email 
        in_email = self.driver.find_element_by_xpath('//*[@id="email"]')
        in_email.send_keys(username)
        #fill in password
        in_password = self.driver.find_element_by_xpath('//*[@id="pass"]')
        in_password.send_keys(password)
        password = ''

        sleep(2)
        #click login
        btn_login = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        btn_login.click()
        sleep(2)
        #previously logged in
        btn_ok = self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/div/table/tbody/tr/td[2]/button[2]')
        btn_ok.click()

        self.driver.switch_to.window(window_base)

        sleep(1)
        #location popup
        btn_allow = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        btn_allow.click()
        sleep(1)
        #notifications popup
        btn_enable = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        btn_enable.click()
        #privacy popup
        btn_accept = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
        btn_accept.click()
    
    def like(self):
        btn_like = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        btn_like.click()

    def dislike(self):
        btn_dislike = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        btn_dislike.click()

    def close_popular(self):
        btn_nopopular = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button[2]')
        btn_nopopular.click()
    
    def close_homescreen(self):
        btn_noadd = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]')
        btn_noadd.click()

    def autoswipe(self):
        for i in range(100):
            pause = random.randrange(1,50)/10 #randomly generated pauses
            sleep(pause)
            try:
                self.like()
            except Exception:
                try:
                    self.close_homescreen()
                except Exception:
                    try:
                        self.close_popular()
                    except Exception:
                        self.matched()

    def matched(self):
        pause = random.randrange(1,10)/10 #randomly generated pauses
        sleep(pause)
        in_greeting = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/div[3]/form/textarea')
        in_greeting.send_keys('Hi how you doing :)')
        sleep(0.5)
        btn_send = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/div[3]/form/button')
        btn_send.click()

bot = TinderBot()
bot.login()
bot.autoswipe()

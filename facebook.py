# alexander.terela@viacom.com
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from conspiracy import jokes

#set username and password
user = "autopost2019@gmail.com"
passw = "superhardpassword"

#get rid of notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#start browser
browser = webdriver.Chrome('/home/bynn/.local/bin/chromedriver', chrome_options=chrome_options)
browser.get('https://www.facebook.com/login')
browser.maximize_window();

#enter email and password and press return
browser.implicitly_wait(3)
username = browser.find_element_by_id('email')
username.send_keys(user)

password = browser.find_element_by_id('pass')
password.send_keys(passw)
password.send_keys(Keys.RETURN)


#go back to main facebook page (usually rerouted to welcome page)
browser.implicitly_wait(3)
browser.get('https://www.facebook.com')

#write joke

while True:
    joke = jokes()
    browser.implicitly_wait(20) #let load
    browser.find_element_by_tag_name('body').send_keys('p') #starts post
    actions = ActionChains(browser)
    actions.send_keys(joke)
    actions.pause(5)
    actions.key_down(Keys.CONTROL)
    actions.send_keys(Keys.RETURN)
    actions.key_up(Keys.CONTROL)
    actions.perform()
    browser.implicitly_wait(30) #let load

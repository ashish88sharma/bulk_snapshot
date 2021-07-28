from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

CREDS = {'email' : 'ashisheagle4@gmail.com','passwd':'qwerty123'}


def login():
    print('trying to login')
    global driver
    driver.get('https://chartink.com/login')
    WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))
    print(driver.current_url)
    emailField = driver.find_element_by_xpath('//*[@id="email"]')
    emailField.click()
    emailField.send_keys(CREDS['email'])
    time.sleep(4)
    passwd = driver.find_element_by_xpath('//*[@id="password"]')
    passwd.click()
    passwd.send_keys(CREDS['passwd'])
    time.sleep(4)

    driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/div/button/span').click()
    time.sleep(3)
    print('login done')

    URL = 'https://chartink.com/stocks/HINDCOPPER.html'
    print(URL)
    driver.get(URL)
    print(driver.current_url)
    movingAvg = driver.find_element_by_xpath('//*[@id="MFIm"]')
    movingAvg.click()
    time.sleep(2)

    mvWindow = driver.find_element_by_tag_name('Moving Avgs')
    mvWindow.click()

    mv = driver.find_element_by_xpath('//*[@id="a3m"]')
    mv.click()
    ##mvvalue = driver.find_element_by_xpath('//*[@id="newone3"]/table/tbody/tr[5]/td[5]/input').sendKeys('100')
    time.sleep(2)

    updateButton = driver.find_element_by_xpath('//*[@id="innerb"]')
    updateButton.click()
    time.sleep(4)

    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height'))
    driver.find_element_by_tag_name('body').screenshot('HIND.png')


def screenshot():
    global driver
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    login()

    driver.quit()


if __name__=="__main__":
    screenshot()

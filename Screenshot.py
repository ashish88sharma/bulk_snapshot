import pandas as pd
import numpy as np
import os
import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def create_dir():
    directory = str(pd.to_datetime('today').date())
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    return directory


def screenshot(dir_path):
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

    df = pd.read_excel(r'StockToTrack.xlsx')
    stockList = df['StockName'].tolist()

    for name in stockList:
        URL = 'https://chartink.com/stocks/'+str(name)+'.html'
        print(URL)
        driver.get(URL)
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(S('Width'),S('Height'))
        driver.find_element_by_tag_name('body').screenshot(str(dir_path)+'/'+str(name)+'.png')
        random_sleep = random.randint(7,20)
        print('Sleeping for '+str(random_sleep)+' Sec')
        time.sleep(random_sleep)
    driver.quit()

def main():
    dir_path = create_dir()
    screenshot(dir_path)

if __name__ == "__main__":
    main()

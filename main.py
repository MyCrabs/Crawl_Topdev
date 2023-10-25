from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get('https://topdev.vn/')
sleep(2)

dataform = open('data.txt')
line  = dataform.readlines()
search_button = driver.find_element(By.XPATH,'/html/body/section[1]/div/div[1]/div[1]/form/div/div/div/div/div[2]/button')
search_field = driver.find_element(By.XPATH,'/html/body/section[1]/div/div[1]/div[1]/form/div/div/div/div/div[1]/input')
search_contain = line[0]
search_field.send_keys(search_contain)
search_button.click()
sleep(1)
print('Finish searching')

def GetURL(): #Hàm dùng để lặp đi lăp lại nếu muốn search nhiều trang web
    page_source = BeautifulSoup(driver.page_source,'html.parser')
    profiles = page_source.find_all('a',class_ = 'text-lg font-bold transition-all text-primary')
    all_profile_URL = []
    for profile in profiles:
        profile_ID = profile.get('href')
        profile_URL = 'https://topdev.vn/' + profile_ID
        if profile_URL not in all_profile_URL:
            all_profile_URL.append(profile_URL)
    return all_profile_URL
#print(GetURL())

all_URL = GetURL()
driver.get(all_URL[0])
page_source1 = BeautifulSoup(driver.page_source,'html.parser')
info_div = page_source1.find('div',class_ = 'flex flex-wrap')
#print(info_div)


    










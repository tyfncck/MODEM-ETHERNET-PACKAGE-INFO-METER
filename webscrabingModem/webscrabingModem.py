import time

from bs4 import BeautifulSoup
from selenium import webdriver
#
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
#
exe1 = 'C:/selenium/chromedriver.exe'
exe2 = 'C:/selenium/geckodriver.exe'
#
driver = webdriver.Chrome(executable_path=exe1, options=options)
#
#
#
driver.get('http://192.168.1.1')
driver.find_element_by_id('txt_Username').send_keys('admin')
driver.find_element_by_id('txt_Password').send_keys('superonline.1')
driver.find_element_by_id('btnLogin').click()
time.sleep(1)
#
#
#
driver.get('http://192.168.1.1/html/content.asp')
driver.switch_to.frame(driver.find_element_by_id('listfrm'))
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="link_User_0_2"]').click())
time.sleep(3)
driver.switch_to.frame(driver.find_element_by_id('contentfrm'))

soup = BeautifulSoup(driver.page_source, 'html.parser')
soup.find_all('td', attrs={'id': 'Ethernet Paket Bilgisi'})
tables =soup.find('table', {'class': 'trTabContent'})

print(tables)
#driver.close()
#driver.quit()

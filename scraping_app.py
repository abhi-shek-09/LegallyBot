import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service = service)
# https://www.latestlaws.com/legal-faqs/district-courts-faq/
# https://www.latestlaws.com/legal-faqs/civil-liability-nuclear-damage-act2010-faqs/
# https://www.latestlaws.com/legal-faqs/fir-faq/ 
# https://www.latestlaws.com/legal-faqs/nri-bank-accounts-faq/
# https://www.latestlaws.com/legal-faqs/drug-addiction-faq/
# https://www.latestlaws.com/legal-faqs/consumer-laws-faqs/
# https://www.latestlaws.com/legal-faqs/credit-cards-faq/
# https://www.latestlaws.com/legal-faqs/bar-council-delhi-faq/
# https://www.latestlaws.com/legal-faqs/india-bar-examination-faqs/
driver.get(url='https://www.latestlaws.com/legal-faqs/nbfc-faq/')
diction = {
    'Header' : [],
    'Description': []
}
df = pd.DataFrame(diction)
div_element = driver.find_element(By.XPATH, "//div[@class='single-page content-area']") 
with open('dummy9.txt', 'w',  encoding='utf-8') as file:
    file.write(div_element.text)

time.sleep(10)
driver.quit()


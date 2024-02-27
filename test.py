from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

x = input ("Enter : ")

wait = WebDriverWait(driver, 10)

driver.get(x)


get_url = driver.current_url
wait.until(EC.url_to_be(x))
if get_url == x:
    page_source = driver.page_source


soup = BeautifulSoup(page_source,features="html.parser")
key=input("Enter something : ")
matches = soup.body.find_all(string=re.compile(key))

len_match = len(matches)

title = soup.title.text


file=codecs.open('key.txt', 'a+')

file.write(title+"\n")

file.write("\n")

count=1

for i in matches:
    file.write(str(count) + "." +  i  + "\n")
    count+=1

file.write("There were "+str(len_match)+" matches found for the keyword.")

file.close()

driver.quit()
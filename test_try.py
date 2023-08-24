

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os
import datetime



def get_course_info(title_list, url_list):
    
    courses = browser.find_element(By.ID, "list")
    courses_info = courses.find_elements(By.TAG_NAME, 'a')
    for course_info in courses_info:
        
        title_list.append(course_info.get_attribute('title'))
        url_list.append(course_info.get_attribute('href'))
        
    
USER = "test_user"
PASS = "test_pw"



browser = webdriver.Chrome(executable_path = "C:\\Users\\hyo\\Documents\\code\\webdriver\\chromedriver")
browser.implicitly_wait(3)


url_login = "https://kino-code.work/membership-login/"
browser.get(url_login)
time.sleep(3)
print("ログインページにアクセスしました")



element = browser.find_element(By.ID, 'swpm_user_name')
element.clear()
element.send_keys(USER)
element = browser.find_element(By.ID, 'swpm_password')
element.clear()
element.send_keys(PASS)
print("フォームを送信")


browser_from = browser.find_element(By.NAME, 'swpm-login')
time.sleep(3)
browser_from.click()
print("情報を入力してログインボタンを押しました")


url = "https://kino-code.work/member-only/"
time.sleep(3)
browser.get(url)
print(url,":アクセス完了")


searcher = browser.find_element(By.ID, 'search-2')
search_item = searcher.find_element(By.XPATH, 'form/input').send_keys('python')
time.sleep(1)

search = searcher.find_element(By.TAG_NAME, 'button').click()
time.sleep(3)

page_num = browser.find_elements(By.CLASS_NAME, "page-numbers")

page_links = []
for page in page_num:
    page_links.append(page.get_attribute("href"))

page_links.pop(0)

if page_links != None:
    page_links.pop()


courses_title = []
courses_url  = []

get_course_info(courses_title, courses_url)

for page in page_links:
    
    browser.get(page)
    get_course_info(courses_title, courses_url)
    time.sleep(3)

courses = {"title" : courses_title, "url" : courses_url}

df = pd.DataFrame(courses)

df.to_csv("course.csv", index=False, encoding="utf-8")
browser.quit()

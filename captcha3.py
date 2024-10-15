# 登陆程序 位于captcha3.py文件 第7行
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def login():
    """登陆程序"""
    # 打开Safari浏览器并进入网站
    driver = webdriver.Safari()
    driver.maximize_window()  # 最大化窗口
    driver.get('https://login2.scrape.center/')
    # 通过NAME定位出输入框元素的位置，并将账号密码输入至输入框中
    driver.find_element(By.NAME, 'username').send_keys('admin')
    driver.find_element(By.NAME, 'password').send_keys('admin')
    # 通过Xpath定位登录键，并点击登录
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[3]/div/input').click()
    # 此网站加载较慢，增加一些加载时间
    time.sleep(60)
    # 退出浏览器
    driver.quit()


login()

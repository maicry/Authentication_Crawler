# 登陆程序 位于captcha8.py文件 第9行
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import ddddocr


def login():
    """登陆程序"""
    # 打开Safari浏览器并进入网站
    driver = webdriver.Safari()
    driver.maximize_window()  # 最大化窗口
    driver.get('https://captcha8.scrape.center')
    # 通过Xpath定位用户名和密码的输入框，并将账号和密码输入
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[1]/div/div/input').send_keys(
        'admin')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[2]/div/div/input').send_keys(
        'admin')

    # 以防反爬虫验证码OCR识别不准确，在这里使用循环直到成功
    # 条件：直到当前网站成功登录才会终止循环
    while driver.current_url != 'https://captcha8.scrape.center/success':
        # 通过Xpath定位验证码图片，并点击登录
        driver.find_element(By.XPATH, '//*[@id="captcha"]').click()
        # 通过Xpath定位验证码图片，并将其暂时储存为png图片
        img = driver.find_element(By.XPATH, '//*[@id="captcha"]').screenshot_as_png
        # 将png图片传入ddddocr识别其中的验证码，将识别结果传入awe
        ocr = ddddocr.DdddOcr()
        awe = ocr.classification(img)
        # 如果第一次没有识别成功，则从第二次开始将之前的错误验证码delete掉
        driver.find_element(By.XPATH,
                            '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[3]/div/div/div[1]/div/input').send_keys(Keys.BACK_SPACE * 4)
        # 通过Xpath定位出输入框元素的位置，并将验证码输入至输入框中
        driver.find_element(By.XPATH,
                            '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[3]/div/div/div[1]/div/input').send_keys(awe)
        # 通过Xpath定位登录键，并点击登录
        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[4]/div/button').click()
        time.sleep(0.5)  # 给0.5秒种时间让网页加载

    time.sleep(10)
    driver.quit()


login()



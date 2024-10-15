
from io import BytesIO
import time
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
import base64
import json
import requests
from selenium.webdriver import ActionChains


# 图灵识别api
def tuling_api(username, password, img_path, ID):
    with open(img_path, 'rb') as f:
        b64_data = base64.b64encode(f.read())
    b64 = b64_data.decode()
    data = {"username": username, "password": password, "ID": ID, "b64": b64}
    data_json = json.dumps(data)
    result = json.loads(requests.post("http://www.tulingtech.xyz/tuling/predict", data=data_json).text)
    return result


# 登录函数
def login():
    # 打开Safari浏览器并进入网站
    url = 'https://captcha3.scrape.center/'
    driver = webdriver.Safari()
    driver.get(url)
    # 通过Xpath定位用户名和密码的输入框，并将账号和密码输入
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[1]/div/div/input').send_keys(
        'admin')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[2]/div/div/input').send_keys(
        'admin')
    time.sleep(3)
    # 通过Xpath定位登录键，并点击登录
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[3]/div/button/span').click()
    time.sleep(3)
    # 将窗口进行截图，储存为screenshot.png
    driver.save_screenshot('screenshot.png')
    # time.sleep(3)

    # 切割出验证码窗口
    with open('screenshot.png', 'rb') as f:
        con1 = f.read()
    img = Image.open(BytesIO(con1))
    img = img.crop((482, 142, 1123, 962))  # 切割出验证码窗口
    img.save('img.png')

    # 切割出已知汉字窗口
    with open('img.png', 'rb') as f1:
        con2 = f1.read()
    img_1 = Image.open(BytesIO(con2))
    img_1 = img_1.crop((307, 0, 600, 90))  # 切割出已知汉字窗口
    img_1.save('known_img.png')

    with open('img.png', 'rb') as f2:
        con3 = f2.read()
    img_2 = Image.open(BytesIO(con3))
    img_2 = img_2.crop((12, 96, 627, 714))  # 切割出选择窗口
    img_2.save('unknown_img.png')

    '''小图部分识别'''
    img_path = 'known_img.png'
    result_small = tuling_api(username="majunyi", password="majunyi",
                              img_path=img_path, ID="02156188")
    result_small = result_small['result']
    print(result_small)

    '''大图部分识别'''
    img_path = 'unknown_img.png'
    result_large = tuling_api(username="majunyi", password="majunyi",
                              img_path=img_path, ID="05156485")
    print(result_large)

    class_name = 'geetest_tip_content'
    element = driver.find_element(By.CLASS_NAME, class_name)

    try:
        for i in range(0, len(result_small)):
            result = result_large[result_small[i]]
            width = Image.open('unknown_img.png').size[0]
            stretch_rate = width / 1600
            ActionChains(driver).move_to_element(element).move_by_offset(-70 + int(result['X坐标值'] / stretch_rate),
                                                                         24 + int(result[
                                                                                      'Y坐标值']) / stretch_rate).click().perform()
            time.sleep(1)
    except:
        pass

    driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[6]/div/div/div[3]/a/div').click()

    '''自动登陆成功！'''

    time.sleep(20)
    driver.quit()


login()



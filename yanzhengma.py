#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time
from PIL import Image
import pytesseract
import baiduyun

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "7.0"
caps["deviceName"] = "redmi"
caps['appPackage'] = 'com.ytsc'
caps['appActivity'] = 'com.zztzt.android.simple.activity.tztRootLayoutActivity'

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

time.sleep(5)
driver.find_element_by_name("交易").click()

time.sleep(3)
driver.find_element_by_name("买入").click()

time.sleep(3)
driver.find_element_by_id("com.ytsc:id/tv_old_login").click()

time.sleep(3)
driver.find_element_by_id("com.ytsc:id/edit_PhoneNumber").send_keys(13800138000)

time.sleep(3)
driver.find_element_by_id("com.ytsc:id/image_yanzhengma").click()

time.sleep(3)
driver.find_element_by_id("com.ytsc:id/edit_yanzhengma_hangqing").send_keys(888888)

time.sleep(3)
driver.find_element_by_id("com.ytsc:id/iamge_login").click()

time.sleep(3)
#截图保存到本地
driver.get_screenshot_as_file('D:\Python36-32\project\yzm.png')
im = Image.open('D:\Python36-32\project\yzm.png')
#设置要裁剪的区域（验证码所在的区域）
box = (900,672,1080,801)
# 截图，生成只有验证码的图片
region = im.crop(box)
region.save('D:\Python36-32\project\yzm1.png')
time.sleep(5)
'''
image = Image.open('D:\Python36-32\project\yzm1.png')
# 开始识别验证码
optcode = pytesseract.image_to_string(image)
print(optcode)
'''
optcode = baiduyun.get_words('D:\Python36-32\project\yzm1.png')
print(optcode)

time.sleep(3)
driver.find_element_by_id("com.ytsc:id/edit_account").send_keys(1100010232)

time.sleep(3)
driver.find_element_by_id("com.ytsc:id/edit_password").send_keys(123321)

time.sleep(3)
driver.find_element_by_id("com.ytsc:id/edit_yanzhengma").send_keys(optcode)

time.sleep(3)
driver.find_element_by_id("com.ytsc:id/login").click()

'''
el1 = driver.find_element_by_xpath("//android.webkit.WebView[@content-desc=\"交易\"]/android.view.View/android.widget.ListView[1]/android.view.View[1]")
el1.click()

driver.quit()
'''
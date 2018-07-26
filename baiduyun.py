#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


""" 调用通用文字识别, 图片参数为本地图片 """
def get_words(filePath):
	image = get_file_content(filePath)
	result = client.basicGeneral(image)
	print(result)
	a = result['words_result'][0]['words']
	return a
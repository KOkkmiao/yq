#!/usr/bin/python
# -*- coding: <UTF-8> -*-
import threading
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import DEFAULT_EXECUTABLE_PATH, Service
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    service = Service(executable_path="./" + DEFAULT_EXECUTABLE_PATH)
    chrome = webdriver.Chrome(service=service)
    chrome.get("https://voice.baidu.com/act/newpneumonia/newpneumonia")
    time.sleep(2)

    # 所有国内的点击按钮
    # 点击展开全部
    chrome.find_element(By.XPATH, "//*[@id='nationTable']/div").click()
    time.sleep(1)
    threading.Thread(target=lambda: {

    }).start()
    elements = chrome.find_elements(By.XPATH, "//*[@id='nationTable']/table/tbody/tr")
    for element in elements:
        # 点击
        total_elements = element.find_elements(By.XPATH, "td")
        elements_ = total_elements[1:]
        all = total_elements[0].text
        for to in elements_:
            all += "\t" + to.text
        # 查看class 内容 是否能打开
        attribute = total_elements[0].find_element(By.XPATH, "div/span[1]").get_attribute("class")

        if attribute != 'VirusTable_1-73-1_2NQDw6 ':
            continue
        # 走到这里证明是可以点击的。
        chrome.execute_script("arguments[0].click();", total_elements[0])
        sub_elements = chrome.find_element(By.CLASS_NAME, "VirusTable_1-73-1_3U6wJT").find_elements(By.XPATH,
                                                                                                    "tbody/tr")
        all += "\n"
        for sub_element in sub_elements:

            for sub_td in sub_element.find_elements(By.XPATH, "td"):
                if sub_td.text == "待确认人员" or sub_td.text == "境外输入":
                    break
                all += "\t" + sub_td.text
            all += "\n"
        # 关闭这个城市
        chrome.execute_script("arguments[0].click();", total_elements[0])
        print(all)

    chrome.find_element(By.XPATH, "//*[@id='foreignTable']/div").click()
    time.sleep(1)
    count = 0
    i = 0
    foreign_elements = chrome.find_elements(By.XPATH, "//*[@id='foreignTable']/table/tbody/tr/td/table/tbody/tr")
    count = foreign_elements.__len__()
    while i < count:
        foreign_total_elements = foreign_elements[i].find_elements(By.XPATH, "td")
        number_elements = foreign_total_elements[1:]
        foreign_all = foreign_total_elements[0].text
        for number in number_elements:
            foreign_all += "\t" + number.text
        foreign_all += "\n"
        contain_a = None
        i += 1
        try:
            contain_a = foreign_total_elements[0].find_element(By.XPATH, "a")
        except BaseException:
            pass

        if contain_a is None:
            print(foreign_all)
            continue
        chrome.execute_script("arguments[0].click();", foreign_total_elements[0])
        # 跳转到另一个页面了。
        find_elements = chrome.find_elements(By.XPATH, "//*[@id='nationTable']/table/tbody/tr[2]/td/table/tbody/tr")
        if find_elements is None:
            foreign_all += "\n"
            continue
        for sub_element in find_elements:
            element_find_elements = sub_element.find_elements(By.XPATH, "td")
            for se in element_find_elements:
                foreign_all += "\t" + se.text
            foreign_all += "\n"
        # 要回到上一个页面去
        print(foreign_all)
        chrome.back()
        time.sleep(0.5)
        chrome.find_element(By.XPATH, "//*[@id='foreignTable']/div").click()
        time.sleep(0.1)
        foreign_elements = chrome.find_elements(By.XPATH, "//*[@id='foreignTable']/table/tbody/tr/td/table/tbody/tr")
        count = foreign_elements.__len__()
    chrome.close()

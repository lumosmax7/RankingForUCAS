from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import os
import time

## add chrome heere
# DriverPath=os.getcwd()
# browser= webdriver.Chrome(DriverPath+'/chromedriver')


## add  firefox here
DriverPath=os.getcwd()
browser = webdriver.Firefox()



class initial():
    def __init__(self):
        self.username = input("name:")
        self.password = input("password:")
        print('initial')

    def login(self):
        browser.get('http://sep.ucas.ac.cn/')
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div/section/div[2]/div/div[1]/div[1]/form/div[1]/"
                                      "div/div/div[1]/input").send_keys(self.username)
        browser.find_element_by_xpath("/html/body/div/section/div[2]/div/div[1]/div[1]/form/div[1]/"
                                      "div/div/div[2]/input").send_keys(self.password)
        try :
            browser.find_element_by_xpath("/html/body/div/section/div[2]/div/div[1]/div[1]/form/div[1]/div/div/div[3]/input")
            self.VerificationCode=input("enter the vertification code:")
            browser.find_element_by_xpath("/html/body/div/section/div[2]/div/div[1]/div[1]/form/div[1]/div/div/div[3]/input").send_keys(self.VerificationCode)
            browser.find_element_by_xpath("/html/body/div/section/div[2]/div/div[1]/div[1]/form/div[3]/div/div/button").click()
        except NoSuchElementException:
            browser.find_element_by_xpath("/html/body/div/section/div[2]/div/div[1]/div[1]/form/div[3]/div/div/button").click()
    def EnterIntoRanking(self):
        browser.find_element_by_xpath("/html/body/div[2]/ul/li[3]/a[3]/img").click()
        time.sleep(2)
        try:
            alert = browser.switch_to.alert
            alert.accept()
            browser.find_element_by_xpath("/html/body/div[2]/div/div/ul/li[4]/a/span[1]").click()
            time.sleep(0.5)
            browser.find_element_by_xpath("/html/body/div[2]/div/div/ul/li[4]/ul/li/a").click()
            time.sleep(0.5)
        except:
            browser.find_element_by_xpath("/html/body/div[2]/div/div/ul/li[4]/a/span[1]").click()
            time.sleep(0.5)
            browser.find_element_by_xpath('/html/body/div[2]/div/div/ul/li[4]/ul/li/a').click()
            time.sleep(0.5)

class RankingClass():
    def __init__(self):
        self.ClassesRows = len(browser.find_elements_by_xpath("/html/body/div[3]/div/div[3]/div[2]/table/tbody/tr"))

    def IsEvalued(self):
        for i in range(1,self.ClassesRows+1):
            try:
                buttom = browser.find_element_by_xpath(
                    "/html/body/div[3]/div/div[3]/div[2]/table/tbody/tr[" + str(i) + "]/td[8]/a")
                print(buttom.text)
                if (buttom.text == "modify the evaluation")or (buttom.text == "修改评估"):
                    self.PageScoll(20)
                    continue
                else:
                    buttom.click()
                    self.EnterintoRanking()
                    self.PageScoll(i*20)
            except:
                continue
        print("all classes have been evauled!")
        browser.execute_script("window.scrollBy(0,-10000000)")

    def EnterintoRanking(self):
        for i in range(2,28):
            try:
                browser.find_element_by_xpath(
                         "/html/body/div[3]/div/div[2]/div[2]/form/table/tbody/tr[" + str(i) + "]/td[1]/input").click()
                if i == 4:
                    browser.find_element_by_xpath(
                        "/html/body/div[3]/div/div[2]/div[2]/form/table/tbody/tr[" + str(i) + "]/td[4]/input").click()
                self.PageScoll(10)
            except NoSuchElementException:
                continue
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/form/div[2]/textarea").click()
        browser.switch_to.active_element.send_keys("老师的课堂互动很多, ppt内容翔实")
        self.PageScoll(30)
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/form/div[4]/textarea").click()
        browser.switch_to.active_element.send_keys("增加更多的实例, 包括图片和视频")
        self.PageScoll(30)
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/form/div[6]/textarea").click()
        browser.switch_to.active_element.send_keys("两个小时, 在下课之后, 温习功课")
        self.PageScoll(30)
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/form/div[8]/textarea").click()
        browser.switch_to.active_element.send_keys("比较有兴趣, 想了解更多相关的知识 ")
        self.PageScoll(30)
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/form/div[10]/textarea").click()
        browser.switch_to.active_element.send_keys("满出勤, 但是没有回答课堂上的问题")
        self.PageScoll(40)
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/form/div[12]/input").click()
        self.PageScoll(40)
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/form/div[19]/input").click()
        self.PageScoll(40)
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/form/div[21]/input").click()
        self.PageScoll(40)
        self.authcode = input("enter auth code:")
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/input").send_keys(self.authcode)
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/button").click()
        browser.find_element_by_xpath("/html/body/div[5]/div[4]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[2]/button[1]").click()




    def PageScoll(self,num):
        for i in range(num):
            js = 'window.scrollBy(0,5)'
            browser.execute_script(js)


class RankingTeacher():
    def __init__(self):
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/li[2]/a").click()
        self.TeachersRows=len(browser.find_elements_by_xpath("/html/body/div[3]/div/div[3]/div[2]/table/tbody/tr"))

    def IsEvalued(self):
        for i in range(1,self.TeachersRows+1):
            try:
                buttom=browser.find_element_by_xpath("/html/body/div[3]"
                                                     "/div/div[3]/div[2]/table/tbody/tr["+str(i)+"]/td[8]/a")
                if (buttom.text == "modify the evaluation")or (buttom.text == "修改评估") :
                    self.PageScoll(20)
                    continue
                else:
                    buttom.click()
                    self.EnterintoRanking()
                    self.PageScoll(i*20)
            except:
                continue
        print("all teachers have been evalued!")
    def EnterintoRanking(self):
        for i in range(2,28):
            try:
                browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]"
                                              "/form/table/tbody/tr["+str(i)+"]/td[1]/input").click()
                self.PageScoll(10)
            except NoSuchElementException:
                continue
        self.PageScoll(20)
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/form/div[2]/textarea").click()
        browser.switch_to.active_element.send_keys("授课的风格以及幽默的讲课，寓教于乐，启发学生")
        self.PageScoll(20)
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/form/div[4]/textarea").click()
        browser.switch_to.active_element.send_keys("希望老师能够保持这种授课方式，让学生能学到更多")
        self.authcode = input("enter auth code:")
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/input").send_keys(self.authcode)
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/button").click()
        browser.find_element_by_xpath("/html/body/div[5]/div[4]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[2]/button[1]").click()


    def PageScoll(self, num):
        for i in range(num):
            js = 'window.scrollBy(0,5)'
            browser.execute_script(js)

if __name__ == '__main__':
    person = initial()
    person.login()
    print("login success")
    time.sleep(3)
    person.EnterIntoRanking()
    time.sleep(1)
    rankingclass =RankingClass()
    rankingclass.IsEvalued()
    rankingteacher=RankingTeacher()
    rankingteacher.IsEvalued()

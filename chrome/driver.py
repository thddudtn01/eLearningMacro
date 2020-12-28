from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

class chrome:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    
    def visitAndLogin(self, url):
        self.driver.get(url)
        try:
            bannerBtn = self.driver.find_element_by_xpath(
                '//*[@id="lb_banner"]').click()
        except:
            pass
        loginBtn = self.driver.find_element_by_xpath(
            '//*[@id="header"]/div/div[1]/div[2]/ul/li[1]/a')
        self.driver.execute_script("arguments[0].click();", loginBtn)

    def switchToLoginWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def waitForLogin(self, waitForLoginTime):
        WebDriverWait(self.driver, waitForLoginTime).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'myClassBox'))
            )

    def switchToLoginWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def visitClassFirst(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        classBtn = self.driver.find_element_by_xpath(
            '//*[@id="cntnr1"]/div/div[2]/div[1]/ul/li[1]')
        self.driver.execute_script("arguments[0].click();", classBtn)
        self.driver.switch_to.window(self.driver.window_handles[1])

    #TODO
    def visitClassLater(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    #TODO
    def studyRoutine(self, i, j):
        continue

    def classRoutine(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        ol = soup.select_one('#lo_tag')
        liCnt = 2
        for li in ol.select('li.oneDepth'):
            liCnt += 1

            IntroBtn = self.driver.find_element_by_xpath(
                '//*[@id="lo_tag"]/li[' + str(liCnt) + ']/div/div[2]/a')
            self.driver.execute_script("arguments[0].click();", IntroBtn)

            for liCnt2 in range(len(li.select_one('ol').select('li'))):
                print("li : " + str(liCnt)+ " li : " + str(liCnt2))
                studyBtn = self.driver.find_element_by_xpath(
                    '//*[@id="lo_tag"]/li['+str(liCnt)+']/ol/li['+str(liCnt2+1)+']/div/div[2]/a')
                self.driver.execute_script("arguments[0].click();", studyBtn)
                time.sleep(3)

                studyRoutine()

        return soup
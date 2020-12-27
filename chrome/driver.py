waitForLoginTime = 30

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class driver:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        return self
    
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
        return self

    def waitForLogin(self):
        WebDriverWait(self.driver, waitForLoginTime).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'myClassBox'))
            )
        return self

    def switchToLoginWindow(self):
        driver.switch_to.window(driver.window_handles[1])
        return self

    def visitClass(self, classNum):
        classBtn = self.driver.find_element_by_xpath(
            '//*[@id="cntnr1"]/div/div[2]/div[1]/ul/li[' + str(classNum) + ']')
        self.driver.execute_script("arguments[0].click();", classBtn)
        return self
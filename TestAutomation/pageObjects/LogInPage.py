'''
Created on Jun 29, 2018

@author: aditya
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage(object):
    def __init__ (self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.timeout = 30 
 
 
class logINPage(BasePage):
   
    userName=(By.ID,"j_username")
    password=(By.ID,"j_password")
    cliclButtton=(By.ID,"submit")
    
    def setUserName(self,uName):
        userNameElement= self.driver.find_element(*logINPage.userName)
        userNameElement.send_keys(uName)
        
    def setPassword(self,passwd):
        passwordElement= self.driver.find_element(*logINPage.password)
        passwordElement.send_keys(passwd)
        
    def click_submit(self):
        submitBttn= self.driver.find_element(*logINPage.cliclButtton)
        submitBttn.click()
    
    def LogInMI(self,userName, password):
        self.setUserName(userName)
        self.setPassword(password)
        self.click_submit()
        
        
        
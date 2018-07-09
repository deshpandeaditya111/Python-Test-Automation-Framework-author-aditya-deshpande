'''
Created on Jul 2, 2018

@author: aditya
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageObjects.LogInPage import logINPage
from distutils.core import setup
class loginTests():
    
 def getName(self):
       global p
       p=3


l=loginTests()
l.getName()
print(p)
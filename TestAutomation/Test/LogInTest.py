'''
Created on Jun 29, 2018

@author: aditya
'''
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageObjects.LogInPage import logINPage
from distutils.core import setup
from Communication.ReadExcel import ExcelCom
import unittest

class SignIN_001(unittest.TestCase):
    
    def getName(self):
        return self.__class__.__name__
     
    def setUp(self):
        global driver
        self.driver = webdriver.Firefox()  
        self.driver.get('http://dt-aditya.technologic.com:9900/eQubeMI')
                             
    def tearDown(self):
        self.driver.close()
        print("tear down ended")

    def test_login(self):
       readExcel=ExcelCom()
       l=SignIN_001()
       readExcel.setFilePath("..//data/TestData.xlsx", "Sheet1")
       testCaseRow=readExcel.getRowContains(l.getName(),"Test Case Name")
       userName=readExcel.getCellData(testCaseRow, 1)
       password=readExcel.getCellData(testCaseRow, 2)
       lgnPage= logINPage(self.driver)
       lgnPage.LogInMI(userName,password)
       self.assertEqual("eQube MI Solution", self.driver.title)
       
suite = unittest.TestLoader().loadTestsFromTestCase(SignIN_001)
runner = HTMLTestRunner(output='E:\Aditya\SELENIUM_PY\TestAutomation\example_suite')
runner.run(suite)
#unittest.TextTestRunner(verbosity=2).run(suite)

       

#global l
#l=SignIN_001()
#l.setUp()
#l.test_login()
#l.tearDown()
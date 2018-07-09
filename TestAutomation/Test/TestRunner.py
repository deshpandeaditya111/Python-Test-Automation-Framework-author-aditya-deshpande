'''
Created on Jul 6, 2018

@author: aditya
'''
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from Test.LogInTest import SignIN_001

var=SignIN_001()
example_tests = TestLoader().loadTestsFromTestCase(var.test_login())
#example2_tests = TestLoader().loadTestsFromTestCase(Example2Test)
#suite = TestSuite([example_tests, example2_tests])
runner = HTMLTestRunner(output='example_suite')
runner.run(example_tests)
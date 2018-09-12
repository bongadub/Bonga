# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
####################################################################"""
import selenium.webdriver.support.expected_conditions as WAITCON
import random
import string
import time
import inspect

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from toolium.pageelements import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from toolium.pageelements import InputText, Button
from toolium.pageobjects.page_object import PageObject
####################################################################

from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from pageobjects.message import MessagePageObject
from pageobjects.secure_area import SecureAreaPageObject


class Buying_ItemPageObject(PageObject):
    def init_page_elements(self):
        self.username = InputText(By.NAME, 'email')
        self.password = InputText(By.NAME, 'passwd')
        self.login_button = Button(By.ID, 'SubmitLogin')

        self.message = MessagePageObject()
        


    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get('{}/login'.format(self.config.get('Test', 'url')))
        return self

    def wait_until_loaded(self):
        """ Wait until login page is loaded

        :returns: this page object instance
        """
        self.username.wait_until_visible()
        return self

    def login(self, user):
        """ Fill login form and submit it

        :param user: dict with username and password values
        :returns: secure area page object instance
        """
        #self.logger.debug("Login with user '%s'", user['username'])
        self.username.text = user['username']
        self.password.text = user['password']
        time.sleep(3)
        self.login_button.click()
        time.sleep(3)
       # return SecureAreaPageObject(self.driver_wrapper)

       #hover over the women tab
    def hover(self):
        self.element = self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')
        

        self.hover = ActionChains(self.driver).move_to_element(self.element).perform()
        time.sleep(3)
        
        return self

        #hover over women tab and move cursor to blouses and click
    def click_tops(self):
        self.click_element =  self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/ul/li[1]/ul/li[2]/a')

        self.hover = ActionChains(self.driver).move_to_element(self.click_element).click(self.click_element).perform()
        
       
        time.sleep(3)

        return self

    def addItem(self):
        #scroll to bottom
        self.driver.execute_script("window.scrollTo(0, -170, document.body.scrollHeight);")

        #Hover to blouse and click add to cart button
        self.item = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/h5/a')

        self.button = ActionChains(self.driver).move_to_element(self.item).perform()

        self.add_to_cart = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]').click()
        time.sleep(3)

        return self
        
        #click Proceed to checkout button to shopping-cart summary page
    def go_to_checkout(self):
        self.checkout = self.driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a').click()
        time.sleep(3)

        return self
        
        #click proceed button to addresses page
    def shopping_summary(self):
        self.summary = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/p[2]/a[1]').click()
        time.sleep(3)

        return self
        
        #click proceed button to shipping page
    def address_verification(self):
        self.address = Button(By.NAME, 'processAddress').click()
        time.sleep(3)

        return self

        #click the agree on terms checkbox buttton
    def agree_on_terms(self):
        self.agree_terms = self.driver.find_element(By.XPATH, '//*[@id="cgv"]').click()
        time.sleep(3)

        return self
        
        #click Proceed to checkout button to payment method page
    def shipping_page(self):
        self.shipping = Button(By.NAME, 'processCarrier').click()
        time.sleep(3)

        return self
        
        #Click payment method button
    def payment_method(self):
        self.payment_type = self.driver.find_element(By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a').click()
        time.sleep(3)

        return self

        #Click confirm order button
    def confirm_order(self):
        self.confirm_order = self.driver.find_element(By.XPATH, '//*[@id="cart_navigation"]/button').click()
        time.sleep(10)

        self.confirm_order = self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a').click()
        time.sleep(5)

        return self

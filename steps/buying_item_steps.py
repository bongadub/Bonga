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
"""

from behave import given, when, then

from pageobjects.buying_item import Buying_ItemPageObject 


@given('the log in page is open')
def step_impl(context):
    context.current_page = Buying_ItemPageObject()
    context.current_page.open()


@when('the user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    user = {'username': username, 'password': password}
    context.current_page = context.current_page.login(user)

@then('the user hovers over women section')
def step_impl(context):
    context.current_page = Buying_ItemPageObject()
    context.current_page.hover()

@given('the user clicks on Tops')
def step_impl(context):
	context.current_page = Buying_ItemPageObject()
	context.current_page.click_tops()

@when('the user add an item to a shopping cart')
def step_impl(context):
	context.current_page = Buying_ItemPageObject()
	context.current_page.addItem()

@then('the user clicks proceed to checkout')
def step_impl(context):
	context.current_page = Buying_ItemPageObject()
	context.current_page.go_to_checkout()

@given('the user goes to shopping summary page')
def step_impl(context):
	context.current_page = Buying_ItemPageObject()
	context.current_page.shopping_summary()

@when('the user goes to address verification page')
def step_impl(context):
    context.current_page = Buying_ItemPageObject()
    context.current_page.address_verification()	

@then('the user clicks agree on terms check button')
def step_impl(context):
	context.current_page = Buying_ItemPageObject()
	context.current_page.agree_on_terms()

@Given('the user goes to shipping page')
def step_impl(context):
	context.current_page = Buying_ItemPageObject()
	context.current_page.shipping_page()

@when('the user must choose payment method')
def step_imp(context):
	context.current_page = Buying_ItemPageObject()
	context.current_page.payment_method()

@then('the user must confirm order')
def step_impl(context):
	context.current_page = Buying_ItemPageObject()
	context.current_page.confirm_order()
from behave import given, when, then

from pageobjects.login import LoginPage


@given('the login page is open')
def step_impl(context):
    context.current_page = LoginPage()
    context.current_page.open()

@when('the user logs with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    user = {'username': username, 'password': password}
    context.current_page = context.current_page.login(user)


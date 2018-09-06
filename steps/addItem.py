@given('user hover over T-SHIRTS menu')
def step_impl(context):
    page = AutomationHomePage(context).HeaderPage(context)
    page.hover(page.menu_women)

@when('add a t-shirt to cart')
def function(context):
    page.DressesPage(context).summer_dresses.click()
    assert "SUMMER DRESSES" in SummerDressesCatalogPage(context).category_name.text
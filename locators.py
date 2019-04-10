from selenium.webdriver.common.by import By


class MainPageLocators(object):
    MyAccountButton = 'div#myAccount'
    LoginFromDropDown = '#login'
    SearchBar = '#productSearch'
    SearchButton = '#buttonProductSearch'


class LoginPageLocators(object):
    Header = '.box-header-title'
    Email = '#email'
    Password = '#password'
    SubmitButton = '.btn.full.btn-login-submit'


class SearchPageLocators(object):
    ProductTitle = '.product-title.title'


class ProductPageLocators(object):
    ProductName = '.product-name.best-price-trick'

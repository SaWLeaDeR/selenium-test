#!/usr/bin/python2.7
# coding=utf-8
from modules import *


class WebSiteAutomation(unittest.TestCase):
    def setUp(self):
        self.driver_path = os.path.dirname(os.path.realpath(__file__))
        self.driver = webdriver.Chrome(self.driver_path + '/chromedriver')
        self.driver.get('https://www.hepsiburada.com/')
        self.driver.maximize_window()

    def login(self):
        self.driver.find_element_by_css_selector(MainPageLocators.MyAccountButton).click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(MainPageLocators.LoginFromDropDown).click()

    def testIsOnMainPage(self, url='https://www.hepsiburada.com/'):
        self.assertEquals(self.driver.current_url, url)

    def testgoLoginPage(self):
        self.login()
        loginPageText = self.driver.find_element_by_css_selector(LoginPageLocators.Header).text
        self.assertEquals(loginPageText.encode('utf-8'), 'Üye Girişi')

    def testLogin(self):
        self.login()
        email = self.driver.find_element_by_css_selector(LoginPageLocators.Email)
        password = self.driver.find_element_by_css_selector(LoginPageLocators.Password)
        email.click()
        email.send_keys("mehmetfatihkoyuncuoglu@gmail.com")
        password.click()
        password.send_keys("hepsiburada")
        self.driver.find_element_by_css_selector(LoginPageLocators.SubmitButton).click()
        self.testIsOnMainPage('https://www.hepsiburada.com/ayagina-gelsin/giris?ReturnUrl=%2f')

    def testSearchForProduct(self, product='iphoneX'):
        self.testLogin()
        time.sleep(1)
        self.driver.find_element_by_css_selector(MainPageLocators.SearchBar).send_keys(product)
        self.driver.find_element_by_css_selector(MainPageLocators.SearchButton).click()
        self.driver.find_elements_by_css_selector(SearchPageLocators.ProductTitle)[3].click()
        productName = self.driver.find_element_by_css_selector(ProductPageLocators.ProductName).text
        self.assertEquals(productName, 'Apple iPhone 8 Plus 64 GB (Apple T\xfcrkiye Garantili)')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

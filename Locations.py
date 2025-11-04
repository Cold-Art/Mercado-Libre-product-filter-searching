import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains, Keys


class MercadoPage:
    mex_button = (By.ID, 'MX')
    search_bar = (By.CLASS_NAME, 'nav-search-input')
    search_bar_icon = (By.CLASS_NAME, 'nav-icon-search')
    product_status = (By.XPATH, '//*[@id="root-app"]/div/div[2]/aside/section[2]/div[5]/ul/li[1]/a/span[1]')
    location_zipcode = (By.XPATH, '/html/body/header/div/div[4]/div/a')
    field_zipcode = (By.XPATH, '//input[@name="zipcode"]')
    order_by = (By.XPATH, '//*[@id=":Rlilie:-display-values"]')
    order_by_expensive = (By.XPATH, '//*[@id=":Rlilie:-menu-list-option-price_desc"]/div/div/span')
    locate_every_post_name = (By.CLASS_NAME, 'poly-component__title-wrapper')
    locate_every_post_price = (By.CLASS_NAME, 'andes-money-amount andes-money-amount--cents-superscript')
    post_title = (By.CSS_SELECTOR,"h3.poly-component__title-wrapper a.poly-component__title")
    post_price = (By.CSS_SELECTOR, "span.andes-money-amount__fraction")


    def __init__(self):
        self.chrome_driver = webdriver.Chrome()
        self.chrome_driver.get(data.mercado_Site)
        self.wait = WebDriverWait(self.chrome_driver, 10)
        self.webActions = ActionChains(self.chrome_driver)


    def navigate(self):
        self.wait.until(EC.visibility_of_element_located(self.mex_button)).click()
        self.wait.until(EC.visibility_of_element_located(self.search_bar)).send_keys('playstation 5')
        self.wait.until(EC.visibility_of_element_located(self.search_bar_icon)).click()

    def filters(self):
        assert self.wait.until(EC.visibility_of_element_located(self.order_by))
        time.sleep(1)
        self.webActions.scroll_by_amount(0, 400).perform()
        self.wait.until(EC.element_to_be_clickable(self.product_status)).click()
        self.wait.until(EC.visibility_of_element_located(self.location_zipcode)).click()

    def zipcode(self):
        iframe = self.chrome_driver.find_element(By.CSS_SELECTOR, "iframe[src*='addresses-hub']")
        self.chrome_driver.switch_to.frame(iframe)  #starting the frame
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.field_zipcode)).send_keys('11510', Keys.ENTER)
        self.chrome_driver.switch_to.default_content() #ending the frame
        time.sleep(1)

    def order_posts(self):
        self.wait.until(EC.visibility_of_element_located(self.order_by)).click()
        self.wait.until(EC.visibility_of_element_located(self.order_by_expensive)).click()

    def research(self):
        ol = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ol.ui-search-layout.ui-search-layout--stack")))
        items = ol.find_elements(By.CSS_SELECTOR, "li.ui-search-layout__item")
        print('')
        print('')
        print('')
        for item in items[:5]:
            try:
                title = item.find_element(*self.post_title).text
                price = item.find_element(*self.post_price).text
                print(f"Producto: {title} - Precio: ${price}")
            except Exception as e:
                print(f"Error leyendo item: {e}")
        print('')
        print('')



'''var button = $x("//button[@class='btn-generic-right-sm']")[0];      #this command is to be used on the console of devtools, it verifies if the path works
    button.disabled'''

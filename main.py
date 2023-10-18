import data
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import requests
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.from_field = (By.ID, 'from')
        self.to_field = (By.ID, 'to')
        self.personal=(By.XPATH,data.personal)
        self.button_taxi = (By.CSS_SELECTOR,'.button.round')
        self.comfort=(By.XPATH,data.comfort)
        self.telephone = (By.CSS_SELECTOR, '.np-button')
        self.phone=(By.ID, 'phone')
        self.next = (By.CSS_SELECTOR,'.button.full')
        self.code = (By.ID, 'code')
        self.confirm = (By.XPATH, data.xpath_button_confirm)
        self.click_payment=(By.CSS_SELECTOR,'.pp-text')
        self.click_add_card=(By.CSS_SELECTOR,'.pp-row.disabled')
        self.number_card = (By.ID, 'number')
        self.code_card= (By.CSS_SELECTOR, '.card-code-input .card-input')
        self.click_link=(By.XPATH,data.xpath_link)
        self.close_window = (By.XPATH, data.xpath_close)
        self.comment=(By.ID,"comment")
        self.manta=(By.XPATH,data.xpath_manta)
        self.ice_cream=(By.XPATH,data.xpath_helado)
        self.button_order = (By.CSS_SELECTOR, '.smart-button-main, .smart-button-secondary')

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

#Seleccionando la opción "Personal"
    def click_personal(self):
        self.driver.find_element(*self.personal).click()

#Click en el botón para pedir taxi
    def click_button_taxi(self):
        self.driver.find_element(*self.button_taxi).click()

#Click en la opción de comfort
    def click_comfort(self):
        self.driver.find_element(*self.comfort).click()

#Click para abrir el cuadro donde se introduce el teléfono
    def click_telephone(self):
        self.driver.find_element(*self.telephone).click()

#Introduciendo el número de teléfono
    def set_phone(self, phone_number):
        self.driver.find_element(*self.phone).send_keys(phone_number)

#Click en siguiente
    def click_next(self):
        self.driver.find_element(*self.next).click()

#Escribir el código
    def set_confirmation_code(self, code):
        self.driver.find_element(*self.code).send_keys(code)

#Click en el botón para Confirmar el código
        def click_confirm_code(self):
            wait = WebDriverWait(self.driver, 10)
            confirm_button = wait.until(EC.element_to_be_clickable(self.confirm))
            confirm_button.click()

#Click para payment
    def click_button_payment(self):
        self.driver.find_element(*self.click_payment).click()

#Click para añadir tarjeta
    def click_to_add_card(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(EC.element_to_be_clickable(self.click_add_card))
            element.click()
        except StaleElementReferenceException:
            # Vuelve a intentar localizar el elemento y hacer clic en él
            element = wait.until(EC.element_to_be_clickable(self.click_add_card))
            element.click()

#Escribiendo número de tarjeta
    def set_card_number(self, card_number):
        self.driver.find_element(*self.number_card).send_keys(data.card_number)

#Escribiendo código de tarjeta
    def set_card_code(self, card_code):
        code_element = self.driver.find_element(*self.code_card)
        code_element.send_keys(card_code)
        code_element.send_keys(Keys.TAB)

#Click en link
    def click_on_link(self):
        self.driver.find_element(*self.click_link).click()

#Cerrar ventana
    def click_on_close(self):
        self.driver.find_element(*self.close_window).click()

#Agregando comentario
    def set_comment(self):
        self.driver.find_element(*self.comment).send_keys(data.message_for_driver)

#Click para manta y pañuelos
    def click_on_manta(self):
        self.driver.find_element(*self.manta).click()

#Añadiendo dos helados
    def adding_2_ice_cream(self):
        self.driver.find_element(*self.ice_cream).click()
        self.driver.find_element(*self.ice_cream).click()

#Botón final para ordenar
    def click_on_order_button(self):
        self.driver.find_element(*self.button_order).click()

class TestPageUrban:
    driver = None

    @classmethod
    def setup_class(cls):
        # Crea un controlador para Chrome
        cls.driver = webdriver.Chrome()
        # Abre la página urban routes
        cls.driver.get(data.urban_routes_url)
        cls.driver.implicitly_wait(10)
        # Crea un objeto de página
        cls.urban_page = UrbanRoutesPage(cls.driver)

    def test_valid_data(self):
        driver = self.driver
        actions = UrbanRoutesPage(driver)
        actions.set_from(data.address_from)
        actions.set_to(data.address_to)
        actions.click_personal()
        actions.click_button_taxi()
        actions.click_comfort()
        actions.click_telephone()
        actions.set_phone(data.phone_number)
        actions.click_next()

        # Agregar una espera para que se realice la solicitud HTTP
        sleep(3)

        #Enviar una solicitud GET para obtener el código de confirmación
        response = requests.get(data.urban_routes_url_code)
        if response.status_code == 200:
            response_data = response.json()
            confirmation_code = response_data.get('code')
            if confirmation_code:
                print(f"El código de confirmación es: {confirmation_code}")
            else:
                print("No se pudo obtener el código de confirmación.")
        else:
            print(f"Error al hacer la solicitud HTTP: {response.status_code}")

        actions.set_confirmation_code(confirmation_code)
        actions.click_confirm_code()
        actions.click_button_payment()
        actions.click_to_add_card()
        actions.set_card_number(data.card_number)
        actions.set_card_code(data.card_code)
        actions.click_on_link()
        actions.click_on_close()
        actions.set_comment()
        actions.click_on_manta()
        actions.adding_2_ice_cream()
        actions.click_on_order_button()

    @classmethod
    def teardown_class(cls):
        # Cerrar el navegador
        sleep(7)
        cls.driver.quit()


first_test = TestPageUrban()
first_test.setup_class()
first_test.test_valid_data()
first_test.teardown_class()
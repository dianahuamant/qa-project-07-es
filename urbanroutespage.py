import data
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from phone_code_util import retrieve_phone_code
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.from_field = (By.ID, data.locator_from)
        self.to_field = (By.ID, data.locator_to)
        self.personal=(By.XPATH,data.personal)
        self.button_taxi = (By.CSS_SELECTOR,data.css_button_taxi)
        self.comfort=(By.XPATH,data.comfort)
        self.telephone = (By.CSS_SELECTOR, data.css_telephone)
        self.phone=(By.ID, data.id_phone)
        self.next = (By.CSS_SELECTOR,data.css_next)
        self.code = (By.ID, data.id_code)
        self.button_confirm_code= (By.XPATH,data.xpath_button_confirm)
        self.click_payment=(By.CSS_SELECTOR,data.css_click_payment)
        self.click_add_card=(By.CSS_SELECTOR,data.css_click_add_card)
        self.number_card = (By.ID, data.id_number_card)
        self.code_card= (By.CSS_SELECTOR, data.css_code_card)
        self.click_link=(By.XPATH,data.xpath_link)
        self.close_window = (By.XPATH, data.xpath_close)
        self.comment=(By.ID,data.id_comment)
        self.manta=(By.XPATH,data.xpath_manta)
        self.selected_slider = (By.CSS_SELECTOR, data.css_selected_slider)
        self.ice_cream=(By.XPATH,data.xpath_helado)
        self.counter_ice_cream=(By.CSS_SELECTOR, data.css_counter_ice_cream)
        self.button_order = (By.CSS_SELECTOR, data.css_button_order)

#Ingresa el dato de from
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

# Ingresa el dato de to
    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

#Value de from
    def get_from(self):
            return self.driver.find_element(*self.from_field).get_property('value')

#Value de to
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

#Comfort es seleccionado
    def is_comfort_rate_selected(self):
            return self.driver.find_element(*self.comfort).get_attribute("class")

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
    def click_confirmation_code(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, data.xpath_button_confirm)))
        self.driver.find_element(*self.button_confirm_code).click()

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

#Value de comment
    def get_comment(self):
            return self.driver.find_element(*self.comment).get_property('value')

#Click para manta y pañuelos
    def click_on_manta(self):
        self.driver.find_element(*self.manta).click()

#Color de boton de manta y pañuelos
    def get_manta_panuelos(self):
            return self.driver.find_element(*self.selected_slider).value_of_css_property("background-color")

#Añadiendo dos helados
    def adding_2_ice_cream(self):
        self.driver.find_element(*self.ice_cream).click()
        self.driver.find_element(*self.ice_cream).click()

#Texto para saber cuántos helados está contando
    def get_ice_creams(self):
            return self.driver.find_element(*self.counter_ice_cream).text

#Botón final para ordenar
    def click_on_order_button(self):
        self.driver.find_element(*self.button_order).click()
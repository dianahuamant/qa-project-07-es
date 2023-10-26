import data
from urbanroutespage import UrbanRoutesPage
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


class TestPageUrban:
    driver = None

    @classmethod
    def setup_class(cls):
        # Crea un controlador para Chrome
        # cls.driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(options=chrome_options)
        # Abre la página urban routes
        cls.driver.get(data.urban_routes_url)
        cls.driver.implicitly_wait(10)
        # Crea un objeto de página
        cls.urban_page = UrbanRoutesPage(cls.driver)

    @classmethod
    #Comprobando si from y to se añadieron
    def test_configure_address(self):
        actions = UrbanRoutesPage(self.driver)
        actions.set_from(data.address_from)
        assert actions.get_from() == data.address_from, "El campo de from no contiene el valor esperado"
        actions.set_to(data.address_to)
        assert actions.get_to() == data.address_to, "El campo de to no contiene el valor esperado"

    # Comprobando si Comfort está seleccionado
    def test_select_comfort_rate(self):
        actions = UrbanRoutesPage(self.driver)
        actions.click_personal()
        actions.click_button_taxi()
        actions.click_comfort()
        assert actions.is_comfort_rate_selected()=="tcard active", "Comfort no está seleccionado"

    # Verificando que sí se obtuvo el código
    def test_retrieve_phone_code(self):
        actions = UrbanRoutesPage(self.driver)
        actions.click_telephone()
        actions.set_phone(data.phone_number)
        actions.click_next()
        sleep(2)
            # Obtener el código de confirmación usando la función retrieve_phone_code
        phone_confirmation_code = retrieve_phone_code(self.driver)
        assert phone_confirmation_code, "No se pudo obtener el código de confirmación del teléfono"
        actions.set_confirmation_code(phone_confirmation_code)
        actions.click_confirmation_code()

    # Validando que sí se ingresó el número telefónico
    def test_confirm_number_telephone(self):
        number_telephone = self.driver.find_element(By.CSS_SELECTOR, data.css_number_telephone).text
        assert number_telephone == data.phone_number, "El número telefónico no se ha agregó correctamente"

    #Agregando tarjeta de crédito
    def test_adding_credit_card(self):
        actions = UrbanRoutesPage(self.driver)
        actions.click_button_payment()
        actions.click_to_add_card()
        actions.set_card_number(data.card_number)
        actions.set_card_code(data.card_code)
        actions.click_on_link()
        actions.click_on_close()
        credit_card_text = self.driver.find_element(By.CSS_SELECTOR, data.css_credit_card_text).text
        assert credit_card_text == "Tarjeta", "La tarjeta de crédito no se ha agregado correctamente"

    #Validando que se escribió un mensaje para el controlador
    def test_write_comment(self):
        actions = UrbanRoutesPage(self.driver)
        actions.set_comment()
        comment = actions.get_comment()
        assert comment == data.message_for_driver, "No se envió el mensaje al driver"

    # Validando que se pidió una manta y pañuelos
    def test_confirm_blanket_scarves(self):
        actions = UrbanRoutesPage(self.driver)
        actions.click_on_manta()
        sleep(2)
        actions.get_manta_panuelos()
        background_color = actions.get_manta_panuelos()
        # Verificar si el color de fondo es igual a #007eff usando una aserción
        assert background_color == 'rgba(0, 126, 255, 1)', "No se pidió manta y pañuelos"

    #Validando que se seleccionaron dos helados
    def test_confirm_two_ice_cream(self):
        actions = UrbanRoutesPage(self.driver)
        actions.adding_2_ice_cream()
        number_ice_creams = actions.get_ice_creams()
        assert number_ice_creams == '2', "El valor de los helados no es igual a 2"

    #Validando que el botón azul aparezca para pedir taxi
    def test_confirm_modal(self):
        actions = UrbanRoutesPage(self.driver)
        actions.click_on_order_button()

        # Encuentra el elemento modal usando el selector previamente definido
        modal_element = self.driver.find_element(By.CSS_SELECTOR,data.css_modal_element)

        # Verifica si el elemento modal está presente
        assert modal_element.is_displayed(), "El modal no está presente en la página"

    @classmethod
    def teardown_class(cls):
        # Cerrar el navegador
        sleep(7)
        cls.driver.quit()


first_test = TestPageUrban()
first_test.setup_class()
first_test.test_configure_address()
first_test.test_select_comfort_rate()
first_test.test_retrieve_phone_code()
first_test.test_confirm_number_telephone()
first_test.test_adding_credit_card()
first_test.test_write_comment()
first_test.test_confirm_blanket_scarves()
first_test.test_confirm_two_ice_cream()
first_test.test_confirm_modal()
first_test.teardown_class()
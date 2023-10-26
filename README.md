# Pruebas de Automatización para Urban Routes

Este proyecto se centra en la automatización de pruebas para la aplicación web Urban Routes, que permite a los usuarios solicitar servicios de taxi. Las pruebas se realizan utilizando Selenium y Python para simular interacciones de usuario y verificar el funcionamiento de la aplicación.

## Tecnologías y Técnicas Utilizadas

- Selenium: Se utiliza para la automatización de navegadores web.
- Python: El lenguaje de programación principal para escribir las pruebas y la lógica de automatización.
- ChromeDriver: El controlador del navegador web utilizado para interactuar con Google Chrome.
- Page Object Model (POM): Se emplea una arquitectura POM para organizar los elementos de la página y las acciones del usuario.

## Pruebas Automatizadas

El proyecto incluye pruebas automatizadas que cubren las siguientes acciones:

1. **Configurar la Dirección**:
   - Se verifica la capacidad de configurar la dirección de origen y destino en la aplicación.

2. **Seleccionar la Tarifa Comfort**:
   - Se comprueba que los usuarios pueden seleccionar la tarifa "Comfort".

3. **Rellenar el Número de Teléfono**:
   - Se verifica que el número de teléfono se puede ingresar correctamente.

4. **Agregar una Tarjeta de Crédito**:
   - Se asegura que los usuarios pueden agregar una tarjeta de crédito para el pago.

5. **Escribir un Mensaje para el Controlador**:
   - Se comprueba que los usuarios pueden enviar un mensaje al conductor.

6. **Pedir una Manta y Pañuelos**:
   - Se verifica la capacidad de solicitar una manta y pañuelos.

7. **Pedir 2 Helados**:
   - Se asegura que los usuarios puedan pedir dos helados.

8. **Aparece el Modal para Buscar un Taxi**:
   - Se verifica que, al completar todas las acciones anteriores, aparece el modal para buscar un taxi.

## Ejecución de las Pruebas

Para ejecutar puedes descargarlo en zip de Github

## Estructura del Código

El proyecto consta de tres archivos principales:

- **data.py**:
  - Contiene los localizadores (locators) utilizados para identificar elementos en la interfaz de la aplicación. Puedes encontrar aquí los identificadores utilizados en las pruebas.

- **urbanroutespage.py**:
  - Contiene la definición de la clase `UrbanRoutesPage`, que representa la página de Urban Routes y contiene métodos para interactuar con elementos de la interfaz de usuario. Aquí se definen las acciones como configurar direcciones, agregar tarjetas de crédito, etc.

- **testpageurban.py**:
  - Define las pruebas de automatización utilizando la clase `UrbanRoutesPage` para interactuar con la aplicación y verificar que las acciones se realicen correctamente. Cada prueba se enfoca en una acción específica, como configurar direcciones, etc.

¡Diviértete probando Urban Routes automatizadamente!
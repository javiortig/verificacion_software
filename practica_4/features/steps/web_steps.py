from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

URL = 'https://www.gabilos.com/calculadoras/rentasconstantes/tiempo_para_devolver_prestamo.htm'


@given(u'que el usuario esta en la pagina WEB de calculo de prestamos')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get(URL)


@when(u'el usuario introduce una cuota de "{param1}"€')
def step_impl(context, param1):
    # Esperamos hasta que el elemento con el resultado esté visible para trabajar con el. Esta logica se aplica a partir de ahora.
    element = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'p4D6'))
    )
    
    element.send_keys(Keys.HOME, Keys.SHIFT + Keys.END)
    element.send_keys(param1)


@when(u'introduce un importe del prestamo de "{param1}"€')
def step_impl(context, param1):
    element = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'p4D7'))
    )
    
    element.send_keys(Keys.HOME, Keys.SHIFT + Keys.END)
    element.send_keys(param1) 


@when(u'selecciona un tipo de interes del "{param1}"%')
def step_impl(context, param1):
    element = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'p4D8'))
    )
    
    element.send_keys(Keys.HOME, Keys.SHIFT + Keys.END)
    element.send_keys(param1) 


@when(u'elige un periodo de pago "{param1}"')
def step_impl(context, param1):
    dropdown = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'p4E6'))
    )

    select = Select(dropdown)
    select.select_by_visible_text(param1)


@then(u'debe aparecer en pantalla un tiempo necesario para devolver el prestamo de "{param1}" años y "{param2}" meses')
def step_impl(context, param1, param2):
    years_element = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'p4D12'))
    )
    years_text = years_element.get_attribute('value')

    months_element = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'p4D13'))
    )
    months_text = months_element.get_attribute('value')

    # Verificamos los resultados
    assert years_text == param1, f"El resultado esperado para los años era 5,44 pero se obtuvo {years_text}"
    assert months_text == param2, f"El resultado esperado para los meses era 21,75 pero se obtuvo {months_text}"


@when(u'el usuario presiona el boton de limpiar el formulario')
def step_impl(context):
    button = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="button" and @value=" Limpiar formulario "]'))
    )

    button.click()


@then(u'todos los campos del formulario deben estar vacios')
def step_impl(context):
    cuota = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'p4D6'))
    )

    importe = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'p4D7'))
    )

    interes = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'p4D8'))
    )

    dropdown = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'p4E6'))
    )
    periodo = Select(dropdown)

    # Verificamos que los campos de texto estan vacios
    assert cuota.get_attribute('value') == '0,00', f"El campo de cuota debería valer '0,00', pero tiene el valor: {cuota.get_attribute('value')}"
    assert importe.get_attribute('value') == '0,00', f"El campo de cuota debería valer '0,00', pero tiene el valor: {importe.get_attribute('value')}"
    assert interes.get_attribute('value') == '0', f"El campo de cuota debería valer '0', pero tiene el valor: {interes.get_attribute('value')}"

    # Verificamos que el dropdown está establecido en su valor por defecto
    selected_option = periodo.first_selected_option
    assert selected_option.text == 'mensual', "El dropdown de período de pago debería estar en su valor por defecto."


    years_element = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'p4D12'))
    )
    years_text = years_element.get_attribute('value')

    # Verificamos los resultados
    assert years_text == "0", f"El resultado esperado para los años era '0' pero se obtuvo {years_text}"



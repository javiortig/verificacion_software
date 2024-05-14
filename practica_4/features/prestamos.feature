Feature: Calculo de amortizacion de prestamos
  Como un usuario del sistema de prestamos
  Quiero ingresar los detalles de mi prestamo
  Para calcular el tiempo necesario para su devolucion

  Scenario: Calcular tiempo de devolucion de un prestamo
    Given que el usuario esta en la pagina WEB de calculo de prestamos
    When el usuario introduce una cuota de "750"€
    And introduce un importe del prestamo de "15000"€
    And selecciona un tipo de interes del "3"%
    And elige un periodo de pago "trimestral"
    Then debe aparecer en pantalla un tiempo necesario para devolver el prestamo de "5,44" años y "21,75" meses
    When el usuario presiona el boton de limpiar el formulario
    Then todos los campos del formulario deben estar vacios

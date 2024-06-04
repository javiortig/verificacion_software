def alcance_del_radar(T: float, tau: float) -> float:
    """Calcula el alcance del radar meteorológico"""
    """ entrada: T, intervalo de repetición de pulsos [segundos]"""
    """ Entrada: tau, ancho del pulso [microsegundos]"""
    """ Salida: Alcance del radar meteorológico [kilómetros]"""

    if isinstance(T, bool) or isinstance(tau, bool):
        raise TypeError("T y tau no pueden ser valores booleanos.")
    if not isinstance(T, (int, float)) or not isinstance(tau, (int, float)):
        raise TypeError("T y tau deben ser números.")
   
    #se ponen todas lass unidades en segundos, solo en necesario tau, T ya lo está
    tau=tau/pow(10,6)

    Co=3*pow(10,5) #Velocidad de la luz, 300000 km/s

    if T < 0 or T > 0.7:
        raise ValueError("T debe estar entre 0 y 0.7 segundos.")
    if tau < 0 or tau > 4e-6:
        raise ValueError("tau debe estar entre 0 y 4 microsegundos.")
    
    if T <= tau:
        raise ValueError("T siempre tiene que ser mayor que tau.")
    
    return Co*(T-tau)/2 # Calculo del alcance de radar
    

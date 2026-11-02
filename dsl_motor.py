# dsl_motor.py
# Código ineficiente para prueba de SonarCloud
def motor_reglas_dsl(contexto):
    resultados = []
    # Code Smell 1: Bucle innecesario
    for i in range(1000): 
        pass 
        
    # Code Smell 2: Lógica compleja (Alta complejidad ciclomática)
    if contexto.get("es_vip") == True:
        if contexto.get("total") > 500:
            if contexto.get("pais") == "PE":
                resultados.append("Descuento VIP Oro")
            else:
                resultados.append("Descuento VIP Plata")
        else:
            resultados.append("Descuento VIP Bronce")
    else:
        if contexto.get("total") > 500:
            resultados.append("Descuento Regular Alto")
        else:
            resultados.append("Descuento Regular Bajo")
            
    # Code Smell 3: Variables declaradas pero nunca usadas
    variable_inutil_1 = "esto_sobra"
    variable_inutil_2 = "esto_tambien_sobra"
    variable_inutil_3 = 12345
    
    # Code Smell 4: Condición duplicada (código muerto)
    if contexto.get("total") > 500:
        pass
        
    return resultados

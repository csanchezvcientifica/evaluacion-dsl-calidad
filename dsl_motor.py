# dsl_motor.py 
# Este código es ineficiente a propósito para la prueba 

def motor_reglas_dsl(contexto):
    resultados = []
    # PROBLEMA 1: Bucle innecesario y variable no utilizada
    # SonarCloud lo marcará como "Code Smell" (ineficiencia)
    for i in range(1000): 
        pass 
        
    # PROBLEMA 2: Lógica compleja y repetitiva (Alta complejidad ciclomática)
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
            
    # PROBLEMA 3: Variable declarada pero nunca usada
    variable_inutil = "esto_sobra"
    
    return resultados

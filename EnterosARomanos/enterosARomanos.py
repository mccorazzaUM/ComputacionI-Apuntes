def entero_a_romano(numero):
    # Definimos la tabla de equivalencias en orden descendente
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    resultado = ""
    
    for valor_entero, simbolo in valores:
        # Mientras el número sea mayor o igual al valor actual
        while numero >= valor_entero:
            resultado += simbolo  # Agregamos el símbolo romano
            numero -= valor_entero  # Restamos el valor procesado
            
    return resultado
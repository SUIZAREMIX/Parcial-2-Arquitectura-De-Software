def parse_float(val):
    if val == '-' or val.strip() == '':
        return 0.0
    return float(val.replace(',', '.'))

archivo = open('DatasetAlimentos.csv', encoding='latin1')
lines = archivo.read().splitlines()
archivo.close()

resultado = ""

for linea in lines[1:]:
    if not linea.strip(): continue
    columnas = linea.split(';')
    alimento = columnas[0].strip()

    vitA = parse_float(columnas[6])
    tiamina = parse_float(columnas[7])
    ribo = parse_float(columnas[8])
    niacina = parse_float(columnas[9]) #profe, la niacina tambien es una vitamina, es la vitamina B3
    vitC = parse_float(columnas[10])
    
    suma = vitA + tiamina + ribo + niacina + vitC
    resultado += "Q4_SumaVit;" + alimento + "|" + str(suma) + "\n"


archivo_salida = open("resultado_mapper_q4.csv", "w", encoding='utf-8')
archivo_salida.write(resultado)
archivo_salida.close()

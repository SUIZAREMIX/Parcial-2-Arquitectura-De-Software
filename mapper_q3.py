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

    tiamina_mg = parse_float(columnas[7])
    # Tiamina está en miligramos, lo pasamos a gramos dividiendo por 1000
    tiamina_g = tiamina_mg / 1000.0
    if tiamina_g > 0.1:
        resultado += "Q3_TiaminaGt01g;1\n"


archivo_salida = open("resultado_mapper_q3.csv", "w", encoding='utf-8')
archivo_salida.write(resultado)
archivo_salida.close()

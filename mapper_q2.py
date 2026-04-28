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

    vitC = parse_float(columnas[10])
    resultado += "Q2_MaxVitC;" + alimento + "|" + str(vitC) + "\n"


archivo_salida = open("resultado_mapper_q2.csv", "w", encoding='utf-8')
archivo_salida.write(resultado)
archivo_salida.close()

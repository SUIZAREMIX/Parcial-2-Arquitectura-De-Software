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

    grasas = parse_float(columnas[3])
    resultado += "Q1_MaxGrasas;" + alimento + "|" + str(grasas) + "\n"


archivo_salida = open("resultado_mapper_q1.csv", "w", encoding='utf-8')
archivo_salida.write(resultado)
archivo_salida.close()

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

    hierro = parse_float(columnas[5])
    grasas = parse_float(columnas[3])
    if hierro > 1 and grasas < 3:
        resultado += "Q5_Filtro;" + alimento + "\n"


archivo_salida = open("resultado_mapper_q5.csv", "w", encoding='utf-8')
archivo_salida.write(resultado)
archivo_salida.close()

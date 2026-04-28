archivo_entrada = open('resultado_mapper_q1.csv', encoding='utf-8')
lines = archivo_entrada.read().splitlines()
archivo_entrada.close()

max_val = -1.0
max_alimento = ""

for linea in lines:
    if not linea.strip(): continue
    clave, valor_str = linea.split(';')
    alimento, val = valor_str.split('|')
    val = float(val)
    if val > max_val:
        max_val = val
        max_alimento = alimento

respuesta = "=== RESPUESTA PREGUNTA 1 ===\nAlimento: " + str(max_alimento) + " | Valor: " + str(max_val) + "\n"
print(respuesta)
archivo_salida = open('resultado_final_q1.txt', 'w', encoding='utf-8')
archivo_salida.write(respuesta)
archivo_salida.close()

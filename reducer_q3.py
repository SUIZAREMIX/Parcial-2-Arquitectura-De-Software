archivo_entrada = open('resultado_mapper_q3.csv', encoding='utf-8')
lines = archivo_entrada.read().splitlines()
archivo_entrada.close()

cuenta = 0
for linea in lines:
    if not linea.strip(): continue
    clave, valor = linea.split(';')
    cuenta += int(valor)

respuesta = "=== RESPUESTA PREGUNTA 3 ===\nCantidad de alimentos con más de 0.1 gramos de tiamina: " + str(cuenta) + "\n"
print(respuesta)
archivo_salida = open('resultado_final_q3.txt', 'w', encoding='utf-8')
archivo_salida.write(respuesta)
archivo_salida.close()

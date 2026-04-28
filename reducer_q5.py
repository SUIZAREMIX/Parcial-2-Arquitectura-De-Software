archivo_entrada = open('resultado_mapper_q5.csv', encoding='utf-8')
lines = archivo_entrada.read().splitlines()
archivo_entrada.close()

alimentos = []
for linea in lines:
    if not linea.strip(): continue
    clave, alimento = linea.split(';')
    alimentos.append(alimento)

respuesta = "=== RESPUESTA PREGUNTA 5 ===\nAlimentos: " + ", ".join(alimentos) + "\n"
print(respuesta)
archivo_salida = open('resultado_final_q5.txt', 'w', encoding='utf-8')
archivo_salida.write(respuesta)
archivo_salida.close()

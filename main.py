import time
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Una ligera desaprobación",
            "CREEPY": "Algo aterrador o siniestro",
            "AGGRO": "Ponerse agresivo o enojado",
            "SHIPEAR": "Concepto de una pareja ficticia. Unir a dos personas de manera ficticia",
            "CUTE": "Cuando algo es bonito, lindo, etc",
            "CRUSH": "Tipo de amor platonico", 
            "TWERK": "Poner las manos en la cadera, tener las rodillas flexionadas y hacer movimientos con la cadera hacia adentro y hacia afuera al ritmo de la musica"
            }
print("Hola y bienvenido a este pequeño diccionario de palabras modernas!")
time.sleep(1)
print("Ingresa una palabra que no entiendas y te daremos su definición")
time.sleep(1)

for i in range(5):
    print("-------------------------------------------")
    word = input("Escribe una palabra que no entiendas(Toda la palabra en mayusuclas!):").upper() #upper hace que no importe si lo escribo en minusculas
    if word in meme_dict.keys(): #If the word is in the keys of meme_dict
        print(word, ":", meme_dict[word])
        time.sleep(1)
    else:
        print("Esta palabra no esta en el diccionario")
        time.sleep(1)

print("Se acabaron los intentos. Quieres volver a empezar? Dale click a stop y luego run otra vez")
    
    

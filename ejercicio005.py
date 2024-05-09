# Desarrollado sobre S.O. Windows 11
import pandas as pd 
import requests

# Lectura del csv
df = pd.read_csv('data/frases.csv', header=None)

# Iteración del dataframe
for index, row in df.iterrows(): 
    frase = row[0]
    # Generación de la url (endpoint del servicio local)
    url = f"http://127.0.0.1:8008/prediccion/{frase}"
    responseWs = requests.get(url)
    response = responseWs.json()['prediction']
    # Imprime el resultado
    print(f"Evaluando la frase: {frase} --> {response}")
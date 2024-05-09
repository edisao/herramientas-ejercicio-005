# Ejercicio 005
Actividad en clase - no calificada

# Pre requisito
Levantar el servicio de Flask

![alt text](https://github.com/edisao/herramientas-ejercicio-005/blob/main/images/pre-requisito.png?raw=true)

```python
from flask import Flask, request, jsonify, render_template
from metodos import load_models, predict

app = Flask(__name__)

@app.route('/prediccion/<string:mensaje>', methods=['POST', 'GET'])
def prediccion(mensaje=None):
    """
    """
    # mensaje = request.args.get('mensaje')
    print(mensaje)

    vectoriser, LRmodel = load_models()
    valor = predict(vectoriser, LRmodel, mensaje)

    return jsonify({'prediction': valor[1]})


@app.route('/', methods=('GET', 'POST'))
def prediccion_formulario():
    valor_prediccion = None
    tipo_prediccion = -1
    if request.method == 'POST':
        mensaje = request.form['mensaje']
        print(mensaje)
        if len(mensaje) >0:
            vectoriser, LRmodel = load_models()
            tipo_prediccion, valor_prediccion = predict(vectoriser, LRmodel, mensaje)
        else:
            valor_prediccion = "Sin procesar"
    return render_template('index.html', valor_prediccion=valor_prediccion,
                           tipo_prediccion=tipo_prediccion)


if __name__ == '__main__':
    app.run(port=8008)
```

# Script
Detalle del script
```python
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
```
Resultado

![alt text](https://github.com/edisao/herramientas-ejercicio-005/blob/main/images/resultado.png?raw=true)

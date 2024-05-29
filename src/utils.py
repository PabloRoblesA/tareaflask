
from flask import Flask, render_template, request
from joblib import load
import pandas as pd

app = Flask(__name__)
model = load("tree_pokemon.sav")

class_dict = {
    "0": "Clase 0",
    "1": "Clase 1",
    "2": "Clase 2"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Obtener los valores de las características del formulario
        dexnum = float(request.form["dexnum"])
        generation = float(request.form["generation"])
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        catch_rate = float(request.form["catch_rate"])
        base_friendship = float(request.form["base_friendship"])
        base_exp = float(request.form["base_exp"])
        percent_male = float(request.form["percent_male"])
        percent_female = float(request.form["percent_female"])
        egg_cycles = float(request.form["egg_cycles"])
        
        # Adaptar los valores ingresados a tu conjunto de datos
        data = pd.DataFrame({
            'dexnum': [dexnum],
            'generation': [generation],
            'height': [height],
            'weight': [weight],
            'catch_rate': [catch_rate],
            'base_friendship': [base_friendship],
            'base_exp': [base_exp],
            'percent_male': [percent_male],
            'percent_female': [percent_female],
            'egg_cycles': [egg_cycles]
        })
        
        # Realizar la predicción con tu modelo
        prediction = str(model.predict(data)[0])
        
        # Obtener la clase correspondiente a la predicción
        pred_class = class_dict.get(prediction, "Clase Desconocida")
    else:
        pred_class = None
    
    return render_template("index.html", prediction=pred_class)

if __name__ == "__main__":
    app.run(debug=True)
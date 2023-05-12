from flask import Flask, request, render_template
from clases import alimentos

app = Flask(__name__,template_folder='html')

@app.route("/")
def alimentos():
    return render_template("start_alimentos.html")

@app.route("/alimentos", methods=['POST'])
def mostrar_alimentos():
 # Obtener la alimento seleccionada por el usuario
 alimento_ingresado=request.form["alimento"]
 # Insertar el código aquí
        
 # Renderizar la página de alimentos con el alimento seleccionado
 return render_template("alimentos.html", alimento=alimento_ingresado)


if __name__ == '__main__':
   app.run(debug=True)




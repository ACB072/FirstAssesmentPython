from flask import Flask, request, render_template
from clases.Pizza import Pizza
from clases.Sushi import Sushi
from clases.Hamburguesa import Hamburguesa


app = Flask(__name__,template_folder='html')

@app.route("/")
def alimentos():
    return render_template("start_alimentos.html")

@app.route("/alimentos", methods=['POST'])
def mostrar_alimentos():
    # Obtener la alimento seleccionada por el usuario
    nombre=request.form["alimento"]
    precio=request.form["precio"]
     # Insertar el código aquí
    if(nombre=="pizza"):
        ingredientes=request.form["ingredientes"]
        alimento_ingresado=Pizza(nombre,precio,ingredientes)
    elif(nombre=="sushi"):
        tipo_sushi=request.form["tipo_sushi"]
        alimento_ingresado=Sushi(nombre,precio,tipo_sushi)
    elif (nombre=="hamburguesa"):
        tipo_carne=request.form["tipo_carne"]
        alimento_ingresado=Sushi(nombre,precio,tipo_carne)

    # Renderizar la página de alimentos con el alimento seleccionado
    return render_template("alimentos.html", alimento=alimento_ingresado)


if __name__ == '__main__':
   app.run(debug=True)




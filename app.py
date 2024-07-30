from flask import Flask, render_template, request
from models.Ofertas import ofertas
from models.Producto import productos7


app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return render_template('inicio.html')

@app.route('/categorias/', methods=['GET'])
def categorias():
    search = request.args.get('search')
    if search:
        print("search parameter: " + search)
        productos = productos7.get_all_filter(search)
    else:
        productos = productos7.get_all()
    return render_template('categorias.html')

@app.route('/oferta', methods=['GET'])
def oferta():
    search = request.args.get('search')
    if search:
        print("search parameter: " + search)
        productos = ofertas.get_all_filter(search)
    else:
        productos = ofertas.get_all()
    return render_template("oferta.html", productos=productos, search=search)

@app.route('/conocenos', methods=['GET'])
def conocenos():
    return render_template('conocenos.html')

@app.route('/cuenta', methods=['GET'])
def cuenta():
    return render_template('cuenta.html')

@app.route('/registrese', methods=['GET'])
def registrese():
    return render_template('registrese.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

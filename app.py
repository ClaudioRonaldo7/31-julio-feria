from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio.html', methods=['GET'])
def inicio():
    return render_template('inicio.html')

@app.route('/categorias.html', methods=['GET'])
def categorias():
    return render_template('categorias.html')

@app.route('/oferta.html', methods=['GET'])
def oferta():
    return render_template('oferta.html')

@app.route('/conocenos.html', methods=['GET'])
def conocenos():
    return render_template('conocenos.html')

@app.route('/cuenta.html', methods=['GET'])
def cuenta():
    return render_template('cuenta.html')

@app.route('/registrese.html', methods=['GET'])
def registrese():
    return render_template('registrese.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

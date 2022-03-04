from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "<h1>¡Hola Mundo!</h1>"

@app.route('/dojo')
def dojo():
    return "<h1> ¡Dojo! </h1>"

@app.route('/say/<string:nombre>')
def hola_nombre(nombre):
    return " ¡Hola " + nombre +"!"

@app.route('/repeat/<int:num>/<string:palabra>')
def repite_palabra(num,palabra):
    output=''
    for i in range (0,num):
        output +='<p>'+palabra+'</p>'
    
    return output 

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__== "__main__":
    app.run(debug=True)

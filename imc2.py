from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/imc')
def form():
    return render_template('imc.html')
 
@app.route('/result', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return "The URL /result is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        return render_template('dati.html', dati_form = request.form)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html') #pagina PRINCIPAL

@app.route('/about')
def about():
    return render_template('about.html') #para segunda pagina que incluye el /


if __name__=='__main__':
    app.run()
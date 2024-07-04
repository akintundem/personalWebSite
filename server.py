from flask import Flask, render_template

app = Flask(__name__)

app.template_folder = "templates"
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('landing.html')

if __name__ == '__main__':
        app.run(host='localhost', port=3000, debug=True) 

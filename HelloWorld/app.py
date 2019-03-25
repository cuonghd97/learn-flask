from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return 'Hello: {}'.format(name)
@app.route('/cuong')
def cuong():
    return 'cuong'
@app.route('/hello-html/<name>')
def render_tp(name):
    return render_template('hello.html', name=name)

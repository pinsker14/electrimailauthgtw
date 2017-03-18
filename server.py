from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/<name>')
def helloName(name):
	return 'Hello ' + name
	
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8080)
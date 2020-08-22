from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.static_folder = 'static' 

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		return "Hello"
	elif request.method == 'GET': 
		return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True)
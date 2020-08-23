import os
from flask import Flask, render_template, url_for, request, redirect, flash
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.static_folder = 'static' 
app.secret_key = "secret key"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		return "Hello"
	elif request.method == 'GET': 
		return render_template('index.html')

@app.route("/predict", methods=["GET", "POST"])
def predict():
	# if request.method == "POST":

	# 	if request.files:

	# 		image = request.files["image"]

	# 		print(image)d

	# 		return redirect(request.url)

	# return render_template("predict.html")
	if request.files:
	
		image = request.files["image"]
	
		if image.filename == '':
			flash('No image selected for uploading')
			return redirect(request.url)
		
		if image and allowed_file(image.filename):
			filename = secure_filename(image.filename)
			image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			
			flash('Image successfully uploaded and displayed')
			return render_template('index.html', filename=filename)
		else:
			flash('Allowed image types are -> png, jpg, jpeg, gif')
			return redirect(request.url)


if __name__ == '__main__':
	app.run(debug = True)

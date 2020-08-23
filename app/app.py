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

@app.route("/upload", methods=["POST"])
def upload():

	file = request.files['file']
	
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)

	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		flash('Image successfully uploaded and displayed')
		return render_template('upload.html', filename=filename)

	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.errorhandler(404)
def page_not_found(e):
	# note that we set the 404 status explicitly
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug = True)

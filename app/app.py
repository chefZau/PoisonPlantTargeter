import os
from flask import Flask, render_template, url_for, request, redirect, flash
from werkzeug.utils import secure_filename
import torch
import torch.nn as nn
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import pickle
import pandas as pd
import numpy as np
from PIL import Image
from torch.autograd import Function, Variable

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.static_folder = 'static' 
app.secret_key = "secret key"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

model = pickle.load(open('model.pkl', 'rb'))
transform = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.ToTensor()
    ])

train_set = datasets.ImageFolder("../model_training/data_mining/image", transform = transform)
classes = train_set.classes

df = pd.read_csv("./static/mushroom_details.csv")

def image_loader(image_name):
    """load image, returns cuda tensor"""
    image = Image.open(image_name)
    image = transform(image)
    image = Variable(image, requires_grad=True)
    image = image.unsqueeze(0)  #this is for VGG, may not be needed for ResNet
    return image  #assumes that you're using GPU

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

		image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		file.save(image_path)
		
		flash('Image successfully uploaded and displayed')

		image = image_loader(image_path)
		predict = model(image)

		_, index = torch.max(predict, 1)
		percentage = torch.nn.functional.softmax(predict, dim=1)[0] * 100

		flash('The model predicts the image to be of a/an {} with a {} confidence.'.format(classes[index[0]], percentage[index[0]].item()))

		return render_template('upload.html', filename=filename)

	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug = True)

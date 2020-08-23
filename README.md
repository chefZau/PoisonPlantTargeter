# PoisonPlantTargeter

## Get Start!
Our model is huge. since giuthub has large file policy, we are unable to push a 500MB file to the server. However, we provide you with this [link](https://drive.google.com/file/d/1Liw_SsOnRxmRoRCWiwjjihPwjuJBspbW/view?usp=sharing). Place it in the app/ folder then you are good to go!

## Inspiration
People are craving for outdoor activities. With cinemas and bars remain on the more dangerous side of the spectrum, national and provincial parks become a top choice for people who are eager to go out. 

Canada has made an active effort in attracting young adults and young families to visit national and provincial parks. As younger people remain the lower-risk group regarding COVID-19, they tend to be more active when going outside. 

With limited botanical expertise, young adults and families with young children tend to be less careful yet curious when encountering plants or fungi in nature. Contacts, if unlucky, with poisonous plants and fungi can pose a serious effect on one's health and requires immediate care. Therefore, we want to build a platform for young users to be more cautious in dealing with plants and fungi in the wild. 

## What it does
MushMush is a mobile app that classifies the species of fungi the user uploads and gives information on the edibility of the mushroom. The app is based on a VGG image classification algorithm in Python.

Moreover, we would like to develop this app into an online community for young nature-lovers. As more young people are venturing into nature, this online community allow users to share their experience and knowledge in plants to help others identify potential danger. 

## How we built it
We are building a complete machine learning web application for predicting the image that our users upload to our server.

We use the Python language for this project. Data is being scraped from a website that provides reliable fungi information. We are using Bootstrap as our front-end tool and flask framework as our back-end tool for our application. 
 
After simply data wrangling, data been applied to a machine learning classifier based on a convolutional neural network, which is considered as a gold standard for image classification. We basically used a pre-trained CNN model called VGG16, which is trained on the ImageNet dataset, and it is suitable for our project.
 
We then modified the number of classes to match the number of different species of mushroom in our dataset and trained on our dataset again. With the model, we are then able to predict on the test image, whenever there’s an image uploaded by a user, we can use our model to classify(more specifically, predict) what species this mushroom might be and give a percentage of how confident is our model about this prediction.
 
The model weight is then saved to a file and can then be easily accessed by simply building the same model structure and can be loaded in easily for our web application


## Challenges we ran into
The unavailability of bulk images in our plant or fungi dataset poses a major challenge to our model. After scrapping the information from http://www.mushroom.world/, we only have five or fewer images per species of fungi which resulted in low accuracy in the testing set. To mitigate this problem, we utilized xxx to scrape more images from Google images/augmentation to increase the number of images in our training and testing sets. Eventually, we obtained xx% accuracy in our testing set. 

## Accomplishments that we're proud of
We have collaborated to work with web application techniques and neural network methods to deploy a complete Machine learning application that can be accessed and used by other people.

## What we learned
Deploy the neural network model using Flask as an API, and use the PyTorch library, which is more convenient to run our code on GPU, and also will not cause trouble like the TensorFlow/Keras version issues.

## What's next for MushMush
We plan to expand our dataset into plants

## Authors

* **Luca(MingCong) Zhou** - *Initial work* - [chefZau](https://github.com/chefZau)
* **Jason** - *Initial work* - [wjhlang](https://github.com/wjhlang)
* **Claudia Lou** - *Initial work* - [ClaudiaLOU](https://github.com/ClaudiaLOU)
* **Zoe(RuiYing) Zhang** - *Initial work* - [rzhan97](https://github.com/rzhan97)

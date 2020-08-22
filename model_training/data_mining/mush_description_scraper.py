import pandas as pd
import numpy as np
import requests
import random
import os
from PIL import Image
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

labels = ['plant_name', 'link']

df = pd.read_csv("mushroom.csv", names=labels)

session = requests.session()
family, location, dimensions, edibility, description = [], [], [], [], []

for index, row in df.iterrows():
	
	print(row['plant_name'], row['link'])
	
	response = session.get(row['link'])
	parsed_html = BeautifulSoup(response.text, 'html.parser')

	# there are four textus in each page, and one description
	textus = parsed_html.find_all("div", {"class":"textus"})
	longtextus = parsed_html.find("div", {"class":"longtextus"})

	family.append(textus[0].getText())
	location.append(textus[1].getText())
	dimensions.append(textus[2].getText())
	edibility.append(textus[3].getText())
	description.append(longtextus.getText())

df['family'] = family
df['location'] = location
df['dimensions'] = dimensions
df['edibility'] = edibility
df['description'] = description

df.to_csv('mushroom_details.csv', index=False)


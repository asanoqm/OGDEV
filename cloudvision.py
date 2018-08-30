import io
import os

from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

file_name = os.path.join(
    os.path.dirname(__file__),
    'leader.jpg')

with io.open(file_name, 'rb') as image_file:
texts = response.text_annotations
    content = image_file.read()

image = types.Image(content=content)

response = client.text_detection(image=image,max_results=5)

print('Texts:')

for text in texts:
    message = '\n"{}"'.format(text.description)
    print(message)
    break


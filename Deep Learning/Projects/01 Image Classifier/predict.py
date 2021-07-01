
import tensorflow as tf
import tensorflow_hub as hub

import warnings
warnings.filterwarnings('ignore')

import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

import numpy as np
import json
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('path', action='store', type=str, help='image path')
parser.add_argument('model', action='store', type=str, help='pretrained model')
parser.add_argument('--top_k', action='store', type=int, default=1, help='top K most likely classes')
parser.add_argument('--category_names', action='store', type=str, default='label_map.json', help='Path to a JSON file mapping labels to flower names')
args=parser.parse_args()

image_size = 224

def process_image(img):
    image = np.squeeze(img)
    image = tf.image.resize(image, (image_size, image_size))
    image /= 255
    return image.numpy()

def predict(image_path, model, top_k):
    image = Image.open(image_path)
    image_array = np.asarray(image)
    image_processed = process_image(image_array)
    prediction = model.predict(np.expand_dims(image_processed, axis=0))
    values, indices = tf.math.top_k(prediction, top_k)
    return values.numpy()[0], indices.numpy()[0]

with open(args.category_names, 'r') as f:
    class_names = json.load(f)
    
model = tf.keras.models.load_model(str('./'+args.model), custom_objects={'KerasLayer': hub.KerasLayer})

probs, labels = predict(args.path, model, args.top_k)

classes = [class_names[str(label+1)] for label in labels]

print('\nImage:', args.path)
for i in range(args.top_k):
    print('{} likely prediction:'.format(i+1))
    print('\t\u2022 Class:', classes[i])
    print('\t\u2022 Label:', labels[i])
    print('\t\u2022 Probs: {:.3%}'.format(probs[i]))

import cv2
import tensorflow as tf
import numpy as np

img=cv2.imread("0.png",cv2.IMREAD_GRAYSCALE)
img=cv2.resize(img,(28,28),cv2.INTER_AREA)
img=[img]
img = tf.keras.utils.normalize(img, axis=1)
print(img.shape)

model = tf.keras.models.load_model('epic_num_reader.model')

prob=model.predict(img)
print(prob)

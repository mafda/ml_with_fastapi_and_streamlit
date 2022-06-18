import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img

img_width, img_height = 28, 28

# ======= PREDICT MODEL =======

test_model = load_model("./my_model/mnist.h5")
img = load_img("./assets/3.png", False, target_size=(img_width, img_height))

# Scale down image to the model input size
img = cv2.resize(np.uint8(img), (img_width, img_height))
# Rescaled image upwards to show
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rescaled = cv2.resize(
    img, (img_width, img_height), interpolation=cv2.INTER_NEAREST
)

x = img_to_array(img)
x = np.expand_dims(x, axis=0)
preds = test_model.predict_step(x)

print(preds)

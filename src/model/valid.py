"""Project: Prototyping a Machine Learning Application with Streamlit

Validation mnist dataset
"""

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array


def predict_model(model, image):
    """Predict model function

    Parameters
    ----------
    model : str
        path to load model
    img : numpy.ndarray
        image to predict

    Returns
    -------
    predict_class : EagerTensor
        probabilities

    """

    model = load_model(model)
    img = img_to_array(image)
    img = np.expand_dims(img, axis=0)
    predict_class = model.predict_step(img)

    return predict_class

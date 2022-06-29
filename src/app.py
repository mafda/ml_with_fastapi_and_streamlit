"""Project: Prototyping a Machine Learning Application with Streamlit

Streamlit app integrated with predict_model.
"""

import cv2
import numpy as np
import streamlit as st
from streamlit_drawable_canvas import st_canvas

from model.valid import predict_model

CANVAS_SIZE = 250
IMG_WIDTH = 28
IMG_HEIGHT = 28
MODEL = "./my_model/mnist.h5"


def main():
    """Main Streamlit function
    Read an image and show a probability
    """

    st.set_page_config(page_title="mnist Prediction", page_icon=":1234:")

    st.header("Prototyping a ML Application")
    st.title("mnist Prediction")
    st.write("Draw something here")

    # Create a canvas component
    canvas_image = st_canvas(
        fill_color="black",
        stroke_width=20,
        stroke_color="gray",
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode="freedraw",
        key="canvas",
        display_toolbar=True,
    )

    if canvas_image.image_data is not None:
        # Scale down image to the model input size
        img = cv2.resize(
            np.uint8(canvas_image.image_data), (IMG_WIDTH, IMG_HEIGHT)
        )
        # Rescaled image upwards to show
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        if st.button("Predict"):
            predict_class = predict_model(MODEL, img)

            predict_class = predict_class.numpy()

            probability = np.amax(predict_class)
            number = np.where(predict_class == np.amax(predict_class))

            st.write("Number Predict:", str(np.amax(number)))
            st.write("Probability:", str(probability))


if __name__ == "__main__":
    main()

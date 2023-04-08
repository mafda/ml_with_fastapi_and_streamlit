"""Project: Prototyping a Machine Learning Application with Streamlit

Streamlit app integrated with predict_model.
"""

import cv2
import numpy as np
import streamlit as st
from streamlit_drawable_canvas import st_canvas

from model.predict import classify_digit


CANVAS_SIZE = 250


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
        if st.button("Predict"):
            img = cv2.cvtColor(canvas_image.image_data, cv2.COLOR_RGBA2RGB)

            probs = classify_digit(img)

            probability = np.amax(probs)

            st.write("Number Predict:", str(probs.argmax()))
            st.write(f"Probability: {probability * 100:.2f}%")
            st.write(f"Probabilities: {[f'{i:.3f}'for i in probs]}")

            canvas_image.image_data = None


if __name__ == "__main__":
    main()

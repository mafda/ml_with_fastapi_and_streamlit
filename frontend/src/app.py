"""
Project: Prototyping a Machine Learning Application with Streamlit.
Streamlit app integrated with a pretrained ViT model for image classification.
"""

import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests
import streamlit as st
from streamlit_drawable_canvas import st_canvas

CANVAS_SIZE = 250


def classify_digit(img):
    """
    Sends a request to the backend with the image data
    to perform a classification on the image.
    """
    # Retrieve the URL of the backend from the environment variables
    url_backend = os.environ["URL_BACKEND"]
    # Send a GET request to the backend with the image data as a JSON payload
    request = requests.get(url_backend, json={"image": img.tolist()})
    # Retrieve the predicted probabilities from the response
    answer = request.json()
    prob = answer["prob"]
    return np.array(prob)


def main():
    """
    Main Streamlit function
    Read an image and show a probability
    """

    # Set the title and caption for the Streamlit app
    st.set_page_config(page_title="Handwritten Digits Recognition")
    st.title("Handwritten Digits Recognition")
    st.caption(
        "App integrated with a pretrained ViT model for image classification"
    )

    # Initialize variables for the probability and the canvas image
    probs = None
    canvas_image = None

    # Create two columns for the Streamlit app layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(":1234: Draw a number here")

        # Create a canvas component for users to draw an image
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

        if canvas_image is not None and canvas_image.image_data is not None:

            if st.button("Classify!"):
                # Convert the canvas image to RGB format
                img = cv2.cvtColor(canvas_image.image_data, cv2.COLOR_RGBA2RGB)

                with st.spinner("Wait for it..."):
                    # Classify the digit and store the predicted probabilities
                    probs = classify_digit(img) * 100.0

    if probs is not None:
        with col2:
            st.subheader(":white_check_mark: Prediction")

            # Display the predicted digit and its probability
            st.metric(label="Predicted digit:", value=f"{probs.argmax()}")

            # Plot the predicted probabilities as a horizontal bar chart
            fig, ax = plt.subplots(figsize=(6, 4))
            class_names = list(range(10))
            ax.barh(class_names, probs, height=0.55, align="center")
            for i, (c, p) in enumerate(zip(class_names, probs)):
                ax.text(p + 2, i - 0.2, f"{p:.2f}%")
            ax.grid(axis="x")
            ax.set_xlabel("Probability")
            ax.set_xlim([0, 120])
            ax.set_xticks(range(0, 101, 20))
            ax.set_ylabel("Digit")
            ax.set_yticks(range(10))
            fig.tight_layout()
            st.pyplot(fig)


if __name__ == "__main__":
    main()

"""Project: Prototyping a Machine Learning Application with Streamlit

Streamlit app integrated with predict_model.
"""

import cv2
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_drawable_canvas import st_canvas

from model.predict import classify_digit

CANVAS_SIZE = 250


def main():
    """Main Streamlit function
    Read an image and show a probability
    """

    st.set_page_config(page_title="Handwritten Digits Recognition")
    st.title("Handwritten Digits Recognition")
    st.caption("Prototyping a ML Application")

    probs = None
    canvas_image = None

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(":1234: Draw a number here")

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

        if canvas_image is not None and canvas_image.image_data is not None:

            if st.button("Classify!"):
                img = cv2.cvtColor(canvas_image.image_data, cv2.COLOR_RGBA2RGB)

                with st.spinner("Wait for it..."):
                    probs = classify_digit(img) * 100.0

    if probs is not None:
        with col2:
            st.subheader(":white_check_mark: Prediction")

            st.metric(label="Predicted digit:", value=f"{probs.argmax()}")

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

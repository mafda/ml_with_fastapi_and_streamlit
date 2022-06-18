import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="mnist Prediction", page_icon=":1234:")

st.title("mnist Prediction")
st.write("Draw something here")

# Create a canvas component
canvas_result = st_canvas(
    fill_color="white",
    stroke_width=20,
    stroke_color="black",
    width=250,
    height=250,
    drawing_mode="freedraw",
    key="canvas",
    display_toolbar=True,
)

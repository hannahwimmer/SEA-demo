import base64
import streamlit as st


st.title("Hill Climbing Algorithm")

st.markdown("""
Further pages can be added as needed. You can use the same structure as the Random
Search page to document all of the other algorithms we'll implement.
""")

gif = open("docs/images/demo_image2.gif", "rb")
contents = gif.read()
data_url = base64.b64encode(contents).decode("utf-8")
gif.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}">',
    unsafe_allow_html=True,
)
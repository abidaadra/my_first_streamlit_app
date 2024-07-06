import streamlit as st

#title
st.title("🎈 My first app - This is the title.")
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
st.write("For more info about streamlit functions go to: https://github.com/abidaadra/my_first_streamlit_app")

#Write Text
st.write("Write")

#Header
st.header("Header") 

#Subheader
st.subheader("Subheader")

#Text
st.text("Text")

#Markdown
st.markdown("### Markdown")

#Success
st.success("Success")

#Information
st.info("Information")

#Warning
st.warning("Warning")

#Error
st.error("Error")

# Exception
exp = ZeroDivisionError("Exception when trying to divide by Zero")
st.exception(exp)

#Built-in Range function
st.write(range(10))

# Display Images

#Importing Image from pillow python library to open images
from PIL import Image
img = Image.open("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png")

#Display image using streamlit
#Width of an image
st.image(img, width=200)

#Checkbox and Title
if st.checkbox("Show/Hide"):
#Displays text when its true
	st.text("Displays text when its true")








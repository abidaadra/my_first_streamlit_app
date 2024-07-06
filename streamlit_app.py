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
img = Image.open("streamlit-logo.png")

#Display image using streamlit
#Width of an image
st.image(img, width=200)

#Checkbox and Title
if st.checkbox("Show/Hide"):
#Displays text when its true
	st.text("Displays text when its true")

#Radio Button
#First argument - title of radio button
#Second argument - options of radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

#Conditional Statement 
#Male if male is selected else print female
#Show the result using the success function
if (status == 'Male'):
	st.success("Male")
else:
	st.success("Female")

#Selection box
#1st argument takes the titleof the selectionbox
#2nd argument takes options
hobby = st.selectbox("Hobbies: ",['Dancing', 'Reading', 'Sports'])

#Print the selected hobby
st.write("Your hobby is: ", hobby)

# Create a simple button that does nothing
st.button("Click me which does nothing")

# Create a button, that when clicked, shows a text
if(st.button("About")):
	st.text("My name is Abida Adra")

#Text Input
#Save the input text in the variable 'name'
#1st argument shows the title of the text input box
#2nd argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")

#Display the name when the submit button is clicked
#.title() is used to get the input text string
if(st.button('Submit')):
	result = name.title()
	st.success(result)










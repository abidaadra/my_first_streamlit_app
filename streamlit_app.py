import streamlit as st

#title
st.title("🎈 My first app - This is the title.")
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
st.write("For more info about streamlit functions go to: https://github.com/abidaadra/my_firststreamlit_app")

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







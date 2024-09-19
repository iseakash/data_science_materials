import streamlit as st
import pandas as pd
import time as ts
from datetime import time

table = pd.DataFrame({"Col 1":[1,2,3,4,5,6], "col 2": [11,12,13,14,15,16]})

## Removing Streamlit Hamburger & Footer
st.markdown("""
<style>
.st-emotion-cache-czk5ss.e16jpq800
{
    visibility:hidden;            
}
</style>
""", unsafe_allow_html=True)

st.title("Hi! Welcome to Streamlit Web Page.")
st.header("Tell me how can I help you.")
st.subheader("You can always choose to be happy.")
st.text("Hope you are having a really good day. Let's navigate throught the page a bit.")

# To apply html text property on text.
st.markdown("> **Akash Gupta** welcomes you to this place.")
st.markdown("[Python Streamlit Full Course](https://www.youtube.com/playlist?list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW)")
st.markdown("---")
st.caption("mathematical_formula")
st.latex(r"\begin{bmatrix} a & b \\c & d \end{bmatrix}")
st.markdown("[Latex Formula](https://katex.org/docs/supported)")

json={"name":"akash, akshay, ajay", "age":"23,26,24"}
st.json(json)
code = """
def test(text):
    print(f"Hello World! {text}")
    return 0;
    """
st.code(code, language="python")

st.write("### It can implement multiple functions like markdown, header, code, latex, etc.")

# Matrix Function: To display different types of values.
st.metric(label="Wind Speed", value="120ms⁻¹", delta="1.4ms⁻¹")
st.table(table) # It is static
st.dataframe(table) # It allows us to sort the data

##  Media Widgets of Streamlit
st.image("image_test.png", caption="This is my image.", width=680)
st.audio("audio_test.m4a")
st.video("video_test.mp4")

## Basic Interactive Widgets of Streamlit
def change():
    print(st.session_state.checker)
state = st.checkbox("Tick me", value=True, on_change=change, key="checker")
if state==True:
    st.write("You are ticked me, Great!")
else:
    pass

# This radio button also support unique identifier, on_change, callback.
radio_btn = st.radio("In which country do you live?", options=("US","UK","IND"))
print(radio_btn)

def btn_click():
    print("Button Clicked.")
btn = st.button("Click Me!", on_click=btn_click)

# Select box allows us to select single object while multiple select box allows us to select multiple objects.
select = st.selectbox("What is your favourite car?", options=("BMW", "AUDI", "FERRARI"))
print(select)

multi_select = st.multiselect("What is your favourite tech brand?", options=("Microsoft", "Apple", "Amazon", "Google"))
st.write("You selected: ", multi_select)

## File Uploader Widget of Streamlit
st.title("Uploading Files")
st.markdown("---")
uploaded_image = st.file_uploader("Please upload an image", type=["png","jpg"],
                                  accept_multiple_files=True) # type = "mp4" for video.
if uploaded_image is not None:
    for img in uploaded_image:
        st.image(img, caption="This is the uploaded image.", width=580)

## Some More Interactive Widgets
# Slider also has callback properties using on_change feature.
slider_value = st.slider("This is a slider", min_value=50, max_value=75, value=61)
st.write(slider_value)

text = st.text_input("Enter your course title.", max_chars=100)
text_area = st.text_area("Course Description:")
date_input = st.date_input("Enter the date")
time_input = st.time_input("Enter time", value=time(0,0,0))
st.write(text, text_area, date_input, time_input)

# To complete the progress bar in certain time period
def converter(value):
    m,s,ms=value.split(":")
    return int(m)*60+int(s)+int(ms)/1000
# print(type(time_input))
if str(time_input) == "00:00:00":
    st.write("Please set the timer")
else:
    sec = converter(str(time_input))
    print(sec)
    perc = sec/100
    ## Timer App With Progress Bar
    progress_status = st.empty()
    bar = st.progress(0)
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i+1) + "%")
        ts.sleep(perc)
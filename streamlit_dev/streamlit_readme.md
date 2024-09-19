# Steps to go ahead with Streamlit:
## Environment Set Up:
1. Open ```VS Code``` and install the ```python``` extension.
2. Create a separate folder and create ```main.py``` file inside it.
3. Install the streamlit python package by running below command in the terminal: ```pip install streamlit```

## Basic Text Elements of Streamlit
1. Import Streamlit package as ```import streamlit as st``` and then try to run this file in the terminal using this command: ```streamlit run main.py```. This will create a Local URL for the app.
2. To define a title, use this: ```st.title("Message")```.
3. To define a header, use this: ```st.header("Message")```.
4. To define a subheader, use this: ```st.subheader("Message")```. 
5. To define a text, use this: ```st.text("Message")```.
6. To define a markdown, use this: ```st.markdown("> **Bold Message**, *Italic Message* ")```. [Refer here for different markdown elements.](https://www.markdownguide.org/cheat-sheet/)
7. To define a mathematical formula, use this: ```st.latex("Formula")```. [Refer here for Latex Formula syntax](https://katex.org/docs/supported)
8. To define a json body, use this: ```st.json("Enter json message")```.
9. To define a python code, use this: ```st.code("Enter code")```.
9. To define a any type of text, use this: ```st.write("Enter code or latex or json or header or markdown")```.

## Display Elements of Streamlit
1. Install the extension: ```Fast Unicode Math Characters```
2. To define a metric, use this: ```st.metric(label="Wind Speed", value="120ms⁻¹", delta="1.4ms⁻¹")```
3. To define value = "120ms⁻¹", use this with SPACE or ENTER: ```"120ms\^-1"```
4. To define a table which is static, use this: ```st.table(table)```
5. To define a dataframe which is more dynamic, use this: ```st.dataframe(table)```

##  Media Widgets of Streamlit
1. To define an image, use this: ```st.image("image file name")```
2. To define an audio, use this: ```st.audio("audio file name")```
3. To define a video, use this: ```st.video("video file name")```

## Removing Streamlit Hamburger & Footer
1. To remove or hide the hamsburger or footer, first INSPECTthe  classname of the hamsburgeror or footer
2. use this ("st-emotion-cache-czk5ss.e16jpq800": hamsburger class name):
```
st.markdown("""
<style>
.st-emotion-cache-czk5ss.e16jpq800
{
    visibility:hidden;            
}
</style>
""", unsafe_allow_html=True)
```

## Basic Interactive Widgets of Streamlit
1. To define a checkbox, use this: ```st.checkbox("label", value=True, on_change=function_name_to_be_called, key="checker")```. *Note* - It returns values like ```[True, False]```.
    - Use ```st.session_state.checker``` to fetch the checkbox state using *key*.
2. To define a radio, use this: ```st.radio("label", options=("US","UK","IND"))```. *Note* - It returns only one selected value.
3. To define a button, use this: ```st.button("label", on_click=function_name_to_be_called)```. *Note* - It calls the mentioned function.
4. To define a selectbox, use this: ```st.selectbox("label", options=("US","UK","IND"))```. *Note* - It returns only one selected value.
5. To define a multiselect, use this: ```st.multiselect("label", options=("US","UK","IND"))```. *Note* - It returns multiple selected values.

## File Uploader Widget of Streamlit
1. To define a file_uploader, use this: ```st.file_uploader("label", type=["png","jpg"], accept_multiple_files=True)```. *Note* - To upload single file, use ```accept_multiple_files=False``` & to upload a video file, use ```type="mp4"```.
2. To define a slider, use this: ```st.slider("label",  min_value=50, max_value=75, value=61)```.
    - Slider also has callback properties using on_change feature.
    - Slider is different from select_slider.
2. To define a text,
    - Use this: ```st.text_input("label",  max_chars=100)```
    - For more descriptive text , use this: ```st.text_area("label")```
    - *Note* : Use ```Enter``` to move to next line in ```text_area``` which is not possible in ```text_input```
3. To define a date_input, use this: ```st.date_input("label")```
4. To define a time_input, use this: ```st.time_input("label")```

## Timer App With Progress Bar
1. To define a progress bar, use this: ```st.progress("integer value")```
2. To empty the status, use this: ```st.empty()```
    - Use the combination of ```status = st.empty() & status.write(value)``` to display the progress bar value.
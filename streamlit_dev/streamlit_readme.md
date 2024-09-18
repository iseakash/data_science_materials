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
6. To define a markdown, use this: ```st.markdown("> Bold Message**, *Italic Message* ")```. [Refer here for different markdown elements.](https://www.markdownguide.org/cheat-sheet/)
7. To define a mathematical formula, use this: ```st.latex("Formula")```. [Refer here for Latex Formula syntax](https://katex.org/docs/supported)
8. To define a json body, use this: ```st.json("Enter json message")```.
9. To define a python code, use this: ```st.code("Enter code")```.

## Display Elements of Streamlit
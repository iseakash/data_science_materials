import streamlit as st
import pandas as pd

table = pd.DataFrame({"Col 1":[1,2,3,4,5,6], "col 2": [11,12,13,14,15,16]})

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
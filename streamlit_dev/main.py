import streamlit as st

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
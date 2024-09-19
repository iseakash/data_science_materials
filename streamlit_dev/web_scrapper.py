import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

# Reference to set streamlit page config: https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
# Reference for icons: https://www.webfx.com/tools/emoji-cheat-sheet/#
st.set_page_config(
    page_title="Webscrapper App",
    page_icon="📍", # 🧊
    layout="wide", # "centered"
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# st.image("https://images.unsplash.com/photo-1470058869958-2a77ade41c02")
st.markdown("<h1 style = 'align-text:center;'>Web Scrapper</h1>", unsafe_allow_html=True)
with st.form("Search"):
    keyword = st.text_input("Enter your keyword")
    search = st.form_submit_button("Search")

placeholder = st.empty()
if keyword: # Use keyword instead of search to avoid error
    page = requests.get(f"https://simple.wikipedia.org/wiki/{keyword}")
    print(page.status_code) # 200 means success
    # To fetch data by tags info
    soup = BeautifulSoup(page.content)
    rows = soup.find_all("figure",class_="mw-halign-right")
    print(len(rows))

    col1, col2 = placeholder.columns(2)
    for i,row in enumerate(rows): # [1:]
        img=row.find("img", class_="mw-file-element")
        # To fetch the image downloadable parent link
        anchor = row.find("a")
        print(anchor["href"])
        # Extracting the exact link or address
        list = img['srcset'].split(",")
        list = list[0].split(" ")[0]
        # print(len(list))
        # print(list)
        if i%2==0:
            col1.image("http:"+list)
            # To add multiple download buttons with unique keys to avoid error
            btn = col1.button("Download", key=str(i))
            if btn:
                print("Button pressed.")
                # way to open the web link in a new tab
                webbrowser.open_new_tab("https://simple.wikipedia.org"+anchor["href"])
        else:
            col2.image("http:"+list)
            # To add multiple download buttons with unique keys to avoid error
            btn = col2.button("Download", key=str(i))
            if btn:
                print("Button pressed.")
                # way to open the web link in a new tab
                webbrowser.open_new_tab("https://simple.wikipedia.org"+anchor["href"])
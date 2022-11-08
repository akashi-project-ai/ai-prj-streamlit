import streamlit as st

def local_css(file_name: str) -> None:
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def local_md(file_name: str) -> None:
    with open(file_name) as f:
        st.markdown(f"""{f.read()}""", unsafe_allow_html=True)
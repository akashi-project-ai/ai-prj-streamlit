import streamlit as st
from info import authors

st.header('EQUIPO')

st.markdown("[Blog](https://akashi-ai-blog.vercel.app/)")
st.markdown("Organización -> [Akashi-Ai](https://github.com/akashi-project-ai)")
st.markdown("HuggingFace -> [Akashi-Ai](https://huggingface.co/akashi-ai)")


made_fuhrerhlemon = authors.made_by_user("FuhrerhLemon", "https://github.com/Fuhrerh-Lemon")
made_hewelFo = authors.made_by_user("HewelFo", "https://github.com/HewelFo")
made_fuhrerhlemon.made_by()
made_fuhrerhlemon.info_dev()
made_hewelFo.info_dev()
st.markdown("")
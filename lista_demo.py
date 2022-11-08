import streamlit as st

from info import intro
from projects import ( 
    plotting_demo, 
    spiral_demo,
    mapping_demo,
    dataframe_demo,
)

class proyectos:
    names_to_funcs = {
        "—": intro.intro,
        "Plotting Demo": plotting_demo.plotting_demo,
        "Espiral Demo": spiral_demo.spiral_demo,
        "Mapping Demo": mapping_demo.mapping_demo,
        "DataFrame Demo": dataframe_demo.dataframe_demo,
    }
    def __lista__(self) -> None:
        funcs = self.names_to_funcs
        demo_name = st.sidebar.selectbox("Selecciona una demo", funcs.keys())
        funcs[demo_name]()
        
import streamlit as st

import lista_demo as llb
from components import my_component
from info import (
    config_page as cfp,
)

cfp.config_page()

# Cargando componentes en ts, html, css
my_component()

# Llamada a la clase con los proyectos(Carpeta projects)
page = llb.proyectos()
page.__lista__()
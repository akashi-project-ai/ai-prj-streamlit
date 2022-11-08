def intro() -> None:
    import streamlit as st

    st.image("https://stickerly.pstatic.net/sticker_pack/pco1gspFuK408WhSIdusEQ/1HX6ZX/19/68e74b79-61c7-4529-8351-f6f3b85f8741.png", caption=None, width=150, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.write("# Bienvenidos! 👋")
    st.sidebar.success("Seleccionar Proyectos.")

    st.markdown(
        """
        Akashi-AI Lab es una organización, para la investigación en el área de la inteligencia artificial.
        Aplicamos este conocimiento al desarrollo de software, como también a la computación cuántica... 
        **👈 Selecciona del lado izquierdo** Algunos de nuestros proyectos realizados!
        """
    )


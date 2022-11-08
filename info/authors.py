import streamlit as st

class made_by_user():
    authors_css = """
        style='
            display: block;
            margin-bottom: 0px;
            margin-top: 0px;
            padding-top: 0px;
            font-weight: 400;
            font-size:1.1em;
            color:#DBBD8A;
            filter: brightness(85%);
            text-align: center;
            text-decoration: none;
        '
    """
    def __init__(self, user, link_):
        self.user = user
        self.link = link_
    
    def made_by(self) -> None:
        authors_css = self.authors_css
        st.sidebar.header(f"\n\n\n")
        st.sidebar.markdown(f"\n\n\n")

        st.sidebar.markdown(
            '<p ' + authors_css + '>' + 'By </p>',
            unsafe_allow_html=True)
        st.sidebar.markdown(f"\n\n\n")

    def info_dev(self) -> None:
        authors_css = self.authors_css
        user = self.user
        link_ = self.link
        st.sidebar.markdown(
            '<a ' + authors_css + f' target="_blank" href={link_}>' + f'{user}</a>',
            unsafe_allow_html=True,
        )

    def contact_developers(self) -> None:
        authors_css = self.authors_css
        st.markdown("<p style=margin-top:190px;padding-bottom:-50px/>",
                    unsafe_allow_html=True, )
        st.markdown("<p " + authors_css + ">" + "We will appreciate any feedback from you, please contact:</p>",
                    unsafe_allow_html=True,)
        st.markdown(
            "<a " + authors_css + ' href="mailto:developers[at]sersitive.eu" target=_blank>' + "SERSitive Developers</a>",
            unsafe_allow_html=True,
        )
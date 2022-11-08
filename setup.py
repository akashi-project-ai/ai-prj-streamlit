import setuptools

setuptools.setup(
    name="components",
    version="0.0.1",
    author="Fuhrerh-Lemon, HewelFo",
    author_email="",
    description="Componentes personalizados, para nuestra web",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.8",
    install_requires=[
        "streamlit >= 1.13.0",
    ],
)
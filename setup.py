# NOTE TO MYSELF: DON'T IMPORT ANY MODULE FROM MY PACKAGE HERE !
import setuptools


with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()


NAME = "rustiql"
VERSION = "0.0.2"
AUTHOR = "Pyrustic Evangelist"
EMAIL = "pyrustic@protonmail.com"
DESCRIPTION = "Graphical SQL Editor for Pyrustic"
URL = "https://github.com/pyrustic/rustiql"


setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["pyrustic"],
    entry_points={
        "console_scripts": [
            "rustiql = rustiql.main:main",
        ],
    },
    python_requires='>=3.5',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

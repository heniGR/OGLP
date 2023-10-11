import datetime
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
# -- Project information -----------------------------------------------------

project = "LAB2301"
author = "© 2023 BAYCII Labs "
year = datetime.datetime.now().year

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "enum_tools.autoenum",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_logo = "_static/logo.png"

# -- Options for autodoc extension -------------------------------------------

autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "requests": ("https://docs.python-requests.org/en/latest/", None),
    # Add more intersphinx mappings as needed
}

# -- Other configuration options ---------------------------------------------

# Add any additional settings or customizations here

# -- Setup hook --------------------------------------------------------------


def setup(app):
    app.add_css_file("custom.css")


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# sys.path.insert(0, os.path.abspath('.'))

# -- End of configuration ----------------------------------------------------

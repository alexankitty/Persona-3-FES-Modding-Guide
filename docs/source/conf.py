# Configuration file for the Sphinx documentation builder.

# -- Project information
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Persona 3 FES Modding Guide'
copyright = '2023, Alexankitty'
author = 'Alexankitty'
html_favicon = 'favicon.png'
html_extra_path = [
    
]

release = '1.2.0'
version = '1.2.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "fix-secnum"
]

# -- OGP Configuration

ogp_site_url = "https://persona-3-fes-modding-guide.readthedocs.io/en/latest/"
ogp_image = "_images/how_to_mod.png"
ogp_use_first_image = True
ogp_social_cards = {
    "enable": False
}
ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary_large_image" />',
    '<meta name="theme-color" content="#40BAE0" />',
]


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_book_theme'

html_theme_options = {
    "repository_url": "https://github.com/alexankitty/Persona-3-FES-Modding-Guide",
    "use_repository_button": True,
    "show_navbar_depth": 2,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'How To Mod Persona 3 FES'
copyright = '2023, Alexankitty'
author = 'Alexankitty'
html_favicon = 'favicon.png'

release = '0.9'
version = '1.0.9'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "sphinxext.opengraph",
]

# -- OGP Configuration

ogp_site_url = "https://persona-3-fes-modding-guide.readthedocs.io/en/latest/"
ogp_image = "_images/how_to_mod.png"
ogp_use_first_image = True
ogp_type = "article"


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

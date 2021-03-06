# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

sys.path.append(os.path.abspath("./_ext"))

extensions = ['sphinx-cal']


# -- Sphinx Cal Config ----------
event_pattern = '_workshops/2021/*'

# -- Project information -----------------------------------------------------

project = 'Visualising your Visualisations'
copyright = '2021, Natalie Thurlby'
author = 'Natalie Thurlby'

# The full version, including alpha/beta/rc tags
release = 'v0.1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions += [
    'myst_nb',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    'github_url': 'https://github.com/Jean-Golding-Institute/grapho_workshop',
    'twitter_url': 'https://twitter.com/hashtag/VisualisingYourVisualisations',
    'search_bar_text': 'Search this site...',
    'search_bar_position': 'navbar',
    'show_prev_next': False,
}

html_sidebars = {
    'index': ['left.html'],
    'sign-up': ['left.html'],
    'upcoming-events': ['left.html'],
}

html_favicon = '_static/favicon.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


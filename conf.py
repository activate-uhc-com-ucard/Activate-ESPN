# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add directories to sys.path if needed
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate ESPN on Any Device'
copyright = '2025, ESPN'
author = 'ESPN'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "How to Activate ESPN on Any Device – Step-by-Step via espn.com/activate"

# Optional short title (e.g., in navigation bars)
html_short_title = "ESPN Activation Guide"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Choose a theme (uncomment one of the following if desired)
# html_theme = 'sphinx_rtd_theme'  # Recommended for clean docs look
# html_theme = 'alabaster'
# html_theme = 'furo'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Paths to templates and static files
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if you plan to include custom CSS or images

# Patterns to exclude when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

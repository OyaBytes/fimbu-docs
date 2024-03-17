# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Fimbu'
copyright = '2024, OyaBytes'
author = 'Edimedia Mutoke'
release = '0.2.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = ['sphinx_copybutton',]

templates_path = ['_templates']
exclude_patterns = []




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static', 'images']

github_url = 'https://github.com'
github_repo_org = 'OyaBytes'
github_repo_name = 'fimbu'
github_repo_slug = f'{github_repo_org}/{github_repo_name}'
github_repo_url = f'{github_url}/{github_repo_slug}'
github_sponsors_url = f'{github_url}/sponsors'
extlinks = {
    'user': (f'{github_sponsors_url}/%s', '@%s'),  # noqa: WPS323
    'pypi': ('https://pypi.org/project/%s', '%s'),  # noqa: WPS323
    'wiki': ('https://wikipedia.org/wiki/%s', '%s'),  # noqa: WPS323
}
extensions += ['sphinx.ext.extlinks']

html_theme_options = {
    "sidebar_hide_name": False,
    # "announcement": "<em>Important</em> announcement!",
    "light_css_variables": {
        "color-brand-primary": "#336790",  # "blue"
        "color-brand-content": "#336790",
        "font-stack": "Arial, sans-serif",
        "font-stack--monospace": "Courier, monospace",
    },
    "dark_css_variables": {
        "color-brand-primary": "#E5B62F",  # "yellow"
        "color-brand-content": "#E5B62F",
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/OyaBytes/fimbu",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}

# for press theme
# html_theme_options = {
#   "external_links": [
#       ("Github", "https://github.com/username/repo"),
#       ("Other", "https://bla.com")
#   ]
# }

# extensions += ['sphinx_favicon']
html_static_path = ['images']  # should contain the folder with icons

# Add support for nice Not Found 404 pages
extensions += ['notfound.extension']

pygments_style = "sphinx"
pygments_dark_style = "monokai"

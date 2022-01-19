from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Flask",
    install_requires=[
        "numpy >= 1.22",
        "pandas >= 1.3",
        "seaborn >= 0.11",
        "ipywidgets >= 7.6",
        "matplotlib >= 3.5"
    ],
)

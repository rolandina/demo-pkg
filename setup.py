from setuptools import setup

setup(
    name='demo-pkg',
    version='0.0.1',
    packages=['rolandviz'],
    install_requires=[
        'pandas',
        'numpy',
        'seaborn',
        'matplotlib',
        'typing'
    ],
    scripts = ['scripts/generate_plots']
    )

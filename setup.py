from setuptools import setup, find_packages

setup(
    name="agriculture_oackage",
    version="0.0",
    packages=find_packages(),
    description="Functions used in the agriculture project",
    author="Muhanad Abulhusn",
    author_email="muhanad.a.husn@gmail.com",
    url="https://github.com/Muhanad-husn/agriculture_package.git",
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "arabic_reshaper",
        "python-bidi"
    ],
)
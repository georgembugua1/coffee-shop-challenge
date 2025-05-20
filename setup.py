from setuptools import setup, find_packages

setup(
    name="coffee-shop-challenge",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest",
    ],
    python_requires=">=3.8",
)
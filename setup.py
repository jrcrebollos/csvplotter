from setuptools import setup, find_packages

setup(
    name="csvplotter",
    version="1.0.0",
    author="Your Name",
    author_email="johnraul.rebollos@email.com",
    description="csvplotter",
    long_description="Long description of your package",
    url="https://github.com/jrcrebollos/csvplotter",
    packages=find_packages(),
    install_requires=[
        "dependency1",
        "dependency2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
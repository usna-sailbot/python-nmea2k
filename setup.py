import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devangel77b", # Replace with your own username
    version="0.0.1",
    author="Dennis Evangelista",
    author_email="evangeli@usna.edu",
    description="nmea2k-like stuff for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/usna-sailbot/python-nmea2k",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

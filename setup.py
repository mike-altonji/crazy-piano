import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crazy-piano",
    version="0.0.1",
    author="Michael Altonji",
    author_email="mikealtonji@gmail.com",
    description="A package for exploring the fundamentals of how we define music.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mike-altonji/crazy-piano",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

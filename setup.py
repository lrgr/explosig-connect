import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="explosig-connect",
    version="0.0.1",
    author="Mark Keller",
    description="Send mutation signature data to ExploSig",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lrgr/explosig-connect",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'requests>=2.22.0',
        'pandas>=0.25.1',
    ],
)
"""spmf - setup.py"""
import setuptools

LONG_DESC = open('README.md').read()

setuptools.setup(
    name="spmf",
    version="1.2",
    author="Lorenz Leitner",
    author_email="lrnz.ltnr@gmail.com",
    description="Python Wrapper for SPMF",
    long_description_content_type="text/markdown",
    long_description=LONG_DESC,
    url="https://github.com/lolei/spmf-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    )

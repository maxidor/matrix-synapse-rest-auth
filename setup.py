import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matrix-synapse-rest-auth",
    version="0.1.2",
    author="Max Dor",
    author_email="git@max.dorius.io",
    description="Synapse REST Password provider",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kamax-matrix/matrix-synapse-rest-auth",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
)

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="adventuregame"
    version="0.0.1",
    author="Joseph Zimmerman",
    author_email="joeyzimmerman17@gmail.com",
    url="https://github.com/yourusername/yourproject",
    description="An text-based adventure game made in python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-translate-po-files',
    version='0.0.7',
    scripts=['django-translate-po'],
    author="Bart Machielsen",
    author_email="bartmachielsen@gmail.com",
    description="Automatically translate all Django PO files in the correct languages using google translate.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bartmachielsen/django-translate-po-files",
    packages=setuptools.find_packages(),
    install_requires=[
        "polib",
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
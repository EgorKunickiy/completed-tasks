import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="math_server",
    version="0.0.1",
    author="Egor",
    author_email="egorkunickiy12357@gmail.com",
    description=" math socket and http server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EgorKunickiy/completed-task",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "package"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

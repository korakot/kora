import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


requirements = [
    "ipython",
    "fastcore",
]


setuptools.setup(
    name="kora", 
    version="0.9.9",
    author="Korakot Chaovavanich",
    author_email="korakot@gmail.com",
    description="Convenient tools for Colab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/airesearch-in-th/kora",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
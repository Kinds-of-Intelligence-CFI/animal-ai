from setuptools import setup, find_packages

setup(
    name="animalai",
    version="3.0.1",
    description="Animal AI environment Python API",
    url="https://github.com/mdcrosby/animal-ai",
    author="Matt Crosby",
    author_email="matt@mdcrosby.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    zip_safe=False,
    install_requires=["mlagents==0.30.0"],
    python_requires=">=3.6",
)
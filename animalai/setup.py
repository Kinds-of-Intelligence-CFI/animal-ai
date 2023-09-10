from setuptools import setup, find_packages

setup(
    name="animalai",
    version="3.1.1",
    description="Animal AI environment Python API",
    url="https://github.com/Kinds-of-Intelligence-CFI/animal-ai",
    author="Matt Crosby; Ibrahim Alhas; K. Voudouris; W. Schellaert",
    author_email="ia424@cam.ac.uk",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    zip_safe=False,
    install_requires=["mlagents==0.30.0",
                      "numpy==1.21.2",
                      "scipy==1.7.2",
                      "pandas== 1.3.2"],
    python_requires=">=3.6",
)
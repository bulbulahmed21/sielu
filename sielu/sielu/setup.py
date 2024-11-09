from setuptools import setup, find_packages

setup(
    name="SiELU",
    version="0.1.0",
    author="Bulbul Ahmed, Anil Rai, Sarika Jaiswal, Mir Asif Iquebal, Dinesh Kumar",
    author_email="ahmedbulbul52@gmail.com", 
    description="A Python package for the sielu activation function developed by Ahmed et al., 2023 in https://doi.org/10.3389/fpls.2022.1008756",
    long_description=open("README.md").read(),
    long_description_content_type="We developed a novel activation function known as sielu, used in a LSTM deep neural network",
    url="https://github.com/yourusername/SiELU",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
    ],
)

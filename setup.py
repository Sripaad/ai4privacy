import setuptools

setuptools.setup(
    name="AI4P",
    version="1.0",
    author="Sripaad",
    author_email="sripaad751@gmail.com",
    description="AI 4 Privacy Models",
    long_description="A framework for detecting, highlighting and masking PII present in natural language text",
    url="https://github.com/Sripaad/ai4privacy.git",
    packages=setuptools.find_packages(),
    install_requires=['transformers', 'sentencepiece', 'tokenizers'],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: MIT",
        "Operating System :: OS Independent",
    ],
)
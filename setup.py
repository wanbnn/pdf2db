from setuptools import setup, find_packages

setup(
    name="pdf2db",
    version="0.1.0",
    author="wanbnn",
    author_email="wanbnn@outlook.com.br",
    description="Uma biblioteca para extrair e armazenar textos de PDFs de forma estruturada em um banco de dados.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wanbnn/pdf2db",
    packages=find_packages(),
    install_requires=[
        "PyPDF2",
        "sqlite3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
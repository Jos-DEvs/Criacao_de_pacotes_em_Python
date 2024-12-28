from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.0.1",
    author="Jos-DEvs",
    author_email="my_email",
    description="Testar a acessibilidade de um site",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jos-DEvs/Criacao_de_pacotes_em_Python.git"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.12.2',
)

from setuptools import setup, find_packages
from os import path

project_root = path.abspath(path.dirname(__file__))

with open(path.join(project_root, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="rmind",
    version="v0.1-alpha",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Phil Fernandez",
    author_email="philfernandez@protonmail.com",
    url="https://github.com/philFernandez/rmind",
    download_url="https://github.com/philFernandez/rmind/archive/refs/tags/v0.1-alpha.tar.gz",
    keywords=["v0.1-alpha", "pre-release"],
    classifiers=[],
    packages=find_packages(),
    license="MIT",
    include_package_data=True,
    install_requires=["Click", "rich", "sqlalchemy", "python-dotenv"],
    entry_points="""
        [console_scripts]
        rmind=remind.scripts.rmind:main
    """,
)
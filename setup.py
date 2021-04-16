from setuptools import setup, find_packages
from os import path

project_root = path.abspath(path.dirname(__file__))

with open(path.join(project_root, "PYPI_README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="rmind",
    version="0.1a1",
    description="A note taking cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Phil Fernandez",
    author_email="philfernandez@protonmail.com",
    url="https://github.com/philFernandez/rmind",
    keywords=["pre-release", "alpha", "note taking cli"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    license="MIT",
    include_package_data=True,
    install_requires=["Click", "rich==10.1.0", "sqlalchemy", "python-dotenv"],
    python_requires=">=3.7",
    entry_points="""
        [console_scripts]
        rmind=remind.scripts.rmind:main
    """,
)
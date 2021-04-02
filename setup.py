from setuptools import setup, find_packages

setup(
    name="rmind",
    version="0.0.1",
    author="Phil Fernandez",
    packages=find_packages(),
    license="MIT",
    include_package_data=True,
    install_requires=["Click", "rich", "sqlalchemy", "python-dotenv"],
    entry_points="""
        [console_scripts]
        rmind=remind.scripts.rmind:entry_point
    """,
)
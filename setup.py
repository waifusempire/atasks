from setuptools import setup, find_packages


setup(
    name="atasks",
    version="0.1.0",
    description="Simple async task manager",
    author="waifusempire",
    packages=find_packages(include=["atasks.py", "README.md"]),
)

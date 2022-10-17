from setuptools import find_packages
from setuptools import setup


setup(
    name="galaxy_express",
    packages=find_packages(),
    python_requires="~=3.8",
    include_package_data=True,
)

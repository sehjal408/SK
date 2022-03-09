from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mentor_mentee/__init__.py
from mentor_mentee import __version__ as version

setup(
	name="mentor_mentee",
	version=version,
	description="Mentor Mentee ",
	author="SK",
	author_email="sehjal021220@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

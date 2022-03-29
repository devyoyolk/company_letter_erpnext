from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in company_letter_erpnext/__init__.py
from company_letter_erpnext import __version__ as version

setup(
	name="company_letter_erpnext",
	version=version,
	description="This app creates frappe forms to generate company letters within the system.",
	author="Queens.lk",
	author_email="info@queens.lk",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

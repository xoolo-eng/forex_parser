import os
from setuptools import setup, find_packages


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_version() -> str:
    """Get current version.

    :return: Curent version.
    :rtype: str
    """
    path = os.path.join(BASE_DIR, "VERSION")
    with open(path, "r") as version_file:
        return version_file.read().strip()


def get_license_file() -> str:
    """Get path file with license text.

    :return: path
    :rtype: str
    """
    return os.path.join(BASE_DIR, "LICENSE")


def get_long_description() -> str:
    """Get README.md text.

    :return: README.md data.
    :rtype: str
    """
    path = os.path.join(BASE_DIR, "README.md")
    with open(path, "r") as readme_file:
        return readme_file.read().strip()


def get_requires() -> [str]:
    """Requires packages.
    If vesion is dev - add packages for development.

    :return: list with packages name.
    :rtype: [str]
    """
    path = os.path.join(BASE_DIR, "requirements.txt")
    with open(path, "r") as require_file:
        packages = [
            package.strip()
            for package in require_file.read().strip().split("\n")
        ]
    return packages


APP_PROPERTY = {
    "name": "fxp",
    "version": get_version(),
    "author": "TMS",
    "author_email": "dmitriy.amelchenko@outlook.com",
    "url": "",
    "packages": find_packages("src", exclude=["tests", "*test*"]),
    "package_dir": {"": "src"},
    "test_suite": "tests",
    "include_package_data": True,
    "license": get_license_file(),
    "description": "Forex parser",
    "long_description": get_long_description(),
    "long_description_content_type": "text/markdown",
    "install_requires": get_requires(),
    "python_requires": ">=3.8",
    "zip_safe": False,
    "entry_points": {"console_scripts": ["fxb = fxp.app"]},
    "classifiers": [
        "Development Status :: 5 Production/Stable"
    ],
}


setup(**APP_PROPERTY)
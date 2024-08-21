import pathlib
from setuptools import setup

import vpscraper.version as v

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

packages = [
    'vpscraper',
    'vpscraper.consts',
    'vpscraper.host',
    'vpscraper.host.shopee',
    'vpscraper.host.tokopedia',
]

setup(
    name=v.NAME,
    version=v.version(),
    packages=packages,
    project_urls={
        "Documentation": "https://vpscraper.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/vnpnh/vpscrape/issues",
    },
    url='https://github.com/vnpnh/vpscrape',
    license=v.LICENSE,
    keywords="Scraping Tools",
    author='vnpnh',
    author_email='vinsonpersie@gmail.com',
    description='All in One Scraping Tools',
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
    ],
    include_package_data=True,
    python_requires='>=3.10.0',
    install_requires=requirements,
)

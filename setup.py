from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Password manager'

classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
]

# Setting up
setup(
    name="pyfort",
    version=VERSION,
    author="Atharva Bhandvalkar",
    author_email="<atharv.bhandvalkar@gmail.com>",
    license='MIT',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['colorama', 'termcolor', 'cryptography'],
    keywords=['python'],
    entry_points={
        'console_scripts': [
            'fort = pyfort.pyfort:main',
        ],
    },
    classifiers=classifiers,
)
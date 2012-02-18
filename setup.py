import os
from setuptools import setup, find_packages

def get_long_description():
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
        return f.read()

setup(
    name = "pyhoe",
    version = __import__('pyhoe').get_version(),
    url = 'https://github.com/modocache/pyhoe',
    author = 'modocache',
    author_email = 'modocache@gmail.com',
    description = 'A project skeleton generator.',
    long_description = get_long_description(),
    keywords = "project setup skeleton",
    tests_require = ["nose"],
    install_requires = [],
    packages = find_packages(),
    include_package_data = True,
    classifiers = [
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
        'Development Status :: 2 - Pre-Alpha',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Debuggers',
    ],
    entry_points = {
        'console_scripts': [
            'pyhoe = pyhoe.main.command:main',
        ]
    }
)

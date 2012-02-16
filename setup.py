import os
from setuptools import setup, find_packages

#included_scripts = []
#bin_dir = "bin"
#for dirpath, dirnames, filenames in os.walk(bin_dir):
#    (included_scripts.append(os.join(bin_dir, f)) for f in filenames)

print __file__, find_packages()

setup(
    # The name of the package. Required. (<200 chars)
    name = "pyhoe",
    # It is recommended that versions take the form
    # major.minor[.patch[.sub]]. Required.
    version = __import__('pyhoe').get_version(),
    # Home page for the package. Required.
    url = 'https://github.com/modocache/pyhoe',
    # Author is required. Alternatively, a maintainer may be
    # specified using the 'maintainer' and 'maintainer_email'
    # parameters. (<200 chars)
    author = 'modocache',
    author_email = 'modocache@gmail.com',
    # A short description of the project (<200 chars)
    description = "A project skeleton generator.",
    keywords = "project setup skeleton",
    # Location where the package may be downloaded.
    # 'download_url': 'DOWNLOAD_URL',
    # Packages and data files included in the project.
    tests_require = ["nose"],
    install_requires = ["nose"], # FIXME - Add Sphinx?
    packages = find_packages(),
    include_package_data = True,
    # 'data_files': data_files,
    # A list of strings used by PyPI to classify the project.
    classifiers = [],
    # Scripts are files containing Python source code, intended to be
    # started from the command line. A list of paths to the files,
    # using the conventional Unix path separator `/`.
    entry_points = {
        'console_scripts': [
            'pyhoe = pyhoe.main.command:main',
        ]
    }
)

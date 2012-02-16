import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Grab list of packages and data files.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != "":
    os.chdir(root_dir)
project_dir = 'PROJECT_NAME'
for dirpath, dirnames, filenames in os.walk(project_dir):
    # Ignore dirnames that start with "."
    for i, dirname in enumerate(dirnames):
        if dirname.startswith("."): del dirnames[i]
    if "__init__.py" in filenames:
        packages.append(".".join((dirpath).split(os.sep)))
    elif filenames:
        data_files.append(
            [dirpath, [os.path.join(dirpath, f) for f in filenames]]
        )

# Grab list of scripts in bin directory.
scripts = []
bin_dir = "bin"
for dirpath, dirnames, filenames in os.walk(bin_dir):
    scripts.append([f for f in filenames if f.endswith(".py")])

config = {
    # The name of the package. Required. (<200 chars)
    'name': 'PROJECT_NAME',
    # It is recommended that versions take the form
    # major.minor[.patch[.sub]]. Required.
    'version': __import__('PROJECT_NAME').get_version,
    # Home page for the package. Required.
    'url': 'https://github.com/AUTHOR_NAME/PROJECT_NAME',
    # Author is required. Alternatively, a maintainer may be
    # specified using the 'maintainer' and 'maintainer_email'
    # parameters. (<200 chars)
    'author': 'AUTHOR_NAME',
    'author_email': 'AUTHOR_EMAIL',
    # A short description of the project (<200 chars)
    # 'description': 'DESCRIPTION',
    # Location where the package may be downloaded.
    # 'download_url': 'DOWNLOAD_URL',
    # Packages and data files included in the project.
    'packages': packages,
    'data_files': data_files,
    # A list of strings used by PyPI to classify the project.
    'classifiers': [],
    'install_requires': ['nose'],
    # Scripts are files containing Python source code, intended to be
    # started from the command line. A list of paths to the files,
    # using the conventional Unix path separator `/`.
    'scripts': scripts,
}

setup(**config)

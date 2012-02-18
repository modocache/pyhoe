from setuptools import setup, find_packages

setup(
    name = "pyhoe",
    version = __import__('pyhoe').get_version(),
    url = 'https://github.com/modocache/pyhoe',
    author = 'modocache',
    author_email = 'modocache@gmail.com',
    description = 'A project skeleton generator.',
    long_description = \
    """
    Like Ruby's `Hoe <https://github.com/seattlerb/hoe>`_, pyhoe aims
    to help developers by providing a basic project skeleton.
    Projects created with pyhoe's default settings include the following:

     * A basic directory structure with templates for README, LICENSE,
       `setup.py <http://docs.python.org/distutils/setupscript.html>`_,
       `.gitignore <http://help.github.com/ignore-files/>`_, and other
       ubiquitous project files.
     * A `virtualenv <http://pypi.python.org/pypi/virtualenv>`_ for the new
       project.
     * Automated tests using `Nosy <https://bitbucket.org/douglatornell/nosy>`_,
       which is built upon `nose <http://readthedocs.org/docs/nose/en/latest/>`_.
       Mac OSX users will find a nose plugin called `Sneazr <https://github.com/jessemiller/Sneazr>`_
       to display Growl notifications on tests results.
     * `Tox <http://tox.readthedocs.org/en/latest/index.html>`_, for testing
       across multiple Python environments.
    """,
    keywords = "project setup skeleton",
    tests_require = ["nose"],
    install_requires = [],
    packages = find_packages(),
    include_package_data = True,
    classifiers = [
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
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

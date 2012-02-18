# pyhoe

Like Ruby's [Hoe](https://github.com/seattlerb/hoe), PyHoe aims
to help developers by providing a basic project skeleton and 
convenient make commands. Projects created with pyhoe's default
settings include the following:

- A basic directory structure with templates for README, LICENSE,
  [setup.py](http://docs.python.org/distutils/setupscript.html),
  [.gitignore](http://help.github.com/ignore-files/), and other
  ubiquitous project files.
- A [virtualenv](http://pypi.python.org/pypi/virtualenv) for the new
  project.
- Automated tests using [Nosy](https://bitbucket.org/douglatornell/nosy),
  which is built upon [nose](http://readthedocs.org/docs/nose/en/latest/).
  Mac OSX users will find a nose plugin called [Sneazr](https://github.com/jessemiller/Sneazr)
  to display Growl notifications on tests results.
- [Tox](http://tox.readthedocs.org/en/latest/index.html), for testing
  across multiple Python environments.
- [Sphinx](http://sphinx.pocoo.org/) for project documentation.
- A [fabfile](http://docs.fabfile.org/en/1.3.4/index.html) for
  performing common tasks such as building documentation and project
  packaging.

# Requirements & Dependencies

Python 2.7 or superior (that includes 3.0+) is required to use pyhoe for now,
although I am considering supporting Python 2.6 as well.

# Usage

## Starting a New Project

    $ pyhoe sow my_new_project
    Create a virtualenv (my_new_project)? [Y/n] > Y
    ... mkvirtualenv my_new_project
    ... (my_new_project) pip install nosy sneazr tox Sphinx Fabric
    
    ... created my_new_project/
    ... created my_new_project/README.md
    ... created my_new_project/.gitignore
    ... created my_new_project/__init__.py
    ... created my_new_project/setup.py
    ... created my_new_project/bin
    ... created my_new_project/tests/
    ... created my_new_project/tests/__init__.py
    ... created my_new_project/tests/my_new_project_tests.py
    ... created my_new_project/fabfile/
    ... created my_new_project/fabfile/__init__.py
    ... created my_new_project/fabfile/doc.py
    ... created my_new_project/fabfile/git.py
    ... created my_new_project/fabfile/project.py
    ... created my_new_project/fabfile/test.py
    
    ... initialized git repository.
    
    Would you like to create documentation for this project? [Y/n] > Y
    ... running sphinx-quickstart
    ... building Sphinx HTML.
    
    Happy coding!
    $

## Getting More Information

    $ pyhoe explain tox

# Options

- Fans of behavior-driven development can pass pyhoe the `-c` or 
  `--cucumber` flag to include basic templates for using [freshen](https://github.com/rlisagor/freshen),
  a Python clone of the Cucumber BDD framework.
- Too many decisions? Just use the `-y` or `--yes-to-all` flag to go
  with all the recommended settings.

- - -

# Fabfile Usage

Coming soon!

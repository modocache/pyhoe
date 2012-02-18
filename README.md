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

# Requirements & Dependencies

Python 2.7 or superior (that includes 3.0+) is required to use pyhoe for now,
although I am considering supporting Python 2.6 as well.

# Usage

## Starting a New Project

    $ pyhoe sow smoothjazz
    Create virtualenv smoothjazz for this project? [Y/n]: Y
    Install recommended packages to virtualenv smoothjazz? [Y/n]: Y
    Create documentation for smoothjazz? [Y/n]: Y
    Initialize git repository for this project? [Y/n]: Y
    ...created smoothjazz
    ...created smoothjazz/tests
    ...created smoothjazz/smoothjazz
    ...created smoothjazz/.gitignore
    ...created smoothjazz/CHANGELOG.md
    ...created smoothjazz/MANIFEST.in
    ...created smoothjazz/MIT-LICENSE
    ...created smoothjazz/README.md
    ...created smoothjazz/setup.cfg
    ...created smoothjazz/setup.py
    ...created smoothjazz/tox.ini
    ...created smoothjazz/tests
    ...created smoothjazz/tests/__init__.py
    ...created smoothjazz/tests/smoothjazz_tests.py
    ...created smoothjazz/smoothjazz
    ...created smoothjazz/smoothjazz/__init__.py
    ...created smoothjazz/smoothjazz/main.py

    New python executable in zzz/bin/python
    [creates virtualenv]
    [installs packages]
   
    Initialized empty Git repository in zoobar/.git/

    [runs sphinx-quickstart]
    
    Happy coding!
    $

# Options

- Too many decisions? Just use the `-y` or `--yes-to-all` flag to go
  with all the recommended settings.

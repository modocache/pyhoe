pyhoe - Top
===========

:Authors:
    modocache <modocache@gmail.com>
:Version: |release|

Overview
********

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


Quickstart
**********

To create a new project directory with the default skeleton,
install pyhoe and run the ``sow`` command.

.. code-block:: bash

        $ pip install pyhoe
        $ pyhoe sow my_new_project


See :ref:`commands` for details on all commands available).


Report a Bug
************

Feel free to open an issue on `Github <https://github.com/modocache/pyhoe>`_
if you notice something wrong with the program or this documentation,
or if you think of a feature for pyhoe you think might be worth adding.
I'll try to get back to you as quickly as possible.

Contributions to the project are also very welcome! `Fork me! <https://github.com/modocache/pyhoe>`_


Documentation Contents
**********************

.. toctree::
   :maxdepth: 2
   :glob:

   installation
   commands


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`


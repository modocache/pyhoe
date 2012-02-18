Commands
========

sow
***

``sow`` initializes a new project with the specified name.
It can also take any number of extra arguments. Type ``pyhoe
sow --help`` at the command line for a full list of all the arguments
``sow`` accepts.

.. code-block:: bash

    $ pyhoe sow my_new_project --python python3.2 --template package

Some details on particular arguments follow.

.. data:: project_name

    The name of the project to create. A new directory and virtualenv
    will be created using this name.

.. data:: -t, --template

    The template to use for your project. Current options are:
     * package - A Python package including tests, a README, and
       a basic directory structure.

.. data:: -p, --python

    The Python version for the virtualenv pyhoe creates.

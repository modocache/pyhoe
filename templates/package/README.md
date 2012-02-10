# PyHoe

Like Ruby's [Hoe](https://github.com/seattlerb/hoe), PyHoe aims
to help developers by providing a basic project skeleton and 
convenient make commands.

# Usage

Assuming `<PROJECT_NAME>` is the project name of your choice:

    $ git clone https://github.com/modocache/PyHoe.git
    $ rm PyHoe/.git
    $ mv PyHoe <PROJECT_NAME> && cd <PROJECT_NAME>
    $ fab init

This will create Sphinx documentation and provide you with a
basic project structure.

# Plans for the future

- Be more like [Hoe](https://github.com/seattlerb/hoe).
- Windows support.
- More commands.

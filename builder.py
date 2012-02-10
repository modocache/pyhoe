#!/usr/bin/env python

import os
from os.path import join
import shutil

TEMPLATE_DIR = "templates"

class ProjectBuilder(object):
    """
    """
    def __init__(self):
        """docstring for __init__"""
        pass

    def build(
        self,
        project_name,
        template,
        python_exe=None,
        skip_confirmation=False
    ):
        print "Building project: %s" % project_name
        if python_exe: print "Using %s" % python_exe
        print "Skip confirmation: %s" % str(skip_confirmation)
        shutil.copytree(join(TEMPLATE_DIR, template), project_name)

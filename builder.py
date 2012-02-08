#!/usr/bin/env python

import os
from os.path import join
import shutil

TEMPLATE_DIR = "template"

class ProjectBuilder(object):
    """
    """
    def __init__(self):
        """docstring for __init__"""
        pass

    def build(self, project_name, python_exe=None, skip_confirmation=False):
        print "Building project: %s" % project_name
        if python_exe: print "Using %s" % python_exe
        print "Skip confirmation: %s" % str(skip_confirmation)
        shutil.copytree(TEMPLATE_DIR, project_name)

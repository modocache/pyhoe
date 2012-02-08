#!/usr/bin/env python

class Delegator(object):
    """
    Performs commands based on arguments provided.
    """
    def __init__(self, args):
        self.args = args
        for arg in self.args:
            print arg
        #    func = getattr(self, arg)

from fabric.api import task
import doc, git, project, test

@task
def init(name=None):
    """docstring for init"""
    project.init(name)
    doc.build()
    doc.view()

@task
def prepare_package():
    """docstring for prepare_package"""
    test.test()
    doc.build()
    git.commit()

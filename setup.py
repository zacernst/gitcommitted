#!/usr/bin/env python

import atexit
from setuptools import setup, find_packages
from setuptools.command.install import install
import glob


HOOK = """#!/bin/sh
# Redirect output to stderr.
exec 1>&2
# enable user input
exec < /dev/tty
commit_handler $1 $2 $3
"""


def _post_install():
    hi()


class new_install(install):
    def __init__(self, *args, **kwargs):
        super(new_install, self).__init__(*args, **kwargs)
        atexit.register(_post_install)

    # def run(self):
    #     install.run(self)
    #     path_list = []
    #     for path in glob.glob('.git/hooks'):
    #         path_list.append(path)
    #     assert len(path_list) == 1, 'Could not find path for hook'
    #     with open(path_list[0] + '/prepare-commit-msg', 'w') as f:
    #         f.write(HOOK + '\n')

def hi():
    path_list = []
    for path in glob.glob('.git/hooks'):
        path_list.append(path)
    assert len(path_list) == 1, 'Could not find path for hook'
    with open(path_list[0] + '/prepare-commit-msg', 'w') as f:
        f.write(HOOK + '\n')
        print('hi there you')

setup(name='gitcommitted',
      cmdclass={'install': new_install},
      version='0.1',
      description='Automate your git commit messages',
      author='Zachary Ernst',
      author_email='zac.ernst@gmail.com',
      # package_dir={"": "src"},  # Optionalpackages
      packages=find_packages(where="src"),  # Requiredscripts
      scripts=['bin/commit_handler'],
     )


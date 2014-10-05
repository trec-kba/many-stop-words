#!/usr/bin/env python

import os
import sys
import fnmatch
import subprocess

## prepare to run PyTest as a command
from distutils.core import Command
from distutils.dir_util import remove_tree

from setuptools import setup, find_packages

from version import get_git_version
VERSION, SOURCE_LABEL = get_git_version()
PROJECT = 'many-stop-words'
URL = 'http://diffeo.com'
AUTHOR = 'Diffeo, Inc.'
AUTHOR_EMAIL = 'support@diffeo.com'
DESC = 'stop words lists in many languages'

def read_file(file_name):
    file_path = os.path.join(
        os.path.dirname(__file__),
        file_name
        )
    return open(file_path).read()

def recursive_glob(treeroot, pattern):
    results = []
    for base, dirs, files in os.walk(treeroot):
        goodfiles = fnmatch.filter(files, pattern)
        results.extend(os.path.join(base, f) for f in goodfiles)
    return results

def recursive_glob_with_tree(treeroot, pattern):
    results = []
    for base, dirs, files in os.walk(treeroot):
        goodfiles = fnmatch.filter(files, pattern)
        one_dir_results = []
        for f in goodfiles:
            one_dir_results.append(os.path.join(base, f))
        results.append((base, one_dir_results))
    return results

def _myinstall(pkgspec):
    subprocess.check_call(['pip', 'install', pkgspec])

class PyTest(Command):
    '''run py.test'''

    description = 'runs py.test to execute all tests'

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if self.distribution.install_requires:
            for ir in self.distribution.install_requires:
                _myinstall(ir)
        if self.distribution.tests_require:
            for ir in self.distribution.tests_require:
                _myinstall(ir)

        errno = subprocess.call(['py.test', '-n', '3', '-s', 'many_stop_words/tests', '--runslow', '--runperf'])
        raise SystemExit(errno)

setup(
    name=PROJECT,
    version=VERSION,
    description=DESC,
    long_description=read_file('README.md'),
    author=AUTHOR,
    license='MIT/X11 license http://opensource.org/licenses/MIT',
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(),
    cmdclass={
        'test': PyTest,
    },
    # We can select proper classifiers later
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',  ## MIT/X11 license http://opensource.org/licenses/MIT
    ],
    include_package_data = True,
)

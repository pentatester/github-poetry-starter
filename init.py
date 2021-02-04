#!/usr/bin/env python
"""This script will setup"""

import argparse
import os
import shutil
import sys


BASE_DIR = os.getcwd()

NAME = 'github-poetry-starter'
SNAME = 'github_poetry_starter'
VERSION = "0.4.0"
DESCRIPTION = "GitHub Actions starter for python with python-poetry"
AUTHOR = 'hexatester'
EMAIL = 'hexatester@protonmail.com'

PDIR = os.path.join(BASE_DIR, 'github_poetry_starter')
TFILE = os.path.join(BASE_DIR, 'tests', 'test_github_poetry_starter.py')


def snake_case(text):
    return text.lower().replace(' ', '_')


def kebab_case(text):
    return text.lower().replace(' ', '-')


def remove(path):
    """param <path> could either be relative or absolute."""
    # thanks https://stackoverflow.com/a/41789397
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        raise ValueError("file {} is not a file or dir.".format(path))


def rewrite(filepath, changes):
    text = ''
    with open(filepath) as f:
        text = f.read()

    for change in changes:
        text = text.replace(*change)

    with open(filepath, "w") as f:
        f.write(text)

def main():
    parser = argparse.ArgumentParser(description='Setup Poetry Starter.')

    parser.add_argument('--name', dest='name', help='Project name', required=True)
    parser.add_argument('--version', dest='version', help='Project version', default="0.1.0")
    parser.add_argument('--description', dest='description', help='Project description', required=True)
    parser.add_argument('--author', dest='author', help='Author name / username', required=True)
    parser.add_argument('--author-email', dest='email', help='Author-email', required=True)

    parser.add_argument('--module', dest='module', action='store_true')
    parser.add_argument('--no-module', dest='module', action='store_false')
    parser.set_defaults(module=True)


    args = parser.parse_args()

    if args.module:
        NS_NAME = snake_case(args.name)
        NDIR = os.path.join(BASE_DIR, NS_NAME)
        TNFILE = os.path.join(BASE_DIR, 'tests', f'test_{NS_NAME}.py')

        if os.path.isdir(PDIR):
            os.rename(PDIR, NDIR)
        if os.path.isfile(TFILE):
            os.rename(TFILE, TNFILE)
        rewrite(TNFILE, [(SNAME, NS_NAME)])
    else:
        remove(PDIR)
        remove(TFILE)
        with open('setup.py', 'w+') as f:
            f.write("#!/usr/bin/env python\n")

    REPLACE_PYPROJECT = [
        (NAME, kebab_case(args.name)),
        (VERSION, args.version),
        (DESCRIPTION, args.description),
        (AUTHOR, args.author),
        (EMAIL, args.email),
    ]

    rewrite('pyproject.toml', REPLACE_PYPROJECT)


    REPLACE_SETUP = [
        (", 'init.py'", '')
    ]

    rewrite('setup.py', REPLACE_SETUP)


    print("Please delete init.py file")

if __name__ == "__main__":
    sys.exit(main())
